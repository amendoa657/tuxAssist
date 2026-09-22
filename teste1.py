import speech_recognition as sr



reconhecedor = sr.Recognizer()

with sr.Microphone() as microfone:
    print("Fale um comando...")
    reconhecedor.adjust_for_ambient_noise(microfone)
    audio = reconhecedor.listen(microfone)

texto = reconhecedor.recognize_google(audio, language="pt-BR")
print("Você disse:", texto)

if "abrir navegador" in texto.lower():
    print("Executando comando para abrir o navegador...")