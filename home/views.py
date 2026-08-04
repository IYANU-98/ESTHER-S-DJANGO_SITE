from django.shortcuts import render
from django.db.models import Q  # <-- Import this to allow complex search filter rules
from questions.models import PastQuestion

def hello_world_view(request):
    # 1. Grab whatever text the user typed into the search box (defaults to empty string)
    query = request.GET.get('search_query', '')
    
    # 2. Fetch questions from your database
    if query:
        # If there is a search query, filter the database rows dynamically
        # 'icontains' means it looks for a match regardless of UPPERCASE or lowercase typos
        questions_list = PastQuestion.objects.filter(
            Q(course_code__icontains=query) | 
            Q(course_name__icontains=query) |
            Q(year__icontains=query)
        )
    else:
        # If the search bar is empty, just fetch absolutely everything like before
        questions_list = PastQuestion.objects.all()
    
    # 3. Package both the questions list and the query back to the HTML template
    context = {
        'all_questions': questions_list,
        'current_search': query
    }
    
    return render(request, 'home/index.html', context)
