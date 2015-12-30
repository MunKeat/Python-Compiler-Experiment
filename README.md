### Python-Compiler-Experiment
This repository aims to document the making of a compiler, based on the reading of the following sources (thus far):
### Reference
#### General
* Compilers: Principles, Techniques, and Tools (otherwise referred as "The Dragon Book") 
  *by A. Aho, J. Ullman, M.S. Lam, and R. Sethi*
* Let's Build A Compiler! 
  *by Jack W. Crenshaw*
* [A Simple Interpreter From Scratch in Python](http://jayconrod.com/posts/37/a-simple-interpreter-from-scratch-in-python-part-1, "by Jay Conrod")

#### Lexer
* [Github: Lexical Python](https://github.com/x2adrew/lexical_python, "by x2adrew")

#### Syntax/Semantic Analyser
* [Stackexchange: How exactly is an abstract syntax tree created](http://programmers.stackexchange.com/questions/254074/how-exactly-is-an-abstract-syntax-tree-created)

***

### Structure
The structure of this toy compiler thus far will take on the following form:
* Lexical Analyser
* Syntax/Semantic Analyser (i.e. Parser)
* Intermediate Code Generator

***

### Language(s)
The compiler aims to convert a simplified version of C to MIPS assembly code (tentative)
