import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Katakan sesuatu:")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio, language="id-ID")
    print("Anda mengatakan: " + text)
except sr.UnknownValueError:
    print("Tidak dapat memahami audio")
except sr.RequestError as e:
    print(f"Tidak dapat meminta hasil; {e}")
