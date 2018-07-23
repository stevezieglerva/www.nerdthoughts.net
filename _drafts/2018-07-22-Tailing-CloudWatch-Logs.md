---
layout: post
title: Tailing CloudWatch Logs
description: Open source Python project to make searching AWS CloudWatch logs easier
date: '2018-07-22T00:00:00.000-05:00'
author: Stephen Ziegler
tags:
- dev, aws
---

The [awslogs](https://github.com/jorgebastida/awslogs) project provies a really easy way to search and understand AWS CloudWatch logs. You can easily wrap the tool in a loop to tail the logs. Here is a simple DOS batch file to tail the logs:

{% highlight python %}
echo off
title CloudWatch Tail

:repeat
echo *** %date% %time%
call awslogs get /aws/lambda/aws-lnkchk-extract-links --start="1m" --filter-pattern="?starting ?processing ?downloading ?extracting ?checked ?finished ?ERROR ?Error ?Exception ?skipping" > results.txt
type results.txt
type results.txt >> log.txt

REM Silent wait
CHOICE /C:AB /d:A /T:15 >NUL

goto repeat

{% endhighlight %}


