import pandas as pd
from services import analise_telefones as an
from pathlib import Path
import os

DIRECTORY_ORIGIN = "---"

dir_pedidos_movel = DIRECTORY_ORIGIN
dir_pedidos_fixa = DIRECTORY_ORIGIN
dir_call_movel = DIRECTORY_ORIGIN
dir_call_fixa_nacional = DIRECTORY_ORIGIN
dir_call_fixa_regional = DIRECTORY_ORIGIN

VERSION = "1.3.0"
HEADER = f"_________________ | Gerar Relatorios v{VERSION} - By Diego C. | _________________"
OPTIONS_MENU = f"\nOpções:\n\n  [1] Anexar arquivos\n  [2] Analisar Telefones\n\n  [3] Ficha de vendas\n  [4] Gerencial\n  [5] Retorno\n  [6] Operacional\n\n  [0] Sair"


def get_archives_selected():
    return (
        f"\nArquivos Anexados:\n\n  Pedidos Movel: {dir_pedidos_movel}\n"
        f"  Pedidos Fixa: {dir_pedidos_fixa}\n"
        f"  Chamadas Movel: {dir_call_movel}\n"
        f"  Chamadas Fixa Nacional: {dir_call_fixa_nacional}\n"
        f"  Chamadas Fixa Regional: {dir_call_fixa_regional}"
    )
    
    
def show_header():
    os.system("cls")
    print(HEADER+"\n\n\n"+get_archives_selected()+"\n"+OPTIONS_MENU)


def valid_dir(diretory_way):
    if not Path(diretory_way).is_file():
        raise FileNotFoundError(f"\nArquivo não encontrado!")

def valid_dir_folder(diretory_way):
    if not Path(diretory_way).is_dir():
        raise FileNotFoundError(f"\nPasta não encontrada!")

def dir_archives():
    
    global dir_pedidos_movel, dir_pedidos_fixa, dir_call_movel ,dir_call_fixa_nacional, dir_call_fixa_regional 
    
    
    os.system("cls")
    print(HEADER+"\n\n\n"+get_archives_selected())
    
    try:
        dir_pedidos_movel = Path(input("\nDiretorio pedidos movel: "))
        valid_dir(dir_pedidos_movel)
        
    except FileNotFoundError as e:
        print(e)
        dir_pedidos_movel = DIRECTORY_ORIGIN
        input("\nPressione [enter]")
        
        
    os.system("cls")
    print(HEADER+"\n\n\n"+get_archives_selected())
        
    try:
        dir_pedidos_fixa = Path(input("\nDiretorio pedidos fixa: "))
        valid_dir(dir_pedidos_fixa)
    
    except FileNotFoundError as e:
        print(e)
        dir_pedidos_fixa = DIRECTORY_ORIGIN
        input("\nPressione [enter]")
        
        
    os.system("cls")
    print(HEADER+"\n\n\n"+get_archives_selected())
        
    try:    
        dir_call_movel = Path(input("\nDiretorio chamadas movel: "))
        valid_dir(dir_call_movel)
        
    except FileNotFoundError as e:
        print(e)
        dir_call_movel = DIRECTORY_ORIGIN
        input("\nPressione [enter]")
        
        
    os.system("cls")
    print(HEADER+"\n\n\n"+get_archives_selected())
    try:
        dir_call_fixa_nacional = Path(input("\nDiretorio chamadas fixa nacional: "))
        valid_dir(dir_call_fixa_nacional)
        
    except FileNotFoundError as e:
        print(e)
        dir_call_fixa_nacional = DIRECTORY_ORIGIN  
        input("\nPressione [enter]")
        
        
    os.system("cls")
    print(HEADER+"\n\n\n"+get_archives_selected())
    
    try:
        dir_call_fixa_regional = Path(input("\nDiretorio chamadas fixa nacional: "))
        valid_dir(dir_call_fixa_regional)
    
    except FileNotFoundError as e:
        print(e)
        dir_call_fixa_regional = DIRECTORY_ORIGIN      
        input("\nPressione [enter]")
    
    os.system("cls")
    print(HEADER+"\n\n\n"+get_archives_selected())
            


def show_options(user_option):
    
    match user_option:
        case 1:
            dir_archives()
            
        case 2:
            while True:
                os.system("cls")
                print("_______________ | Analisar telefones - By Diego | _______________")
                
                try:
                    option_user = int(input("\n[1] Converter TXT to CSV\n[2] Concatenar diferentes arquivos CSV\n[3] Remover duplicadas\n[4] Comparar com mailing\n[5] Contabilizar cargas\n\n[0] Voltar\n\nDigite: "))
                except ValueError:
                    print("\nDigite apenas numeros!")
                    continue

                if option_user == 1:
                    
                    try:
                        dir_txt_retorno = Path(input("\nDigite o caminho para o txt de retorno: "))
                        valid_dir_folder(dir_txt_retorno)
                        
                        mounth = input("Digite o mes: ")
                        product = input("Digite o produto: ")
                        
                    except FileNotFoundError as e:
                        print(e)
                        input("\nPressione [enter] para continuar: ")
                        continue
                    
                    an.Analisar_Telefones.convert_txt_in_csv(dir_txt_retorno=dir_txt_retorno, mounth_relatory=mounth, product=product)
                    print("\nConvertido!")
                    input("Pressione [enter] para continuar")
                    break
                
                elif option_user == 2:
                    
                    try:
                        dir_csv_retorno = Path(input("\nDigite o caminho para o csv de retorno: "))
                        valid_dir_folder(dir_csv_retorno)
                        
                        mounth = input("Digite o mes: ")
                        product = input("Digite o produto: ")
                                            
                    except FileNotFoundError as e:
                        print(e)
                        input("\nPressione [enter] para continuar: ")
                        continue
                    
                    an.Analisar_Telefones.concat_csv_return(dir_csv_retorno=dir_csv_retorno, mounth_relatory=mounth, product=product)
                    print("\nConcatenado!")
                    input("Pressione [enter] para continuar")
                    break

                elif option_user == 3:
                    try:
                        dir_csv_unido = Path(input("\nDigite o caminho para o csv unido: "))

                        
                        mounth = input("Digite o mes: ")
                        product = input("Digite o produto: ")
                                                                
                    except FileNotFoundError as e:
                        print(e)
                        input("\nPressione [enter] para continuar: ")
                        continue
                    
                    an.Analisar_Telefones.remove_duplicates(dir_csv_unido=dir_csv_unido, mounth_relatory=mounth, product=product)
                    print("\nRemovido!")
                    input("Pressione [enter] para continuar")
                    break
                
                    
                elif option_user == 4:
                    print("\nAnalisar mailing...")
                    
                    try:
                        dir_mailing_analizer = Path(input("\nDigite o local do arquivo do mailing: "))
                        valid_dir(diretory_way=dir_mailing_analizer)
                        
                        dir_csv_analizer = Path(input("\nDigite o local do arquivo do csv unido: "))
                        valid_dir(diretory_way=dir_csv_analizer)
                        
                        mounth = input("Digite o mês: ")
                        product = input("Digite o produto: ")
                        
                    except FileNotFoundError as e:
                        print(e)
                        input("\nPressione [enter] para continuar")
                    
                    
                    an.Analisar_Telefones.verify_tel_cpf(mounth=mounth, product=product, dir_mailing=dir_mailing_analizer, dir_csv_unido=dir_csv_analizer)
                    
                    
                elif option_user == 5:
                    print("\nContabilizar cargas...")
                    
                    while True:
                        try:
                            dir_csv_unido = Path(input("\nDigite o caminho para o csv unido: "))
                            dir_carga_mailing = Path(input("\nDigite o caminho para a carga a verificar: "))
                        
                            mounth = input("Digite o mes: ")
                            day_cumulate = input("Digite X dia que esta acumulado: ")
                            product = input("Digite o produto: ")
                            
                            break
                        except FileNotFoundError as e:
                            print(e)
                            input("\nPressione[enter] para continuar")
                            continue                     
                    
                    an.Analisar_Telefones.contabil_ids(dir_csv_unido=dir_csv_unido, carga_mailing=dir_carga_mailing, day_acumulado=day_cumulate, mounth=mounth, product=product)
                    
                    
                elif option_user == 0:
                    break    
                
                else:
                    print("\nOpção Invalida!")
                    continue
        
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
    
    