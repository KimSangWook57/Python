# find()와 find_all() 메서드를 사용한 예시

# find() 메서드는 HTML 코드에서 조건에 맞는 첫 번째 태그를 찾아서 반환합니다. 
# find_all() 메서드는 HTML 코드에서 조건에 맞는 모든 태그를 찾아서 리스트 형태로 반환합니다.
from bs4 import BeautifulSoup

html = '''
<html>
<body>
<div class="menu">
    <ul>
        <li><a href="/home">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
</div>
<div class="content">
    <h1>Hello, World!</h1>
    <p>This is an example of using Beautifulsoup.</p>
</div>
</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')

# find() 메서드 사용 예시
# div 형식의 menu 클래스를 찾는다.
div_menu = soup.find('div', {'class': 'menu'})
print(div_menu)
print("=================================")
# 원하는 태그를 감싸고 있는 태그인 div_menu를 먼저 찾은 다음, 그 안에서 a 찾기.
div_menu = soup.find('div', {'class': 'menu'})
links = div_menu.find_all('a')
for link in links:
    print(link.get('href'))
print("=================================")
# .text를 붙이는 방법 참고
print(div_menu.text)
print("=================================")
# find_all() 메서드 사용 예시
# 모든 a 태그를 찾아서...
links = soup.find_all('a')
# # 각각의 하이퍼링크를 반환.
for link in links:
    print(link.get('href'))
print("=================================")
# .text를 붙이는 방법 참고
for link in links:
    print(link.text)
print("=================================")
