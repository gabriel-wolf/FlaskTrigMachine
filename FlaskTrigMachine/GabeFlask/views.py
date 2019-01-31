from __future__ import division
from datetime import datetime
from flask import render_template
from GabeFlask import app
from sympy import *
from sympy import sin, cos, tan, asin, atan, acos, Function, diff
from sympy import limit
from sympy.solvers import solve
from sympy import ImageSet, Lambda, pi, S, Dummy, pprint
from sympy import Point
from sympy.printing.latex import print_latex
from sympy.printing.dot import dotprint
import re
from sympy import Rel
from flask import request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from sympy import latex, Rational
from sympy.abc import tau
from sympy import latex, simplify
from sympy.abc import x, y, mu, r, tau
import codecs
n = Dummy('n')
import webbrowser

x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
x, y, z, a = symbols('x y z a')
n = Dummy('n')
init_printing(use_latex='mathjax')

f = Function('f')
from sympy.parsing.sympy_parser import parse_expr

initexpr = parse_expr("sin((11*pi*x)/(6))")
exprangle = 40

maineq = "$\sin{\left (3 x / 4 \pi \\right )}$"
x1 = "$8 n \pi^{2} / 3 + 2 \pi^{2} / 3$"
x2 = "$8 n \pi^{2} / 3 + 2 \pi^{2}$"
domainx = "$\left [ 2 \pi^{2} / 3, \quad 2 \pi^{2}\\right ]$"
periocity = "$8 \pi^{2} / 3$"
quad = "1"
inversed = "$\left [ 4 \pi \left(- \{asin}{\left (x \right )} + \pi\right) / 3, \quad 4 \pi \{asin}{\left (x \right )} / 3\right ]$"
simplified = "$\sin{\left (3 x / 4 \pi \\right )}$"


def runallWithExpr(getexpr):
    print("in run all")
    print(getexpr)
    #uinput = input("Enter Equation: ")
    #if (uinput == ""):
    #    None
    #else:
    #    expr = parse_expr(uinput)

    from sympy import latex, Rational
    from sympy.abc import tau
    from sympy import latex, simplify
    from sympy.abc import x, y, mu, r, tau
    import codecs
    n = Dummy('n')

    expr = parse_expr(getexpr)

    def inversesolve(func):
        newxexpr = func.replace("x","y")
        inverseexpr = (Eq(x,newxexpr))
        return solve(inverseexpr,y)


    def simplifyme(expr):
        simplifyexpr = simplify(expr)
        return(simplifyexpr)


    maineq = latex(expr, mode='inline')
    try:
        x1 = latex(((solve((diff(expr, x)), x)[0]) + ((expr.period())*n)), mode='inline')
        pass
    except:
        x1 = "None"
        pass
    try:
        x2 = latex(((solve((diff(expr, x)), x)[1]) + ((expr.period())*n)), mode='inline')
        pass
    except:
	    x2 = "None"
	    pass
    domainx = latex(solve(diff(expr, x),x), mode='inline')
    try:
        periocity = latex((expr).period(), mode='inline')
        pass
    except:
        periocity = latex(periodicity(expr, x), mode='inline')
        pass

    p = Point(cos(exprangle), sin(exprangle))
    if ((cos(exprangle)) > 0) and ((sin(exprangle)) > 0):
        quad = 1
    elif ((cos(exprangle)) < 0) and ((sin(exprangle)) > 0):
        quad = 2
    elif ((cos(exprangle)) < 0) and ((sin(exprangle)) < 0):
        quad = 3
    elif ((cos(exprangle)) > 0) and ((sin(exprangle)) < 0):
        quad = 4 
    else:
       quad = "None"
    print(inversesolve(expr))
    inversed = latex(inversesolve(expr), mode='inline')
    print(inversed)
    simplified = latex(simplifyme(expr), mode='inline')
    
    return([maineq, x1, x2, domainx, periocity, quad, inversed, simplified])
   

#webbrowser.open('localhost:5555/')

@app.route('/')
@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        print("exprform")
        runallarray = runallWithExpr(request.form.get('exprform'))

        return render_template(
            "trigview-demo.html",
            title = "Trigview Demo Result",
            message = "Hello, Trig!",
		    maineq = runallarray[0].replace("\r","\\r"),
		    x1 = runallarray[1].replace("\r","\\r"),
		    x2 = runallarray[2].replace("\r","\\r"),
		    domainx = runallarray[3].replace("\r","\\r"),
		    periocity = runallarray[4].replace("\r","\\r"),
		    quad = runallarray[5],
		    inverse = runallarray[6].replace("\r","\\r"),
		    simplify = runallarray[7].replace("\r","\\r"))

    return render_template(
        "trigview-demo.html",
        title = "Trigview Demo",
        message = "Hello, Trig!",
		maineq = "$\sin{\left (3 x / 4 \pi \\right )}$",
		x1 = "$8 n \pi^{2} / 3 + 2 \pi^{2} / 3$",
		x2 = "$8 n \pi^{2} / 3 + 2 \pi^{2}$",
		domainx = "$\left [ 2 \pi^{2} / 3, \quad 2 \pi^{2}\\right ]$",
		periocity = "$8 \pi^{2} / 3$",
		quad = "1",
		inverse = "$\left [ 4 \pi \left(- \operatorname{asin}{\left (x \\right )} + \pi\\right) / 3, \quad 4 \pi \operatorname{asin}{\left (x \\right )} / 3\\right ]$",
		simplify = "$\sin{\left (3 x / 4 \pi \\right )}$")



@app.route('/trig')
def trig():
	return render_template(
        "trigview-demo.html",
        title = "Trigview Demo",
        message = "Hello, Trig!",
		maineq = maineq.replace("\r","\\r"),
		x1 = x1.replace("\r","\\r"),
		x2 = x2.replace("\r","\\r"),
		domainx = domainx.replace("\r","\\r"),
		periocity = periocity.replace("\r","\\r"),
		quad = quad,
		inverse = inversed.replace("\r","\\r"),
		simplify = simplified.replace("\r","\\r"))


@app.route('/trigtemp')
def trigtemp():
	return render_template(
        "trigview-demo.html",
        title = "Trigview Demo",
        message = "Hello, Trig!",
		maineq = "$\sin{\left (3 x / 4 \pi \\right )}$",
		x1 = "$8 n \pi^{2} / 3 + 2 \pi^{2} / 3$",
		x2 = "$8 n \pi^{2} / 3 + 2 \pi^{2}$",
		domainx = "$\left [ 2 \pi^{2} / 3, \quad 2 \pi^{2}\\right ]$",
		periocity = "$8 \pi^{2} / 3$",
		quad = "1",
		inverse = "$\left [ 4 \pi \left(- \operatorname{asin}{\left (x \\right )} + \pi\\right) / 3, \quad 4 \pi \operatorname{asin}{\left (x \\right )} / 3\\right ]$",
		simplify = "$\sin{\left (3 x / 4 \pi \\right )}$")


@app.route('/home')
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    return render_template(
        "index.html",
        title = "Hello Flask",
        message = "Hello, Flask!",
        content = " on " + formatted_now)


@app.route('/getmethod/<jsdata>')
def get_javascript_data(jsdata):
    print("get")
    print("get method")
    print(str(jsdata))
    return jsdata


@app.route('/api', methods = ['POST'])
def api():
  # Do something useful here...
  print(str(request.values.get('input', '')))
  runallWithExpr(str(request.values.get('input', '')))
  return request.values.get('input', '')

#get_post_javascript_data()
#runallWithExpr(initexpr)
