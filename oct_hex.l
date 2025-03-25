%{
/* Program to identify octal and hexadecimal numbers */
#include <stdio.h>
%}

Oct  o[0-7]+
Hex  o[xX][0-9A-Fa-f]+

%%
{Hex} { 
    printf("This is a hexadecimal number: %s\n", yytext); 
}
{Oct} { 
    printf("This is an octal number: %s\n", yytext); 
}
[0-9]+ { 
    printf("This is a decimal number: %s (Not Octal or Hex)\n", yytext); 
}
.+ { 
    printf("Invalid input: %s\n", yytext); 
}
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