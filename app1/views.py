from django.shortcuts import render
from app1 import forms
from app1.models import Category, JobPost, Application, Location, JobTitle
# Create your views here.


def index(request):
    jb = JobTitle.objects.values()
    jb_lst = [entry for entry in jb]
    non_clinician = []
    clinician = []
    
    for i in range(len(jb_lst)):
        cat_id = jb_lst[i]['category_id']
        c = Category.objects.filter(id=cat_id).values()
        print(c)
        for j in c:
            if j["category_name"] == "Clinician":
                clinician.append([jb_lst[i]['title'],cat_id])
            else:
                non_clinician.append([jb_lst[i]['title'],cat_id])
                
    print(non_clinician)
    print(clinician)
    print(jb_lst)
    print(type(jb_lst))
    
    return render(request, 'app1/index.html', {'non_clinician':non_clinician, 'clinician':clinician} )

def location(request, title_id):
    l = Location.objects.filter(job_title=title_id).values()
    print(title_id)
    print(l)
    return render(request, 'app1/location.html', {'location' : l, 'title_id': title_id})

def job_search(request, title_id, location_id):
    #j = JobPost.objects.filter(job_title_id=2).values
    j = []
    jb = JobPost.objects.values()
    print(jb)
    for i in jb:
        #if ((i.job_title_id == title_id) and (i.location_id == location_id)):
        #    j.append(i)
        print(i)
    l = Location.objects.filter(id=location_id).values()
    t = JobTitle.objects.filter(id=title_id).values()
    print(title_id)
    print(location_id)
    print(j)
    print(jb)
    print(t)
    print(l)
    return render(request, 'app1/search.html', {'location' : l,'job' : j, 'job_title' : t})
def application_form(request) :
    form = forms.ApplicationForm()

    if request.method == 'POST':
        form = forms.ApplicationForm(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("CONTACT NUMBER: " + form.cleaned_data['mobile_no'])
            applications = Application()
            applications.current_designation = form.cleaned_data['current_designation']
            applications.current_location = form.cleaned_data['current_location']
            applications.preferred_designation = form.cleaned_data['preferred_designation']
            applications.preferred_location = form.cleaned_data['preferred_location']
            applications.current_salary = form.cleaned_data['current_salary']
            applications.expected_salary = form.cleaned_data['expected_salary']
            applications.can_join = form.cleaned_data['can_join']
            applications.name = form.cleaned_data['name']
            applications.mobile_no = form.cleaned_data['mobile_no']
            applications.alternate_mobile = form.cleaned_data['alternate_mobile']
            applications.total_experience = form.cleaned_data['total_experience']
            applications.email = form.cleaned_data['email']
            applications.pg_name = form.cleaned_data['pg_name']
            applications.ug_name = form.cleaned_data['ug_name']
            applications.message = form.cleaned_data['message']
            applications.resume = form.cleaned_data['resume']
            applications.save()
        else:
            form = forms.FormName()
    return render(request, 'app1/application_form.html', {'form':form})