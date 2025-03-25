%{
#include <stdio.h>
int real_count = 0, total_count = 0;
%}

%%
[0-9]+\.[0-9]+ {
    real_count++;
    total_count++;
    printf("Real Number: %s\n", yytext);
}

[0-9]+ {
    total_count++;
    printf("Integer: %s\n", yytext);
}

[ \t\n] { /* Ignore whitespace */ }
%%

int main() {
    printf("Enter numbers: ");
    yylex();
    
    if (total_count > 0) {
        printf("\nTotal Numbers: %d\n", total_count);
        printf("Real Numbers: %d\n", real_count);
        printf("Precision (Real Numbers / Total Numbers): %.2f\n", (float)real_count / total_count);
    } else {
        printf("\nNo numbers found.\n");
    }
    
    return 0;
}

int yywrap() {
    return 1;
}


// flex real_precision.l
// gcc lex.yy.c -o real_precision.out -ll
// ./real_precision.out