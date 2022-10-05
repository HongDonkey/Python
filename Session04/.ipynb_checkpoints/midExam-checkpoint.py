#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install selenium # 자동화를 위한 셀레니움 설치


# In[1]:


#-*- coding: UTF-8 -*- 
import pandas as pd  # pandas import
from selenium import webdriver # selenium import
from bs4 import BeautifulSoup # bs4 import
from selenium.webdriver.common.by import By # 마우스 이동하는 라이브러리
from selenium.webdriver.common.keys import Keys # 검색하게 해주는 라이브러리


# In[2]:


options = webdriver.ChromeOptions()


# In[3]:


# 셀레니움 헤더변경 필요
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:71.0) Gecko/20100101 Firefox/71.0'    
options.add_argument('user-agent={0}'.format(user_agent))


# In[4]:


# options.add_argument('headless')
# 드라이버옵션설정
# 헤드리스 옵션 / 일반 옵션
# options.add_argument('--headless')  # 헤드리스 옵션(리눅스 - 화면을 띄우지 않음)
options.add_argument("window-size=1920x1080") # 일반옵션(윈도우서버 - 개발할 때 디버깅 확인용도)
options.add_argument("disable-gpu")


# In[5]:


driverLoc = "../addon/chromedriver/chromedriver.exe"  # 드라이버위치설정


# In[6]:


# 웹드라이버정의
driver = webdriver.Chrome(executable_path=driverLoc,options=options)
# driver = webdriver.Chrome(dirver_loc, options=options) 
#executable_path에 변수를 지정하여 사용햇다면 options에도 변수를 지정하여 사용해야 함
#자동화된 테스트 소프트 웨어에 의헤 제어되는 크롬창 열림


# In[7]:


# 웹페이지 파싱될 때까지 최대 3초 기다림
driver.implicitly_wait(3)


# In[8]:


# URL 이동
driver.get("http://www.sfunbox.com/index.html") # 광동스펀몰


# In[9]:


# 현재 URL 정보 확인
driver.current_url


# In[10]:


# 현재 URL 개발자 페이지 정보 확인
driver.page_source


# In[11]:


sfunSearchXpath = '//*[@id="headerSearchArea"]/div/div/form/fieldset/input' # 광동스펀몰 검색창의 Xpath를 sfunSearchXpath에 담음

sfunSearchBox = driver.find_element_by_xpath(sfunSearchXpath) # 광동스펀몰 검색창 지정 - sfunSearchBox

searchKeyword = "비타" # "비타" 검색어 입력

sfunSearchBox.send_keys(searchKeyword) # 검색창에 "비타" 입력

sfunSearchBox.send_keys(Keys.ENTER) # 검색창에 "비타" 입력 후 엔터

pgSource = driver.page_source # 페이지의 개발자 정보를 변수에 담음


# In[12]:


pgObj = BeautifulSoup(pgSource, "html.parser") # 개발자 페이지 코드를 bs4를 이용하여 출력


# In[13]:


vitaResearch=pgObj.find_all(name = "div", attrs={"class":"price_tit"})  # div 태그의 "class":"price_tit"의 내용을 vitaResearch에 배열로 담음


# In[14]:


productList = [] # 상품명이 들어갈 리스트 생성
priceList = [] # 가격이 들어갈 리스트 생성
for i in range(0, len(vitaResearch)):
    vitaResult = vitaResearch[i].find(name="a") # vitaResearch의 a태그를 가진 내용을 순서대로 찾아 vitaResult 변수에 담음 (상품명만 출력)
    product = vitaResult.text # 상품명만 product 변수에 담음
    productList.append(product) # product를 productList에 추가함
    vitaPrice=vitaResearch[i].find(name="strong") # vitaResearch의 strong태그를 가진 내용을 순서대로 찾아 vitaPrice 변수에 담음 (가격만 출력)
    price = vitaPrice.text # 가격만 price 변수에 담음
    priceList.append(price) # price를 priceList에 추가함


# In[15]:


vitaDf = pd.DataFrame(zip (productList, priceList), columns=["상품명","가격"]) # 데이터프레임으로 출력하고 컬럼명을 '상품명' , '가격'으로 지정
vitaDf.to_csv("vita.csv",encoding="ms949",index=False) # vita라는 이름의 csv파일로 export


# In[ ]:





# In[16]:


import smtplib # 메일 전송 라이브러리


# In[17]:


from email.message import EmailMessage # 이메일을 간단하게 보낼 수 있는 라이브러리 로드


# In[18]:


# GMAIL 메일 설정
smtp_gmail = smtplib.SMTP('smtp.gmail.com',587)


# In[19]:


# 서버 연결을 설정하는 단계
smtp_gmail.ehlo()


# In[20]:


# 연결을 암호화
smtp_gmail.starttls()


# In[21]:


userid = "hdk2006" # gmail ID
userpw = "osxkiqrkgczkknbt" # 앱 비밀번호
smtp_gmail.login(userid, userpw) # ID와 비밀번호 변수를 통하여 로그인


# In[22]:


# 엑셀에서 만든 이름과 이메일 정보가 있는 csv파일 로드
emailList = pd.read_csv("emailAddress.csv",encoding = 'UTF8')
emailList


# In[23]:


# 이메일 컬럼의 내용을 리스트에 담음
to = emailList['이메일'].tolist()
to


# In[24]:


msg = EmailMessage() # EmailMessage 모듈의 별칭을 msg로 이름을 지정.
msg['Subject'] = "홍동기 중간고사 제출입니다." # 이메일 제목
msg.set_content("csv파일 첨부합니다.") # 이메일 내용
msg['From'] = 'hdk2006@gmail.com' # 발신자 이메일
msg['To'] = ",".join(to) # 이메일 목록이 담긴 리스트와 수신자를 ","로 구분 / 이메일 csv에 있는 이메일 주소를 수신자로 설정


# In[25]:


file='vita.csv' # 보낼 vita.csv파일을 file변수에 담음
fp = open(file,'rb') # file을 선택
file_data = fp.read() # vita.csv파일을 읽어오는 함수
msg.add_attachment(file_data,maintype='text',subtype='plain',filename=file) # 파일에 대한 옵션


# In[26]:


smtp_gmail.send_message(msg) # 메일 전송
smtp_gmail.close() # 종료

