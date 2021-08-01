from tkinter import *
from chatbot import response,bot_name
from emoji import emojize

BG_GRAY = "sky blue"
BG_COLOR = "#fff"
TEXT_COLOR = "#000"

FONT = "Melvetica 14"
FONT_BOLD = "Melvetica 13 bold"

class chatApplication:

    def __init__(self):
        self.window=Tk()
        self.main()

    def execution(self):
        self.window.mainloop()

    def main(self):

        self.window.title("Chatbot")
        self.window.resizable(width=True, height=True)
        self.window.configure(width=500 , height=600 ,bg =BG_COLOR)

        head_label = Label(self.window , bg=BG_COLOR,fg=TEXT_COLOR,text="Bienvenue sur 💬:",font=FONT_BOLD,pady=1)
        head_label.place(relwidth =1)

        line = Label(self.window,width=450,bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight =0.012)

        self.text_widget=Text(self.window,width=18,height=2,bg=BG_COLOR,fg=TEXT_COLOR, font=FONT,padx=5,pady=5)
        self.text_widget.place(relheight=0.8,relwidth=1,rely=0.08)
        self.text_widget.configure(cursor="arrow",state=DISABLED)

        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)


        bottom_label = Label(self.window, bg=BG_GRAY, height=85)
        bottom_label.place(relwidth=1, rely=0.825)


        self.msg_entry = Entry(bottom_label, bg="light cyan", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.78, relheight=0.06, rely=0.008, relx=0.008)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self.enter)

        send_button = Button(bottom_label, text="Envoyer", font=FONT_BOLD, width=20, bg=BG_GRAY,command=lambda: self.enter(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def enter(self,event):
        msg = self.msg_entry.get()
        self.message(msg," 👨 ")
    def message(self,msg,sender):
        if not msg:
            return

        self.msg_entry.delete(0,END)
        msg1 = f"{sender} : {msg}\n\n"
        self.text_widget.configure(cursor="arrow", state=NORMAL)
        self.text_widget.insert(END,msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name} : {response(msg)}\n\n"
        self.text_widget.configure(cursor="arrow", state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = chatApplication()
    app.execution()