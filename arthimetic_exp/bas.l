%{
#include "bas.tab.h"
%}
%%
[0-9a-z]+ { 
    yylval = atoi(yytext); return NUMBER; 
    }
[\t ]+ { /* Ignore whitespaces */ }
[\n] { return END; }
[+\-*/()] { return *yytext; }
. { 
    printf("Invalid character: %s\n", yytext);
     return 0; }
%%
int yywrap() { 
    return 1;
    
     }

// bison -d bas.y
// flex bas.l
// gcc -o parser lex.yy.c bas.tab.c -lfl
// ./parser.out