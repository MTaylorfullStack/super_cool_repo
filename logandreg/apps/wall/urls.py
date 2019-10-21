from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.success),
    url(r'^add_new_message$', views.add_message),
    url(r'^add_new_comment/(?P<message_id>\d+)', views.add_comment),
    url(r'^edit/(?P<message_id>\d+)', views.editpage),
    url(r'^edit_message/(?P<message_id>\d+)', views.save_edit),
    url(r'^delete/(?P<message_id>\d+)', views.destroy),
    url(r'^like/(?P<message_id>\d+)', views.like),
    url(r'^view/(?P<message_id>\d+)', views.view_mess)
]