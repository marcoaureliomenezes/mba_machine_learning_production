from abc import ABC, abstractmethod

class DataAnalyser(ABC):
    
        def mine_data(self, path, email):
            self.__analyse_data(path)
            self.__send_report(email)

        def __analyse_data(self, path):
            self._open_file(path)
            self._extract_data()
            self._parse_data()
            self._close_file()

        def __send_report(self, email):
            print(f"Enviando email com relatório em anexo para {email}")

        @abstractmethod
        def _open_file(self, path):
            raise NotImplementedError()

        @abstractmethod
        def _extract_data(self):
            raise NotImplementedError()

        @abstractmethod
        def _parse_data(self):
            raise NotImplementedError()

        @abstractmethod
        def _close_file(self):
            raise NotImplementedError()


class CsvAnalyser(DataAnalyser):
    
        def _open_file(self, path):
            print(f"Abriu arquivo CSV no caminho {path}")
    
        def _extract_data(self):
            print("Extraiu dados do arquivo CSV")
    
        def _parse_data(self):
            print("Parseou dados do arquivo CSV")
    
        def _close_file(self):
            print("Fechou arquivo CSV")


class JsonAnalyser(DataAnalyser):

    def _open_file(self, path):
        print(f"Abriu arquivo JSON no caminho {path}")

    def _extract_data(self):
        print("Extraiu dados do arquivo JSON")

    def _parse_data(self):
        print("Parseou dados do arquivo JSON")

    def _close_file(self):
        print("Fechou arquivo JSON")

class Main():
    
    def test_template(self):

        csv_analyser: DataAnalyser = CsvAnalyser()
        csv_analyser.mine_data("path/to/file.csv", "marco_1234@gmail.com")
        print("\n")
        json_analyser: DataAnalyser = JsonAnalyser()
        json_analyser.mine_data("path/to/file.json", "marco_1234@gmail.com")


if __name__ == "__main__":
    main = Main()
    main.test_template()
        
    
