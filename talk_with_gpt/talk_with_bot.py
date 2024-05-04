from openai import OpenAI


def talk_with_bot(answer):
    print("begin talk with bot ...")
    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "你是一个很有用的老师，请使用中文回答问题",
            },
            {"role": "user", "content": answer},
        ],
    )
    print("End talk with bot")
    return response.choices[0].message.content


if __name__ == "__main__":
    result = talk_with_bot("What is the capital of China?")
    print(result)
