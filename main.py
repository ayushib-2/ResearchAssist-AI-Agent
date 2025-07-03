from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor
from tools import search_tool, wiki_tool, save_tool


load_dotenv()

class ResearchResponse(BaseModel): # specify all of the fields wanted as output from the LLM call
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]
    
llm = ChatOpenAI(model="gpt-4o-mini")
parser = PydanticOutputParser(pydantic_object=ResearchResponse) # take output of LLM and parse it into a Pydantic model


# set up a prompt

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
                You are a research assistant that will help generate a research paper. 
                Answer the user query and use necessary tools. 
                Wrap the output in this format and provide no other text\n{format_instructions}""",
        ),
        ("placeholder", "{chat_history}"), # will be filled in automatically by agent executor
        ("human", "{query}"), 
        ("placeholder", "{agent_scratchpad}"),  # will be filled in automatically by agent executor                                 
    ]
).partial(format_instructions=parser.get_format_instructions())   

# parser is converted to a string which can be given to the LLM as a prompt in format_instructions
tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, max_iterations=3) # verbose follows thought process of agent
query=input("What can I help you search?\n")
raw_response = agent_executor.invoke({"query": query})

try:
    structured_response = parser.parse(raw_response.get("output")) # parse the output into a Pydantic model
    print(structured_response)
except Exception as e:
    print("Error parsing response:", e, "Raw Response - ", raw_response)