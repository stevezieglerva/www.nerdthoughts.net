---
layout: post
title: Beauty of Elasticsearch Bool Query Should Clauses for Boosting
date: '2015-03-24T17:47:00.002-04:00'
author: Stephen Ziegler
tags:
- work
- elasticsearch
modified_time: '2017-01-05T00:23:11.981-05:00'
thumbnail: https://4.bp.blogspot.com/-Ts7XVeU8nc0/WG3YLiKhv-I/AAAAAAAAhTQ/CzhtS3w2OHo7_Q8nWBV16rt7I8hl3pvKwCLcB/s72-c/email_search.png
blogger_id: tag:blogger.com,1999:blog-1727955271917225446.post-5125240127210316901
blogger_orig_url: http://www.nerdthoughts.net/2015/03/beauty-of-elasticsearch-bool-query.html
---

Elasticsearch's boolean query gives you an elegant way to simply provide complex boosting conditions. &nbsp;I've used boosting query fields as part of match clauses. But on their own, those clauses force a match as part of the boosting.

But, the bool query lets you have set of mandatory *must* clauses along with optional *should* clauses. The should clauses boost matches when more of the clauses are true. In addition, you can increase the boost per clause.

I index my Outlook email in Elasticsearch and recently started using a boosted bool query that has dramatically increased the accuracy of my searches and reduced the time to find what I'm looking for. This is actually my second attempt to index my email in the last 5 years. &nbsp;Over the years, I learned that I'm typically looking for emails:

*with several AND'd keywords
* from a specific person
* to a specific person
* that I've searched for and looked at before
* with attachments&nbsp;
* that's recent, usually within a month but at least within the last six months

Here is query that matches my searching habits:


<br />  "query": {

<br />    "filtered": {

<br />      "query": {

<br />        "bool": {

<br />            "must" : [

<br />                    { "query_string": {"query": "--query-- +_type:email",&nbsp;

</span>

</pre>

<pre>

<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace;">                          "default_operator" : "AND" } }

<br />                           ],

<br />          "should": [

<br />

<br />                      { "query_string" : { "fields" : ["from"], "query" :&nbsp;

</span>

</pre>

<pre>

<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace;">                          "--query--", 

<b>

<span style="color: #b45f06;">"boost" : 2

</span>

</b>}},

<br />                      { "query_string" : { "fields" : ["to"],&nbsp;

</span>

</pre>

<pre>

<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace;">                          "query" : "--query--", 

<b>

<span style="color: #b45f06;">"boost" : 2

</span>

</b>}},

<br />                      { "match" : { "opened" : {"query" : "Y",&nbsp;

</span>

</pre>

<pre>

<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace;">                          

<b>

<span style="color: #b45f06;">"boost" : 2

</span>

</b>}}},

<br />                      { "match" : { "attachment" : "--query--"}},

<br />                      { "match" : { "dateYear" : "--query--"}},

<br />                      { "match" : { "dateMonth" : "--query--"}},

<br />                      { "match" : { "has_attach" : "Y"}},

<br />                      { "range" : { "@timestamp" : {"gt" : "now-30d", "lt" : "now" }}},

<br />                      { "range" : { "@timestamp" : {"gt" : "now-180d", "lt" : "now" }}}

<br />                 ]

<br />               }

<br />            }

<br />          }

<br />       },

<br />  "highlight": {

<br />    "fields": {

<br />      "subject": {},

<br />      "body-stem": {},

<br />      "attachment": {}

<br />    },

<br />    "fragment_size": 50,

<br />    "number_of_fragments" : 1,

<br />    "pre_tags": [

<br />      "

<em>"

<br />    ],

<br />    "post_tags": [

<br />      "

</em>"

<br />    ]

<br />  },

<br />  "size": 20,

<br />  "fields" : ["subject", "_id", "@timestamp", "has_attach", "from", "body-stem"],

<br />  "sort": [

<br />    {

<br />      "_score": {

<br />        "order": "desc",

<br />        "ignore_unmapped": true

<br />      }

<br />    }

<br />  ]

<br />}

</span>

<br />

</pre>

I created a simple test client for a research project and decided to re-purpose it as a simple email search client. It's not pretty, but it's very effective for finding lost email needles in the daily onslaught of emails. I like the simplicity of just typing search words and getting very relevant results back. I had been using Kibana to find emails but got frustrated that I kept having to manually add filters when I felt the search should have just been smarter. I've been very happy with the results and impressed with the elegance of the simple, yet powerful, query syntax.


<a href="https://4.bp.blogspot.com/-Ts7XVeU8nc0/WG3YLiKhv-I/AAAAAAAAhTQ/CzhtS3w2OHo7_Q8nWBV16rt7I8hl3pvKwCLcB/s1600/email_search.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;">

<img border="0" height="337" src="https://4.bp.blogspot.com/-Ts7XVeU8nc0/WG3YLiKhv-I/AAAAAAAAhTQ/CzhtS3w2OHo7_Q8nWBV16rt7I8hl3pvKwCLcB/s640/email_search.png" width="640" />

</a>

