
# Abrir arquivo
arquivo_clientes = open("cadastro_clientes_pizzaria.csv", "r", encoding="utf-8")

# Excluir cabeçalho
arquivo_clientes.readline()

# Ler uma linha 
registros = arquivo_clientes.readlines()

total_clientes = 0
moram_em_casa = 0
moram_em_condominio = 0


# Quebrar a linha nos campos
for um_registro in registros:
    
    # Quebrar a linha nos campos
    dados_do_registro = um_registro.strip().split(",")

# Guardar cada dado em uma variável
    telefone, nome, endereco, complemento, bairro = dados_do_registro 

    
   
# Contagem de clientes:
total_clientes += 1

# Casa ou condomínio
if complemento != "":
        moram_em_condominio += 1
else:
        moram_em_casa += 1


# Exibir Resultados:
print("Total de clientes:", total_clientes)
print("Clientes em condomínio:", moram_em_condominio)
print("Clientes em casa:", moram_em_casa)

arquivo_clientes.close()