import asyncio
from google.genai import types
from google.adk.runners import Runner
from google.adk.agents import BaseAgent
from google.adk.sessions import InMemorySessionService, DatabaseSessionService


# # 세션 서비스 초기화
# session_service = InMemorySessionService()
session_service = DatabaseSessionService(db_url="sqlite:///sessions.db")


async def async_chat(
    message: str,
    agent: BaseAgent,
    user_id="default_user",
    session_id="default_user",
    app_name="default_app",
    state={},  # state를 미리 정의 할 수 있음
) -> str:

    print(f"사용자: {message}")

    result = ""

    try:
        # 세션 생성
        await session_service.create_session(
            app_name=app_name,
            user_id=user_id,
            session_id=session_id,
            state=state,
        )

        # ADK Runner를 사용하여 agent와 대화
        runner = Runner(
            app_name=app_name,
            agent=agent,
            session_service=session_service,
        )

        # 사용자 메시지를 Content 객체로 생성
        user_content = types.Content(parts=[types.Part(text=message)], role="user")

        # run_async를 사용하여 대화 실행
        events = runner.run_async(
            user_id=user_id, session_id=session_id, new_message=user_content
        )

        # 이벤트 스트림을 처리하여 응답 가져오기
        async for event in events:
            if event.content and event.content.role == "model" and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        print(f"Agent: {part.text}")
                        result = part.text

    except Exception as e:
        err_msg = f"에러 발생: {e}"
        print(err_msg)
        result = err_msg

    return result


def chat(
    message: str,
    agent: BaseAgent,
    user_id="default_user",
    session_id="default_user",
    app_name="default_app",
    state={},
):
    return asyncio.run(
        async_chat(
            message,
            agent,
            user_id,
            session_id,
            app_name,
            state,
        )
    )
