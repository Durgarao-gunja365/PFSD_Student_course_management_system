from django.db.models import Q
from django.shortcuts import render,redirect

from adminapp.models import faculty,FacultyCourseMapping,Course

from .forms import AddCourseContentForm
from .models import coursecontent
from django.conf import settings


# Create your views here.
def facultyhome(request):
    fname = request.session['fname']
    return render(request,'facultyhome.html',{'facultyname':fname})


def checkfacultylogin(request):
    facultyname = request.POST.get('uname')
    facultypwd = request.POST.get('pwd')

    # Ensure facultyid is a number
    if not facultyname.isdigit():
        msg = 'Invalid Faculty ID or Password'
        return render(request, 'facultylogin.html', {'msg': msg})

    flag = faculty.objects.filter(Q(facultyid=facultyname) & Q(password=facultypwd)).exists()

    if flag:
        print("Login successful")
        request.session['fname'] = facultyname
        return render(request, 'facultyhome.html', {'facultyname': facultyname})
    else:
        msg = 'Username or Password is Wrong'
        return render(request, 'facultylogin.html', {'msg': msg})

def facultycourse(request):
    fname = request.session['fname']
    mappingcourse=FacultyCourseMapping.objects.all()
    fmcourses=[]
    for Course in mappingcourse:
        if(Course.faculty.facultyid==int(fname)):
            fmcourses.append(Course)

    dir(fmcourses)
    count=len(fmcourses)
    return render(request, 'facultycourse.html', {'facultyname': fname,'count':count,'fmcourses':fmcourses})

def facultyupload(request):
    fname = request.session['fname']
    if request.method == 'POST':
        form = AddCourseContentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg="content uploaded sucessfully"
            return render(request, 'facultyupload.html', {'facultyname': fname, 'msg':msg})

    else:
        form = AddCourseContentForm()


    return render(request, 'facultyupload.html', {'facultyname': fname,'form': form})

def facultychangepassword(request):
    fname = request.session['fname']
    return render(request,'facultychangepassword.html',{'facultyname':fname})
def facultyupdatepwd(request):
    fname = request.session['fname']
    opwd=request.POST['opwd']
    npwd=request.POST['npwd']
    flag=faculty.objects.filter(Q(facultyid=fname)& Q(password=opwd))
    if flag:
        print("password is correct")
        faculty.objects.filter(facultyid=fname).update(password=npwd)
        print("update successfully.....")
        msg="Password update successfully....."
    else:
        print("wrong password")
        msg = "Password update Failed....."
    return render(request,'changepassword.html',{'msg':msg,'admi12345nname':fname})

