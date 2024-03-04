from os.path import exists
from csv import DictReader, DictWriter
import datetime

def get_info():
    index = 0
    title = input("Введите заголовок заметки ")
    body = input("Введите текст заметки ")
    dt_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return [index+1, title, body, dt_now]


def create_file(file_name):
    #менеджер контекста
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Идентификатор', 'Заголовок', 'Текст', 'Дата и время последнего изменения'])
        f_writer.writeheader()

def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)
        
def write_file(file_name, lst):
    res = read_file(file_name)   
    obj = {'Идентификатор' : lst[0], 'Заголовок' : lst[1], 'Текст' : lst[2], 'Дата и время последнего изменения' : lst[3]}
    res.append(obj)
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Идентификатор', 'Заголовок', 'Текст', 'Дата и время последнего изменения'])
        f_writer.writeheader()
        f_writer.writerows(res)

file_name = 'note.csv'

def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            print("До свидания")
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print("Файл отсутствует. Создайте файл")
                continue 
            print(*read_file(file_name), sep="\n")            
main()