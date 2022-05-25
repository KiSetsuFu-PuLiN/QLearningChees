mod='learning' #or 'fighting'
alpha=.9
gamma=.4
epsilon=.1



R_real=0
import random,time,pandas as pd,numpy as np
random.seed(time.gmtime())

latest_plantform=''
latest_selection=''

#pd.DataFrame([]).to_excel('Table.xls')  #Q_init


Q=pd.read_excel('Table.xls',index_col=0,header=0)

def get_selection(plantform,selections):    #更新R值并返回最优选项
    global R_real,Q,latest_plantform,latest_selection
    plantform=str(plantform)
    selections=[str(selection) for selection in selections]
    #对新接受的选项进行写入Q表
    if plantform not in Q.index: #The unknown
        for selection in selections:
            Q.loc[plantform,selection]=0
    else:                           #The known
        pass
    #选择最优选项索引
    Q_max_selection_key=selections[0]
    for selection in selections[1:]:
        if Q.loc[plantform,selection]>Q.loc[plantform,Q_max_selection_key]:
            Q_max_selection_key=selection
    #更新R值
    if latest_plantform=='':      #The begin，不更新R
        pass
    else:                           #The midle，更新R
        if abs(Q.loc[latest_plantform,latest_selection])<100000000:
            Q.loc[latest_plantform,latest_selection]+=alpha*(R_real+gamma*Q.loc[plantform,Q_max_selection_key]-Q.loc[latest_plantform,latest_selection])

    #'learning' mod
    if mod=='learning':
        if random.random()<epsilon:
            latest_selection=selections[random.randint(0,len(selections)-1)]
    #更新指针    
    latest_selection=Q_max_selection_key
    latest_plantform=plantform
    
    #print(Q)
    
    R_real=0    
    #Q.to_excel('Table.xls')
    return eval(latest_selection)
def send_R(R):
    global R_real
    R_real+=R


