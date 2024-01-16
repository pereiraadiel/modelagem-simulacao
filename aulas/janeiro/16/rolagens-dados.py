import numpy as np
import matplotlib.pyplot as plt

NUM_DADOS = 1
NUM_FACES = 6
NUM_ROLAGENS = int(1e5)
rolagens = []

def rolarDados(num_dados = 1):
		total = 0
		for i in range(num_dados):
			total += np.random.randint(1, NUM_FACES + 1)
		return total

for i in range(NUM_ROLAGENS):
		rolagens.append(rolarDados(NUM_DADOS))

print('NUM_DADOS: ', NUM_DADOS)
plt.hist(rolagens, align='left', bins= range(1, NUM_DADOS * NUM_FACES + 2), rwidth=0.8, edgecolor='black')
plt.show()