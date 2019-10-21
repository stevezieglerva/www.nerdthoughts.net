---
layout: post
title: Modern Architecture Conference Talks
description: List of conference talks on modern architecture considerations
---

A senior developer in my engineering group expressed interest in leading our next modernization project. It got me thinking about some modern architecture ideas that a lead architect should understand. While you might not use all of these techniques, you should have an understanding of them. 

I love conference talks as a quick and easy way to get introduced to concepts. Here are some of my favorites.


# Many Meanings of Event-Driven Architectures
[![Many Meanings of Event-Driven Architectures](https://i.ytimg.com/vi/STKCRSUsyP0/hqdefault.jpg)](https://youtu.be/STKCRSUsyP0)

You can never go wrong with Martin Fowler. He frequently reminds us that many of these ideas are not actually new, but just re-packaged with modern tooling. I love his point that most developers have used a fully event-based data source without even knowing it.

<hr/>





# Microservices
[![Microservices](https://i.ytimg.com/vi/wgdBVIX9ifA/hqdefault.jpg)](https://youtu.be/wgdBVIX9ifA)

https://youtu.be/wgdBVIX9ifA

<hr/>

# 6 Million Registrations in 30 Days
[![6 Million Registrations in 30 Days](https://i.ytimg.com/vi/9tm0LsNBbzs/hqdefault.jpg)](https://youtu.be/9tm0LsNBbzs)

I really like how this talk focuses a lot of the business drivers for Chik-fil-a's mobile architecture. It's really driven home with the pictures of the kitchens how their are fed with info on mobile orders to anticipate demand.

<hr/>

# Pragmatic Microservices
Given his resume, Randy Shoup has a lot of good talks describing his experiences with distributed architectures. He, like many others, recommends building the monolith first. Distributed systems come with their own, complex problems.

[![Pragmatic Microservices](https://i.ytimg.com/vi/9vS7TbgirgY/hqdefault.jpg)](https://youtu.be/9vS7TbgirgY)
<hr/>

# Stream All Things - Patterns of Modern Data Integration
I think streams are the future for integrations, especially pub/sub. They are fast, can handle high volume, and let you play back history. AWS even uses streams for some of Lambda events from other services (like Dynamo DB). You can also use streams to queue up fast data arrivals for a slower downstream ingestion (like to Elasticsearch). 

[![Stream All Things - Patterns of Modern Data Integration](https://i.ytimg.com/vi/Hjae0Cw9oew/hqdefault.jpg)](https://youtu.be/Hjae0Cw9oew)
<hr/>

# Robust anomaly Detection For Real User Monitoring Data
I loved this talk, especially the practical discussions of what counts as an anomaly given business and operating conditions. I really like how they analyzed possible root causes of anomalies of their  metrics and sent that information to Ops along with the alerts to help with resolution. 

[![Robust anomaly Detection For Real User Monitoring Data](https://i.ytimg.com/vi/0PtehdUL-38/hqdefault.jpg)](https://youtu.be/0PtehdUL-38)
<hr/>

# What I Learned From 4 Years of Researching the Crap Out of DevOps
Jez Humble and Dr Nicole Forsgren
https://pbell.wistia.com/medias/xlxb0awlp4?wtime=0

{% include image.html name="jezhumbledevops" atl="Jez Humble video thumbnail" caption="" %}



You are not Google
https://blog.bradfieldcs.com/you-are-not-google-84912cf44afb 

find pragmatic orielly of conference talks