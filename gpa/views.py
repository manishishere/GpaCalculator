from django.shortcuts import render, redirect,get_object_or_404
from gpa.forms import MenuCreateForm,RegisterForm
from gpa.models import Details
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/gpa/finalgpa')
    else:
        form = AuthenticationForm()
        
    return render(request,'login.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/gpa/login')
    else:
        form = RegisterForm()          



    return render(request,'register.html',{'form': form})
@login_required(login_url='/gpa/login/')
def gpaCalculate(request):

    if request.method == 'POST':
        data = request.POST
        db_data = MenuCreateForm(data)
        if db_data.is_valid():

            db_data.save()
            return redirect('finalGpa')
        else:   
            return redirect('/calculate')
        

    context = {'form':MenuCreateForm()}
    return render (request, 'calculate.html',context)

@login_required(login_url='/gpa/login/')
def finalgpa(request):
    GRADE_POINTS = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'D': 1.0,
    'F': 0.0,
}




    final_details = Details.objects.all()
    total_points = 0
    total_credits = 0

    for detail in final_details:
        grade = detail.s_grade
        credit = detail.s_credit

        point = GRADE_POINTS.get(grade, 0)

        #If grade exists → return value
        # If not → return 0 (safe, no crash)

        total_points += point * credit
        total_credits += credit

    if total_credits == 0:
        gpa = 0
    else:
        gpa = round(total_points / total_credits, 2)






    


        
    context = {
        'final_details' : final_details,
        'gpa':gpa
        }

    return render(request, 'gpa.html',context)

@login_required(login_url='/gpa/login/')
def update(request,id):
    details = get_object_or_404(Details,id = id)
    if request.method == 'POST':
        form = MenuCreateForm(request.POST, instance=details)
        if form.is_valid():
            form.save()
            return redirect('finalGpa')
    else:
        form = MenuCreateForm(instance=details)
    




    return render(request,'update.html',{'form': form})

@login_required(login_url='/gpa/login/')

def delete(request, id):
    details = Details.objects.filter(id = id)
    details.delete()
    return redirect('finalGpa')
