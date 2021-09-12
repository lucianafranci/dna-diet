import collections
from typing import Counter
from structures import *


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
