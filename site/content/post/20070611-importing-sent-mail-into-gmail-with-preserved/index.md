+++
title = "Importing Sent Mail Into Gmail With Preserved Dates"
date = "2007-06-11T04:51:00Z"
tags = ['Code']
categories = ['Technology']
+++

There are many sites out there dedicated to importing your email into gmail,
this is not meant to be another. This little page is here to document the
method that I used specifically to import sent mail into my gmail account with
the correct date and have it show up in the sent mail section.

I used Mark Lyon's [Gmail Loader](http://www.marklyon.org/gmail/) on OS X
([Mac specific
instructions](http://paskal.net/gmail_loader_instructions_for_mac_os_x/)).
Gmail loader just reads mbox files, parses them and sends them to you gmail
account. When the mbox file is a sent mail folder, then it also sets the from
address to be the gmail address you are sending to.

One catch is that the mail will be time stamped with the current time on
google's servers rather than the time that the message was sent/received. A
trick to get around this is to use a third gmail account. Use Gmail Loader to
send all mail to a temporary gmail account, then setup your main account to
pull mail from the temporary gmail account. When it pulls the mail it will
correctly set the date and time.

This is where I ran into a problem. If I import sent mail to
[temp@gmail.com](mailto:temp@gmail.com), it works fine in the context of
[temp@gmail.com](mailto:temp@gmail.com). But as soon as it gets transferred to
my real Gmail account it no longer is from me, but from
[temp@gmail.com](mailto:temp@gmail.com). To get around this I simply edited
the Gmail Loader python script. At the point where it sets the from field to
be the destination gmail account (i.e.
[temp@gmail.com](mailto:temp@gmail.com)), I hardcoded it to be my real gmail
account. For me this is at line 302:

> 

>

>  if self.rcvorsn.get() == self.rcvtyps[1]:

>

>   fullmsg = re.sub(r'From: .*', 'From: [my-real-
email@gmail.com](mailto:my-real-email@gmail.com)',         
     self.msg.__str__( ) + '\x0a' + self.document, 1 )

>

>   server.sendmail(self.recipnt.get(), self.recipnt.get(), fullmsg)

>

>  else:

>

>   fullmsg = self.msg.__str__( ) + '\x0a' + self.document

>

>   server.sendmail(self.msg.getaddr('From')[1], self.recipnt.get(),
fullmsg)

>

> 

