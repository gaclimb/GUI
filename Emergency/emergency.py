import tkinter
from tkinter import ttk


class Emergency():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('应急处理')
        self.window.overrideredirect(True)
        self.window.geometry('1000x380+100+50')
        self.window["background"] = "blanchedalmond"
        self.layout()
        self.openfile()
        self.window.mainloop()

    def layout(self):
        self.label = tkinter.Label(self.window, text='参与处室:', font=('仿宋', 14), bg='blanchedalmond').place(x=565, y=40)
        self.label = tkinter.Label(self.window, text='应急内容发布', font=('仿宋', 14), bg='blanchedalmond').place(x=700, y=70)
        self.label = tkinter.Label(self.window, text='备注:应急处置人员和应急内容发布格式均可以' + '\n' +
                                                     '通过文件修改' + '\t', font=('仿宋', 14), foreground='red',
                                   justify='left', bg='blanchedalmond').place(x=565, y=270)
        self.text_personnel = tkinter.Text(self.window, font=('仿宋', 16), width=50, height=15, bg='springgreen')
        self.text_personnel.place(x=5, y=40)
        self.text_change_release = tkinter.Text(self.window, font=('仿宋', 12), width=52, height=10, bg='springgreen')
        self.text_change_release.place(x=570, y=100)

        self.Doing_things_deal = ttk.Combobox(self.window, )

        self.Doing_things_deal['value'] = ('应用管理一处：', '应用管理二处：', '应用管理三处:', '应用管理四处:', '应用管理一处四组:',
                                           '系统管理一处:', '系统管理二处:', '资源管理处:', '网络管理一处:')
        self.Doing_things_deal.place(x=655, y=40)
        self.Doing_things_deal.current(0)

        def personnel(event):
            self.text_personnel.insert('insert', '\n' + self.Doing_things_deal.get())

        self.Doing_things_deal.bind("<<ComboboxSelected>>", personnel)
        self.buttom = tkinter.Button(self.window, text='退出', width=10, command=self.quit, cursor='hand2',
                                     bg='red').place(x=915,
                                                     y=330)

    def openfile(self):
        with open('./Emergency/personnel', 'r', encoding='utf8')as fp:
            self.text_personnel.insert('insert', fp.read() + '\n')
        with open('./Emergency/release', 'r', encoding='utf8')as fr:
            self.text_change_release.insert('insert', fr.read() + '\n')

    def quit(self):
        self.window.destroy()


if __name__ == '__main__':
    change = Emergency()
