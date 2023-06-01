import openai
import time

proxy = {
'http': 'http://localhost:7890',
'https': 'http://localhost:7890'
}
openai.proxy = proxy

# 模型:GPT3.5-turbo
def chatgpt(text):
    def chatgpt_inquery(text):
        start = time.time()
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                # model="text-davinci-003",
                messages=[{"role": "user", "content": text}]
            )
            print(completion)
        except (openai.APIError, openai.error.APIConnectionError):
            raise RuntimeError

        # print(completion["choices"][0]["message"]["content"])
        # print(completion)
        end = time.time()
        print(end - start)
        return completion
    
    try:
        completion = chatgpt_inquery(text)
        # print(completion["choices"][0]["message"]["content"])
        return completion["choices"][0]["message"]["content"]
    except RuntimeError:
        return 'API调用发生错误，请检查网络情况'
    
if __name__ == '__main__':
    # chatgpt('你好！')
    completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                # model="text-davinci-003",
                messages=[{"role": "user", "content": '你好！'}]
            )
    print(completion)
