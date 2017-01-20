+++
title = "Parsing Incomplete or Malformed URLs with Regular Expressions"
date = "2006-09-03"
categories = ['Technology']
tags = ['Code', 'Regular Expressions']
+++

This is part 1 of a two part article on url handling. Part 2 will talk about normalizing and joining urls (a link will be posted when it is up).

Recently I was writing some C# code that works with web pages and I was sorely disappointed to learn that .NET's HttpWebRequest could not handle a URL without a scheme (aka protcol). So if I tried to request the page at www.filbar.org it would fail outright, but it works fine for http://www.filbar.org. I decided I would write my own Url class that could perform intelligent parsing. Additionally it would properly join relative path's to a base class; this appears to be possible with .NET but you have to request the page and check the returned url in the headers.

Parsing URLs is a common task for anyone who is writing code that interacts with a webpage. There are many sites that give a regular expression that can perfectly match a well-formed URL. But if the URL is mal-formed or imperfect then the match fails completely. So if you want more robust URL parsing read on!

### More About URLs Than You Really Wanted to Know

I use urls daily so I have a pretty good idea how they are formed, but to make the class as robust as possible I decided to look up the standards for URLs. Anyone wishing to find more information should read through http://www.gbiv.com/protocols/uri/rfc/rfc3986.html. This rfc also contains many oddball cases and examples that are useful when testing.

Here is the example that they give to demonstrate the different components of a URL:

      foo://example.com:8042/over/there?name=ferret#nose
      \_/   \______________/\_________/ \_________/ \__/
       |           |            |            |        |
    scheme     authority       path        query   fragment
Because the authority portion can be "[user:pass@]hostname[:port]", I chose to break the authority component into three: userinfo, host and port. In this case ftp://user:pass@secretftp.com/ userinfo would be equal to "user:pass". So I decided upon 7 general fragments that can exist in a url: scheme, userinfo, host, port, path, query and fragment.

It is also interesting to note that the "//" preceding the server name is not a part of the protocol version, instead it marks the beginning of an authority. Since this is not widely known I think it is more or less irrelevant, but it may be useful when trying to parse odd cases.

### Like Regularly Expressed Chickens

The goal here is to have a routine that parses well-formed urls perfectly and degrades nicely on incomplete or mal-formed urls. One thing to keep in mind is that this will generally perform poorly when trying to parse a relative url without a base url to work from. Since you will always have a base url when you have a relative url, this should not be a problem.

Parsing a url with regular expressions is fairly easy, even for malformed regular expressions, when you consider the components of a url and how people normally use urls. The crucial part of this problem is the scheme and host portion because they have the most variance. For example, it is common to omit the http:// from the beginning of the url and only enter the host name. The RFC given above provides a reference regular expression that will match a well-formed url.

    ^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?

The biggest problem with this regular expression is that it assumes that the user is going to enter a scheme (http:) and start the authority with //. So in the case of www.truelocal.com, the host name wouldn't be www.truelocal.com, it would be the scheme! So we need to adjust the regex so that it can still parse a url correclty when url's are entered without the scheme and start of authority. Beyond the scheme and authority, common use of urls follows the standard very closely. As a result of these the rest of the regular expression can be left as is.

Here is the regular expression that I am currently using. It is broken down into chunks by the component of the url that it parses. I think that these individual chunks are fairly easy to understand so I won't go over them unless someone specifically requests it.

{{< highlight csharp >}}
Regex urlRegex = new Regex(
      @"^((?<scheme>[A-Za-z0-9_+.]{1,8}):)?(//)?" +
      @"((?<userinfo>[!-~]+)@)?" +
      @"(?<host>[^/?#:]*)(:(?<port>[0-9]*))?" +
      @"(/(?<path>[^?#]*))?" +
      @"(\?(?<query>[^#]*))?" +
      @"(#(?<fragment>.*))?",
      RegexOptions.ExplicitCapture);
{{< /highlight >}}

As said above, most problems parsing urls are related to the scheme and the authority section.. Therefore, the only part of this regex that does not adhere to the reference grammar posted in the rfc is the scheme and host parsing. There are two changes here that make this system more robust:

The scheme is limited to be 8 characters in length or less, and
The // part of the authority has become entirely optional and independent of the scheme or the authority.
To understand the reason I limit the length of the scheme, consider the following example: "www.filbar.org:80/index.html". If I did not limit the scheme it would be parsed as scheme=www.filbar.org, host=80 and path=/index.html. With the length limit on the scheme it will be correctly parsed as host=www.filbar.org, port=80 and path=/index.html.

There are very few schemes that are longer than 8 characters and they are uncommon so this will not have many side effects, especially if you are only parsing urls that are common on the web. If you want to be more certain, you could always attempt to match known scheme names, in my case they will always be http or https.

Making the '//' independant from the authority and optional was not necessary but it improves the robustness of the regular expression. Since most people view the // as part of the protocol definition it could have been added to the scheme section without having a detrimental effect on parsing. By making it independant of both the scheme and the authority we increase the number of forms that can be matched, consider: http:filbar.org or //filbar.org.

