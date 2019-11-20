def file_reader(file_name, reverse=False):

    with open(file_name) as file:
        seq_list = []
        for line in file:
            line = line.replace(" ", "").rstrip()
            if reverse:
                seq_list.append(complementing_strand(line.upper()))
            else:
                seq_list.append(line)

    return seq_list


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
