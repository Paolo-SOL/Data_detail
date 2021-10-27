# import  pandas as pd
# str='uibgbbk'
# stt='danuxan'
# stt_arr=(str+stt)
#
# print(str)
# print(str)
# print(str[0])
# print(str[2:])
# print(len(stt_arr))
# print('uibgbbk\ndanuxan')
# print(r'hello\nW3Cschool')
# import pandas as pd
# import re
# mydata_txt = pd.read_csv("C:\\fontsize\\abox_workview1-www.w3cschool.cn-2021-10-15.log", sep='\t', encoding='utf-8')
# fo = open("C:\\fontsize\\abox_workview1-www.w3cschool.cn-2021-10-15.log")
# # f=fileObject.readline("C:\\fontsize\\abox_workview1-www.w3cschool.cn-2021-10-15.log");
# # print(f)
# # print(mydata_txt)
# print(fo)
# with open('C:\\fontsize\\abox_workview1-www.w3cschool.cn-2021-10-15.log') as f: # 默认模式为‘r’，只读模式
#     contents =f.read() # 读取文件全部内容
#     print(contents)
#     # 输出时在最后会多出一行（read()函数到达文件末会返回一个空字符，显示出空字符就是一个空行）
#     print('------------')
#     print(contents.rstrip())
#     # rstrip()函数用于删除字符串末的空白
# 显示内容
#
# file f = open("C:\\fontsize\\abox_workview1-www.w3cschool.cn-2021-10-15.log")
# # f = text.readlines("C:\\fontsize\\abox_workview1-www.w3cschool.cn-2021-10-15.log")
# # list2 = list(set(list1))
# print(f)
# 表格创建
# import csv
# rows=[[ '张三',123, ' abc'],['李四',456, 'xyz '],['王五',789, 'ij']]
# rows1=[ '张三123','李四456','王五789']
# # csv文件在写入的时候,黑认每次写入时会有一个空行作为分割,使用newline=""会把空行去掉
# with open('test1.csv', 'w', newline='')as csv_file:
#     writer = csv.writer(csv_file)
#     for row in rows:
#         writer.writerow(row)
# #写入多行
#     writer.writerows(rows)
#     writer1=csv.writer(csv_file)
#     for row1 in rows1:
#         writer1.writerow(row1)
# print(rows)
import csv
import re
import pandas as pd
import numpy as np
from collections import Counter
# ff = open('C:\\fontsize\\abox_workview1-www.w3cschool.cn-2021-10-15.log')
# C:\\fontsize\\abox_workview1-www.w3cschool.cn-2021-10-16.log
# ds = ff.readlines()
# sc = pd.Series(ds)
# item = []
# for i in sc:
#     ip = re.search(r"\d+.\d+.\d+.\d", i).group()
#     date = re.search(r"\d+/\w+/\d+:", i).group()[:-1]
#     time = re.search(r"\d+:\d+:\d+\s+", i).group()[:-1]
#     method = re.search(r"\"\w{3,}\s", i).group()[1:-1]
#     req = re.search(r"\s/\w*/\w*.*HTTP", i).group()[1:-5]
#     http = re.search(r"HTTP/1.1", i).group()
#     status = re.search(r"\s\d{3}", i).group()[1:]
#     page = re.search(r"\d{5,}", i)
#     if (page == None):
#         page = "NaN"
#     else:
#         page = page.group()
#     ua = re.search(r"\w{6,}/\d\.\d.*\"", i).group()[:-1]
#     array = [ip, date, time, method, req, http, status, page, ua]
#     item.append(array)
# item
# news_ids = []
# for id in item:
#     if id not in news_ids:
#         news_ids.append(id)
# print (news_ids)
# import csv
# import re
# import pandas as pd
# import numpy as np
# from collections import Counter
# # 导入创建文件函数
# # with open('C:\\fontsize\\abox_workview1-www.w3cschool.cn-2021-10-15.log') as f:
# #     list1 = f.readlines()
# #     sc = pd.Series(list1)
# #     sc.to_csv()
# #     d = list(set(sc))
# #     print(d)
# #     print("去重之后有：")
# #     print(csv.excel)
    # if x not in sc:
    #     newList.append(x)

# def unique(old_list):
#     newList = []
#     for x in old_list:
#         if x not in newList :
#             newList.append(x)
#     return newList
# old_list=list1
# print(old_list)



# 获取数据
#将数据去重导入表格
# def cleardata(l):
#     li = list(set(l))
#     print(lil)
# l=[1,1,22,21,222,2,22,33,33,3333,3333,444,4,4,4,5,5,5,5]
# cleardata(l)

    # print(list1)
    #
    # for i in f:
    #     df = pd.DataFrame(np.random.rand(i), idnex=[[i]],
    #                       columns=[range(i)])
    #     print(df)
    # fo = f.readlines()
    # d = Counter(f)
    # mao_a = map(list, f)
    # print(fo)
# df=pd.DataFrame(np.random.rand(i),idnex=[['id','url' ,'deress','sj','sja','hsan','rda']],columns=[range(i)])
# print(df)
#
# rows = [['', '', '','', '', '', '', '', '', '', '', '', '']]
# rows1 = pd.lines
# # csv文件在写入的时候,黑认每次写入时会有一个空行作为分割,使用newline=""会把空行去掉
# with open('test-4.csv', 'w', newline='')as csv_file:
#     writer = csv.writer(csv_file)
#     for row in rows:
#         writer.writerow(row)
# #写入多行
#     writer.writerows(rows)
#     writer1=csv.writer(csv_file)
#     for row1 in rows1:
#         writer1.writerow(row1)
# print(rows)

    # for i in lines:
    #     print(i)
    #     # 每行末尾会有一个换行符
    # print('------------')
# 此时文件已经读完，line2指向文本末尾，因此不会有输出

# with open('C:\\fontsize\\abox_workview1-www.w3cschool.cn-2021-10-15.log') as f:
#     lines = f.readlines()  # 读取文本中所有内容，并保存在一个列表中，列表中每一个元素对应一行数据
# print(lines)
# # 每一行数据都包含了换行符
# print('------------')
# for line in lines:
#     print
#     (line.rstrip())
# print('------------')
# pi_str = ''  # 初始化为空字符
# for line in lines:
#     pi_str += line.rstrip()  # 字符串连接
# print(pi_str)

# list1 = ['asd',':','00',':','24',' +','8000']
# kl=pd.Series(list1)
# kl.to_csv('klk.csv')
# # print(list1[:-2])
# # list2 = list(set(list1))
# # print(list2)
# print("ok")


from typing import List

# f = open("C:\\fontsize\\abox_workview1-www.w3cschool.cn-2021-10-15.log")
#list1 = f.readlines()
# # list2 = list(set(list1))
# # len(list2)
# print(list1)

# for i in y:
#     print(i)
# print(list2)
# print(list2)
# for i in list1:
#     print("数值："+i)
# list2 = list(set(list1))
# for y in list2:
#     print(y)
# import
# workbook = xlsxwriter.workbook('c:\\tex.xlsx ')
# worksheet = workbook.add_worksheet()
# for i in range(100):
#     worksheet.write(i, e, self.img_name)
#     #第i行e列
#     worksheet.write(i, 1, str(angle))
#     #第i行1列
# workbook.close()

# import xlwt
# work_book = xlwt.workbook(encoding=' utf-8')
# sheet = work_book.add_sheet('sheet表名')
# sheet.write(e, 0, '第一行第一列')
# sheet.write(e, 1, '第一行第二列')
# work_book.save(' Excel.xls ')
# book = xlwt.workbook()
#
# # 创建表单
# sheet = book.add_sheet(u'sheet1', cell_overwrite_ok=True)
# sheet.write(e, e, 'id')
# sheet.write(0, 1, 'text')
# sheet.write(e, 2, ' user_id ')
# sheet.write(e, 3, "geo_coordinates1 ")
# sheet.write(e, 4, 'geo_coordinates2 ')
# sheet.write(e, 5, ' created_at ')
# i = 1
# for All in searchRes:
#     sheet.write(i, 0, All['_id'])
#     sheet.write(i, 1, All['text'])
#     sheet.write(i, 2, All['user_id'])
#     sheet.write(i, 3, All['geo'][' coordinates '][0])
#     sheet.write(i, 4, All['geo']['coordinates '][1])
#     sheet.write(i, 5, All['created_at'])
#     i = i + 1
#     if i == 65530:
#         break
# book.save('Excel_workbook.xls ')

# 显示内容
#
# file f = open("C:\\fontsize\\abox_workview1-www.w3cschool.cn-2021-10-15.log")
# # f = text.readlines("C:\\fontsize\\abox_workview1-www.w3cschool.cn-2021-10-15.log")
# # list2 = list(set(list1))
# print(f)
# 表格创建
# import csv
# rows=[[ '张三',123, ' abc'],['李四',456, 'xyz '],['王五',789, 'ij']]
# rows1=[ '张三123','李四456','王五789']
# # csv文件在写入的时候,黑认每次写入时会有一个空行作为分割,使用newline=""会把空行去掉
# with open('test1.csv', 'w', newline='')as csv_file:
#     writer = csv.writer(csv_file)
#     for row in rows:
#         writer.writerow(row)
# #写入多行
#     writer.writerows(rows)
#     writer1=csv.writer(csv_file)
#     for row1 in rows1:
#         writer1.writerow(row1)
# print(rows)



import re
mm = "45.201.215.98 - - [15/Oct/2021:00:00:24 +0800] GET /memcached/memcached-clear-data.html?appfunction=vip&fcode=abox_workview1&vipPopup=1 HTTP/1.1 200 12981 https://www.w3cschool.cn/memcached/memcached-clear-data.html?appfunction=vip&fcode=abox_workview1&vipPopup=1" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)66.144.108.242"
s=re.search("\d+/\w+/\d+:",mm).group()
ret = re.search(r"\d+/\w+/\d+:", mm).group()
print(s)
print(ret)
