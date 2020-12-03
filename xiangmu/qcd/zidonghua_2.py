#工具里面所有的内容都导入
# import selenium
from selenium import webdriver  #不会导入所有内容，节约资源,从selenium工具里导入webdriver
# from selenium.webdriver import Chrome

import  time;  #导入时间库
driver=webdriver.Chrome()   #选择chrome这个浏览器，初始化driver=可以在浏览器进行沟通   建立会话==session
#1、打开一个新的页面
# driver.get("http://120.78.128.25:8765/")
# driver.maximize_window()   #浏览器窗口最大化
# time.sleep(3)  #等待，默认秒，添加等待时间时，可以导入时间库
#智能等待--隐性等待
driver.implicitly_wait(10)
driver.get("http://erp.lemfix.com/")  #打开新的页面
driver.maximize_window()   #浏览器窗口最大化
#向前、退后、刷新
# driver.back()  #返回上一个页面
# time.sleep(3)
# driver.forward()   #前进到下一个页面
# time.sleep(3)
# driver.refresh()   #刷新页面
# driver.quit()    #退出，关闭驱动,session关闭
# driver.close()   #关闭当前的窗口，不会退出会话
# username = driver.find_element_by_id("username") #找到username这个id的元素，然后点击-->输入内容
# username.send_keys("test123")
u=driver.find_element_by_xpath("//input[@id='username']").send_keys("test123")
# #获取页面标题
# text_1=driver.find_element_by_xpath("//b[text()='柠檬ERP']").text
# print("这个页面标题是{}".format(text_1))
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("btnSubmit").click()

#获取当前用户
# user_now=driver.find_element_by_xpath("//div[@class='login-logo']//b").text
# print("当前登录的用户是{}".format(user_now))
#点击零售出库
chuku=driver.find_element_by_xpath("//span[text()='零售出库']").click()
# #搜索单据编号
#
# #切换iframe的方式
#通过找到这个元素--获取id属性--`
# p_id=driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
# f_id=p_id+"-frame"
# driver.switch_to.frame(f_id)
# driver.find_element_by_id("searchNumber").send_keys("314")

#通过元素定位xpath来切换frame
# p_id=driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
# f_id=p_id+"-frame"
# driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(f_id)))
# driver.find_element_by_id("searchNumber").send_keys("314")

#通过iframe下标来找 ：从0开始  html-页面==0，第一个宝宝==1，第二个宝宝==2
driver.switch_to.frame(1)
driver.find_element_by_id("searchNumber").send_keys("314")
#点击搜索按钮
driver.find_element_by_id("searchBtn").click()

time.sleep(2)
#找到单据的编号
num=driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
print(num)
if '314' in num:
      print("搜索结果是正确的")
else:
    print("用例测试不通过")