"""
随机生成一个八数码问题分布，设计一个可解的目标状态（要求棋盘9个位置都不同）。
分别用广度优先搜索策略、深度优先搜索策略和至少两种启发式搜索算法求解八数码问题。

想法：
我想做一个用三个最优解出的玩法策略：
1-显示出数字游戏版面
2-给选广、深度优先，把走的策略显示路径
3- 然后在版面上显示按钮（下一步），这样把走法显示出来

可能需要编写：
评估函数

"""

if __name__ == "__main__":
    bCut = 0

    # if bCut == 1:

    from tkinter import *
    from tkinter.messagebox import *
    import random

    root = Tk('八数码问题')
    root.title("八数码问题")
    
    # 数字文字
    Num = [x for x in range(1,9)]
    # 画布尺寸
    WIDTH = 600
    HEIGHT = 600
    # 图像块边长
    IMAGE_WIDTH = WIDTH // 3
    IMAGE_HEIGHT = HEIGHT // 3

    # 棋盘行列数
    ROWS = 3
    COLS = 3
    # 移动步数
    steps = 0
    # 保存所有块的列表(正常序列，但是题目貌似不是正常序列)
    board = [
        [0,1,2],
        [3,4,5],
        [6,7,8]
    ]

    # 数字块类
    class numberBlock:
        def __init__(self,orderID):
            self.orderID=orderID

        def draw(self,canvas,board_pos):
            number=Num[self.orderID]
            canvas.create_text(board_pos,text=number,font=("Helvetica",24),fill="black")
            
    # 初始化拼图版
    def init_board():
        # 打乱数字块坐标(老师给的那个和文档那个初始不一样，这个可能要自己最后调成那样子的)
        L = list(range(8))
        L.append(None)
        random.shuffle(L)
        # 填充拼图版
        for i in range(ROWS):
            for j in range(COLS):
                idx=i*ROWS+j
                orderID=L[idx]
                if orderID is None:
                    board[i][j]=None #为None时为空格
                else:
                    board[i][j]=numberBlock(orderID)

    #重置游戏
    def play_game():
        global steps
        steps = 0
        init_board()

    # 貌似只是给个八数码图，似乎不用显示？
    def drawBoard(canvas):
        # 画黑框
        canvas.create_polygon((0,0,WIDTH,0,WIDTH,HEIGHT,0,HEIGHT))
        #画图像块
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] is not None:
                    board[i][j].draw(canvas,(IMAGE_WIDTH*(j+0.5),IMAGE_HEIGHT*(i+0.5)))

    
    # 重新开始回滚
    def callBack2():
        print("重新开始")
        play_game()
        cv.delete('all')# 清除canvas画布上的内容
        drawBoard(cv)

    # 设置窗口
    cv = Canvas(root,bg='green',width=WIDTH,height=HEIGHT)
    b1 = Button(root,text="重新开始",command=callBack2,width=20)
    drawBoard(cv)
    root.mainloop()