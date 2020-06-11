# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def to_add():
    """add a and b params"""

    a = int(request.args["a"])
    b = int(request.args["b"])
    result_add = add(a, b)
    # DO WE ALWAYS HAVE TO STRING THE RESULTS???
    return str(result_add)


@app.route("/sub")
def to_sub():
    """subtract a and b params"""

    a = int(request.args["a"])
    b = int(request.args["b"])
    result_sub = sub(a, b)
    # DO WE ALWAYS HAVE TO STRING THE RESULTS???
    return str(result_sub)


@app.route("/mult")
def to_mult():
    """multipy a and b params"""

    a = int(request.args["a"])
    b = int(request.args["b"])
    result_mult = mult(a, b)
    # DO WE ALWAYS HAVE TO STRING THE RESULTS???
    return str(result_mult)


@app.route("/div")
def to_div():
    """divide a and b params"""

    a = int(request.args["a"])
    b = int(request.args["b"])
    result_div = div(a, b)
    # DO WE ALWAYS HAVE TO STRING THE RESULTS???
    return str(result_div)


@app.route("/math/<operator>")
def all_in_one(operator):
    dict_funcs = {"add": to_add(), "sub": to_sub(),
                  "mult": to_mult(), "div": to_div()}
    return dict_funcs[operator]


'''
### PART TWO from Springboard

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)
'''
