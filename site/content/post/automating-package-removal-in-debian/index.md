+++
title = "Automating Package Removal in Debian"
date = "2005-09-19T16:27:00Z"
tags = []
galleryprefix = ""
gallerythumbnailprefix = ""
+++

This is a quick way to remove packages matching a grep pattern. Use with
caution!

This removes all the gimp packages:

> apt-get remove --purge `dpkg -l | grep gimp | cut -d ' ' -f 3`

