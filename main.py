#Quiz educativo em python

#Capa do jogo
print("=" * 35)
print("       QUIZ DE CONHECIMENTOS")
print("=" * 35)

print("\nBem-vindo(a) ao nosso Quiz!")
print("Teste seus conhecimentos e acumule pontos!")

#Regras do jogo
print("\nREGRAS:")
print("- O jogo possui perguntas de múltipla escolha.")
print("- Cada pergunta possui 4 alternativas.")
print("- Cada resposta correta vale 10 pontos.")

print("\nPrepare-se para começar!")

#Lista com as perguntas do quiz
perguntas = [
    {
        "pergunta": "Qual linguagem estamos utilizando?",
        "alternativas": [
            "A) Java",
            "B) Python",
            "C) PHP",
            "D) C++"
        ],
        "resposta": "B"
    },
    {
        "pergunta": "Qual comando exibe uma mensagem no Python?",
        "alternativas": [
            "A) print()",
            "B) return()",
            "C) input()",
            "D) import()"
        ],
        "resposta": "A"
    },
    {
        "pergunta": "Qual estrutura permite repetir comandos?",
        "alternativas": [
            "A) if",
            "B) else",
            "C) print",
            "D) for"
        ],
        "resposta": "D"
    }
]

print("\nPerguntas cadastradas:", len(perguntas))

#Iniciando a pontuação
pontuacao = 0

#Fazendo as perguntas
for pergunta in perguntas:

    print("\n" + pergunta["pergunta"])

    for alternativa in pergunta["alternativas"]:
        print(alternativa)

    resposta = input("\nDigite sua resposta (A, B, C ou D): ")

    if resposta.upper() == pergunta["resposta"]:
        print("Parabéns! Você acertou!")
        pontuacao += 10
    else:
        print("Que pena! Você errou.")
        print("Resposta correta:", pergunta["resposta"])

print("\n================================")
print("FIM DO QUIZ!")
print("Sua pontuação foi:", pontuacao)
print("================================")
