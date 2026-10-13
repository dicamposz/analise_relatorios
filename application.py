import pandas as pd
from pathlib import Path
import os

DIRECTORY_ORIGIN = "---"

dir_pedidos_movel = DIRECTORY_ORIGIN
dir_pedidos_fixa = DIRECTORY_ORIGIN
dir_call_movel = DIRECTORY_ORIGIN
dir_call_fixa_nacional = DIRECTORY_ORIGIN
dir_call_fixa_regional = DIRECTORY_ORIGIN

VERSION = "1.0.1"
HEADER = f"_________________ | Gerar Relatorios v{VERSION} - By Diego C. | _________________"
ARCHIVES_SELECTED = f"Arquivos Anexados:\n\n  Pedidos Movel: {dir_pedidos_movel}\n  Pedidos Fixa: {dir_pedidos_fixa}\n  Chamadas Movel: {dir_call_movel}\n  Chamadas Fixa Nacional: {dir_call_fixa_nacional}\n  Chamadas Fixa Regional: {dir_call_fixa_regional}"
OPTIONS_MENU = f"\nOpções:\n\n  [1] Anexar arquivos\n  [2] Analisar Telefones\n\n  [3] Ficha de vendas\n  [4] Gerencial\n  [5] Retorno\n  [6] Operacional\n\n  [0] Sair"


def show_header():
    os.system("cls")
    print(HEADER+"\n\n\n"+ARCHIVES_SELECTED+"\n"+OPTIONS_MENU)


def show_options(user_option):
    
    match user_option:
        case 1:
            ...
        case 2:
            ...
        case 3:
            ...
        case 4:
            ...
        case 5:
            ...
        
user_option = 0
 
 
while True:
    show_header()
    user_option == 0

    try:
        user_option = int(input("\nDigite uma das opções: "))
    except ValueError:
        show_header()
        print("\nDigite apenas numeros!")
        input("\b\nPrecione [enter] para continuar")
        continue
    
    if user_option == 0:
        show_header()
        print("\nSAINDO . . .")
        raise SystemExit
    elif user_option not in range(1, 7):
        show_header()
        print("\nOpção invalida!")    
        input("\b\nPrecione [enter] para continuar")
        continue
        
    show_options(user_option=user_option)
    
    break