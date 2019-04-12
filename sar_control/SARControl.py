from parser.sar import SarXmlParser

class SARControl:
    def __init__(self, host: str, port: int, login: str, passwd:str):
        self.sar_binary_path = None
        self.host = host
        pass

    def connect(self):
        pass  # Connect to server via ssh

    def upload_sar(self, path_from: str, path_to:str):
        pass  # Загрузка бинарников из path_from на локальной тачке на удаленную тачку по пути path_to по уже установленному коннекту

    def start_sar(self, path: str):
        pass  # Запуска САРа на удаленной тачке и сохранение результатов в path (на удаленной тачке)

    def stop(self):
        pass  # Остановка SARa

    def parse(self):
        pass  # Парсинг в csv результатов

    def collect(self, path_to_save):
        pass  # копирование результатов (лучше не только csv, а всех) на локальную тачку по пути path_to_save

    def config(self, sar_path: str, sar_dest_path: str):
        pass

    def connect_and_start(self, path_to_save: str):
        self.connect()
        self.upload_sar(self.sar_path)
        self.start_sar(path_to_save)

    def parse_sar_data(self):
        parser = SarXmlParser()
        parser.parse(path)
        return parser.get_stat()


if __name__ == '__main__':
    sar = SARControl()
    sar.connect()
    .....)
    data = sar.parse_sar_data()
    StanGraph.plot(data)