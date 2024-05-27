#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В операционных системах на базе Unix обычно присутствует утилита с названием head.
# Она выводит первые десять строк содержимого файла, имя которого передается в качестве
# аргумента командной строки. Напишите программу на Python, имитирующую поведение
# этой утилиты. Если файла, указанного пользователем, не существует, или не задан
# аргумент командной строки, необходимо вывести соответствующее сообщение об ошибке

import sys

def head(file_name):
    try:
        with open(file_name, 'r') as file:
            for _ in range(10):
                line = file.readline()
                if not line:
                    break
                print(line, end='')
    except FileNotFoundError:
        print("Ошибка: Файл не найден")
    except:
        print("Ошибка: Что-то пошло не так")

if len(sys.argv) < 2:
    print("Ошибка: Не указан файл")
else:
    head(sys.argv[1])