from django.urls import path,include
from .views import *

urlpatterns = [
    path('sender-list/', allSender),
    path('sender-detail/<int:pk>/', detailSender),
    path('sender-create/', CreateSender),
    path('sender-update/<int:pk>/', UpdateSender),
    path('sender-delete/<int:pk>/', deleteSender),


    path('category-list/', allCategory),
    path('category-detail/<int:pk>/', detailCategory),
    path('category-create/', CreateCategory),
    path('category-update/<int:pk>/', UpdateCategory),
    path('category-delete/<int:pk>/', deleteCategory),

    
    path('receiver-list/', allReceiver),
    path('receiver-detail/<int:pk>/', detailReceiver),
    path('receiver-create/', CreateReceiver),
    path('receiver-update/<int:pk>/', UpdateReceiver),
    path('receiver-delete/<int:pk>/', deleteReceiver),


    path('templete-list/', allTemplate),
    path('templete-detail/<int:pk>/', detailTemplate),
    path('templete-create/', CreateTemplate),
    path('templete-update/<int:pk>/', UpdateTemplate),
    path('templete-delete/<int:pk>/', deleteTemplate),


    
    path('history-list/', allHistory),
    path('allHistory-detail/<int:pk>/', detailHistory),
    path('allHistory-create/', CreateHistory),
    path('allHistory-update/<int:pk>/', UpdateHistory),
    path('allHistory-delete/<int:pk>/', deleteHistory),
    
    
    path('bulk/', createBulkReceiver),

    path('send_email_to_receiver/<int:receiver_id>/<int:sender_id>/', sendEmailToReceiver),
    

]
