import csv
import math
import os
import random
import time

helperyou = {
    "nome": "helperyou.tech",
    "versao": "0.0.1",
    "tipo": "software",
    "slogan": "Seu sistema Cyber-Guarda-Costas",
    "plano": "Gratuito (sem cobrança ou mensalidade)",
}

ARQUIVO_CSV = "dados.csv"
MATRIZ_PADRAO = "Matriz Principal"

# Identificação dos servidores
lista_servidores = [
    [0, 3, 2],  # Servidores A - Portas 1 livre, 2 e 3 ocupadas
    ["x", 0, 1],  # Servidores B - Portas 1 bloqueada, 2 livre e 3 ocupada
]


def converter_para_float(valor, fallback=0.0):
    """Converte com segurança valores textuais (ex.: '24.5', '12,0') para float."""
    if valor is None:
        return float(fallback)

    if isinstance(valor, (int, float)):
        if math.isnan(valor) or math.isinf(valor):
            return float(fallback)
        return float(valor)

    texto = str(valor).strip().replace(",", ".")
    if texto == "":
        return float(fallback)

    try:
        numero = float(texto)
        if math.isnan(numero) or math.isinf(numero):
            return float(fallback)
        return numero
    except ValueError:
        return float(fallback)


def normalizar_matriz(valor_matriz):
    """Retorna o nome da Matriz ou o valor padrão caso esteja vazio/ausente."""
    if valor_matriz is None:
        return MATRIZ_PADRAO
    texto = str(valor_matriz).strip()
    return texto if texto != "" else MATRIZ_PADRAO


def resumo_metricas_servidores():
    """Calcula métricas operacionais de portas/slots a partir de lista_servidores."""
    total_slots = 0
    portas_livres = 0
    portas_ativas_ou_bloqueadas = 0

    for grupo in lista_servidores:
        for slot in grupo:
            total_slots += 1
            if slot == 0:
                portas_livres += 1
            else:
                portas_ativas_ou_bloqueadas += 1

    return {
        "grupos": len(lista_servidores),
        "total_slots": total_slots,
        "portas_livres": portas_livres,
        "portas_ativas_ou_bloqueadas": portas_ativas_ou_bloqueadas,
    }


def showservidores():
    metricas = resumo_metricas_servidores()
    print("\n--- Servidores ---")
    print(f"{lista_servidores[0]}")
    print(f"{lista_servidores[1]}")
    print(
        f"Resumo técnico: {metricas['grupos']} grupos | "
        f"{metricas['total_slots']} posições | "
        f"{metricas['portas_livres']} livres | "
        f"{metricas['portas_ativas_ou_bloqueadas']} ocupadas/bloqueadas"
    )
    print("-" * 15)


def salvar_dados_csv(
    numero_cadastro,
    email,
    nome,
    codigo,
    senha,
    matriz=MATRIZ_PADRAO,
    horas_monitoramento=0.0,
    status_sistema="Cadastro realizado com sucesso",
    caminho_arquivo=ARQUIVO_CSV,
):
    """Salva os dados cadastrados da empresa, matriz, métrica operacional e log em dados.csv."""
    arquivo_existe = (
        os.path.exists(caminho_arquivo) and os.path.getsize(caminho_arquivo) > 0
    )
    cabecalho = [
        "sistema",
        "versao",
        "numero_cadastro",
        "nome_empresa",
        "email_empresa",
        "codigo_empresa",
        "senha_empresa",
        "matriz_empresa",
        "horas_monitoramento",
        "status_log",
    ]
    matriz_limpa = normalizar_matriz(matriz)
    horas_float = converter_para_float(horas_monitoramento, fallback=0.0)
    if horas_float < 0:
        horas_float = 0.0

    linha = [
        helperyou["nome"],
        helperyou["versao"],
        numero_cadastro,
        nome,
        email,
        codigo,
        senha,
        matriz_limpa,
        f"{horas_float:.1f}",
        f"[{helperyou['nome']} v{helperyou['versao']}] {status_sistema}",
    ]

    with open(caminho_arquivo, mode="a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")
        if not arquivo_existe:
            escritor.writerow(cabecalho)
        escritor.writerow(linha)


def ler_dados_csv_readline(caminho_arquivo=ARQUIVO_CSV):
    """Lê dados.csv linha a linha usando estritamente .readline() em um loop while."""
    print("\n" + "=" * 45)
    print(f"LEITURA DO ARQUIVO: {caminho_arquivo} (.readline())")
    print("=" * 45)

    if not os.path.exists(caminho_arquivo):
        print(f"[Aviso] O arquivo '{caminho_arquivo}' ainda não existe.")
        print("Dica: Realize um cadastro na opção [1] para gerar o arquivo.\n")
        return

    with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
        numero_linha = 0
        linha = arquivo.readline()

        while linha != "":
            numero_linha += 1
            linha_limpa = linha.rstrip("\r\n")

            if numero_linha == 1:
                print(f"[Cabeçalho] {linha_limpa}")
                print("-" * 45)
            else:
                colunas = linha_limpa.split(";")
                if len(colunas) >= 10:
                    horas_val = converter_para_float(colunas[8], fallback=0.0)
                    print(f"Registro #{numero_linha - 1}:")
                    print(f"  • Sistema / Versão : {colunas[0]} (v{colunas[1]})")
                    print(f"  • Nº Cadastro      : {colunas[2]}")
                    print(f"  • Empresa          : {colunas[3]}")
                    print(f"  • E-mail           : {colunas[4]}")
                    print(f"  • Código           : {colunas[5]}")
                    print(f"  • Senha            : {colunas[6]}")
                    print(
                        f"  • Matriz           : {normalizar_matriz(colunas[7])}"
                    )
                    print(f"  • Horas Monitor.   : {horas_val:.1f} h")
                    print(f"  • Log / Status     : {colunas[9]}")
                    print("-" * 45)
                elif len(colunas) >= 8:
                    print(f"Registro #{numero_linha - 1} (formato legado):")
                    print(f"  • Sistema / Versão : {colunas[0]} (v{colunas[1]})")
                    print(f"  • Nº Cadastro      : {colunas[2]}")
                    print(f"  • Empresa          : {colunas[3]}")
                    print(f"  • E-mail           : {colunas[4]}")
                    print(f"  • Código           : {colunas[5]}")
                    print(f"  • Senha            : {colunas[6]}")
                    print(f"  • Matriz           : {MATRIZ_PADRAO} (padrão)")
                    print(f"  • Horas Monitor.   : 0.0 h (padrão)")
                    print(f"  • Log / Status     : {colunas[7]}")
                    print("-" * 45)
                else:
                    print(f"Linha {numero_linha}: {linha_limpa}")

            linha = arquivo.readline()

    print(f"Leitura concluída ({numero_linha} linha(s) lida(s) no total).\n")


def consolidar_registros_csv(caminho_arquivo=ARQUIVO_CSV):
    """Lê dados.csv com .readline(), converte métricas para float e consolida Empresa x Matriz."""
    consolidado = {}
    total_horas_geral = 0.0
    total_registros = 0

    if not os.path.exists(caminho_arquivo):
        return consolidado, total_horas_geral, total_registros

    with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
        numero_linha = 0
        linha = arquivo.readline()

        while linha != "":
            numero_linha += 1
            linha_limpa = linha.rstrip("\r\n")

            if numero_linha > 1 and linha_limpa.strip() != "":
                colunas = linha_limpa.split(";")
                if len(colunas) >= 8:
                    empresa = (
                        colunas[3].strip()
                        if colunas[3].strip() != ""
                        else "Empresa não informada"
                    )

                    # Layout novo tem 10 colunas (matriz em [7], horas em [8], status em [9]).
                    # Layout legado tem 8 colunas (status em [7]).
                    if len(colunas) >= 10:
                        matriz = normalizar_matriz(colunas[7])
                        horas = converter_para_float(colunas[8], fallback=0.0)
                    elif len(colunas) == 9:
                        matriz = normalizar_matriz(colunas[7])
                        horas = 0.0
                    else:
                        matriz = MATRIZ_PADRAO
                        horas = 0.0

                    if horas < 0:
                        horas = 0.0

                    chave = (empresa, matriz)
                    if chave not in consolidado:
                        consolidado[chave] = {
                            "empresa": empresa,
                            "matriz": matriz,
                            "registros": 0,
                            "horas_monitoramento": 0.0,
                        }

                    consolidado[chave]["registros"] += 1
                    consolidado[chave]["horas_monitoramento"] += horas
                    total_horas_geral += horas
                    total_registros += 1

            linha = arquivo.readline()

    return consolidado, total_horas_geral, total_registros


def exibir_painel_consolidado(caminho_arquivo=ARQUIVO_CSV):
    """Exibe no terminal o painel consolidado de Empresa x Matriz x Métricas Operacionais."""
    consolidado, total_horas, total_registros = consolidar_registros_csv(
        caminho_arquivo
    )
    servidores = resumo_metricas_servidores()

    largura = 78
    print("\n" + "=" * largura)
    print(f"{helperyou['nome'].upper()} - PAINEL CONSOLIDADO OPERACIONAL")
    print(f"{helperyou['slogan']} | Serviço: {helperyou['plano']}")
    print("=" * largura)

    if not consolidado:
        print(
            f"[Aviso] Nenhum registro encontrado em '{caminho_arquivo}' para consolidar."
        )
        print(
            "Dica: Cadastre uma empresa na opção [1] para gerar métricas operacionais."
        )
    else:
        cabecalho_fmt = (
            f"{'EMPRESA':<24} | {'MATRIZ':<20} | {'REG.':>4} | {'HORAS MONIT.':>12}"
        )
        print(cabecalho_fmt)
        print("-" * largura)

        for chave in sorted(consolidado.keys()):
            item = consolidado[chave]
            print(
                f"{item['empresa'][:24]:<24} | "
                f"{item['matriz'][:20]:<20} | "
                f"{item['registros']:>4} | "
                f"{item['horas_monitoramento']:>10.1f} h"
            )

        print("-" * largura)
        print(
            f"{'TOTAL CONSOLIDADO':<47} | "
            f"{total_registros:>4} | "
            f"{total_horas:>10.1f} h"
        )

    print("-" * largura)
    print(
        f"Infraestrutura de Servidores: {servidores['grupos']} grupos | "
        f"{servidores['total_slots']} posições totais | "
        f"{servidores['portas_livres']} livres | "
        f"{servidores['portas_ativas_ou_bloqueadas']} ocupadas/bloqueadas"
    )
    print("Cobrança / Financeiro: R$ 0,00 (Plataforma 100% gratuita)")
    print("=" * largura + "\n")


# Variáveis globais para armazenar os dados cadastrados
nome_empresa = ""
codigo_empresa = ""
senha_empresa = ""
emailempresa = ""


def cadastro_menu():
    global nome_empresa, codigo_empresa, senha_empresa, emailempresa
    while True:
        print("")
        print("=" * 20)
        print("Bem-vindo!")
        print("=" * 20)
        print("Escolha uma das opções:")
        print("[1] Realizar cadastro \n[2] Entrar \n[3] Voltar ao menu principal")
        opcao = input("Selecione apenas uma opcao (1, 2 ou 3):\n> ").strip()

        if opcao == "1":
            print("=" * 20)
            print("Seja bem-vindo!")
            print("=" * 20)
            print("Realizaremos o cadastro da sua empresa em nosso sistema!")
            print("=" * 20)

            while True:
                numerodecadastro = random.randint(100, 9999999)
                emailempresa = input("> Coloque o email empresarial: ").strip()
                nome_empresa = input("> Nome da empresa: ").strip()
                matriz_entrada = input(
                    f"> Matriz / Unidade (Enter para '{MATRIZ_PADRAO}'): "
                ).strip()
                horas_entrada = input(
                    "> Horas previstas de monitoramento (ex.: 24.5 ou 12,0): "
                ).strip()
                codigo_empresa = input("> Crie um codigo: ").strip()
                senha_empresa = input("> Crie uma senha: ").strip()

                if (
                    nome_empresa != ""
                    and codigo_empresa != ""
                    and emailempresa != ""
                    and senha_empresa != ""
                ):
                    matriz_final = normalizar_matriz(matriz_entrada)
                    horas_final = converter_para_float(horas_entrada, fallback=0.0)
                    if horas_final < 0:
                        horas_final = 0.0

                    dadosempresa = {
                        "nome da empresa": nome_empresa,
                        "matriz": matriz_final,
                        "horas de monitoramento": horas_final,
                        "senha": senha_empresa,
                    }
                    salvar_dados_csv(
                        numero_cadastro=numerodecadastro,
                        email=emailempresa,
                        nome=nome_empresa,
                        codigo=codigo_empresa,
                        senha=senha_empresa,
                        matriz=matriz_final,
                        horas_monitoramento=horas_final,
                        status_sistema="Empresa cadastrada e pronta para monitoramento",
                    )

                    print("")
                    print(f"== Empresa [{nome_empresa}] cadastrada com sucesso! ==")
                    time.sleep(1)
                    print("\nGerando número de cadastro...")
                    print(f"== Número de Cadastro [{numerodecadastro}] ==")
                    print("")
                    print(f"> Dados de sua empresa: {dadosempresa} <")
                    print(f"> Registro salvo em '{ARQUIVO_CSV}'!")
                    print("> Realize o login na opção [2].")
                    print("")
                    time.sleep(2)
                    break
                else:
                    print("\n== Algo deu errado. Preencha todos os campos. ==\n")

        elif opcao == "2":
            if nome_empresa == "":
                print(
                    "\n[Erro] Nenhuma empresa cadastrada no sistema! Cadastre-se na"
                    " opção [1] primeiro.\n"
                )
                time.sleep(1.5)
                continue

            while True:
                print("=" * 20)
                print("Seja bem-vindo de volta!")
                print("")
                print("Preencha as 3 verificações!")
                print("=" * 20)

                helperyoucode = "helpertech123"
                numerodecadastro2 = random.randint(100, 9999999)
                codigo_empresa2 = input("> Insira seu codigo: ").strip()
                senha_empresa2 = input("> Insira a senha: ").strip()
                verificacao_helperyou = input(
                    f"Enviamos um codigo para o email: [{emailempresa}]. \nColoque-o:"
                    " "
                ).strip()

                if (
                    codigo_empresa2 == codigo_empresa
                    and senha_empresa2 == senha_empresa
                    and verificacao_helperyou == helperyoucode
                ):
                    print("\nPesquisando e coletando dados, aguarde...")
                    time.sleep(2)
                    print(f"Empresa [{nome_empresa}] encontrada!")
                    print(f"Número de cadastro: [{numerodecadastro2}].")
                    time.sleep(2)
                    print("== Registro realizado com sucesso. ==")
                    print("== Iniciando sistema Cyber-Guarda-Costas...")
                    time.sleep(2)
                    print("> Dados criptografados com sucesso!")
                    time.sleep(1)
                    print("> Sua empresa está sendo monitorada.")
                    print(".*+ == Tenha uma boa jornada tech! == +*.\n")
                    time.sleep(2)
                    break
                else:
                    print("\n== Dados incorretos! Tente Novamente. ==\n")

        elif opcao == "3":
            print("\nSaindo do menu de cadastro...\n")
            break
        else:
            print(
                "Selecione apenas o que se pede! \n[Erro: caractere sem ser 1, 2 ou"
                " 3]\n"
            )


# Loop Principal do Programa
while True:
    print("=" * 30)
    print("HELPERYOU.TECH")
    print("=" * 30)
    print("\nBem-vindo ao Menu principal! \nSelecione uma das opções para começar:")
    print(
        "[1] Iniciar \n[2] Observar setores \n[3] Informações da empresa \n"
        "[4] Ler dados salvos (dados.csv) \n[5] Painel Consolidado \n[6] Sair"
    )
    print("=" * 30)

    selecao = input("> ").strip()

    if selecao == "":
        print("Coloque ao menos um caractere.")
    elif selecao == "1":
        cadastro_menu()
    elif selecao == "2":
        showservidores()
    elif selecao == "3":
        print(helperyou)
    elif selecao == "4":
        ler_dados_csv_readline()
    elif selecao == "5":
        exibir_painel_consolidado()
    elif selecao == "6":
        print("\nO programa foi encerrado. Até depois!")
        break
    else:
        print("Digite apenas 1, 2, 3, 4, 5 ou 6!\n")
