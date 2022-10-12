# -*- coding : utf-8 -*-
# @Time      : 2022/9/10 13:57
# @Author    : Zong
# @File      : Fund.py
# @Software  : PyCharm
# @Function  : 
# @ChangeLog :

# 策略
# 1、观察大盘走向（低买高卖）
# 2、根据新闻和生活判断发展方向
# 3、观察发展方向相关的主题基金
# 4、比较大盘和主题基金（主题溢价？）
# 5、比较主题相关基金（40%管理者，30%价格波动，20%板块企业，10%分红）

import akshare as ak
import datetime
import mplfinance as mpf
import BasicFund
import Config
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc("font", family='YouYuan')
plt.rcParams['axes.unicode_minus'] = False


# 1、观察大盘走向（低买高卖）
def step1():
    BasicFund.BasicFund(fund1_id="519300", fund1_name='沪深300', fund2_id="000962", fund2_name='天弘中证500', date_during=365*3, canvas_name=Config.imgs_path+"BasicFund_3year")
    BasicFund.BasicFund(fund1_id="519300", fund1_name='沪深300', fund2_id="000962", fund2_name='天弘中证500', date_during=365*1, canvas_name=Config.imgs_path+"BasicFund_1year")
    BasicFund.BasicFund(fund1_id="519300", fund1_name='沪深300', fund2_id="000962", fund2_name='天弘中证500', date_during=30, canvas_name=Config.imgs_path+"BasicFund_1month")

step1()

# 2、根据新闻和生活判断发展方向（自己心里清楚）

# 3、观察发展方向相关的主题基金（自己在蚂蚁财富上看）

# 4、比较大盘和主题基金

# 5、比较主题相关基金（回复基金序号，由程序判断）
