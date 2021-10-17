import collections
import numpy as np
import matplotlib.pyplot as plt
from typing import Counter
from config.structures import *


def validateSeq(dna_seq):
    """Valida una secuencia de ADN y retorna False si no es correcta"""
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


def countNucFrequency(seq):
    """Cuenta cantidad de nucleótidos en una secuencia"""
    # diccionario
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict


def countNucFrequencySimple(seq):
    """Cuenta cantidad de nucleótidos en una secuencia (optimizada)"""
    # con diccionarios y colecciones
    return dict(collections.Counter(seq))


def transcription(seq):
    """ DNA -> RNA Transcription. Replacing Thymine with Uracil"""
    return seq.replace("T", "U")


def complement(seq):
    """Complement string: Swapping A-T, G-C"""
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])


def reverse_complement(seq):
    """Reverse string: Swapping A-T, G-C"""
    # return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]

    # Pythonic approach, A little bit faster solution (optimizado)
    mapping = str.maketrans('ATCG', 'TAGC')
    return seq.translate(mapping)[::-1]


def gc_content(seq):
    """GC Content in a DNA/RNA sequence"""
    return round(((seq.count('C') + seq.count('G')) / len(seq) * 100), 6)


def gc_content_subsec(seq, k=20):
    """GC Content in DNA/RNA sub-sequence length k. k=20 by default"""
    # calcula gc_content en ventana de K=20
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i+k]
        res.append(gc_content(subseq))
    return res


def translate_seq(seq, init_pos=0):
    """Translates a DNA sequence into an aminoacid sequence"""
    return [DNA_Codons[seq[pos:pos+3]] for pos in range(init_pos, len(seq)-2, 3)]


def codon_usage(seq, aminoacid):
    """Provides the frequency of each codon ecoding a given aminoacid in a DNA sequence"""
    tmpList = []
    for i in range(0, len(seq) - 2, 3):
        if DNA_Codons[seq[i:i+3]] == aminoacid:
            tmpList.append(seq[i:i+3])

    freDict = dict(Counter(tmpList))
    totalWight = sum(freDict.values())
    for seq in freDict:
        freDict[seq] = round(freDict[seq]/totalWight, 2)

    return freDict


def gen_reading_frames(seq):
    """Generate the six reading frames of a DNA sequence, including the reverse complement"""
    frames = []
    frames.append(translate_seq(seq, 0))
    frames.append(translate_seq(seq, 1))
    frames.append(translate_seq(seq, 2))
    frames.append(translate_seq(reverse_complement(seq), 0))
    frames.append(translate_seq(reverse_complement(seq), 1))
    frames.append(translate_seq(reverse_complement(seq), 2))
    return frames


def proteins_from_rf(aa_seq):
    """Compute all possible proteins in an aminoacid seq and return a list of possible proteins"""
    current_pos = []  # proteina actual (donde se ira creando)
    proteins = []  # proteinas encontradas (banco de proteinas)
    for aa in aa_seq:
        if aa == "_":
            # STOP accumulating amino acid if _ - STOP was found
            if current_pos:
                for p in current_pos:
                    proteins.append(p)
                current_pos = []
        else:
            # START accumulating amino acids if M - START was found
            if aa == "M":
                current_pos.append("")
            for i in range(len(current_pos)):
                current_pos[i] += aa
    return proteins


def name_from_amino(aa_seq, init_pos=0):
    """Translates a DNA sequence into an aminoacid sequence"""
    aa_seq_unique = list(dict.fromkeys(aa_seq))
    aa_seq_unique = sorted(aa_seq_unique)

    # contar los aa
    amino_count = countAminoFrequency(aa_seq)
    #print(f'>>>> {amino_count["A"]}')

    # de la lista de amino, mostrar los no repetidos
    print('Amino encontrados...')
    for amino in aa_seq_unique:
        contador = 0
        if amino != "_":
            print(f' {amino} - {AMINO_NAME[amino]} ({amino_count[amino]})')
            contador = contador + 1

    print(f'Total Amino count: {len(aa_seq_unique)}')
    print(f'Total Amino count: {amino_count}')
    return


def amino_not_present(aa_seq):
    """Identify aminos not present"""
    aa_seq_unique = list(dict.fromkeys(aa_seq))
    # aa_seq_unique = sorted(aa_seq_unique)
    # print(aa_seq_unique)
    # print(AMINOS)
    aa_not_found = np.setdiff1d(AMINOS, aa_seq_unique, False).tolist()
    # print(aa_not_found)

    # de la lista de amino, mostrar los no repetidos
    print('Amino no encontrados...')
    for amino in aa_not_found:
        # contador = 0
        if amino != "_":
            print(' [' + amino + '] - ' + AMINO_NAME[amino])
            # contador = contador + 1
    return len(aa_not_found)


def countAminoFrequency(seq):
    """Cuenta cantidad de aminoacids en una secuencia"""
    # diccionario
    tmpFreqDict = {"A": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "K": 0, "L": 0,
                   "M": 0, "N": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "V": 0, "W": 0, "Y": 0, "_": 0}
    for aa in seq:
        tmpFreqDict[aa] += 1
    return tmpFreqDict


def food_from_amino(aa_seq, init_pos=0):
    """Translates a DNA sequence into an aminoacid sequence"""
    aa_seq_unique = list(dict.fromkeys(aa_seq))

    # de la lista de amino, mostrar los no repetidos

    for amino in aa_seq_unique:
        # proteins.append(AMINO_NAME[aa])
        if amino != "_":
            print('Amino encontrado: [' + amino + '] - ' + AMINO_FOOD[amino])

    return ''


def amino_chart(aa_seq):
    """Genera chart de barras de contadores de amino"""
    # diccionarios de contadores de aminoacid
    amino_count = countAminoFrequency(aa_seq)

    amino = []  # aminos
    contador = []  # cantidad de aminos
    for element in amino_count:
        amino.append(element)
        contador.append(amino_count[element])

    #print(f'Aminos: {amino}')
    #print(f'Contadores: {contador}')

    plt.bar(amino, contador)
    plt.title('Cantidad de aminoácidos')
    plt.xlabel('Aminoácidos')
    plt.ylabel('Cantidad (u)')
    plt.show()
