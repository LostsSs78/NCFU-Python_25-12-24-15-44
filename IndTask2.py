#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import date


if __name__ == "__main__":
    # Список студентов
    students = []

    # Организовать бесконечный цикл запроса команд
    while True:
        # Запросить команду из терминала
        command = input(">>> ").lower()

        # Выполнить действие в соответствии с командой
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о работнике
            name = input("Фамилия и инициалы? ")
            group_number = input("Номер группы? ")
            marks = [int(mark) for mark in input("Успеваемость? (Список из 5 цифр, записывать через пробел)? ").split()]

            # Создать словарь
            student = {
                'name': name,
                'group': group_number,
                'marks': marks,
        }

            # Добавить словарь в список
            students.append(student)

            # Отсортировать список в случае необходимости
            if len(students) > 1:
                students.sort(key=lambda item: item.get('group', ''))

        elif command == 'list':
            # Заголовок таблицы
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 12
            )

            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^12} |'.format(
                    '№',
                    'Ф.И.О.',
                    'Номер группы',
                    'Успеваемость'
                )
            )
            print(line)

            # Вывести данные о всех сотрудниках
            for idx, student in enumerate(students, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>12} |'.format(
                        idx,
                        student.get('name', ''),
                        student.get('group', ''),
                        " ".join([str(mark) for mark in student.get('marks', '')])
                    )
                )

            print(line)

        elif command == 'select':
            count = 0

            for student in students:
                if (sum(student['marks']) / 5) > 4.0:
                    count += 1
                    print(
                        '{:>4}: {}, Группа: {}'.format(count, student.get('name', ''), student.get('group', ''))
                    )

            # Если счетчик равен 0, то работники не найдены.
            if count == 0:
                print("Студенты со средним баллом выше 4.0 не найдены")
        
        elif command == 'help':
        # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("select - вывод списка студентов со средним баллом больше 4.0;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)