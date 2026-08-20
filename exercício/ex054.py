sexo = str(input('Informe seu dados [m/f]').strip
().lower())[0]
while sexo not in 'mf':
    sexo = str(input('dados inconsistentes informe novamente').strip().lower())
sexo.lower()[0]
print(f'o seu sexo é {sexo}')
