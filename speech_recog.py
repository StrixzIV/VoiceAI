import speech_recognition as sr
import webbrowser as wb
import random

recognizer = sr.Recognizer()

with sr.Microphone() as source:

    while True:

        print('กำลังฟัง...')

        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language = 'th')
            print(text)

            if text == 'ออกจากโปรแกรม' or text == 'หยุดการทำงาน':
                print('กำลังออกจากโปรแกรม...')
                exit()

            elif text.startswith('เล่นเพลง') or text.startswith('เปิดเพลง'):
                print('กำลังเปิดเพลงจากไฟล์ song.txt')

                with open('song.txt') as song:
                    songlist = song.readlines()
                    wb.open(songlist[random.randint(0, len(songlist) - 1)])           

        except sr.UnknownValueError:
            print('ไม่สามารถตรวจจับเสียงพูดได้ กรุณาลองใหม่อีกครั้ง')