from pydub import AudioSegment

def convert_audio_to_wav(audio_file_path, output_file_path):
    audio = AudioSegment.from_file(audio_file_path)
    audio = audio.set_frame_rate(16000).set_channels(1)
    audio.export(output_file_path, format="wav")

audio_file_path = 'data/audiofile.mp3'  # Укажите путь к вашему аудиофайлу
output_file_path = 'data/audiofile.wav'
convert_audio_to_wav(audio_file_path, output_file_path)
