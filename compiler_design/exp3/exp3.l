%{
#include <stdio.h>
%}

KW integer | read | display | if | else | then | while | for | to | step 

%%
[KW]          {printf("Keyword: %s", yytext); }
"<"          { printf("Relational Operator: <\n"); }
"<="         { printf("Relational Operator: <=\n"); }
">"          { printf("Relational Operator: >\n"); }
">="         { printf("Relational Operator: >=\n"); }
"=="         { printf("Relational Operator: ==\n"); }
"#"          { printf("Relational Operator: #\n"); }
"+"          { printf("Arithmetic Operator: +\n"); }
"-"          { printf("Arithmetic Operator: -\n"); }
"*"          { printf("Arithmetic Operator: *\n"); }
"/"          { printf("Arithmetic Operator: /\n"); }
"++"         { printf("Increment Operator: ++\n"); }
"--"         { printf("Decrement Operator: --\n"); }
"="          { printf("Assignment Operator: =\n"); }
"("          { printf("Special Symbol: (\n"); }
")"          { printf("Special Symbol: )\n"); }
"{"          { printf("Special Symbol: {\n"); }
"}"          { printf("Special Symbol: }\n"); }
","          { printf("Special Symbol: ,\n"); }
";"          { printf("Special Symbol: ;\n"); }
[a-zA-Z_][a-zA-Z0-9_]* { printf("Identifier: %s\n", yytext); }
[0-9]+       { printf("Number: %s\n", yytext); }
[ \t\n]      ; /* Ignore whitespace */
.            ; /* Ignore other symbols */
%%

int yywrap(){}

int main(int argc, char *argv[]) {
    extern FILE *yyin;
    yyin = fopen(argv[1], "r");
    yylex();
    return 0;
}
