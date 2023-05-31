from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Question
from chataki.chatgpt import digital_person_chat
from chataki.chatgpt import digital_person
import json

# Create your views here.

def index(request):
    return render(request, 'chataki/chat_page.html')
    
def chat_test(request):
    return render(request, 'chataki/chat_test.html')

history = '聊天记录：'
def process(request):

    global history

    if request.method == 'POST':
        print("received")
        data = json.loads(request.body)
        input_string = data.get('input_string')
        print(input_string)
        # 在这里执行对输入字符串的处理操作，得到处理后的字符串

        # if len(history) > 1600:
        #     history = '聊天记录：' + history[800:]
        # input_text = input_string
        # history += input_text + '  '
        # print(f"{input_text}")

        answer = digital_person_chat(digital_person[0], history, input_string)
        # print(answer)
        # history += answer + '  '

        processed_string = answer
        print(processed_string)
        # processed_string = '111'
        return JsonResponse({'processed_string': processed_string})

    return JsonResponse({'error': 'Invalid request method'})
