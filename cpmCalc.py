# A wee calculator to work out CPMs, Budgets, Impressions etc.

def workOutCPM(impressions,budget):
	cpmCalc = (budget / impressions) * 1000
	return cpmCalc

def workOutBudget(cpm,impressions):
	budgetCalc = (impressions * cpm) / 1000
	return budgetCalc

def workOutImpressions(cpm,budget):
	impressionsCalc = (budget / cpm) * 1000
	return impressionsCalc

prompt = ">>>"

print "what metric do you want to work out?"
print "Enter CPM, budget, impressions."
metric = raw_input(prompt)

if metric == "cpm":
	print "Okay, you want to work out a CPM"
	print "Please let me know the budget"
	budget = float(raw_input(prompt))
	print "Now let me know the impressions"
	impressions = float(raw_input(prompt))
	print "the CPM is: ", "%.2f" % workOutCPM(impressions,budget)

elif metric == "impressions":
	print "Okay, you want to work out impressions"
	print "Please let me know the CPM"
	cpm = float(raw_input(prompt)) 
	print "Now let me know the budget"
	budget = float(raw_input(prompt))
	print "The impressions are:" "%.0f" % workOutImpressions(cpm,budget)

elif metric == "budget":
	print "Okay, you want to work out the budget"
	print "Please let me know the CPM"
	cpm = float(raw_input(prompt))
	print "Now let me know the impressions"
	impressions = float(raw_input(prompt))
	print "The budget is: " "%.2f" % workOutBudget(cpm,impressions)

else:
	print "You haven't entered a valid function to run"    