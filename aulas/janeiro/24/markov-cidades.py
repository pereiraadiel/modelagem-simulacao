## D&D (Vantagem)
import numpy as np
import matplotlib.pyplot as plt

matriz_transicao = np.array([[0.2, 0.3, 0.5], [0.6, 0, 0.4], [0.1, 0.7, 0.2]]) # probabilidades de saindo de cada cidade chegar em cada uma das outras em 1 passo
cidades = ['Amsterdam', 'Berlin', 'Copenhagen']
cidade_atual = 0
visitas = [0, 0, 0]

# caminhar
passos = int(3.14159596e5)
for i in range(passos):
	# print(f"passo:", i + 1," | cidade atual:", cidades[cidade_atual])
	visitas[cidade_atual] += 1
	cidade_atual = np.random.choice([0,1,2], p=matriz_transicao[cidade_atual])

print(visitas)
print(np.divide(visitas, passos))