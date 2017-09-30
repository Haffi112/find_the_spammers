#!/usr/bin/env python

import datetime as dt
from collections import Counter
import twitter
api = twitter.Api(consumer_key="SEE README",
                  consumer_secret="SEE README",
                  access_token_key="SEE README",
                  access_token_secret="SEE README")

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
