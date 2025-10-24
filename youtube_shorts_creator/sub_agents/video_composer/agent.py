from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from .prompt import DESCRIPTION, INSTRUCTION
from .tools import assemble_video

MODEL = LiteLlm(model="openai/gpt-4o")

video_composer_agent = Agent(
    name="VideoComposerAgent",
    model=MODEL,
    description=DESCRIPTION,
    instruction=INSTRUCTION,
    output_key="video_assembler_output",
    tools=[
        assemble_video,
    ],
)
