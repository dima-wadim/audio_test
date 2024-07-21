# Audio Test Project

Этот проект предназначен для выявления пропущенных фрагментов ("потеряшек") в аудиозаписях.


## Установка

1. Установите необходимые зависимости:
    ```bash
    pip install -r requirements.txt
    ```

2. Убедитесь, что у вас установлен ffmpeg.

3. Убедитесь, что ваш аудиофайл находится в папке `data/` и имеет имя `audiofile.mp3`. Если у вас аудиофайл в другом формате, используйте `convert_audio.py` для конвертации в WAV:
    ```bash
    python convert_audio.py
    ```

4. Поместите текстовый файл с оригинальным текстом в папку `data/` и назовите его `textfile.txt`.

## Использование

Запустите основной скрипт для анализа "потеряшек":
```bash
python main.py
