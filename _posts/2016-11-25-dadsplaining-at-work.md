---
layout: post
title: Dadsplaining at Work
description: Finding the right way to teach at work
permalink: /2016/11/dadsplaining-at-work.html
date: '2016-11-25T09:41:00.002-05:00'
author: Stephen Ziegler
tags:
- work
- leadership
modified_time: '2016-11-26T10:00:23.887-05:00'
thumbnail: https://4.bp.blogspot.com/-hmyKSxGoK7k/WDhELEnD9FI/AAAAAAAAhRc/0FIRgFwk248UuAUiEbDZQnmxp8KQZflCgCLcB/s72-c/skype.png
blogger_id: tag:blogger.com,1999:blog-1727955271917225446.post-1541103662754598807
blogger_orig_url: http://www.nerdthoughts.net/2016/11/dadsplaining-at-work.html
---

<div class="separator" style="clear: both; text-align: center;"><a href="http://www.partyworld.ie/store_images/customcontent/0/homer_simpson_picture_jpg.jpg" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://www.partyworld.ie/store_images/customcontent/0/homer_simpson_picture_jpg.jpg" height="320" width="185" /></a></div><br /><br />


Growing up, my dad wouldn't just answer a question from the kids. He would follow it up with background info, reasons why, and ask us related questions. It always stuck with me and I find myself "dadsplaining" things to my kids. It's a good, impromptu moment for teaching and getting the kids to think creatively and analytically.

I also try to do it with co-workers, but I'm sensitive not to force it on people like I force it on my kids. I also try to save it for receptive audiences. I recently helped a team look into a slow data conversion routine. I was convinced that indexes would help since the total data manipulated was less than .5GB (pretty small in database terms).

I used my usual story for explaining how indexes can and cannot help, depending on the uniqueness of the index columns:

> Imagine I gave you a 1,000 page medical encyclopedia and asked you to find the verb of every sentence that had the word "cancer" in it. How would you do that? Would you open to page 1 and start reading? That would be a slow way to do it and is equivalent to a full-table scan on a large table.	

> The faster way would be to flip back to the index, see if "cancer" is one of the indexed words, and jump directly to those pages to read. You might only have to read a few pages and this would be a great use of an index. Because the word cancer is pretty unique across the pages, it saves a lot of time reading pages. This is like an index with high selectivity: the number of unique items in the index compared to the number of items in the table.

> Imagine if the index of the book told you that "cancer" appeared somewhere between pages 200 and 700 or it listed several hundred pages where cancer appeared. Or, imagine you wanted to find the verbs of sentences that contained the word "the." A database table index wouldn't help you much in these scenarios. This is like an index with low selectivity. There aren't enough unique index values to help find exact records.
	
I also described how composite indexes are needed to match the the exact columns and column order of the where clauses in your SQL. I think that was the missing piece in the previous attempt to add indexes to improve performance.

I got a nice IM after the discussion thanking me for the descriptions of indexes. I don't always dadsplain at work, but when I do, it's nice to get some positive feedback.

{% include image.html name="skype" atl="Skype Message" caption="Skype Message" %}

