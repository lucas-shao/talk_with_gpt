from openai import OpenAI


def txt2audio(text, file_path="answer.mp3"):
    print("begin txt 2 audio ...")
    client = OpenAI()

    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=text,
    )

    response.stream_to_file(file_path)
    print("End txt 2 audio")


if __name__ == "__main__":
    result = txt2audio("今天天气怎么样？")
    print(result)
