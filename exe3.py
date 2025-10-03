# Dicionário inicial com frutas e preços
loja_fruta = {
    'maca': 2.40,
    'banana': 3.60,
    'uva': 7.60
}

# João quer adicionar mais três frutas e aumentar o preço em 20%
novas_frutas = {
    'laranja': 4.50,
    'morango': 6.00,
    'abacaxi': 5.00
}

# Atualizando preços e incluindo novas frutas
loja_fruta.update(novas_frutas)

# Aumentando 20% no preço das frutas existentes
for chave, valor in loja_fruta.items():
    loja_fruta[chave] = round(valor * 1.20, 2)

# João quer adicionar mais 20 unidades de cada fruta
quantidade_frutas = {
    'maca': 0,  # Vamos remover as maçãs, já que ele vendeu todas
    'banana': 20,
    'uva': 20,
    'laranja': 20,
    'morango': 20,
    'abacaxi': 20
}

# Imprimindo os preços atualizados e as quantidades
for chave, valor in loja_fruta.items():
    print(f"Fruta: {chave} | Preço: {valor} | Quantidade: {quantidade_frutas.get(chave, 0)}")