import numpy as np
import matplotlib.pyplot as plt

NUM_EXPIREMENTS = int(1e5)

sorteados = []

for i in range(NUM_EXPIREMENTS):
	white = 7
	black = 5
	
	whiteProbability = (white/(white + black))
	blackProbability = (black/(white + black))
	
	sorteado = 0

	for j in range(5):
		sorteado = np.random.choice(['W', 'B'], p=[whiteProbability, blackProbability])
		if(sorteado == 'W'):
			white -= 1
		else:
			black -= 1
	sorteados.append(sorteado)

print(sorteados.count('W'))


# plt.hist(retiradas, align='left', bins= range(1, NUM_RETIRADAS * 2), rwidth=0.8, edgecolor='black', orientation='horizontal')
# plt.show()