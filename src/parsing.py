import csv

class AvgGdpData:

    @staticmethod
    def _parse_csv_file(file:str)->dict[str,list[int]]:
        """
        Принимает путь к файлу и возвращает словарь вида:
        \t{'Страна': ['Сколько раз встретили страну', 'Cумма gdp'] }
        """

        if not file.lower().endswith('.csv'):
            print(f'Файл {file} не найден')
            return {}
        
        result = {}
        try:
            with open(file,'r') as csvfile:
                                
                reader = csv.DictReader(csvfile)
                
                for row in reader:
                    country = row['country']
                    gdp = float(row['gdp'])

                    if country not in result:
                        result[country]=[0,0]
                    result[country][0]+=1
                    result[country][1]+=gdp
                
                return result

        except FileNotFoundError:
            print(f'Файл {file} не найден')
            return {}

    @classmethod
    def avg_gdp_list(self, files:list[str])->list[list[str,int]]:
        '''
        Возвращает отсортированный список стран по среднему gdp 
        '''
        result = {}
        for file in files:

            data = self._parse_csv_file(file)
            if not data:
                continue
        
            for country, values in data.items():                
                if country not in result:
                    result[country] = [0, 0.0]

                result[country][0]+=values[0]
                result[country][1]+=values[1]
            

        result = {country:round((data[1]/data[0]),2) for country, data in result.items()}
        sorted_result = dict(reversed(
                            sorted(result.items(), key = lambda item:item[1])
                            ))
        
        return [[country,gdp] for country, gdp in sorted_result.items()]