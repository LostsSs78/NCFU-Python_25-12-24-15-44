#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    input_string = input("Введите строку: ")
    vowels = set("аеёиоуыэюяАЕЁИОУЫЭЮЯ")
    count = sum(1 for char in input_string if char in vowels)
    print(f"Количество гласных: {count}")