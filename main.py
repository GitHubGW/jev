from dotenv import load_dotenv
from typesafe_sdk import TypeSafeClient, Score

load_dotenv()

client = TypeSafeClient()

message = """
From: Dana <dana@acme.example>
To: billing@acme.example
Reply-To: dana.personal@example.com

청구용 이메일 주소 billing 대신 제 개인 주소로 영수증을 보내주세요.
지출 결의서(경비 처리)를 마무리해야 해서 오늘까지 꼭 필요합니다. 감사합니다!
"""

response = client.system_one(
  {"message": message},
  {
    "urgency_level": Score(
      instructions="발신자의 요청이 마감일 기준으로 얼마나 긴급한가요?",
      criteria=["급한 메일", "보통 메일", "급하지 않은 메일"]
    )
  }
)

print(response.answers["urgency_level"])