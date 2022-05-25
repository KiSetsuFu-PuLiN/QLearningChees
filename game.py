import players

players.rand.mod='human' #select rand's mod:{'random','human'}
players.Sarsa.mod='fighting' #select Sarsa's mod:{'fighting','learning'}

import numpy as np
class Chess():
    def __init__(self):
        self.location=[0,0]
    def show_selections(self):#返回这个棋子的选择列表
        selections=[]          #8,4,2,6==>up,left,down,right
        if self.location[0]==0:
            if self.location[1]==0:
                if plantform[1,0]==-1:
                    selections.append(2)
                if plantform[0,1]==-1:
                    selections.append(6)
                if plantform[1,1]==-1:
                    selections.append(3)
            elif self.location[1]==1:
                if plantform[0,0]==-1:
                    selections.append(4)
                if plantform[1,1]==-1:
                    selections.append(2)
                if plantform[0,2]==-1:
                    selections.append(6)
            elif self.location[1]==2:
                if plantform[0,1]==-1:
                    selections.append(4)
                if plantform[1,1]==-1:
                    selections.append(1)
                if plantform[1,2]==-1:
                    selections.append(2)
        elif self.location[0]==1:
            if self.location[1]==0:
                if plantform[0,0]==-1:
                    selections.append(8)
                if plantform[1,1]==-1:
                    selections.append(6)
                if plantform[2,0]==-1:
                    selections.append(2)
            elif self.location[1]==1:
                if plantform[0,0]==-1:
                    selections.append(7)
                if plantform[0,1]==-1:
                    selections.append(8)
                if plantform[0,2]==-1:
                    selections.append(9)
                if plantform[1,0]==-1:
                    selections.append(4)
                if plantform[1,2]==-1:
                    selections.append(6)
                if plantform[2,0]==-1:
                    selections.append(1)
                if plantform[2,1]==-1:
                    selections.append(2)
                if plantform[2,2]==-1:
                    selections.append(3)
            elif self.location[1]==2:
                if plantform[0,2]==-1:
                    selections.append(8)
                if plantform[1,1]==-1:
                    selections.append(4)
                if plantform[2,2]==-1:
                    selections.append(2)
        elif self.location[0]==2:
            if self.location[1]==0:
                if plantform[1,0]==-1:
                    selections.append(8)
                if plantform[1,1]==-1:
                    selections.append(9)
                if plantform[2,1]==-1:
                    selections.append(6)
            elif self.location[1]==1:
                if plantform[2,0]==-1:
                    selections.append(4)
                if plantform[1,1]==-1:
                    selections.append(8)
                if plantform[2,2]==-1:
                    selections.append(6)
            elif self.location[1]==2:
                if plantform[2,1]==-1:
                    selections.append(4)
                if plantform[1,1]==-1:
                    selections.append(7)
                if plantform[1,2]==-1:
                    selections.append(8)
        return selections 
    def move_to(self,x,y):
        global plantform
        index=plantform[self.location[0],self.location[1]]
        plantform[self.location[0],self.location[1]]=-1
        self.location[0],self.location[1]=x,y
        plantform[self.location[0],self.location[1]]=index
    def move(self,num):
        move_dict={
                1:(1,-1),
                2:(1,0),
                3:(1,1),
                4:(0,-1),
                6:(0,1),
                7:(-1,-1),
                8:(-1,0),
                9:(-1,1)
                }
        self.move_to(self.location[0]+move_dict[num][0],self.location[1]+move_dict[num][1])
def chess_reset():
    global plantform
    reset_locations=((0,0),(0,1),(0,2),(2,0),(2,1),(2,2))
    for i in range(len(reset_locations)):
        chess_list[i].location[0],chess_list[i].location[1]=reset_locations[i][0],reset_locations[i][1]
    plantform=np.array([[0,1,2],[-1,-1,-1],[3,4,5]])
def judge():
    if chess_list[0].location[0]==chess_list[1].location[0] and chess_list[0].location[0]==chess_list[2].location[0] and chess_list[0].location[0]!=0:
        return 'SarsaWin'
    if chess_list[0].location[1]==chess_list[1].location[1] and chess_list[0].location[1]==chess_list[2].location[1]:
        return 'SarsaWin'
    if chess_list[0].location[0]==chess_list[0].location[1] and chess_list[1].location[0]==chess_list[1].location[1] and chess_list[2].location[0]==chess_list[2].location[1]:
        return 'SarsaWin'
    if chess_list[0].location[0]==2-chess_list[0].location[1] and chess_list[1].location[0]==2-chess_list[1].location[1] and chess_list[2].location[0]==2-chess_list[2].location[1]:
        return 'SarsaWin'
    
    if chess_list[3].location[0]==chess_list[4].location[0] and chess_list[3].location[0]==chess_list[5].location[0] and chess_list[3].location[0]!=2:
        return 'randWin'
    if chess_list[3].location[1]==chess_list[4].location[1] and chess_list[3].location[1]==chess_list[5].location[1]:
        return 'randWin'
    if chess_list[3].location[0]==chess_list[3].location[1] and chess_list[4].location[0]==chess_list[4].location[1] and chess_list[5].location[0]==chess_list[5].location[1]:
        return 'randWin'
    if chess_list[3].location[0]==2-chess_list[3].location[1] and chess_list[4].location[0]==2-chess_list[4].location[1] and chess_list[5].location[0]==2-chess_list[5].location[1]:
        return 'randWin'
    return 'continue'
def plantform_format():
    global plantform,chess_list
    count_rand,count_Sarsa=3,0
    for x in range(3):
        for y in range(3):
            if plantform[x,y]<3 and plantform[x,y]>=0:  #Sarsa's
                plantform[x,y]=count_Sarsa
                chess_list[count_Sarsa].location=[x,y]
                count_Sarsa+=1
            elif plantform[x,y]>=3:  #rand's
                plantform[x,y]=count_rand
                chess_list[count_rand].location=[x,y]
                count_rand+=1

plantform=np.array([[0,1,2],[-1,-1,-1],[3,4,5]])
chess_list=[Chess() for i in range(6)]
chess_reset()
while True:
    for i in range(10000):
        #rand Round
        selections=[]
        for chess_num in range(3,6):
            selections.extend([(chess_num,i) for i in chess_list[chess_num].show_selections()])
        rand_selestion=players.rand.get_selection(plantform,selections)
        chess_list[rand_selestion[0]].move(rand_selestion[1])
        state=judge()
        if state=='randWin':
            players.rand.send_R(1)
            players.Sarsa.send_R(-1)
            chess_reset()
            print(state)
        #input(plantform)
    
        #Sarsa Round
        plantform_format()
        selections=[]
        for chess_num in range(0,3):
            selections.extend([(chess_num,i) for i in chess_list[chess_num].show_selections()])
        Sarsa_selestion=players.Sarsa.get_selection(plantform,selections)
        chess_list[Sarsa_selestion[0]].move(Sarsa_selestion[1])
        state=judge()
        if state=='SarsaWin':
            players.rand.send_R(-1)
            players.Sarsa.send_R(5)
            chess_reset()
            print(state)
        #input(plantform)
    players.Sarsa.Q.to_excel('Table.xls')
    print('学习进度已存入！')

