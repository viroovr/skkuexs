from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.db.models import Max
from common.views import community_profile_required
from .models import Report, Article, Comment
import requests
from statistics import mean
from django.conf import settings
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

SEARHCH_ENGINE_API_KEY = getattr(settings, 'SEARCH_ENGINE_API_KEY')
OPENCAGE_API_KEY = getattr(settings, 'OPENCAGE_API_KEY')
AIRLAB_API_KEY = getattr(settings, 'AIRLAB_API_KEY')
SEARCH_ENGINE = getattr(settings, 'SEARCH_ENGINE')

def search_google_images(keyword):
	url = 'https://www.googleapis.com/customsearch/v1'
	params = {
		'key': SEARHCH_ENGINE_API_KEY,
		"cx": SEARCH_ENGINE,
		'tbm': 'isch',  # 이미지 검색 모드로 설정
		'q': keyword + " landmarks",  # 검색할 키워드]
		'searchType': 'image'
	}
	# print(SEARHCH_ENGINE_API_KEY)
	response = requests.get(url, params=params)
	# print(response.json())
	if response.status_code == 200:
		pages = response.json()['items']
		# print(pages)
		image_srcs = []
		for page in pages:
			if 'link' in page:
				image_srcs.append(page['link'])

		return image_srcs[:3]
	else:
		print('Request failed with status code:', response.status_code)


def main(request, school_name):
	report_list = Report.objects.filter(university=school_name)
	if not report_list:
		return render(request, 'forums/empty.html', { 'school_name': school_name })
	report = report_list[0]
	context = {
		'school_name': school_name,
		'country': report.country,
		'introduction': report.introduction,
		'wordCloudUrl':report.word_cloud_url,
		'rank': mean(report.satisfaction for report in report_list),
        'image_urls': search_google_images(school_name)
	}
	return render(request, 'forums/main.html', context)

def submain_preparation(request, school_name):
	report_list = Report.objects.filter(university=school_name)
	context = {
		'school_name': school_name,
		'country': report_list[0].country if report_list else 'South Korea'
	}
	return render(request, 'forums/submain_preparation.html', context)

def submain_uni_life(request, school_name):
	report_list = Report.objects.filter(university=school_name)
	context = {
		'school_name': school_name,
		'country': report_list[0].country if report_list else 'South Korea'
	}
	return render(request, 'forums/submain_uni_life.html', context)

def courses(request, school_name):
	report_list = Report.objects.filter(university=school_name)

	course_name = []
	courses = []
	for report in report_list:
		course_name.append(report.course_name)
		if(report.course_etc == ""):
			continue
		courses.append({'rank': report.satisfaction,
		  				'title': report.department,
						'date': report.semester,
						'content': report.course_etc
						})
	context = {
        'school_name': school_name,
        'course_name': course_name,
        'courses': courses,
		'country': report_list[0].country if report_list else 'South Korea'
	}
	return render(request, 'forums/courses.html', context)

def uni_review(request, school_name):
	report_list = Report.objects.filter(university=school_name).order_by("-semester")

	uni_review = []
	for report in report_list:
		uni_review.append({ 'rank': report.satisfaction,
							'date': report.semester,
							# 'photo': ['/static/images/Harvard2.jpg'],
							'photo': "",
							'photo_num': 1,
							'content': report.impression
							})
	context = {
		'school_name': school_name,
		'uni_review': uni_review,
		'country': report_list[0].country if report_list else 'South Korea'
	}
	return render(request, 'forums/uni_review.html', context)

@community_profile_required
def community(request, school_name):
	if request.method == 'POST':
		if "comment" in request.POST:
			article = get_object_or_404(Article, pk=request.POST['article_id'])
			comment = Comment(
								user=request.user,
								article=article,
								content=request.POST['comment'],
								date=timezone.now()
							)
			comment.save()
		elif request.POST['community_title'] and request.POST['community_article']:
			article = Article(
								user=request.user,
								university=school_name,
								title=request.POST['community_title'],
								content=request.POST['community_article'],
								date=timezone.now(),
								recommand=0
							)
			article.save()
		return HttpResponseRedirect(reverse("forums:community", args=(school_name,)))

	article_list = Article.objects.filter(university=school_name).order_by("-date")
	community = []

	query = ""
	try:
		query = request.GET["query"]
	except:
		pass

	for article in article_list:
		if(query != ""):
			if(article.title.find(query) == -1 and article.content.find(query) == -1):
				continue
		community.append({ 'title_15': article.title if len(article.title) < 16 else article.title[:15]+"...",
		    				'title': article.title,
							'content_15': article.content if len(article.content) < 16 else article.content[:15]+"...",
							'content': article.content,
							'date': article.date.date,
							'recommand': article.recommand,
							'comment': article.comment.all(),
							'article': article
							})
	if(len(community) % 3 != 0):
		for i in range(3 - (len(community) % 3)):
			community.append({
				'title_15': "!hidden",
				'title': "!hidden",
				'content_15': "",
				'content': "",
				'date': "",
				'recommand': "",
				'comment': "",
			})	

	
	report_list = Report.objects.filter(university=school_name)
	context = {
		'school_name': school_name,
		'community': community,
		'country': report_list[0].country if report_list else 'South Korea',
		'query': query,
	}
	return render(request, 'forums/community.html', context)

def visa(request, school_name):
	report_list = Report.objects.filter(university=school_name)
	if not report_list:
		return render(request, 'forums/empty.html', { 'school_name': school_name })
	
	update_date = Report.objects.filter(university=school_name).exclude(visa_issuance_procedure__exact='').aggregate(Max('semester'))
	report = report_list[0]
	context = {
        'school_name': school_name,
        'visa_type': report.visa_type,
        'visa_period': report.visa_issuance_time,
        # 'visa_application_process': [f'{r}.' for r in report.visa_issuance_procedure.split('.') if r],
		'visa_application_process': report.visa_issuance_procedure,
		'country': report.country,
		'country_code': report.country_code,
        'update_date': update_date
    }
	return render(request, 'forums/visa.html', context)


def dorm(request, school_name):
	report_list = Report.objects.filter(university=school_name).annotate(count_dorm_name=Count('dorm_name', distinct=True)).order_by('-count_dorm_name')[:5]

	if not report_list:
		return render(request, 'forums/empty.html', { 'school_name': school_name })
	
	web_site_list = Report.objects.filter(university=school_name).exclude(dorm_website__exact='').filter(dorm_website__startswith='http')
	update_date = Report.objects.filter(university=school_name).exclude(dorm_etc__exact='').aggregate(Max('semester'))

	report = report_list[0]
	context = {
        'school_name': school_name,
		'dorm_list': sorted(set(r.dorm_name.strip() for r in report_list if r.dorm_name.strip() not in ("", "-")), key=len),
		'dorm_cost': report.dorm_cost,
		'dorm_link': web_site_list[0].dorm_website if web_site_list else "",
		'dorm_characteristics': ".".join(report.dorm_etc.split('.')[:3]),
        'update_date': update_date,
		'country': report.country
    }
	return render(request, 'forums/dorm.html', context)


def etc_pre(request, school_name):
	report_list = Report.objects.filter(university=school_name).exclude(pre_etc__exact='').order_by('-semester')
	if not report_list:
		return render(request, 'forums/empty.html', { 'school_name': school_name })
	
	update_date = Report.objects.filter(university=school_name).exclude(pre_etc__exact='').aggregate(Max('semester'))
	report = report_list[0]
	context = {
        'school_name': school_name,
		'pre_list': [],
		'pre_info': [{
				'content': report.pre_etc,
				'date': report.semester,
			}
			for report in report_list],
		'update_date': update_date,
		'country': report.country
    }
	return render(request, 'forums/etc_pre.html', context)

from geopy.distance import geodesic
def search_airport_nearby(school_name):
    # OpenCage Geocoding API 설정
    geocoding_api_key = OPENCAGE_API_KEY
    geocoding_url = f'https://api.opencagedata.com/geocode/v1/json?key={geocoding_api_key}'

    # 학교 이름을 기반으로 주소를 검색
    params = {
        'q': school_name,
        'limit': 1
    }
    response = requests.get(geocoding_url, params=params)
    data = response.json()
    # print(data)
    if 'results' in data and len(data['results']) > 0:
        # 학교의 위도와 경도 추출
        latitude = data['results'][0]['geometry']['lat']
        longitude = data['results'][0]['geometry']['lng']
        country_code = data['results'][0]['components']['country_code']
        # country_name = data['results'][0]['components']['country']
        airport_code_url = f"https://airlabs.co/api/v9/airports?country_code={country_code}&api_key={AIRLAB_API_KEY}"
        response = requests.get(airport_code_url)
        # print(country_name)
        # print(country_code)
        data = response.json()['response']
        # print(data)
        # print(response.json()['response'][0]['iata_code'])
        iata_code =[(item['lat'],item['lng']) for item in data if 'iata_code' in item] 
        # print(iata_code) 
        # 주변 항공 검색
        # airport_search_api_url = 'https://api.opencagedata.com/geocode/v1/json'
        # airport_search_params = {
        #     'q': f'{iata_code}',
        #     'limit': 5,  # 주변 항공 중 최대 5개 검색
        #     'proximity': f'{latitude},{longitude}',
        #     'no_annotations': 1,
        #     'key': geocoding_api_key,
        #     'countrycode': country_code
        # }
        # airport_response = requests.get(airport_search_api_url, params=airport_search_params)
        # airport_data = airport_response.json()['results']
        # print(airport_data)
		
        if iata_code:
            # airports = []
            nearest_airport = None
            shortest_distance = None
            for result in iata_code:
				
                airport_lat = result[0]
                airport_lng = result[1]
                distance = geodesic((latitude, longitude), (airport_lat, airport_lng)).km
                
                if shortest_distance is None or distance < shortest_distance:
                    shortest_distance = distance
                    nearest_airport = [airport_lat, airport_lng]
            # airports.append((airport_lat,airport_lng))

            # print(nearest_airport[0], nearest_airport[1])
            return latitude, longitude, nearest_airport[0], nearest_airport[1]

    return None


def etc_uni(request, school_name):
	# report_list = Report.objects.filter(university=school_name).exclude(etc_uni__exact='').order_by('-???')

	# etc_uni = []
	# # unilife_info=[]

	# update_date = Report.objects.filter(university=school_name).exclude(etc_uni__exact='').aggregate(Max('???'))

    # update_date = Report.objects.filter(user_university=school_name).exclude(etc_uni__exact='').aggregate(Max('???'))

	# for report in report_list:
	#    etc_uni.append({ 'rank': report.rank,
	#                   'date': report.semester,
	#                   'content': report.etc_feel
	#                   })
	# address = school_name
	# url = f'https://nominatim.openstreetmap.org/search?q={address}&format=json&limit=1'
	# response = requests.get(url)
	# if response.status_code == 200:
	# 	data = response.json()
	# 	print(data)
	# 	if data:
	# 		school_latitude = float(data[0]['lat'])
	# 		school_longitude = float(data[0]['lon'])
	# 		# 위도(latitude)와 경도(longitude)를 사용하여 필요한 작업 수행
	latitude, longitude, airport_lat, airport_lng = search_airport_nearby(school_name)
	# print(latitude, longitude, airport_lat, airport_lng) 

	# url = f'https://nominatim.openstreetmap.org/search?q={address}&format=json&limit=1'
	# response = requests.get(url)
	# if response.status_code == 200:
	# 	data = response.json()
	# 	print(data)
	# 	if data:
	# 		airport_latitude = float(data[0]['lat'])
	# 		airport_longitude = float(data[0]['lon'])
	# 		# 위도(latitude)와 경도(longitude)를 사용하여 필요한 작업 수행
			
	# print(airport_latitude, airport_longitude)

	report_list = Report.objects.filter(university=school_name).exclude(leisure='').order_by('-semester')
	tip = []
	for report in report_list:
		tip.append(report.leisure)

	update_date = Report.objects.filter(university=school_name).exclude(leisure='').aggregate(Max('semester'))
	report = report_list[0]

	context = {
		'school_name': school_name,
		# 'etc_uni_list': [],
		'tip': tip,
		"school_latitude": latitude, 
		"school_longitude": longitude,
		"airport_lat": airport_lat, 
		"airport_lng": airport_lng, 

		# 'unilife_info': [{
		#       'content': report.pre_etc,
		#       'date': report.semester,
		#    }
		#    for report in report_list],
		'update_date': update_date,
		'country': report.country,
	}
	return render(request, 'forums/etc_uni.html', context)