# GOATS AI

Assistente de voz local para Linux, construído em Python e pensado para o GNOME. O projeto, chamado **TuxAssist**, escuta a palavra de ativação **“hey jarvis”**, transcreve a fala em português, envia o pedido para um modelo de linguagem e pode executar ações no sistema.

> Projeto experimental em desenvolvimento. A execução de comandos ainda é simples e deve ser revisada antes de usar o assistente em uma máquina importante.

## O que ele faz

- Detecta a palavra de ativação com o modelo local `jasper.onnx`.
- Captura áudio do microfone com `sounddevice`.
- Detecta o fim da fala após um período de silêncio.
- Converte o áudio para WAV em memória.
- Transcreve o áudio em português com Whisper via Groq.
- Gera uma resposta estruturada em JSON usando um modelo da Groq.
- Exibe notificações no desktop com o ícone do Tux.
- Abre o Ptyxis ou o navegador quando o modelo retorna um comando compatível.

## Estrutura

```text
.
├── ai/
│   └── api.py              # Groq: transcrição e respostas
├── audio/
│   ├── record.py           # Captura e detecção de silêncio
│   └── wav.py              # Conversão do áudio para WAV
├── assets/
│   ├── tux.svg             # Ícone das notificações
│   └── tux.webp
├── system/
│   ├── commands.py         # Execução das ações do sistema
│   └── notify.py           # Notificações do GNOME
├── jasper.onnx             # Modelo local de wake word
├── main.py                 # Ponto de entrada
└── .env.example            # Modelo das variáveis de ambiente
```

## Requisitos

- Linux com microfone funcional.
- Python 3.10 ou mais recente.
- GNOME ou outro desktop com `notify-send`.
- Uma chave da API da Groq.
- PortAudio para o `sounddevice`.

No Arch Linux, CachyOS ou derivados:

```bash
sudo pacman -S --needed python portaudio libnotify
```

## Instalação

Clone o projeto e crie um ambiente virtual:

```bash
git clone https://github.com/amendoa657/tuxAssist.git
cd tuxAssist
python -m venv .venv
source .venv/bin/activate
```

Instale as dependências Python:

```bash
python -m pip install --upgrade pip
python -m pip install numpy sounddevice openwakeword groq python-dotenv
```

## Configuração

Crie o arquivo local de variáveis a partir do exemplo:

```bash
cp .env.example .env
```

Edite `.env` e informe sua chave da Groq:

```env
GROQ_API_KEY=sua-chave-da-groq
```

O arquivo `.env` é ignorado pelo Git e **não deve ser enviado ao GitHub**. O projeto também mantém `GEMINI_API_KEY` no exemplo por compatibilidade futura, mas o código atual usa a API da Groq.

## Como executar

Com o ambiente virtual ativado:

```bash
python main.py
```

Quando aparecer:

```text
Diga 'hey jarvis'...
```

diga a palavra de ativação. Depois do aviso **“Pode falar!”**, faça sua pergunta ou dê um comando em português.

Para sair, interrompa o processo com `Ctrl+C`.

## Comandos atuais

O módulo de sistema contém suporte experimental para:

- abrir o Ptyxis quando a resposta contém `terminal`;
- abrir o navegador quando a resposta contém `navegador`;
- executar o comando retornado pelo modelo.

Como a execução é controlada por resposta de modelo, não use o projeto com credenciais importantes ou dados sensíveis sem revisar e restringir `system/commands.py`.

## Solução de problemas

### Microfone não funciona

Verifique se o dispositivo aparece no sistema:

```bash
python -c "import sounddevice as sd; print(sd.query_devices())"
```

Confirme também as permissões e o dispositivo de entrada selecionado no GNOME.

### `PortAudio library not found`

Instale o pacote do sistema:

```bash
sudo pacman -S portaudio
```

### Notificações não aparecem

Confirme que `notify-send` está instalado:

```bash
command -v notify-send
```

No Arch Linux:

```bash
sudo pacman -S libnotify
```

### O modelo de wake word não é encontrado

Confirme que `jasper.onnx` está na raiz do projeto e execute o programa a partir dela:

```bash
cd /caminho/para/TuxAssist
python main.py
```

## Segurança

- Nunca versione `.env`, tokens ou chaves de API.
- Revogue imediatamente qualquer chave que tenha sido exposta em um commit ou log.
- Prefira uma lista explícita de comandos permitidos em vez de executar texto arbitrário retornado por um modelo.
- Revise as dependências e os comandos antes de instalar o projeto em outra máquina.

## Licença

Este repositório ainda não define uma licença. Até que uma licença seja adicionada, todos os direitos permanecem reservados ao autor.
