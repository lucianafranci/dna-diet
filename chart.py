import matplotlib.pyplot as plt

Amino = ['A', 'C', 'D', 'E', 'F', 'G',
         'H', 'I', 'K', 'L', 'M', 'N',
         'P', 'Q', 'R', 'S', 'T', 'V',
         'W', 'Y', '_']
Contador = [375, 635, 290, 270, 593, 394,
            332, 436, 413, 886, 117, 472,
            292, 325, 558, 810, 679, 548,
            263, 505, 774]

plt.bar(Amino, Contador)
plt.title('Cantidad de amino')
plt.xlabel('Amino')
plt.ylabel('Cantidad')
plt.show()
