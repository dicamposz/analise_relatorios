import pandas as pd
import logging
from pathlib import Path

class Analisar_Telefones:
    
    def __init__(self, mounth, product, mailing, dir_txt_retorno = None, dir_csv_retorno = None, dir_csv_unido = None, carga_mailing = None):
        self.mounth_relatory = mounth
        self.product = product
        self.mailing_product = mailing
        self.txt_retorno = dir_txt_retorno
        self.dir_retorno = dir_csv_retorno
        self.csv_unido = dir_csv_unido
        self.carga_mailing =carga_mailing
    
    
    
    def convert_txt_in_csv(dir_txt_retorno, mounth_relatory, product):

        folder_exit = Path(__file__).resolve().parent / f"csv_retorno_gerado {product} - {mounth_relatory}"
        folder_exit.mkdir(exist_ok = True)
    
        archive_txt_to_csv = sorted(dir_txt_retorno.glob("*.txt"))
        
        if not archive_txt_to_csv:
            raise SystemExit("Nenhum TXT foi encontrado")

        errors = []
        
        for txt in archive_txt_to_csv:
            
            try:
                df = pd.read_csv(txt, sep="|")
                df.to_csv(folder_exit / f"{txt.stem}.csv", sep=";", index=False, encoding="utf-8-sig")
            
            except Exception as e:
                errors.append((txt.name, str(e)))
                
        print(f"{len(archive_txt_to_csv) - len(errors)} de {len(archive_txt_to_csv)} arquivos convertidos")
        for nome, erro in errors:
            print(f"  {nome}: {erro}")
        print(f"\n{len(errors)} erros encontrados!")
        
        
        
    def concat_csv_return(dir_csv_retorno, mounth_relatory, product):
        
        folder_exit = Path(__file__).resolve().parent / f"csv_retorno_unido_{product}_{mounth_relatory}"
        folder_exit.mkdir(exist_ok = True)
           
        csv_concat = sorted(dir_csv_retorno.glob("*.csv")) 
        
        if not csv_concat:
            raise SystemExit("Nenhum CSV foi encontrado")
        
        print(f"\n{len(csv_concat)} arquivos encontrados")
        
        csv_unido = pd.concat((pd.read_csv(a) for a in csv_concat), ignore_index=True)
        csv_unido.to_csv(folder_exit / f"csv_unido_{product}_{mounth_relatory}.csv", index=False)
            
        print(f"Total de linhas concatenadas: {len(csv_unido)}")
        
        
        
    def remove_duplicates(dir_csv_unido, mounth_relatory, product):
        
        folder_exit = Path(__file__).resolve().parent / f"csv__unido_sem_duplicadas_{product}_{mounth_relatory}"
        folder_exit.mkdir(exist_ok = True)
        
        df = pd.read_csv(dir_csv_unido, sep=";")
        removed_duplicades = df.drop_duplicates(subset=[df.columns[0], df.columns[1]])
        removed_duplicades.to_csv(folder_exit / f"{product} sem duplicadas - {mounth_relatory}.csv", sep=";", index=False)   
             
        print(f"Total: {len(df)} | Final: {len(removed_duplicades)}")
        
        
        
    def verify_tel_cpf(mailing, mounth, product, dir_csv_unido):
        ...
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def contabil_ids(dir_csv_unido, carga_mailing, mounth, day_acumulado, product):
        
        folder_exit = Path(__file__).resolve().parent / f"IDS_Ocorrencias"
        folder_exit.mkdir(exist_ok = True)
        
        i = 0
        j = 0
        total_lines_csv = 0
        num_ocurrences = 0
        verify_index = 0
        list_id_verified = []
        lines_exit = []
        errors = []
        
        df_carga_mailing = pd.read_excel(carga_mailing)
        
        while True:
              
            j = 0
            cel_carga_mailing = int(df_carga_mailing.iloc[i, 1])
            
            for chunk in pd.read_csv(dir_csv_unido, sep=";", chunksize=500_000):
                
                total_lines_csv += len(chunk)
            
                while True:
                
                    cel_csv_unido = int(chunk.iloc[j, 0])
                    if cel_carga_mailing == cel_csv_unido:
                        num_ocurrences += 1
                        if cel_carga_mailing not in list_id_verified:
                            list_id_verified.append(cel_carga_mailing)
                
                    j += 1
                    verify_index += 1
                    
                    if j == 500_000 or verify_index == total_lines_csv:
                        j = 0
                        break
                    
                print(f"Verificadas: {total_lines_csv}")
                
            print(f"\nTotal de linhas verificadas para o id {cel_carga_mailing}")
            print(f"ID - {cel_carga_mailing} - foi encontrado - {num_ocurrences} - vezes em - {total_lines_csv} - linhas\n\n")
            
            lines_exit.append({"ID": cel_carga_mailing, "ocorrencias": num_ocurrences})
            
            i += 1
            total_lines_csv = 0
            num_ocurrences = 0
            verify_index = 0
                                  
            if i == len(df_carga_mailing):
                print(f"\n{len(df_carga_mailing)} IDs lidos ---")
                break
        
        df_relatory = pd.DataFrame(lines_exit)
        df_relatory.to_excel(folder_exit / f"Ids - {product}_{mounth} acumulado até {day_acumulado}.xlsx", index=False)