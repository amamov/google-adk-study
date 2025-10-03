from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from tools import web_search_tool


MODEL = LiteLlm(model="openai/gpt-4o")


news_analyst = Agent(
    name="NewsAnalyst",
    model=MODEL,
    description="Uses Web Search tools to search and scrape real web content from the web.",
    instruction="""
    당신은 웹 도구를 사용하여 최신 정보를 찾는 뉴스 분석 전문가입니다. 업무:

    1. **웹 검색**: web_search_tool()을 사용하여 기업 관련 최근 뉴스 찾기
    2. **결과 요약**: 발견한 내용과 관련성 설명

    **사용 가능한 웹 도구:**
    - **web_search_tool()**: Firecrawl web search for company news

    외부 API를 사용하여 최신 정보를 위한 웹 콘텐츠 검색 및 수집.
    """,
    output_key="news_analyst_result",  # "news_analyst_result" state 저장
    tools=[
        web_search_tool,
    ],
)
