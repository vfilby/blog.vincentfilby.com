+++
title = "Convert Audible Files to mp3"
date = "2005-11-15T23:09:00Z"
tags = []
galleryprefix = ""
gallerythumbnailprefix = "t190_"
+++

> **Update April 13th, 2007**  
>  Many people have been asking for the old version of Goldwave as an
alternative for converting audible files. You can easily find this file by
doing a Google search for gwave506.exe will turn up some download sites that
still have 5.06 mirrored.

Audible is a great service and they have a nice format that is flexible, but
sometimes it just isn't flexible enough. I have an mp3 player in my truck that
I wanted to use, doesn't support .aa or drm for that matter. I certainly
didn't want to burn them to however many cd's it would take, so I started
scouring the web for ways to convert this file to a usable format. Most of the
sites I found recommended playing the book and recording the stream, then
compress that to mp3. This is a silly idea and is wholely uesless to me, work
though it may. I did, however, find instructions to convert .aa using
dbpoweramp on a forum that I can no longer find. To preserve these
instructions I will post them here as well.

  1. Install dbpoweramps DirectShow codec: <http://www.dbpoweramp.com/codecs/dBpowerAMP-codec-DirectShowDecoder.exe>
  2. Install AudibleManager AND Windows Media Player Filter (bottom of download page): <http://www.audible.com/software>
  3. Set DirectShow to know about Audible file types: Start &gt;&gt; Programs &gt;&gt; dbpoweramp Music Converter &gt;&gt; Configure DirectShow Decoder at the end of this text file type (on a new line): ` .aa ` Save the file (File &gt;&gt; Save)
  4. Run dBpowerAMP Configuration: Start &gt;&gt; Programs &gt;&gt; dBpowerAMP Music Converter &gt;&gt; Configuration &gt;&gt; dMC Configuration That is it, dbpoweramp can read audible files and Sveta Portable audio can upload Audible files to portables that support it.

