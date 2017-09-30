#!/usr/bin/env python

import datetime as dt
from collections import Counter
import twitter
api = twitter.Api(consumer_key="ocmS4FANGXabcRBM5ib3YRFe7",
                  consumer_secret="EzsP8zSqvPJqUn08MgTPQauC52b1wwmV1lme08bzT16r4ZwFNC",
                  access_token_key="14073406-1xkIBNL8pTSq9Zs7ipA6EggaOWkc45LPkaMUCC29e",
                  access_token_secret="HcrK5pxmLH9JhDFN8aUn5aWF49cT2Dm9SZeWxgKwEIvI7")

favs = api.GetFavorites(count=200)
users_liked = [t.user.screen_name for t in favs]

counts = Counter(users_liked)
users_with_likes = [item for item in counts]
counts_sorted = [(counts[item],item) for item in counts if counts[item]>1]
counts_sorted.sort()

if counts_sorted != None:
  for (count,item) in counts_sorted:
    print item,":",count

print "Did not receive likes sorted by activity:"

following = [item.screen_name for item in api.GetFriends()]

unpopular = [item for item in following if item not in users_with_likes]
unpopular_weighted = []
a = dt.datetime.now()
for user in unpopular:
  tweets = api.GetUserTimeline(screen_name=user,count=10)
  if len(tweets) > 0:
    oldest = tweets[-1].created_at
    b = dt.datetime.strptime(tweets[-1].created_at,"%a %b %d %X +0000 %Y")
    delay = (a-b).total_seconds()
    unpopular_weighted.extend([(delay,user)])
    print user,": ", delay

unpopular_weighted.sort()
print unpopular_weighted
for (weight,item) in unpopular_weighted:
  print item,": ", weight
