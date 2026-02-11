#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    original_dict = {
    1: "один",
    2: "два",
    3: "три",
    4: "четыре"
    }

    reversed_dict = {value: key for key, value in original_dict.items()}
    print(f"Исходный словарь: {original_dict}")
    print(f"Обратный словарь: {reversed_dict}")