import csv
import sys
from datetime import datetime


import pandas as pd


print("--------- Executando Script ---------")
print("Dica: Você pode passar o nome do arquivo do extrato como parametro no terminal.")
print("Exemplo: win_extrato_nubank_facca.bat NOME_DO_EXTRATO")
try:
    import tkinter as tk
    from tkinter import filedialog
except ImportError:
    print("Tkinter não está instalado. Instale-o no sistema.")
    exit(1)

if len(sys.argv) < 2:
    root = tk.Tk()
    root.withdraw()
    csv_path = filedialog.askopenfilename(
        title="Selecione o arquivo CSV",
        filetypes=[("Arquivos CSV", "*.csv")],
    )
    file = open(csv_path)

    if not csv_path:
        print("Nenhum arquivo selecionado. Encerrando.")
        exit()
else:
    file = open(sys.argv[1])

csv_file = csv.reader(file)
print(csv_file)
payments = []
df = pd.DataFrame()
for line in csv_file:
    els = line[3].split("-")
    if len(els)>1:
        name = els[1]
        value = line[1]
        payment = {"name":name, "value":float(value)}
        df = df._append(payment, ignore_index=True)
        payments.append(payment)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
df.to_csv(f'pagamentos_{timestamp}.csv')