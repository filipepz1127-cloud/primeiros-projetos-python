from datetime import datetime

nome = str(input("qual e seu nome? "))
cidade = str(input("onde vc mora? "))
ocupaçao = str(input("oque vc faz da vida? ")).lower
humor = int(input("como esta o seu humor hoje? "))

print ("\33[7;30m ===== RELATORIO DO USUARIO =====\33[")
print ("seu nome é: {}".format(nome))
print ("mora em: {}".format(cidade))
if ocupaçao == "trabalha" or ocupaçao == "trabalho":
 print ("ocupaçao: trabalhador")
elif ocupaçao == "estudo" or ocupaçao == "estuda":
      print("ocupacao; estudante")
else:
     print("ocupacao; nao informada")
     
if humor <= 2:
    print("\033[31mHumor: Baixo\033[m")
elif humor == 3:
    print("\033[33mHumor: Neutro\033[m")
else:
    print("\033[32mHumor: Alto\033[m")

print(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
print("\033[34m============================\033[m\n")