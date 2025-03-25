%{
#include <stdio.h>
#include <string.h>

void print_transition(char *text){
    printf("Transition sequence: ");
    for(int i=0;i<strlen(text);i++){
        printf("%c",text[i]);
        if(i!=strlen(text)-1){
            printf("-> ");
        }
    }
}
%}

%%
"if"|"else"|"while"|"continue"|"break" {
    print_transition(yytext);
    printf("- > keyword\n");
}
[0-9]+ {
    print_transition(yytext);
    printf("- > integer\n");
}
[a-zA-Z_][a-zA-Z_0-9]+ {
    print_transition(yytext);
    printf("- > Identifier\n");
}
"+"|"-"|"*"|"/" {
    print_transition(yytext);
    printf("- > operator\n");
}
"("|")"|"{"|"}"|";" {
    print_transition(yytext);
    printf("- > Special character\n");
}
[ \t\n]+ {}

. {
    printf("invalid character: %s\n",yytext);
}

%%
int main(int argc,char *argv[]){
    if(argc>1){
        FILE *f=fopen(argv[1],"r");
        if(!f){
            perror("error in opening the file");
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