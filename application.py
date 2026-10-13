import pandas as pd
from pathlib import Path
import os

DIRECTORY_ORIGIN = "---"

dir_pedidos_movel = DIRECTORY_ORIGIN
dir_pedidos_fixa = DIRECTORY_ORIGIN
dir_call_movel = DIRECTORY_ORIGIN
dir_call_fixa_nacional = DIRECTORY_ORIGIN
dir_call_fixa_regional = DIRECTORY_ORIGIN

VERSION = "1.0.0"
HEADER = f"_________________ | Gerar Relatorios v{VERSION} - By Diego C. | _________________"
ARCHIVES_SELECTED = f"Arquivos Anexados:\n\n  Pedidos Movel: {dir_pedidos_movel}\n  Pedidos Fixa: {dir_pedidos_fixa}\n  Chamadas Movel: {dir_call_movel}\n  Chamadas Fixa Nacional: {dir_call_fixa_nacional}\n  Chamadas Fixa Regional: {dir_call_fixa_regional}"
OPTIONS_MENU = f"\nOpções:\n\n  [1] Anexar arquivos\n  [2] Analisar Telefones\n\n  [3] Ficha de vendas\n  [4] Gerencial\n  [5] Retorno\n  [6] Operacional\n\n  [0] Sair"

user_option = 0

 
while True:
    os.system("cls")
    print(HEADER+"\n\n\n"+ARCHIVES_SELECTED+"\n"+OPTIONS_MENU)

    try:
        user_option = int(input("\nDigite uma das opções: "))
    except ValueError:
        os.system("cls")
        print(HEADER+"\n\n\n"+ARCHIVES_SELECTED)
        print("\nDigite apenas numeros!")
        input("\b\nPrecione [enter] para continuar")
        continue
    
    break