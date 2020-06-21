import tkinter
import sqlite3


class Operational_phone():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('运维电话')
        self.window.geometry('450x210+800+500')
        self.window["background"] = "blanchedalmond"
        self.window.overrideredirect(True)  # 隐藏主窗口标题栏
        # self.window.wm_attributes('-topmost', 1)  # 强制窗口置于程序顶端
        self.file_db = 'DATA/system_office.db'
        self.layout()
        self.window.mainloop()

    def layout(self):
        self.label = tkinter.Label(self.window, text='运维电话', font=('仿宋', 14), bg='blanchedalmond').grid(row=0, column=1)
        self.label = tkinter.Label(self.window, text='系统名称：', font=('仿宋', 14), bg='blanchedalmond').grid(row=1,
                                                                                                         column=0)
        self.label = tkinter.Label(self.window, text='注意：运维电话可能与查找到的不同。', font=('仿宋', 15), foreground='red',
                                   bg='blanchedalmond').place(x=5, y=175)
        self.entry = tkinter.Entry(self.window, width=25, bg='lime', font=('仿宋', 14))
        self.entry.grid(row=1, column=1)

        self.button = tkinter.Button(self.window, text='查询', width=10, bg='blanchedalmond', cursor='hand2',
                                     command=self.query)
        self.button.grid(row=1, column=2, padx=10)
        self.entry.bind("<Return>", self.event)
        self.button = tkinter.Button(self.window, text='退出', width=5, bg='red', cursor='hand2',
                                     command=self.quit).place(x=400, y=175)
        self.phone = tkinter.Text(self.window, width=43, height=5, font=('仿宋', 15), bg='springgreen')
        self.phone.place(x=8, y=65)

    def quit(self):
        self.window.destroy()

    def event(self, event):
        self.query()

    def query(self):
        self.phone.delete('1.0', tkinter.END)
        connt = sqlite3.connect(self.file_db)
        cur = connt.cursor()
        sql = 'SELECT * FROM "sys_phone"'
        cur.execute(sql)
        data = cur.fetchall()
        var = self.entry.get()
        if var == '':
            pass
        else:
            for i in data:
                if var in i[3]:
                    data_i = i[1] + '\t' + i[2] + '\n'
                    self.phone.insert('1.0', data_i)
                continue
        cur.close()
        connt.close()
        self.entry.delete(0,25)
if __name__ == '__main__':
    phone = Operational_phone()
