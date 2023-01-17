# converter .pdf in .docx (Documento Word)

# Requires: pip install aspose-words

#import api
import aspose.words as aw

# load the PDF file
doc = aw.Document("exemplo01.pdf")

# convert PDF to Word DOCX format
doc.save("pdf-to-word.docx")