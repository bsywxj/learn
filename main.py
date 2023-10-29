# 找一个网址 以字符串的形式保存在一个变量中！
# url = "https://v26-web.douyinvod.com/351620a280feb6dc9002423f7a76fa5a/63d7cbeb/video/tos/cn/tos-cn-ve-15/owmt7LiA9okAJNfbClQg4znjYIueDAmwBgiAAs/?a=6383&ch=54&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=998&bt=998&cs=0&ds=3&ft=LjhJEL998xIouEkmD0P5H4eaciDXtks0d5QEeg-czijD1Ini&mime_type=video_mp4&qs=0&rc=ZDM5aTY1ZjRpM2U7PDZnOkBpanc6OjQ6ZjxqaDMzNGkzM0BjMS4yNmA1NTUxYzY2XzRfYSNvYTA2cjRnLW1gLS1kLWFzcw%3D%3D&l=202301302053005280D9206CC8081A59C4&btag=20000"
#
# 导入请求模块 一定要先安装！
# # import requests
# #
# 使用requests的get功能 获取网站的响应
# # res = requests.get(url)
# #
# 打开一个空的视频(真·狗粮.mp4) 把得到res.content丢进去 得到一个可以播放的视频
# # open('美女1.mp4', 'wb').write(res.content)
# # import pandas as pd
# # df =pd.read_excel("D:\三菱.xlsx")
# # print(df)
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True) # 规整格式
data=['李光地','张宏仁','王鹏']
s=pd.Series(data=data, index=[1,2,3])
print(s)
print(type(s))
#列表方式创建dataframe
data1=[["小太阳",320.9,100],["鼠标",150.3,50],["小刀",1.5,200]]
columns=["名称","单价","数量"]
df=pd.DataFrame(data=data1,columns=columns,index=[1,2,3])
print(df)
print(type(df))
#字典方式创建dataframe
data2={
    "名称":["小太阳","鼠标","小刀"],
    "单价":[320.9,150.3,1.5],
    "数量":[100,50,200]
}
df2=pd.DataFrame(data=data2)
print(df2)
df3=pd.read_csv('F:\BaiduNetdiskDownload\数据分析学习资料\书籍+随堂源码+说明\sample_code\data\HR.csv',sep=',',encoding='utf-8')
print(df3)

url='https://www.espn.com/nba/salaries'
df4=pd.DataFrame()
# df4=pd.append(pd.read_html(url))
df5=pd.append(pd.read_html(url,header=0))
print(df5)

data =[[110,105,99],[185,88,115],[109,120,138]]
columns =['chinese','math','engL1sh']
index=['王','张','李']
df =pd.DataFrame(data=data,index=index,columns=columns)
df1=pd.DataFrame({'chinese':[100,123,138],'math':[99,142,60],'engLish':[98,139,99]})
df2 =pd.concat([df,df1])
print(df2)
