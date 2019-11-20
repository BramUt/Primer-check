from tkinter import *
from tkinter import scrolledtext, messagebox


def gui():

    def clicked_5():
        raw_seq_5 = txt_5.get("1.0", END)
        txt_5.configure(state='disabled', bg="light grey")

    def clicked_3():
        raw_seq_5 = txt_3.get("1.0", END)
        txt_3.configure(state="disabled", bg="light grey")

    window = Tk()
    window.title("Primer check 2")
    window.geometry("750x750")

    label_5 = Label(window, text="Enter 5'-UTR")
    txt_5 = scrolledtext.ScrolledText(window, width=40, height=20)
    button_5 = Button(window, text="OK", command=clicked_5)
    label_5.grid(column=0, row=0, sticky=W)
    txt_5.grid(column=0, row=1)
    button_5.grid(column=0, row=2, sticky=E)
    txt_5.focus()

    label_3 = Label(window, text="Enter 3'-UTR")
    txt_3 = scrolledtext.ScrolledText(window, width=40, height=20)
    button_3 = Button(window, text="OK", command=clicked_3)
    label_3.grid(column=3, row=0, sticky=W)
    txt_3.grid(column=3, row=1)
    button_3.grid(column=3, row=2, sticky=E)

    exit_button = Button(window,text="Quit", command=window.quit)
    exit_button.grid(column=3, row=4, sticky=E)

    window.mainloop()


gui()
