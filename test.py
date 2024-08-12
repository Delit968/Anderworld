import subprocess
import time

# Путь к видеофайлу
video_path = "Anderworld\mus\music\VID_20240207_190430_594.mp4"  # замените на путь к вашему видеофайлу

# Путь к видеоплееру VLC
vlc_path = "C:/Program Files (x86)/Windows Media Player/wmplayer.exe"  # замените на путь к вашему VLC плееру

# Запуск 5 экземпляров плеера
for _ in range(5):
    subprocess.Popen([vlc_path, video_path])
    time.sleep(1)  # небольшая задержка между запусками
