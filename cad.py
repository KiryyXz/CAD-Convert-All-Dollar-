#ferramenta fudida de conversão em python kk

import  time

print("Adicione somente valores\n[00] nunca coloque [0,0] ou [0.0]")

rd=int(input("Adicione um valor em dolar:"))

result=rd*5.42

time.sleep(0.5)

print("Resultado: R$",result)

time.sleep(1.0)

input("Aperte [ENTER] p/ converter BRL em USD")

time.sleep(0.7)

rr=int(input("Adicione um valor em real:"))

res_re=rr*0.18

time.sleep(1.0)

print("Resultado: U$D",res_re)
