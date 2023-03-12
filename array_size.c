#include <stdio.h>
 
int main()
{   
    int n;
    printf("Enter the array Size: ");
    scanf("%d",&n);
    int arr[n];
    
    printf("Enter the %dth element of an array: \n",n);
    for(int i=0; i<n; i++)
    {
        scanf("%d", &arr[i]);
    }
    printf("\nThe Array is : ",n);
    for(int i=0; i<n; i++)
    {
        printf(" %d", arr[i]);
    }


}