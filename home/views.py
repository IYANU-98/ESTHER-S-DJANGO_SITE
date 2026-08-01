from django.shortcuts import render
from questions.models import PastQuestion

def hello_world_view(request):
    # 1. Fetch all questions from your database
    questions_list = PastQuestion.objects.all()
    
    # 2. Package the data into a dictionary (Context) to hand over to HTML
    context = {
        'all_questions': questions_list
    }
    
    # 3. Render the specific HTML template file using that data context
    return render(request, 'home/index.html', context)
