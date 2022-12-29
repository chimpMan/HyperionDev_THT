## Marked Grade
1. Completeness: 2/4

2. Efficiency: 3/4

3. Style: 4/4

4. Documentation: 4/4

## Reasoning

**COMPLETNESS 2/4**
    Due to syntax errors in line 1, 26 and 30, the compiler cannot compile the code to its entirity and must stop at each error for it to be corrected so that it may continue to the next line.
    If these errors are corrected the code does infact, run smoothly.

**EFFICIENCY 3/4**
    The code cannot be run without errors as it is since:
        1. The function in line 18 does not return a valid value.
        2. The class name has not been properly named as per naming conventions.
        3. Use of the '<T>' to define an arbitrary variable conflicts with the duplicate variable in line 30, where the generic variable maxValue conflicts with the integer variable of the same name as the two data types are incompatible.

**STYLE 2/4**
    The code is well space and different blocks of code are seperately spaced and easy to identify.
    However, the student may employ better use of whitespace and not use whitespaces carelessly.

    There is also an excess of characters in line 11 and line 25 which exceeds the 72 character limit.

    Naming conventions of Java have not been adhered to in line 1 where classes must have Sentence case format,
    line 10 and 18 utilise underscores and lowercase instead of the recommended camelCase and line 26 returns a function
    name not previously defined due to mixing up of the naming conventions.

**DCUMENTATION 3/4**
    Good use of comments througout the code, line 38-40 however, have comments with-in the actual code that could be placed 
    at the beggining of the block for a neater combination of block of comments and code.

## Positive Aspects
1. A good understanding of the concept of recursion.
2. Comments are well utilised in the majority of the code. They are short and to the point

With correction of the few mistakes found, the code runs quit well and the student will be set on the right track.

## Areas to improve on
1. Correct usage of whitespaces: Whitespaces are used only when neccessary according to the Java specifications.
2. Line length must not exceed 72 characters: Move to the next line when a phrase becomes too long. (Maintain correct syntax while moving to a new line.)
3. Correct placement of comments: Its highly recommended to place comments at the forefront of a block of code. Inline comments can be implemented where necessary.
4. Study more about the data type '<T>' and its correct usage. Otherwise, a simple use of basic datatypes can be more useful than complex types in most cases.(I have provided a link to guide with the use of the generic type '<T>' variable. )
5. Use of meaninful variable names can be implemented in line 28 instead of naming a user defined function with a generic name as was done.

https://www.geeksforgeeks.org/generics-in-java/
