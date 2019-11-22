from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
import re


class InputGui:

    def __init__(self):
        def clicked_5():
            self.raw_seq_5 = txt_5.get("1.0", END)
            txt_5.configure(state="disabled", bg="light grey")

        def clicked_3():
            self.raw_seq_3 = txt_3.get("1.0", END)
            txt_3.configure(state="disabled", bg="light grey")
            exit_button.configure(state="active")

        window = Tk()
        window.title("Primer check 2")
        window.geometry("700x430")

        label_5 = Label(window, text="Enter 5'-UTR")
        txt_5 = scrolledtext.ScrolledText(window, width=40, height=20)
        button_5 = Button(window, text="Enter", command=clicked_5)
        label_5.grid(column=0, row=0, sticky=W)
        txt_5.grid(column=0, row=1)
        button_5.grid(column=0, row=2, sticky=E)
        txt_5.focus()

        label_3 = Label(window, text="Enter 3'-UTR")
        txt_3 = scrolledtext.ScrolledText(window, width=40, height=20)
        button_3 = Button(window, text="Enter", command=clicked_3)
        label_3.grid(column=3, row=0, sticky=W, padx=10)
        txt_3.grid(column=3, row=1, padx=10)
        button_3.grid(column=3, row=2, sticky=E, padx=10)

        exit_button = Button(window, text="Continue",
                             command=lambda: window.quit(),
                             state="disabled")
        exit_button.grid(column=3, row=4, sticky=E)

        window.mainloop()


def fun_return():
    return InputGui()


def gui_2():

    window_2 = Toplevel()
    window_2.title("Primer check 2: parameter")
    window_2.geometry("230x260")

    var_1, var_2, var_3 = IntVar(), IntVar(), IntVar()
    var_4, var_5, var_6 = IntVar(), IntVar(), IntVar()

    var_1.set(60)
    var_2.set(40)
    var_3.set(62)
    var_4.set(55)
    var_5.set(25)
    var_6.set(18)

    label_maxcg = Label(window_2, text="Max CG%", font=("Arial", 12))
    selector_maxcg = Spinbox(window_2, from_=0, to=100, width=5,
                             textvariable=var_1, font=("Arial", 12))
    label_maxcg.grid(column=0, row=0, sticky=W)
    selector_maxcg.grid(column=0, row=1, sticky=W)
    selector_maxcg.focus()

    label_mincg = Label(window_2, text="Min CG%", font=("Arial", 12))
    selector_mincg = Spinbox(window_2, from_=0, to=100, width=5,
                             textvariable=var_2, font=("Arial", 12))
    label_mincg.grid(column=0, row=2, sticky=W)
    selector_mincg.grid(column=0, row=3, sticky=W)

    label_maxtm = Label(window_2, text="Max Tm", font=("Arial", 12))
    selector_maxtm = Spinbox(window_2, from_=0, to=100, width=5,
                             textvariable=var_3, font=("Arial", 12))
    label_maxtm.grid(column=0, row=4, sticky=W)
    selector_maxtm.grid(column=0, row=5, sticky=W)

    label_mintm = Label(window_2, text="Min Tm", font=("Arial", 12))
    selector_mintm = Spinbox(window_2, from_=0, to=100, width=5,
                             textvariable=var_4, font=("Arial", 12))
    label_mintm.grid(column=0, row=6, sticky=W)
    selector_mintm.grid(column=0, row=7, sticky=W)

    label_maxlen = Label(window_2, text="Max primer length", font=("Arial", 12))
    selector_maxlen = Spinbox(window_2, from_=0, to=100, width=5, textvariable=var_5, font=("Arial", 12))
    label_maxlen.grid(column=0, row=8, sticky=W)
    selector_maxlen.grid(column=0, row=9, sticky=W)

    label_minlen = Label(window_2, text="Min primer length", font=("Arial", 12))
    selector_minlen = Spinbox(window_2, from_=0, to=100, width=5,
                              textvariable=var_6, font=("Arial", 12))
    label_minlen.grid(column=0, row=10, sticky=W)
    selector_minlen.grid(column=0, row=11, sticky=W)

    continue_button = Button(window_2, text="Continue",
                             command=lambda: window_2.quit())
    continue_button.grid(column=2, row=11, sticky=E)

    window_2.mainloop()

    max_cg = selector_maxcg.get()
    min_cg = selector_mincg.get()
    max_tm = selector_maxtm.get()
    min_tm = selector_mintm.get()
    max_len = selector_maxlen.get()
    min_len = selector_minlen.get()

    return max_cg, min_cg, max_tm, min_tm, max_len, min_len


def primer_searcher(seq, max_cg, min_cg, max_tm, min_tm, max_len, min_len):

    primer_list = []

    for nuc in range(len(seq)):
        if nuc != len(seq)-min_len:
            for length in range(min_len, max_len):
                temp_seq = seq[nuc: nuc + length]
                info_list = seq_info(temp_seq)
                if min_cg <= info_list[3] <= max_cg and \
                        min_tm <= info_list[4] <= max_tm and \
                        info_list[5] >= min_len:
                    info_list.append(str(nuc+1))
                    primer_list.append(list(map(str, info_list)))

    return primer_list


def seq_stove(raw_seq):
    """Removes any numbers or whitespaces from a sequence

    Input:  raw_seq - str, DNA/RNA sequence

    Output: rare_seq - str, DNA/RNA sequence without numbers or whitespaces
    """

    med_seq = raw_seq.replace(" ", "").replace("\n", "")

    rare_seq = re.sub(r'[0-9]+', "", med_seq)

    return rare_seq


def complementing_strand(seq):
    """Takes a DNA sequence and returns the reverse complementing strand.

    Input:  seq - str, DNA sequence

    Output: comp_seq
    """

    comp_dict = {"A": "T", "C": "G", "G": "C", "T": "A"}
    comp_strand = []

    for char in seq:
        comp_strand.append(comp_dict[char])

    comp_seq = ("".join(comp_strand))
    comp_seq = comp_seq[::-1]

    return comp_seq


def seq_info(seq):
    """Takes a sequence and returns a list with the sequence, cg count,
    at count, cg% smelt temperature and length

    Input:  seq - str, DNA sequence

    Output: a list
    """

    at_count = seq.count("A") + seq.count("T")
    cg_count = seq.count("C") + seq.count("G")
    cg_perc = round((cg_count / len(seq)*100),2)
    smelt_temp = ((at_count*2) + (cg_count*4))
    length = len(seq)

    return [seq, cg_count, at_count, cg_perc, smelt_temp, length]


def file_writer(forward_list, reverse_list):
    """Writes the info in the forward_list and rever_list to a .csv file

    Input:  forward_list, list, list with sequences and information
            reverse_list, list, list with sequences and information
    """

    with open("Resultaten.csv", "w") as res_file:
        kopje = ("Forward primers\nSeq 5'-3',CG,AT,CG%,Smelt temp,"
                 "Length,Position\n")
        res_file.write(kopje)
        for x in forward_list:
            temp_string = str(",".join(x) + "\n")
            res_file.write(temp_string)

        kopje_2 = ("\nReverse Primers\nSeq 5'-3',CG,AT,CG%,Smelt temp,"
                   "Length,Position\n")
        res_file.write(kopje_2)
        for y in reverse_list:
            temp_string = str(",".join(y) + "\n")
            res_file.write(temp_string)


def main():

    res = fun_return()

    pre_seq_3, pre_seq_5 = res.raw_seq_3, res.raw_seq_5

    med_seq_3 = seq_stove(pre_seq_3).upper()
    three_utr_seq = complementing_strand(med_seq_3)

    five_utr_seq = seq_stove(pre_seq_5).upper()

    max_cg, min_cg, max_tm, min_tm, max_len, min_len = list(map(int, gui_2()))

    print("5' UTR\n", five_utr_seq)
    print("3' UTR:\n", three_utr_seq)

    rev_primers = primer_searcher(three_utr_seq, max_cg, min_cg, max_tm,
                                  min_tm, max_len, min_len)

    fw_primers = primer_searcher(five_utr_seq, max_cg, min_cg, max_tm, min_tm,
                                 max_len, min_len)

    file_writer(fw_primers, rev_primers)


main()
