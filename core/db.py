import PyPDF2

reader = PyPDF2.PdfReader(r"C:\Users\ponak\JurisAI\data\31-1959___jonew__judis__62.pdf")
text = " ".join([t.extract_text() for t in reader.pages])
print(text)