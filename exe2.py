loja_carros = {
    'roxo': {'nome': 'Fusca', 'preco': 35000},
    'vermelho': {'nome': 'Civic', 'preco': 45000},
    'branco': {'nome': 'Corolla', 'preco': 40000}
}

# Obter o preço e nome do carro roxo
roxo = loja_carros.get('roxo', {})
print('Roxo:', roxo)

# Atualizar o carro roxo e adicionar um carro preto
loja_carros.update({
    'roxo': {'nome': 'Fusca', 'preco': 37000},
    'preto': {'nome': 'BMW', 'preco': 55000}
})

# Imprimir o dicionário atualizado
print(loja_carros, '#Carro preto adicionado')

# Exibir todos os carros com seus respectivos preços
for chave, valor in loja_carros.items():
    print(f'Cor: {chave}, Carro: {valor["nome"]}, Preço: {valor["preco"]}')