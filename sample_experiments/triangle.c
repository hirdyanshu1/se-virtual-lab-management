/*
 * Experiment 1: Triangle Problem (Classic Black-box & Boundary Value Testing)
 * LabPilot AI — Software Engineering Virtual Lab
 */

#include <stdio.h>

int main() {
    int a, b, c;
    if (scanf("%d %d %d", &a, &b, &c) != 3) {
        printf("ERROR: Invalid input format\n");
        return 1;
    }

    // Boundary check for positive side lengths
    if (a <= 0 || b <= 0 || c <= 0) {
        printf("NOT_A_TRIANGLE\n");
        return 0;
    }

    // Triangle inequality theorem
    if ((a + b <= c) || (a + c <= b) || (b + c <= a)) {
        printf("NOT_A_TRIANGLE\n");
        return 0;
    }

    // Classification
    if (a == b && b == c) {
        printf("EQUILATERAL\n");
    } else if (a == b || b == c || a == c) {
        printf("ISOSCELES\n");
    } else {
        printf("SCALENE\n");
    }

    return 0;
}
