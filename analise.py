# 1. Importando Pandas

import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure

# 2. Lendo CSV:

df = pd.read_csv("aula_15_atividade_f.csv")


nome = df["Nome"]
vendas = df["Compra"]
regiao = df["Região"]

# print("\n",nome,"\n",vendas,"\n",regiao)

# 3. Vendas por Vendedor:

vpv = df.groupby("Nome")["Compra"].sum()

print(vpv)

vpvpl = vpv.to_list()
# 4. Vendas por Região:

vpr = df.groupby("Região")["Compra"].sum()

print(vpr)

vprl = vpr.to_list()
# 5.Atuação por Região:

apr = df.groupby("Nome")["Região"].sum()

print(apr)

aprl = apr.str.replace("SulNordesteSudeste NorteSulCentro-Oeste","Todas Regiões").to_list()

print(vpvpl,vprl,aprl)

#5. Agrupamento de vendedores:
ns = nome.to_list()
for n in range(5):
    ns.remove("Ana")
    ns.sort()

print(ns)

#6. Agrupamento de região:
rs = regiao.to_list()


for n in range(2):
    rs.remove("Sudeste ")
    rs.sort()

for n in range(2):
    rs.remove("Sul")
    rs.sort()
    
print(rs)

# print(ns)

# print(vpvpl,vprl,aprl)

# 7. Testando gráficos:

# plt.subplot(1,3,1)
# plt.bar(ns,vpvpl)
# plt.xlabel("Vendedor")
# plt.ylabel("Valores")
# plt.title("Vendas por vendedor")

# plt.subplot(1,3,2)
# plt.bar(rs,vprl)
# plt.xlabel("Vendedor")
# plt.ylabel("Valores")
# plt.title("Vendas por Região")

# plt.subplot(1,3,3)
# plt.scatter(aprl,ns)
# plt.xlabel("Região")
# plt.ylabel("Vendedor")
# plt.title("Vendedores por Região")


# plt.show()


#Interface:

janela = tk.Tk()

janela.title("Desafio Data Science")

text = tk.Label(janela,text = "Graficos e Informações",) #Titulo
text2 = tk.Label(janela,text= "Escolha uma das opções abaixo:")
text.grid(row=0,column=0,columnspan=5)
text2.grid(row=1,column=0,columnspan=5)


#Graficos:
    
def v1():
    fig = Figure(figsize=(8, 4), dpi=100)
    fig, grafico = plt.subplots()
    grafico.bar(ns,vpvpl)
    grafico.set_ylabel("Valores")
    grafico.set_xlabel("Vendedor")
    canvas = FigureCanvasTkAgg(fig, master=janela)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=3,column=0,columnspan=5)
    
def v2():
    fig = Figure(figsize=(8, 4), dpi=100)
    fig, grafico = plt.subplots()
    grafico.bar(rs,vprl)
    grafico.set_ylabel("Valores")
    grafico.set_xlabel("Região")
    canvas = FigureCanvasTkAgg(fig, master=janela)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=3,column=0,columnspan=5)
    
def v3():
    fig = Figure(figsize=(8, 4), dpi=100)
    fig, grafico = plt.subplots()
    grafico.scatter(aprl,ns)
    grafico.set_ylabel("Vendedor")
    grafico.set_xlabel("Região")
    canvas = FigureCanvasTkAgg(fig, master=janela)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=3,column=0,columnspan=5)

def info():
    info = tk.Label(janela,text= "Info:")
    info.config(text= f"""Relátorio
                Através da análise de dados,concluimos que:
                1 - Ana é a melhor vendedora da empresa, portanto,merece uma bonificação de desempenho(Ver gráfico 1);
                2 - Os nossos maiores compradores se concentram na região Sul e Sudeste, logo serão os cliente prioritários(Ver gráfico 2);
                3 - Ana é unica vendedora atuando em todas as regiões, logo,devemos engajar os demais vendedores em outras regiões(Ver gráfico 3);
                4 - Além do engajamento dos vendedores, devemos também melhorar o marketing nas outras regiões do pais para aumentar nossas vendas(Ver gráficos 2 e 3).
        
            """ ,justify="left") 
    info.grid(row=2,column=0,columnspan=5)
    
#Botões:
btn1 = tk.Button(janela,text="1.Vendas por Vendedor", command=v1) # Executa o comando
btn2 = tk.Button(janela,text="2.Vendas por Região", command=v2) # Executa o comando
btn3 = tk.Button(janela,text="3.Vendedores por Região", command=v3) # Executa o comando
btn5 = tk.Button(janela,text="4.Relátorio", command=info) # Executa o comando


btn1.grid(column=0,row=4,padx=5)
btn2.grid(column=1,row=4,padx=5)
btn3.grid(column=2,row=4,padx=5)
btn5.grid(column=3,row=4,padx=5)

        

janela.mainloop()