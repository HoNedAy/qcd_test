# # 1、安装requests库
# import requests  #导入库  除了url，其他都要使用字典来进行传递
# import jsonpath
# #jsonpath滴第三方库
# #requests==请求
# #http协议===请求--响应模式
# #注册请求
# #封装函数
# lo_url='http://120.78.128.25:8766/futureloan/member/login' #请求地址
# da_reg = {"mobile_phone": "15815541763", "pwd": "lemon123456"}
# def login_data(url,da_r):
#     headers_data={'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json'} #请求头部信息
#     #返回来的响应结果
#     res=requests.post(url=url,json=da_r,headers=headers_data)  #post方法把参数都传进去
#     reponse=res.json() #查看json格式的响应结果
#     print(reponse)
#     return reponse
# result=login_data(lo_url,da_reg)
# print(result)


# #充值接口
# #取值方法一：
# member_id=result['data']['id']#字典嵌套的取值方式
# # tonken_id=reponse['data']['token_info']['token'] #取到tonken的值
# # print(member_id,tonken_id)
# #取值方法二：jsonpath--
# tonken_id=jsonpath.jsonpath(result,'$..token')[0]  #$--代表是最外层的括号  ..匹配任意数据，递归搜索
# rec_url='http://120.78.128.25:8766/futureloan/member/recharge'#输入充值地址
# rec_heaher={'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json','Authorization':'Bearer '+tonken_id} #充值请求头
# rec_data={ "member_id": member_id, "amount": 6300 }
# print(tonken_id)
# res=requests.post(url=rec_url,json=rec_data,headers=rec_heaher)  #post方法把参数都传进去
# reponse=res.json() #查看json格式的响应结果
# print(reponse)
#
#
# #百度接口请求
# #输入接口地址
# ba_url='https://www.baidu.com/'
# hes={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
# res=requests.get(url=ba_url,headers=hes)
# txt=res.content.decode()
# print(txt)
#
#
#


import requests  #导入安装好的requests库使用
import jsonpath #导入安装好的jsonpath库使用

#把登录接口封装成函数
def login_fuc(l_url,l_data):
    # 请求头部信息--字典的方式
    login_head = {'X-Lemonban-Media-Type': 'lemonban.v2', 'Content-Type': 'application/json'}
    # 传参方式--响应方式--有严格的传参方式，第一个是必备参数，第二、第三是默认参数（data和json格式），最后一个是**kwargs不定长参数
    # 要定义一个变量，用来存储返回过来的响应结果
    # 返回来的响应结果看看是什么格式，然后利用什么格式进行查看（json,text格式）  headers
    res_1 = requests.post(url=l_url, json=l_data, headers=login_head)
    res_2 = res_1.json()
    return res_2
# 填写接口请求地址--登录请求地址
url = 'http://120.78.128.25:8766/futureloan/member/login'
# 请求的参数体--字典方式
login_data = {"mobile_phone": "15815541764", "pwd": "lemon123456"}
#调用函数并进行传参,并返回一个结果
reponse=login_fuc(url,login_data)
print(reponse)

#充值接口请求--要取到token值
#取tonken值方法一===字典的取值方式
# token_1=reponse['data']['token_info']['token']
#取tonken值方法二===jsonpath取值方式--要安装jsonpath库，然后导入 import jsonpath才能运用
#因为取出来的值会以列表的形式存在，所以可以允许有多个值存在，后面想取哪一个就用[索引]进行取值
#两种方式：$..token  或者$.data.token_info.token-------#$--代表是最外层的括号  ..匹配任意数据，递归搜索
token_1=jsonpath.jsonpath(reponse,'$..token')[0]
#取member_id的值
member_id=reponse['data']['id']
print(token_1,member_id)
#充值请求地址
rec_url='http://120.78.128.25:8766/futureloan/member/recharge'
#充值请求头部信息
rec_head={'X-Lemonban-Media-Type':'lemonban.v2',
          'Content-Type':'application/json',
          'Authorization':'Bearer '+token_1}
#充值请求参数体
rec_data={"member_id": member_id, "amount": 6200}
#请求方式==响应结果--返回是一个对象
result=requests.post(url=rec_url,json=rec_data,headers=rec_head)
#以json格式进行查看
result_res=result.json()
print(result_res)


#百度接口请求地址，如果没有传相应的User-Agent,会被误认为是恶意攻击的请求
baidu_url='https://www.baidu.com/'
baidu_head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
#get请求--返回响应结果,有时返回的结果乱码
result=requests.get(url=baidu_url,headers=baidu_head)
#一、获取响应结果的内容--自动解码--80% ok
# res=result.text
#二、手动指定解码格式  utf8
res=result.content.decode()
print(res)



