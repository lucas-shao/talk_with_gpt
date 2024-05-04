from openai import OpenAI


def audio2txt(audio_file_path):
    print("begin audio 2 txt ...")
    client = OpenAI()

    audio_file = open("recorded_audio.wav", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", file=audio_file
    )
    print("End audio 2 txt")

    return transcription.text


if __name__ == "__main__":
    result = audio2txt("recorded_audio.wav")
    print(result)
