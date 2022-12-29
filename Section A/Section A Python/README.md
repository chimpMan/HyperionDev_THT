## Maked Grade
1. Completeness: 2/4

2. Efficiency: 2/4

3. Style: 2/4

4. Documentation: 0/4

## Reasoning

**COMPLETNESS 2/4**

    Due to syntax errors in line 2, and line 5 the interpreter will not move past line 2 
    to interpret the rest of the code, hence this error prevents the code from running. 
    Students should confirm that their submissions are free from such errors before a review.
   
    A simple dendentation of line two and addition of a parameter for the sorrted(x) function would be sufficient to have the code fully running.

**EFFICIENCY 2/4**

    The code cannot be run without errors as it is since:
        1. There is an indent on line 2 that does not coincide with the rest of the code.

**STYLE 2/4**

    Since python mainly uses spacing and indentation as opposed to brackets, the student 
    must learn more about correct indentation to avoid some simple errors when coding in python.
    All the lines of code have all been put together and on further inspection, 
    tab spaces were not utilised in indentation but the spacebar was used. 
    This can lead to deeply rooted syntax errors, especially when writting longer code.
    Genearally the code could be a little bit more spaced out as shown below.

    ```python
- `class Solution:
       def groupAnagrams(self, strs):
      result = {}
      for i in strs:
         x = "".join(sorted())
         if x in result:
            result[x].append(i)
         else:
            result[x] = [i]
      return list(result.values())
ob1 = Solution()
print(ob1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))`
```

**VS**

 ```python
- `class Solution:

    def group_anagrams(self,strs):
        result = {}

        for i in strs:
            x = "".join(sorted(i))

            if x in result:
                result[x].append(i)
            else:
                result[x] = [i]

        return list(result.values())

ob1 = Solution()
print(ob1.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))`
```

**DCUMENTATION 0/4**

    No comments were used in the code. Despite the code being short, 
    comments are still useful and are a staple for well written code.

## Positive Aspects
1. A good use of in-built functions such as join(sorted())

2. A good use of classes and an object to instanciate the class.

3. The code is highly modularised through a combination of classes, objects, user defined functions and in-built functions


## Areas to improve on
1. Implementation of comments is key to learn as comments serve as a guide to anyone reading your code which may be used in future to help someone understand a concept or to even revisit by the author. Comments also make the marker's work easier as they can easily identify the blocks of code and what they do through a short comment.

2. Naming conventions of python need to be follwed so as to have a consitency when it come to naming variables e.t.c... . In this case, kindly check on the python conventions for naming classes.

3. Use of correct indentation is a paramount tool in the development of any python code. More research can be conducted on how to properly use spacing and indentation.

4. The sorted function must have atleast 1 argument in order for it to function.

A little bit of refining of the code is all that is needed. For further studies, the student may look at the following resources:
    1. https://www.docs.python.org/3/library/functions.html#sorted
    2. https://www.peps.python.org/pep-0008/

