from django.shortcuts import render

def main(request, school_name):
    return render(request, 'forums/main.html', {'school_name': school_name})