from google.adk.agents import ParallelAgent
from .prompt import ASSET_MAKER_DESCRIPTION
from .image_maker.agent import image_maker_agent
from .voice_maker.agent import voice_maker_agent

content_maker_agent = ParallelAgent(
    name="ContentMakerAgent",
    description=ASSET_MAKER_DESCRIPTION,
    sub_agents=[
        image_maker_agent,
        voice_maker_agent,
    ],
)
