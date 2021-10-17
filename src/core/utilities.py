from Bio import SeqIO


def colored(seq):
    """Retorna secuencia coloreada"""
    bcolors = {
        'A': '\033[92m',
        'C': '\033[94m',
        'G': '\033[93m',
        'T': '\033[91m',
        'U': '\033[91m',
        'reset': '\033[0;0m'
    }

    tmpStr = ""

    for nuc in seq:
        if nuc in bcolors:
            tmpStr += bcolors[nuc] + nuc
        else:
            tmpStr += bcolors['reset'] + nuc

    return tmpStr + '\033[0;0m'


def readFileToList(input_file):
    """Reading a fila an returning a list of lines"""
    with open(input_file, 'r') as f:
        return[l.strip() for l in f.readlines()]


def readFastaFile(input_file):
    dna_sequece = ''
    for seq_record in SeqIO.parse(input_file, "fasta"):
        # print(seq_record.id)
        # print(repr(seq_record.seq))
        # print(len(seq_record))
        dna_sequece = dna_sequece + seq_record.seq

    # limpiar caracteres raros
    dna_sequece = dna_sequece.replace("N", "")
    return dna_sequece
