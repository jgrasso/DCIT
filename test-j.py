#!/usr/bin/python

# test-j.py
# Authors: C. Clayton Violand & Jessica E. Grasso

from get_dcons import dcon_scrape
from get_tweets import tweet_scrape
from get_matches_singles import get_matches_singles
from get_matches_phrasals import get_matches_phrasals
from get_stats import get_stats
from get_convos import convo_scrape
 
def main():
	# Get list of Tweet objects.
	#tweets = tweet_scrape()

	# Get list of conversation pairs
	convos = convo_scrape()
	
	# print convos to file
	f = open('testing.txt','w')
	for c in convos:
		f.write(c.encode('utf8'))
		f.write('\n')
	f.close()


"""
def main():
	# Get list of Tweet objects.
	tweets = tweet_scrape()

	# Get list of Conversations amongst Tweets.
	#convos = convo_compile(tweets)

	# Get list of Discourse Connective objects.
	dcons = dcon_scrape()

	# Check for occurances of Discourse Connectives (type=="single") in Tweets.
	matches_singles, num_dc = get_matches_singles(tweets, dcons)

	# Check for occurances of Discourse Connectives (type=="phrasal") in Tweets.
	matches_phrasals = get_matches_phrasals(tweets, dcons)

	# Get some statistics / info about the connectives
	get_stats(dcons, matches_singles, 10, 'a')
"""

if __name__ == "__main__":
	main()
