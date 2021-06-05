import csv, os
import pandas as pd
from configparser import RawConfigParser
import psycopg2


class Load:
    '''
    Ta klasa tworzy słownik zawierający parametry połaczenia do bazy, na podstawie pliku
    konfiguracynego .ini, a następnie ładuje dane do tabeli z pliku csv
    '''

    def __init__(self, inifile: str, section: str, data_path: str):

        self.inifile = inifile
        self.section = section
        self.data_path = data_path

    def conn_params(self):

        parser = RawConfigParser()

        parser.read(self.inifile)

        database = {}

        params = parser.items(self.section)

        for param in params:
            database[param[0]] = param[1]

        return database

    def load_data(self):

        params = self.conn_params()

        connection = psycopg2.connect(**params
                                    )

        cur = connection.cursor()

        with open(self.data_path, 'r') as f:
            reader = csv.reader(f)

            for row in reader:
                cur.execute("INSERT INTO public.mask_xxx_kontrah(id_kontrahent, kontrahe, ""DL_kontrahent"")""VALUES ( %s, %s, %s);",
                            row)

            connection.commit()

            cur.close()

class ImpData:
    '''
    Ta klas pobiera dane z pliku txt znajdującego się w określonej lokalizacji,
    tworzy ramkę danych, usuwa zbedne kolumny i znaki,
    exportuje ramkę danych do cvs, a następnie usuwa utworzony plik cvs.
    '''

    def __init__(self, path_in: str, path_out: str):
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

        df = df.replace({'_': ' ', '"': ''},
                        regex=True)

        df_csv = df.to_csv(self.path_out,
                           quoting=csv.QUOTE_NONNUMERIC,
                           columns=[0, 1, 2],
                           index=False,
                           header=False,
                           encoding='windows-1250')

        return df_csv

    def clean(self):
        os.remove(self.path_out)







