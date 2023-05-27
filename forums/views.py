from django.shortcuts import render
from .models import Report, School

import requests
import json

def main(request, school_name):
    try:
        school_info = School.objects.filter(school=school_name)[0]
        context = {
            'school_name': school_info.school,
            'rank': school_info.rank
        }
        return render(request,'forums/main.html',context)
    except IndexError as e:
        context = {
            'school_name': school_name,
        }
        return render(request,'forums/empty.html',context)

def submain_preparation(request, school_name):
    context = {
        'school_name': school_name}

    return render(request, 'forums/submain_preparation.html',context)

def submain_uni_life(request, school_name):
    context = {
        'school_name': school_name}

    return render(request, 'forums/submain_uni_life.html',context)



# def half_length_slice(lst):
#     half_length = len(lst) // 2
#     return lst[:half_length]
# def half_length_slice_rest(lst):
#     half_length = len(lst) // 2
#     return lst[half_length:]


def courses(request, school_name):
    context = {
        'school_name': school_name,
        'course_name':"Software",
        'courses': [
            {  'rank': 4,
                "title": "SWE3208",
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            },
            {  'rank': 3,
                "title": "SWE3208",
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            },
            {  'rank': 5,
                "title": "SWE3208",
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            },
            {  'rank': 2,
                "title": "SWE3208",
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            },{  'rank': 1,
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

def uni_review(request, school_name):
    context = {
        'school_name': school_name,
        'uni_review': [
            {  'rank': 4,
      
                "date": "23년 1학기 수강자",
                "photo":['/static/images/Harvard2.jpg'],"photo_num":1,
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia.",
            },
            {  'rank': 3,
               'photo':["/static/images/Harvard1.jpg"],
               "photo_num":1,
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            },
            {  'rank': 5,
                
                "date": "23년 1학기 수강자",
                "photo":["/static/images/Harvard1.jpg" ,"/static/images/Harvard3.jpg" ],
                "photo_num":2,
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia.Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia ",
               
            },
            {  'rank': 2,
                
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            },{  'rank': 1,
               
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            },
            {  'rank': 4,
              
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            },
            {  'rank': 4,
                
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            },
            {  'rank': 4,
            
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            },{  'rank': 4,
               
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            },{  'rank': 4,
              
                "date": "23년 1학기 수강자",
                "content": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia . o est sit aliqua dolor do amet sint. Velit officia .",
            }
            
            
            ]}

    return render(request, 'forums/uni_review.html',context)

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
        'school_name': school_name,
        'visa_type': 'D-4',
        'visa_period': '약 2개월',
        'visa_application_process': [
             '비자 온라인 신청서 ABC 작성 (파견교 XYZ 문서 필수)',
             '비자 수수료 납부',
             '비자 인터뷰 예약'
        ],
        'update_date': '2023.04'

    }
    return render(request, 'forums/visa.html', context)

def dorm(request, school_name):
    context = {
        'school_name': school_name,
        'dorm_list': [
             'Starbucks',
             'Facebook',
             'Apple',
             'Google',
             'Amazon'
        ],
        'dorm_cost': '약 $1000/월',
        'dorm_link': 'https://www.naver.com',
        'dorm_characteristics': 'Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. ',
        'update_date': '2023.04'

    }
    return render(request, 'forums/dorm.html', context)

def etc_pre(request, school_name):
     context = {
        'school_name': school_name,
        'pre_list': [
            'Starbucks',
            'Facebook',
            'Apple',
            'Google',
            'Amazon'
        ],
        'pre_info': [
            {
               'content': 'Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit. Ecitation veniam consequat sunt nostrud amet.',
               'date': '2023년 1학기'
            },
            {
               'content': 'Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit. Ecitation veniam consequat sunt nostrud amet.',
               'date': '2023년 1학기'
            },
            {
               'content': 'Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit. Ecitation veniam consequat sunt nostrud amet.',
               'date': '2023년 1학기'
            },
            {
               'content': 'Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit. Ecitation veniam consequat sunt nostrud amet.',
               'date': '2023년 1학기'
            },
            {
               'content': 'Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit. Ecitation veniam consequat sunt nostrud amet.',
               'date': '2023년 1학기'
            },
            {
               'content': 'Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit. Ecitation veniam consequat sunt nostrud amet.',
               'date': '2023년 1학기'
            },
        ]
     }
     return render(request,'forums/etc_pre.html',context)

def fill_out(request, school_name):
    context = {
        'school_name': school_name
    }
    return render(request,'forums/fill_out.html',context)