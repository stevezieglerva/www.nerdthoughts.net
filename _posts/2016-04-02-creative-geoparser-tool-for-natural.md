---
layout: post
title: Creative Geoparser Tool for Natural Language
date: '2016-04-02T00:09:00.000-04:00'
author: Stephen Ziegler
tags:
- machine learning
- gis
- natural language
modified_time: '2016-04-02T00:09:03.151-04:00'
blogger_id: tag:blogger.com,1999:blog-1727955271917225446.post-3264684173076715521
blogger_orig_url: http://www.nerdthoughts.net/2016/04/creative-geoparser-tool-for-natural.html
---

<div class="separator" style="clear: both; text-align: center;"><a href="https://clavin.bericotechnologies.com/"><img border="0" src="https://clavin.bericotechnologies.com/wp-content/uploads/2015/04/clavin_logo-300x163.png" /></a></div>While preparing for a client demo, someone recommended I look at <a href="https://clavin.bericotechnologies.com/">Clavin </a>as a geoparser to extract locations out of natural language text. I was impressed with the results and thought it was a pretty creative solution using three core open-source technologies to solve a problem:<br /><br /><ul><li><a href="http://nlp.stanford.edu/software/CRF-NER.shtml">Stanford NER</a>&nbsp;- Performing named entity recognition (people, locations, organizations, times) out of natural language is tough. You need more than just a dictionary lookup of location names, especially for international locations that happen to match English words: "nice" and "Nice, France." The Stanford NER uses parts of speech patterns to intelligently guess when words are locations.</li><li><a href="http://download.geonames.org/">Geoname gazetteer</a>&nbsp;- A comprehensive list of 10M locations, alternative names, and lat/longs</li><li><a href="https://lucene.apache.org/">Lucene </a>- A full text search engine used to quickly lookup text references, including fuzzy matches</li></ul><div>Clavin uses Stanford NER as the first pass for guesses on locations. It then uses Lucene to look up exact and fuzzy matches of the Geoname gazetteer data as the second pass on location detection. It works best on news-style language. It works pretty well, especially given the complexities of natural language.&nbsp;</div><div><br /></div><br /><div><br /></div>