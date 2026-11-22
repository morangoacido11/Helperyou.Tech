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
def showservidores():
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
