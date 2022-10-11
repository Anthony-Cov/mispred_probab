import pandas as pd
import numpy as np
'''Счёт неделям'''
def getweeks(fdates):
    dati=pd.to_datetime(fdates)
    yearweek=[]
    for dy in dati.year.unique():
        year=dati[dati.year==dy]
        week=(dati[dati.year==dy].dayofyear.values//7)
        week=np.char.zfill(np.where(week<=51, week, 51).astype(str),2)
        yearweek+=list(year.year.astype(str) +'-'+ week)
    return yearweek   

'''Линейное укладывание в диапазон [0,1], возвращает коэффициенты для восстановления (max(X))!=0'''
def Norm01(x):
    mi=np.nanmin(x)
    ma=np.nanmax(np.array(x)-mi)
    if ma>0.:
        x_n=(np.array(x)-mi)/ma
        return x_n, mi, ma
    else:
        return np.zeros(len(x)), mi, ma
'''Восстановление'''
def Nback(x_n, mi, ma):
    return x_n*ma+mi

'''Наименьшие квадраты для одной переменной'''
def MLS(x,y):
    x=np.array(x).astype(float)
    y=np.array(y).astype(float) 
    n=len(x)
    sumx, sumy=sum(x), sum(y)
    sumx2=sum([t*t for t in x])
    sumxy=sum([t*u for t,u in zip(x,y)])
    a = (n * sumxy - (sumx * sumy)) / (n * sumx2 - sumx * sumx);
    b = (sumy - a * sumx) / n;
    return a, b 

'''скользящее среднее'''
def  MovingAverage(x, numb=10):
    n=len(x)//numb
    ma=list(x[:n])
    for j in range(len(x)-n):
        ma.append(np.mean(x[j:j+n]))
    return np.array(ma)

'''Подсчет метрик: x-модель, y-реальность; выход - ошибки:средняя, абс. средняя, процентная, СКО'''
def Metr(x,y):
    y=np.array(y)
    x=np.array(x)
    d=x-y
    m=np.mean(d)
    d1=np.mean(abs(d))
    d2=sum([abs(d[i]/y[i]) for i in range(len(y)) if y[i]!=0])/len([y[i]for i in range(len(y)) if y[i]!=0 ])*100
    d3=sum([abs(d[i]/(x[i]+y[i])*2) for i in range(len(y)) if (x[i]+y[i])!=0])/len([y[i]
                                                        for i in range(len(y)) if (x[i]+y[i])!=0 ])*100
    d4=np.std(d)
    return m, d1, d2, d3, d4


'''Секунды в строку ЧЧ:ММ:СС, на входе скалярно'''
def seconds_to_str(seconds):
    mm, ss = divmod(seconds, 60)
    hh, mm = divmod(mm, 60)
    return "%02d:%02d:%02d" % (hh, mm, ss)

'''Наименьшие квадраты для одной переменной'''
def MLS(x,y):
    x=np.array(x).astype(float)
    y=np.array(y).astype(float) 
    n=len(x)
    sumx, sumy=sum(x), sum(y)
    sumx2=sum([t*t for t in x])
    sumxy=sum([t*u for t,u in zip(x,y)])
    a = (n * sumxy - (sumx * sumy)) / (n * sumx2 - sumx * sumx);
    b = (sumy - a * sumx) / n;
    return a, b

