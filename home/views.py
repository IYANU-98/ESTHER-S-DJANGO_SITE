from django.http import HttpResponse
from questions.models import PastQuestion  # This imports your questions database table 

def hello_world_view(request):
    # 1. Fetch all past questions currently saved in your database
    all_questions = PastQuestion.objects.all()

    # 2. Start building our website's visual layout
    html_content = """
    <html>
      <body>
    """

    return HttpResponse(html_content)