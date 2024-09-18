
""" 
Copyright (c) 2018 Stark Bank S.A.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files 
(the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, 
publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do 
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION 
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Original Repository: https://github.com/starkbank/febraban-python
"""

from .tipos_dados import *

class Row:

    @classmethod
    def setStructs(cls, structs, content):
        for (start, end, len, type, value) in structs:
            replacement = cls.__formatted(
                string=str(value),
                charactersType=type,
                numberOfCharacters=len,
                defaultCharacter={numeric: "0", alphaNumeric: " "}[type]
            )
            content = content[:start] + replacement + content[start+len:]
        return content

    @classmethod
    def __formatted(cls, string, charactersType, numberOfCharacters, defaultCharacter=" "):
        """
            This method fix the received String and a default complement according the alignment
            and cut the string if it' bigger than number of characters

            Args:
                string:             String to be completed
                charactersType:     Can be .numeric or .alphaNumeric
                numberOfCharacters: Integer that represents the max string len
                defaultCharacter:   Single string with default character to be completed if string is short
            Returns:
                String formatted
        """
        if type(string) != str:              return defaultCharacter * numberOfCharacters
        if len(string) > numberOfCharacters: return string[:numberOfCharacters]
        if charactersType == numeric:        return defaultCharacter * (numberOfCharacters - len(string)) + string
        if charactersType == alphaNumeric:   return string + defaultCharacter * (numberOfCharacters - len(string))