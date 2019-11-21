from tkinter import *
from tkinter.ttk import *


def gui_2():
    window = Tk()
    window.title("Primer check 2: parameter")
    window.geometry("250x175")

    var_1, var_2, var_3, var_4 = IntVar(), IntVar(), IntVar(), IntVar()
    var_1.set(60)
    var_2.set(40)
    var_3.set(55)
    var_4.set(62)

    label_maxcg = Label(window, text="Max CG%", font=("Arial", 12))
    selector_maxcg = Spinbox(window, from_=0, to=100, width=5,
                             textvariable=var_1, font=("Arial", 12))
    label_maxcg.grid(column=0, row=0, sticky=W)
    selector_maxcg.grid(column=0, row=1, sticky=W)
    selector_maxcg.focus()

    label_mincg = Label(window, text="Min CG%", font=("Arial", 12))
    selector_mincg = Spinbox(window, from_=0, to=100, width=5,
                             textvariable=var_2, font=("Arial", 12))
    label_mincg.grid(column=0, row=2, sticky=W)
    selector_mincg.grid(column=0, row=3, sticky=W)

    label_maxtm = Label(window, text="Max Tm", font=("Arial", 12))
    selector_maxtm = Spinbox(window, from_=0, to=100, width=5,
                             textvariable=var_3, font=("Arial", 12))
    label_maxtm.grid(column=0, row=4, sticky=W)
    selector_maxtm.grid(column=0, row=5, sticky=W)

    label_mintm = Label(window, text="Min Tm", font=("Arial", 12))
    selector_mintm = Spinbox(window, from_=0, to=100, width=5,
                             textvariable=var_4, font=("Arial", 12))
    label_mintm.grid(column=0, row=6, sticky=W)
    selector_mintm.grid(column=0, row=7, sticky=W)

    label_maxlen = Label(window, text="Max primer length", font=("Arial", 12))
    selector_maxlen = Spinbox(window, from_=0, to=100, width=5,
                              textvariable=var_3, font=("Arial", 12))
    label_maxlen.grid(column=0, row=4, sticky=W)
    selector_maxlen.grid(column=0, row=5, sticky=W)

    label_minlen = Label(window, text="Min primer length", font=("Arial", 12))
    selector_minlen = Spinbox(window, from_=0, to=100, width=5,
                              textvariable=var_4, font=("Arial", 12))
    label_minlen.grid(column=0, row=6, sticky=W)
    selector_minlen.grid(column=0, row=7, sticky=W)

    continue_button = Button(window, text="Continue",
                             command=lambda: window.quit())
    continue_button.grid(column=2, row=7, sticky=E)

    window.mainloop()

    max_cg = selector_maxcg.get()
    min_cg = selector_mincg.get()
    max_tm = selector_maxtm.get()
    min_tm = selector_mintm.get()
    max_len = selector_maxlen.get()
    min_len = selector_minlen.get()

    return [max_cg, min_cg, max_tm, min_tm, max_len, min_len]


def main():

    para_list = list(gui_2())

    print(para_list)


main()
