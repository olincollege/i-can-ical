<h1 align="center"style="color:#3275a8">I Can iCal Code Guide</h1>

Welcome to I Can iCal! This is a python project that aims to remove the hassle of converting dates from emails into events in your calendar. When running, I Can iCal acts as an email bot that receives any email and returns an iCal event created based on context from the email body and header. For security reasons, I Can iCal requires you provide your own email address to act as a bot.

---

<h2 style="color:#3275a8"> Libraries </h2>
To get started we need to need to download the libraries for I Can iCal. Below is a short description of each library along with the code needed to install it in linux terminal. Each name in <b style="color:#942b2b"> red </b> is hyperlinked to further documentation on the package.
<br/><br/>
<a href = "https://dateparser.readthedocs.io/en/latest/" style="color:#942b2b; font-size:1.25em;" > Dateparser </a>

Dateparser provides the <i>parse</i> function which allows us to convert most simple strings that contain a date or time into a datetime datatype.

    pip install dateparser

<a href = "https://icalendar.readthedocs.io/en/latest/usage.html" style="color:#942b2b; font-size:1.25em;" > icalendar </a>

icalendar allows us to provide a start time, end time, and other event details to receive an ical file to email.

    pip install icalendar

<a href = "https://docs.python.org/3/library/email.html" style="color:#942b2b; font-size:1.25em;" > email </a>

Email creates an email type datatype that allows us to easily parse through received emails as well as send our own.

    pip install email

---

<h2 style="color:#3275a8"> Overview </h2>

This section will provide a overview of how this code works. The diagram below illustrates the relationship between the main functions and classes within I Can iCal.
<br/><br/>

![overall code diagram](/images/code.png)

<br/><br/>

To run the overall code one simply has to type:

    python icanical_main.py

But lets take a closer look at what is happening under the hood. As you can see, the main function is what connects the everything with the help of the model, which stores all of the data between the two classes. Main will prompt the user for an email address and password to create an email bot, facilitating all of the interactions to follow.

The <b style="color:#3275a8"> controller </b> class is what handles everything that involves receiving an email, decoding its contents, and figuring out what times or dates are located in the email, if any. If at least a time is found, then the controller sends it to the main where it is stored along with the end time and email header in the model.

Now that these details are in the model, the <b style="color:#3275a8"> view </b> class is what handles creating an iCal file from them. Once this file is created, it then attaches it to an email that is sent to the user, which emailed the email bot.

The main function assures that all of this happens in an infinite loop so it never stops unless the user terminates the code. Main will also send an error email to whoever emails the bot when an error does occur in the code.

---

<h2 style="color:#3275a8"> Attributes and License </h2>

This code was written by Isha Goyal, Malvina Clavering, and Phillip Post. All are students at Olin college of engineering class of 2025. This code is under an Attribution-NonCommercial (CC BY-NC) license.


