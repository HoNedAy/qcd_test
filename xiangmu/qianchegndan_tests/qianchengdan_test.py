#
from selenium import webdriver

def fangwen_web_page(url,mobilephone,driver,password):
    driver.get(url)
    driver.maximize_window()
    login_button=driver.find_element_by_xpath("//a[text()='登录']") #找到登录按钮
    login_button.click();  #点击登录
    phone=driver.find_element_by_name("phone").send_keys(mobilephone)#找到手机号元素并输入手机号
    password=driver.find_element_by_name('password').send_keys(password)
    button=driver.find_element_by_xpath("//button[text()='登录']")
    button.click()  #点击登录
    driver.implicitly_wait(5)
    zhanhu=driver.find_element_by_xpath("//div[@class='right fs-12']//span[3]")
    zhanhu.click()
    chasename=driver.find_element_by_xpath("//img[@id='modify_regname']")
    chasename.click()
    find_text=driver.find_element_by_xpath("//div[@class='layui-layer-content']//div[1]//input")  #得到input框
    find_text.clear()  #清空文本框里面的内容
    find_text.send_keys("1234656x") #重新输入昵称
    find_queding_button=driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()

    # find_text_reshuru=find_text.get_attribute("value")=="砂浆回复过圣诞节"

    print()



def serach_number(url,mobilephone,driver,password):  #访问所有的函数
    print(url)
    fangwen_web_page(url,mobilephone,driver,password)