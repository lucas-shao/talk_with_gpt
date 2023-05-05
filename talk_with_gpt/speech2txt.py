from paddlespeech.cli.asr.infer import ASRExecutor


def speech2txt(audio_file):
    asr = ASRExecutor()
    result = asr(audio_file=audio_file)
    return result


if __name__ == '__main__':
    result = speech2txt('recorded_audio.wav')
    print(result)
