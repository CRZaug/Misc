#include<stdio.h>
#include<stdlib.h>

int main() {

	
	int stringLength;
	char* ptr;

	stringLength = 0;
	
	printf("%i\n", stringLength);
	printf("%p\n", &stringLength);

	printf("Insert the number of letters in your name: ");
	scanf("%i",&stringLength);
	
	printf("\n%p\n",&ptr);

	// pointer: advance number of bits made up by that type 
	ptr = (char*) malloc(stringLength);

	printf("\n%p\n",ptr);	

	printf("Insert your name: ");
	scanf("%s",ptr);

	printf("Hello, my name is: %s", ptr);
}
