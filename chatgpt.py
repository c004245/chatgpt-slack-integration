import openai

YOUR_API_KEY = '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'


def ChatGPT(prompt, API_KEY=YOUR_API_KEY):
    openai.api_key = API_KEY

    completion = openai.Completion.create(
        engine='text-davinci-003'  # 'text-curie-001'  # 'text-babbage-001' #'text-ada-001'
        , prompt=prompt
        , temperature=0.5
        , max_tokens=1024
        , top_p=1
        , frequency_penalty=0
        , presence_penalty=0)

    return completion['choices'][0]['text']


def main():
    # 지문 입력 란
    prompt = input("Insert a prompt: ")
    print(ChatGPT(prompt).strip())


if __name__ == '__main__':
    main()
