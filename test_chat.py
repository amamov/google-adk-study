import asyncio
from google.genai import types
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from financial_advisor.agent import root_agent


async def test_chat():
    """root_agent와 간단한 대화 테스트"""

    message = "안녕 내 이름은 윤상석이야"

    print(f"사용자: {message}")

    try:
        # 세션 서비스 초기화
        session_service = InMemorySessionService()

        # 세션 ID와 사용자 ID (임의로 설정)
        user_id = "test_user"
        session_id = "test_session"

        # 세션 생성
        await session_service.create_session(
            app_name="financial_advisor_test", user_id=user_id, session_id=session_id
        )

        # ADK Runner를 사용하여 agent와 대화
        runner = Runner(
            app_name="financial_advisor_test",
            agent=root_agent,
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

    except Exception as e:
        print(f"에러 발생: {e}")


if __name__ == "__main__":
    asyncio.run(test_chat())
