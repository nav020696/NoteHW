from os.path import exists
from commands import *

file_name = 'note.csv'
commands = ('1 - Exit', '2 - Write','3 - Read','4 - Change', '5 - Delete')

def main():
    while True:
        print("Введите номер команды из списка")
        print(*commands, sep="\n")
        command = input("Команда: ")
        if command == '1':
            print("До свидания")
            break
        elif command == '2':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == '3':
            if not exists(file_name):
                print("Файл отсутствует. Создайте файл")
                continue 
            print(*read_file(file_name), sep="\n")
        elif command == '4':       
            is_valid_number = False
            while not is_valid_number:
                try:
                    ident = int(input("Введите идентификатор заметки для изменения: "))
                    print('Какие данные Вы хотите изменить: заголовок или текст?')
                    print ('1 - Заголовок')
                    print ('2 - Текст')
                    dates = input()
                    change_note(file_name, ident, dates)
                    is_valid_number = True
                except ValueError:
                    print("Не валидный номер заметки")
                    continue
        elif command == '5':       
            is_valid_number_1 = False
            while not is_valid_number_1:
                try:
                    ident_of_note = int(input("Введите идентификатор заметки для удаления: "))
                    delete_note(file_name, ident_of_note)
                    is_valid_number_1 = True
                except ValueError:
                    print("Не валидный номер заметки")
                    continue   
main()