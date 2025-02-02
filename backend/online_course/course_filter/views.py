from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from course_filter.models import Course, Teacher, Website, Status, Fundraising, Discount, StudentsCount, Category, Review

from django.db.models import Count
from django.db.models import Q
import datetime


def Course_Sorting(courses: Course, method): # 課程排序機制
    if method == '價格由低到高':
        return sorted(courses, key=lambda d: d['course_price'], reverse=False)
    elif method == '價格由高到低':
        return sorted(courses, key=lambda d: d['course_price'], reverse=True)
    elif method == '課程時長從少到多':
        return sorted(courses, key=lambda d: d['course_time'], reverse=False)
    elif method == '課程時長從多到少':
        return sorted(courses, key=lambda d: d['course_time'], reverse=True)
    elif method == '學生人數從少到多':
        return sorted(courses, key=lambda d: d['course_students'], reverse=False)
    elif method == '學生人數從多到少':
        return sorted(courses, key=lambda d: d['course_students'], reverse=True)
    elif method == '評價數從少到多':
        return sorted(courses, key=lambda d: d['review_count'], reverse=False)
    elif method == '評價數從多到少':
        return sorted(courses, key=lambda d: d['review_count'], reverse=True)
    return sorted(courses, key=lambda d: d['course_name'])

def Course_Return_Form(courses): # 課程回傳格式
    result = []

    for i in range(len(courses)):
        data = {}
        data['course_name'] = courses[i]['course_name']
        data['course_intro'] = courses[i]['course_intro']
        data['course_img_url'] = courses[i]['course_img_url']
        data['course_time'] = courses[i]['course_time']
        #data['min_price'] = courses[i]['min_price']
        #data['max_price'] = courses[i]['max_price']
            
        status_description = Status.objects.filter(status_id = courses[i]['status_id']).values('status_description')[0]['status_description']
        data['status'] = status_description
        website_name = Website.objects.filter(website_id = courses[i]['website_id']).values('website_name')[0]['website_name']
        data['website_name'] = website_name
        teacher_name = Teacher.objects.filter(teacher_id = courses[i]['teacher_id']).values('teacher_name')[0]['teacher_name']
        data['teacher_name'] = teacher_name
        #category_name = Category.objects.filter(category_id = courses[i]['course_id']).values('category_name')[0]['category_name']
        #data['category_name'] = category_name
        #students_count = StudentsCount.objects.filter(course_id = courses[i]['course_id']).values('students_count')[0]['students_count']
        #data['students_count'] = students_count
        reviews = len(list(Review.objects.filter(course_id = str(courses[i]['course_id'])).values()))
        data['review_count'] = reviews
        #print(courses[i])
        result.append(data)
    
    return result


# Create your views here.
@api_view(['POST'])
def quick_search(request):
    if 'application/json' not in request.content_type:
        return Response("Content type should be 'application/json'.", status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'POST':
        try:
            content = request.data['Input']
            method = request.data['Sorting_method']
        except KeyError:
            return Response("No Input Data", status=status.HTTP_400_BAD_REQUEST)

        #potential_tid = Teacher.objects.filter(teacher_name__contains=content).values('teacher_id')
        
        potential_course = list(Course.objects.filter(
            Q(course_name__contains=content) |
            #Q(teacher_id__in=potential_tid) |
            Q(course_intro__contains=content)).values())
        
        #potential_course = list(Course.objects.filter(course_intro__contains=content).values())
        result = Course_Sorting(Course_Return_Form(potential_course), method)
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response("Request method error.", status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def search_all(request):
    if 'application/json' not in request.content_type:
        return Response("Content type should be 'application/json'.", status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'POST':
        try:
            content = request.data['Input']
            category = request.data['Category']
            tag = request.data['Tags']
            website = request.data['Website']
            method = request.data['Sorting_method']
            students_range = request.data['Students_range']
            price_range = request.data['Price_range']
            time_range = request.data['Time_range']
            status_type = request.data['Status']
        except KeyError:
            return Response("No Input Data", status=status.HTTP_400_BAD_REQUEST)
        
        if category == []:
            potential_category = Category.objects.values('category_id')
        else:
            potential_category = Category.objects.filter(category_name__in=category).values('category_id')
        if website == []:
            potential_web = Website.objects.values('website_id')
        else:
            potential_web = Website.objects.filter(website_name__in=website).values('website_id')
        if status == []:
            potential_status = Status.objects.values('status_id')
        else:
            potential_status = Status.objects.filter(status_description__in=status_type).values('status_id')
        
        if time_range == []:
            time_range = [0, 100000]
        elif len(time_range) == 1:
            time_range.insert(0, 0)
        
        if price_range == []:
            price_range = [0, 100000]
        elif len(time_range) == 1:
            price_range.insert(0, 0)

        #print(potential_category, potential_status, potential_web)

        potential_course = list(Course.objects.filter(
            Q(course_name__contains=content) &
            Q(category_id__in=potential_category) &
            Q(course_time__lte=int(time_range[1])) & 
            Q(course_time__gte=int(time_range[0])) &
            Q(website_id__in=potential_web) &
            Q(status_id__in=potential_status)).values())
        
        result = Course_Sorting(Course_Return_Form(potential_course), method)
        return Response(result, status=status.HTTP_200_OK)


@api_view(['POST'])
def category_view(request):
    if 'application/json' not in request.content_type:
        return Response("Content type should be 'application/json'.", status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'POST':
        try:
            category = request.data['Category']
            method = request.data['Sorting_method']
        except KeyError:
            return Response("No category is selected.", status=status.HTTP_400_BAD_REQUEST)
        
        c_id = Category.objects.filter(category_name=category).values('category_id')[0]['category_id']
        potential_course = list(Course.objects.filter(category_id=c_id).values())
        result = Course_Sorting(Course_Return_Form(potential_course), method)
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response("Request method error.", status=status.HTTP_405_METHOD_NOT_ALLOWED)