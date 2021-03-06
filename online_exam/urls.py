from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^faculty_dashboard/$', views.faculty_dashboard, name='faculty_dashboard'),
    url(r'^faculty_add_course/$', views.faculty_add_course, name='faculty_add_course'),
    url(r'^faculty_add_exam/$', views.faculty_add_exam, name='faculty_add_exam'),
    url(r'^faculty_add_topic/$', views.faculty_add_topic, name='faculty_add_topic'),
    url(r'^faculty_add_subtopic/$', views.faculty_add_subtopic, name='faculty_add_subtopic'),
    url(r'^faculty_add_question/$', views.faculty_add_question, name='faculty_add_question'),
    url(r'^faculty_evaluate/$', views.faculty_evaluate, name='faculty_evaluate'),
    url(r'^faculty_exam_registrations/$', views.faculty_exam_registrations, name='faculty_exam_registrations'),
    url(r'^faculty_modify_course/$', views.faculty_modify_course, name='faculty_modify_course'),
    url(r'^faculty_modify_exam/$', views.faculty_modify_exam, name='faculty_modify_exam'),
    url(r'^faculty_modify_topic/$', views.faculty_modify_topic, name='faculty_modify_topic'),
    url(r'^faculty_modify_subtopic/$', views.faculty_modify_subtopic, name='faculty_modify_subtopic'),
    url(r'^faculty_modify_question/$', views.faculty_modify_question, name='faculty_modify_question'),
    url(r'^faculty_profile/$', views.faculty_profile, name='faculty_profile'),
    url(r'^faculty_update_course/$', views.faculty_update_course, name='faculty_update_course'),
    url(r'^faculty_update_exam/$', views.faculty_update_exam, name='faculty_update_exam'),
    url(r'^faculty_update_topic/$', views.faculty_update_topic, name='faculty_update_topic'),
    url(r'^faculty_update_subtopic/$', views.faculty_update_subtopic, name='faculty_update_subtopic'),
    url(r'^faculty_update_question/$', views.faculty_update_question, name='faculty_update_question'),
    url(r'^faculty_user_registrations/$', views.faculty_user_registrations, name='faculty_user_registrations'),
    url(r'^faculty_view_courses/$', views.faculty_view_courses, name='faculty_view_courses'),
    url(r'^faculty_view_exams/$', views.faculty_view_exams, name='faculty_view_exams'),
    url(r'^faculty_view_topics/$', views.faculty_view_topics, name='faculty_view_topics'),
    url(r'^faculty_view_subtopics/$', views.faculty_view_subtopics, name='faculty_view_subtopics'),
    url(r'^faculty_view_questions/$', views.faculty_view_questions, name='faculty_view_questions'),
    url(r'^student_dashboard/$', views.student_dashboard, name='student_dashboard'),
    url(r'^student_exams/$', views.student_exams, name='student_exams'),
    url(r'^student_profile/$', views.student_profile, name='student_profile'),
    url(r'^student_progress/$', views.student_progress, name='student_progress'),
]
