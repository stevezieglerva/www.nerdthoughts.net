---
layout: post
title: AWS Cloudwatch Cron Expression for Every Ten Minutes
description: AWS Cloudwatch Cron Expression for every time minutes
---
I recently tried to schedule an AWS Lambda defined through a SAM template to run every 10 minutes. I used some online cron expression builders but the syntax would not work with Cloudwatch.

Somehow, I missed this reference in the [Schedule Expressions for Rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html). The online expression builders put * for both day of the month and day of the week.

```
You cannot use * in both the Day-of-month and Day-of-week fields. 
If you use it in one, you must use ? in the other.
```

Here is the expression that worked:

```
      Events:
         CronEvent:
          Type: Schedule
          Properties:
              Schedule: cron(0,10,20,30,40,50 * ? * * *)
```

