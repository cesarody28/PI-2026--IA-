bairros = {}

with open("cadastro_clientes_pizzaria.csv", "r", encoding="utf-8") as arquivo_clientes:

    arquivo_clientes.readline()  # Ignora cabeçalho

    registros = arquivo_clientes.readlines()

    for um_registro in registros:
        dados_do_registro = um_registro.strip().split(",")
        telefone, nome, endereco, complemento, bairro = dados_do_registro
        
        if bairro in bairros:
            bairros[bairro] += 1
        else:
            bairros[bairro] = 1

print("Distribuição por bairro:")

print (bairros)

for bairro, quant in bairros.items():
    print(f"{bairro}: {quant}", "clientes")

print("Bairros atendidos:", len(bairros))