---
layout: post
title: CloudWatch Metric Filter Works, But Alarm Doesn't
description: How to get a CloudWatch alarm for a log metric to work if scripted through Python boto
tags: aws
---

I was recently struggling with getting a CloudWatch alarm on a log filter metric to work. I was refactoring the creation from a CloudFormation template into just Lambda Python code. I was able to get both the filter metric (looking for errors and exceptions in logs) and alarm created. 

But, when I tested the alarm, it never went into an alarm state, even when then metric filter showed active data. It was driving me crazy. I was able to manually create a new alarm, pointing to the same metric filter and see it work. This is the type of bug that developers hate: a completely illogical bug (as viewed by the bug's creator).

Here is the metric showing data:
![Working CloudWatch metric showing a spike](/assets/img/cloudwatch_working_metric.png)

Here is what the empty alarm looked like:
![Broken CloudWatch alarm never showing the showing the spike](/assets/img/cloudwatch_empty_alarm.png)

Searching online for an answer was not easy. My heart sunk when Stack Overflow didn't have the exact answer to my question with my first search. :) Searches for "alarms not working for filter metrics" weren't leading anywhere. 

I slept on it and tried different searches the next day. Luckily, [Marta Tatiana](https://medium.com/@martatatiana) blogged her solution once she finally found it: 
[Insufficient data: CloudWatch alarm based on custom metric filter.](https://medium.com/@martatatiana/insufficient-data-cloudwatch-alarm-based-on-custom-metric-filter-4e41c1f82050). It turns out that you can't specify the period units (seconds, minutes, ...) when creating the alarm programmatically. 

Marta demonstrated one of the best reasons for blogging: showing other people your solution to a problem using your words. Your words may end up being better SEO for some lucky developer down the road.
