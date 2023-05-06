#include <stdio.h>
 
int main()
{   
    int n=8;
    float arr[n], max, min, total, avg, number;
    
    printf("Enter the 8th element of an array: \n");
    for(int i=0; i<8; i++)
    {
        scanf("%f", &arr[i]);
    }
 
    max = arr[0];
    min = arr[0];
    total = 0;
 
 
    printf("\nTotal Elements of the Array: ");
    for(int i=0; i<8; i++)
    {
        // for maximum number
        if(arr[i] > max)
        {
            max = arr[i];
        }
        // for minimum number
        if(arr[i] < min)
        {
            min = arr[i];
        }   
        total += arr[i];
 
        printf(" %.0f ", arr[i]);
    }
 
    // find the average.
    avg = total/n;
 
    printf("\nMaximum: %.2f\n", max);
    printf("Minimum: %.2f\n", min);
    printf("Average: %.2f\n", avg);
 
}