%{
#include <stdio.h>
#include <string.h>
void check_keyword(char *str);
%}
%%
"if"|"else"|"while"|"return"|"int"|"float"|"char" { 
    printf("Keyword: %s\n", yytext); 
}

[a-zA-Z_][a-zA-Z0-9_]* { 
    check_keyword(yytext); 
}

[ \t\n]+ ; /* Ignore whitespace */

. { 
    printf("Other character: %s\n", yytext); 
}
%%

void check_keyword(char *str) {
    // List of keywords
    char *keywords[] = {"if", "else", "while", "return", "int", "float", "char"};
    int num_keywords = sizeof(keywords) / sizeof(keywords[0]);
    
    for (int i = 0; i < num_keywords; i++) {
        if (strcmp(str, keywords[i]) == 0) {
            printf("Keyword: %s\n", str);
            return;
        }
    }
    printf("Identifier: %s\n", str);
}

int main() {
    yylex(); // Start scanning input
    return 0;
}
int yywrap(){
    return 1;
}

// flex identifier.l
// gcc  lex.yy.c -o identifier.out -ll
// ./identifier.out 