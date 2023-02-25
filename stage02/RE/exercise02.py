"""
从exc.txt中输入一个端口名称，然后返回一个地址，输错则提示输入错误。
exc.txt的格式是第一段是设备信息，从第二段开始是一个端口生成的信息，
每两段中间都有一个空行。每一段第一个单词就是端口名。
"""
import re


class PortManager:
    def __init__(self, file="./exc.txt"):
        self.file = file
        self.port_pattern = r"^\w+"
        self.addr_pattern = r"address is ([\/\.\d]+)"

    def get_addr(self):
        port = input("请输入端口名：")
        addr = self.__get_addr(port)
        print(addr)

    def __get_addr(self, port):
        count = 0
        for p in self.__get_paragraphs():
            if port == re.findall(self.port_pattern, p):
                count += 1
                return self.__use_re(p)
            else:
                continue
        self.__port_not_found()

    def __get_paragraphs(self):
        f = open(self.file, "r")
        data = f.read()
        paragraphs = data.split("\r\n\r\n")[1:]
        return paragraphs

    def __use_re(self, para):
        return re.search(self.addr_pattern, para).group(1)

    @staticmethod
    def __port_not_found():
        print("输入的端口有误")


def main():
    manager = PortManager()
    manager.get_addr()


if __name__ == '__main__':
    main()
