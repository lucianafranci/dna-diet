from core.DNAToolkit import *
from core.utilities import colored, readFastaFile
import random

# https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2?report=fasta
#randDNAStr = readFastaFile('./fasta-files/fasta-dna-covid.txt')

# https://www.ncbi.nlm.nih.gov/nuccore/U49897.1?report=fasta
#randDNAStr = readFastaFile('./fasta-files/fasta-dna-covid.txt')

# randDNAStr = readFastaFile('./fasta-files/fasta-liver-carboxylesterase.txt') 
#randDNAStr = readFastaFile('./fasta-files/fasta-dna-fen.txt')
randDNAStr = readFastaFile('./fasta-files/fasta-RANDOM.txt')

DNAStr = validateSeq(randDNAStr)
print('---------------------------------------------------------------------------')
print('PROYECTO DE CIENCIAS: TRADUCTOR DE ADN A PROTEINAS')

print('---------------------------------------------------------------------------')
print(f'\nSECUENCIA: {colored(DNAStr)}\n')

print('---------------------------------------------------------------------------')
print(f'[PROCESO N° 1] - Longitud de la secuencia: {len(DNAStr)}\n')

print('---------------------------------------------------------------------------')
print(colored(
    f'[PROCESO N° 2] - Frecuencia de nucleótidos: {countNucFrequency(DNAStr)}\n'))

print('---------------------------------------------------------------------------')
print(
    f'[PROCESO N° 3] - Transcripción de ADN/ARN: {colored(transcription(DNAStr))}\n')

print('---------------------------------------------------------------------------')
print('[PROCESO N° 4] - Cadena de ADN + Complemento inverso: \n')
print(f"5' {colored(DNAStr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {colored(complement(DNAStr))} 5'  [Complemento]\n")

#print(f"5' {colored(reverse_complement(DNAStr))} 3'  [Reverse Complement]")

print('---------------------------------------------------------------------------')
print(f'[PROCESO N° 5] - Contenido de GC: {gc_content(DNAStr)}%\n')

print('---------------------------------------------------------------------------')
print(
    f'[PROCESO N° 6] - Contenido de GC en la subsección k=5: {gc_content_subsec(DNAStr, k=5)}\n')

print('---------------------------------------------------------------------------')
print('[PROCESO N° 7] - Secuencia de aminoácidos del ADN')
# trauccion de cadena DNA a Amino
aminoStr = translate_seq(DNAStr, 0)
print(aminoStr)

print('---------------------------------------------------------------------------')
print('[PROCESO N° 8] + Aminoácidos:')
name_from_amino(aminoStr)

print('---------------------------------------------------------------------------')
print('[PROCESO N° 9] + Aminoácidos no encontrados')
print(f'Total de aminoácidos no encontrados: {amino_not_present(aminoStr)}')

print('---------------------------------------------------------------------------')
print('---------------------------------------------------------------------------')
print('[PROCESO N° 10] - Generar gráfico:')
amino_chart(aminoStr)
