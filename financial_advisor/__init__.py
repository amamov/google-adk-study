from . import agent

"""
[ Note ]
__init__.py를 폴더에 넣으면 그 폴더는 파이썬 패키지가 되고 __init__.py는 그 파이썬 패키지의 진입점이 된다.
패키지의 진입 지점에서 agent를 export하는 것
from . import agent ===> 이것으로 Google ADK에 root_agent 변수가 노출되게 한것
Google ADK는 자동으로 root_agent가 있는 agent 모듈 파일을 찾는것
"""
