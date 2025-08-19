import tkinter as tk #导入tkinter GUI库
import tkinter.messagebox as tkmessage
import time
import loadzip
def getZip():#目前用来显示通知，后面会用于导入ZIP文件
    tkmessage.showinfo("来自作者的提示","此项目正处于新建文件夹阶段，暂未实现导入文件的功能！")#显示未完工通知
    status_text.insert(tk.END,"您似乎已经导入了一个ZIP文件。\n")
    status_text.insert(tk.END,"文件名"+"{Filename}"+"\n")
    for i in range(10000):
        status_text.insert(tk.END,"当前正在尝试的密码是："+str(i)+"\n")
    loadzip.load_zip_file()

Mainwindow=tk.Tk()
Mainwindow.title("KsCracker V0.0.1_Beta")#设置窗口标题
Header=tk.Label(Mainwindow,text="Welcome to KsCracker！",font=("宋体",25))#标题文字 "Welcome to Kscracker！"
Header.grid()#定位

button1=tk.Button(Mainwindow,text="导入ZIP文件",font=("宋体",25),fg="blue",command=getZip)#导入ZIP文件的按钮，点击后执行getZIP函数的相关内容，按钮标题"导入ZIP文件"
button1.grid(row=1,column=0)#位置：第2行，第1列（第1行，第0列，如果你想这样理解的话）

# 创建容器，包裹滚动条与文本框
text_frame = tk.Frame(Mainwindow)
text_frame.grid(row=2, column=0, sticky='nsew')

status_text=tk.Text(text_frame,font=("宋体",20),fg="green")#用于显示状态的文本框(绿色文字)
status_text.insert(tk.END,"欢迎使用KsCracker！\n")#显示默认文本 "欢迎使用KsCracker！"

# 创建一个滚动条
scroll_status_text = tk.Scrollbar(text_frame, orient="vertical", command=status_text.yview)

# 绑定滚动条和文本框
status_text.configure(yscrollcommand=scroll_status_text.set)

# 将文本框和滚动条包裹到容器中
scroll_status_text.pack(side="right", fill="y")
status_text.pack(side="left", fill="both", expand=True)

Mainwindow.mainloop()
