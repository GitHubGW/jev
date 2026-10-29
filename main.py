from dotenv import load_dotenv
from typesafe_sdk import Noul, NoulAnswer, ScoreAnswer, TypeSafeClient, Score, SystemOneResponse

load_dotenv()

client = TypeSafeClient()

bug = ("페이지에 둥근 모서리가 있어요. 환불 받을 수 있을까요?",)

class BugResponse(SystemOneResponse):
  severity: ScoreAnswer
  urgent: NoulAnswer

response = client.system_one(
  {"report": bug},
  {
    "severity": Score(
    instructions="보고된 문제가 얼마나 심각한가요? 해결 방법이 있을까요?", 
    criteria=[
      "외관상 문제지만, 사용자들은 평소처럼 업무를 완료할 수 있는 큰 문제는 아닙니다.",
      "기능 하나가 고장났지만 사용자는 우회 방법으로 목표를 완료할 수 있습니다.",
      "사용자는 우회할 수 없고, 업무를 완료할 수 없는 심각한 문제입니다."
    ]
    ),
    "urgent": Noul(instructions="이 문제는 얼마나 급한가요? 해결 방법이 있을까요?")
  },
  response_model=BugResponse
)

print(response.severity)

