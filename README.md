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

## 🚀 Setup & Installation

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/ResearchAssist-AI-Agent.git
cd ResearchAssist-AI-Agent
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys

Create a `.env` file in the root of the project and add your keys:

```env
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key  # optional
```

---

## ▶️ How to Run the Agent

```bash
python main.py
```

Then enter a natural language query like:

```text
What can I help you search?
> History of quantum computing
```

---

## 🌟 Example Output

```
--- Research Output ---
Timestamp: 2025-07-03 11:55:14

Topic: Artificial Intelligence

Summary:
Artificial intelligence (AI) is the capability of computational systems to perform tasks associated with human intelligence...

Sources:
- Wikipedia - Artificial Intelligence
- Recent advancements in Artificial Intelligence

Tools Used: wikipedia, search
--- End of Research Output ---
```

---