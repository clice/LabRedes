import numpy as np

d_duracao = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])
d_taxa_bits = np.array([560, 698, 577, 617, 553, 612, 575, 565, 641, 624, 650, 637, 567, 621, 619, 638, 598, 628, 639, 664, 626, 598, 627, 654, 628, 635])

r = np.corrcoef(d_duracao, d_taxa_bits)[0, 1]
print("Coeficiente de correlação de Pearson:", r)
