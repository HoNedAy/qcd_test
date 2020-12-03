from selenium import webdriver
from login_data import  login_data
from qcd import lession_11_18
driver=webdriver.Chrome()  #选择浏览器,并进行初始化
url=login_data.url['url']  #获取地址
username=login_data.login_date.get('username')
password=login_data.login_date['password']
s_key=login_data.key_s.get('s_key')
lession_11_18.search_fuc(url,driver,username,password,s_key)