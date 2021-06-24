import akshare as ak
from datetime import datetime


# 最大回撤
def max_drawdown(fCode, cPeriod=0, sDate='', eDate=''):
    # 排除非法参数 1) cPeriod与(sDate或eDate)同时出现 2) 有sDate无eDate 3) 有eDate无sDate
    if (cPeriod and (sDate or eDate)) or (sDate and not eDate) or (eDate and not sDate):
        raise ValueError("Illegal Argument")

    fInfo = ak.fund_em_open_fund_info(fund=fCode, indicator="单位净值走势")
    if cPeriod:
        fInfo = fInfo[-cPeriod:]
    elif sDate and eDate:
        sDate, eDate = datetime.strptime(sDate, "%Y-%m-%d").date(), datetime.strptime(eDate, "%Y-%m-%d").date()
        fInfo = fInfo.loc[(fInfo["净值日期"] >= sDate) & (fInfo["净值日期"] <= eDate)]



max_drawdown(fCode="002083", sDate="2021-06-15")

