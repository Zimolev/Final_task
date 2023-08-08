from datetime import date
import os

def input_file():
    """Добавляет заметку в блокнот."""
    current_date = date.today()
    heading = input("Введите заголовок заметки: ")
    note_body = input("Введите тело заметки: ")
    with open('note.csv', 'a', encoding='utf-8') as note:
       id = get_id()
       note.write(f"{id}; {current_date}; {heading}; {note_body}\n")
    print("Заметка успешно сохранена")
    note.close()

def get_id() -> None:
    """Поиск последнего id"""    
    with open('note.csv', 'r', encoding='utf-8') as file:
        if (os.stat("note.csv").st_size == 0):
            id = 1
        else:
            id = max([int (row.split(";").pop(0)) for row in file]) + 1
            print(id)
    return id

def find_data() -> list:
    """Контекстный поиск по все заметкам."""
    with open('note.csv', 'r', encoding='utf-8') as file:
        note = file.read().split('\n')
    text_to_find = input('Введите текст который хотите найти: ')
    result = search(note, text_to_find)
    return result

def find_data_print() -> None:
    """Контекстный поиск по всем заметкам и вывод на экран."""
    with open('note.csv', 'r', encoding='utf-8') as file:
        note = file.read().split('\n')
    text_to_find = input('Введите текст который хотите найти: ')
    result = search(note, text_to_find)
    print(result)

def search(note: list[str], info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    result = [text for text in note if info in text]
    if not result:
        return "Совпадений нет"
    elif len(result) == 1:
        return result[0]
    elif len(result) > 1:
        print()
        print('________________')
        print('\n'.join(result))
        new_info = input('Введите уточнения поиска: ')
        return search(result, new_info)

def delete(line: list[str]) -> None:
    line_del = line
    with open('note.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open('note.csv', 'w', encoding='utf-8') as file:
        for line in lines:
            if line.strip("\n") != line_del:
                file.write(line)

def update(line: list[str]) -> None:
    old_data = line
    old_data_array = old_data.split(";")
    heading = input("Введите заголовок заметки, если не хотите менять оставте пустым: ")
    note_body = input("Введите тело заметки, если не хотите менять оставте пустым: ")
    if (heading != ""): 
        old_data_array[len(old_data_array) - 2] = heading
    if (note_body != ""): 
        old_data_array[len(old_data_array) - 1] = note_body
    delete(old_data)
    with open('note.csv', 'a', encoding='utf-8') as note:
       note.write(f"{old_data_array[0]}; {date.today()}; {old_data_array[2]}; {old_data_array[3]}\n")

def data_print() -> None:
    with open('note.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        print(line)
