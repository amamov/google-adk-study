from adk_chat import chat
from lina.agent import root_agent as lina_agent


chat("안녕", lina_agent, state={"username": "상석"})
