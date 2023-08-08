from datetime import date
import os
#id = max([int (row.split(";").pop(0)) for row in file]) + 1

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

input_file()