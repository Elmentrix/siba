from django.urls import path
from . import views

# url
urlpatterns = [
    # log paths
    path('', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('index/', views.student_report, name='student-report'),
    path('course/', views.course_form, name='courses'),
    path('subjects/', views.subjects_view, name='subject'),
    path('assign/', views.assiner, name='assign'),
    path('time-table/', views.time_table, name='table'),

    # del paths
    path('student_delete_confirmation/<str:pk>/', views.delete_object_student, name='delete_student'),
    path('course_delete_confirmation/<str:pk>/', views.delete_object_course, name='delete_course'),
    path('assign_delete_confirmation/<str:pk>/', views.delete_object_assignment, name='delete_assign'),
    path('subject_delete_confirmation/<str:pk>/', views.delete_object_subject, name='delete_subject'),
    path('table_delete_confirmation/<str:pk>/', views.delete_object_table, name='delete_table'),

    # edit paths
    path('update_details/<str:pk>/', views.student_update, name='student_update'),
    path('update_course_details/<str:pk>/', views.course_update, name='course_update'),
    path('update_csubject_details/<str:pk>/', views.subject_update, name='subject_update'),
    path('update_assignment_details/<str:pk>/', views.assignment_update, name='assignment_update'),

    # print paths
    path('print-pdf/', views.ViewPDF.as_view(), name='view_pdf'),
    path('time-table-pdf/<int:pk>/', views.TimeTableViewPDF, name='table_view_pdf')
]