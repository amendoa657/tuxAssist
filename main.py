import sounddevice as sd
import json

import openwakeword
from openwakeword.model import Model

from ai.api import transcrever, perguntar
from audio.record import gravar

from system.commands import executar
from system.notify import notificar

openwakeword.utils.download_models()
detector = Model(wakeword_models=["jasper.onnx"], inference_framework="onnx")



if __name__=="__main__":
    with sd.InputStream(samplerate=16000, channels=1, dtype="int16") as mic:
        print("Diga 'hey jarvis'...")

        while True:
            bloco, _ = mic.read(1280)

            if max(detector.predict(bloco[:, 0]).values()) > 0.5:
                detector.reset()
                print("Pode falar!")
                notificar("Pode falar!")

                texto = transcrever(gravar(mic))
                print("Você:", texto)

                #if not executar(texto):
                resposta = json.loads(perguntar(texto))
                if("resposta" in resposta):
                    print("Jarvis:", resposta["resposta"])
                    notificar(resposta["resposta"])
                if("comando" in resposta):
                    notificar(resposta["comando"])
                    executar(resposta["comando"])

                print("Diga 'hey jarvis'...")