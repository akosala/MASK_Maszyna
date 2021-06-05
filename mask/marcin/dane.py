import csv, os
import pandas as pd


class ImpData:

    '''
    Ta klas pobiera dane z pliku txt znajdującego się w określonej lokalizacji, 
    tworzy ramkę danych, usuwa zbedne kolumny i znaki,
    exportuje ramkę danych do cvs, a następnie usuwa utworzony plik cvs.
    '''

    def __init__(self, path_in:str, path_out:str):
        
        self.path_in = path_in
        self.path_out = path_out

    def impexp(self):
        
        df = pd.read_fwf(self.path_in,
                     sep='delimiter',
                     header=None,
                     engine='python',
                     skiprows=2,
                     skipfooter=2,
                     skipinitialspace=True,
                     encoding='windows-1250',
                     )

        df = df.replace({'_': ' ', '"':''},
                        regex=True)


        df_csv = df.to_csv(self.path_out,
                       quoting=csv.QUOTE_NONNUMERIC,
                       columns=[0,1,2],
                       index=False,
                       header=False,
                       encoding='utf-8')

        return df_csv
       
    def clean(self):
       
       os.remove(self.path_out)
