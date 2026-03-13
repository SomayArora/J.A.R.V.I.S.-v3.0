
#include<stdio.h>

int main()
{
    int choice;
    float num1, num2, res;

    printf("Simple Menu Driven Calculator\n");
    printf("1. Addition\n");
    printf("2. Subtraction\n");
    printf("3. Multiplication\n");
    printf("4. Division\n");
    printf("5. Exit\n");

    while(1)
    {
        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                printf("Enter two numbers: ");
                scanf("%f %f", &num1, &num2);
                res = num1 + num2;
                printf("Result = %.2f\n", res);
                break;

            case 2:
                printf("Enter two numbers: ");
                scanf("%f %f", &num1, &num2);
                res = num1 - num2;
                printf("Result = %.2f\n", res);
                break;

            case 3:
                printf("Enter two numbers: ");
                scanf("%f %f", &num1, &num2);
                res = num1 * num2;
                printf("Result = %.2f\n", res);
                break;

            case 4:
                printf("Enter two numbers: ");
                scanf("%f %f", &num1, &num2);
                if(num2 != 0)
                    res = num1 / num2;
                else
                    printf("Error! Division by zero is not allowed.\n");
                printf("Result = %.2f\n", res);
                break;

            case 5:
                return 0;

            default:
                printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}
