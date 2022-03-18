from gtts import gTTS

arquivo = open('arquivo.txt', 'r')

texto = arquivo.read()

arquivo.close()

linguagem= 'pt-br'

transcritor = gTTS(text=texto, lang=linguagem, slow=False)

transcritor.save("/audio.mp3")
