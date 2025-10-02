import asyncio
from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    filters,
    ContextTypes,
)
from google.genai import types
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from financial_advisor.agent import root_agent
from env import TELEGRAM_BOT_TOKEN

# 글로벌 runner와 session_service 초기화
session_service = None
runner = None


async def init_agent():
    """ADK agent 초기화"""
    global session_service, runner

    # 세션 서비스 초기화
    session_service = InMemorySessionService()

    # ADK Runner 초기화
    runner = Runner(
        app_name="financial_advisor_telegram",
        agent=root_agent,
        session_service=session_service,
    )


async def run_agent(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ADK agent를 실행하여 사용자 메시지에 응답"""
    if update.message is None or update.message.text is None:
        return

    user_message = update.message.text
    user_id = str(update.message.from_user.id if update.message.from_user else None )
    session_id = f"telegram_session_{user_id}"

    await update.message.reply_text(
        "에이전트가 요청을 처리하고 있습니다. 잠시만 기다려주세요..."
    )

    try:
        # 세션이 없으면 생성
        try:
            await session_service.get_session(user_id, session_id)
        except:
            await session_service.create_session(
                app_name="financial_advisor_telegram",
                user_id=user_id,
                session_id=session_id,
            )

        # 사용자 메시지를 Content 객체로 생성
        user_content = types.Content(parts=[types.Part(text=user_message)], role="user")

        # ADK agent 실행
        events = runner.run_async(
            user_id=user_id, session_id=session_id, new_message=user_content
        )

        # 응답 수집
        bot_response = ""
        async for event in events:
            if event.content and event.content.role == "model" and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        bot_response += part.text

        # 응답 전송
        if bot_response:
            await update.message.reply_text(bot_response)
        else:
            await update.message.reply_text("죄송합니다. 응답을 생성할 수 없었습니다.")

    except Exception as e:
        print(f"에러 발생: {e}")
        await update.message.reply_text(f"오류가 발생했습니다: {str(e)}")


async def main() -> None:
    """텔레그램 봇 시작"""
    # ADK agent 초기화


    await init_agent()

    # 텔레그램 봇 설정
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, run_agent))

    # 봇 실행
    await application.initialize()
    await application.start()
    await application.updater.start_polling()

    print("텔레그램 봇이 시작되었습니다. Ctrl+C로 종료하세요.")

    try:
        # 봇이 계속 실행되도록 대기
        await asyncio.Event().wait()
    except KeyboardInterrupt:
    finally:
        await application.stop()


if __name__ == "__main__":
    asyncio.run(main())
