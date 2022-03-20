
#---------------------------------------------------------------------------------------------------------------------#
pergunta = ''
guardar_nomes = []

while pergunta != '0':
    nome = str(input('\nDigite um nome: '))
    guardar_nomes.append(nome)
    parar = str(input('Se deseja parar a contagem digite: "0"\nSe deseja continuar digite qualquer outro valor!\n'))
    pergunta = parar


print(f'Nomes atuais na lista: {guardar_nomes}')


#---------------------------------------------------------------------------------------------------------------------#

guardar_idade = []
tamanho_lista_nomes = len(guardar_nomes)
dados_usuarios = []

for ler_nomes in range (tamanho_lista_nomes):
    pergunta_idade = int(input(f'\nDigite a idade deste usuário: {guardar_nomes[ler_nomes]} \n'))
    guardar_idade.append(pergunta_idade)

    #print(guardar_nomes[ler_nomes], ': ' , guardar_idade[ler_nomes])

    dados_usuarios.append([guardar_nomes[ler_nomes], pergunta_idade])

print(dados_usuarios)

