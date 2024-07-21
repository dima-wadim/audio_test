import speech_recognition as sr
from pydub import AudioSegment
import difflib
import os


def convert_audio_to_wav(audio_file_path, output_file_path):
    audio = AudioSegment.from_file(audio_file_path)
    audio = audio.set_frame_rate(16000).set_channels(1)
    audio.export(output_file_path, format="wav")


def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)
    try:
        transcript = recognizer.recognize_google(audio, language="ru-RU")
        return transcript
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""


def compare_texts(original_text, transcribed_text):
    original_lines = original_text.split('. ')
    transcribed_lines = transcribed_text.split('. ')

    differ = difflib.Differ()
    diff = list(differ.compare(original_lines, transcribed_lines))

    missing_lines = [line for line in diff if line.startswith('- ')]

    return missing_lines


def main():
    audio_file_path = 'data/audiofile.mp3'  # Укажите путь к вашему аудиофайлу
    wav_file_path = 'data/audiofile.wav'
    text_file_path = 'data/textfile.txt'

    # Конвертируем аудиофайл в формат WAV
    convert_audio_to_wav(audio_file_path, wav_file_path)

    with open(text_file_path, 'r', encoding='utf-8') as file:
        original_text = file.read()

    transcribed_text = transcribe_audio(wav_file_path)

    missing_lines = compare_texts(original_text, transcribed_text)

    if missing_lines:
        print("Потеряшки найдены:")
        for line in missing_lines:
            print(line[2:])
    else:
        print("Потеряшек нет")


if __name__ == '__main__':
    main()
