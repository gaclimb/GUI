import tkinter
import tkinter.messagebox
from Emergency.emergency import Emergency as emergency
from Information.Information import Information as information
from Operational_phone.Operational_phone import Operational_phone as phone
from Changes.Change import Change as change
from Content.Content import Content as content


class Integrated_DWS():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('值班')
        self.window.geometry('555x30+600+0')
        self.window.overrideredirect(True)  # 隐藏主窗口标题栏
        self.window.wm_attributes('-topmost', 1)  # 强制窗口置于程序顶端
        self.layout()
        self.window.mainloop()

    def layout(self):
        self.button = tkinter.Button(self.window, text='信息处理', width=10, font=('仿宋', 13), cursor='hand2',
                                     bg='blanchedalmond', command=self.information).grid(row=0, column=0)
        self.button = tkinter.Button(self.window, text='内容发布', width=10, font=('仿宋', 13), cursor='hand2',
                                     bg='blanchedalmond', command=self.content).grid(row=0, column=1)
        self.button = tkinter.Button(self.window, text='运维电话', width=10, font=('仿宋', 13), cursor='hand2',
                                     bg='blanchedalmond', command=phone).grid(row=0, column=2)
        self.button = tkinter.Button(self.window, text='应急管理', width=10, font=('仿宋', 13), cursor='hand2',
                                     command=self.emergency, bg='blanchedalmond').grid(row=0, column=3)
        self.button = tkinter.Button(self.window, text='数据维护', width=10, font=('仿宋', 13), cursor='hand2',
                                     bg='blanchedalmond', command=change).grid(row=0, column=4)
        self.button = tkinter.Button(self.window, text='退出', width=5, font=('仿宋', 13), cursor='hand2',
                                     command=self.quit, bg='red').grid(row=0, column=5)

    def quit(self):
        quit = tkinter.messagebox.askokcancel('提示', '确定要退出吗')
        if quit == True:
            self.window.destroy()

    def emergency(self):
        emergency()

    def information(self):
        information()

    def phone(self):
        phone()

    def change(self):
        change()

    def content(self):
        content()


if __name__ == '__main__':
    idws = Integrated_DWS()
