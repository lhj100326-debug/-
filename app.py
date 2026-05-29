import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="오늘의 운세",
    page_icon="🔮",
)

st.title("🔮 오늘의 운세")
st.write("이름을 입력하고 오늘의 운세를 확인해보세요!")

name = st.text_input("이름 입력")

fortunes = [
    "오늘은 행운이 가득한 하루입니다 🍀",
    "좋은 소식이 찾아올 가능성이 높아요 📩",
    "새로운 도전을 하면 좋은 결과가 있습니다 🚀",
    "휴식을 취하면 에너지가 회복됩니다 ☕",
    "뜻밖의 기회가 찾아올 수 있어요 ✨",
    "주변 사람들과의 대화에서 힌트를 얻습니다 💬",
    "작은 행운이 큰 행복으로 이어집니다 😊",
]

if st.button("운세 보기"):
    if name.strip() == "":
        st.warning("이름을 입력해주세요!")
    else:
        # 날짜 + 이름 기준으로 항상 같은 운세 나오게 설정
        today = datetime.now().strftime("%Y-%m-%d")
        random.seed(name + today)

        fortune = random.choice(fortunes)

        st.success(f"{name}님의 오늘의 운세")
        st.subheader(fortune)
