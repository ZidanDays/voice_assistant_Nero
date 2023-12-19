import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib

print("Initializing Nero")

MASTER = "Master"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

# speak
def speak(text):
    engine.say(text)
    engine.runAndWait()
    

# Fungsi takeUserInput untuk mengambil input dari pengguna
def takeUserInput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-US")
        print(f"User said: {query}\n")
        return query.lower()
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Fungsi searchOnGoogle untuk mencari kata kunci di Google
def searchOnGoogle():
    speak("What would you like to search for on Google?")
    search_query = takeUserInput()
    
    if search_query:
        search_url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(search_url)

# function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning " + MASTER)
    elif 12 <= hour < 18:
        speak("Good Afternoon " + MASTER)
    else:
        speak("Good Evening " + MASTER)
        speak("")

def takeCommand():
    # main starts here
    speak("Hello, I'm a personal assistant NEIRO. May I help you?")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print(f"user said: {query}\n")



        if "wikipedia" in query.lower():
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
        elif "open youtube" in query.lower():
            url = "https://www.youtube.com/"
            webbrowser.open(url)
        elif "open google" in query.lower():
            url = "https://www.google.com/"
            webbrowser.open(url)
        elif "what's the time" in query.lower() or "current time" in query.lower():
            current_time = datetime.datetime.now().strftime("%H:%M")
            print(current_time)
            speak(f"The current time is {current_time}")
        elif "open notepad" in query.lower():
            os.system("notepad.exe")
            # ...

        elif "open calculator" in query.lower():
            os.system("calc.exe")

        elif "search on Google" in query.lower():
            searchOnGoogle()

        elif "tell a joke" in query.lower():
            joke = "Why don't scientists trust atoms? Because they make up everything!"
            speak(joke)

        elif "play music" in query.lower():
            music_folder = "C:\\Path\\To\\Your\\Music\\Folder"
            music_files = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
            if music_files:
                selected_music = random.choice(music_files)
                os.system(os.path.join(music_folder, selected_music))
            else:
                speak("No music files found.")

        elif "how are you" in query.lower():
            speak("I'm just a computer program, but I'm doing well. Thank you for asking!")
            
            # ...

        elif "send email" in query.lower():
            speak("Who is the recipient?")
            recipient = takeUserInput()
            speak("What is the subject of the email?")
            subject = takeUserInput()
            speak("What should I say in the email?")
            body = takeUserInput()
            send_email(recipient, subject, body)  # Tentukan fungsi send_email sesuai kebutuhan

        elif "weather" in query.lower():
            speak("Which city's weather would you like to know?")
            city = takeUserInput()
            get_weather(city)  # Tentukan fungsi get_weather sesuai kebutuhan

        elif "tell me a fact" in query.lower():
            fact = "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible."
            speak(fact)

        elif "shutdown" in query.lower():
            speak("Are you sure you want to shutdown your computer?")
            confirmation = takeUserInput()
            if "yes" in confirmation.lower():
                os.system("shutdown /s /t 1")
            else:
                speak("Shutdown canceled.")

        elif "restart" in query.lower():
            speak("Are you sure you want to restart your computer?")
            confirmation = takeUserInput()
            if "yes" in confirmation.lower():
                os.system("shutdown /r /t 1")
            else:
                speak("Restart canceled.")
                
                
        elif "open file explorer" in query.lower():
            os.system("explorer")

        elif "open command prompt" in query.lower():
            os.system("cmd")

        elif "play a joke" in query.lower():
            speak("Why did the computer go to therapy? It had too many bytes of emotional baggage!")

        elif "tell me a riddle" in query.lower():
            riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"
            speak(riddle)

        elif "set a reminder" in query.lower():
            speak("What should I remind you about?")
            reminder = takeUserInput()
            speak("When should I remind you?")
            reminder_time = takeUserInput()
            set_reminder(reminder, reminder_time)  # Definisikan fungsi set_reminder sesuai kebutuhan

        elif "stop" in query.lower():
            speak("Goodbye!")
            exit()


    except Exception as e:
        print("Say that again, please...")
        query = None

# Call the wishMe function
wishMe()

# Call the takeCommand function
takeCommand()