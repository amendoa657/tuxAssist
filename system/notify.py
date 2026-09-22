import subprocess

ICONE = "/home/amendoa/IdeaProjects/TuxAssist/assets/tux.svg"


def notificar(mensagem, substituir=None):
    comando = ["notify-send", "-a", "Jarvis", "-i", ICONE, "-p"]

    if substituir:
        comando += ["-r", substituir]

    comando += ["Jarvis", mensagem]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    return resultado.stdout.strip()  # número da notificação