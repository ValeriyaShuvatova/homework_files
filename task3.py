import os


def count(file: str):  # функция, для подсчета кол-ва строк в файле.
    return sum(1 for _ in open(file, 'r', encoding='utf-8'))


def write_file(writing_file: str, path, locate):
    files = []
    for i in list(os.listdir(os.path.join(path, locate))):
        if i.endswith('.txt'):
            files.append([count(os.path.join(path, locate, i)), os.path.join(path, locate, i), i])
    for file_from_list in sorted(files):
        opening_files = open(writing_file, 'a')  # Сюда записываем (результирующий файл)
        opening_files.write(f'{file_from_list[2]}\n')  # Название файла
        opening_files.write(f'{file_from_list[0]}\n')  # Кол-во строк.
        with open(file_from_list[1], 'r', encoding='utf-8') as file:  # Путь
            counting = 1
            for line in file:
                opening_files.write(f'строка № {counting} в файле {file_from_list[2]} : {line}')
                counting += 1
        opening_files.write(f'\n')
        opening_files.close()


writing_file = os.path.abspath('result.txt')  # Сюда записываем результат.
path = os.getcwd()
locate = os.path.abspath('.')
write_file(writing_file, path, locate)