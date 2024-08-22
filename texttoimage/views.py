# # views.py
import requests
from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    if request.method == 'POST':
        text_to_detect = request.POST.get('text')
        url = "https://ai-text-to-image-generator-api.p.rapidapi.com/realistic"
        payload = { "inputs": text_to_detect }  
        headers = {
            "x-rapidapi-key": "3e1142daa4msha68efb8f6386457p16a8bdjsnd710b0ae0d33",
            "x-rapidapi-host": "ai-text-to-image-generator-api.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)
        data  = response.json()
        imgurl = data['url']

        context={
            'response': imgurl,
        }
       
        return render(request,'homepage.html',context)
    return render(request,'homepage.html')

