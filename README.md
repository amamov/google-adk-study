# Google ADK Study

- [docs](https://google.github.io/adk-docs/)

## Note

- 루트 폴더 경로에서 `adk web` 명령어 치면, 서버 열림 --> 멀티모달 처리 가능
- `adk api_server` 명령어 치고, `/docs` 경로로 들어가면 API Server 있음.
- [google adk 튜토리얼](https://google.github.io/adk-docs/tutorials/agent-team/#step-1-your-first-agent-basic-weather-lookup)
- 참고 : `sub_agents` 폴더 이름은 그냥 아무 이름으로 지어도 된다. 규칙은 에이전트 폴더 안에 `__init__.py` 파일 만들고 `root_agent` 변수가 정의된 파이썬 파일을 import 시켜주기만 하면 됨. but `sub_agents`라고 이름을 지은 이유는 google-adk sample github에 가면 이렇게 되어 있고 거기에 따라 지정하는 것임
- google adk로 작업할때는 tool 개발에서 ai model이 잘 알아들을 수 있도록, JSON 형식(혹은 Dict 형식)으로 return 해주는 것이 좋다.
- [artifacts](https://google.github.io/adk-docs/artifacts/) agent랑 tool이 텍스트가 아닌 데이터를 다룰 수 있게 해준다.
- https://google.github.io/adk-docs/agents/workflow-agents/
