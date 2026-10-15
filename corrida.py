idade_minima = 16
"""Corrida da Ponte Estaiada - Etapa 1
      Inscrição e resultado de um corredor por vez.
"""


def calcular_valor_incricao(idade, distancia, lote):
    """Calcula o valor da inscrição em reais.

    Regras de negócio:
    1º lote: R$80,00; 2º lote: R$100,00.
    Provas de 5 km têm valor padrão; provas de 10 km têm acréscimo de R$20,00.

        Parâmetros:
            idade: Idade do corredor.
            distancia: Distância da prova, em quilômetros (5 ou 10).
            lote: Lote de inscrição (1 ou 2).
        """
    if lote == 1:
        valor = 80.0
    else:
        valor = 100.0

    if distancia == 10:
        valor += 20.0
    if idade >= 60:
        valor /= 2
    return valor


def selecionar_categoria(idade):
    """Selecionar a categoria do corredor baseado na sua idade.
          Juvenil: 16 a 19 anos;
          Adulto: 20 a 39 anos;
          Master: 40 a 59 anos;
          Veterano: 60 anos ou mais.
       """
    if idade < 16:
        return "Não permitido"
    elif idade <= 19:
        return "Juvenil"
    elif idade <= 39:
        return "Adulto"
    elif idade <= 59:
        return "Master"
    else:
        return "Veterano"


def informar_primeiro_nome(nome_completo):
    """Retorna o primeiro nome."""
    nome = nome_completo.strip()
    posicao = nome.find(" ")
    if posicao == -1:
        return nome
    return nome[:posicao]


def informar_ultimo_nome(nome_completo):
    """Retorna o último nome."""
    nome = nome_completo.strip()
    posicao = nome.rfind(" ")
    return nome[posicao + 1:]


def gerar_codigo(nome_completo, idade):
    """Gera o código do corredor."""
    primeiro = informar_primeiro_nome(nome_completo)
    ultimo = informar_ultimo_nome(nome_completo)
    return primeiro[:3].upper() + ultimo[:3].upper() + str(idade)
