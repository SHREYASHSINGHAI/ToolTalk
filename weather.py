import json, os, requests
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq()

MODEL = "openai/gpt-oss-120b"

def get_weather(location, units="metric"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={os.getenv('OPENWEATHER_API_KEY')}&units={units}"
    try:
        res = requests.get(url, timeout=5).json()
        if res.get("cod") != 200:
            return json.dumps({"error": res.get("message", "City not found")})
        unit = "°C" if units == "metric" else "°F"
        return json.dumps({"city": res["name"], "temp": f"{res['main']['temp']}{unit}", "sky": res["weather"][0]["description"]})
    except Exception as e:
        return json.dumps({"error": str(e)})

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather for a city.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"},
                "units": {"type": "string", "enum": ["metric", "imperial"]}
            },
            "required": ["location"]
        }
    }
}]

def ask(prompt):
    messages = [{"role": "user", "content": prompt}]
    res = client.chat.completions.create(model=MODEL, messages=messages, tools=tools)
    msg = res.choices[0].message

    if msg.tool_calls:
        messages.append(msg)
        call = msg.tool_calls[0]
        args = json.loads(call.function.arguments)
        messages.append({"role": "tool", "tool_call_id": call.id, "name": call.function.name, "content": get_weather(**args)})
        msg = client.chat.completions.create(model=MODEL, messages=messages).choices[0].message

    print(f"\nAssistant: {msg.content}")

if __name__ == "__main__":
    print("==================================================")
    print(" Hello! What city weather would you like to know?")
    print("==================================================")
    while True:
        prompt = input("\nYou: ").strip()
        if prompt.lower() in ["exit", "quit"]:
            break
        if prompt:
            ask(prompt)