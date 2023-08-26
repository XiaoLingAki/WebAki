from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Question

from .api import *
import json
import openai
import base64
import time

# Create your views here.

def index(request):
    return render(request, 'chataki/chat_page.html')
    
def chat_test(request):
    return render(request, 'chataki/chat_test.html')

history = '聊天记录：'
def process_gpt(request):

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
        
        answer = response_create(input_string)
        # answer1 = chatgpt_inquery(input_string)
        print(answer)
        # history += answer + '  '

        processed_string = answer
        print(processed_string)
        # processed_string = '111'
        return JsonResponse({'processed_string': processed_string})

    return JsonResponse({'error': 'Invalid request method'})

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
        
        answer = response_create(input_string)
        # answer1 = chatgpt_inquery(input_string)
        print(answer)
        # history += answer + '  '

        processed_string = answer
        print(processed_string)
        # processed_string = '111'
        return JsonResponse({'processed_string': processed_string})

    return JsonResponse({'error': 'Invalid request method'})

def process_one(request):
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
        input_string = '           ' + input_string
        answer = response_create(input_string)
        # answer1 = chatgpt_inquery(input_string)
        # print(answer)
        # history += answer + '  '

        processed_string = answer
        print(processed_string)
        # processed_string = '111'
        return JsonResponse({'processed_string': processed_string})

    return JsonResponse({'error': 'Invalid request method'})

def image_passing(request):

    def encode_image(image_path):
        with open(image_path, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return encoded_string

    # 读取图片并编码为Base64字符串
    image_path = '/home/kira/codes/WebAki/chataki/templates/chataki/background.jpg'
    encoded_image = encode_image(image_path)

    # 创建包含图片的JSON响应
    response = {
        'image': encoded_image
    }

    # 将JSON对象转换为字符串
    return JsonResponse(response)