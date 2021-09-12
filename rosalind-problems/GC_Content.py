def readFileToList(filePath):
    """Reading a fila an returning a list of lines"""
    with open(filePath, 'r') as f:
        return[l.strip() for l in f.readlines()]


def gc_content(seq):
    """GC Content in a DNA/RNA sequence"""
    return round(((seq.count('C') + seq.count('G')) / len(seq) * 100), 6)

# calcular GC Content from FASTA formatted text file


# === Read data from th file (FASTA formatted file)
# Storing File contents in a list
FASTAFile = readFileToList("test_data/gc_content.txt")

# Dictionary fo Labels + Data
FASTADict = {}

# String for holding the current label
FASTALabel = ""

print(FASTAFile)
print(FASTADict)

# Converting FASTA/List file data into a dictionary
for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

# === Format the data
# Using dictionary comprhension to generate a new dictionary with GC Content
RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items()}
print(RESULTDict)

# Looking for max value
MaxGCKey = max(RESULTDict, key=RESULTDict.get)

print(f'Maximo -> {MaxGCKey[1:]}: {RESULTDict[MaxGCKey]}')
