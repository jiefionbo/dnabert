from Bio import SeqIO

def read_fasta(input_file, output_file):
    with open(input_file, "r") as in_handle, open(output_file, "w") as out_handle:
        for record in SeqIO.parse(in_handle, "fasta"):
            sequence = str(record.seq)
            label = 0
            for i in range(0, len(sequence) - 1000 + 1, 100):
                sub_sequence = sequence[i:i + 1001]
                if i // 100 >= 41 and i // 100 <= 51:
                    label = 1
                else:
                    label = 0
                out_handle.write(f"{sub_sequence} {label}\n")

if __name__ == "__main__":
    # C:\Users\yamaguchi\OneDrive - Kyushu University\lab\Member\Yamaguchi\date
    input_fasta_file = "/home/yamaguchi/OneDrive - Kyushu University/lab/Member/Yamaguchi/date/TATA.txt"
    output_fasta_file = "/home/yamaguchi/OneDrive - Kyushu University/lab/Member/Yamaguchi/date/TATA.txt"
    read_fasta(input_fasta_file, output_fasta_file)

