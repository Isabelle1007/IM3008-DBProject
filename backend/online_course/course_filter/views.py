from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from course_filter.models import Course, Teacher, Website, Status, Fundraising, Discount, StudentsCount, Category

from django.db.models import Count
from django.db.models import Q
import datetime


def Course_Sorting(courses: Course, method): # 課程排序機制
    if method == 'Default':
        return courses.order_by('course_name')
    elif method == '價格由低到高':
        return courses.order_by('course_price')
    elif method == '價格由高到低':
        return courses.order_by('-course_price')
    elif method == '課程時長從少到多':
        return courses.order_by('course_time')
    elif method == '課程時長從多到少':
        return courses.order_by('-course_time')
    elif method == '學生人數從少到多':
        return courses.order_by('course_students')
    elif method == '學生人數從多到少':
        return courses.order_by('-course_students')
    elif method == '評價數從少到多':
        return courses.order_by("reviews_of_course")
    elif method == '評價數從多到少':
        return courses.order_by("-review_of_course")
    return []

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
        teacher_name = Teacher.objects.filter(teacher_id = courses[i]['teacher_id']).values('teacher_name')[0]['teacher_name']
        data['teacher_name'] = teacher_name
        #students_count = StudentsCount.objects.filter(course_id = courses[i]['course_id']).values('students_count')[0]['students_count']
        #data['students_count'] = students_count
        website_name = Website.objects.filter(website_id = courses[i]['website_id']).values('website_name')[0]['website_name']
        data['website_name'] = website_name
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
        except KeyError:
            return Response("No Input Data", status=status.HTTP_400_BAD_REQUEST)

        #potential_tid = Teacher.objects.filter(teacher_name__contains=content).values('teacher_id')
        
        potential_course = list(Course.objects.filter(
            Q(course_name__contains=content) |
            #Q(teacher_id__in=potential_tid) |
            Q(course_intro__contains=content)).values())
        
        #potential_course = list(Course.objects.filter(course_intro__contains=content).values())
        result = Course_Return_Form(potential_course)
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
            website = request.data['Websites']
            sort = request.data['Sorting_method']
            students_range = request.data['Students_range']
            price_range = request.data['Price_range']
            time_range = request.data['time_range']
            status_type = request.data['status']
        except KeyError:
            return Response("No Input Data", status=status.HTTP_400_BAD_REQUEST)

        potential_tid = Teacher.objects.filter(teacher_name__contains=content).values('teacher_id')
        
        potential_course = list(Course.objects.filter(
            Q(course_name__contains=content) |
            Q(teacher_id__in=potential_tid) |
            Q(course_intro__contains=content)).values())
        
        #potential_course = list(Course.objects.filter(course_intro__contains=content).values())
        result = Course_Return_Form(potential_course)
    
        return Response(result, status=status.HTTP_200_OK)


@api_view(['POST'])
def category_view(request):
    if 'application/json' not in request.content_type:
        return Response("Content type should be 'application/json'.", status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'POST':
        try:
            category = request.data['Category']
            sort = request.data['Sorting_method']
        except KeyError:
            return Response("Not select any category.", status=status.HTTP_400_BAD_REQUEST)
        
        c_id = Category.objects.filter(category_name=category).values('category_id')[0]['category_id']
        #print(c_id)
        Course.objects.annotate(review_count = Count("reviews_of_course"))
        potential_course = Course.objects.filter(category_id=c_id).values()
        '''
        if sort == 'Name_A':
            potential_course = list(potential_course.order_by("course_name"))
        elif sort == 'Name_Z':
            potential_course = list(potential_course.order_by("-course_name"))
        elif sort == 'Price_Min':
            potential_course = list(potential_course.order_by("course_price"))
        elif sort == 'Price_Max':
            potential_course = list(potential_course.order_by("-course_price"))
        '''
        potential_course = list(Course_Sorting(potential_course, sort))
        #potential_course = list(Course.objects.filter(course_intro__contains=content).values())
        result = Course_Return_Form(potential_course)
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response("Request method error.", status=status.HTTP_405_METHOD_NOT_ALLOWED)