Title: Half Time: What's up at Trojitá
Date: 01-07-2014
Category: Tech
Tags: c++, gsoc, trojita, kde, foss
Slug: half-time-whats-up-at-trojita
Author: Karan Luthra
Summary: Second half has just begun for the GSoC coding period as well as for the year 2014. We are all more warmed up and pacing up to see another "you will be glued to the second half", but let's take a look at what has kept me involved in Trojitá uptil now. My project proposal is to rewrite Trojitá's SMTP code to enable it to use Trojitá's Sockets, and make it a first class citizen wrt the code quality, robustness, maintainabilty, and features. Another goal is to bring essential features and UI changes that will make Trojitá more usable and ready for a larger user-base

Second half has just begun for the GSoC coding period as well as for the year 2014. We are all more warmed up and pacing up to see another "you will be glued to the second half", but let's take a look at what has kept me involved in Trojitá uptil now. My [project proposal](http://www.google-melange.com/gsoc/project/details/google/gsoc2014/luthrak/5685265389584384) for [Trojitá](http://trojita.flaska.net/) is to:  

* Rewrite Trojitá's SMTP code to enable it to use Trojitá's Sockets, and make it a first class citizen wrt the code quality, robustness, maintainabilty and features.  
* Bring essential features and UI changes that will make Trojitá more usable and ready for a larger user-base.  

Since the second goal consists of small tasks that would also help a newbie (me) get more comfortable with the code, me and my mentors decided to start with these small tasks first. This is what has been done uptil now:

1. Network Reconnection Attempts  
Trojitá got a feature to automatically start a reconnect attempt cycle whenever there's a network error.  
Previously, whenever the application was hit by a network error, it would switch to offline mode and inform the user by throwing an error message (which would be a modal message box). Now, a message box is still thrown the first time an error is faced and attempts for reconnect begin. To keep in line with Trojitá's prinicples of being less resource hungry and be usable for users with expensive mobile connections, any two reconnect attempts are separated with timeout that doubles every step. So, timeouts go like 5 secs, 10 secs,.. 160 secs, 300 secs (Inspired by the [Exponential Backoff](http://en.wikipedia.org/wiki/Exponential_backoff) algorithm I came across in Computer Networks class). And beyond that, attempts are made every 5 mins or manually stopped and restarted by the user. An unattended message box gets closed if network reconnects successfully. _Status: Merged in master_

2. Forwarding Support  
Trojitá already had the ability to treat whole messages dragged and dropped into the attachments view in a composer as messages to be forwarded as dot.eml files. In addition to that, trojitá now has a patch (under review atm) that would enable forward as attachment by a single click from the GUI. This includes mangling the subject of the original message and prefixing the "Fwd: " string, as well as marking the original message as $Forwarded. _Status: Under [review](https://git.reviewboard.kde.org/r/118606/)_

3. Improvements around Compose Widget  
	* One improvement is a bug fix that allows any changes to the subject field or the recipients fields to be treated as modifications eligible for storing in a draft. _Status: Merged in master_  
	* Another improvement is the ability to switch the reply mode { private reply, reply to all, reply to all but me, mailing list reply} from the composer as well (previously, a mode would be picked up at the time of creating the compose reply dialog and switching between modes wasn't possible unless a new dialog be opened). The change of mode triggers the automatic setting up of recipients in the current composer and modifying the recipients puts the reply mode in a fifth state, named "hand picked recipients". This patch is under [review](https://git.reviewboard.kde.org/r/118802/) and it is yet to be finalised _*where*_ in the compose window should this dropdown menu be placed.  
	* Another improvement (that won't be visible to the user) is a change in how a GUI::ComposeWidget is created. A compose widget needs a parent (MainWindow), an MSA(Mail Submissin Agent) object, a settings (QSettings) object and a couple of purpose specific parameters that can pre-fill the fields in the composer (eg: subject, body(quoted), in-reply-to, etc in the case of a "reply"). Due to increasing use-cases for the Compose Widget (Message Forwarding and Message Redirection are two such that are being added in this GSoC project), we felt the need to refactor the ComposeWidget and provide a static API for creating ComposeWidget instances with specific roles. It looks like this:  
	<script src="https://gist.github.com/karanluthra/37c3f65e229761002958.js"></script>
	[Gist](https://gist.github.com/karanluthra/37c3f65e229761002958#file-static-cw)

The second half has started off with shifting the focus onto the bigger task of rewriting the SMTP library. While writing this blog post I realised how it has become a long one to read, and I will try and write about whats up with SMTP more regularly, and hopefully as smaller posts. I find twitter to be a better output stream while in the code-sprint mood and you can follow me on Twitter, I am [@karanluthra06](https://twitter.com/karanluthra06). Best wishes to all GSoCers; Let's make this second half the most exciting ever!

Cheers! :)