# find_the_spammers
Sort the twitter users you follow and haven't liked by how active they are.

As a somewhat regular twitter user I felt that a feature was missing to suggest which accounts to unfollow based on disinterest. There are several reasons in my opinion to follow an account but for me the most significant one is the signal to noise ratio.

# Setup
To run the script you need the [python-twitter](https://python-twitter.readthedocs.io/en/latest/index.html) API. Furtheremore, you need to get an API key from Twitter (see instructions [here](https://python-twitter.readthedocs.io/en/latest/getting_started.html)). With that you are good to go.

# What the script does
The script finds all users you follow which you have not liked in your 200 most recent likes (this is limited by the twitter API). For each such user the script fetches the ten most recent tweets which can be considered as a rough estimate of activity/spam level. The script then orders the users by how much they tweet based on that estimate. Based on that information one can start cutting down the noise or move the super-active accounts to a separate list.
