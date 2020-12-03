#接口自动化步骤
# 1、excel测试用例准备好，代码自动读取数据
# 2、发送接口请求，得到响应结果
# 3、执行结果 vs预期结果  --断言  通过 不通过
# 4、写入最终的真实结果--execl表格里
#
# 第三方库：操作excel表格--openpyxl库，实现去excel表格里读取数据，数据的回写
# 1.安装：pip install openpyxl==或pycharm安装
# 2、导入 import openpyxl

# 注意：execl表格要跟python文件在同一级别
# execl表格三大对象：
# 1、工作簿对象
# 2、表格对象：sheet
# 3、单元格对象：cell
# print("kjhjk")   #单元格里面的内容
# import openpyxl
# wb1=openpyxl.load_workbook('jiekou.xlsx')  #加载工作簿--execl表格名字--内存
# # sheet=wb1["register"]
# #获取表单
# print(wb1.cell(1,0))
# cell=sheet.cell(row=1,column=1)  #通过表单获取行号、列号==单元格
# print("kjhjk")   #单元格里面的内容


