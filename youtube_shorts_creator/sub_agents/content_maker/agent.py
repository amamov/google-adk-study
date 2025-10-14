from google.adk.agents import ParallelAgent
from .prompt import ASSET_GENERATOR_DESCRIPTION
from .image_maker.agent import image_maker_agent
from .voice_maker.agent import voice_maker_agent

asset_generator_agent = ParallelAgent(
    name="AssetGeneratorAgent",
    description=ASSET_GENERATOR_DESCRIPTION,
    sub_agents=[
        image_maker_agent,
        voice_maker_agent,
    ],
)
