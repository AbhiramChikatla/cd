%{
#include <stdio.h>
#include <stdlib.h>
void yyerror(const char* s);
int yylex();
%}
%token A B
%%
start: S '\n' { return 0; }
 ;
S: A S B
 | ;
%%
int main() {
 printf("Enter the String: ");
 if (yyparse() == 0) {
 printf("Valid String\n");
 }
 return 0;
}
void yyerror(const char* s) {
 printf("String is not accepted\n");
 exit(0);
}
