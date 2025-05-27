from flask import Flask, render_template, request
from exprlang.lexer import tokenize
from exprlang.parser import Parser
from exprlang.symbol_table import SymbolTable
from exprlang.evaluator import evaluate
from exprlang.codegen import generate_code
from exprlang.astviz import visualize_asts

app = Flask(__name__)
symbols = SymbolTable()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    code_lines = []
    expr = ''
    error = ''
    ast_svg = ''
    if request.method == 'POST':
        expr = request.form['expr'].strip()
        try:
            result_lines = []
            code_lines = []
            for line in expr.splitlines():
                if not line.strip():
                    continue
                tokens = tokenize(line)
                parser = Parser(tokens)
                ast = parser.parse()
                result_val = evaluate(ast, symbols)
                result_lines.append(f"{line.strip()} → {result_val}")
                _, code_out = generate_code(ast, [])
                code_lines.extend(code_out)
            result = "\n".join(result_lines)
            ast_svg = visualize_asts([ast])
        except Exception as e:
            error = str(e)
    symbol_snapshot = symbols.table.copy()
    return render_template('index.html', result=result, code=code_lines, expr=expr, error=error, symbols=symbol_snapshot, ast_svg=ast_svg)

if __name__ == '__main__':
    app.run(debug=True)
