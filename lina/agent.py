from google.genai import types
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from .prompt import PROMPT

MODEL = LiteLlm("openai/gpt-4o")


lina_agent = Agent(
    name="MyBro",
    instruction=PROMPT,
    model=MODEL,
    tools=[],
)

root_agent = lina_agent
