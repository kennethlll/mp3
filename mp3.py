import pyttsx3 as tts, PyPDF2
pdfreader = PyPDF2.PdfReader("mp3/sample.pdf")
speaker = tts.init()
book = str()
for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
    #book += clean_text
speaker.say(clean_text)
speaker.save_to_file(clean_text, 'test.mp3')
speaker.runAndWait()
