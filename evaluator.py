def evaluate(node, symbols):
    if node.type == 'NUMBER':
        return float(node.value)

    elif node.type == 'IDENT':
        if node.value in symbols.table:
            return symbols.get(node.value)
        else:
            raise NameError(f"Variable '{node.value}' not defined")

    elif node.type == 'ASSIGN':
        value = evaluate(node.right, symbols)
        symbols.set(node.left.value, value)
        return value

    elif node.type == 'PLUS':
        return evaluate(node.left, symbols) + evaluate(node.right, symbols)

    elif node.type == 'MINUS':
        return evaluate(node.left, symbols) - evaluate(node.right, symbols)

    elif node.type == 'MUL':
        return evaluate(node.left, symbols) * evaluate(node.right, symbols)

    elif node.type == 'DIV':
        return evaluate(node.left, symbols) / evaluate(node.right, symbols)

    else:
        raise Exception(f"Unknown node type: {node.type}")
