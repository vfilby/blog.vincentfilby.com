+++
title = "Syntax Highlighting for Drupal"
date = "2005-08-06T23:36:00Z"
tags = ['Drupal']
+++

**UPDATE: This is no longer maintained by me and can be found at <http://drupal.org/project/geshifilter>**



I am a comp sci student so I often post code on my website. I just happen to
use a wonderful CMS/blogger called [Drupal](http://www.drupal.org) that
supports filters and all kinds of other goodies. I wanted a filter that would
take anything posted in &lt;code&gt; tags and automagically apply syntax
highlighting.

## GeSHi and Codefilter

My solution was to take the existing codefilter module that drupal provides
and intergrate [GeSHi](http://qbnz.com/highlighter/) into it. All in all it is
very simple, you just have to install the codefilter patch and install genshi.
Then go to admin -&gt; settings -&gt; codefilter to configure and enable
genshi. Because it is extremely difficult to determine the language from a
code fragment you have to do it yourself. There is an option where a default
language can be configured. But I wanted to make sure that I could use this
for more than one language so I added some options to the &lt;code&gt; tag.
The have the code hightlighted in a language other than the default do this:

> &lt;code lang="html4strict"&gt;

>

> ...

>

> &lt;/code&gt;

If you want to turn it off temporarily do this:  

> &lt;code lang="html4strict"&gt;

>

> ...

>

> &lt;/code&gt;

The path can be downloaded below. There is an alternative coloring module
called [VIM color](http://www.bluefeet.net/vimcolor_module) which uses the
coloring schemes from vim. This is arguably more powerful and more tested
however it requries certain perl modules and access to perl which limits its
usefulness on windows. My module uses a php library called
[GeSHi](http://qbnz.com/highlighter/) so it will run where ever drupal is
running. In truth if I would have noticed vim color first I wouldn't have
bothered writing this, as it is I may change to it at some point in the
future.

## ``Supported Languages``

`` ``



Actionscript | ADA | Apache Log  
---|---|---  
AppleScript | ASM | ASP  
Bash | Blitz | Basic  
C | C for Macs | C#  
C++ | CAD DCL | CadLisp  
CSS | Delphi | DIV  
DOS | Eiffel | FreeBasic  
GML | HTML | Inno  
Java | Javascript | Lisp  
Lua | Microprocessor ASM | MySQL  
NSIS | Objective C | OCaml  
OpenOffice | BASIC | Oracle 8 SQL  
Pascal | Perl | PHP  
Python | Q(uick)BASIC | Ruby  
Scheme | SDL | Basic  
Smarty | SQL | VB.NET  
Visual BASIC | Visual Fox Pro | XML

