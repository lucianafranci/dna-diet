from DNAToolkit import *
from utilities import colored, readFastaFile
import random

randDNAStr = 'TGGCTATAATAACGCTCCCACGGGTTGATGCCTTGGCAAAAGTTTGGACTATCGGTGGGACGAGACCACTGTCAGTACACGGTCC'
#randDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(50)])

DNAStr = validateSeq(randDNAStr)
print('---------------------------------------------------------------------------')
print('PROYECTO REINA DEL MUNDO - DNA DIET')


print('---------------------------------------------------------------------------')
print(f'\nSequence: {colored(DNAStr)}\n')

print('---------------------------------------------------------------------------')
print(f'[PROCESO N° 1] - Sequence Length: {len(DNAStr)}\n')


print('---------------------------------------------------------------------------')
print(colored(
    f'[PROCESO N° 2] - Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))

print('---------------------------------------------------------------------------')
print(
    f'[PROCESO N° 3] - DNA/RNA Transcription: {colored(transcription(DNAStr))}\n')

print('---------------------------------------------------------------------------')
print('[PROCESO N° 4] - DNA String + Reverse Complement: \n')
print(f"5' {colored(DNAStr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {colored(complement(DNAStr))} 5'  [Complement]\n")
print(f"5' {colored(reverse_complement(DNAStr))} 3'  [Reverse Complement]")

print('---------------------------------------------------------------------------')
print(f'[PROCESO N° 5] - GC Content: {gc_content(DNAStr)}%\n')

print('---------------------------------------------------------------------------')
print(
    f'[PROCESO N° 6] - GC Content in subsection k=5: {gc_content_subsec(DNAStr, k=5)}\n')

print('---------------------------------------------------------------------------')
print('[PROCESO N° 7] - Aminoacids Sequence from DNA')
# trauccion de cadena DNA a Amino
aminoStr = translate_seq(DNAStr, 0)

print(aminoStr)

print('---------------------------------------------------------------------------')
print('[PROCESO N° 8] - Amino names:')
name_from_amino(aminoStr)

print('---------------------------------------------------------------------------')
print('[PROCESO N° 9] - Not found amino names:')
print(f'Total not found amino count: {amino_not_present(aminoStr)}')

print('---------------------------------------------------------------------------')
print('[PROCESO N° 10] - Generate chart:')
amino_chart(aminoStr)
