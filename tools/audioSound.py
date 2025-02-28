import pyaudio
import speech_recognition as sr
import tkinter as tk

def readMicrophone(DeviceIndex=1, timeout=7, phrase_time_limit=5):
    windows = tk.Tk()
    windows.geometry("650x450")
    windows.title("Запись с микрофона")
    windows.resizable(False, False)

    # p = pyaudio.PyAudio() device microphone use users 
    # for i in range(p.get_device_count()):
    #     print(i, p.get_device_info_by_index(i)['name'])



    r = sr.Recognizer()

    def speech():
        with sr.Microphone(device_index=DeviceIndex) as sourse:
            txt_label.configure(text="Говорите...")
            windows.update()

            try:
                audio = r.listen(sourse, phrase_time_limit=phrase_time_limit, timeout=timeout)
                query = r.recognize_google(audio, language='ru-RU')
            
            except(sr.WaitTimeoutError, sr.UnknownValueError):
                txt_label.configure(text="Я вас не понял или не слышу....Скажите еще раз....")
                windows.update()
                speech()
            
            else:
                txt_label.configure(text="Нажмите на кнопку и говорите")
                return query.capitalize()
            
    def insert_rec():
        recording = speech()
        txt.insert(1.0, recording)
            
    txt = tk.Text(windows)
    txt.place(x=0, y=0)


    # def save_output(): # funcition not active 
    #     with open("static/audio/output.mp3", "w+") as file:
    #         file.write(txt_label)
    #         file.close()

    button_rec = tk.Button(windows, text='rec', bg='red', font=('copper', 16), command=insert_rec)
    button_rec.place(x=30, y=400)
    # button_save_audio = tk.Button(windows, text="save output", font=('copper', 16), command=save_output)

    txt_label = tk.Label(windows, text="Нажмите на кнопку и говорите", font=('coover', 16))
    txt_label.place(x=100, y=408)
    # button_save_audio.place(x=30, y=10)
    windows.mainloop()

readMicrophone()