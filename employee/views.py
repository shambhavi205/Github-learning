from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee, Univercity
# Create your views here.


def employee_create_view(request):
    if request.method == "GET":
        form = EmployeeForm()
        empdetail = Employee.objects.all()
        unidetails = Univercity.objects.all()

        context = {
            'form': form,
            "empList": empdetail,
            'univercity':unidetails
        }
        return render(request, "employee_create.html", context)
    if request.method == "POST":

        form = EmployeeForm(request.POST or None)
        if form.is_valid():
            form.save()
            context = {
                'msg': 'submited',
                'form': EmployeeForm()
            }
        else:
            context = {
                'msg': 'Age is less than 18',
                'form': form
            }
        return render(request, "employee_create.html", context)


