import final_task
while True:
    print('1. вывод, 2. добавление, 3. поиск, 4 изменение, 5 удаление, прочее выход')
    mode = int(input())
    if mode == 1:
        final_task.data_print()
    elif mode == 2:
        final_task.input_file()
    elif mode == 3:
        final_task.find_data_print()
    elif mode == 4:
        final_task.update(final_task.find_data())
    elif mode == 5:
        final_task.delete(final_task.find_data())
    else:
        break