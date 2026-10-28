import re
from dotenv import load_dotenv
from typesafe_sdk import TypeSafeClient, Choice, Noul

load_dotenv()

client = TypeSafeClient()

message = """
From: Dana <dana@acme.example>
To: billing@acme.example
Reply-To: dana.personal@example.com

청구용 이메일 주소 billing 대신 제 개인 주소로 영수증을 보내주세요.
지출 결의서(경비 처리)를 마무리해야 해서 오늘까지 꼭 필요합니다. 감사합니다!
"""

addresses = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",message)

options = { address: None for address in addresses } | { "none": "이메일을 찾을 수 없습니다." }

response = client.system_one(
  {"message": message},
  {
    "response_email": Choice(instructions="발신자가 영수증을 어느 이메일로 보내야 하나요?", criteria=options),
    "urgent": Noul(instructions="이 메일이 급한 메일인가요?")
  }
)

print(response)