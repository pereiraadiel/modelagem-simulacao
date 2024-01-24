## D&D (Vantagem)
import numpy as np
import matplotlib.pyplot as plt

NUM_DADOS = 2
NUM_FACES = 20
NUM_ROLAGENS = int(1e6)
rolagens = []

def rolarDados(num_dados = 1):
		total = 0
		for i in range(num_dados):
			total += np.random.randint(1, NUM_FACES + 1)
		return total

for i in range(NUM_ROLAGENS):
		rolagens.append(max(rolarDados(NUM_DADOS - 1), rolarDados(NUM_DADOS - 1)))

print('NUM_DADOS: ', NUM_DADOS)

print(np.sum(rolagens)/len(rolagens))

plt.hist(rolagens, align='left', bins= range(1, (NUM_DADOS - 1) * NUM_FACES + 2), rwidth=0.8, edgecolor='black', orientation='vertical')
plt.grid(axis='x', alpha=0.7)
plt.show()