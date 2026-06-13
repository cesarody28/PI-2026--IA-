
# Abrir arquivo
arquivo_clientes = open("cadastro_clientes_pizzaria.csv", "r", encoding="utf-8")

# Excluir cabeçalho
arquivo_clientes.readline()

# Ler um registro do arquivo
registros = arquivo_clientes.readlines()

# Ler uma linha 
for um_registro in registros:

# Quebrar a linha nos campos
dados_do_registro = um_registro.strip(),split(",")

# Guardar cada dado em uma variável
telefone, nome, endereco, complemento_endereco, bairro = dados_do_registro 

# Fechar arquivo
arquivo_clientes.close()

# Listar clientes
print(registros)