import openai
import pyttsx3
import speech_recognition as sr
import time

#API KEY
openai.api_key = "COPY PASTE YOUR API KEY HERE"

#GLOBAL VARIABLES
opening = True
phone_number = int(input("Welcome to AFTERLIFE. An AI which connects you to the spirit of the dead. Enter the phone number of the ghost you want to contact. The numbers are: \n "
                         "Steve Jobs - 101 \n "
                         "Dr Homi Bhabha - 102 \n "
                         "Rabindranath Tagore - 103 \n"
                         "Dr. Bhim Rao Babasaheb Ambedkar - 104 \n"
                         "Nelson Mandela - 105 \n"
                         "Winston Churchill - 106 \n"
                         "Netaji Subhash Chandra Bose - 107 \n"))

#SPEECH TO TEXT
engine = pyttsx3.init()

def audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print("SOME ERROR OCCOURED. TRYING AGAIN")

#PROMPTING FUNCTION
if phone_number == 101:
    def response(prompt):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt="Assume that you are the ghost of steve jobs. The reply must be in accordance with all the data you have about steve jobs as if steve jobs actual spirit is answering." + prompt,
            max_tokens = 4000,
            n=1,
            stop=None,
            temperature=1,
        )
        return response["choices"][0]["text"]
elif phone_number == 102:
    def response(prompt):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt="Assume that you are the ghost of Indian Nuclear Physicise, Dr Homi Jahangir Bhabha. The reply must be in accordance with all the data you have about Dr Homi Jahangir Bhabha as if Dr Homi Jahangir Bhabha's actual spirit is answering." + prompt,
            max_tokens = 4000,
            n=1,
            stop=None,
            temperature=1,
        )
        return response["choices"][0]["text"]
elif phone_number == 103:
    def response(prompt):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt="Assume that you are the ghost of Rabindranath Tagore. The reply must be in accordance with all the data you have about Rabindranath Tagore as if Rabindranath Tagore's actual spirit is answering." + prompt,
            max_tokens = 4000,
            n=1,
            stop=None,
            temperature=1,
        )
        return response["choices"][0]["text"]
elif phone_number == 104:
    def response(prompt):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt="Assume that you are the ghost of Dr. Bhim Rao Babasaheb Ambedkar. The reply must be in accordance with all the data you have about Dr. Bhim Rao Babasaheb Ambedkar as if Dr. Bhim Rao Babasaheb Ambedkar's actual spirit is answering." + prompt,
            max_tokens = 4000,
            n=1,
            stop=None,
            temperature=1,
        )
        return response["choices"][0]["text"]
elif phone_number == 105:
    def response(prompt):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt="Assume that you are the ghost of Nelson Mandela. The reply must be in accordance with all the data you have about Nelson Mandela as if Nelson Mandela's actual spirit is answering." + prompt,
            max_tokens = 4000,
            n=1,
            stop=None,
            temperature=1,
        )
        return response["choices"][0]["text"]
elif phone_number == 106:
    def response(prompt):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt="Assume that you are the ghost of Winston Churchill. The reply must be in accordance with all the data you have about Winston Churchill as if Winston Churchill's actual spirit is answering." + prompt,
            max_tokens = 4000,
            n=1,
            stop=None,
            temperature=1,
        )
        return response["choices"][0]["text"]
elif phone_number == 107:
    def response(prompt):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt="Assume that you are the ghost of Subhash Chandra Bose. The reply must be in accordance with all the data you have about Subhash Chandra Bose as if Subhash Chandra Bose's actual spirit is answering." + prompt,
            max_tokens = 4000,
            n=1,
            stop=None,
            temperature=1,
        )
        return response["choices"][0]["text"]
else:
    print("YOU SEEM TO HAVE DIALED A WRONG NUMBER. COULDN'T CONNECT WITH ANY GHOST")

#TEXT TO SPEECH
def text_to_audio(text):
    engine.say(text)
    engine.runAndWait()

#MAIN PROGRAM
def main():
    while True:
        print("Say Hello to interact with me")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "hello":
                    filename = "input.wav"
                    print("You may start speaking")
                    while opening == True:
                        with sr.Microphone() as source:
                            recognizer = sr.Recognizer()
                            source.pause_threshold = 1
                            audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                            with open(filename, "wb") as f:
                                f.write(audio.get_wav_data())

                        #AUDIO TO TEXT TRANSCRIPTION
                        text = audio_to_text(filename)
                        if text:
                            print(f"PROCESSING...")

                            #RESPONSE
                            answer = response(text)
                            print(f" Ghost Says:")
                            text_to_audio(answer)
            except Exception as e:
                print("An error has occoured: {}".format(e))

if __name__ == "__main__":
    main()













