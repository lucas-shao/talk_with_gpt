import pyaudio
import numpy as np
import wave
import time


def record_speech(audio_recorded_file):
    recorded_data = record_voice(fs=16000)
    save_to_wav(recorded_data, audio_recorded_file, fs=16000)


def voice_detector(data, threshold=1000):
    # 通过判断数据的均值是否大于阈值来判断是否有声音
    volume = np.abs(data).mean()
    print("当前音量：", volume, "是否有声音：", volume > threshold)
    return volume > threshold


def record_voice(stop_time=2, fs=44100, channels=1, chunk=1024):
    print("正在监听...")

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=channels, rate=fs, input=True, frames_per_buffer=chunk)

    buffer = []
    last_voice_time = time.time()

    while True:
        data = stream.read(chunk)
        data_np = np.frombuffer(data, dtype=np.int16)
        if voice_detector(data_np):
            buffer.append(data)
            last_voice_time = time.time()
        elif buffer and (time.time() - last_voice_time > stop_time):
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    print("录音结束")
    return b''.join(buffer)


def save_to_wav(data, file_name, fs=44100, channels=1):
    with wave.open(file_name, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(pyaudio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(fs)
        wf.writeframes(data)


if __name__ == "__main__":
    record_speech("recorded_audio.wav")
