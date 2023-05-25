from django.shortcuts import render
from .models import Report, School

import requests
import json

def main(request, school_name):

    # data = {
    #     'key': value
    # }
    # url = 'https://~~'
    # response = requests.get(url,params=data)
    # context = json.loads(response.text)

	school_info = School.objects.filter(school=school_name)[0]
	context = {
		'school_name': school_info.school,
		'rank': school_info.rank
	}
	return render(request, 'forums/main.html', context)

    # return render(request, 'forums/main.html', {'school_name': school_name})

def submain_preparation(request, school_name):
    context = {
        'school_name': school_name}

    return render(request, 'forums/submain_preparation.html',context)

def submain_uni_life(request, school_name):
    context = {
        'school_name': school_name}

    return render(request, 'forums/submain_uni_life.html',context)

def courses(request, school_name):
    context = {
        'school_name': school_name,
        'courses': [
            {  'rank': 4,
                "title": "SWE3208",
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            },
            {  'rank': 4,
                "title": "SWE3208",
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            },
            {  'rank': 4,
                "title": "SWE3208",
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            },
            {  'rank': 4,
                "title": "SWE3208",
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            },{  'rank': 4,
                "title": "SWE3208",
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            },
            {  'rank': 4,
                "title": "SWE3208",
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            },
            {  'rank': 4,
                "title": "SWE3208",
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            },
            {  'rank': 4,
                "title": "SWE3208",
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            },{  'rank': 4,
                "title": "SWE3208",
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            },{  'rank': 4,
                "title": "SWE3208",
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            }
            
            
            ]}

    return render(request, 'forums/courses.html',context)

def community(request, school_name):

    context = {
        'school_name': school_name,
        'community': [
            {
                "title": "파견학교 성적 에프",
                "content": "성적표에 안올릴 방법은 없나요? ㅠ",
                "date": "2023.05.23",
                "recommand": 0,
                "comment": 4,
            },
            {
                "title": "교환학생 여행",
                "content": "학기 할 거 다 끝나고 가나요?",
                "date": "2023.05.19",
                "recommand": 2,
                "comment": 3,
            },
            {
                "title": "공용주방",
                "content": "기숙사 공용주방 어떤가요?",
                "date": "2023.05.18",
                "recommand": 0,
                "comment": 10,
            },            
            {
                "title": "성적환산",
                "content": "알파벳으로 어떻게 바꾸셨나요?",
                "date": "2023.05.18",
                "recommand": 0,
                "comment": 2,
            },
            {
                "title": "학점인정",
                "content": "전공심화도 인정 되나요?",
                "date": "2023.05.17",
                "recommand": 0,
                "comment": 0,
            },
            {
                "title": "!hidden",
                "content": "",
                "date": "",
                "recommand": 0,
                "comment": 0,
            }
            ]
    }

    # 3의 배수가 되게끔 !hidden json을 추가로 넣어줘야 함

    return render(request, 'forums/community.html', context)

def visa(request, school_name):
    context = {
        'school_name': school_name
    }
    return render(request, 'forums/visa.html', context)