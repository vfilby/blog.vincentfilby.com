+++
title = "Getting Forms Authentication Timeout from web.config programmatically"
date = "2009-09-14"
tags = ['Programming']
category = ['Tech']
+++

I have to create Forms Authentication ticket's on my own for some parts of a web application. I won't get into the why as it's a bit complicated, so trust when when I say that I need to.

I wanted to rely on defaults as much as possible so when I went to set the default timeout I was astounded to find that it wasn't available easily through code. I didn't just want to hardcode the value of '30' minutes because it can be overridden in the web.config.

So I hit Google figuring someone's run into this before, and they had with no better conclusion. Scott Hanselman listed a whole bunch of methods that were attempted but failed and eventually ended up using xpath to access the value directly from the file. That's 2004, 5 years ago, I figured there had to be a better way.

I ran to Reflector and looked at how the forms authentication timeout is initialized in the first place.

{{< highlight csharp >}}
AuthenticationSection authentication = 
   RuntimeConfig.GetAppConfig().Authentication;
	 
...

_Timeout = 
   (int)authentication.Forms.Timeout.TotalMinutes;
{{</highlight>}}

It just loads the config section and accesses it directly. Nothing really preventing me from doing just that. A little extra help on accessing the System.Web section from dotnetcurry.com and here is what I came up with:

{{< highlight csharp >}}
Configuration config =
   WebConfigurationManager.OpenWebConfiguration( "~" );

AuthenticationSection authentication =
   (AuthenticationSection)config.GetSection(   
       "system.web/authentication" );

return (int)authentication.Forms.Timeout.TotalMinutes;
{{</highlight>}}

As an added bonus, even if the Timeout isn't specified in the web.config, it will return the default of 30 minutes. Add some error handling for the cases with the section or value are not present and voila.

