#shows text content inside a docx file
import docx

def getText(filename):
    doc=docx.Document(filename)
    fullText=[]
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText('c:\\users\\kerbo\\OneDrive\\Documents\\test.docx'))

