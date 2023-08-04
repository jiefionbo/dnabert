from Bio import SeqIO

def read_fasta(input_file, output_file):
    with open(output_file, "w") as out_handle:
        for record in SeqIO.parse(input_file, "fasta"):
            sequence = str(record.seq)
            for i in range(len(sequence) - 300 + 1):
                sub_sequence = sequence[i:i + 300]
                out_handle.write(f"{sub_sequence}\n")

if __name__ == "__main__":
    input_fasta_file = "/home/yamaguchi/DNABERT/examples/TATA.txt"
    output_fasta_file = "/home/yamaguchi/DNABERT/examples/fasta_TATA.txt"
    read_fasta(input_fasta_file, output_fasta_file)
