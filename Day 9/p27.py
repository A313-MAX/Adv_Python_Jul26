# Understanding Program Execution in Python
# Program runs line by line, executing instructions in sequence

# Python does not execute src code line-by-line directly.
# Instead compile it into an intermediate format called Bytecode, which is then 
# Run by Virtual Machine

# 1. Complilation Stage : src code to bytecode
    # >> Lexical analysis : break down text based src code into small chunks called as tokens.

    # >> Parsing : Tokens are structured into a hierrachial tree callde
    # Abstract Syntax Tree (AST)
    # >> Bytecode generated
    # >> Caching (__pycache__): .pyc file

# 2. Interpretation Stage : (Python Virtual Machine)
# Bytecode is passed to core runtime engine : PVM

# 3. Execution Architecture 
# Execution Frames : Stack created for function call 
# Memory & GC : Heap memory , Garbage Collector.
# GIL : Global Interpreter Lock : only one thread exectes bytecode at a time