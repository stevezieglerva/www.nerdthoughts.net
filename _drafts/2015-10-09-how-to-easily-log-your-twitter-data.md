---
layout: post
title: How to Easily Log Your Twitter Data Using Zapier and Dropbox
description: Archiving tweets with Zapier and Dropbox
date: '2015-10-09T13:46:00.002-04:00'
author: Stephen Ziegler
tags:
- data
- twitter
modified_time: '2015-10-09T13:46:40.747-04:00'
thumbnail: http://2.bp.blogspot.com/-DRSy59p_5Qw/Vhf4besIhTI/AAAAAAAAhKM/4paIpE5ZvKo/s72-c/twitter_zap_setup.png
blogger_id: tag:blogger.com,1999:blog-1727955271917225446.post-766429352419566457
blogger_orig_url: http://www.nerdthoughts.net/2015/10/how-to-easily-log-your-twitter-data.html
---

I often find myself looking for past tweets and followers trying to find a specific link to a blog post or an image. Twitter itself is pretty useless for this task. There are several ways to download your data from Twitter, but I've found a new way using [Zapier](https://zapier.com/) and [Dropbox](https://www.dropbox.com/) that doesn't required coding and allows you to track other data besides tweets. At some point, I'll index this data in Elasticsearch to make it really easy to find stuff. But for now, using a text editor's Find in a consolidated text file works pretty well as an MVP. In the future, I'd like to do some analysis with my followers. I'm especially fascinated with bots and how spammers are making them more and more realistic (including pics, topical tweets, short profile bios, realistic number of followers/following).

Here's how you can set up a Zap to automatically append Twitter (tweets, mentions, favorites, new followers) data to a simple text file:

<ul>


<li>Create a Zap with Twitter/My Tweet as the trigger and Dropbox/Append Text File as the action. The Append Text File action is key to this solution and allows you to continually add to the end of the file. I think it's new within the last year or so. I had previously set up a Zap to store tweet information in a Google Spreadsheet but it forced me to set up the exact columns beforehand and was not easy to change.</li>
</ul>

{% include image.html name="zapier_triggers" atl="Zapier triggers" caption="Zapier triggers" %}


<ul>

<li>Select and authenticate your Twitter and Dropbox accounts</li>
<li>Select the folder for your Dropbox files. I created a new folder called Twitter to store several files</li>
<li>Choose the fields to append to your file. I chose to use a multi-line format with record delimiters and field labels. I like this format because it is human-readable and will allow me to easily parse it in the future with a tool like AWK, even if the file becomes huge. To make it a little more readable, I added a literal "@" before any user name fields. Since I use the same file for tweets and mentions, I added a literal "type: mytweet" to help me separate that data.</li></ul>

<div class="separator" style="clear: both; text-align: center;"><a href="http://3.bp.blogspot.com/-qBCTNt9jVrg/Vhf5rfJ3ilI/AAAAAAAAhKY/6zSC24eO6iI/s1600/Twitter%2BTweet%2BFile.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="243" src="http://3.bp.blogspot.com/-qBCTNt9jVrg/Vhf5rfJ3ilI/AAAAAAAAhKY/6zSC24eO6iI/s400/Twitter%2BTweet%2BFile.png" width="400" /></a></div>

<ul>
<li>Create other Zaps to log mentions, new followers and favorites. Here is how I setup the file contents for the other files:</li><ul>
<li>mentions:</li></ul></ul><div class="separator" style="clear: both; text-align: center;"><a href="http://1.bp.blogspot.com/-lY18wQDkPXE/Vhf7CSt6lhI/AAAAAAAAhKk/-w514BTbQ5s/s1600/Twitter%2BMentions.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="135" src="http://1.bp.blogspot.com/-lY18wQDkPXE/Vhf7CSt6lhI/AAAAAAAAhKk/-w514BTbQ5s/s400/Twitter%2BMentions.png" width="400" /></a></div><div><ul><ul>
<li>favorites:</li></ul></ul><div class="separator" style="clear: both; text-align: center;"><a href="http://1.bp.blogspot.com/-vy0ItuLK_A4/Vhf7gD0bx1I/AAAAAAAAhKs/Y_XlCCkfR58/s1600/Twitter%2BFavorite.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="121" src="http://1.bp.blogspot.com/-vy0ItuLK_A4/Vhf7gD0bx1I/AAAAAAAAhKs/Y_XlCCkfR58/s400/Twitter%2BFavorite.png" width="400" /></a></div><div class="separator" style="clear: both; text-align: center;">
</div><div class="separator" style="clear: both; text-align: center;"></div><ul><ul><li style="text-align: left;">new followers:</li></ul></ul><div class="separator" style="clear: both; text-align: center;"><a href="http://3.bp.blogspot.com/-SSmlneWZZrg/Vhf74ANOWRI/AAAAAAAAhK0/TdmcTxlapMs/s1600/Twitter%2BFollowers.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="221" src="http://3.bp.blogspot.com/-SSmlneWZZrg/Vhf74ANOWRI/AAAAAAAAhK0/TdmcTxlapMs/s400/Twitter%2BFollowers.png" width="400" /></a></div><div style="text-align: left;">
</div>

If you don't like this method, you can try [downloading your Twitter archive](https://support.twitter.com/articles/20170160) (tweets only), using scripting in a language like Python, or [find an existing tool/service](https://www.google.com/webhp?sourceid=chrome-instant&amp;ion=1&amp;espv=2&amp;ie=UTF-8#q=search%20tool%20for%20my%20twitter%20data).
