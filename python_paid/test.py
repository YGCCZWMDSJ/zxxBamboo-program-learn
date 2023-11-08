import tkinter as tk

# 初始化Tkinter窗口
root = tk.Tk()
root.title("可移动的数字块")

# 创建Canvas小部件
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# 创建一个类来表示可移动的数字块
class NumberBlock:
    def __init__(self, canvas, x, y, number):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.number = number
        self.text_id = canvas.create_text(x, y, text=str(number), font=("Helvetica", 24), fill="black")

    def move(self, dx, dy):
        self.canvas.move(self.text_id, dx, dy)
        self.x += dx
        self.y += dy

# 创建可移动的数字块示例
block1 = NumberBlock(canvas, 50, 50, 1)
block2 = NumberBlock(canvas, 150, 50, 2)
block3 = NumberBlock(canvas, 250, 50, 3)

# 移动数字块示例
block1.move(0, 50)
block2.move(0, 50)
block3.move(0, 50)

# 启动主循环
root.mainloop()
