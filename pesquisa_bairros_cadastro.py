
# Abrir arquivo
arquivo_clientes = open("cadastro_clientes_pizzaria.csv", "r", encoding="utf-8")

# Excluir cabeçalho
arquivo_clientes.readline()

# Ler uma linha 
registros = arquivo_clientes.readlines()


bairros = {}


for um_registro in registros:

    dados_do_registro = um_registro.strip().split(",")

    telefone, nome, endereco, complemento, bairro = dados_do_registro


    # Verifica se o bairro já existe no dicionário
if bairro in bairros:
        bairros[bairro] = bairros[bairro] + 1
else:
        bairros[bairro] = 1

# Mostrar a distribuição por bairro
print("Distribuição por bairro:")

for bairro in bairros:
    print(bairro, ":", bairros[bairro], "clientes")


# Mostrar bairros atendidos:
print("Bairros atendidos:", len(bairros))

arquivo_clientes.close()