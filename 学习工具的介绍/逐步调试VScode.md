[TOC]
# 在VScode中逐步调试代码
> 文主之前一直不会调试VScode，今天下定决心一定要搞懂他。本文将列出文主目前会得的一点皮毛语言举例。欢迎也有此苦恼的同学与文主一起拨开迷雾见青云！

## 调试python
### step 1 开始调试
![VSCODE逐步python_step1](images/4572819ed2f0748e731c26405cb1153e05749af3ca2fb91e688e941026e1f920.png)  
![VSCODE逐步python_step12](images/4cad6d689a18d38c83e8d697d8888da1653ce8962a520d8d1d2a0e3cebb9791e.png)  
![VSCODE逐步python_step13](images/3e6f9bdc14781d105cc6c159397c39415a615f302ccc43d8bfe596d675392b3a.png)  
![VSCODE逐步python_step14](images/5b543297d041330df81b875044ce0cee32808d54a0a06dd0f5f8a1b78770aae7.png)  

### step2 介绍调试时比较好玩的功能
![VSCODE逐步python_step21](images/639eeecd21409465d92e55348d42554aa674d3f3de89aca66f375730db72a1ea.png)  
#### 调试条框
![VSCODE逐步python_step211](images/b3c8685239ba0ee787d9eba9b99c74c5a96342770586032b7a52fd9c367a499a.png)  
- **继续F5**：直接执行到下一个断点处，若无断点则直接执行完剩下的全部过程。
- **单步跳过F10**：当光标到达有函数的指令时，点击即运行完该函数，直接到下一条指令
- **单步调试F11**：前提为已经在一个断点处停下，从此断点开始点击一次，运行一条指令（一行代码）
- **单步跳出shift+F11**：当单步调试进入函数体中时，点击即可跳回到即将进入函数中的那条指令，此时该函数未执行
- **重启ctrl+shift+F5**：重新开始执行代码到第一个断点位置停下
- **停止shift+F5**：结束调试代码，直接推出该过程，此时没有执行代码
#### 左栏变量框
![VSCODE逐步python_step22](images/faaa6c21d0e4c2fc94fba1730c6bdd1ddcbbf82670bf1b569aa1131033d8ec95.png)  

#### 左栏监视框
![VSCODE逐步python_step231](images/beb421e4faf8d9d813231121926ff017b2ab3504cf8f24f63da3da298b296a9c.png)  
![VSCODE逐步python_step232](images/62960166c7723530bedd75b0dc4c2abfa31c13d93ec11d789efc3466d54ee352.png)  

#### 左栏调用堆栈框
![VSCODE逐步python_step24](images/b6e99adefc76ba7356541add75ed7ead3e8f3afe934e7560e28f4bb42c54f70a.png)  

#### 左栏断点框

#### 下方调试控制台