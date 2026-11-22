import time
import random
helperyou = {
    "nome":"helperyou.tech",
    "versao":"0.0.1",
    "tipo": "software",
    "slogan":"Seu sistema Cyber-Guarda-Costas"
}
#Identificação dos servidores
showservidores = [
    [0,0,1], #Servidores A - Portas 1,2 livres e 3 ocupada
    ["x",0,1] #Servidores B - Portas 1 bloqueada, 2 livre e 3 ocupada
]
def showservidores(): #Mostra os servidores
  print("setores:")
  print(f"{showservidores[0]}")
  print(f"{showservidores[1]}")
def cadastro_menu(): #Cadastro empresarial - Onde sera feito o cadastro da empresa para que o sistema "Cyber-Guarda_Costas seja executado".
nome_empresa = ""
codigo_empresa = ""
senha_empresa = ""
print("Bem-vindo ao cadastro.")
print("Escolha uma das opções:")
print("[1]Realizar cadastro. \n[2] Entrar. \n[3] Sair.")
while True:
    opcao = input("Selecione apenas uma opcao (1, 2 ou 3):\n> ").strip()
    if opcao == "1" or opcao == "2" or opcao == "3":
          break
    else:
        print("Selecione apenas o que pede! \n[Erro: caractere sem ser 1, 2 ou 3]")

    if opcao == "3":
      print("\nObrigado por usar a HelperYou! Até logo.")
      break

      def menu_1():
        if opcao == "1":
              print("="*20)
              print("Seja bem-vindo!")
              print("="*20)
              print("Realizaremos o cadastro da sua empresa em nosso sistema!")
              print("="*20)
              while True:
                  numerodecadastro = random.randint(100, 9999999)
                  emailempresa = input("> Coloque o email empresarial: ").strip()
                  nome_empresa = input("> Nome da empresa: ").strip()
                  codigo_empresa = input("> Crie um codigo: ").strip()
                  senha_empresa = input("> Crie uma senha: ").strip()


                  if nome_empresa != "" and codigo_empresa != "" and emailempresa != "" and senha_empresa != "":
                      dadosempresa = {
                          "nome da empresa": nome_empresa,
                          "senha": senha_empresa
                      }
                      print("")
                      print(f"==Empresa [{nome_empresa}] cadastrada com sucesso!==")
                      time.sleep(2)
                      print("\n Gerando número de cadastro.") # O numero de cadastro serve como enderço dos dados atuais da sua empresa e é usado para o monitoramento.
                      print(f"== Numero de Cadastro [{numerodecadastro}] ==")
                      print("")
                      print(f">Dados de sua empresa: {dadosempresa} <")
                      print("> Realize o login na opção, selecionando-a no menu.")
                      print("")
                      time.sleep(2)
                      break
                  else:
                      print("")
                      print("==Algo deu errado. Preencha todos os campos.==")
                      print("")

