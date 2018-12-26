---
layout: post
title: Resolving Git Multiple Credential Helpers
description: My first blog post
---

In playing with getting git's credential helper to work on Windows, I accidentally added multiple helpers to my local config file. It took me a while to figure out where it was stored and how to reset it. I used this command when in the local repo directory.

{% highlight shell %}
git config  --unset-all credential.helper
{% endhighlight %}

This [Stack Overflow](https://stackoverflow.com/questions/11693074/git-credential-cache-is-not-a-git-command) post got me close but was based on the multiple values coming from different versions of the config file. This [blog post]. The key was the --unset-all option. This [blog post](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/Where-system-global-and-local-Windows-Git-config-files-are-saved) helped explain the different scope of config files.



