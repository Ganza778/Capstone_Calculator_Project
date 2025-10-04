from django.shortcuts import render
from .forms import CalculatorForm
from .models import CalculationHistory

def calculator_view(request):
    result = None
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            expression = form.cleaned_data['expression']
            try:
                result = eval(expression)  # simple calculation
                # Save calculation to database
                CalculationHistory.objects.create(expression=expression, result=result)
            except Exception:
                result = "Error"
    else:
        form = CalculatorForm()

    # Make sure this return is INSIDE the function
    return render(request, 'calculator/calculator.html', {
        'form': form,
        'result': result,
        'history': CalculationHistory.objects.all().order_by('-created_at')[:10]
    })
