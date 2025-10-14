import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from .prompt import PROMPT
from env import OPENAI_API_KEY


os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

MODEL = LiteLlm("openai/gpt-4o")

# 반드시 root_agent 변수에 Agent 인스턴스를 담아야 함
root_agent = Agent(
    name="lina",
    instruction=PROMPT,
    model=MODEL,
    tools=[],
)
