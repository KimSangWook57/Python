# 웹크롤링(BeautifulSoup) + pandas + matplotlib 과제

import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

# 구글 뉴스 한국어 헤드라인 페이지 URL
url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR&ceid=KR%3Ako"

# URL로 GET 요청 보내기
response = requests.get(url)

# HTML 내용을 Beautiful Soup로 파싱하기
soup = BeautifulSoup(response.content, 'html.parser')

# 페이지의 모든 헤드라인 찾기
headlines = soup.find_all('h4')

# 헤드라인에서 텍스트 추출하고 정리하기
cleaned_headlines = [re.sub('[^ㄱ-ㅎㅏ-ㅣ가-힣\s]', '', headline.text) for headline in headlines]

# 정리된 헤드라인 토큰화하기
tokens = [headline.split() for headline in cleaned_headlines]

# 의미없는 용어 제거하기
stop_words = ['그', '이', '수', '것', '그것', '여기', '저기', '거기', '내', '너', '그녀', '그들', '제', '하다', '되다', '같다', '년', '월', '일']
tokens = [[word for word in headline if word not in stop_words] for headline in tokens]

# 토큰 리스트 평탄화하기
flat_tokens = [word for headline in tokens for word in headline]

# 각 단어 빈도수 카운트하기
word_count = Counter(flat_tokens)

# 가장 많이 사용된 30개 단어 가져오기
most_common_words = word_count.most_common(30)

# 단어 빈도수 시각화하기
plt.bar([word[0] for word in most_common_words], [word[1] for word in most_common_words])
plt.xticks(rotation=90)
plt.xlabel("word")
plt.ylabel("count")
plt.title("Google News Headline Word Frequency in Korea")
plt.show()

# 단어 빈도수 딕셔너리를 Pandas 데이터프레임으로 변환
df = pd.DataFrame(list(word_count.items()), columns=['단어', '빈도수'])

# DataFrame을 CSV 파일로 저장
df.to_csv('word_freq.csv', index=False, encoding='cp949')

