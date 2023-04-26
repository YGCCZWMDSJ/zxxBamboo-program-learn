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
![VSCODE逐步python_step25](images/054e48a6a070a1ffd134990069108ad2562c67bf42abd4f9a57f1e81b9211b91.png)  

#### 下方调试控制台
![VSCODE逐步python_step26](images/fad4b9296463d3980cfe3b1ac1f9945c824f2e765824b3a933a882761dadecfe.png)  
下面是简单的调试演示：
![VSCODE逐步python_step262](images/e4d19dc9117e44baf8411386ec7ba5b2ac10b46360f2c5ade59c98d4283e5873.png)  
![VSCODE逐步python_step263](images/60e23b266998dce13a4bb00e1342ced6678a1df8e87d4565c2fc950259613975.png)  

## 调试C/C++
> 这个的环境是大头，主要是因为缺gcc
### 环境安装
推荐文章：
https://blog.csdn.net/m0_62721576/article/details/127207028
按需据教程安装
### 调试
与python大同小异，比较有意思的是调试时的左边变量框
![VSCODE逐步python_step271](images/23a12cd12c81d9c8fe8fa57f1b1766220d662dac3b0f957a399d312f014aa83a.png)  

## 调试Java
### 环境安装
https://blog.csdn.net/LKFMYQQ/article/details/120519567
vscode扩展安装：Java Extension Pack(包含插件Java Debugger for Visual Studio Code+插件Language Support for Java™ by Red Hat)
### 调试步骤
1. 准备项目。打开一个 .java 文件，Java 扩展会激活。Maven、Gradle 和 Eclipse 项目都能得到支持。这个扩展会自动构建项目，不需要手工触发构建。

2. 开始调试。切换到调试视图(Ctrl+Shift+D)，打开 launch.json 并添加 Java 调试配置。

3. 在 mainClass 中填入要启动的类，或者在hostName 中填入要附加的主机名以及在 port 中填入端口。

4. 设置断点并按 F5 开始调试

剩下操作与python大同小异

________________________________
~~懒了，php，vue，go，R那些不想写了,除了环境都差不多~~
算了，php也给个地址吧：https://blog.csdn.net/qq_44803335/article/details/108806851

**又到了题主喜闻乐见的交友时刻（喜）**
## 资料共和学习白嫖群，资料全弄的网盘的：
![图 17](images/fe7cf61096d40b0f0f3a590df3f5231c885888052fc24b26082a73070ce3c520.png)  
还有群主的每日打卡以此来下饭促学（喜）
## chatgpt plus 共和合用群
![图 18](images/2b8505352cc4bd96185cf57b261161706485ec4e19035ed66d2add634b19f088.png)  

## 题主的Offensive Security系列之路
![图 19](images/e7aa53eccef9fac898a31283256ceece3040a0705adcb008999c5a58427965e6.png)  
有意愿来玩的或者来见证群主痛苦的来！群主愿意做你的共学伙伴（喜）一起的话还有每天的撅醒服务（悲）