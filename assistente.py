import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import pywhatkit as kit

# confirgurações iniciais

engine = pyttsx3.init()
engine.setProperty('rate', 170)

wikipedia.set_lang("pt")

def falar(texto):
    print("Assistente:", texto)
    engine.say(texto)
    engine.runAndWait()


# ouvir usuário

def ouvir():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ouvindo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        comando = recognizer.recognize_google(audio, language="pt-BR")
        print("Você disse:", comando)
        return comando.lower()

    except:
        falar("Não entendi, pode repetir?")
        return ""

# funções de assistente

def pesquisar_wikipedia(termo):
    try:
        resumo = wikipedia.summary(termo, sentences=2)
        falar(resumo)
    except:
        falar("Não encontrei resultados.")

def abrir_youtube():
    falar("Abrindo Youtube")
    webbrowser.open("https://www.youtube.com")

def tocar_musica(musica):
    falar(f"Tocando {musica}")
    kit.playonyt(musica)

def farmacia_proxima():
    falar("Mostrando farmácias próximas")
    webbrowser.open("https://www.google.com/maps/search/farmácia+próxima")

# loop principal

def iniciar_assistente():
    falar("Olá! Assistente virtual iniciado.")

    while True:
        comando = ouvir()

        if "wikipedia" in comando:
            falar("O que deseja pesquisar?")
            termo = ouvir()
            pesquisar_wikipedia(termo)

        elif "youtube" in comando:
            abrir_youtube()

        elif "toque" in comando:
            musica = comando.replace("toque", "")
            tocar_musica(musica)

        elif "farmácia" in comando:
            farmacia_proxima()

        elif "sair" in comando or "encerrar" in comando:
            falar("Encerrando assistente. Até logo!")
            break

        elif comando != "":
            falar("Comando não reconhecido.")

# iniciar

iniciar_assistente()
