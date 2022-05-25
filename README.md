players是存放玩家行为（rand.py）和Sarsa行为（Sarsa.py）的包  
Table.xls是一个表格，存放了Sarsa的训练数据，删除它就可以让Sarsa回到最初的状态  
game.py是main程序，在其中可以设置Sarsa与rand的行为模式（mod）  
	random：rand进行随机输出  
	human：由用户接管rand的输出  
	fighting：Sarsa将直接选择以往经验中的最优行动  
	learning：Sarsa有几率（epsilon=10%）选择随机行动  
人均决策1万次后将进行一次存档（更新Table.xls）  
Sarsa.py中可以修改学习相关的数值：  
	alpha：学习效率  
	gamma：Q值（选项的价值）的递归衰减率  
	epsilon：learning mod下的随机选择概率  
