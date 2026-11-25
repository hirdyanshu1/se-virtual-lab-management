"""
Experiment 1: Triangle Problem (Python Implementation)
LabPilot AI — Software Engineering Virtual Lab
"""
import sys

def main():
    try:
        raw = sys.stdin.read().split()
        if len(raw) < 3:
            print("ERROR: Invalid input format")
            return
        a = int(raw[0])
        b = int(raw[1])
        c = int(raw[2])
    except Exception:
        print("ERROR: Invalid input format")
        return

    # Boundary check
    if a <= 0 or b <= 0 or c <= 0:
        print("NOT_A_TRIANGLE")
        return

    # Triangle inequality theorem
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        print("NOT_A_TRIANGLE")
        return

    if a == b == c:
        print("EQUILATERAL")
    elif a == b or b == c or a == c:
        print("ISOSCELES")
    else:
        print("SCALENE")

if __name__ == "__main__":
    main()
