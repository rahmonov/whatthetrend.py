# What The Trend

[![Data](http://api.whatthetrend.com/images/wtt_api_badge_120.png)](http://api.whatthetrend.com/)

## Description

Whatthetrend.py provides a friendly Python interface to the What The Trend API

Python Wrapper for What the Trend API

## Usage

##### Get current trending terms on Twitter, with descriptions.


```python

>> wtt = WhatTheTrend()
>> wtt.get_trends()
>> {"ok": True,
    "data": [
        {
        "description" : { "created_at" : "2009-10-15 19:54:32",
                "text" : "A 6 year old was believed to be stuck in a homemade hot air balloon in Denver, Colorado. The balloon landed with no boy found inside. The boy is still missing.",
                "score" : "0"
            },
		"first_trended_at" : "2009-10-15 19:00:01",
		"last_trended_at" : "2009-10-15 19:55:01",
		"name" : "Colorado",
		"newly_trending" : "0",
		"query" : "Colorado",
		"trend_index" : "1",
		"url" : "http://search.twitter.com/search?q=Colorado",
		"related_url" : "http://www.wikipedia.com/Colorado",
		"category_id" : "11",
		"category_name" : "News",
		"locked" : false
        },
        ...
    ]}
```