import pandas as pd

# Funnção que eleva ao cubo
def eleva_ao_cubo(x):
    return x ** 3

# Função lambda que eleva ao cubo
# eleva_ao_cubo_lambda = lambda x: x ** 3

# print(eleva_ao_cubo(2))
# print(eleva_ao_cubo_lambda(2))

df = pd.DataFrame({'Numeros':[1,2,3,4,5,6,7,8,9,10]})

df['cubo função'] = df['Numeros'].apply(eleva_ao_cubo)
df['cubo lambda'] = df['Numeros'].apply(lambda x: x ** 3)

print(df)