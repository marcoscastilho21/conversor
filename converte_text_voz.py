#marcoscastilho21@hotmail.com

import pyttsx3

speaker = pyttsx3.init() #inicia serviço biblioteca
voices = speaker.getProperty('voices') #metodo de voz

#texto = "O Nicolas e legal"

f = open(r"C:\Users\Marcos\Documents\projetos\Conversor\text.txt", 'r', encoding="utf8")
texto = f.read()

for voice in voices:
    print(voice, voice.id) #traz os idiomas de voz instalados na maquina

speaker.setProperty('voice', voices[0].id) #define a voz padrao, no meu caso o portugues era o[0] (iniciando do zero)
rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate -25) #muda velocidade da leitura, quando menor mais lento

#print(texto) #escreve o texto na tela
speaker.say(texto) #define o texto que será lido
speaker.runAndWait() #le o texto
f.close() #fecha o modo deleitura do arquivo txt