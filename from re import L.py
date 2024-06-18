from re import L
import sys

line = sys.stdin.read().rstrip().split("\n")
line.pop()
final = 0
save = []
for case in line:
    case = case.split(' ')
    cases = [int(i) for i in case]
    m = ((cases[0]**4 + cases[1]**2) * (cases[2]**(1/2) / cases[3]))**(1/3)
    if m > final:
        m = final
        save = case

print(f"{save[0]} Kindess, {save[1]} Stickers On Phone, {save[2]} Friends and {save[3]} Laughter produced the most Magic: {final}")
        
