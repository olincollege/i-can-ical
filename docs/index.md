
# About I Can iCal
## An interactive automated calendar creator
### Brought to you by Isha Goyal, Malvina Clavering, and Phillip Post

Have you ever been frustrated by the process of receiving an email about an event and a time, say "Tuesday at 1pm", then having to manually copy all that information into your Outlook calendar at risk of misremembering? Was it Tuesday or Thursday? Why can't people just send an ical? Well now you no longer need to preach the wondrous convenience of ical invites to all these senders of emails, you can just request one from our magical assistant. The I Can iCal program can read through any email and extract the date and time for an event, and will then automatically send you an ical with the correct information. All you need to do is open the .ics attachment to add it to your calendar. No tedious copying necessary!

# Setup

See also: [project README](https://github.com/olincollege/i-can-ical/blob/main/README.md)

### Create Bot Email Account
To begin using I Can iCal, you first need to set up a way for the program to send you emails. This project uses a gmail account that allows less secure app access. If you don't have the password to youcanical@gmail.com, which is the account we used, you will need to create your own email account for the bot to listen on. We will assume this is a gmail account for these instructions. Once you have created your gmail account, go to the account settings, navigate to __security__, then __turn on less secure app access__. Remember your username and password or store them in a secure place. A warning: this process makes your account more vulnerable, we do not recommend using a personal account as your bot account.

### Install Dateparser
The program uses the datetparser package to extract dates and times from natural language. To install dateparser, use the following command:
```
pip install dateparser
```
You will also need the email library:
```
pip install email
```
To create ical files, you will also need the icalendar library:
```
pip install icalendar
```
All other packages are from the python standard library and are ready to use. You can now begin generating ical files for yourself or any user with the email address for the bot.

# Running the Program
Once you have dowloaded the code, run the icanical_main.py from a terminal. The program is now listening to the inbox you created and will send an ical for any new email that appears. To use this program to automatically generate an ical, simply send or forward any email containing a text that has a meeting time in either the body or the subject line. You should receive a reply with an ical attachment, you will also see a printed output with "ical invite sent" if everything worked properly. If the date and time cannot be detected, you will receive an email saying "iCal could not be created."
### Step 1: Run the Main Program in Terminal
__You will be prompted to log in__
![](assets/run_main.png)
### Step 2: Send Email to Bot
__You can send your own email or forward one from your inbox__
![](assets/Screenshot 2022-05-08 162935.png)
### Step 3: Receive iCal Attachment
__Just open the attachment to add it to your calendar__
![](assets/Screenshot 2022-05-08 163057.png)

# Assumptions and Limitations

While I Can iCal has a fairly robust logic that will capture most dates and times, there are a few limitations and key assumptions. Remember that the program will not work if there is no time detected, so a message with only a date will not be enough. If no date is given, the default date is today. The program also defaults to pm if no am or pm marker is detected; for a range of times, the later time will default to pm and the earlier time will got to am or pm based on if the numerical value is greater than or less than the second time. Another important assumption is that all dates will be set to the current year, so note that creating event times around new years may result in an inaccurate date. You can specify relative times in the text, such as "today" or "tomorrow", but weekdays without a date will not be accurately captured.

Another limitation is that you need to create an account or have the login credentials to an existing account set up for this purpose, which requires some additional work at setup meaning the program is not super easily transferrable. It is also important to note that the program needs to be running for it to work, so anytime you want to use this tool, you need to make sure you start up the program in terminal or have it running constantly.

# Video
See a more in-depth description of the project [here](https://youtu.be/yIs8783s6K0)
