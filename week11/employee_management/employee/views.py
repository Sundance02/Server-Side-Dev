from django.shortcuts import render
from django.db.models import *
from django.db.models.functions import *
from django.db.models.lookups import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from employee.forms import *
from django.views import View
from django.db import transaction
from company.models import *
from employee.models import *

def employee(request):
    count_em = Employee.objects.count()
    all_em = Employee.objects.all().order_by('-hire_date')
    for employee in all_em:
        employee.position_id = Position.objects.using('db2').get(pk=employee.position_id)
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
class add_employee(View):
    def get(self, request):
        form = EmployeeForm()
        return render(request, 'employee_form.html', {'form':form})
    @transaction.atomic
    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            position = form.cleaned_data['position'].id
            form.instance.position_id = position

            emp = form.save()

            EmployeeAddress.objects.create(employee = emp, 
                                           location = form.cleaned_data["location"],
                                           district = form.cleaned_data["district"],
                                           province = form.cleaned_data["province"],
                                           postal_code =form.cleaned_data["postal_code"]
                                           )
            return HttpResponseRedirect('/employee')
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