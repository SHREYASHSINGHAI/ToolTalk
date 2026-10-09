# ToolTalk 🌤️

ToolTalk is a lightweight, single-file Python CLI application demonstrating zero-shot native tool calling (function calling) using the **Groq SDK** and **OpenWeatherMap API**. 

The app leverages low-latency inference on high-performance open-weights models (such as `openai/gpt-oss-120b` or `llama-3.3-70b-versatile`) to dynamically extract user intent, execute real-time local tools, and synthesize structured, human-readable answers.

---

## 🚀 Features

- **Native Tool Calling:** Uses standard JSON schema tool definitions rather than custom string-parsing regex.
- **Two-Pass Execution Loop:** 
  1. *Pass 1:* The model evaluates the query and generates structured tool parameters.
  2. *Pass 2:* The script executes local Python code and passes execution context back to the model for final response synthesis.
- **Fail-Safe Weather Lookups:** Wraps OpenWeatherMap API queries in error-handled routines to ensure model gracefully answers even if an invalid city or API limit is encountered.
- **Zero-Dependency Core Design:** Operates inside a single, clean executable file (`weather.py`).

---

## 🛠️ Prerequisites & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/SHREYASHSINGHAI/ToolTalk.git](https://github.com/SHREYASHSINGHAI/ToolTalk.git)
cd ToolTalk
