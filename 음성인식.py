# -*- coding: utf-8 -*-
"""음성인식.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uQWKnitvCvdnhv1qSILGDfNvOmn820a2

# 녹음파일 인식
"""

!pip install SpeechRecognition

import speech_recognition as sr
sr.__version__


r = sr.Recognizer()

harvard = sr.AudioFile('test11.wav')

with harvard as source:
    audio = r.record(source)

type(audio)

r.recognize_google(audio, language='ko-KR')

!gh repo clone 2023-Sju-Capstone-Team4/Speech-to-Text