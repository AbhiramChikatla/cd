%{
#include <stdio.h>
#include <stdlib.h>
void yyerror(const char *s); 
int yylex();
%}

/* Declare token types */
%token NUMBER END
/* Define operator precedence and associativity */
%left '+' '-'
%left '*' '/'
%right UMINUS /* Unary minus (negative numbers) */
%%
input:
 expr END { printf("Valid arithmetic expression\n"); return 0; }
 ;
expr:
 expr '+' expr
 | expr '-' expr
 | expr '*' expr
 | expr '/' expr
 | '-' expr %prec UMINUS /* Handle negative numbers */
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