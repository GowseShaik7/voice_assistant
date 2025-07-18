import speech_recognition as sr
import pyttsx3
import pyaudio

# Text to Speech Engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech Recognizer
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("🎤 Speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("⏳ Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {command}")
        return command
    except sr.UnknownValueError:
        print("😅 Sorry, I didn't understand.")
        return ""
    except sr.RequestError:
        print("❌ Network Error")
        return ""

# Main Logic
if __name__ == "__main__":
    speak("Hi! I am your assistant. What can I do for you?")
    while True:
        query = listen().lower()

        if 'hello' in query:
            speak("Hello! How can I help you?")
        elif 'your name' in query:
            speak("I am your personal assistant.")
        elif 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a nice day.")
            break
        elif query != "":
            speak("You said " + query)
