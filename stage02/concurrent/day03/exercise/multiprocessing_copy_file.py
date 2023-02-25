from multiprocessing import Process, freeze_support


def copy_file(data, file_name):
    f = open(file_name, "wb")
    f.write(data)
    f.close()


if __name__ == "__main__":
    freeze_support()
    f = open("face.jpg", "rb")
    bytes_data = f.read()
    f.close()

    mid = len(bytes_data) // 2
    p1 = Process(target=copy_file, args=(bytes_data[:mid], "1.jpg"))
    p2 = Process(target=copy_file, args=(bytes_data[mid:], "2.jpg"))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
