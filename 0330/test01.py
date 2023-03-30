# 웹 스크래핑의 개념과 목적
# 웹 페이지에서 데이터를 추출하여 수집하는 것을 말합니다. 주로 데이터 수집 및 분석, 기업 비교 및 분석 등의 목적으로 사용됩니다.
# 장점으로는 대량의 데이터 수집, 효율적인 데이터 분석, 비용 절감 등이 있습니다. 
# 단점으로는 웹사이트의 로봇 배제 표준에 따른 규제, 데이터 보안 위협 등이 있습니다.

# 한겨레 신문의 오늘의 뉴스 기사 제목을 크롤링
import requests
from bs4 import BeautifulSoup

url = "https://www.hani.co.kr/arti/list.html?sec=news&subsec=politics"
response = requests.get(url)
# print(response.text)
print("=============================================")
# html 파싱
# BeautifulSoup()는 HTML, XML 등의 문서를 파싱하여 파이썬에서 사용할 수 있는 객체로 만드는 클래스입니다.
# markup (필수): 파싱할 HTML, XML 등의 코드
# features: 파서 엔진의 종류를 지정합니다. 기본값은 html.parser입니다. 다른 파서 엔진으로 lxml, html5lib 등을 지정할 수 있습니다.
# soup 객체를 이용하여 HTML 코드에서 필요한 데이터를 추출하거나 탐색
soup = BeautifulSoup(response.text, "html.parser")

# BeautifulSoup 객체 soup에서 find_all() 메서드를 이용하여, HTML 코드에서 h4 태그 중 class 속성이 "article-title"인 요소를 찾는 코드
# find_all() 메서드
# 조건에 맞는 모든 태그를 찾아서 리스트 형태로 반환합니다. 
# h4 태그를 찾고, 이 중 class 속성이 "article-title"인 요소를 모두 찾아서 titles 변수에 할당
titles = soup.find_all("h4", class_="article-title")

# find(): 조건에 맞는 첫 번째 태그를 찾아 반환합니다.
# Name: 태그 이름을 지정합니다.
# Attrs: 태그의 속성과 값을 지정합니다.
# Recursive: 하위 태그를 포함하여 검색할지 여부를 지정합니다.
# find_all(): 조건에 맞는 모든 태그를 찾아 리스트형태로 반환합니다.
# name: 태그 이름을 지정합니다.
# attrs: 태그의 속성과 값을 지정합니다.
# recursive: 하위 태그를 포함하여 검색할지 여부를 지정합니다.
# limit: 반환할 최대 태그 개수를 지정합니다.
# select_one() 메서드는 선택된 태그 중에서 첫 번째 태그만을 반환합니다.
# select(): CSS 선택자를 이용하여 선택된 모든 태그를 리스트 형태로 반환합니다. 
# text(): 태그의 텍스트 내용을 반환합니다.
# get(): 태그의 속성 값을 반환합니다.
# find_parents(): 해당 태그의 모든 부모 태그를 반환합니다. 반환값은 ResultSet 객체입니다.
# find_parent(): 해당 태그의 첫 번째 부모 태그를 반환합니다. 반환값은 Tag 객체입니다.
# find_next_siblings(): 해당 태그 다음에 나오는 모든 형제 태그들을 반환합니다. 반환값은 ResultSet 객체입니다.
# find_next_sibling(): 해당 태그 다음에 나오는 첫 번째 형제 태그를 반환합니다. 반환값은 Tag 객체입니다.
# find_previous_siblings(): 해당 태그 이전에 나온 모든 형제 태그들을 반환합니다. 반환값은 ResultSet 객체입니다.
# find_previous_sibling(): 해당 태그 이전에 나온 첫 번째 형제 태그를 반환합니다. 반환값은 Tag 객체입니다.


for title in titles:
    print(title.text.strip())
print("=============================================")
# get() 메서드가 반환하는 객체는 Response 객체입니다. 
# 이 객체는 HTTP 응답에 대한 정보를 가지고 있으며, HTML 코드는 text 속성에 저장되어 있습니다.
# response.text를 이용하여 HTTP 응답에서 HTML 코드를 가져와서, 웹 스크래핑에 활용할 수 있습니다.

