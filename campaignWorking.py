# A script to work out campaign values and metrics

from __future__ import division

prompt = ">>>"

def cost_per_unique(campaign_value, campaign_uniques):
	cost_per_unique = campaign_value / campaign_uniques
	return cost_per_unique

def cost_per_minute(campaign_value,dwell_time):
	cost_per_minute = campaign_value / dwell_time
	return cost_per_minute

def cpm(campaign_value,impressions):
	cpm = (campaign_value / impressions) * 1000
	return cpm

def cpc(campaign_value,clicks):
	cpc = campaign_value / clicks
	return cpc

print "Campaign Name"
campaign_name = raw_input(prompt)

print "Campaign Value"
campaign_value = float(raw_input(prompt))

print "Campaign Uniques"
campaign_uniques = float(raw_input(prompt))

print "Total Dwell Time"
dwell_time = float(raw_input(prompt))

print "Total Impressions"
impressions = float(raw_input(prompt))

print "Total Clicks"
clicks = float(raw_input(prompt))

print "======"

print "For the campaign", campaign_name
print "The cost per unique is: $", "%.2f" % cost_per_unique(campaign_value, campaign_uniques) 
print "The cost per minute is: $", "%.2f" % cost_per_minute(campaign_value,dwell_time)
print "The CPM of this campaign is: $", "%.2f" % cpm(campaign_value,impressions)
print "The CPC of this campaign is: $", "%.2f" % cpc(campaign_value,clicks)

print "======"


