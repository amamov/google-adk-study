from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from .prompt import DESCRIPTION, INSTRUCTION
from .tools import generate_narrations

MODEL = LiteLlm(model="openai/gpt-4o")

voice_maker_agent = Agent(
    name="VoiceMakerAgent",
    description=DESCRIPTION,
    instruction=INSTRUCTION,
    model=MODEL,
    tools=[
        generate_narrations,
    ],
)
