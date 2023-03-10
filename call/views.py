from django.shortcuts import render, redirect
from time import time
from .zoom import createMeeting
from user.models import RecordedCall

# Create your views here.
def home(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            meeting = createMeeting() 
            host_url = meeting['start_url']
            join_url = meeting['join_url']
            password = meeting['password']
            meet_id = meeting['id'] 
            datetime = meeting['start_time']
            duration = meeting['duration']
            #file_name = 'video'
            print(meet_id,  datetime,  duration)
            context = {'meet_id':meet_id, 'join_url':join_url, 'password':password}
            data = RecordedCall(user = request.user, meeting_id = meet_id, date_time = datetime, duration = duration )
            data.save()
            return render(request, 'meet_landing.html', context)

        else:
            return redirect('/myaccount/login/') 

    return render(request, 'home.html')

