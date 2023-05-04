# SyntaxHighlighter

##This Syntax Highlighter is to be used with python only, I did not error check or create a robust pipeline that will spit out clean feedback

##Known Bugs
* Syntax for variables overwhelms Comments and Strings (I've tried every solution in the book, I believe the problem lies with the re.compile but I have tried fixing it many different times)
* Had a fix for comments but only the # showed up in the correct color, other text behind it was noted as either variable or nothing. 

#How to Use

*the only import you will need outside of this fileset is re*

1.) In the example.py file is a place where you can put your code, to start, there is already test code that illustrates the highlighter
2.) All files have to be in the same directory (or specify the filepath)
3.) When you execute, run the 'example.py' file once it is done running it will output an HTML webpage
4.) If the HTML webpage doesn't open automatically, the HTML page will be placed in the same directory as your code is in. (this code)

#That's it, enjoy!
