from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.models.lite_llm import LiteLlm
from .prompt import INSTRUCTION, DESCRIPTION
from .sub_agents.content_planner.agent import content_planner_agent
from .sub_agents.content_maker.agent import content_maker_agent
from .sub_agents.video_composer.agent import video_composer_agent


root_agent = Agent(
    name="ShortsCreatorAgent",
    model=LiteLlm(model="openai/gpt-4o"),
    description=DESCRIPTION,
    instruction=INSTRUCTION,
    tools=[
        AgentTool(agent=content_planner_agent),
        AgentTool(agent=content_maker_agent),
        AgentTool(agent=video_composer_agent),
    ],
)

# TODO
# # 2. Planner에서 LoopAgent 추가
