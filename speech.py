# -*- coding: utf-8 -*-
import speech_recognition as sr 
from datetime import datetime

r = sr.Recognizer()
mic = sr.Microphone()

txt='result.txt'
with open(txt,'w') as f:
    f.write(str(datetime.now()) + '\n')

while True:
    print("何か話してください")
    #音声認識開始
    with mic as source:
        r.adjust_for_ambient_noise(source) #雑音対策
        audio = r.listen(source)
    print("おまちください")
    
    try:
        print(r.recognize_google(audio, language='ja-JP'))
         #ストップというとストップする
        if r.recognize_google(audio, language='ja-JP') == "ストップ" :
                print("終了します")
                break

        with open(txt,'a') as f: #ファイルの末尾に追記していく
            f.write("\n" + r.recognize_google(audio, language='ja-JP'))


       
    except sr.UnknownValueError:
        print("聞き取れませんでした")
    