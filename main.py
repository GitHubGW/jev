from dotenv import load_dotenv
from typesafe_sdk import Choice, Noul, NoulCriteria, TypeSafeClient, Score

load_dotenv()

client = TypeSafeClient()

state = {
    "student": {
        "experience": "Python의 변수, 반복문, 함수는 알고 있지만, 웹 API를 만들어본 적은 없습니다.",
        "projects": [
            {"goal": "내 모바일 앱이 학습 기록을 저장하고 조회할 수 있는 Python API 구축하기"},
            {"goal": "나중에 개인 포트폴리오 웹사이트 만들기"},
        ],
    },
}


response = client.system_one(state, {
  "recommendation": Choice(
  instructions={
    "question": "어떤 학습 주제가 가장 적합한가요? `student.projects[0].goal`",
    "context": "`student.experience`를 참고하세요"
  },
  criteria={
    "frontend": {
        "topics": ["HTML", "CSS", "browser interfaces"],
        "prerequisites": "No previous web development required.",
        "project_example": "A personal portfolio website.",
    },
    "python_api": {
        "topics": ["HTTP", "Python API routes", "database storage"],
        "prerequisites": "Basic Python, variables, loops, and functions.",
        "project_example": "A backend that stores data for a mobile app.",
    },
    "data_analysis": {
        "topics": ["CSV files", "dataframes", "charts"],
        "prerequisites": "Basic Python.",
        "project_example": "Analyze workout history from a spreadsheet.",
    },
    "none": {
        "description": "None of the listed topics fits the current project."
    },
  }
  )
})

print(response)