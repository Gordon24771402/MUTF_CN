import akshare as ak
from datetime import datetime


# 最大回撤
def max_drawdown(fCode, cPeriod=0, sDate='', eDate=''):
    """
    计算历史数据区间某基金的最大回撤
    :param fCode: 基金代码
    :param cPeriod: 区间长度（天）
    :param sDate: 开始日期（yyyy-mm-dd）
    :param eDate: 结束日期（yyyy-mm-dd）
    :return: 最大回撤（%）
    """
    # 排除非法参数： 1) cPeriod与(sDate或eDate)同时出现 2) 有sDate无eDate 3) 有eDate无sDate
    if (cPeriod and (sDate or eDate)) or (sDate and not eDate) or (eDate and not sDate):
        raise ValueError("Illegal Argument")
    # 用akshare获取：开放式基金-历史数据
    fInfo = ak.fund_em_open_fund_info(fund=fCode, indicator="单位净值走势")
    # 用cPeriod参数：选出历史数据区间
    if cPeriod:
        fInfo = fInfo[-cPeriod:].reset_index(drop=True)
    # 用sDate和eDate参数：选出历史数据区间
    elif sDate and eDate:
        sDate, eDate = datetime.strptime(sDate, "%Y-%m-%d").date(), datetime.strptime(eDate, "%Y-%m-%d").date()
        fInfo = fInfo.loc[(fInfo["净值日期"] >= sDate) & (fInfo["净值日期"] <= eDate)].reset_index(drop=True)
    # 计算历史数据区间的最大回撤
    maximumDrawdown = 0
    for i in range(len(fInfo) - 1):
        for j in range(i + 1, len(fInfo)):
            drawdown = (fInfo["单位净值"][i] - fInfo["单位净值"][j]) / fInfo["单位净值"][i]
            if drawdown > maximumDrawdown:
                maximumDrawdown = drawdown
    return "{:.2%}".format(maximumDrawdown)


# 击败基准比率
def benchmark_ratio(fCode, cPeriod=0, sDate='', eDate=''):
    # 排除非法参数： 1) cPeriod与(sDate或eDate)同时出现 2) 有sDate无eDate 3) 有eDate无sDate
    if (cPeriod and (sDate or eDate)) or (sDate and not eDate) or (eDate and not sDate):
        raise ValueError("Illegal Argument")
    # 用akshare获取：开放式基金-历史数据
    fInfo = ak.fund_em_open_fund_info(fund=fCode, indicator="单位净值走势")
    # 用cPeriod参数：选出历史数据区间
    if cPeriod:
        fInfo = fInfo[-cPeriod:].reset_index(drop=True)
    # 用sDate和eDate参数：选出历史数据区间
    elif sDate and eDate:
        sDate, eDate = datetime.strptime(sDate, "%Y-%m-%d").date(), datetime.strptime(eDate, "%Y-%m-%d").date()
        fInfo = fInfo.loc[(fInfo["净值日期"] >= sDate) & (fInfo["净值日期"] <= eDate)].reset_index(drop=True)



# print(benchmark_ratio("005888", cPeriod=180))
stock_zh_index_daily_df = ak.stock_zh_index_daily(symbol="sh000300")
print(stock_zh_index_daily_df)
