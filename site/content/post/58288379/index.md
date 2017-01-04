+++
title = "Overriding Posterous Blockquote Styles"
date = "2011-06-23T17:25:00Z"
tags = []
galleryprefix = ""
gallerythumbnailprefix = "t190_"
+++

If you have used Posterous for blockquotes you will find that it post
processes the blockquotes based on size. Small, medium and large block
quotes are all treated differently and styled differently.This is a pain in
the ass if you are quoting different sections and the quotes are styled
differently

An easy and permanent workaround is to adjust the styles for you blockquotes
on your posterous theme.

    
    
    blockquote.posterous_medium_quote::before { content: none; }
    blockquote.posterous_medium_quote::after { content: none; }
    blockquote.posterous_medium_quote{ border-left: 4px solid #DDD!important; padding-left: 10px; font-family: inherit; font-size: inherit; line-height: inherit; }

With this it overrides the posterous medium_blockquote theme and applies the
same style as a long block quote.

Before:

![](/post/58288379/Posterous_-_Customizing_Biometric_Me.jpg)

After:

![](/post/58288379/Biometric_Privacy_Concerns_-_Biometric_Me.jpg)

