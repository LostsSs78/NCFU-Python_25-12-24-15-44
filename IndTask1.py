#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")
    
    A = {"c", "g", "h", "k", "y"}
    B = {"a", "b", "k", "n", "u"}
    C = {"i", "j", "o", "y", "z"}
    D = {"a", "b", "f", "g", "y", "z"}
    
    # X = (A ∪ B) ∩ D
    X = (A.union(B)).intersection(D)
    print(f"X = {X}")
    
    # Найдем дополнения множеств
    A_not = u.difference(A)
    C_not = u.difference(C)
    
    # Y = (Ā ∩ D) ∪ (C̅ / B)
    Y = (A_not.intersection(D)).union(C_not.difference(B))
    print(f"Y = {Y}")