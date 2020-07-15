#include<stdio.h>
#include<string.h>
#include<stdbool.h>

int main(void){

    char string[3] = "afb";
    bool match;

    for (int i =0; i<strlen(string); i++){

        char tempChar1 = string[i];

        for (int j =0; j<strlen(string); j++){
            char tempChar2 = string[j];
                // printf("%c, %c", tempChar1, tempChar2);
            if (tempChar1 == tempChar2 && i != j){
                
                match = true;
                break;
            }
            else {
                // This might be in the wrong place but I think it is ok
                match = false; 
            }
        }
    }

    printf(match ? "true\n" : "false \n");
    if (match == true){
            printf("Not unique \n");
        }
        else {
            printf("Unique \n");
        }
}