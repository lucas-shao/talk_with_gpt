from paddlespeech.cli.tts.infer import TTSExecutor
from pydub import AudioSegment
from pydub.playback import play


def txt2speech(text, output):
    tts = TTSExecutor()
    tts(text=text, output=output)

    # 加载音频文件
    audio = AudioSegment.from_file(output, format="wav")

    # 播放音频
    play(audio)


if __name__ == '__main__':
    result = txt2speech(
        '五月天（Mayday），中国台湾摇滚乐团，成立于1997年3月29日，由温尚翊（怪兽）、陈信宏（阿信）、石锦航（石头）、蔡升晏（玛莎）、刘谚明（冠佑）五名成员组成。', 'output.wav'
    )
    print(result)
