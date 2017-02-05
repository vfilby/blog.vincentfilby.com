+++
title = "Enhanced NEdit"
desrcription = "This is a snapshot of the nedit 5.2 cvs tree that I have added export functionality to.  For the moment it can only export to color HTML but color postscript might be added as well."
date = "2001-08-06"
tags = ["C", "Programming","Nedit"]
categories = ["Programming"]
+++

This is a snapshot of the nedit 5.2 cvs tree that I have added export functionality to.  For the moment it can only export to color HTML but color postscript might be added as well.

You can download a copy of my nedit [here]({{< localresource "vnedit-5.2-DEV.tar.gz" >}}) or from [github](https://github.com/vfilby/NEdit-Export)

If you want to download the original nedit or find out more information about it, go to http://www.nedit.org

#### Wish List
* Line Numbering
* Controlling Tab behaviour
* Much nicer dialogs (Calling all Motif programmers)
* Support for color PS and LaTeX

#### Examples

* [Makefiles]({{< relref "#makefile" >}})
* [LaTeX]({{< relref "#latex" >}})
* [C]({{< relref "#c" >}})
* [HTML]({{< relref "#html" >}})

### Makefile

{{< include "Makefile.fragment" >}}

### LaTeX

{{< include "crossreference.dtx.fragment" >}}

### C

{{< include "export.c.fragment" >}}

### HTML

{{< include "index.html.fragment" >}}