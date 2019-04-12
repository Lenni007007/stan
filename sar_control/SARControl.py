import paramiko
from parser.sar import SarXmlParser

class SARControl:
    def __init__(self, host=None, port=None, user=None, passwd=None):
        self.sar_binary_path = None
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        pass

    def connect(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=self.host, port=self.port, username=self.user)
        stdin, stdout, stderr = client.exec_command('ls -l')
        data = stdout.read() + stderr.read()
        client.close()
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

    # def parse_sar_data(self):
    #     parser = SarXmlParser()
    #     parser.parse()
    #     return parser.get_stat()


if __name__ == '__main__':
    sar = SARControl(host='192.168.78.117', port=22, user='root')
    sar.connect()
    # .....)
    # data = sar.parse_sar_data()
    # StanGraph.plot(data)