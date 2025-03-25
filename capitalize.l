%{
#include <stdio.h>
#include <ctype.h>
%}
%%
[a-z] { putchar(toupper(yytext[0])); }
. { putchar(yytext[0]); }
%%
int main() {
yylex();
return 0;
}
int yywrap() {
    return 1;
}
// flex capitalize.l
// gcc  lex.yy.c -o cap.out -ll
// ./cap.out 