import ipaddr,os,time

import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
class IPSORT():
    def __init__(self):
        self.ipsortdone = ''

    def openfile(self):
        '''打开选择文件夹对话框'''
        root = tk.Tk()
        root.withdraw()#隐藏主窗口
        root.iconbitmap('D:/pythonlab/ico/command_prompt_32px_1082683_easyicon.net.ico')#换标题的图标
        # self.Folderpath = filedialog.askdirectory()  # 获得选择好的文件夹
        self.Filepath = filedialog.askopenfilename()  # 获得选择好的文件

        # fold=self.Folderpath
        return  self.Filepath

    def ipsort(self):
        try:
            l = []
            m = {}
            line=0
            ipl = []
            file=IPSORT.openfile(self)
            iplist=open(file)
            for i in iplist:
                line+=1
                ii = i.rstrip()
                l.append(ii)
                ip = ipaddr.IPv4Address(ii)
                m.update({ip.__int__(): ip})
            iplist.close()
            for j in m.keys():
                ipl.append(j)

            ipl.sort()

            for k in ipl:
                self.ipsortdone=str(self.ipsortdone)+str(m.get(k))+'\n'
            iplist = open(file,mode='w',encoding='utf8')
            iplist.write(self.ipsortdone.rstrip())
            iplist.close()

            info=str(time.strftime("%Y-%m-%d %H:%M:%S")+'\n'+'IP地址排序完成.')
            tkinter.messagebox.showinfo('提示', info)
            return
        except ValueError:
            errorcode=str('error line: '+str(line)+'\n'+'"%s"'%(i.rstrip()))
            warning = str(time.strftime("%Y-%m-%d %H:%M:%S") + '\n' + '错误，请确认IP地址簿！'+'\n'+errorcode)
            tkinter.messagebox.showwarning('提示', warning)
        finally:
            iplist.close();




a=IPSORT()
a.ipsort()
