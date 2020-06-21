import tkinter
from tkinter import filedialog, messagebox



class Edite():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry('700x700')
        self.window.title('文本编辑')
        self.window["background"] = "blanchedalmond"
        self.edite()
    def edite(self):
        self.label = tkinter.Label(self.window, text='选择要编辑的文件', bg='blanchedalmond').place(x=116, y=15)
        self.entry = tkinter.Entry(self.window, width=45, bg='lime')
        self.entry.place(x=220, y=15)
        self.text = tkinter.Text(self.window, width=60, height=30, font=('仿宋', 16), bg='lime')
        self.text.place(x=18, y=50)
        self.button_save = tkinter.Button(self.window, text='保存', width=10, cursor='hand2', bg='aquamarine', command=self.save_file).place(x=18, y=10)
        self.button_exit = tkinter.Button(self.window, text='取消', width=10, cursor='hand2', bg='aquamarine', command=self.clear).place(x=600, y=10)
        self.button_open = tkinter.Button(self.window, text='打开', width=5, cursor='hand2', bg='aquamarine', command=self.open_file).place(x=550, y=10)
        self.window.mainloop()


    def open_file(self):
        try:
            file_path = filedialog.askopenfilename(initialdir=r'DATA/')
            self.entry.insert('insert',file_path)
            with open(file_path, 'r', encoding='utf-8')as rf:
                result = rf.read()
                self.text.insert('1.0', result)
        except:
            pass

    def clear(self):
        self.entry.delete(0,tkinter.END)
        self.text.delete('1.0', tkinter.END)

    def save_file(self):
        try:
            file_path = filedialog.asksaveasfilename(initialdir=r'DATA/')
            with open(file_path, 'w', encoding='utf-8')as wf:
                result = wf.write(self.text.get('1.0', tkinter.END))
                self.text.insert('1.0', result)
        except:
            pass



if __name__ == '__main__':
    edit = Edite()
