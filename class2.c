#include <stdio.h>

int main() {
    char operator;
	double a, b, ans;

    printf("What do you want to do (+, -, *, /): ");
    scanf(" %c", &operator);

    printf("Enter 2 numbers: ");
    scanf("%lf %lf", &a, &b);

    if (operator == '+') {
        ans = a + b;
        printf("Result: %lf\n", ans);
    } 
    else if (operator == '-') {
        ans = a - b;
        printf("Result: %lf\n", ans);
    } 
    else if (operator == '*') {
        ans = a * b;
        printf("Result: %lf\n", ans);
    } 
	else if(operator =='/') {
        if (b==0){
            printf("Can't divide by 0");
        }
        else{
            ans = a / b;
            printf("Result: %lf\n", ans);
        }
    }
    else {
        printf("You entered a wrong operator :(\n");
    }

    return 0;
}

