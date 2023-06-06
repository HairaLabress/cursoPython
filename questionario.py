perguntas = [
    {
        'pergunta': 'Quanto é 3*3?',
        'alternativas': ['6', '9', '3', '0'],
        'resposta': '9',
    },
    
    {
        'pergunta': 'Quanto é 20/4?',
        'alternativas': ['5', '2', '1', '12'],
        'resposta': '5',
    },
    
    {
        'pergunta': 'Quanto é 10% de 100?',
        'alternativas': ['10', '100', '1', '11'],
        'resposta': '10',
    },
]

contador = 0
num_acertos = 0
for pergunta in perguntas:
    print(perguntas[contador]['pergunta'])
    
    for valor in perguntas[contador]['alternativas']:
        print(valor)
        
    resp_usuario = input("Digite sua resposta: ")
    if resp_usuario == perguntas[contador]['resposta']:
        print('Voce acertou')
        num_acertos += 1
    else:
        print('Voce errou, a resposta correta é: ', perguntas[contador]['resposta'] )
        
    contador += 1
    
print("O numero de acertos foi: ", num_acertos)
