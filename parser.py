class ASTNode:
    def __init__(self, type_, value=None, left=None, right=None):
        self.type = type_
        self.value = value
        self.left = left
        self.right = right

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else (None, None)

    def match(self, expected):
        token = self.peek()
        if token[0] == expected:
            self.pos += 1
            return token[1]
        raise SyntaxError(f"Expected {expected} but got {token[0]}")

    def parse(self):
        if not self.tokens:
            raise SyntaxError("No tokens to parse.")
        result = self.assignment()
        if result is None:
            raise SyntaxError("Parsing failed: AST is None.")
        return result

    def assignment(self):
        start_pos = self.pos

        if self.peek()[0] == 'IDENT':
            ident = self.match('IDENT')
            if self.peek()[0] == 'ASSIGN':
                self.match('ASSIGN')
                expr = self.expr()
                return ASTNode('ASSIGN', None, ASTNode('IDENT', ident), expr)
            else:
                self.pos = start_pos

        return self.expr()





    def expr(self):
        node = self.term()
        while self.peek()[0] in ('PLUS', 'MINUS'):
            op_token = self.peek()[0]
            self.match(op_token)
            right = self.term()
            node = ASTNode(op_token, None, node, right)
        return node

    def term(self):
        node = self.factor()
        while self.peek()[0] in ('MUL', 'DIV'):
            op_token = self.peek()[0]
            self.match(op_token)
            right = self.factor()
            node = ASTNode(op_token, None, node, right)
        return node


    def factor(self):
        token = self.peek()
        if token[0] == 'NUMBER':
            self.match('NUMBER')
            return ASTNode('NUMBER', token[1])
        elif token[0] == 'IDENT':
            self.match('IDENT')
            return ASTNode('IDENT', token[1])
        elif token[0] == 'LPAREN':
            self.match('LPAREN')
            node = self.expr()
            self.match('RPAREN')
            return node
        else:
            raise SyntaxError(f"Unexpected token: {token}")
