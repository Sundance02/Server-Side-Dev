from django.shortcuts import render, redirect
from django.db.models import *
from django.db.models.functions import *
from django.db.models.lookups import *
from .models import *
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from employee.forms import *
from django.views import View

def employee(request):
    count_em = Employee.objects.count()
    all_em = Employee.objects.all().order_by('-hire_date')
    context = {"Employees": all_em, "count": count_em}
    return render(request, "employee.html", context)

def position(request):
    position_info = Position.objects.all().values('name', 'id').annotate(count=Count('employee__id')).order_by('id')
    context = {"positions": position_info}
    return render(request, "position.html", context)

def project(request):
    project = Project.objects.all()
    context = {"projects": project}
    return render(request, "project.html", context)

def project_delete(request, project_id):
    del_pro = Project.objects.get(id=project_id)
    del_pro.delete()
    return JsonResponse({'del':'delete'}, status=200)

# def project_detail(request, project_id):
#     project = Project.objects.get(pk=project_id)
#     start = project.start_date.strftime("%Y-%m-%d")
#     end = project.due_date.strftime("%Y-%m-%d")
#     context = {"project":project, 'start':start, "end":end}
#     return render(request, "project_detail.html", context)

def project_detail_manage(request, employee_id, project_id):
    if(request.method == "PUT"):
        employee = Employee.objects.get(pk=employee_id)
        project_id = Project.objects.get(pk=project_id)
        project_id.staff.add(employee)
    elif(request.method == "DELETE"):
        employee = Employee.objects.get(pk=employee_id)
        project_id = Project.objects.get(pk=project_id)
        project_id.staff.remove(employee)
    return JsonResponse({'manage':'manage'}, status=200)



#form
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["first_name"])

            Employee.objects.create(
                    first_name = form.cleaned_data["first_name"],
                    last_name = form.cleaned_data["last_name"],
                    gender = form.cleaned_data["gender"],
                    birth_date = form.cleaned_data["birth_date"],
                    hire_date = form.cleaned_data["hire_date"],
                    salary = form.cleaned_data["salary"],
                    position = form.cleaned_data["position"]
            )
            return HttpResponseRedirect('/employee')
    else:
        form = EmployeeForm()

    return render(request, "employee_form.html", {"form": form})



class add_project(View):

    def get(self, request):
        form = ProjectForm()
        return render(request, 'project_form.html', {'form':form})
    
    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employee/project')
        return render(request, 'project_form.html', {'form':form})

class project_detail(View):
    def get(self, request, project_id):
        project = Project.objects.get(pk=project_id)
        form = ProjectDetailForm(initial={"name":project.name, "description":project.description, "manager":project.manager, 'due_date':project.due_date, 'start_date':project.start_date})
        return render(request, 'project_detail.html', {'form':form, 'project':project})
    
    def post(self, request, project_id):
        project = Project.objects.get(pk=project_id)
        form = ProjectDetailForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employee/project')
        
        return render(request, 'project_detail.html', {'form':form})