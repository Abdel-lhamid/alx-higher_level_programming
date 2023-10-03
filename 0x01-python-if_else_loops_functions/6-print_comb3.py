#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
        if i != j:
            sep = ", " if i < 8 or j < 9 else "\n"
            print(f"{i}{j}", end=sep)
