#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>

// Something I have learned from this: allocating memory with malloc makes for READ ONLY data
char* sortString(char ptr[]){
	int l = strlen(ptr);
	char temp;

	for (int i=0;i<l-1;i++){

		for (int j = i+1; j<l;j++){
			if (ptr[i]>ptr[j]){
				temp = ptr[i];
				ptr[i]=ptr[j];
				ptr[j]=temp;
			}
		}
	}	
	return ptr;
}

bool isPerm(char string1[], char string2[]){

	char* ptr1 = sortString(string1);
	char* ptr2 = sortString(string2);
	printf("%s\n",ptr1);
	printf("%s\n",ptr2);

	if (strcmp(ptr1,ptr2)==0){
		return true;
	}

return false;

}

int main(){

	char string1[]="asdfafsdstring2";
	char string2[]="string2";

	bool result;

	if (strlen(string1) != strlen(string2)){	
		printf("in the right place");
		result = false;
	}
	else{	
		result = isPerm(string1, string2);
	}
	printf(result ? "isPerm: true\n" : "isPerm: false\n");

	

}
