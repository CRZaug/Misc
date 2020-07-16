#include<stdio.h>
#include<stdlib.h>

int main() {

	
	int stringLength;
	char* ptr;

	stringLength = 0;
	
	// Prints the variable
	printf("%i\n", stringLength);

	// Prints the location of the variable in memory
	printf("%p\n", &stringLength);

	printf("Insert the number of letters in your name: ");
	scanf("%i",&stringLength);
	
	// Prints the location of the pointer in memory (stack)
	printf("\n%p\n",&ptr);
 
	ptr = (char*) malloc(stringLength);
	
	// prints memory allocated to pointer in the heap
	printf("\n%p\n",ptr);	

	printf("Insert your name: ");
	scanf("%s",ptr);

	printf("Hello, my name is: %s", ptr);
}
