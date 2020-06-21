import tkinter
import tkinter.messagebox
from Editor.editor import Edite as edit


class Content():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('内容发布')
        self.window.geometry('600x600+200+50')
        self.window.overrideredirect(True)  # 隐藏主窗口标题栏
        # self.window.wm_attributes('-topmost', 1)  # 强制窗口置于程序顶端
        self.window["background"] = "blanchedalmond"
        self.layout()
        self.window.mainloop()

    def layout(self):
        self.lable = tkinter.Label(self.window, text='日志', font=('仿宋', 18), bg='blanchedalmond').place(x=275, y=5)
        self.text = tkinter.Text(self.window, width=80, height=35, bg='aquamarine')
        self.text.place(x=18, y=40)
        self.buttom = tkinter.Button(self.window, text='夜间', width=10, cursor='hand2', bg='aquamarine',
                                     command=self.night).place(x=18,
                                                               y=510)
        self.buttom = tkinter.Button(self.window, text='上午', width=10, cursor='hand2', bg='aquamarine',
                                     command=self.moning).place(x=113,
                                                                y=510)
        self.buttom = tkinter.Button(self.window, text='下午', width=10, cursor='hand2', bg='aquamarine',
                                     command=self.afternoon).place(x=210,
                                                                   y=510)
        self.buttom = tkinter.Button(self.window, text='业务单', width=10, cursor='hand2', bg='aquamarine',
                                     command=self.business_single).place(x=308,
                                                                         y=510)
        self.buttom = tkinter.Button(self.window, text='上午升级', width=10, cursor='hand2', bg='aquamarine',
                                     command=self.moning_updata).place(x=406,
                                                                       y=510)
        self.buttom = tkinter.Button(self.window, text='昨日变更', width=10, cursor='hand2', bg='aquamarine',
                                     command=self.changes).place(x=504,
                                                                 y=510)
        self.buttom = tkinter.Button(self.window, text='下午升级', width=10, cursor='hand2', bg='aquamarine',
                                     command=self.afternoon_updata).place(x=18,
                                                                          y=550)
        self.buttom = tkinter.Button(self.window, text='事件单', width=10, cursor='hand2', bg='aquamarine',
                                     command=self.single_event).place(x=113,
                                                                      y=550)
        self.buttom = tkinter.Button(self.window, text='值班人员', width=10, cursor='hand2', bg='aquamarine',
                                     command=self.duty_work).place(x=210,
                                                                   y=550)
        self.buttom = tkinter.Button(self.window, text='夜间升级', width=10, cursor='hand2', bg='aquamarine',
                                     command=self.night).place(x=308,
                                                               y=550)
        self.buttom = tkinter.Button(self.window, text='编辑', width=10, cursor='hand2', bg='mediumslateblue',
                                     command=self.edits).place(x=406,
                                                               y=550)
        self.buttom = tkinter.Button(self.window, text='退出', width=10, cursor='hand2', bg='red',
                                     command=self.quit).place(x=504,
                                                              y=550)

    def quit(self):
        self.window.destroy()

    def edits(self):
        self.text.delete('1.0', tkinter.END)
        edit()

    def single_event(self):
        with open('DATA/事件单', 'r', encoding='utf-8')as rf:
            self.text.insert('insert', rf.read())

    def night(self):
        with open('DATA/夜间', 'r', encoding='utf-8')as rf:
            self.text.insert('insert', rf.read())

    def moning(self):
        with open('DATA/上午', 'r', encoding='utf-8')as rf:
            self.text.insert('insert', rf.read())

    def afternoon(self):
        with open('DATA/下午', 'r', encoding='utf-8')as rf:
            self.text.insert('insert', rf.read())

    def moning_updata(self):
        with open('DATA/上午升级', 'r', encoding='utf-8')as rf:
            self.text.insert('insert', rf.read())

    def afternoon_updata(self):
        with open('DATA/下午升级', 'r', encoding='utf-8')as rf:
            self.text.insert('insert', rf.read())

    def business_single(self):
        with open('DATA/业务单', 'r', encoding='utf-8')as rf:
            self.text.insert('insert', rf.read())

    def changes(self):
        with open('DATA/昨日变更', 'r', encoding='utf-8')as rf:
            self.text.insert('insert', rf.read())

    def night_updata(self):
        with open('DATA/夜间升级', 'r', encoding='utf-8')as rf:
            self.text.insert('insert', rf.read())

    def duty_work(self):
        work = tkinter.messagebox.askquestion(title='提示',message='是否工作日')
        if work == 'yes':
            with open('DATA/值班人员-工作日', 'r', encoding='utf-8')as rf:
                self.text.insert('insert', rf.read())
        else:
            self.duty_unwork()

    def duty_unwork(self):
        with open('DATA/工作人员-夜班及非工作日', 'r', encoding='utf-8')as rf:
            self.text.insert('insert', rf.read())


if __name__ == '__main__':
    content = Content()
