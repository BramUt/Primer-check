from tkinter import *
from tkinter import scrolledtext, messagebox


def gui():

    def clicked_5():
        raw_seq_5 = txt_5.get("1.0", END)
        txt_5.configure(state='disabled')

    def clicked_3():
        raw_seq_5 = txt_3.get("1.0", END)
        txt_3.configure(state="disabled", bg="grey")

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

    forward_file = "Potential primers"
    reverse_file = "Potential reverse primers"

    forward_seq_list = file_reader(forward_file)
    reverse_seq_list = file_reader(reverse_file, reverse=True)

    forward_info_list = seq_info(forward_seq_list)
    reverse_info_list = seq_info(reverse_seq_list)

    file_writer(forward_info_list, reverse_info_list)


main()
