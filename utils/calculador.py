def calcular_consumo_por_segundo(equipamentos_usuario, base_equipamentos):
    gasto_total = 0
    for item in equipamentos_usuario:
        nome = item.get('nome')
        quantidade = item.get('quantidade', 1)
        custo_base = base_equipamentos.get(nome, 0)
        gasto_total += quantidade * custo_base
    return gasto_total

def estimar_consumo_por_hora(gasto_por_segundo):
    return gasto_por_segundo * 3600

def estimar_consumo_por_mes(gasto_por_hora):
    return gasto_por_hora * 3600 * 24 * 30