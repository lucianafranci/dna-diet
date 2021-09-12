from DNAToolkit import *
from utilities import colored
from helpers import (preInit,
                     printOnConsole,
                     executeOnBucle)
from view import *
import random


def imprimirDNATabla():
    randDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(50)])
    DNAStr = validateSeq(randDNAStr)

    # [1] secuencia ADN
    data_table = []
    titulo = 'Secuencia'
    contenido = colored(DNAStr)

    detalle = f'Sequence Length: {len(DNAStr)}\n'
    detalle = detalle + \
        colored(f'Nucleotide Frequency: {countNucFrequency(DNAStr)}\n')
    detalle = detalle + f'GC Content: {gc_content(DNAStr)}%\n'

    data_table.append([contenido, detalle])
    printSingleTable(data_table, titulo, heading_row=False)

    # [2] DNA/RNA trancripción
    data_table = []
    titulo = 'DNA/RNA Transcription'
    contenido = colored(transcription(DNAStr))
    detalle = ''
    data_table.append([contenido, detalle])
    printSingleTable(data_table, titulo, heading_row=False)

    # [3] Reverse complement
    data_table = []
    titulo = 'DNA String + Reverse Complement'
    contenido = ''

    contenido = f"5' {colored(DNAStr)} 3'\n"
    contenido = contenido + \
        f"   {''.join(['|' for c in range(len(DNAStr))])}\n"
    contenido = contenido + \
        f"3' {colored(complement(DNAStr))} 5'  [Complement]\n"
    contenido = contenido + \
        f"\n5' {colored(reverse_complement(DNAStr))} 3'  [Reverse Complement]"
    detalle = ''
    data_table.append([contenido, detalle])
    printSingleTable(data_table, titulo, heading_row=False)

    # [4] Aminoacid Sequence
    data_table = []
    titulo = 'Aminoacids Sequence from DNA'
    contenido = translate_seq(DNAStr, 0)
    detalle = f'Codon frequency (L):{codon_usage(DNAStr,"L")}'
    data_table.append([contenido, detalle])
    printSingleTable(data_table, titulo, heading_row=False)

    # [5] Reading frames
    data_table = []
    titulo = 'Reading frames'

    contenido = ''
    detalle = ''
    cont = 0
    for gen in gen_reading_frames(DNAStr):
        contenido = contenido + f'{gen}\n'
        detalle = detalle + f'{proteins_from_rf(gen)}\n'

    data_table.append([contenido, detalle])
    printSingleTable(data_table, titulo, heading_row=False)
