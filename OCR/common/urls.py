
from django.urls import path
from common import views

urlpatterns = [
    path('',views.showCommonPage,name='common_page'),
    path('student/',views.StudentPage,name='student'),
    path('std_register/',views.StudentRegister,name='std_register'),

    path('std_otp/',views.openStudentOtp,name='std_otp'),
]