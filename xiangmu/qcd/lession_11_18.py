#web自动化
from selenium import webdriver
import time

def open_url(url,driver):  #访问登录函数
    url=driver.get(url) #打开浏览器进行访问
    driver.maximize_window()#窗口最大化
    time.sleep(3)
def login_page(driver,username,password):
   # username=driver.find_element_by_id('username') #获取文本框
    username1=driver.find_element_by_xpath("//input[@id='username']")  #xpath获取方式
    username1.click()# #点击
    username1.send_keys(username) #输入内容
    password=driver.find_element_by_id('password').send_keys(password)#获取密码文本框并填写数据
    submit=driver.find_element_by_id('btnSubmit').click()  #获取提交按钮并点击


def search_fuc(url,driver,username,password,s_key):
    open_url(url,driver)  #打开网址
    login_page(driver,username,password)  #登录操作
    driver.implicitly_wait(10)
    t=driver.find_element_by_xpath("//b[text()='柠檬ERP']").text  #得到标题
    lingshou=driver.find_element_by_xpath('//span[text()="零售出库"]').click()#找到零售出库并点击
    #找到frame窗口并切换
    f_id=driver.switch_to.frame(1)
    seach_data=driver.find_element_by_id('searchNumber').send_keys(s_key)
    driver.implicitly_wait(10)
    driver.find_element_by_id('searchBtn').click()


