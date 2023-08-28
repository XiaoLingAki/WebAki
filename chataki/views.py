from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Question

from .api import *
import json
import openai
import base64
import time

import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin

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

def stable_diffusion(request):
    
    logger.debug("received")
    url = "http://192.168.31.76:7861"
    
    logger.debug(request.body)
    data = json.loads(request.body)
    
    prompt_prefix = 'masterpiece, best quality, illustration, extremely detailed 8K wallpaper'
    # 负面提示词，sd 的一个参数
    negative_prompt = 'NG_DeepNegative_V1_75T, badhandv4, EasyNegative, bad hands, missing fingers, cropped legs, worst quality, low quality, normal quality, jpeg artifacts, blurry,missing arms, long neck, Humpbacked,multiple breasts, mutated hands and fingers, long body, mutation, poorly drawn , bad anatomy,bad shadow,unnatural body, fused breasts, bad breasts, more than one person,wings on halo,small wings, 2girls, lowres, bad anatomy, text, error, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, out of frame, lowres, text, error, cropped, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers,'
    # 这也是 sd 的一个参数
    sampler_index = 'DPM++ SDE Karras'


    input_string = data.get('input_string')
    logger.debug(input_string)
    payload = {
        "prompt": prompt_prefix + ', ' + input_string,
        "negative_prompt": negative_prompt,
        "cfg_scale": 7,
        "width": 1024, 
        "height": 768, 
        "steps": 50
    }
    logger.debug(payload["prompt"])
    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

    r = response.json()
    encoded_image = r['images'][0]
    # logger.debug(encoded_image)
    # 将JSON对象转换为字符串
    
    response1 = {
        'image': encoded_image
    }
    return JsonResponse(response1)