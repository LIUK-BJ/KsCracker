import tkinter as tk #导入tkinter GUI库
import tkinter.messagebox as tkmessage
import time
def getZip():#目前用来显示通知，后面会用于导入ZIP文件
    tkmessage.showinfo("来自作者的提示","此项目正处于新建文件夹阶段，暂未实现导入文件的功能！")#显示未完工通知
    status_text.insert(tk.END,"您似乎已经导入了一个ZIP文件。\n")
    status_text.insert(tk.END,"文件名"+"{Filename}"+"\n")
    for i in range(10000):
        status_text.insert(tk.END,"当前正在尝试的密码是："+str(i)+"\n")
        status_text.see(tk.END)

Mainwindow=tk.Tk()
Mainwindow.title("KsCracker V0.0.1_Beta")#设置窗口标题
Header=tk.Label(Mainwindow,text="Welcome to KsCracker！",font=("宋体",25))#标题文字 "Welcome to Kscracker！"
Header.grid()#定位

button1=tk.Button(Mainwindow,text="导入ZIP文件",font=("宋体",25),fg="blue",command=getZip)#导入ZIP文件的按钮，点击后执行getZIP函数的相关内容，按钮标题"导入ZIP文件"
button1.grid(row=1,column=0)#位置：第2行，第1列（第1行，第0列，如果你想这样理解的话）

status_text=tk.Text(Mainwindow,font=("宋体",20),fg="green")#用于显示状态的文本框(绿色文字)
status_text.grid(row=2,column=0)#定位
status_text.insert(tk.END,"欢迎使用KsCracker！\n")#显示默认文本 "欢迎使用KsCracker！"

Mainwindow.mainloop()
