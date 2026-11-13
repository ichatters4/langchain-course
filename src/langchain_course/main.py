from typing import Dict, Any
from unittest import result

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
# from tavily import TavilyClient
from langchain_tavily import TavilySearch


from dotenv import load_dotenv

# @tool
# def search(query: str) -> Dict[str, Any]:
#     """
#     Tool that searches over the internet
#     Args:
#         query (str): search query
#     Returns:
#         str: search result
#     """
#     tavily = TavilyClient()
#     print(f"Searching for {query}")
#     return tavily.search(query=query)



def main() -> None:
    print("Hello from langchain-course!")
    llm = ChatOpenAI(model="gpt-5")

    # tools = [search]
    tools = [TavilySearch()]
    agent = create_agent(model=llm, tools=tools)
    weather = agent.invoke({"messages": HumanMessage(content="What is the weather in Bangalore?")})
    print(weather)

if __name__ == "__main__":
    load_dotenv()
    main()