from pydantic import BaseModel, Field
from google.adk.models.lite_llm import LiteLlm
from google.adk.agents import Agent
from .prompt import DESCRIPTION, INSTRUCTION
from typing import List


class SceneSchema(BaseModel):
    id: int = Field(description="Scene ID number")
    narration: str = Field(description="Narration(text) for the scene")
    image_description: str = Field(description="이미지 설명 텍스트")
    text_overay: str = Field(description="Text overlay for the image")
    text_overay_location: str = Field(
        description="Where to position the text on the image (ex. 'middle left', 'top center', 'bottom right', 'center')"
    )
    duration: int = Field(description="Duration in seconds for this scene")


class PlanSchema(BaseModel):
    topic: str = Field(description="Topic for the shorts video")
    total_duration: int = Field(description="Total video duration in seconds (max 25)")
    scenes: List[SceneSchema] = Field(
        description="List of scenes (agent decides how many)"
    )


content_planner_agent = Agent(
    name="ContentPlannerAgent",
    model=LiteLlm(model="openai/gpt-4o"),
    description=DESCRIPTION,
    instruction=INSTRUCTION,
    output_schema=PlanSchema,
    output_key="content_planner_output",
)
