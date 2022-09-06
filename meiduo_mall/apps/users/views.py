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
        # 2. query database
        count = User.objects.filter(username=username).count()
        # 3. return response
        return JsonResponse({'code':0,'count':count,'errmsg':'ok'})
