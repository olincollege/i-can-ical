
# i-can-ical
## An interactive automated calendar creator
### Brought to you by Isha Goyal, Malvina Clavering, and Philip Post

Have you ever been frustrated by the process of receiving an email about an event and a time, say "Tuesday at 1pm", then having to manually copy all that information into your Outlook calendar at risk of misremembering? Was it Tuesday or Thursday? Why can't people just send an ical? Well now you no longer need to preach the wondrous convenience of ical invites to all these senders of emails, you can just request one from our magical assistant. The i-can-ical program can read through any email and extract the date and time for an event, and will then automatically send you an ical with the correct information. All you need to do is hit accept to add it to your calendar. No tedious copying necessary!

# Setup

See also: (project README)[https://github.com/olincollege/i-can-ical/blob/main/README.md]

### Create Bot Email Account
To begin using i-can-ical, you first need to set up a way for the program to send you emails. This project uses a gmail account that allows less secure app access. If you don't have the password to youcanical@gmail.com, which is the account we used, you will need to create your own email account for the bot to listen on. We will assume this is a gmail account for these instructions. Once you have created your gmail account, go to the account settings, navigate to __security__, then __turn on less secure app access__. Remember your username and password or store them in a secure place.

### Install Dateparser
The program uses the datetparser package to extract dates and times from natural language. To install dateparser, use the following command:
```
pip install dateparser
```
All other packages are from the python standard library and are ready to use. You can now begin generating ical files for yourself or any user with the email address for the bot.

# Running the Program
Once you have dowloaded the code, run the icanical_main.py from a terminal. The program is now listening to the inbox you created and will send an ical for any new email that appears. To use this program to automatically generate an ical, simply send or forward any email containing a text that has a meeting time in either the body or the subject line.

# Assumptions and Limitations

While i-can-ical has a fairly robust parsing logic that will capture most dates and times, there are a few limitations and key assumptions. Remember that the 
