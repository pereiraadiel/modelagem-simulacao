## Caminhada do bebado (1 dimensao: cima-baixo ou esq-dir ou frente-tras)
import numpy as np
import matplotlib.pyplot as plt

NUM_EXPERIMENTOS = int(1e2) * 2
posicoes = []
posicao_atual = 0

for i in range(NUM_EXPERIMENTOS):
	posicao_atual += np.random.choice([-1, 1])
	posicoes.append(posicao_atual)


print(np.sum(posicoes)/len(posicoes))

plt.plot(posicoes)
plt.show()

## Caminhada do bebado (2 dimensao: cima-baixo + esq-dir)
import numpy as np
import matplotlib.pyplot as plt

NUM_EXPERIMENTOS = int(1e2) * 2
posicoes_x = [0]
posicoes_y = [0]
posicao_x = 0
posicao_y = 0

for i in range(NUM_EXPERIMENTOS):
	angulo = np.random.uniform(0, 2 * np.pi)
	posicao_x += np.cos(angulo)
	posicao_y += np.sin(angulo)
	posicoes_x.append(posicao_x)
	posicoes_y.append(posicao_y)

plt.plot(posicoes_x, posicoes_y)
plt.show()

