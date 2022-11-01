import threading
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tkinter import Tk, Frame, Button, Label, ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

urlsReady=[]
urlsDone=[]
urls=[]
keywords_technology=[]
keywords_soccer=[]
common_words=[]
urlsDoneFR=[]

with open('urls.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    word=lines[i]
    if (len(word)>3):
        if (len(lines)-1==i):
            urls.append(word)
        else:
            urls.append(word[:-1])

with open('urls2.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    word=lines[i]
    urlsDone.append(word[:-1])

ary=[]
for i in range(len(urlsDone)):
    trigger=True
    if (urlsDone[i]=="Cant access this website" or urlsDone[i]=="Cant be determined"):
        ary.append(urlsDone[i])
        urlsDoneFR.append(ary)
        ary=[]
        trigger=False

    if (len(urlsDone[i])>25):
        if urlsDone[i][0]!="h" or urlsDone[i][1]!="t" or urlsDone[i][2]!="t" or urlsDone[i][3]!="p":
            palabra=urlsDone[i].split(',')
            ary.append(palabra)
            urlsDoneFR.append(ary)
            ary=[]
        else:
            if trigger:
                ary.append(urlsDone[i])
    else:
        if trigger:
            ary.append(urlsDone[i])


with open('keywords_technology.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    word=lines[i]
    if (len(lines)-1==i):
        keywords_technology.append(word)
    else:
        keywords_technology.append(word[:-1])


with open('keywords_soccer.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    word=lines[i]
    if (len(lines)-1==i):
        keywords_soccer.append(word)
    else:
        keywords_soccer.append(word[:-1])

with open('commonwords.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    word=lines[i]
    if (len(lines)-1==i):
        common_words.append(word)
    else:
        common_words.append(word[:-1])

totalKeyWords=len(keywords_soccer)+len(keywords_technology)
previousProbabilitySoccer=len(keywords_soccer)/totalKeyWords
previousProbabilityTechnology=len(keywords_technology)/totalKeyWords

def addToFile():
    for i in range(len(urlsReady)):
        for j in range(len(urlsReady[i])):
            f = open("urls2.txt", "a+")
            if j!=5:
                f.write(str(urlsReady[i][j]))
                f.write("\n")
            if j==5:
                for h in range(len(urlsReady[i][j])):
                    if urlsReady[i][j][h]!='':
                        f.write(urlsReady[i][j][h])
                        f.write(",")
                f.write("\n")
            f.close()
    exit()
def printUrls():
    ventana=Tk()
    ventana.geometry('780x505')
    ventana.wm_title("URLs result")
    ventana.minsize(width=655, height=505)
    frame=Frame(ventana,bg="gray")
    frame.grid(column=0,row=0,sticky='nsew')
    soccer=1
    technology=0
    not_found=0
    not_determined=0
    for i in range(len(urlsDoneFR)):
        if str(urlsDoneFR[i][2])=="Soccer":
            soccer+=1
        if str(urlsDoneFR[i][2]) == "Technology":
            technology+=1
        if str(urlsDoneFR[i][2]) == "Cant access this website":
            not_found+=1
        if str(urlsDoneFR[i][2]) == "Cant be determined":
            not_determined+=1

    titulos=["Technology","Soccer","Cant access this website","Cant be determined"]
    colors=["blue","red","yellow","green"]
    percentage=100/(soccer+technology+not_found+not_determined)
    soccer=soccer*percentage
    technology=technology*percentage
    not_found=not_found*percentage
    not_determined=not_determined*percentage
    tamano=[technology,soccer,not_found,not_determined]
    explotar=[0,0,0,0]

    fig,ax1=plt.subplots(dpi=100,facecolor='gray',figsize=(5,5))
    plt.title("URLs result", color="white", size="18", family="Arial")
    ax1.pie(tamano,explode=explotar,labels=titulos,colors=colors,
    autopct='%1.0f%%',pctdistance=0.6,
    shadow=True, startangle=60,radius=0.7,labeldistance=0.3)
    ax1.axis('equal')

    canvas=FigureCanvasTkAgg(fig,master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0,row=0,rowspan=3)

    urlsGUI=[]
    for i in urlsDoneFR:
        urlsGUI.append(i[1])


    cmb=ttk.Combobox(ventana,value=urlsGUI,width=40)
    lb1=Label(ventana,text="Select an URL")
    lb1.grid(row=0,column=0)
    lb1.place(x=500, y=0)
    cmb.grid(row=1,column=0)
    cmb.place(x=500, y=25)
    def showResults():
        urlsita=cmb.get()
        for i in range(len(urlsDoneFR)):
            if urlsita==urlsDoneFR[i][1]:
                if urlsDoneFR[i][2]=="Soccer" or urlsDoneFR[i][2]=="Technology":
                    keywords=urlsDoneFR[i][5]
                    topic=urlsDoneFR[i][2]
                    new_keywords=','.join(keywords)
                    messagebox.showinfo(message=topic+"\n"+"Technology :"+urlsDoneFR[i][3]+" Soccer: "+urlsDoneFR[i][4]+"\n"+new_keywords, title=urlsita)
                    return
                if urlsDoneFR[i][2]=="Cant access this website":
                    messagebox.showinfo(message="Cant access this website", title=urlsita)
                    return
                if urlsDoneFR[i][2]=="Cant be determined":
                    messagebox.showinfo(message="Cant be determined", title=urlsita)
                    return
    btn=Button(ventana,text="Ok",command=showResults)
    btn.grid(row=0,column=0)
    btn.place(x=500,y=50)
    ventana.mainloop()

def analyzeUrls(urlList,arrayLenght):
    for url in range(len(urlList)):
        usedWords=[]
        found=True
        text=""
        try:
            html = urlopen(urlList[url]).read()
            soup = BeautifulSoup(html, features="html.parser")
            for script in soup(["script", "style"]):
                script.extract()
            text = soup.get_text()
        except:
            print(url + 1 + arrayLenght)
            urlsReady.append([url+1+arrayLenght,urlList[url],"Cant access this website"])
            urlsDone.append([url + 1 + arrayLenght, urlList[url], "Cant access this website"])
            found=False

        if found:
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split(" "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            contadorsoccer=0
            contadortechnology=0
            words=text.split()
            for i in words:
                if len(i)>4:
                    if i.lower() not in usedWords:
                        usedWords.append(i.lower())
                        usedWords.append(1)
                    else:
                        for j in range(len(usedWords)):
                            if i.lower()==usedWords[j]:
                                usedWords[j+1]=usedWords[j+1]+1

            words_soccer=[]
            words_technology=[]

            for i in range(len(keywords_soccer)):
                if keywords_soccer[i] in text and keywords_soccer[i]!="":
                    contadorsoccer=contadorsoccer+1
                    words_soccer.append(keywords_soccer[i])

            for i in range(len(keywords_technology)):
               if keywords_technology[i] in text and keywords_technology[i]!="":
                    contadortechnology=contadortechnology+1
                    words_technology.append(keywords_technology[i])

            incidenceProbabilitySoccer=contadorsoccer/previousProbabilitySoccer
            incidenceProbabilityTechnology=contadortechnology/previousProbabilityTechnology
            probabilitySoccer=previousProbabilitySoccer*incidenceProbabilitySoccer
            probabilityTechnology=previousProbabilityTechnology*incidenceProbabilityTechnology

            if probabilityTechnology==probabilitySoccer:
                print(url + 1 + arrayLenght)
                urlsReady.append([url+1+arrayLenght,urlList[url], "Cant be determined",probabilityTechnology,probabilitySoccer])
                urlsDone.append([url + 1 + arrayLenght, urlList[url], "Cant be determined"])
                print(url)
            if probabilityTechnology>probabilitySoccer:
                print(url + 1 + arrayLenght)
                urlsReady.append([url+1+arrayLenght,urlList[url], "Technology",probabilityTechnology,probabilitySoccer,words_technology])
                urlsDone.append([url + 1 + arrayLenght, urlList[url], "Technology", probabilityTechnology, probabilitySoccer, words_technology])
                print(url)
                for i in range(len(usedWords)):
                    if i%2!=0:
                        if usedWords[i]>=20:
                            wordd=usedWords[i-1]
                            if len(wordd)>3:
                                if wordd not in keywords_technology and wordd not in common_words:
                                    try:
                                        f = open("keywords_technology.txt", "a+")
                                        f.write("\n")
                                        f.write(wordd)
                                        f.close()
                                        keywords_technology.append(wordd)
                                    except:
                                        print("Error")

            if probabilityTechnology < probabilitySoccer:
                urlsReady.append([url+1+arrayLenght,urlList[url], "Soccer",probabilityTechnology,probabilitySoccer,words_soccer])
                urlsDone.append([url+1+arrayLenght,urlList[url], "Soccer",probabilityTechnology,probabilitySoccer,words_soccer])
                print(url)
                print(url+1+arrayLenght)
                for i in range(len(usedWords)):
                    if i%2!=0:
                        if usedWords[i]>=20:
                            wordd=usedWords[i-1]
                            if len(wordd) > 3:
                                if wordd not in keywords_soccer and wordd not in common_words:
                                    try:
                                        f = open("keywords_soccer.txt", "a+")
                                        f.write("\n")
                                        f.write(wordd)
                                        f.close()
                                        keywords_soccer.append(wordd)
                                    except:
                                        print("Error")
        if (url+1==400):
            addToFile()
        if len(urlsReady)==7900:
            print("Done analyzing data, building GUI...")
            printUrls()


def main():
    url1=urls[0:1975]
    url2=urls[1975:3950]
    url3=urls[3950:5925]
    url4=urls[5925:]
    thread1=threading.Thread(target=analyzeUrls, args=(url1,0))
    thread2=threading.Thread(target=analyzeUrls, args=(url2,1975))
    thread3=threading.Thread(target=analyzeUrls, args=(url3,3950))
    thread4=threading.Thread(target=analyzeUrls, args=(url4,5925))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()


main()