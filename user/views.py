from constant import SUCCESSCODE,CODE,MESSAGE,ERROR
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import User
from django.db import transaction
from datetime import datetime
from errors import MandatoryInputMissingException,PasswordLengthError
from constant import SE001,SE001MESSAGE,IN001,IN001MESSAGE,IN002,IN002MESSAGE

import logging,hashlib,re

logger = logging.getLogger(__name__)


@api_view(['POST'])

def Signup(request):
    errorkeys = ['Info','Business_Errors','Warnings','System_Errors']
    errordisplay = [[],[],[],[]]
    ec = []
    ek = []
    try:
        data = request.data
        logger.info(f"Requested Data: {data}")
        name = data['name'] 
        email = data['email'] if data.get('email') else None
        phone = data['phone'] if data.get('phone') else None
        password = data['password'] if data.get('password') else None

        if name in ('None','') or email in ('None','') or phone in  ('None','') or password in (None,''):
            raise MandatoryInputMissingException("name/email/phone/password Mising")
        
        if len(str(password)) < 3 and len(str(password)) > 20 :
            raise PasswordLengthError("Password length is too short or too long")
        else:
            hashmd5 =hashlib.md5(str(password).encode()).hexdigest()
            logger.info(f"hashmd5 -> {hashmd5}")
            if hashmd5 is None:
                raise Exception("Md5 creation failed")
            
        if phone is not None:
            if re.match(r"^[123456789]{1}\d{9}$", phone):
                logger.info("Phone number format is valid")
                phone_exist = User.objects.filter(phone=phone).exists()

                if phone_exist:
                    raise Exception("Phone Already Exists")
                
        if email is not None:
            if re.match(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$",email):
                logger.info("Email format is valid")

                email_exists = User.objects.filter(email=email).exists()
                if email_exists:
                    raise Exception("Email already exists")
                
        with transaction.atomic():
            user_data = {'name':name,'email':email,'phone':phone,'password':password,'created_on':datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),'updated_on':datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}
            User.objects.create(**user_data)
            logger.info("User Creataed Successfully!")

        return Response({'CODE':SUCCESSCODE})
    
    except MandatoryInputMissingException as mime:
        logger.exception(mime)
        ec.append(IN001)
        ec.append(IN001MESSAGE)
        ek.append(CODE)
        ek.append(MESSAGE)
        errordisplay[0].append(dict(zip(ek,ec)))
        return Response({ERROR:(dict(zip(errorkeys,errordisplay)))})
    
    except PasswordLengthError as ple:
        logger.exception(ple)
        ec.append(IN002)
        ec.append(IN002MESSAGE)
        ek.append(CODE)
        ek.append(MESSAGE)
        errordisplay[0].append(dict(zip(ek,ec)))
        return Response({ERROR:(dict(zip(errorkeys,errordisplay)))})
    
    except Exception as e:
        logger.exception(e)
        ec.append(SE001)
        ec.append(SE001MESSAGE)
        ek.append(CODE)
        ek.append(MESSAGE)
        errordisplay[3].append(dict(zip(ek,ec)))
        return Response({ERROR:(dict(zip(errorkeys,errordisplay)))})
    

@api_view(['POST'])

def SignIn(request):
    errorkeys = ['Info','Business_Errors','Warnings','System_Errors']
    errordisplay = [[],[],[],[]]
    ec = []
    ek = []
    try:
        data = request.data
        logger.info(f"Requested Data: {data}")
        phone = data['phone'] if data.get('phone') else None
        email = data['email'] if data.get('email') else None
        password = data['password'] 

        if phone in (None ,'') and email in('None',''):
            raise MandatoryInputMissingException('Phone/Email Missing')
        
        if password in (None,''):
            raise MandatoryInputMissingException('Password is Missing')
        
        

    except Exception as e:
        logger.exception(e)
        ec.append(SE001)
        ec.append(SE001MESSAGE)
        ek.append(CODE)
        ek.append(MESSAGE)
        errordisplay[3].append(dict(zip(ek,ec)))
        return Response({ERROR:(dict(zip(errorkeys,errordisplay)))})
