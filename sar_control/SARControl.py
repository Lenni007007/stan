import paramiko
#from parser.sar import SarXmlParser

class SARControl:
    def __init__(self, host=None, port=None, user=None, passwd=None, ):
        self.sar_binary_path = None
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.client = paramiko.SSHClient()
    def connect(self):
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.host, port=self.port, username=self.user, password=self.passwd)
        #return ssh
        # stdin, stdout, stderr = client.exec_command('ls -l')
        # data = stdout.read() + stderr.read()
        # print(data)
        # client.close()  # Connect to server via ssh

    def upload_sar(self, path_from=None, path_to=None): #Загрузка бинарников из path_from на локальной тачке на удаленную тачку по пути path_to по уже установленному коннекту
        output = self.client.exec_command('echo $HOME')
        print(output[1].read())
        transfer = self.client.open_sftp()
        transfer.put(path_from, path_to)
        transfer.close()

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
    sar = SARControl(host='192.168.126.133', port=22, user='root', passwd='root')
    sar.connect()
    sar.upload_sar('/home/greg/Programs/SAR.tar.xz', '/root/SAR.tar.xz')
    # .....)
    # data = sar.parse_sar_data()
    # StanGraph.plot(data)