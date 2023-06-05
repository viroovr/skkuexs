from django.shortcuts import render
from django.db.models import Max
from common.views import community_profile_required
from .models import Report, Article

from statistics import mean

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
		courses.append({'rank': report.satisfaction,
		  				'title': report.course_num,
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
	report_list = Report.objects.filter(university=school_name)

	uni_review = []
	for report in report_list:
		uni_review.append({ 'rank': report.satisfaction,
							'date': report.semester,
							'photo': ['/static/images/Harvard2.jpg'],
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
	article_list = Article.objects.filter(university=school_name)

	community = []
	for article in article_list:
		community.append({ 'title': article.title,
							'content': article.content,
							'date': article.date.date,
							'recommand': article.recommand,
							'comment': article.comment
							})
	report_list = Report.objects.filter(university=school_name)
	context = {
		'school_name': school_name,
		'community': community,
		'country': report_list[0].country if report_list else 'South Korea'
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
        'visa_application_process': [
			report.visa_issuance_procedure,
			report.pre_departure_preparation
        ],
		'country': report.country,
		'country_code': report.country_code,
        'update_date': update_date
    }
	return render(request, 'forums/visa.html', context)

from django.db.models import Count

def dorm(request, school_name):
	report_list = Report.objects.filter(university=school_name).annotate(count_dorm_name=Count('dorm_name', distinct=True)).order_by('-count_dorm_name')[:5]

	if not report_list:
		return render(request, 'forums/empty.html', { 'school_name': school_name })
	
	web_site_list = Report.objects.filter(university=school_name).exclude(dorm_website__exact='').filter(dorm_website__startswith='http')
	update_date = Report.objects.filter(university=school_name).exclude(dorm_etc__exact='').aggregate(Max('semester'))

	report = report_list[0]
	context = {
        'school_name': school_name,
		'dorm_list': list(set(r.dorm_name.strip() for r in report_list if r.dorm_name.strip() not in ("", "-"))),
		'dorm_cost': max([report.dorm_cost for report in report_list], key=len),
		'dorm_link': web_site_list[0].dorm_website if web_site_list else "",
		'dorm_characteristics': report.dorm_etc,
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
	return render(request,'forums/etc_pre.html', context)

def etc_uni(request, school_name):
	# report_list = Report.objects.filter(university=school_name).exclude(etc_uni__exact='').order_by('-???')

	# etc_uni = []
	# # unilife_info=[]

	# update_date = Report.objects.filter(university=school_name).exclude(etc_uni__exact='').aggregate(Max('???'))


	# for report in report_list:
	#    etc_uni.append({ 'rank': report.rank,
	#                   'date': report.user_duration,
	#                   'content': report.etc_feel
	#                   })
	context = {
		'school_name': school_name,
		'etc_uni_list': [],
		'tip': [
				"학교 시내 무어마켓에서 저렴하게 식자재 구입이 가능합니다",
				"학생증으로 할인 받을 수 있는 품목(쇼핑, 교통 등)이 많습니다",
				"학교 기숙사 주관으로 열리는 다양한 무료행사들이 많습니다",
				"학기초 열리는 동아리 Fair에서 들어볼 동아리 선택할 수 있어요",
				"Give it A Go라는 1회 체험 프로그램도 있답니다"
		]
		# 'unilife_info': [{
		#       'content': report.pre_etc,
		#       'date': report.user_duration,
		#    }
		#    for report in report_list],
		# 'update_date': update_date,
		# 'country': report.user_country,
	}
	return render(request, 'forums/etc_uni.html', context)