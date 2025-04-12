import pandas as pd

x = {'name':['Alyne', 'Joaquim'], 'age':[38,42]}

a = pd.DataFrame(x)
b = pd.Series(x)

print(f"Dataframe: \n{a}")
print(f"Series: \n{b}")

