#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")
    common_chars = set(str1) & set(str2)
    print(f"Общие символы: {common_chars}")