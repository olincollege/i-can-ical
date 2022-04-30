import PyPDF2

def email_to_text(path):
    """
    Extracts the text for the body, header, and sender from a pdf of an email.

    Args: 
        path: a string representing the path to the pdf version of the email. 

    Return: 
        A list of strings where the first is the sender, second is the subject
        line, and the third is the body of the email.
    """

    pdf = open(path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdf)

    text = pdfReader.getPage(0).extractText()
    pdf.close()

    text = ' '.join(text.replace('xa0', ' ').strip().split())
    text = text.encode(encoding='ascii')
    return text

print(email_to_text('test_emails/smoothie_event_carpe.pdf'))
