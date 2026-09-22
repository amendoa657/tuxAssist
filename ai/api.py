from groq import Groq
from dotenv import load_dotenv

from audio.wav import para_wav

load_dotenv()
groq = Groq()

def transcrever(audio):
    resultado = groq.audio.transcriptions.create(
        file=("audio.wav", para_wav(audio)),
        model="whisper-large-v3-turbo",
        language="pt",
    )
    return resultado.text.strip()


def perguntar(texto):
    resposta = groq.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": "Quero que sempre me retorne uma resposta em formato json, se eu pedir pra fazer algo que tenha relacao com abrir algum app, trocar de janela e etc... Voce vai adicionar no json 'comando' e a sua resposta no campo 'resposta', se nao exigir um comando apenas preencha o campo resposta. Eu uso um sistema archbased cachy os com gnome. Para executar apps voce pode apenas digitar o nome do app no terminal"},
            {"role": "user", "content": texto},
        ],
        reasoning_effort="low",
        max_tokens=300,
    )

    if(resposta):
        return resposta.choices[0].message.content
    else:
        return "{}"
