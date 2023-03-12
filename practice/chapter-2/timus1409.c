#include <stdio.h>

int main()
{
    int harry, larry, total_can;
    scanf("%d %d", &harry, &larry);
    total_can = harry + larry - 1;
    printf("%d %d\n", total_can-harry, total_can-larry);
    return 0;
}