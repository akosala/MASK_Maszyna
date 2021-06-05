from configparser import ConfigParser
import psycopg2, csv


class Load:
	
		'''
		Ta klasa tworzy słownik zawierający parametry połaczenia do bazy, na podstawie pliku 
		konfiguracynego .ini, a następnie ładuje dane do tabeli z pliku csv 
		'''
		
		def __init__(self, inifile:str, section:str, data_path:str):
			
			self.inifile = inifile
			self.section = section
			self.data_path = data_path
	
	
		def conn_params(self):
			
			parser = ConfigParser()
			
			parser.read(self.inifile)
			
			database = {}
			
			params = parser.items(self.section)
			
			for param in params:
				
				database[param[0]] = param[1]
			
			return database
			
		
		def load_data(self):
				
			params = self.conn_params()
			
			connection = psycopg2.connect(**params)
			
			cur = connection.cursor()
			
			with open(self.data_path, 'r') as f:   
				
				reader = csv.reader(f)
				
				for row in reader:
					
					cur.execute(
					"INSERT INTO data VALUES (%s, %s, %s)",
							row)
				
				connection.commit()
				
				cur.close()