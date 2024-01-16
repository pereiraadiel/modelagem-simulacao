## Probabilidades

#### probabilidade de A dado B

```
	P(A|B) = ( P(B|A) · P(A) ) / P(B)
```

#### probabilidade de B dado A

```
	P(B|A) = ( P(A|B) · P(B) ) / P(A)
```

#### teorema de Bayes
```
	P(B) = P(B|F) · P(F) + P(B|F©) · P(F©)
```

### Exemplos:

### Dado uma caixa com 7 bolas pretas e 5 bolas brancas, queremos "comprar" 2 bolas sem reposição. Qual a possibilidade de ambas serem pretas? E que ambas sejam brancas?

```sh
# probabilidade de tirar uma preta
P(tirar uma preta) = 7 / 12

# probabilidade de tirar uma branca
P(tirar uma branca) = 5 / 12

# probabilidade de tirar uma preta dado que já foi tirada uma preta
P(tirar uma preta | já foi tirada uma preta) = P(já foi tirada uma preta | tirar uma preta) · P(tirar uma preta) / P(já foi tirada uma preta)

```
