import webbrowser
import subprocess



def executar(texto):
    pass
    """Executa o comando. Devolve False se não for um comando."""
    texto = texto.lower()

    if "navegador" in texto:
        webbrowser.open("https://www.google.com")
    elif "terminal" in texto:
        subprocess.Popen(["ptyxis"])
    else:
        return False

    return True

def executar(comando):
    subprocess.Popen([comando])