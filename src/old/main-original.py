from DNAToolkit import *
from utilities import colored
import random

# rndDNAStr = "ATTTCGT"
randDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(50)])

# print(validateSeq(rndDNAStr))
# print(validateSeq(randDNAStr))
# print(countNucFrequency(randDNAStr))

DNAStr = validateSeq(randDNAStr)
print('---------------------------------------------------------------------------')
print('PROJECT: DNA TO PROTEINS')


print('---------------------------------------------------------------------------')
print(f'\nSequence: {colored(DNAStr)}\n')


print('---------------------------------------------------------------------------')
print(f'[STEP 1] + Sequence Length: {len(DNAStr)}\n')


print('---------------------------------------------------------------------------')
print(colored(
    f'[STEP 2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))


print('---------------------------------------------------------------------------')
print(
    f'[STEP 3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}\n')


print('---------------------------------------------------------------------------')
print('[STEP 4] + DNA String + Reverse Complement: \n')
print(f"5' {colored(DNAStr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {colored(complement(DNAStr))} 5'  [Complement]\n")
print(f"5' {colored(reverse_complement(DNAStr))} 3'  [Reverse Complement]")


print('---------------------------------------------------------------------------')
print(f'[STEP 5] + GC Content: {gc_content(DNAStr)}%\n')


print('---------------------------------------------------------------------------')
print(
    f'[STEP 6] + GC Content ins subsection k=5: {gc_content_subsec(DNAStr, k=5)}\n')


print('---------------------------------------------------------------------------')
print(
    f'[STEP 7] + Aminoacids Sequence from DNA: {translate_seq(DNAStr, 0)}\n')


print('---------------------------------------------------------------------------')
print(f'[STEP 8] + Codon frequency (L):{codon_usage(DNAStr,"L")}')


print('---------------------------------------------------------------------------')
print('[STEP 9] + Reading frames:')

for gen in gen_reading_frames(DNAStr):
    print(gen)


print('---------------------------------------------------------------------------')
test_rf_frame = ['L', 'M', 'T', 'A', 'L', 'V', 'V',
                 'L', 'V', 'R', 'R', 'G', 'S', '_', 'G', 'H', 'L', 'M', 'T', 'A', 'L', 'V', 'V',
                 'L', 'V', 'R', 'R', 'G', 'S', '_', 'G', 'H']

print(f'Proteins from rf: {proteins_from_rf(test_rf_frame)}')


print('---------------------------------------------------------------------------')
print('[STEP 10] + Amino acids names:')
#test_protein_frame = ['MTALVVLVRRGS', 'MTALVVLVRRGS']

print(f'Amino acids from amino: {name_from_amino(test_rf_frame)}')


# print('---------------------------------------------------------------------------')
#print('[PROCESO N° 11] + Food with amino:')
#test_protein_frame = ['MTALVVLVRRGS', 'MTALVVLVRRGS']

#print(f'Ami from amino: {food_from_amino(test_rf_frame)}')
