---
layout: post
title: DevOpsDay Raleigh 2019
description: Take-aways from the conference
---
![My conference badge](/assets/img/devopsday-rdu-badge.jpg)


I attended the 2019 DevOpsDays Raleigh and really enjoyed it. Here are my take-aways and highlights from my favorite talks. The live-stream video of talks are on the [DevOpsDays Raleigh YouTube channel.](https://www.youtube.com/channel/UC4Xs0UbAdDaMRmStzhSsSag) and the individual talk videos should be up by mid-November.


## General Thoughts

![DevOpsDays Raliegh logo with Wright brothers plane](/assets/img/Raleigh-NC-DevOps-Logo.jpg)

- Don't forget culture during your transformation
- Don't focus on finding a *single* root cause for an incident. There's rarely a single event.
- Failures are great opportunities to learn
- VPs don't get much respect as these events. Lots of jokes at our expense. :) 

	 
---

## Culture
<a data-flickr-embed="true" href="https://www.flickr.com/photos/statedeptdss/38303584095/in/photolist-21mKT5k-y4uiCp-WaP4RR-2bnM6uj-25pJjm2-p55gcj-4jyDtK-fKyS7T-oy97z2-hKR3sp-osTcFs-4jyD9F-dhXDJb-JpxrV-i3ayvZ-oDvPEH-hRMWRK-i8oaPb-4jyEjp-i4XbBF-ov75pe-4jCCdw-hQE1pF-i6bQSN-4jyBvZ-i8bZHa-hSkP8W-4jyF6Z-oeXSoi-nvQTfG-4jCHBS-4jyndM-odacp5-4jCFZC-4jyDFM-hPkVHB-4jyDMk-4jykRK-4jCHu1-i6Cv7c-i5hiET-i2FuKw-4jCHEJ-ZYmb9X-4jCH91-hTvwqm-otUENK-i7iDNU-i93Cw2-hRJF49" title="DSS at UNGA 72 - Dignitary Protection Operations Center"><img src="https://live.staticflickr.com/4640/38303584095_39678a621f_w.jpg" width="400" height="267" alt="DSS at UNGA 72 - Dignitary Protection Operations Center"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>



### [Know Your Numbers](https://drive.google.com/open?id=18-OFq--aD-4dswf73zuY-ngWGlP5LQib) 
#### *by Anne Hungate*

I had seen Anne preview this talk at the local meetup but really enjoyed it a second time. 

Here's what I liked:

- Her list of the reasons why companies execute projects
- "Right people working on the right projects at the right time." to make sure your best people are working on the most important projects.
- Her belief that like the retail apocolypse, there is a digital apoloclypse for companies not ready to move fast with DevOps.



### [Expand Your DevOps Practice](https://drive.google.com/open?id=1qkMp7U8IKXWtWSHiwMhVyvY1c_VpBmne) 
#### *by Marguerite Bryan*

I attended this workshop without really knowing what it was about. It turned out to be a nice workshop on value streams and being Lean.

Here's what I liked:
- DevOps is about culture and lean processes as much as technology
- A fast DevOps approach and pipeline will be useless if ideas/projects are approved on an annual budgeting cycle and a Change Control Board only meets quartlerly
- The We Believe hypothesis template. I've seen this before in design thinking workshops and it was nice to see someone else recommend it. This is a great simple way to plan a test of a hyptohesis. 

```
We believe that: [doing this]
for: [target users/people]
will achieve: [this outcome]
We’ll know this is true when:
[this condition]
```

```
We believe that offering $25 gift cards to sign up new free-tier customers
for existing customers
will achieve an increase in sales of the premium subscription service.

We'll know this is true when 25% of the new customers have purchased the premium service.
```
  



### [Avoiding the Infamous DevOps Team!](https://drive.google.com/open?id=1xKHChHBRYo5jM1adWgTOjk9usuyo23H9) 
#### *by John Esser*

This talk focused on when to bring any separate innovative DevOps teams back into the main business engine of standard work. I think some people missed this main point and focused too much on the somewhat controversial topic of what *not* to name the team.

Here's what I liked:
- His stories of early DevOps conferences
- The advice to not let innovation teams exist separately for too long before bringing them back into the main business engine.

---


## Tech

<a data-flickr-embed="true" href="https://www.flickr.com/photos/132131207@N04/17330026471/in/photolist-spoV6R-aRYXXc-s7RB83-rsqF2h-eQgxro-ouzjqm-fvcxxG-6Gox4c-SZLXUM-hHZuQG-qr211X-ownYHo-od8YM4-out3wb-4w35YY-p6rhz2-od8GwN-2ar49SH-ovDZwT-oeXex4-org9iJ-qFb93y-qqUAew-38fXsC-23PGNga-ouBKqs-PuLd1-owfZyh-ouCaGb-ovqib8-bZKEsd-occmfx-ayaKv6-tnWvqJ-odoWeh-otAGec-ow8DjR-rptR8Q-qTFBQ4-oeSmec-otJFRW-ouA4B9-JecJz7-PuLdQ-gTZgQm-rw9SYe-6Q3Pf-q15wd1-to2e9o-jV2ucn" title="server"><img src="https://live.staticflickr.com/7658/17330026471_b5dc440647_o.jpg" width="273" height="185" alt="server"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

### [Just Enough Feature Flagging](https://drive.google.com/open?id=1m6pSIkTsifA5SaABbWhDGCCEQ7qf_zK8) 
#### *by Dave Rogers*

Here's what I liked:
- Very interactice session with the Story Time breaks to discuss deployment issues and feature flags with your seat neighbor
- Last few slides summarizing common mistakes and good ideas




### [Build and Monitor Machine Learning Services in Kubernetes](https://drive.google.com/open?id=10n2aGAXUhDhjq-mZRXnd9GgQZDi5HWyV)
#### *by Kirk Kaiser*
I think confidently deploying and monitoring AI/ML services will become a huge focus area for organizations as they want the value of data science but with the deployment and testing rigors of engineering.


Here's what I liked:
- Description of the differences between AI/ML work and workloads from traditional appdev
- Good list of deployment tools:
    - Kubeflow - ML toolkit for kubernetes
    - TensorRT - Inference server
    - Pachyderm - Version control for ML data and pipelines
    - NVIDIA container registry - registry of GPU and ML containers



### [Intelligent Deployment Pipelines](https://drive.google.com/open?id=1Ykx7VWBOtOcTbGCeiErgAO2XhzHHCVrg) 
#### *by Martez Reed*

Here's what I liked:
- Smart focus on environmental awareness to determine if it's a good time to deploy
- Intelligent checks:
    - Are the services and servers available before we deploy?
    - Are the required security groups available (in case another group is responsible for that)?
    - Any open there any critical network outages that should make us pause the deployment?
    - Is there really high traffic on the application now?
    - Has there been any major infrastructure drift?

---

## Security
<a data-flickr-embed="true" href="https://www.flickr.com/photos/140641142@N05/48631169337/in/photolist-ow72no-ouj7hA-oeGwMA-oeRrDa-oeHP2P-oeQ9En-ow8EAn-oy1Cut-2h6nsrq-2h6jSS1-2h6nsqy-2h6mGS5-2h6nsoj-2h6mGRo-2h6nsmR-2h6mGSv-2h6jSNd-2h6nskd-2h6nsmq-2h6nsi9-2h6mGM5-2h6mGNn-2h6jSKH-2h6nsjw-2h6jSJA-2h6nsgA-2h6mGL8-2h6nshh-2h6jSHP-odcBWN-ovBqqi-ovY8dj-oewgDR-xehw1E-oeKEQo-oxYtAa-wZ6prf-ow5mVY-oeV1Mb-wZ9aP1-oeMeyX-owcF19-ovH3zw-owdHj8-oeKzzz-xqszpg-xjQk33-xfi5oQ-oePiLd-otB5ze" title="Vault"><img src="https://live.staticflickr.com/65535/48631169337_567d5e4784_n.jpg" width="320" height="240" alt="Vault"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

### [DevSecOps: How to level up your organization’s security expertise](https://drive.google.com/open?id=19JNUB4xAL3RCmacNQdALot0dFGeAvu69) 
#### by Ann Marie Fred

This was the start of a series of security-focused talks. I enjoyed all of them, but this was my favorite.  

Here's what I liked:
- Great summary slide of tradition IT security vs. DevOps security
- Focus on active hacks vs. theorectical hacks! 
- IBM open-sourced their [npm_audit_fixer](https://github.com/IBM/npm_audit_fixer) tool



### [Did Netflix Inadvertently Figure Out How to Better Secure the Cloud?](https://drive.google.com/open?id=1LVjLn83OjE0oX0jUCVcGovIHLeO7OUZB) 
#### *by Ricardo Green*

Here's what I liked:
- Misconfigured IAM is a huge risk
- Who gets alerted if ports opened? S3 buckets made public?
- Use drift detection to help automate remeadiation
- Use required tags as part of drift strategy
- Chaos engineering has benefits for security as well



### [Open Source Container Security: A Brief Overview](https://drive.google.com/open?id=1EZkw1l4WUXMvl1WQ9Qnf1L6kW9_gBWlO) 
#### *by Jessica Repka*

This one was honestly over my head but I knew that many of my colleagues would like it.

Here's what I liked:
- Good overview of Anchore Engine (scan images for CVEs and apply policies), Falco (image deployment prevention), and Sysdig Inspect (capture logs for forensics)
- Jenkins plug-in information

The DevOpsDays series of conferences are a great (and cheap!) way to quickly get up to speed on current best practices. You should definitely try to attend one of your [local events.](https://devopsdays.org/)



