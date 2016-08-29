# What The Trend

[![Data](http://api.whatthetrend.com/images/wtt_api_badge_120.png)](http://api.whatthetrend.com/)

## Description

Whatthetrend.py provides a friendly Python interface to the What The Trend API

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

##### Get current trending terms around a specific location

```python
>> wtt = WhatTheTrend()
>> wtt.get_trends(around='United States')
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

##### Get currently most-edited trends on What the Trend in the last 24 hours.

```python
>> wtt = WhatTheTrend()
>> wtt.get_active_trends()
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

##### Get a list of the trends most recently identified as SPAM or spam targets.

```python
>> wtt = WhatTheTrend()
>> wtt.get_spammy_trends()
>> {"ok": True,
    "data": [
        { "description" : { "created_at" : "2009-10-15 19:54:10",
			"text" : "A 6 year old was believed to be stuck in a homemade hot air balloon in Denver, Colorado. The balloon landed with no boy found inside. The boy is still missing.",
			"score" : "0"
			},
		"first_trended_at" : "2009-10-15 19:30:01",
		"last_trended_at" : "2009-10-15 19:55:01",
		"name" : "#saveballoonboy",
		"newly_trending" : "0",
		"query" : "#saveballoonboy",
		"trend_index" : "2",
		"url" : "http://search.twitter.com/search?q=%23saveballoonboy",
		"category_id" : "11",
		"category_name" : "News",
		"locked" : false
		},
        ...
    ]}
```

##### Get list of the top trends by locations. Choices: earth, country, region, state, town 

```python
>> wtt = WhatTheTrend()
>> wtt.get_trends_by_location('country')
>> {"ok": True,
    "data": [
        { "description" : { "created_at" : "2010-03-02T05:22:50+00:00",
			"text" : "People explaining why they don't care about what someone else is doing or saying",
			"score" : "0"
			},
		"id" : "41236",
		"last_trended_at" : "2010-03-04T18:09:50+00:00",
		"name" : "#BitchSoWhat",
		"place_name" : "United Kingdom",
		"slug" : "%23BitchSoWhat",
		"woeid" : "23424975"
		},
        ...
    ]}
```

##### Get list of categories available 

```python
>> wtt = WhatTheTrend()
>> wtt.get_categories()
>> {"ok": True,
    "data": [
		{"id":1,"name":"Entertainment"},
		{"id":2,"name":"Gaming"},
		{"id":3,"name":"Lifestyle"},
		{"id":4,"name":"Science"},
		{"id":5,"name":"Sports"},
		{"id":6,"name":"Technology"},
		{"id":7,"name":"Business"},
		{"id":8,"name":"SPAM"},
		{"id":9,"name":"Meme"},
		{"id":10,"name":"Conference or Event"},
		{"id":11,"name":"News"},
		{"id":12,"name":"Place or Location"},
		{"id":13,"name":"Holiday or Date"},
		{"id":14,"name":"Other"}
	]}
```

##### Get list of all locations to ever trend.

```python
>> wtt = WhatTheTrend()
>> wtt.get_locations()
>> {"ok": True,
    "data": [
		{ "country_name" : "1",
		"name" : "Earth",
		"place_type_code" : "19",
		"place_type_name" : "Supername",
		"updated" : "2010-04-05T18:05:17+00:00",
		"woeid" : "1"
		},
		...
	]}
```

##### Get a list of current trending locations 

```python
>> wtt = WhatTheTrend()
>> wtt.get_trendy_locations()
>> {"ok": True,
    "data": [
		{ "count" : "326",
		"country_name" : "1",
		"name" : "Earth",
		"place_type_code" : "19",
		"place_type_name" : "Supername",
		"woeid" : "1"
		},
		...
	]}
```

##### Search for a trend with the specified text. Returns up to the top 10 matching trends as a list. This is useful for auto-complete text boxes.

```python
>> wtt = WhatTheTrend()
>> wtt.search_trend('friday')
>> {"ok": True,
    "data": [
		"#followfriday"
        "Fridays"
        "Follow Friday"
        "#fridaynight"
        "Good Friday"
        "Happy Good Friday"
        "It's Good Friday"
        "Friday Night Lights"
        "#UnFollowFriday"
        "Its Friday"
	]}
```

##### Search for a trend with the specified text. Returns up to the top 10 matching trends along with with their explanation 

```python
>> wtt = WhatTheTrend()
>> wtt.extended_search_trend('friday')
>> {"ok": True,
    "data": [
		{
		"id": "108",
		"name": "#followfriday",
		"dates": {
			"firstTrend": "2009-02-20T03:35:01Z",
			"lastTrend": "2009-03-07T06:40:01Z"
		},
		"links": {
			"url": "http://www.whatthetrend.com/trend/%23followfriday",
			"tinyUrl": "http://wttrend.com/108"
		},
		"blurb": {
			"id": "83",
			"text": "Game in which people recommend people to follow on Twitter, on Fridays.",
			"timestamp": "2009-02-20T03:07:39Z"
		},
		"versions": ""
		},
	]}
```

##### Get all information about a single trend, given a trend id.

```python
>> wtt = get_trend_by_id(141)
>> wtt.get_trendy_locations()
>> {"ok": True,
    "data": {
      "id": "141",
      "name": "#smbottawa",
      "slug": "%23smbottawa",
      "index": "",
      "editCount": "",
      "isNewTrend": "",
      "locked": "0",
      "categoryId": "9",
      "categoryName": "Meme",
      "dates": {
        "firstTrend": "2008-12-11T13:55:00Z",
        "lastTrend": "2009-02-20T16:15:02Z"
      },
      "links": {
        "url": "http:\/\/www.whatthetrend.com\/trend\/%23smbottawa",
        "tinyUrl": "http:\/\/wttrend.com\/141"
      },
      "blurb": {
        "id": "106125",
        "text": "Social Media Breakfast Ottawa",
        "timestamp": "2010-04-21T14:03:03Z",
        "originator": "",
        "relatedUrl": "",
        "score": "0"
      },
      "versions": ""
     }
    }
```

### Responses

If successful:

```python
{
  'ok': True,
  'data': {...}
}
```

If error:

```python
{
  'ok': False,
  'message': 'Something went wrong',
  'status': 401
}
```
