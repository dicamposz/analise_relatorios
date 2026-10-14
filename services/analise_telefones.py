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