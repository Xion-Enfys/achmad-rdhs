import speech_recognition as srec

def perintah():
    mendengar = srec.Recognizer()
    with srec.Microphone() as source:
        print('Mendengarkan')
        suara = mendengar.listen(source, phrase_time_limit=5)
        try:
            print('Diterima')
            dengar = mendengar.recognize_google(suara, language='id-ID')
            print(dengar)
        except:
            pass
        return dengar

def run_xion():
    Layanan = perintah()
    print(Layanan)

run_xion()