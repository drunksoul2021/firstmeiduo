
import re

from django.shortcuts import render

# Create your views here.
from django.views import View

"""
1. demand analasis
"""

"""
judge user_name is_repeated function
front_end: when user input uername,lost blur, send axios request

back_end:
    request:  receive username
    bussniess logic:  according to username query databases,
    if query result equal 0, it means no register
    if query result equal 1, it means is already register
    
    
    response:  JSON
                {code:0,count:0/1,errmsg:0k}
                
    route       GET   	/usernames/<username>/count/
                
    step:
#    1. recevie username
#    2. query database
#    3. return response
"""
from apps.users.models import User
from django.http import JsonResponse
class UsernameCountView(View):

    def get(self,request,username):
        # 1. recevie username judge username is_fulfill username rule
        # if not re.match('[a-zA-Z0-9_-]{5,20}',username):
        #     return JsonResponse({'code':200,'errmsg':'username is not fit for username rule'})

        # 2. query database
        count = User.objects.filter(username=username).count()
        # 3. return response
        return JsonResponse({'code':0,'count':count,'errmsg':'ok'})

"""
we don't trust front_end's data !!! must be checked out!
front_end: as user enter uername,password,mobile, agree agreement, click register button
            front end will send axios request

back_end:
    request:        recevie(JSON) request ,
    business logic: auth data, data insert into database
    response:       JSON{'code':0,'errmsg':'ok'}
    code	响应码 0 表示成功 400表示失败
    
    route:  POST  register/
    step:
        # 1. recevie requst(POST----------JSON)
        # 2. get data
        # 3. auth data
        #     3.1 uername,password,mobile, agree agreement
        #     3.2 username fullfil rules,can not repeat
        #     3.3 password fullfil rules
        #     3.4 comfirm password identical
        #     3.5 mobile fullfil rules ,can not repeat
        #     3.6 agree files
        # 4. insert data
        # 5. return response
"""
import json
class RegisterView(View):

    def post(self,request):
        # 1. recevie requst(POST----------JSON)
        body_bytes = request.body
        body_str = body_bytes.decode()
        body_dict = json.loads(body_str)
        # 2. get data
        username = body_dict.get('username')
        password = body_dict.get('password')
        password2 = body_dict.get('password2')
        mobile = body_dict.get('mobile')
        allow = body_dict.get('allow')
        # 3. auth data
        #     3.1 uername,password,mobile, agree agreement
        #all([xxx,xxx,xxx])
        #if the fators in all are None,False
        #then return False, or return True
        if not all([username,password,password2,mobile,allow]):
            return JsonResponse({'code':400,'errmsg':'agr need to fill all'})
        #     3.2 username fullfil rules,can not repeat
        if not re.match('[a-zA-Z_-]{5,20}',username):
            return JsonResponse({'code': 400, 'errmsg': 'username unfullfil rules'})
        #     3.3 password fullfil rules
        #     3.4 comfirm password identical
        #     3.5 mobile fullfil rules ,can not repeat
        #     3.6 agree files
        # 4. insert data
        # user = User(username=username,password=password,mobile=mobile)
        # user.save()
        #User.objects.create(username=username,password=password,mobile=mobile)
        # above two ways can not encrypt, use the blow way
        User.objects.create_user(username=username,password=password,mobile=mobile)
        # 5. return response
        return JsonResponse({'code':0,'errmsg':'ok'})
