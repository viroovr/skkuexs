from django.shortcuts import render

import requests
import json

def main(request, school_name):

    # data = {
    #     'key': value
    # }
    # url = 'https://~~'
    # response = requests.get(url,params=data)
    # context = json.loads(response.text)

    context = {
        'school_name': school_name,
        'rank': 4
    }
    return render(request, 'forums/main.html', context)

    # return render(request, 'forums/main.html', {'school_name': school_name})