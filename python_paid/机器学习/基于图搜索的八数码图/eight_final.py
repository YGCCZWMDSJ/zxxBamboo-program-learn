"""
随机生成一个八数码问题分布，设计一个可解的目标状态（要求棋盘9个位置都不同）。
分别用广度优先搜索策略、深度优先搜索策略和至少两种启发式搜索算法求解八数码问题。

想法：
我想做一个用三个最优解出的玩法策略：
1-显示出文字型的，不要图像型
2-给选广、深度优先，把走的策略显示路径
3- 然后在版面上显示按钮（下一步），这样把走法显示出来

可能需要编写：
评估函数

"""
if __name__=="__main__":
    import random
    # 初始化
    board=[]
    rip_board={}
    def init_board():
        print('初始棋盘：')
        global board
        board=[[x for x in range(3)] for y in range(3)]
        a=1
        for i in range(3):
            for j in range(3):
                board[i][j]=a
                a+=1
        board[2][2]=0
        print(board)

    # 打乱棋盘
    def radom_board():
        print('打乱棋盘：')
        L=list(range(9))
        random.shuffle(L)
        global rip_board
        for i in range(3):
            for j in range(3):
                idx=i*3+j
                rip_board[board[i][j]]=L[idx]
        a=0
        for i in rip_board.keys():
            if i%3==0:
                end='\n'
            else:
                end=' '
            print(rip_board[i],end=end)
    # 广度优先搜索

    # 深度优先搜索
    # A
    # A*

    #main
    # 初始化
    init_board()
    # 打乱棋盘
    radom_board()
    # 广度优先搜索
    # 深度优先搜索
    # A
    # A*