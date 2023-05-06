#include <stdio.h>

int main() {
    char str[100];
    int count=0;
    printf("Enter a string: ");
    gets(str); //  // get full line of string input


    printf("Vowels: ");
    for(int i=0; i<strlen(str); i++)
    {
        if(str[i]=='A' || str[i]=='E' || str[i]=='I' || str[i]=='O' || str[i]=='U')
        {
            printf("%c, ", str[i]);
            count++;
        }
        else if(str[i]=='a' || str[i]=='e' || str[i]=='i' || str[i]=='o' || str[i]=='u')
        {
            printf("%c ", str[i]);
            count++;
        }

        
    }
    printf("\nNumber of Vowels: %d\n", count);
    return 0;
}