#封装函数
def login_pg(username,password,driver):
    driver.find_element_by_xpath("//input[@id='username']").send_keys("test123")
    driver.find_element_by_id("password").send_keys("123456")
    driver.find_element_by_id("btnSubmit").click()

def open_page(url,driver):
    driver.get(url)  # 打开新的页面
    driver.maximize_window()  # 浏览器窗口最大化

def derach(url,username,password,driver):
    open_page(url,driver)
    login_pg(username,password,driver)