import pyaudio
import audioop
import wave


def record_audio(filename):
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1
    fs = 44100  # Record at 44100 samples per second
    silence_threshold = 500  # Silence threshold
    silence_limit = 30  # Silence limit

    p = pyaudio.PyAudio()

    stream = p.open(
        format=sample_format,
        channels=channels,
        rate=fs,
        frames_per_buffer=chunk,
        input=True,
    )

    frames = []

    while True:
        data = stream.read(chunk)
        rms = audioop.rms(data, 2)  # Get RMS value

        if rms > silence_threshold:
            print("Sound detected, start recording...")
            frames.append(data)

            silence_counter = 0
            while silence_limit >= silence_counter:
                if rms > silence_threshold:
                    silence_counter = 0
                else:
                    silence_counter += 1
                data = stream.read(chunk)
                rms = audioop.rms(data, 2)
                frames.append(data)
            print(silence_counter)
            print("Sound ended, stop recording.")
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    print("Saving file...")
    wf = wave.open(filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b"".join(frames))
    wf.close()
    print("File saved.")


if __name__ == "__main__":
    record_audio("recorded_audio.wav")
