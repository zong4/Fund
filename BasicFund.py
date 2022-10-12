# -*- coding : utf-8 -*-
# @Time      : 2022/9/11 16:55
# @Author    : Zong
# @File      : BasicFund.py
# @Software  : PyCharm
# @Function  : 
# @ChangeLog :

import akshare as ak
import datetime
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc("font", family='YouYuan')
plt.rcParams['axes.unicode_minus'] = False


def BasicFund(fund1_id, fund1_name, fund2_id, fund2_name, date_during, canvas_name):
    # 画布
    canvas = plt.figure(figsize=(16, 10))

    # 单位净值图
    figure1 = canvas.add_subplot(211)
    figure1.set_ylabel('单位净值')
    figure1.set_xlabel('日期')

    # 519300 沪深300
    fund_hushen300 = ak.fund_open_fund_info_em(fund=fund1_id, indicator="单位净值走势")
    print(fund_hushen300)

    # 起始日期
    date_len = len(fund_hushen300)
    date_start = date_len - date_during
    if date_start < 0:
        date_start = 0

    # 提取净值数据
    fund_hushen300_date = fund_hushen300["净值日期"][date_start : date_len]
    fund_hushen300_price_data = fund_hushen300["单位净值"][date_start : date_len]

    # 添加净值数据
    figure1.plot(fund_hushen300_date, fund_hushen300_price_data, label=fund1_name + "单位净值")

    # 000962 天弘中证500
    fund_tianhongzhongzheng500 = ak.fund_open_fund_info_em(fund=fund2_id, indicator="单位净值走势")

    # 起始日期
    date_len = len(fund_tianhongzhongzheng500)
    date_start = date_len - date_during
    if date_start < 0:
        date_start = 0

    # 提取净值数据
    fund_tianhongzhongzheng500_date = fund_tianhongzhongzheng500["净值日期"][date_start : date_len]
    fund_tianhongzhongzheng500_price_data = fund_tianhongzhongzheng500["单位净值"][date_start : date_len]

    # 添加净值数据
    figure1.plot(fund_tianhongzhongzheng500_date, fund_tianhongzhongzheng500_price_data, label=fund2_name + "单位净值")

    # 完成绘图
    plt.title('基金单位净值大盘')
    plt.legend(loc='upper left')

    # 累计净值图
    figure2 = canvas.add_subplot(212)
    figure2.set_ylabel('累计净值')
    figure2.set_xlabel('日期')

    # 519300 沪深300
    fund_hushen300 = ak.fund_open_fund_info_em(fund=fund1_id, indicator="累计净值走势")

    # 起始日期
    date_len = len(fund_hushen300)
    date_start = date_len - date_during
    if date_start < 0:
        date_start = 0

    # 提取净值数据
    fund_hushen300_date = fund_hushen300["净值日期"][date_start : date_len]
    fund_hushen300_price_data = fund_hushen300["累计净值"][date_start : date_len]

    # 添加净值数据
    figure2.plot(fund_hushen300_date, fund_hushen300_price_data, label=fund1_name + "累计净值")

    # 000962 天弘中证500
    fund_tianhongzhongzheng500 = ak.fund_open_fund_info_em(fund=fund2_id, indicator="累计净值走势")

    # 起始日期
    date_len = len(fund_tianhongzhongzheng500)
    date_start = date_len - date_during
    if date_start < 0:
        date_start = 0

    # 提取净值数据
    fund_tianhongzhongzheng500_date = fund_tianhongzhongzheng500["净值日期"][date_start : date_len]
    fund_tianhongzhongzheng500_price_data = fund_tianhongzhongzheng500["累计净值"][date_start : date_len]

    # 添加净值数据
    figure2.plot(fund_tianhongzhongzheng500_date, fund_tianhongzhongzheng500_price_data, label=fund2_name + "累计净值")

    # 完成绘图
    # plt.title('基金累计净值大盘')
    plt.legend(loc='upper left')
    plt.savefig(canvas_name + '.png', bbox_inches='tight')