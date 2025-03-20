from models import *


def my_help():
    text = ('Список команд:\n'
            'help - список команд\n'
            'show_figure - вывести список фигур\n'
            'delete_figure <id> - удалить фигуру\n'
            'create_point <x> <y> - создать точку\n'
            'create_line <x1> <y1> <x2> <y2> - создать вектор\n'
            'create_circle <x> <y> <radius> - создать круг\n'
            'create_square <x> <y> <size> - создать квадрат координаты x, y означают левый верхний угол\n'
            'Для выхода напишите exit')
    print(text)


def delete_figure(id: str, list_figures: list):
    id = int(id)
    if id <= len(list_figures):
        print(list_figures.pop(id), ' - удалена!')
    else:
        print('Такой фигуры нет!')


def show_figure(list_figures: list):
    for i in range(len(list_figures)):
        print(f'{i} - {list_figures[i]}')


# словарь команд, которые можно вызвать через консоль
action_dict = {
    'help': my_help,
    'create_point': Point,
    'create_line': Vector,
    'create_circle': Circle,
    'create_square': Square,
    'delete_figure': delete_figure,
    'show_figure': show_figure,
}
