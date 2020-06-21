import tkinter
import sqlite3


class Information():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('信息处理')
        self.window.geometry('700x370+600+100')
        self.window["background"] = "blanchedalmond"
        self.window.overrideredirect(True)  # 隐藏主窗口标题栏
        # self.window.wm_attributes('-topmost',1)  # 强制窗口置于程序顶端
        self.layout()
        self.file_db = 'DATA/system_office.db'
        self.window.mainloop()

    def layout(self):
        self.label = tkinter.Label(self.window, text='报警信息整理', font=('仿宋', 16), bg='blanchedalmond').place(x=285, y=5)
        self.label = tkinter.Label(self.window, text='负责处室查询', font=('仿宋', 16), bg='blanchedalmond').place(x=285, y=270)
        self.label = tkinter.Label(self.window, text='系统：', font=('仿宋', 16), bg='blanchedalmond').place(x=4, y=305)
        self.label = tkinter.Label(self.window, text='结果：', font=('仿宋', 16), bg='blanchedalmond').place(x=300, y=305)
        self.label = tkinter.Label(self.window, text='注意：如果系统名出错可修改为正确的系统名称', font=('仿宋', 16), foreground='red',
                                   bg='blanchedalmond').place(x=5, y=335)
        self.entry = tkinter.Entry(self.window, width=98, bg='lime')
        self.entry.place(x=4, y=35)
        self.entry_sys = tkinter.Entry(self.window, width=22, bg='lime', font=('仿宋', 14))
        self.entry_sys.place(x=65, y=310)
        self.entry_office = tkinter.Entry(self.window, width=30, bg='lime', font=('仿宋', 14))
        self.entry_office.place(x=370, y=310)
        self.Informtion = tkinter.Text(self.window, width=76, height=8, font=('仿宋', 13), bg='aquamarine')
        self.Informtion.place(x=5,y=65)
        self.button = tkinter.Button(self.window, text='整理', width=10, cursor='hand2', bg='aquamarine', command=self.process).place(x=120,
                                                                                                              y=230)
        self.button = tkinter.Button(self.window, text='重置', width=10, cursor='hand2', bg='aquamarine',
                                     command=self.clear).place(x=215, y=230)
        self.button = tkinter.Button(self.window, text='复制', width=10, cursor='hand2', bg='aquamarine', command=self.cut).place(x=310,
                                                                                                              y=230)
        self.button = tkinter.Button(self.window, text='查询', width=10, cursor='hand2', bg='aquamarine',
                                     command=self.query).place(x=405, y=230)
        self.entry_sys.bind("<Return>", self.event)
        self.button = tkinter.Button(self.window, text='退出', width=10, bg='red', cursor='hand2',
                                     command=self.quit).place(x=500, y=230)

    def quit(self):
        self.window.destroy()

    def cut(self,event=None):
        self.Informtion.tag_add(tkinter.SEL, '1.0', tkinter.END)
        self.Informtion.event_generate("<<Cut>>")

    def event(self, event):
        self.query()

    def query(self):
        self.entry_office.delete(0, 30)
        connt = sqlite3.connect(self.file_db)
        cur = connt.cursor()
        sql = f"SELECT * FROM sys_office WHERE sys_name='{self.entry_sys.get()}'"
        cur.execute(sql)
        data = cur.fetchall()
        for i in data:
            data_i = i[1] + '\t' + i[2]
            self.entry_office.insert(0,data_i)
        cur.close()
        connt.close()
        self.entry_sys.delete(0, 22)

    def process(self):
        if self.entry.get() == '':
            data = '时间：' + '\n' + '系统：' + '\n' + '问题：' + '\n' + '案例：' + '\n' + '状态：未处理'
            self.Informtion.insert('1.0', data)
        else:
            pass

    def clear(self):
        self.entry.delete(0,tkinter.END)
        self.entry_sys.delete(0,tkinter.END)
        self.entry_office.delete(0,tkinter.END)
        self.Informtion.delete('1.0', tkinter.END)

if __name__ == '__main__':
    change = Information()
