from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class RegisterUser(APIView):
    def post(self,request):
        serializers = UserSerializer(data= request.data)
        
        if not serializers.is_valid():
            return Response({'Error': serializers.errors, 'message':'Sonething went wrong'})
        else:
            serializers.save()
            user = User.objects.get(username = serializers.data['username'])
            token_obj = Token.objects.get_or_create(user=user)

        return Response({'Employee': serializers.data, 'Token':str(token_obj),'message': 'Your data is saved successfully'})



class company(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        company_obj = Company.objects.all()
        serializers = CompanySerializer(company_obj,many=True)
        return Response({'Status':200, 'Company': serializers.data})
    
    def post(self,request):
        serializers = CompanySerializer(data=request.data)
        if not serializers.is_valid():
            return Response({'Error': serializers.errors, 'message':'Sonething went wrong'})
        else:
            serializers.save()
        return Response({'Company': serializers.data, 'message': 'Your data is saved successfully'})


#-----------------------------------------------------------------------------------------------------
class employee(APIView):
    def get(self,request):
        emp_obj = Employee.objects.all()
        serializers = EmployeeSerializer(emp_obj,many=True)
        return Response({'Status':200, 'Employee': serializers.data})
    
    def post(self,request):
        serializers = EmployeeSerializer(data=request.data)
        if not serializers.is_valid():
            return Response({'Error': serializers.errors, 'message':'Sonething went wrong'})
        else:
            serializers.save()
        return Response({'Employee': serializers.data, 'message': 'Your data is saved successfully'})
    
class companyemployee(APIView):
    def get(self,request, id):
        try:
            company_obj = Company.objects.get(id=id)
            emp_data = Employee.objects.filter(eid=company_obj)
            serializer = EmployeeSerializer(emp_data, many=True)
            return Response({'status': 200, 'Employee_data': serializer.data})
        
        except Company.DoesNotExist:
            return Response({'status': 404, 'error': 'Company not found'})
        except Employee.DoesNotExist:
            return Response({'status': 404, 'error': 'Employee data not found'})
        

