---
layout: post
title: Bash alias for GMT
description: Simple bash script that lists out local and GMT time for the last 24 hours
---
I always struggle trying to convert GMT time to EST or EDT especially in 24 hour format. It's even harder when I'm staring at a log file trying to find the root cause of an issue. 

I wrote this bash alias to output the last 24 hours of time in both local and GMT. I find I'm using it all of the time now. Since it's an alias, I can easily run it from a Terminal window or within VSCode.

Here is the script:
```bash
gmt(){

for i in {-24..-1}
do
    est=$(date -v${i}H)
    gmt=$(date -u -v${i}H)
    echo "$i	$est	$gmt"
done
est=$(date)
gmt=$(date -u)
echo "0	$est	$gmt"

}
```

Here is sample output:
```
-24     Sun Feb 16 08:49:05 EST 2020    Sun Feb 16 13:49:05 UTC 2020
-23     Sun Feb 16 09:49:05 EST 2020    Sun Feb 16 14:49:05 UTC 2020
-22     Sun Feb 16 10:49:05 EST 2020    Sun Feb 16 15:49:05 UTC 2020
-21     Sun Feb 16 11:49:05 EST 2020    Sun Feb 16 16:49:05 UTC 2020
-20     Sun Feb 16 12:49:05 EST 2020    Sun Feb 16 17:49:05 UTC 2020
-19     Sun Feb 16 13:49:05 EST 2020    Sun Feb 16 18:49:05 UTC 2020
-18     Sun Feb 16 14:49:05 EST 2020    Sun Feb 16 19:49:05 UTC 2020
-17     Sun Feb 16 15:49:05 EST 2020    Sun Feb 16 20:49:05 UTC 2020
-16     Sun Feb 16 16:49:05 EST 2020    Sun Feb 16 21:49:05 UTC 2020
-15     Sun Feb 16 17:49:05 EST 2020    Sun Feb 16 22:49:05 UTC 2020
-14     Sun Feb 16 18:49:05 EST 2020    Sun Feb 16 23:49:05 UTC 2020
-13     Sun Feb 16 19:49:05 EST 2020    Mon Feb 17 00:49:05 UTC 2020
-12     Sun Feb 16 20:49:05 EST 2020    Mon Feb 17 01:49:05 UTC 2020
-11     Sun Feb 16 21:49:05 EST 2020    Mon Feb 17 02:49:05 UTC 2020
-10     Sun Feb 16 22:49:05 EST 2020    Mon Feb 17 03:49:05 UTC 2020
-9      Sun Feb 16 23:49:05 EST 2020    Mon Feb 17 04:49:05 UTC 2020
-8      Mon Feb 17 00:49:05 EST 2020    Mon Feb 17 05:49:05 UTC 2020
-7      Mon Feb 17 01:49:05 EST 2020    Mon Feb 17 06:49:05 UTC 2020
-6      Mon Feb 17 02:49:05 EST 2020    Mon Feb 17 07:49:05 UTC 2020
-5      Mon Feb 17 03:49:05 EST 2020    Mon Feb 17 08:49:05 UTC 2020
-4      Mon Feb 17 04:49:05 EST 2020    Mon Feb 17 09:49:05 UTC 2020
-3      Mon Feb 17 05:49:05 EST 2020    Mon Feb 17 10:49:05 UTC 2020
-2      Mon Feb 17 06:49:05 EST 2020    Mon Feb 17 11:49:05 UTC 2020
-1      Mon Feb 17 07:49:05 EST 2020    Mon Feb 17 12:49:05 UTC 2020
0       Mon Feb 17 08:49:05 EST 2020    Mon Feb 17 13:49:05 UTC 2020
```