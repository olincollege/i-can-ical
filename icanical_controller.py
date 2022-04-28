"""
Controller for our python code. 

Gets input for the header, sender, and body from the user. Creates instance of
model. 
"""

sender = input('Input sender\'s name or email address')
header = input('Input header of event (or subject line of email).')
body = input('Input body text of email. Make sure it includes a date/time.')