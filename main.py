from dotenv import load_dotenv
from typesafe_sdk import TypeSafeClient, Noul

load_dotenv()

client = TypeSafeClient()

review = "헤드폰은 괜찮아요. 근데 먼지투성이였고, 3일 늦게 왔어요"

request = client.system_one(
  {"review": review, "rating": "1/5"}, 
  {
    "delay": Noul(instructions="리뷰에 지연에 대한 언급이 있나요?"),
    "broken": Noul(instructions="리뷰에 제품이 고장났다는 내용이 있나요?"),
    "price": Noul(instructions="리뷰에 가성비에 대한 언급이 있나요?"),
    "product": Noul(instructions="이 리뷰가 헤드폰에 대한 리뷰인가요?"),
    "positive": Noul(instructions="이 리뷰가 긍정적인 리뷰인가요?"),
    "negative": Noul(instructions="이 리뷰가 부정적인 리뷰인가요?"),
    "recommend": Noul(instructions="이 리뷰가 제품을 추천하는 리뷰인가요?"),
  }
)

print(request.answers)