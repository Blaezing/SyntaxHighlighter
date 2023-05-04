import re

class Highlighter():
    def highlight_code(code):
        # Define regex's to match different tokens in Python code
        comments = re.compile(r'#.*|\'\'\'.*?\'\'\'|"""\s*.*?\s*"""', re.DOTALL)
        strings = re.compile(r'(\'[^\']*\'|\"[^\"]*\")')
        keywords = re.compile(r'\b(if|else|elif|while|for|in|and|or|not|try|except|finally|raise|assert|with|as|from|import|global|nonlocal|lambda|def|class|return|yield|async|await)\b')
        builtins = re.compile(r'\b(print|len|range|input|open|abs|bin|bool|chr|complex|dict|float|hex|int|list|oct|pow|set|slice|str|tuple|type|zip|super|setattr|getattr|delattr|issubclass|isinstance)\b')
        variables = re.compile(r'\b[a-zA-Z]\w*\b')
        numbers = re.compile(r'\b(\d+)\b')






        # Define the HTML tags to use for different types of tokens
        tags = {
            keywords: 'keyword',
            builtins: 'builtin',
            strings: 'string',
            comments: 'comment',
            variables: 'variable',
            numbers: 'number',
        }

        # Tokenize the code and highlight with HTML tags
        html = ""
        for line in code.splitlines():
            line_html = ""
            pos = 0
            for match in re.finditer(r'\b|\s|$', line):
                token = line[pos:match.start()].strip()
                if token:
                    tag = None
                    for pattern, tag_name in tags.items():
                        if pattern.match(token):
                            tag = tag_name
                            break
                    if tag:
                        line_html += f'<span class="{tag}">{token}</span>'
                    else:
                        line_html += token
                line_html += line[match.start():match.end()]
                pos = match.end()
            html += f'<div>{line_html}</div>'

        # Wrap the html highlighted code and return it
        return f'''
        <html>
            <head>
                <link rel="stylesheet" type="text/css" href="style.css">
            </head>
            <body>
                <div class="highlight"><pre>{html}</pre></div>
            </body>
        </html>
        '''
