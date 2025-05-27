temp_counter = 0

def new_temp():
    global temp_counter
    temp = f"t{temp_counter}"
    temp_counter += 1
    return temp

def generate_code(node, code=None):
    if code is None:
        code = []

    if node is None:
        raise Exception("Cannot generate code from empty node.")

    if node.type == 'NUMBER':
        temp = new_temp()
        code.append(f"{temp} = {node.value}")
        return temp, code

    elif node.type == 'IDENT':
        return node.value, code

    elif node.type == 'ASSIGN':
        right_temp, code = generate_code(node.right, code)
        code.append(f"{node.value} = {right_temp}")
        return node.value, code

    elif node.type in ('PLUS', 'MINUS', 'MUL', 'DIV'):
        left_temp, code = generate_code(node.left, code)
        right_temp, code = generate_code(node.right, code)
        temp = new_temp()
        op = {'PLUS': '+', 'MINUS': '-', 'MUL': '*', 'DIV': '/'}[node.type]
        code.append(f"{temp} = {left_temp} {op} {right_temp}")
        return temp, code

    else:
        raise Exception(f"Unknown node type in codegen: {node.type}")
