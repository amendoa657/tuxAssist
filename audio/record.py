import numpy as np

VOLUME_FALA = 300

def gravar(mic):
    """Espera você falar e grava até ficar 1 segundo em silêncio."""
    audio = []
    silencio = 0
    falou = False

    while silencio < 12:
        bloco, _ = mic.read(1280)
        audio.append(bloco[:, 0])

        if np.abs(bloco).mean() > VOLUME_FALA:
            falou = True
            silencio = 0
        elif falou:
            silencio += 1

    return np.concatenate(audio)