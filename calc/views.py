from django.shortcuts import render

def landing(request):
    return render(request, 'index.html')

def calculator(request):
    result = None
    error = None
    a = request.POST.get('a')
    b = request.POST.get('b')
    op = request.POST.get('op', '+')

    if request.method == 'POST':
        try:
            x = float(a or 0)
            y = float(b or 0)
            if op == '+':
                result = x + y
            elif op == '-':
                result = x - y
            elif op == '*':
                result = x * y
            elif op == '/':
                if y == 0:
                    error = "Cannot divide by zero"
                else:
                    result = x / y
            else:
                error = "Unknown operation"
        except ValueError:
            error = "Please enter valid numbers"

    return render(request, 'home.html', {'a': a or '', 'b': b or '', 'op': op, 'result': result, 'error': error})

def about(request):
    return render(request, 'about.html')