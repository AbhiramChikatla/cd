%{
#include <stdio.h>
#include <string.h>


void print_transition(char *text) {
    // Print the transition sequence
    printf("Transition sequence: ");
    for (int i = 0; i < strlen(text); i++) {
        printf("%c", text[i]);
        if (i != strlen(text) - 1) {
            printf("->");
        }
    }
}
%}

%%
"int"|"float"|"while"|"for"|"return"|"if"|"else"|"true"|"false" {
    print_transition(yytext);
    printf(" -> Keyword\n");
}

[0-9]+ {
    print_transition(yytext);
    printf(" -> Integer\n");
}

[a-zA-Z_][a-zA-Z_0-9]* {
    print_transition(yytext);
    printf(" -> Identifier\n");
}

"+"|"-"|"*"|"/"|"="|"=="|"<"|"<="|">"|">="|"!"|"!="|"," {
    print_transition(yytext);
    printf(" -> Operator\n");
}

"("|")"|"{"|"}"|"["|"]"|";" {
    print_transition(yytext);
    printf(" -> Special character\n");
}

[ \t\n\r]+ { /* Skip whitespace */ }

. {
    printf("Invalid character: %s\n", yytext);
}
%%

int main(int argc, char *argv[]) {
    if (argc > 1) {
        FILE *f = fopen(argv[1], "r");
        if (!f) {
            perror("File open failed");
            return 1;
        }
        yyin = f;
    }
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}

// flex dfa.l
// gcc lex.yy.c -o dfa.out -ll
// ./dfa.out file.txt