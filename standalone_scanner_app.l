%{
#include <stdio.h>
#include <string.h>

int line_num = 1; // Initialize line number to 1

void print_transition(char *text) {
    // Print the transition sequence
    printf("%-10d %-20s ", line_num, text);
}
%}

%%
"int"|"float"|"while"|"for"|"return"|"if"|"else"|"true"|"false" {
    print_transition(yytext);
    printf("-> Keyword\n");
}

[0-9]+ {
    print_transition(yytext);
    printf("-> Integer\n");
}

[a-zA-Z_][a-zA-Z_0-9]* {
    print_transition(yytext);
    printf("-> Identifier\n");
}

"+"|"-"|"*"|"/"|"="|"=="|"<"|"<="|">"|">="|"!"|"!="|"," {
    print_transition(yytext);
    printf("-> Operator\n");
}

"("|")"|"{"|"}"|"["|"]"|";" {
    print_transition(yytext);
    printf("-> Special character\n");
}

[ \t\n\r]+ {
    // If we encounter a newline, increment the line number.
    if (yytext[0] == '\n') {
        line_num++;
    }
    // Skip whitespace (tabs, spaces).
}

. {
    print_transition(yytext);
    printf("-> Invalid character\n");
}
%%

int main(int argc, char *argv[]) {
    // Print table header
    printf("%-10s %-20s %-15s\n", "Line No.", "Lexeme", "Token");
    
    if (argc > 1) {
        FILE *f = fopen(argv[1], "r");
        if (!f) {
            perror("File open failed");
            return 1;
        }
        yyin = f;
    }
    
    yylex(); // Start lexical analysis
    return 0;
}

int yywrap() {
    return 1; // Indicate end of input
}



// flex standalone_scanner.l
// gcc lex.yy.c -o standalone_scanner.out -ll
// ./standalone_scanner.out file.txt