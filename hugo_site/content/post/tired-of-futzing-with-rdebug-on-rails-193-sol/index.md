+++
title = "Tired of futzing with rdebug on rails 1.9.3? Solution: gem 'debugger'"
date = "2012-04-18T15:48:00Z"
tags = ['geek']
galleryprefix = ""
gallerythumbnailprefix = ""
+++

I have been cautiously sticking with ruby 1.9.2-p290 for all development so
that I can use the debugger if needed. There are patches for newer version
but it was a serious pain in the ass. Some strange issues with delayed_job
forced my hand in the upgrade so I was started to dread recompiling ruby and
patching rdebug. Someone has a new fork of rdebug that is current and works
with 1.9.3 called 'debugger':<https://github.com/cldwalker/debugger>

Thanks to @ryanb for pointing out a new gem.

[http://stackoverflow.com/questions/8087610/ruby-debug-with-
ruby-1-9-3/8268091...](http://stackoverflow.com/questions/8087610/ruby-debug-
with-ruby-1-9-3/8268091#comment12872331_8268091)

