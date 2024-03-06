from csv import DictReader, DictWriter
import datetime

index = 0
def count():
    global index
    index += 1
    return index

def get_info():
    i = count()
    title = input("Введите заголовок заметки ")
    body = input("Введите текст заметки ")
    dt_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return [i, title, body, dt_now]

def create_file(file_name):
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

def write_file_1(file_name, res):
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Идентификатор', 'Заголовок', 'Текст', 'Дата и время последнего изменения'])
        f_writer.writeheader()
        f_writer.writerows(res)

def change_note(file_name, number_of_note, dates):
    res = read_file(file_name)
    if number_of_note > len(res) or number_of_note <= 0:
        print("Заметки с таким идентификатором не существует")
        return
    temp = res[number_of_note - 1]
    if dates == '1':
        new_title = input("Введите новый заголовок заметки ")
        temp['Заголовок'] = new_title
    else:
        new_body = input("Введите новый текст заметки ")
        temp['Текст'] = new_body
    temp['Дата и время последнего изменения'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    res[number_of_note - 1] = temp
    write_file_1(file_name, res)

def delete_note(file_name, number_of_note):
    res = read_file(file_name)
    if number_of_note > len(res) or number_of_note <= 0:
        print("Заметки с таким идентификатором не существует")
        return
    res.pop(number_of_note - 1)
    write_file_1(file_name, res)