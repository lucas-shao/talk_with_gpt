from record_audio import record_audio
from audio2txt import audio2txt
from talk_with_gpt.txt2audio import txt2audio
from talk_with_gpt.talk_with_bot import talk_with_bot
from play_audio import play_audio

# 1、录制用户的声音，保存到文件中
record_audio("recorded_audio.wav")

# 2、将用户声音转成TXT文字
input = audio2txt("recorded_audio.wav")

# 3、将TXT文件调用Chatgpt
output = talk_with_bot(input)

# 4、将Chatgpt的输出结果转成语音
txt2audio(output, "answer.mp3")

# 5、播放语音
play_audio("answer.mp3")
