import tkinter as tk #导入tkinter GUI库
import tkinter.messagebox as tkmessage
def getZip():#目前用来显示通知，后面会用于导入ZIP文件
    tkmessage.showinfo("来自作者的提示","此项目正处于新建文件夹阶段，暂未实现导入文件的功能！")#显示未完工通知

Mainwindow=tk.Tk()
Mainwindow.title("KsCracker V0.0.1_Beta")#设置窗口标题
Header=tk.Label(Mainwindow,text="Welcome to KsCracker！",font=("宋体",25))#标题文字 "Welcome to Kscracker！"
Header.grid()#定位

button1=tk.Button(Mainwindow,text="导入ZIP文件",font=("宋体",25),fg="blue",command=getZip)#导入ZIP文件的按钮，点击后执行getZIP函数的相关内容，按钮标题"导入ZIP文件"
button1.grid(row=1,column=0)#位置：第2行，第1列（第1行，第0列，如果你想这样理解的话）

Mainwindow.mainloop()
