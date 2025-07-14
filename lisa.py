import wikipedia
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import random as ra
import pywhatkit
import pyjokes

#setting the voice
engine =pyttsx3.init('sapi5')
v=engine.getProperty('voices')
#print(v[1].id)
engine.setProperty('voice',v[1].id)

#code to speak
def speak(querry):
    engine.say(querry)
    print(querry)
    engine.runAndWait()

#wishing the user
def wish():
    current=int(datetime.datetime.now().hour)
    if(current>=0 and current<12):
        speak("Good morning! sir ")
    elif(current>=12 and current<18):
        speak("Good afternoon! Sir")
    else:
        speak("Good night! Sir")
    print("hi i am lisa")

    speak("hi i am lisa,how may i help you")

#taking user command 
def takeCommand():
    r=sr.Recognizer()
    while True:
        with sr.Microphone() as mick:
            print('listening ...')
            querry=r.listen(mick)
            try:
                querry=r.recognize_google(querry,language='en-in')
                print(querry)
                return querry                
            except Exception as e:
                speak("can you say it again... please")

#action to be performed
def action(querry):

    #opening website
    if ("open" in querry and "website" in querry):
        querry=querry.replace('open ',"")
        querry=querry.replace(" website","")
        result=querry+".com"
        webbrowser.open(result)

    #opening folder by name
    elif("open"in querry and( "folder" in querry)):
        rootpath="D:/"
        speak("what is the name of the folder")
        folderName=takeCommand()
        for root,dirs,files in os.walk(rootpath):
            if(folderName in dirs):
                speak("folder found")
                path=os.path.join(root,folderName)
                #print(path)
                os.startfile(path)
                return
        speak("folder not found")

    #palying music
    elif ("play"in querry and ("songs"or "song" in querry or "music" in querry)):
        speak("palying...")
        path="D:\\projects\Lisa\music" #replace the path to the music folder
        songs=os.listdir(path)
        c=ra.choice(songs)
        os.startfile(os.path.join(path,c))
        print(c)

    #wikipedia search
    elif("tell me about " in querry):
        querry=querry.replace("tell me about","")
        result=wikipedia.summary(querry,sentences=5)
        speak(result)

    #telling current time or date
    elif(("tell me " in querry or "what is " in querry)and("present" in querry or "today's" in querry  or "current"in querry) ):
        if("time" in querry):
            speak("pesent time is ")
            t=datetime.datetime.now().time()
            speak(t)
            return
        if("date" in querry ):
            speak("present date is")
            t=datetime.datetime.now().date()
            speak(t)
            return
    #sending message in whatsapp
    elif(("send" in querry or  "whatsapp" in querry) and (" message"in querry)):
        speak("what is the message ")
        querry=takeCommand()
        t=str(datetime.datetime.now().time())
        
        s=t.split(":")
        phno="phone number" #replace the phone number to the person you want to send the message
        pywhatkit.sendwhatmsg(phno,querry,int(s[0]),int(s[1])+3)

    #telling jokes
    elif("tell" in querry and ("joke" in querry or "jokes" in querry)):
        myJoke=""
        speak("what type of joke tongue twister or normal")
        querry=takeCommand().lower()
        if("tongue twister" in querry):
            myJoke=pyjokes.get_joke(language='en', category="twister")
        elif("normal" in querry):
            myJoke=pyjokes.get_joke(language="en" , category="neutral")
        elif("any" in querry):
            myJoke=pyjokes.get_joke(language="en" , category="all")

        speak(myJoke)
    #if command is not present
    else :
        speak("that command is not present")
    
        
        
        
    
        
if __name__=="__main__":
    wish()
    while True:
        ToDo=takeCommand().lower()
        if ("stop" in ToDo or "exit" in ToDo):
            speak("I hope your day goes well ")
            speak("Thanks for using my services")
            break
        action(ToDo)

    
