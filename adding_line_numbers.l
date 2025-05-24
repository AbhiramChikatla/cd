%{
#include <stdio.h>
int line_number = 1;
%}

%%
^(.*)\n { 
    printf("%d %s\n", line_number++, yytext); 
}

. { 
    printf("%s", yytext); 
}
%%

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input_file>\n", argv[0]);
        return 1;
    }
    
    FILE *fp = fopen(argv[1], "r");
    if (!fp) {
        perror("Error opening file");
        return 1;
    }
    
    yyin = fp;
    yylex();
    fclose(fp);
    return 0;
}

int yywrap() {
    return 1;
}