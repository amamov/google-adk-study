from typing import Type
from firecrawl import Firecrawl
from pydantic import BaseModel, Field
from env import FIRECRAWL_API_KEY


def web_search_tool(query: str):
    """
    Arg:
    query (str): The search query to look for.

    Description:
    Searches the web for information based on a query and returns relevant results with titles, URLs, and content snippets.

    Return:

    """
    firecrawl = Firecrawl(api_key=FIRECRAWL_API_KEY)

    response = firecrawl.search(query, limit=5, integration="crewai")

    if not response:
        return f"No search results found for query: {query}"

    search_results = []

    if response.web:
        for result in response.web:
            title = getattr(result, "title", "No Title")
            url = getattr(result, "url", "")
            description = getattr(result, "description", "")

            search_results.append(
                {
                    "title": title,
                    "url": url,
                    "content": description,
                }
            )
        search_result = {
            "query": query,
            "results_count": len(search_results),
            "results": search_results,
        }
        return search_result
