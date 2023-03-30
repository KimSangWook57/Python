# 다음 영화 예매 순위 정보를 출력하는 예시

import requests
from bs4 import BeautifulSoup

url = 'https://movie.daum.net/ranking/reservation'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
# 1. 전체 태그 확인
# print(soup)

# 2. 원하는 태그를 감싸는 태그 확인
ol = soup.select_one('.list_movieranking')
# print(ol)

# 3. 하위 태그로 내려가면서 확인
li_list = ol.find_all('li')
# print(li_list)

movie = []

# 4. 리스트 안의 순위와 평점 확인
for li in li_list:
    rank = li.select_one('.rank_num').text
    name = li.select_one('.link_txt').text
    see = li.select_one('.ico_see').text
    grade = li.select_one('.txt_grade').text
    # 예매율은 %를 빼고 가져온다.
    num = li.select_one('.txt_num').text[:-1]
    mvdate = li.select_one('.txt_info > .txt_num').text

    movie.append([rank, name, see, grade, num, mvdate])

# print(movie)

# csv 파일 만들기 실습
import pandas as pd

# df = pd.DataFrame(movie, columns = ['순위', '영화명', '관람가', '평점', '예매율', '개봉일'])
# df.to_csv('movie_info.csv', index=False, encoding='cp949')

# 조건 부여
# 비교를 위해 위에서 만든 파일을 다시 불러와서 자료형을 바꿔준다.
df = pd.read_csv('movie_info.csv', encoding='cp949')
# print(df.info())
# 평점이 8점 이상인 영화만 표시
# print(df[df['평점'] > 8])

import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

# 시계열처리
# 현재 날짜 형식 = 23.01.04 ('%y.%m.%d')
# datetime 타입으로 바꿔준다.
df['개봉일'] = pd.to_datetime(df['개봉일'], format = '%y.%m.%d')
# print(df.info())

# 위 형식은 VS에서는 지원하지 않는 것 같다.
# df_weekly = df.resample('W', on = '개봉일').mean(numeric_only = True)
df_weekly = df.resample('W', on = '개봉일').mean()
# print(df_weekly)

# 그래프 그리기 전 데이터 전처리
# 결측치 처리하기 (na를 0으로 변경)
df_weekly = df_weekly.fillna(0)

plt.plot(df_weekly.index, df_weekly['예매율'])
plt.show()


