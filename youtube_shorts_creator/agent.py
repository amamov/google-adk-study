from google.genai import types
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.models.lite_llm import LiteLlm
from .sub_agents.content_planner.agent import content_planner_agent
from .sub_agents.content_maker.agent import asset_generator_agent
from .sub_agents.video_assembler.agent import video_assembler_agent
from .prompt import SHORTS_PRODUCER_DESCRIPTION, SHORTS_PRODUCER_PROMPT
from google.adk.agents.callback_context import CallbackContext
from google.adk.models.llm_request import LlmRequest
from google.adk.models.llm_response import LlmResponse


def before_model_callback(
    callback_context: CallbackContext,
    llm_request: LlmRequest,
):
    """
    [Note]
    https://google.github.io/adk-docs/callbacks/#introduction-what-are-callbacks-and-why-use-them
    callback에 뭘 return하느냐에 따라 모든게 달라진다. (오버라이딩)
    prompt validation 할때 쓴다고 보면됨
    """
    # print(callback_context.agent_name)
    history = llm_request.contents
    last_message = history[-1]
    if last_message and last_message.parts and last_message.role == "user":
        text = str(last_message.parts[0].text)
        if (
            "hummus" in text
        ):  # 일종에 예시로 그냥 hummus라고 있으면 보내도록 하는 필터 기능
            return LlmResponse(
                content=types.Content(
                    parts=[
                        types.Part(text="Sorry I can't help with that."),
                    ],
                    role="model",
                )
            )
    return None  # 기본적으로 기본 동작을 허용 한다는 것


root_agent = Agent(
    name="Shorts_PD_Agent",
    model=LiteLlm(model="openai/gpt-4o"),
    description=SHORTS_PRODUCER_DESCRIPTION,
    instruction=SHORTS_PRODUCER_PROMPT,
    sub_agents=[
        content_planner_agent,
        asset_generator_agent,
        # video_assembler_agent,
    ],
    before_model_callback=before_model_callback,
)
