


# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = input('Quantos GB você consome em média?:')
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
consumo_in_float = float(consumo)
def recomendar_plano():
    numero = 11
    lista_gbs = [11,12,13,14,15,16,17,18,19,20]
    if consumo_in_float == 10:
        print('Plano ideal para você: - Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.')
    elif consumo_in_float in lista_gbs :
        print('Plano ideal para você: - Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.')
    elif consumo_in_float >= 21:
        print('- Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.')

recomendar_plano()