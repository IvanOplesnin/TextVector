from action import *


def main():
    '''
    Основной поток программы.
    '''
    command = None
    list_f = []
    # Определяем ссылку на список с фигурами в функцию просмотра фигур.
    action_dict['show_figure'] = lambda x=list_f: show_figure(x)
    # Определяем ссылку на список с фигурами в функцию удаления фигуры.
    action_dict['delete_figure'] = lambda id, x=list_f: delete_figure(id, x)
    my_help()  # Информационное сообщение о возможных командах.
    while command != 'exit':
        command, *args = input('>>> ').split()
        if 'create' in command:
            if command in action_dict:
                try:
                    list_f.append(action_dict[command](*args))
                except TypeError as e:
                    print('Ожидалось другое кол-во аргументов', e)
                except ValueError as e:
                    print(f'Не удалось преобразовать данные в числа\n'
                          f'{e}')
            else:
                print('Такой команды не существует')
        elif command not in action_dict.keys() and command != 'exit':
            print('Такой команды не существует')
        else:
            action_dict[command](*args)


if __name__ == '__main__':
    main()
