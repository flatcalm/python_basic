
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time as t
# 뷰티풀수프 임포트
from bs4 import BeautifulSoup
# 날짜 정보 얻어오는 모듈 (연, 월, 일, 시, 분, 초)
from datetime import datetime
import codecs

d = datetime.today()

file_path = f'C:/test/교보문고_주간_베스트_이미지_링크_{d.year}_{d.month}_{d.day}.html'

'''
- with문을 사용하면 with 블록을 벗어나는 순간
객체가 자동으로 해제됩니다. (자바의 try with resource과 비슷)

- with 작성 시 사용할 객체의 이름을 as 뒤에 작성해 줍니다.
'''

'''
* 표준 모듈 codecs

- 웹이나 다른 프로그램의 텍스트 데이터와
파이썬 내부의 텍스트 데이터의 인코딩 방식이 서로 다를 경우에
내장함수 open()이 제대로 인코딩을 적용할 수 없어서
에러가 발생합니다. (UnicodeEncodeError)

- 파일 입/출력 시 인코딩 코덱을 변경하고 싶다면
codecs 모듈을 사용합니다.
'''

with codecs.open(file_path, mode='w', encoding='utf-8') as f:

  f.write(f'''<!DOCTYPE html>
<html>
<head>
  <meta charset='utf-8'>
  <meta http-equiv='X-UA-Compatible' content='IE=edge'>
  <title>Page Title</title>
  <meta name='viewport' content='width=device-width, initial-scale=1'>
  <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
  <script src='main.js'></script>
</head>
<body>
''')

  options = webdriver.ChromeOptions()
  options.add_experimental_option('detach', True)

  service = webdriver.ChromeService(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=service, options=options)

  driver.get('https://www.kyobobook.co.kr/')
  t.sleep(2)

  rank = 1 # 순위 표시

# 베스트 탭 클릭
  driver.find_element(By.XPATH, '//*[@id="welcome_header_wrap"]/div[3]/nav/ul[1]/li[3]/a').click()
  t.sleep(2)

# 주간 탭 클릭
  driver.find_element(By.XPATH, '//*[@id="mainDiv"]/main/section[2]/div/aside/div[2]/div/ul/li[1]/ul/li[1]/a').click()
  t.sleep(2)

  src = driver.page_source
  soup = BeautifulSoup(src, 'html.parser')

  prod_item = soup.find_all('li', class_='prod_item')

  for item in prod_item:
    item_link = item.find('a', class_='prod_link')
    print(item_link)

    f.write(f'<span>{rank}위</span>')
    f.write(str(item_link))
    rank += 1
  
  f.write(f'''</body>
</html>
''')

