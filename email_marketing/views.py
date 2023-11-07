from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

import csv
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
import pandas as pd


# Create your views here.



@api_view(['GET'])
def allSender(request):
    data = Sender.objects.all().order_by('-id')
    serializer = SenderSerializer(data, many=True)
    return Response(serializer.data)
    
    
    
    
    
    
@api_view(['GET'])
def detailSender(request, pk ):
    data = Sender.objects.get(id=pk)
    serializer = SenderSerializer(data)
    return Response(serializer.data)






@api_view(['POST'])
def CreateSender(request):
    data = request.data 
    serializer = SenderSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['POST'])
def UpdateSender(request, pk):
    data = Sender.objects.get(id = pk)
    serializer = SenderSerializer(instance=data, data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['DELETE'])
def deleteSender(request, pk):
    data = Sender.objects.get(id=pk)
    data.delete()
    return Response({
        "message":" Sender deleted successfully"
    })


#--------------------------------------------------





@api_view(['GET'])
def allCategory(request):
    data = Category.objects.all().order_by('-id')
    serializer = CategorySerializer(data, many=True)
    return Response(serializer.data)
    
    
    
    
    
    
@api_view(['GET'])
def detailCategory(request, pk ):
    data = Category.objects.get(id=pk)
    serializer = CategorySerializer(data)
    return Response(serializer.data)






@api_view(['POST'])
def CreateCategory(request):
    data = request.data 
    serializer = CategorySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['POST'])
def UpdateCategory(request, pk):
    data = Category.objects.get(id = pk)
    serializer = CategorySerializer(instance=data, data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['DELETE'])
def deleteCategory(request, pk):
    data = Category.objects.get(id=pk)
    data.delete()
    return Response({
        "message":" Category deleted successfully"
    })


#-------------------------------------------------



@api_view(['POST'])
def createBulkReceiver(request):
    if 'csv_file' in request.FILES:
        csv_file = request.FILES['csv_file']
        try:
            df = pd.read_csv(csv_file)

            receivers_data = []
            for _, row in df.iterrows():
                receiver_data = {
                    'email': row['gmail'],
                }

                if 'name' in row and not pd.isna(row['name']):
                    receiver_data['name'] = row['name']
                if 'phone' in row and not pd.isna(row['phone']):
                    receiver_data['phone'] = row['phone']
                if 'address' in row and not pd.isna(row['address']):
                    receiver_data['address'] = row['address']

                receivers_data.append(receiver_data)

            receivers = Receiver.objects.bulk_create([Receiver(**data) for data in receivers_data])

            serializer = ReceiverSerializer(receivers, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': 'Error processing the CSV file'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        data = request.data
        serializer = ReceiverSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








#------------------------------------------------------




@api_view(['GET'])
def allReceiver(request):
    data = Receiver.objects.all().order_by('-id')
    serializer = ReceiverSerializer(data, many=True)
    return Response(serializer.data)
    
    
    
    
    
    
@api_view(['GET'])
def detailReceiver(request, pk ):
    data = Receiver.objects.get(id=pk)
    serializer = ReceiverSerializer(data)
    return Response(serializer.data)






@api_view(['POST'])
def CreateReceiver(request):
    data = request.data 
    serializer = ReceiverSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['POST'])
def UpdateReceiver(request, pk):
    data = Receiver.objects.get(id = pk)
    serializer = ReceiverSerializer(instance=data, data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['DELETE'])
def deleteReceiver(request, pk):
    data = Receiver.objects.get(id=pk)
    data.delete()
    return Response({
        "message":" Category deleted successfully"
    })


#------------------------------------------------


@api_view(['GET'])
def allTemplate(request):
    data = Template.objects.all().order_by('-id')
    serializer = TemplateSerializer(data, many=True)
    return Response(serializer.data)
    
    
    
    
    
    
@api_view(['GET'])
def detailTemplate(request, pk ):
    data = Template.objects.get(id=pk)
    serializer = TemplateSerializer(data)
    return Response(serializer.data)






@api_view(['POST'])
def CreateTemplate(request):
    data = request.data 
    serializer = TemplateSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['POST'])
def UpdateTemplate(request, pk):
    data = Template.objects.get(id = pk)
    serializer = TemplateSerializer(instance=data, data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['DELETE'])
def deleteTemplate(request, pk):
    data = Template.objects.get(id=pk)
    data.delete()
    return Response({
        "message":" Template deleted successfully"
    })



#-------------------------------------------------



@api_view(['GET'])
def allHistory(request):
    data = History.objects.all().order_by('-id')
    serializer = HistorySerializer(data, many=True)
    return Response(serializer.data)
    
    
    
    
    
    
@api_view(['GET'])
def detailHistory(request, pk ):
    data = History.objects.get(id=pk)
    serializer = HistorySerializer(data)
    return Response(serializer.data)






@api_view(['POST'])
def CreateHistory(request):
    data = request.data 
    serializer = HistorySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['POST'])
def UpdateHistory(request, pk):
    data = History.objects.get(id = pk)
    serializer = HistorySerializer(instance=data, data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['DELETE'])
def deleteHistory(request, pk):
    data = History.objects.get(id=pk)
    data.delete()
    return Response({
        "message":" History deleted successfully"
    })




#-----------------------------------------------------------


# @api_view(['POST'])
# def sendEmailToReceiver(request, receiver_id, sender_id):
#     try:
#         receiver = Receiver.objects.get(id=receiver_id)
#         sender = Sender.objects.get(id=sender_id)

#         # Prepare email details
#         subject = "Your Subject Here"
#         message = "Your Email Message Here"
#         from_email = sender.EMAIL_HOST_USER
#         recipient_list = [receiver.email]

#         # Send the email
#         print("before")
#         send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#         print("after")

#         # Update the receiver to record that an email was sent
#         receiver.email_sent = True
#         receiver.save()

#         # Serialize and return the updated receiver
#         receiver_serializer = ReceiverSerializer(receiver)
#         return Response(receiver_serializer.data, status=status.HTTP_200_OK)
#     except ObjectDoesNotExist:
#         return Response({'error': 'Receiver or Sender not found'}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         print(f"Error sending email: {str(e)}")
#         return Response({'error': 'Error sending the email'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


from django.core.mail import send_mail, BadHeaderError
from smtplib import SMTPException  # Import SMTPException for exception handling

# ...

from django.core.mail import send_mail, BadHeaderError

# ...

@api_view(['POST'])
def sendEmailToReceiver(request, receiver_id, sender_id):
    try:
        receiver = Receiver.objects.get(id=receiver_id)
        sender = Sender.objects.get(id=sender_id)

        # Prepare email details
        subject = "Your Subject Here"
        message = "Your Email Message Here"
        from_email = sender.EMAIL_HOST_USER
        recipient_list = [receiver.email]

        # Send the email
        print("before")
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        print("after")

        # Update the receiver to record that an email was sent
        receiver.email_sent = True
        receiver.save()

        # Serialize and return the updated receiver
        receiver_serializer = ReceiverSerializer(receiver)
        return Response(receiver_serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'error': 'Receiver or Sender not found'}, status=status.HTTP_404_NOT_FOUND)
    except BadHeaderError:
        return Response({'error': 'Invalid header found'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return Response({'error': 'Error sending the email'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

