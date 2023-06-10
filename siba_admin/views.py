from django.shortcuts import render, redirect
from siba_student.models import student_db
from .models import Courses, Assignments, Subjects, TimeTable
from .forms import Courses_forms, Assignments_form, subject_form
from siba_student.forms import student_form
import random

# imports for pdf
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View
# from weasyprint import HTML

# imports for django user authentication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm



# function for login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('student-report')  # Redirect to the desired page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# functions for students page
def student_report(request):
    data = student_db.objects.all()
    auto_increment = 1

    # increment count
    for item in data:
        item.auto_increment_number = auto_increment
        auto_increment += 1

    context = {
        'data': data,
    }
    return render(request, 'student-report.html', context)


# function for courses page
def course_form(request):
    # course form
    form = Courses_forms()

    # checking for post method and validation
    if request.method == "POST":
        form = Courses_forms(request.POST)
        if form.is_valid:
            form.save()
            return redirect('courses')
    else:
        form = Courses_forms()

    # list of courses from database 
    course_tb = Courses.objects.all()
    auto_increment = 1

    # increment count
    for i in course_tb:
        i.auto_increment_number = auto_increment
        auto_increment += 1

    context = {
        'course_tb': course_tb,
        'form': form,
    }
    return render(request, 'course-form.html', context)


# suject function
def subjects_view(request):
     # subject form
    form = subject_form()

    # checking for post method and validation
    if request.method == "POST":
        form = subject_form(request.POST)
        if form.is_valid:
            form.save()
            return redirect('subject')
    else:
        form = subject_form()

    # list of subjects from table 
    subject_tb = Subjects.objects.all()
    auto_increment = 1

    # increment count
    for i in subject_tb:
        i.auto_increment_number = auto_increment
        auto_increment += 1

    context = {
        'subject_tb': subject_tb,
        'form': form,
    }
    return render(request, 'subject-form.html', context)



# function for assignment page
def assiner(request):
    # tb
    data = Assignments.objects.all()
    subjects = Subjects.objects.all()

    # co = data.course.course_Id
    # sb = subjects.course_alloc.course_Id


    if request.method == 'POST':
        form = Assignments_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assign')  # Redirect to a success page after form submission
    else:
        form = Assignments_form()

    context = {
        'form': form,
        'data': data,
        # 'co': co,
        # 'sb': sb,
        'sub': subjects
    }
    return render(request, 'assign.html', context)


# deletions
# student del function
def delete_object_student(request, pk):
    obj_del = student_db.objects.get(student_Id=pk)
    name = obj_del.name

    if request.method == 'POST':
        obj_del.delete()
        return redirect('student-report')  # Redirect to a success page after deletion
    return render(request, 'student_del_confirm.html', {'name': name})

# course del function
def delete_object_course(request, pk):
    obj_del = Courses.objects.get(course_Id=pk)
    course_name = obj_del.course_name

    if request.method == 'POST':
        obj_del.delete()
        return redirect('courses')  # Redirect to a success page after deletion
    return render(request, 'course_del_confirm.html', {'name': course_name})

# assignment del function
def delete_object_assignment(request, pk):
    obj_del = Assignments.objects.get(id=pk)
    name = obj_del.student.name

    if request.method == 'POST':
        obj_del.delete()
        return redirect('assign')  # Redirect to a success page after deletion
    return render(request, 'assign_del_confirm.html', {'name': name})

# subject del function
def delete_object_subject(request, pk):
    obj_del = Subjects.objects.get(id=pk)
    subject = obj_del.subject

    if request.method == 'POST':
        obj_del.delete()
        return redirect('subject')  # Redirect to a success page after deletion
    return render(request, 'subject_del_confirm.html', {'subject': subject})

# table del function
def delete_object_table(request, pk):
    obj_del = TimeTable.objects.get(id=pk)

    if request.method == 'POST':
        obj_del.delete()
        return redirect('table')  # Redirect to a success page after deletion
    return render(request, 'table_del_confirm.html', {'tabletime': obj_del})



# edit functions
# students edit function
def student_update(request, pk):
    obj_update = student_db.objects.get(student_Id=pk)
    form = student_form(instance=obj_update)

    if request.method == "POST":
        form = student_form(request.POST, instance=obj_update)
        if form.is_valid():
            form.save()
            return redirect('student-report')

    return render(request, 'student_update.html', {'form': form, 'id': obj_update})

# courses edit function
def course_update(request, pk):
    obj_update = Courses.objects.get(course_Id=pk)
    form = Courses_forms(instance=obj_update)

    if request.method == "POST":
        form = Courses_forms(request.POST, instance=obj_update)
        if form.is_valid():
            form.save()
            return redirect('courses')

    return render(request, 'course_update.html', {'form': form, 'id': obj_update})

# subject edit function
def subject_update(request, pk):
    obj_update = Subjects.objects.get(id=pk)
    form = subject_form(instance=obj_update)

    if request.method == "POST":
        form = subject_form(request.POST, instance=obj_update)
        if form.is_valid():
            form.save()
            return redirect('subject')

    return render(request, 'subject_update.html', {'form': form, 'id': obj_update})

# assignment edit function
def assignment_update(request, pk):
    obj_update = Assignments.objects.get(id=pk)
    form = Assignments_form(instance=obj_update)

    if request.method == "POST":
        form = Assignments_form(request.POST, instance=obj_update)
        if form.is_valid():
            form.save()
            return redirect('assign')

    return render(request, 'assign_update.html', {'form': form, 'id': obj_update})



# print function
# pdf file generating function
def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

# page request and submission class
class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        # Retrieve all data from the database table
        queryset = student_db.objects.all()            

        student_list = list(queryset.values())
        context = {'data': student_list}

        # Generate the PDF
        pdf = render_to_pdf('print-page.html', context)
        # response
        return HttpResponse(pdf, content_type='application/pdf')


def render_to_pdf_table(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()

    # Create a PDF document with HTML content
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

    if not pdf.err:
        return result.getvalue()
    return None



def TimeTableViewPDF(request, pk):
    # tester
    # print(pk)
    selected = TimeTable.objects.get(pk=pk)
    
    context = {
        'selected': selected,
        'timedata': selected.get_timetable_data,
    }

    pdf = render_to_pdf_table('table-print.html', context)

    if pdf:
        # Create a HttpResponse object with the PDF content
        response = HttpResponse(pdf, content_type='application/pdf')
        # Add a Content-Disposition header to force download the PDF file
        response['Content-Disposition'] = 'attachment; filename="timetable.pdf"'
        return response

    return HttpResponse("Error generating PDF", status=500)


# time table generation
def time_table(request):
    subjects = Subjects.objects.all()
    courses = Courses.objects.all()
    form_course = subject_form()
    
    # selected = TimeTable.objects.get(id=pk)
    # print(selected)

    coursa = Courses.objects.values_list('course_name', flat=True)
    # taking stored data from the database
    dtime = TimeTable.objects.order_by('-TimeGenerated')

    # post action to be taken
    if request.method == 'POST':
        selected_course_name = request.POST.get('course')
        selected_course = Courses.objects.get(course_name=selected_course_name)
        selected_course_id = selected_course.course_Id

        # tester
        # print("Course ID: ", selected_course_id)

        core_subjects = ["ENGLISH", "CORE MATHEMATICS", "SCIENCE", "SOCIAL STUDIES", "FREE PERIOD"]
        listings = []
        for row in subjects:
            content = row.course_alloc.course_Id
            if content == selected_course_id:
                listings.append(row.subject)

                # testers
                # print("Course ID in Subject: " + str(content))
                # print("Subject: ", row.subject)
        
        core_subjects.extend(listings)
        core = list(core_subjects)
        random.shuffle(core)        

        # Define the timetable slots
        timetable_data = [
            {
                'time': '8:00 - 10:00',
                'monday': core[0],
                'tuesday': core[5],
                'wednesday': core[1],
                'thursday': core[4],
                'friday': core[6],
            },

            {
                'time': '10:00 - 12:00',
                'monday': core[1],
                'tuesday': core[6],
                'wednesday': core[2],
                'thursday': core[5],
                'friday': core[7],
            },

            {
                'time': '12:00 - 12:40',
                'monday': "BREAK",
                'tuesday': "BREAK",
                'wednesday': "BREAK",
                'thursday': "BREAK",
                'friday': "BREAK",
            },

            {
                'time': '12:40 - 2:40',
                'monday': core[2],
                'tuesday': core[7],
                'wednesday': core[3],
                'thursday': core[8],
                'friday': core[2],
            },

            {
                'time': '2:40 - 4:00',
                'monday': core[3],
                'tuesday': core[8],
                'wednesday': core[4],
                'thursday': core[0],
                'friday': core[3],
            },

            # Add more timetable slots as needed
        ]

        # storing generated data into the database
        timetable = TimeTable()
        timetable.save_timetable_data(timetable_data)

        context = {
            'timetable_data': timetable_data,
            'date_and_time': dtime,
        }
        return render(request, 'time-table.html', context)

    # # taking stored data from the database
    # dtime = TimeTable.objects.order_by('-TimeGenerated')

    context = {
        'coursa': coursa, 
        'date_and_time': dtime,
    }
    
    return render(request, 'time-table.html', context)



# logout function
def logout_view(request):
    logout(request)
    return redirect('login_view')

