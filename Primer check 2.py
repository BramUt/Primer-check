from tkinter import *
from tkinter import scrolledtext, messagebox
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

        exit_button = Button(window, text="Continue", command=window.quit,
                             state="disabled")
        exit_button.grid(column=3, row=4, sticky=E)

        window.mainloop()


def fun_return():
    return InputGui()


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


def seq_info(seq_list):
    """Takes a list of sequences returns a nested list with the sequences,
    AT count, CG count, CG% and smelting temperature.

    Input:  seq_list - list, list with sequences

    Output: info_list - list, nested list with sequences and information
    """

    info_list = []

    for seq in seq_list:
        seq = seq.upper()
        at_count = seq.count("A") + seq.count("T")
        cg_count = seq.count("C") + seq.count("G")
        cg_perc = round((cg_count / len(seq)*100),2)
        smelt_temp = ((at_count*2) + (cg_count*4))

        temp_list = [seq, cg_count, at_count, cg_perc, smelt_temp]

        info_list.append(list(map(str, temp_list)))

    return info_list


def file_writer(forward_list, reverse_list):
    """Writes the info in the forward_list and rever_list to a .csv file

    Input:  forward_list, list, list with sequences and information
            reverse_list, list, list with sequences and information
    """

    with open("Resultaten.csv", "w") as res_file:
        kopje = str("Forward primers\nSeq 5'-3',CG,AT,CG%,Smelt temp\n")
        res_file.write(kopje)
        for x in forward_list:
            temp_string = str(",".join(x) + "\n")
            res_file.write(temp_string)

        kopje_2 = "\nReverse Primers\nSeq 5'-3',CG,AT,CG%,Smelt temp\n"
        res_file.write(kopje_2)
        for y in reverse_list:
            temp_string = str(",".join(y) + "\n")
            res_file.write(temp_string)


def main():

    res = fun_return()

    pre_seq_3, pre_seq_5 = res.raw_seq_3, res.raw_seq_5

    seq_5 = seq_stove(pre_seq_5).upper()

    med_seq_3 = seq_stove(pre_seq_3).upper()
    seq_3 = complementing_strand(med_seq_3)

    print(med_seq_3)
    print(seq_3)

    print(seq_5)


main()
