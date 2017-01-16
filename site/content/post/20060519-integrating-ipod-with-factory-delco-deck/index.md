+++
title = "Integrating an iPod with a Factory Delco Deck"
date = "2006-10-12"
tags = []
description = "description" 
+++

Integrating an iPod with a Factory Delco Deck

So having an iPod is cool and having a ride is cool. Now it is supremely cool if they work well together. My stipulations here are:

Seemless audio integration with the radio. I don't care if the controls on the deck control the iPod
The iPod must use the line out from the iPod dock adapter
The iPod must be charging while plugged into the car
There must not be a mess of wires connecting everything to the iPod, ideally one dock adapter nothing more
I have a GM with an aftermarket panasonic deck. The deck works well and I have no problem with it except that it doesn't have an aux in and it is too old to support iPod connectors.

Now--for those of you who are about to scream FM transmitter just shut up and sit back down. I don't want an FM transmitter because I have heard many horror stories or poor audio quality, signal dropping and having to change radio stations when driving around. More importantly though I do not want a mess of wires (see above!) that i would get from having an FM transmitter and a car adapter to charge.

So barring the FM option I starting looking into my options. The panasonic has a CD changer input on the back, but it is only enabled when there is a cd changer there. Since I don't have one I looked around on the net for hacks and found the panasonic cdchanger emulator (http://www.lafrog.com/cdcemu/). However when it arrived it didn't work as expected, actually it didn't work at all. The maker offered to refund the money if I shipped it back but I would like to reprogram the PIC to try a few things first. I don't have an in-circuit pic programmer and I don't really have time to build one now so I am going to shelve this options for the time being. Keep in mind though that this is only a temporary solution until I get my aftermarket deck working.

### Hacking the Delco

I had a long trip up to Manitoulin island and back and I definitely wanted to iPod to work for that trip so I pulled out my old factory deck, a beastly old delco jobby. Unlike my panasonic, however, the delco was made with non-surface mount components and solid connectors that I can hack away at. [I am adept at soldering, but I am scared of anything surface mount.]

So my old delco has an AM/FM radio and a cassette deck but no aux inputs. I thought to myself, who the heck actually uses cassette decks anymore. Since I am the principle user and I answered 'not me', I saw fit to begin my investigation there.

The first thing I looked at was the outputs from the magnetic head reader. Following these inputs on the circuit board, they lead directly to a Toshiba 2025p preamplifier IC. Looking up the specs I quickly found the outputs from the preamp and followed them through the cassete subsystem.

![]({{< localresource "149066950_7ceaa54b44.jpg" >}})

Cassette head and preamp IC

The cassette deck subsystem is connected to the main deck by 10 wires. These wires convey audio information and information to from the deck controls. The two outputs from the preamp also go through this connector. This is the point where I decided to hack my ipod connector in. As a test I let the deck play a cassette while I cut the two wires, allowing me to verify that a) the sound disappered when the wires were cut, and b) which was left and which was right.

Now that I had two inputs I took a small 3.5mm (headphone jack) extension and wired that in. By the end I had a small auxillary jack at the back of my stereo. This accomplished one of my goals. I could not play music from my iPod through my car stereo via the *new* aux connector on the back.

Now there is something funny to be said about this method. I haven't bothered to figure out how the circuit passes control to the tape deck yet, so if you want to listen to the iPod you have to pop a tape in. I think it is kinda funny personally so I will probably leave it that way. I doubt I'll put any more effort into it considering this is really just a stop gap until I get my aftermarket deck working with my iPod.

### Charging and Using the iPod's Line Out

So far I have no more than a few dollars and an hour's time invested in this project. Unfortunately you can't build a dock connector so I had to buy one. I bought a belkin autokit off ebay for around $20. This is a cigarette lighter adapter that charges the iPod and provides a line out. Perfect for what I wanted and it is black so it blends in well with my truck interior.

![]({{< localresource "149066968_94c29b1ccf.jpg" >}})

Belkin AutoKit properly shelled (It is so nice of them to label their PCB so clearly!)

![]({{< localresource "149066974_d4ff260cf3.jpg" >}})

Belkin AutoKit wired into the 12v inswitched feed

So now my task is to hook the belkin autokit into the wiring harness behind my deck. The audio out is the easy task, the belkin adapter has a built in line out with preamp so I can adjust the iPod's volume to match the FM stereo's volume. All I had to do was use a short male-male adapter to plug it into my *new* aux in.

The power source was also fairly easy. cigarette lighters run on 12v (give or take ;-) ) and there is a 12v unswitched lead on the car audio wiring harness. So I simply connected the 12v feed to the 12v in on the belkin adapter, taking care to put a 2amp fuse inline to prevent damage.

Once all the wiring was completed I simply placed the autokit circuit and an extra wires in an old static protection bag and tucked them away behind the deck. The belkin dock connector I fed behind the dash and under in a small storage area in the dash, perfect for an iPod!

### The end

So that is all there is to it. I now have a a single black dock connector in a storage space in the dash. I just plug my iPod in (with the required cassette tape!), and it plays and charges like is was meant to be there.
