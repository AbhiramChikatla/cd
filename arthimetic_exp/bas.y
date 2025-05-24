%{
#include <stdio.h>
#include <stdlib.h>
void yyerror(const char *s); 
int yylex();
%}

%token NUMBER END
%left '+' '-'
%left '*' '/'
%right UMINUS 
%%
input:
 expr END { printf("Valid arithmetic expression\n"); return 0; }
 ;
expr:
 expr '+' expr
 | expr '-' expr
 | expr '*' expr
 | expr '/' expr
 | '-' expr %prec UMINUS 
 | '(' expr ')'
 | NUMBER
 ;
%%
void yyerror(const char *s) {
 fprintf(stderr, "Error: %s\n", s);
}
int main() {
 printf("Enter an arithmetic expression:\n");
 return yyparse();
}