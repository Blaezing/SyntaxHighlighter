from Highlighter import Highlighter

code = '''
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

"Printing fib sequence"
print("Fibonacci sequence:")
for i in range(10):
    print(len(fibonacci(i)))
'''

html = f'''
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="styles.css">
    </head>
    <body>
        {Highlighter.highlight_code(code)}
    </body>
</html>
'''

with open('output.html', 'w') as f:
    f.write(html)
