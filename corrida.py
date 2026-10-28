idade_minima = 16
corredores = []

codigos_usados = set()

CATEGORIAS = (
    ("Juvenil", 16, 19, 1500, 3120),
    ("Adulto", 20, 39, 1320, 2760),
    ("Master", 40, 59, 1500, 3120),
    ("Veterano", 60, 120, 1800, 3780)
)
"""Corrida da Ponte Estaiada - Etapa 1
      Inscrição e resultado de um corredor por vez.
"""


def calcular_valor_inscricao(idade, distancia, lote):
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
    """retorna o primeiro nome;"""
    nome = nome_completo.strip()
    posicao = nome.find(" ")
    if posicao == -1:
        return nome
    return nome[:posicao]


def informar_ultimo_nome(nome_completo):
    """retorna o ultimo nome;"""
    nome = nome_completo.strip()
    posicao = nome.rfind(" ")
    return nome[posicao + 1:]


def gerar_codigo(nome_completo, idade):
    """gera o código do corredor
       3 primeiras letras do primeiro nome(maiúsculas) + 3 primeiras letras do último nome(maiúsculas) + idade;
       exemplo: "Gustavo Patricio Silva", 21 --> 'GUSSIL21';"""

    primeiro = informar_primeiro_nome(nome_completo)
    ultimo = informar_ultimo_nome(nome_completo)
    return primeiro[:3].upper() + ultimo[:3].upper() + str(idade)


def informar_primeiro_nome(nome_completo):
    """retorna o primeiro nome;"""
    nome = nome_completo.strip()
    posicao = nome.find(" ")
    if posicao == -1:
        return nome
    return nome[:posicao]


def informar_ultimo_nome(nome_completo):
    """retorna o ultimo nome;"""
    nome = nome_completo.strip()
    posicao = nome.rfind(" ")
    return nome[posicao + 1:]


def gerar_codigo(nome_completo, idade):
    """gera o código do corredor
       3 primeiras letras do primeiro nome(maiúsculas) + 3 primeiras letras do último nome(maiúsculas) + idade;
       exemplo: "Gustavo Patricio Silva", 21 --> 'GUSSIL21';"""

    primeiro = informar_primeiro_nome(nome_completo)
    ultimo = informar_ultimo_nome(nome_completo)
    return primeiro[:3].upper() + ultimo[:3].upper() + str(idade)


def tempo_valido(tempo):
    """retorna TRUE se o tempo estiver no formato HH:MM:SS válido;
       rejeita '1:07:59', '00h22m00', minutos ou segundos acima de 59 e o tempo zerado;"""
    if len(tempo) != 8:
        return False
    if tempo[2:3] != ":" or tempo[5:6] != ":":
        return False
    horas = tempo[0:2]
    minutos = tempo[3:5]
    segundos = tempo[6:8]
    if not (horas.isdecimal() and minutos.isdecimal() and segundos.isdecimal()):
        return False
    if int(minutos) > 59 or int(segundos) > 59:
        return False
    return int(horas) * 3600 + int(minutos) * 60 + int(segundos) > 0


def converter_tempo_para_segundos(tempo):
    """converter um tempo válido 'HH:MM:SS' para segundos(int);"""
    horas = int(tempo[0:2])
    minutos = int(tempo[3:5])
    segundos = int(tempo[6:8])
    return horas * 3600 + minutos * 60 + segundos


def calcular_pace(tempo_segundos, distancia):
    """retorna o pace calculado em segundos por km;"""
    return tempo_segundos // distancia


def formatar_pace(pace_segundos):
    """formata o pace de segundos por km como texto;
       exemplo: 4'18"/ km;"""
    return f"{pace_segundos // 60}'{pace_segundos % 60:02d}\"km"


def formatar_reais(valor):
    """formata um valor em reais com duas casas;
       exemplo: 'R$80,00';"""
    return f"R$ {valor:.2f}".replace(".", ",")


def obter_tempo_limite(categoria, distancia):
    """Retorna o tempo limite da categoria usando a tupla CATEGORIAS."""
    for nome, idade_minima_cat, idade_maxima_cat, limite_5km, limite_10km in CATEGORIAS:
        if nome == categoria:
            if distancia == 5:
                return limite_5km
            return limite_10km
    return 0


def verificar_premiacao(categoria, distancia, tempo_segundos):
    """retorna TRUE se o tempo for menor ou igual ao limite da sua respectiva categoria;"""
    return tempo_segundos <= obter_tempo_limite(categoria, distancia)


def ler_nome():
    """Pede o nome completo até receber nome e sobrenome."""
    while True:
        nome = input("Nome completo:").strip()
        if " " in nome:
            return nome
        print("Digite o nome completo(nome e sobrenome).")


def ler_idade():
    """Pede idade até receber um inteiro entre 1 e 120"""
    while True:
        texto = input("Idade: ").strip()
        if texto.isdecimal() and 1 <= int(texto) <= 120:
            return int(texto)
        print("Idade inválida. Digite um número inteiro entre 1 e 120.")


def ler_opcao(pergunta, validas):
    """Pede um número até que esteja entre as opções válidas"""
    while True:
        texto = input(pergunta).strip()
        if texto.isdecimal() and int(texto) in validas:
            return int(texto)
        opcoes = " ou ".join(str(v) for v in validas)
        print(f"Opção inválida. Digite {opcoes}.")


def ler_tempo():
    """Pede o tempo até receber um HH:MM:SS válido."""
    while True:
        tempo = input("Tempo de prova (HH:MM:SS): ").strip()
        if tempo_valido(tempo):
            return tempo
        print("Tempo inválido. Use HH:MM:SS, com minutos e segundos até 59.")


def fazer_inscricao(corredores, codigos_usados):
    """Cadastra um corredor e guarda seus dados."""

    nome = ler_nome()
    idade = ler_idade()

    if idade < idade_minima:
        print(f"Inscrição recusada: idade mínima de {idade_minima} anos.\n")
        return

    distancia = ler_opcao("Distância em km (5 ou 10): ", (5, 10))
    lote = ler_opcao("Lote (1 ou 2): ", (1, 2))

    valor = calcular_valor_inscricao(idade, distancia, lote)
    categoria = selecionar_categoria(idade)
    codigo = gerar_codigo(nome, idade)

    # Evita códigos repetidos
    codigo_original = codigo
    numero = 2

    while codigo in codigos_usados:
        codigo = codigo_original + str(numero)
        numero += 1

    codigos_usados.add(codigo)

    corredor = {
        "nome": nome,
        "idade": idade,
        "distancia": distancia,
        "lote": lote,
        "codigo": codigo,
        "categoria": categoria,
        "valor": valor,
        "tempo": None
    }

    corredores.append(corredor)

    print("\n===== COMPROVANTE =====")
    print(f"Nome: {informar_primeiro_nome(nome)}")
    print(f"Código: {codigo}")
    print(f"Categoria: {categoria}")
    print(f"Distância: {distancia} km")
    print(f"Valor: {formatar_reais(valor)}")
    print("=======================\n")


def calcular_resultado():
    """Lê os dados da prova e exibe o resultado."""
    idade = ler_idade()
    if idade < idade_minima:
        print(f"Não há categoria para menores de {idade_minima} anos.\n")
        return
    distancia = ler_opcao("Distância em km(5 ou 10): ", (5, 10))
    tempo = ler_tempo()
    categoria = selecionar_categoria(idade)
    segundos = converter_tempo_para_segundos(tempo)
    pace = calcular_pace(segundos, distancia)
    premiado = verificar_premiacao(categoria, distancia, segundos)
    print("\n=======RESULTADO=======")
    print(f"Categoria: {categoria}")
    print(f"Tempo: {segundos} segundos")
    print(f"Pace: {formatar_pace(pace)}")
    print(f"Premiado: {'Sim' if premiado else 'Não'}")
    print("========================\n")


def listar_inscritos(corredores):
    """Mostra todos os corredores cadastrados."""

    if not corredores:
        print("Nenhum corredor cadastrado.\n")
        return

    for corredor in corredores:
        print("-------------------------")
        print(f"Nome: {corredor['nome']}")
        print(f"Código: {corredor['codigo']}")
        print(f"Idade: {corredor['idade']}")
        print(f"Categoria: {corredor['categoria']}")
        print(f"Distância: {corredor['distancia']} km")
        print(f"Valor: {formatar_reais(corredor['valor'])}")

        if corredor["tempo"] is None:
            print("Tempo: Não registrado")
        else:
            print(f"Tempo: {corredor['tempo']}")

    print("-------------------------\n")


def buscar_corredor(corredores):
    """Procura um corredor pelo código."""

    codigo = input("Digite o código do corredor: ").strip().upper()

    for corredor in corredores:
        if corredor["codigo"].upper() == codigo:
            print(f"Nome: {corredor['nome']}")
            print(f"Categoria: {corredor['categoria']}")
            print(f"Distância: {corredor['distancia']} km")
            print(f"Valor: {formatar_reais(corredor['valor'])}")
            print(f"Tempo: {corredor['tempo'] or 'Não registrado'}\n")
            return

    print("Corredor não encontrado.\n")


def registrar_tempo(corredores):
    """Registra o tempo de um corredor cadastrado."""

    codigo = input("Código do corredor: ").strip().upper()

    for corredor in corredores:
        if corredor["codigo"].upper() == codigo:
            tempo = ler_tempo()
            corredor["tempo"] = tempo

            segundos = converter_tempo_para_segundos(tempo)
            pace = calcular_pace(
                segundos, corredor["distancia"]
            )

            premiado = verificar_premiacao(
                corredor["categoria"],
                corredor["distancia"],
                segundos
            )

            print(f"Tempo: {tempo}")
            print(f"Pace: {formatar_pace(pace)}")
            print(f"Premiado: {'Sim' if premiado else 'Não'}\n")
            return

    print("Corredor não encontrado.\n")


def contar_categorias(corredores):
    """Conta os corredores de cada categoria."""

    quantidades = {
        categoria[0]: 0 for categoria in CATEGORIAS
    }

    for corredor in corredores:
        quantidades[corredor["categoria"]] += 1

    for categoria, quantidade in quantidades.items():
        print(f"{categoria}: {quantidade} corredor(es)")

    print()


def mostrar_premiados(corredores):
    """Lista os corredores premiados que já têm tempo."""

    premiados = [
        corredor for corredor in corredores
        if corredor["tempo"] is not None
        and verificar_premiacao(
            corredor["categoria"],
            corredor["distancia"],
            converter_tempo_para_segundos(corredor["tempo"])
        )
    ]

    com_tempo = [
        corredor for corredor in corredores
        if corredor["tempo"] is not None
    ]

    print(f"Corredores com tempo registrado: {len(com_tempo)}")

    if not premiados:
        print("Nenhum corredor premiado até agora.\n")
        return

    print("\n===== CORREDORES PREMIADOS =====")

    for corredor in premiados:
        print(
            f"{corredor['nome']} - {corredor['codigo']} "
            f"- {corredor['tempo']}"
        )

    print()


def mostrar_classificacao(corredores, distancia):
    """Mostra a classificação geral de uma distância, do menor tempo ao maior."""
    classificados = [
        corredor for corredor in corredores
        if corredor["distancia"] == distancia
        and corredor["tempo"] is not None
    ]

    classificados.sort(
        key=lambda corredor: converter_tempo_para_segundos(corredor["tempo"])
    )

    print(f"\n===== CLASSIFICAÇÃO GERAL - {distancia} KM =====")
    if not classificados:
        print("Nenhum tempo registrado nessa distância.\n")
        return

    for posicao, corredor in enumerate(classificados, start=1):
        print(
            f"{posicao}º - {corredor['nome']} - {corredor['tempo']} "
            f"- {corredor['categoria']}"
        )
    print()


def mostrar_podio(corredores, distancia):
    """Mostra os três melhores corredores de cada categoria na distância."""
    for categoria in CATEGORIAS:
        nome_categoria = categoria[0]
        participantes = [
            corredor for corredor in corredores
            if corredor["categoria"] == nome_categoria
            and corredor["distancia"] == distancia
            and corredor["tempo"] is not None
        ]

        participantes.sort(
            key=lambda corredor: converter_tempo_para_segundos(
                corredor["tempo"])
        )

        print(f"\n===== PÓDIO: {nome_categoria} - {distancia} KM =====")
        if not participantes:
            print("Nenhum tempo registrado nessa categoria.")
            continue

        for posicao, corredor in enumerate(participantes[:3], start=1):
            print(
                f"{posicao}º lugar: {corredor['nome']} - {corredor['tempo']}")
    print()


def relatorio_final(corredores, total_arrecadado):
    """Mostra total de inscritos, arrecadação, médias e mais rápidos."""
    print("\n===== RELATÓRIO FINAL =====")
    print(f"Total de inscritos: {len(corredores)}")
    print(f"Arrecadação: {formatar_reais(total_arrecadado)}")

    for distancia in (5, 10):
        participantes = [
            corredor for corredor in corredores
            if corredor["distancia"] == distancia
            and corredor["tempo"] is not None
        ]

        print(f"\nProva de {distancia} km:")
        if not participantes:
            print("Nenhum tempo registrado.")
            continue

        tempos = [
            converter_tempo_para_segundos(corredor["tempo"])
            for corredor in participantes
        ]
        media = sum(tempos) // len(tempos)
        horas = media // 3600
        minutos = (media % 3600) // 60
        segundos = media % 60

        mais_rapido = min(
            participantes,
            key=lambda corredor: converter_tempo_para_segundos(
                corredor["tempo"])
        )

        print(f"Tempo médio: {horas:02d}:{minutos:02d}:{segundos:02d}")
        print(
            f"Corredor mais rápido: {mais_rapido['nome']} - {mais_rapido['tempo']}")

    print("===========================\n")


def main():
    """Executa o sistema completo da corrida."""

    total_arrecadado = 0.0

    while True:
        print("=== CORRIDA DA PONTE ESTAIADA ===")
        print("1 - Cadastrar corredor")
        print("2 - Listar inscritos")
        print("3 - Buscar corredor")
        print("4 - Registrar tempo")
        print("5 - Contar inscritos por categoria")
        print("6 - Mostrar premiados")
        print("7 - Classificação geral")
        print("8 - Mostrar pódio por categoria")
        print("9 - Sair")

        opcao = ler_opcao("Escolha uma opção: ", (1, 2, 3, 4, 5, 6, 7, 8, 9))

        if opcao == 1:
            quantidade_antes = len(corredores)
            fazer_inscricao(corredores, codigos_usados)

            if len(corredores) > quantidade_antes:
                total_arrecadado += corredores[-1]["valor"]

        elif opcao == 2:
            listar_inscritos(corredores)

        elif opcao == 3:
            buscar_corredor(corredores)

        elif opcao == 4:
            registrar_tempo(corredores)

        elif opcao == 5:
            contar_categorias(corredores)

        elif opcao == 6:
            mostrar_premiados(corredores)

        elif opcao == 7:
            distancia = ler_opcao("Distância (5 ou 10 km): ", (5, 10))
            mostrar_classificacao(corredores, distancia)

        elif opcao == 8:
            distancia = ler_opcao("Distância (5 ou 10 km): ", (5, 10))
            mostrar_podio(corredores, distancia)

        else:
            relatorio_final(corredores, total_arrecadado)
            break


if __name__ == "__main__":
    main()
