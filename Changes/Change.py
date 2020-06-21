import tkinter
import sqlite3


class Change():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('数据维护')
        self.window.geometry('700x315+600+100')
        self.window["background"] = "blanchedalmond"
        self.window.overrideredirect(True)  # 隐藏主窗口标题栏
        # self.window.wm_attributes('-topmost',1)  # 强制窗口置于程序顶端
        self.layout()
        self.window.mainloop()

    def layout(self):
        self.lable = tkinter.Label(self.window, text='数据维护', font=('仿宋', 20), bg='blanchedalmond').place(x=285, y=5)
        self.lable = tkinter.Label(self.window, text='系统处室', font=('仿宋', 16), bg='blanchedalmond').place(x=295, y=40)
        self.lable = tkinter.Label(self.window, text='结果：', font=('仿宋', 16), bg='blanchedalmond').place(x=5, y=145)
        self.lable = tkinter.Label(self.window, text='系统：', font=('仿宋', 16), bg='blanchedalmond').place(x=5, y=70)
        self.lable = tkinter.Label(self.window, text='数据：', font=('仿宋', 16), bg='blanchedalmond').place(x=305, y=75)
        self.lable = tkinter.Label(self.window, text='录入数据：', font=('仿宋', 16), bg='blanchedalmond').place(x=5, y=110)
        self.entry_sys = tkinter.Entry(self.window, width=20, font=('仿宋', 16), bg='lime')
        self.entry_sys.place(x=70,y=75)
        self.entry_sj = tkinter.Entry(self.window, width=20, font=('仿宋', 16), bg='lime')
        self.entry_sj.place(x=372,y=75)
        self.entry_office = tkinter.Entry(self.window, width=15, font=('仿宋', 16), bg='lime')
        self.entry_office.place(x=110,y=110)
        self.entry_system = tkinter.Entry(self.window, width=15, font=('仿宋', 16), bg='lime')
        self.entry_system.place(x=280,y=110)
        self.entry_name = tkinter.Entry(self.window, width=13, font=('仿宋', 16), bg='lime')
        self.entry_name.place(x=450,y=110)
        self.entry_JG = tkinter.Entry(self.window, width=51, font=('仿宋', 17), bg='lime')
        self.entry_JG.place(x=70,y=145)
        self.lable = tkinter.Label(self.window, text='运维电话', font=('仿宋', 16), bg='blanchedalmond').place(x=295, y=175)
        self.lable = tkinter.Label(self.window, text='结果：', font=('仿宋', 16), bg='blanchedalmond').place(x=5, y=276)
        self.lable = tkinter.Label(self.window, text='系统：', font=('仿宋', 16), bg='blanchedalmond').place(x=5, y=205)
        self.lable = tkinter.Label(self.window, text='数据：', font=('仿宋', 16), bg='blanchedalmond').place(x=305, y=205)
        self.lable = tkinter.Label(self.window, text='录入数据：', font=('仿宋', 16), bg='blanchedalmond').place(x=5, y=242)
        self.entry_phone_sys = tkinter.Entry(self.window, width=20, font=('仿宋', 16), bg='lime')
        self.entry_phone_sys.place(x=70, y=205)
        self.entry_phone_sj = tkinter.Entry(self.window, width=20, font=('仿宋', 16), bg='lime')
        self.entry_phone_sj.place(x=372, y=205)
        self.entry_phone_system = tkinter.Entry(self.window, width=15, font=('仿宋', 16), bg='lime')
        self.entry_phone_system.place(x=110, y=242)
        self.entry_phone_tel = tkinter.Entry(self.window, width=15, font=('仿宋', 16), bg='lime')
        self.entry_phone_tel.place(x=280, y=242)
        self.entry_phone_name = tkinter.Entry(self.window, width=13, font=('仿宋', 16), bg='lime')
        self.entry_phone_name.place(x=450, y=242)
        self.entry_phone_JG = tkinter.Entry(self.window, width=51, font=('仿宋', 17), bg='lime')
        self.entry_phone_JG.place(x=70, y=276)
        self.button = tkinter.Button(self.window, text='查询', width=10, cursor='hand2', bg='aquamarine', command=self.query).place(x=605,y=73)
        self.button = tkinter.Button(self.window, text='更新', width=10, cursor='hand2', bg='aquamarine', command=self.updata).place(x=605,y=108)
        self.button = tkinter.Button(self.window, text='录入', width=10, cursor='hand2', bg='aquamarine', command=self.insert).place(x=605,y=175)
        self.button = tkinter.Button(self.window, text='清空', width=10, cursor='hand2', bg='blue', command=self.clear).place(x=605,
                                                                                                                  y=208)
        self.button = tkinter.Button(self.window, text='退出', width=10, cursor='hand2', bg='red', command=self.quit).place(x=605,
                                                                                                              y=240)


    def quit(self):

        self.window.destroy()

    def query(self):
        if self.entry_sys.get() != '':
            self.entry_JG.delete(0,51)
            connt = sqlite3.connect('DATA/system_office.db')
            cur = connt.cursor()
            sql = f"SELECT * FROM sys_office WHERE sys_name='{self.entry_sys.get()}'"
            cur.execute(sql)
            data = cur.fetchall()
            for i in data:
                data_office = i[1] + '\t' + i[2]
                self.entry_JG.insert(0, data_office)
                self.entry_sys.delete(0,16)
                self.entry_sys.insert(0, i[2])
            cur.close()
            connt.close()
        else:
            self.entry_phone_JG.delete(0,51)
            connt = sqlite3.connect('DATA/system_office.db')
            cur = connt.cursor()
            sql = f"SELECT * FROM sys_phone WHERE sys_name='{self.entry_phone_sys.get()}'"
            cur.execute(sql)
            data = cur.fetchall()
            for i in data:
                data_office = i[1] + '\t' + i[2]
                self.entry_phone_JG.insert(0, data_office)
                self.entry_phone_sys.delete(0, 16)
            cur.close()
            connt.close()


    def updata(self):
        if self.entry_sys.get() != '':
            connt = sqlite3.connect('DATA/system_office.db')
            cur = connt.cursor()
            sql = f"UPDATE sys_office SET office='{self.entry_sj.get()}' WHERE name='{self.entry_sys.get()}'"
            cur.execute(sql)
            connt.commit()
            cur.close()
            connt.close()
            data = self.entry_sys.get() + '\t' + self.entry_sj.get()
            self.entry_JG.delete(0,tkinter.END)
            self.entry_JG.insert(0,data)

        else:
            connt = sqlite3.connect('DATA/system_office.db')
            cur = connt.cursor()
            sql = f"UPDATE sys_phone SET phone='{self.entry_phone_sj.get()}' WHERE name='{self.entry_phone_sys.get()}'"
            cur.execute(sql)
            connt.commit()
            cur.close()
            connt.close()
            data = self.entry_phone_sys.get() + '\t' + self.entry_sj.get()
            self.entry_phone_JG.delete(0, tkinter.END)
            self.entry_phone_JG.insert(0, data)



    def insert(self):
        if self.entry_office.get() != '':
            self.entry_JG.delete(0, tkinter.END)
            connt = sqlite3.connect('DATA/system_office.db')
            cur = connt.cursor()
            sql = f"INSERT INTO sys_office('office','name','sys_name') VALUES ('{self.entry_office.get()}','{self.entry_system.get()}','{self.entry_name.get()}')"
            cur.execute(sql)
            connt.commit()
            cur.close()
            connt.close()
            data = self.entry_office.get() + '\t' + self.entry_system.get() + '\t' + self.entry_name.get()
            self.entry_JG.insert(0,data)
        else:
            self.entry_phone_JG.delete(0, tkinter.END)
            connt = sqlite3.connect('DATA/system_office.db')
            cur = connt.cursor()
            sql = f"INSERT INTO sys_phone('name', 'phone', 'sys_name') VALUES ('{self.entry_phone_system.get()}','{self.entry_phone_tel.get()}','{self.entry_phone_name.get()}')"
            cur.execute(sql)
            connt.commit()
            cur.close()
            connt.close()
            data = self.entry_phone_system.get() + '\t' + self.entry_phone_tel.get() + '\t' + self.entry_phone_name.get()
            self.entry_phone_JG.insert(0, data)

    def clear(self):
        self.entry_sys.delete(0,tkinter.END)
        self.entry_sj.delete(0,tkinter.END)
        self.entry_office.delete(0,tkinter.END)
        self.entry_system.delete(0,tkinter.END)
        self.entry_name.delete(0,tkinter.END)
        self.entry_JG.delete(0,tkinter.END)
        self.entry_phone_sys.delete(0,tkinter.END)
        self.entry_phone_sj.delete(0,tkinter.END)
        self.entry_phone_system.delete(0,tkinter.END)
        self.entry_phone_tel.delete(0,tkinter.END)
        self.entry_phone_name.delete(0,tkinter.END)
        self.entry_phone_JG.delete(0,tkinter.END)
if __name__ == '__main__':
    chang = Change()