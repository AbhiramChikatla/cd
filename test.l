%{
#include<stdio.h> 
#include<string.h> 
int line_num=1;

void print_transition(char *text){
    printf("%-10d %-20s",line_num,text);
}
%}

%%
"int"|"while"|"do"|"return"|"if"|"for" {
    print_transition(yytext);
    printf("- > keyword\n");
}
[0-9]+ {
    print_transition(yytext);
    printf("- > Integer\n");
}
[a-zA-Z_][a-zA-Z0-9_]+ {
    print_transition(yytext);
    printf("- > Identifier\n");
}
"+"|"-"|"/"|"*"|">"|"<" {
    print_transition(yytext);
    printf("- > operator\n");
}
"("|")"|"{"|"}"|";"|"," {
    print_transition(yytext);
    printf("- > special symbol\n");
}
[ \t\n\r] {
    if(yytext[0] == '\n'){
        line_num++;
    }
}
. {
    print_transition(yytext);
    printf("- > Invalid character\n");
}

%%

int main(int argc,char *argv[]) {
    printf("%-10s %-20s %-15s\n","Line no","Lexeme","Token");
    if(argc>1){
        FILE *f =fopen(argv[1],"r");
        if(!f){
            perror("file open failed");
            return 1;
        }
        yyin=f;
    }
    yylex();
    return 0;
}
int yywrap(){
    return 1;
}