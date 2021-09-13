Nucleotides = ["A", "C", "G", "T"]

DNA_ReverseComplement = {
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G'
}

NUCLEOTIDE_BASE = {
    "DNA": ["A", "T", "C", "G"],
    "RNA": ["A", "U", "C", "G"]
}


DNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "_", "TAG": "_", "TGA": "_"
}

RNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UGU": "C", "UGC": "C",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UUU": "F", "UUC": "F",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAU": "H", "CAC": "H",
    "AUA": "I", "AUU": "I", "AUC": "I",
    "AAA": "K", "AAG": "K",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUG": "M",
    "AAU": "N", "AAC": "N",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UGG": "W",
    "UAU": "Y", "UAC": "Y",
    "UAA": "_", "UAG": "_", "UGA": "_"
}

AMINOS = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L",
          "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y", "_"]

#
# Nombre de cada nucleotido
AMINO_NAME = {
    "A": "ALANINE",
    "C": "CISTEINE",
    "D": "ASPARTIC ACID",
    "E": "GLUTAMIC ACID",
    "F": "PHENYLALANINE",
    "G": "GLYCINE",
    "H": "HISTIDINE",
    "I": "ISOLEUCINE",
    "K": "LYSINE",
    "L": "LEUCINE",
    "M": "METHIONINE",
    "N": "ASPARAGINE",
    "P": "PROLINE",
    "Q": "GLUTAMINE",
    "R": "ARGININE",
    "S": "SERINE",
    "T": "THREONINE",
    "V": "VALINE",
    "W": "THRYPTOPHAN",
    "Y": "TYROSINE",
    "_": "END"
}

# Relación aminoacido / comida
# Pendiente
AMINO_FOOD = {
    "A": "ZAPALLO",
    "C": "ZAPALLO",
    "D": "ZAPALLO",
    "E": "ZAPALLO",
    "F": "ZAPALLO",
    "G": "ZAPALLO",
    "H": "ZAPALLO",
    "I": "ZAPALLO",
    "K": "ZAPALLO",
    "L": "MANZANA", "M": "MANZANA", "R": "MANZANA",
    "N": "ZAPALLO",
    "P": "ZAPALLO",
    "Q": "ZAPALLO",
    "R": "ZAPALLO",
    "S": "ZAPALLO",
    "T": "ZAPALLO",
    "V": "ZAPALLO",
    "W": "ZAPALLO",
    "Y": "ZAPALLO",
    "_": "ZAPALLO"
}

# pendiente
PROTEINS_FOOD = {
    "MTALVVLVRRGS": "PAPA", "MTALVVLVRRSS": "PAPA",
    "MTALVVLVRRGS": "ZAPALLO"
}
