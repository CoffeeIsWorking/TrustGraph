#include <stdio.h>

int main() {
    double user_input = 0.0;

    printf("Enter a number (e.g., 3.75): ");
    
    // ❌ BUG: %f is for float (4 bytes), but user_input is a double (8 bytes)
    scanf("%f", &user_input); 

    // This will print a bizarre, random number or 0.000000 because memory got corrupted!
    printf("You entered: %lf\n", user_input); 

    return 0;
}
