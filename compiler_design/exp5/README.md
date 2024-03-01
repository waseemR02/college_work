# Predictive Parsing

## Instructions to compile
Compile the lex file with `flex`
```
lex parse_number.l
```
Compile the yacc file with `bison/yacc`
```
yacc -d parser.y
```
>The -d option creates the file y.tab.h, which contains the #define statements that associate the yacc-assigned integer token values with the user-defined token names. 

Finally compile the lexical analzer and parser with gcc
```
gcc lex.yy.c y.tab.c -w
```
