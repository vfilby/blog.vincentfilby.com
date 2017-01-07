+++
title = "'Simple Audit' gem patch for Rails3"
date = "2011-02-28T03:59:00Z"
tags = []
+++

In Rails3 all strings are escaped by default, in [Simple
Audit](https://github.com/gtarnovan/simple_audit) this doubly escapes the html
output of the audit history display. While waiting for the main trunk to be
updated I forked the main repo and created a version that explicitly outputs
the audit history in raw format so that it can be displayed.

If you want to try it you can get my fork of simple audit:
<https://github.com/vfilby/simple_audit>

