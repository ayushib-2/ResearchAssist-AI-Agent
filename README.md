# 🧠 ResearchAssist-AI-Agent

**ResearchAssist-AI-Agent** is an AI-powered research assistant that takes a natural language query and autonomously gathers information using web search and Wikipedia, summarizes the findings, and saves a neatly formatted report to a text file.

Built using:
- **LangChain Agents**
- **OpenAI (GPT-4o-mini)**
- **Anthropic Claude (optional)**
- **DuckDuckGo Search**
- **Wikipedia API**

---

## 🔍 What It Does

- Accepts a user query (e.g. *“Tell me about artificial intelligence”*)
- Uses LLMs and integrated tools (search, Wikipedia)
- Gathers relevant information autonomously
- Summarizes the results using a structured Pydantic format
- Saves a clean, readable research report to `research_output.txt`

---

## 📂 Project Structure

ResearchAssist-AI-Agent/
│
├── main.py # Entry point – runs the agent
├── tools.py # Custom tools (search, wiki, save-to-file)
├── requirements.txt # All required Python dependencies
├── .gitignore # Ignored files (e.g. .venv, .env, output files)
├── research_output.txt # Auto-generated file with saved summaries


---

## 🚀 Setup & Installation

### 1. Clone the Repo

git clone https://github.com/yourusername/ResearchAssist-AI-Agent.git
cd ResearchAssist-AI-Agent



### 2. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate


### 3. Install Dependencies
pip install -r requirements.txt


### 4. Set Up API Keys
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key   # optional


## How to run the agent
python main.py

Then enter a natural language query like:
What can I help you search?
> History of quantum computing