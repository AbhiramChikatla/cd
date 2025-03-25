%{
#include "bas.tab.h"
%}
%%
[a] { return A; }
[b] { return B; }
[\n] { return '\n'; }
. { /* Ignore other characters */ }
%%
int yywrap() {
 return 1;
}

// bison -d bas.y
// flex bas.l
// gcc -o parser lex.yy.c bas.tab.c -lfl
// ./parser.out