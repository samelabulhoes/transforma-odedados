def converter_para_float(valores):
    valores_float = []
    for valor in valores:
        valor = valor.replace(".", "").replace(",", ".")
        valores_float.append(float(valor))
    return valores_float

# Testando a função com a lista de exemplo
valores = ["1.000", "2.000,50", "3.500", "4.200,00", "5.000"]
valores_convertidos = converter_para_float(valores)
print(valores_convertidos)
