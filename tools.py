# looking up wikipedia
# going to duckduckgo to search for something
# custom tool to write ourselves

from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime



def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text= f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n--- End of Research Output ---\n"
    
    with open(filename, "a", encoding="utf-8") as file:
        file.write(formatted_text) 
    
    return f"Data successfully saved to {filename}"

# custom tool
save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves the research output to a text file with a timestamp.",
)

# search tool to crawl Duck Duck Go
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name = "search", # name cannot have any spaces
    func=search.run,
    description="Search the web for information",
)

# Wikipedia tool to look up information
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=1000)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)





