
import time
def login_page(username,password,driver):  #传参方式--形参--登录的函数
    driver.find_element_by_xpath("//input[@id='username']").send_keys(username)#获取文本框并输入用户名
    driver.find_element_by_id("password").send_keys(password) #获取文本框并输入密码
    driver.find_element_by_id("btnSubmit").click()  #点击登录按钮

def open_url(url,driver):  #封装打开网页地址的函数
    driver.get(url)  # 打开新的页面
    driver.maximize_window()  # 浏览器窗口最大化

def search_key(url,driver,username,password,s_key):
    open_url(url,driver)  #调用打开浏览器的函数
    login_page(username,password,driver)#调用登录的函数、#点击零售出库
    chuku=driver.find_element_by_xpath("//span[text()='零售出库']").click()
    p_id=driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
    f_id=p_id+"-frame"
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(f_id)))
    driver.find_element_by_id("searchNumber").send_keys(s_key)
    #点击搜索按钮
    driver.find_element_by_id("searchBtn").click()

    time.sleep(2)
    #找到单据的编号
    num=driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return num  #返回搜索结果