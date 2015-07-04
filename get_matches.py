#!/usr/bin/env python

# get_matches.py
# Authors: C. Clayton Violand & Jessica E. Grasso

def get_matches(tweets, dcons, verbose = False, write_xml = False):
	separables = [i for i in dcons if i.sep == "discont"]
	matches_separables = []
	hit_count_separables = 0 # number of discontinuous Discourse Connectives

	phrasals = [i for i in dcons if i.type == "phrasal" and i.sep == "cont"]
	matches_phrasals = []
	hit_count_phrasals = 0	# number of phrasal Discourse Connectives

	singles = [i for i in dcons if i.type == "single" and i.sep == "cont"]
	matches_singles = []
	hit_count_singles = 0	# number of single Discourse Connectives

	tweet_hit_count = 0		# number of Tweets containing a Discourse Connective.
	tweet_trigger = False

	for t in tweets:
		tweet_trigger = False

		for k in separables:
			if (" " + k.part_one + " ") in t.raw and (" " + k.part_two + " ") in t.raw and t.raw.find(k.part_one) < t.raw.find(k.part_two):
				tweet_trigger = True
				hit_count_separables += 1
				matches_separables.append((t,k))

				# Remove Separables before looking for Continuous.
				########
				t.raw = t.raw.replace(k.part_one, '')
				t.raw = t.raw.replace(k.part_two, '')
				########

		for p in phrasals:
			if p.part_one in t.raw:
				tweet_trigger = True
				hit_count_phrasals += 1
				matches_phrasals.append((t,p))

				# Remove Phrasals before looking for Singles.
				########
				t.raw = t.raw.replace(p.part_one, '')
				########

		for s in singles:
			if s.part_one in t.raw:
				tweet_trigger = True
				hit_count_singles += 1
				matches_singles.append((t,s))

		if tweet_trigger == True:
			tweet_hit_count += 1
			t.has_dc = True
	
	matches = matches_singles + matches_phrasals + matches_separables
	hit_count = hit_count_singles + hit_count_phrasals + hit_count_separables
	ratio = tweet_hit_count / float(len(tweets))

	if verbose:
		print
		print "--SUMMARY--"
		print "-----------------------------------"
		print "Pre-disambiguation"
		print "--------------------------------------------------------------------"
		print "Found %d Discourse Connectives amongst %d Tweets." % (hit_count, len(tweets))
		print "Found a Discourse Connective in %d out of %d Tweets." % (tweet_hit_count, len(tweets))
		print "Tweet Saturation is %f." % ratio
		print "--------------------------------------------------------------------"
		print "Discourse Connectives of type = 'continuous single': %d " % len(matches_singles)
		print "Discourse Connectives of type = 'continuous phrasal: %d" % len(matches_phrasals)
		print "Discourse Connectives of type = 'discontinuous': %d " % len(matches_separables)
		print "--------------------------------------------------------------------"
		print

	return matches
