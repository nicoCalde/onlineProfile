from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name='opApp'
urlpatterns = [
    path('',views.index,name='index'),
    path('skills',views.skills,name='skills'),
    path('works',views.works,name='works'),
    path('get-works/', views.get_works, name='get_works'),
    path('education',views.education,name='education'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('opApp/chatbot/', views.chatbot, name='chatbot'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)