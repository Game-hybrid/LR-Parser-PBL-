import re

TOKEN_REGEX = [
    (r'[ \t]+',              None),
    (r'#[^\n]*',             None),
    (r'\n',                  'NEWLINE'),
    (r'[0-9]+(?:\.[0-9]+)?', 'NUMBER'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*','IDENT'),
    (r'\+',                 'PLUS'),
    (r'-',                   'MINUS'),
    (r'\*',                 'MUL'),
    (r'/',                   'DIV'),
    (r'=',                   'ASSIGN'),
    (r'\(',                 'LPAREN'),
    (r'\)',                 'RPAREN'),
]

def tokenize(code):
    pos = 0
    tokens = []
    while pos < len(code):
        match = None
        for token_expr in TOKEN_REGEX:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(code, pos)
            if match:
                text = match.group(0)
                if tag:
                    tokens.append((tag, text))
                break
        if not match:
            raise SyntaxError(f'Illegal character: {code[pos]}')
        else:
            pos = match.end(0)
    return tokens
