%{
/* Define regular expressions for identifiers and keywords */
#include <stdio.h>
%}
%%
int|if|include { printf("Keyword: %s\n", yytext); }
[iI][a-zA-Z0-9_]* { printf("Identifier: %s\n", yytext); }
[ \t\n] { /* Ignore whitespace */ }
. { /* Ignore other characters */ }
%%
int main() {
 yylex(); /* Call the lexer */
 return 0;
}
int yywrap() {
 return 1;
}

// flex identifiers_starting_with_i.l
// gcc lex.yy.c -o identifiers.out -ll
// ./identifiers.out 