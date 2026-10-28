from dotenv import load_dotenv
from typesafe_sdk import Choice, Noul, NoulCriteria, TypeSafeClient, Score

load_dotenv()

client = TypeSafeClient()

paragraphs = {
  "P1": "배송일로부터 30일 이내에 사용하지 않은 제품은 반품하실 수 있습니다.",
  "P2": "환불은 영업일 기준 5일 이내에 원래 결제 수단으로 지급됩니다.",
  "P3": "일반 배송은 영업일 기준 3~5일이 소요됩니다.",
  "P4": "제품이 파손되어 도착한 경우, 교환을 위해 사진을 첨부하여 고객센터로 문의해 주세요.",
}

question = "해외 배송도 가능한가요?"

criteria = {}

for paragraph_id in paragraphs:
  criteria[paragraph_id] = None


response = client.system_one(paragraphs, {
  "answer": Choice(instructions=f"어느 것이 다음 질문에 답하고 있나요?: {question}", criteria=criteria),
  "exists": Noul(instructions=f"다음 질문에 답할 수 있는 답을 가지고 있는 내용이 있나요?: {question}", 
  criteria=NoulCriteria(true="paragraphs에서 답을 직접 명시하거나 답을 암시함", false="paragraphs에서 답을 직접 명시하거나 답을 암시하지 않음"))
})


print(response)