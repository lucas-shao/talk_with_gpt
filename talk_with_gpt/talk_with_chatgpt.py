from record_speech import record_speech
from speech2txt import speech2txt
from txt2speech import txt2speech
from chat_with_gpt import chat_with_gpt

# 1、录制用户的声音，保存到文件中
record_speech("recorded_audio.wav")

# 2、将用户声音转成TXT文字
input = speech2txt("recorded_audio.wav")

# 3、将TXT文件调用Chatgpt
output = chat_with_gpt(input)

# 4、将Chatgpt的输出结果转成语音
txt2speech(output, "output.wav")
