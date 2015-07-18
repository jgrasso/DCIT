#!/usr/env/python coding
# -*- coding: utf-8 -*-

# Authors: C. Clayton Violand & Jessica E. Grasso

import re
import string

def disambiguate(tweets, tagged_tweets, dcons):
	pattern = re.compile(r'[a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/[A-ZÄÖÜẞ]+')
	tagged_tweet_id = re.compile('r') # TODO: PULL OUT 18 DIGIT ID.
	text = open(tagged_tweets).read()

	results = re.findall(pattern,text)
	instances = {}
	for i in results:
		parts = string.split(i,'/')

		if parts[1] in instances.keys():
			continue
		else:
			instances[parts[1]] = (parts[0], parts[2])

	# Add type 0s and finish type 2s.
	# 1 = Connectives distinguishable by POS with 80% Precision (Schneider).
	# 2 = Connectives w/ ngrams POS w/ context.
	# 0 = The rest.
	schneiders = [('denn',1,['KON']),('doch',1,['KON']),('entgegen',1,['APPO','APPR']),('seit',1,['KOUS']),('seitdem',1,['KOUS']),('trotz',1,['APPR']),('während',1,['KOUS']),('wegen',1,['APPO','APPR']),('also',2,),('auch',2,),('außer',2,),('da',2,),('darum',2,),('nebenher',2,),('nur',2,),('so',2,),('sonst',2,),('soweit',2,)]
	for i in range(len(schneiders)):
		if schneiders[i][1] == 1:
			for j in instances:
				if schneiders[i][0] == j:
					if instances[j][1] in schneiders[i][2]:
						pass
						# match instance IDs to IDs in tweets file and add flag property.
		# Add functionality for context Schneiders. For now, just save to run stats.
		elif schneiders[i][1] == 2:
			pass
		# Add funcitonality for rest. For now, just save to run stats.
		else:
			pass

	return tweets

