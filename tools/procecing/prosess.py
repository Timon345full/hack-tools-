import subprocess
# import pygetwindow
# import psutil
# import time

# while True:
#     windows = pygetwindow.getAllTitles() # для получения названий всех процесов

#     for window in windows:
#         if 'браузер' in windows: # если в названии есть браузер то он будет его закрывать 
#             proces = psutil.process_iter([]) # для получения всех процесов
            
#             for proc in proces:
#                 if proc.info['name'] == "msedge.exe":
#                     proc.kill()
#     time.sleep(1) 