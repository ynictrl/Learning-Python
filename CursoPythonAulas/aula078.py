# exercicio - sistema de perguntas e respostas

questions = [
    {
        'question': 'Qual é a capital do Brasil?',
        'options': ['Serrinha', 'Alcântara', 'Brasília', 'Amazonas'],
        'response': 'Brasília',
    },
    {
        'question': 'Quem descobriu o Brasil?',
        'options': ['Índegenas', 'Pedro Álvares Cabral', 'Lula', 'Ronaldinho Gaucho'],
        'response': 'Índegenas',
    },
    {
        'question': 'Qual é o idioma do Brasil?',
        'options': ['Espanhol', 'Português', 'Inglês', 'Brasileiro'],
        'response': 'Português',
    },
]

def quiz():
    successes = 0
    for i in range(len(questions)):
        correct = False
        print(questions[i]['question'])

        for k in range(len(questions[i]['options'])):
            curr = questions[i]['options'][k]
            print(f'{k}) {curr}')

        reply = input()
        if reply.isdigit() is True:
            int_reply = int(reply)

            if 0 <= int_reply <= len(questions[i]['options']):

                if questions[i]['options'][int_reply] == questions[i]['response']:
                    successes += 1
                    correct = True

        if correct is True:
            print('Você acertou!')
        else:
            print('Você errou!')

    print(f'Você acertou {successes}/{len(questions)}')
            
quiz()

# try:
        #     reply = input()
        #     curr = questions[i]['options'][int(reply)] 
        #     if curr == questions[i].get('response'): 
        #         print('Você Acertou! :)')
        #         successes += 1
        #         continue
        #     else:
        #         print('Você Errou! :(')
        #         continue
        # except:
        #     print('Você Errou! :(')
        #     continue

