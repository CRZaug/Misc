#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>

bool isUnique(char* ptr){
	bool returnValue;
	int strLen;
	char testArray[128];

	strLen = strlen(ptr);

	// Strings larger than 128 are automatically not unique in ASCII
	if (strLen > 128){
		return false;
	}

	for (int i=0; i<strLen; i++){
		// not sure if it's truly necessary to write the next lines in two parts.
		char c = ptr[i];
		int a = c;
		if (testArray[a]!=0){
			return false;
		}
		else{
			testArray[a] = 1;
		}
	}
	return true;
}


int main(){

	int stringLength;
	char* ptr;
	bool result;

	stringLength = 128; // Any longer and this will be guarenteed NOT to be unique

	ptr =  (char*) malloc(stringLength+1); // Adding in an extra piece for the \0

	ptr = "";

	printf("This is the string %s\n",ptr);

	result = isUnique(ptr);

	printf(result ?  "true\n" : "false\n");

}
