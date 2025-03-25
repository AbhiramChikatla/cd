%{
#include <stdio.h>
%}
%%
[aeiouAEIOU] { printf("Vowel: %s\n", yytext); }
[a-zA-Z] { printf("Consonant: %s\n", yytext); }
[^a-zA-Z] { printf("Other character: %s\n", yytext); }
%%
int main() {
 printf("Enter text: ");
 yylex();
 return 0;
}
int yywrap() {
 return 1;
}

// flex vowels_consonants.l
// gcc lex.yy.c -o vowels.out -ll
// ./vowels.out