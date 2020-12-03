# # 1、常用类型 整型int 浮点型 float 布尔型bool 字符串str
# # 2、内置函数
# # print()
# # type()
# # isinstance()
# print("不要再想那么多了")
# print(type(12))
# print(isinstance("fgf",str))
#
# # 切片取值，获取字符串[开始索引:结束索引:步长]步长为负数时是倒着取值
# str="今天你认真学习了吗"
# print(str[1:len(str):2])
# #替换的内置函数.replace(旧值，新值)--替换后要重新赋值才可以更新成功
# str="还不赶紧找工作"
# str2=str.replace("找工作","找高薪工作")
# print(str2)

#格式化输出{}--搭配.format()使用---随意输入值
# height=input()
# # weight=input()
# # age=input()
# # gongzi=8000
# # name="皮卡丘"
# # print(
# #     '''
# #  ----{1}的 名字
# #  身高：{1}
# #  体重：{2}
# #  年龄：{3}
# #  工资：{0}'''.format(name,height,weight,age,gongzi)
# # )
# #算术运算符：+——*/加减乘除
# # print(10+90)
# # print("你好"+"袁冰妍")
# # print(str(12)+"袁冰妍好可爱")
# # print(10/2)
# #
# # #比较运算符：> >= < <= == !=
# # #赋值运算符：= += -=
# # #逻辑运算符：and(与) or(或) not(非)
# # # 成员运算符：in not in
# # tr2="adasd"
# # print("f" in tr2)
#
# #列表list [] 元素可重复 有顺序
# list1=["袁冰妍","成毅粉一生黑","成毅一生黑"]
# print(list1[0:len(list1):1])
# print(list1.count("袁冰妍"))
# #增加--append()--末尾增加--是以列表的行驶证增加
# list1.append(["尾巴"])
# print(list1)
# #insert--指定位置加入
# list1.insert(0,"首位")
# print(list1)
# #extend---多个数据增加---不是以列表的形式增加
# list1.extend(["成毅一生黑1"])
# print(list1)
# #添加多个元素--以列表的形式增加--在末尾增加----这个方法用的最多
# list1.append(["zengjiav","akfjhd"])
# print(list1)
#
# #####删除--pop()--删除最后一个元素--指定位置删除    remove()--指定元素删除    clear()---删除所有
# # list1.pop()
# # print(list1)
# # list1.remove("首位")
# # print(list1)
# # list1.pop(3)
# # print(list1)
# # list1.clear()
# # print(list1)
# ###修改
# # list1[0]="首位1" #没有这个元素就增加，有就修改
# # print(list1)

#元组--元素不能被改变--也就是不能进行增加修改--如果要修改  可以转换成列表
# tuple1=("你好","冰研","冰淇淋")
# # print(tuple1)
# # #增加
# # del tuple1
# # # print(tuple1)

#字典{}---键值对出现---增删改
# dict_1={"name":"袁冰妍","height":"167"}
# print(dict_1)
#增+修改--根据key值
# dict_1["hobby"]="演戏"
# print(dict_1)
# dict_1["hobby1"]="跳舞"
# print(dict_1)
# dict_1.update({"name1":"hahah","gender":"jifjg"})  #可修改多个元素
# print(dict_1)
# #删除
# dict_1.pop("hobby")  #指定删除
# print(dict_1)
# print(dict_1["hobby1"])
# print(dict_1.get("name1"))

#集合--无序，给列表去重
# list1=["skjgfh","1","1","2"]
# l=set(list1)
# l=list(l)
# print(l)


#控制流----if else
# money=int(input("输入工资"))
# if money==9000:
#     print("吃好吃的")
# elif money>10000:
#     print("工资还不错")
# else:
#     print("继续努力学习")

#for循环--中断循环  ------continue---中断当前循环  break:跳出循环
# str="袁冰妍你真好看，好喜欢你，我一定会去见你的"
# count=0  #---可以统计总数
# for item in str:
#     if (item=="冰"):
#         continue
#     if (item=="妍"):
#         break
#     print(item)

#range(,,,)--新建一个整数序列
# for i in range(0,10,3):  #取出偶数
# #     print(i)
# list1 = ['方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝']
# list4 = ['male', 'male', 'female', 'male', 'female', 'male']
# list5 = [18,19,20,21,22,23]
# list6 = ['广州', '深圳', '上海', '长沙', '北京', '东莞']
# # 列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。
# # 并且把字典都存在新的 list中，最后打印最终的列表。
# # kist1=[]
# # # for item in range(6):
# # #     result=dict(name=list1[item],sex=list4[item],age=list5[item],city=list6[item])
# # #     kist1.append(result) #将字典存入空列表里面
# # # print(kist1)