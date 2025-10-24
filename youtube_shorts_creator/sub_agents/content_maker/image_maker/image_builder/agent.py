from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from .prompt import DESCRIPTION, INSTRUCTION
from .tools import generate_images

MODEL = LiteLlm(model="openai/gpt-4o")

image_builder_agent = Agent(
    name="ImageBuilder",
    description=DESCRIPTION,
    instruction=INSTRUCTION,
    model=MODEL,
    output_key="image_builder_output",
    tools=[
        generate_images,
    ],
)
