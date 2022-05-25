mod='human' #or 'random'

import random,time
random.seed(time.gmtime())
def get_selection(plantform,selections):
    if mod=='random':
        return selections[random.randint(0,len(selections)-1)]
    elif mod=='human':
        chesses=[]
        for x in range(3):
            for y in range(3):
                if plantform[x,y]==-1:
                    chesses.append(0)
                elif plantform[x,y]<3:
                    chesses.append(1)
                else:
                    chesses.append(plantform[x,y])
        chesses=iter(chesses)
        print(f'{next(chesses)}-{next(chesses)}-{next(chesses)}')
        print(r'|\|/|')
        print(f'{next(chesses)}-{next(chesses)}-{next(chesses)}')
        print(r'|/|\|')
        print(f'{next(chesses)}-{next(chesses)}-{next(chesses)}')

        num=0
        move_dict={
                1:'左下',
                2:'下',
                3:'右下',
                4:'左',
                6:'右',
                7:'左上',
                8:'上',
                9:'右上'
                }
        for selection in selections:
            num+=1
            print(f'{selection[0]}号棋子，{move_dict[selection[1]]}----{num}')
        return selections[eval(input('Select your action\'s index (input the index):'))-1]
def send_R(R):
    if mod == 'human':
        if R==-1:
         print('You lost!')
        elif R==1:
            print('You win!')
        else:
            pass
