import akshare as ak
from datetime import datetime


# 最大回撤
def max_drawdown(fCode, cPeriod=0, sDate='', eDate=''):
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


print(max_drawdown(fCode="001300", cPeriod=180))
print(max_drawdown(fCode="002083", cPeriod=180))
print(max_drawdown(fCode="161725", cPeriod=180))
print(max_drawdown(fCode="005888", cPeriod=180))
print(max_drawdown(fCode="009777", cPeriod=180))
