# HackTheMountains3.O

In the pandemic, online classes were life saver for students and people who are learning were able
to continue their studies just because of meeting platforms like zoom, meet, teams etc. . But theirs
the thing we all faced during online classes or meetings, &#39;Online Class Raiding&#39; or &#39;Class Bombing’. If
you don’t know what this is, then let us just quickly tell you. In online Bombing people used to come
and join these sessions with fake identity. Just because they know they can’t be traced and when the
host was letting them in, they used to play sounds and videos which they are not supposed to be
played on these types of academic sessions or webinars. So here is what we can do, we created a
our own application &quot;STAY ON ALERT &quot; in the form of a GUI which is automating a zoom meeting app
or any another platform. In this app teachers don&#39;t have to share the meeting link as our application
is directly automating the current meeting for the students , only authorized users will be able to
join the meeting. This application will allow us to create a bridge between student and meeting
platforms landing page we are able to trace the traffic of the users who are attempting to join the
class. While they are joining, we are collecting machine name, serial no, mac ,Ip location, name,
mail-id, profile etc of the participants and storing it in a database(MySQL Workbench).
Here we are also giving the other features to tighten the security,

i) Camera recording: If someone misbehave by opening their cameras then the recording
will be saved in folder and teacher will be able to authenticate whether the student is
from the class or some outsider.

ii) Audio recording: If someone is using the desktop and don’t have the cameras for that
we have the audio recording option also and our application will be able to authenticate
whether the student is the authorized person or not.

iii) Chat: Messages (which are usually disturbing and offensive) need to be blocked in such
a way that they are not shown in the chat box or displayed during the session.
Python libraries of Profanity are used along side pyautogui.
A profanity filter will scan user-generated content (UGC) to filter out profanity words
such as swear words, words associated with hate speech, harassment, etc.
Tracing IP address using Wireshark: From our database we can trace the Ip address of
the unauthorized user and can traces his details, and the application will be able to block
it. If the Ip address is changed dynamically, we are also storing the MAC details of the
user and block his device.

#contributed  by sania, neha and chetna 
