# PPL-MiniGo
Go, also known as Golang, is a statically typed, compiled programming language developed
by Google. It was created in 2007 by Robert Griesemer, Rob Pike, and Ken Thompson, and
was officially released to the public in 2009. The language was designed to address the short-
comings of other programming languages in terms of performance, scalability, and ease of use,
particularly for large software systems. Go emphasizes simplicity, efficiency, and concurrency,
making it ideal for modern, distributed applications.

One of the key reasons for Go’s creation was to improve the development process at Google.
The team wanted a language that would be faster to compile than C++ and more efficient
in terms of concurrency management than languages like Java. Go introduces features such
as goroutines (lightweight threads) and channels, which facilitate concurrent programming and
make it highly effective for handling multiple tasks simultaneously.

Go has become increasingly popular, particularly in cloud computing, microservices, and DevOps. Its growing community and extensive standard library have contributed to its widespread
adoption. Some of the most notable projects developed using Go include Docker, Kubernetes,
Terraform, and the cloud infrastructure behind companies like Uber, Dropbox, and Netflix.
The language’s strong performance, ease of use, and scalability have made it a top choice for
building large, reliable systems that require high concurrency and low-latency processing.

MiniGo is a simplified version of the Go programming language. It retains the core concepts
of Go, such as basic data types, structs, and interfaces, but removes more complex features like
goroutines, channels, and the extensive standard library
# Assignment1 - Lexer and Parser
- The lexer (or lexical analyzer) takes raw source code as input and converts it into a sequence of tokens. Each token represents a meaningful unit, such as a keyword, identifier, number, or symbol.
- The parser takes the sequence of tokens from the lexer and organizes them into a syntax tree (often an Abstract Syntax Tree or AST) based on the grammar of the language.
# Assignment2 - AST Generation
A parser will check if the input is grammatically correct or not. If the input is grammatically wrong, an error message is released. In the case the input is grammatically correct, an intermediate code is generated - AST
# Assignment3 - Static Checker
A static checker plays an important role in modern compilers. It checks in the compiling time if a program conforms to the semantic constraints according to the language specification
# Script
- python3 run.py gen
- python3 run.py test LexerSuite
- python3 run.py test ParserSuite
- python3 run.py test CheckSuite
