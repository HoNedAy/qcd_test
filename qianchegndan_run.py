from selenium import webdriver
import time
from qianchegndan_datas import qianchengdan_data
from qianchegndan_tests import qianchengdan_test
driver=webdriver.Chrome()
url=qianchengdan_data.url.get('url')
mobilephone=qianchengdan_data.mobilephone.get('mobilephone')
password=qianchengdan_data.password['password']
driver.implicitly_wait(5)
qianchengdan_test.serach_number(url,mobilephone,driver,password)