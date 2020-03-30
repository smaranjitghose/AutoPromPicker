import collections

#The preferrence lists of the boys
preferred_rankings_boys = {
	'ryan': 	['lizzy', 'sarah', 'zoey', 'daniella'],
	'josh': 	['sarah', 'lizzy', 'daniella', 'zoey'],
	'blake': 	['sarah', 'daniella', 'zoey', 'lizzy'],
	'connor': 	['lizzy', 'sarah', 'zoey', 'daniella']
}

#The preferrence lists of the girls
preferred_rankings_girls = {
	'lizzy': 	['ryan', 'blake', 'josh', 'connor'],
	'sarah': 	['ryan', 'blake', 'connor', 'josh'],
	'zoey':  	['connor', 'josh', 'ryan', 'blake'],
	'daniella':	['ryan', 'josh', 'connor', 'blake']
}

#Keeping track of the people that "may" end up together
tentative_engagements = []

#Unmatched boys
unmatched_boys = []


def init_unmatched_boys():
	'''Initialize the arrays of girls and boys to represent 
		that they're all initially unpaired'''
	for boy in preferred_rankings_boys.keys():
	    unmatched_boys.append(boy)


def begin_matching(boy):
	'''Find the first free girl available to a boy at
		any given time'''

	print("DEALING WITH %s" % (boy))
	for girl in preferred_rankings_boys[boy]:

	    #Boolean for whether woman is taken or not
	    taken_match = [
	    	couple for couple in tentative_engagements if girl in couple]

	    if (len(taken_match) == 0):
		    #tentatively engage the man and woman
	        tentative_engagements.append([boy, girl])
	        unmatched_boys.remove(boy)
	        print('%s is no longer a free man and is now tentatively engaged to %s' % (boy, girl))
	        break

	    elif (len(taken_match) > 0):
	        print('%s is taken already..' % (girl))

	        #Check ranking of the current dude and the ranking of the 'to-be' dude
	        current_boy = preferred_rankings_girls[girl].index(taken_match[0][0])
	        potential_boy = preferred_rankings_girls[girl].index(boy)

	        if (current_boy < potential_boy):
	            print('She\'s satisfied with %s..' % (taken_match[0][0]))
	        else:
	            print('%s is better than %s' % (boy, taken_match[0][0]))
	            print('Making %s free again.. and tentatively engaging %s and %s' %
	                  (taken_match[0][0], boy, girl))

	            #The new boy is engaged
	            unmatched_boys.remove(boy)

	            #The old boy is now single
	            unmatched_boys.append(taken_match[0][0])

	            #Update the partner of the girl (tentatively)
	            taken_match[0][0] = boy
	            break


def stable_matching():
	'''Matching algorithm until stable match terminates'''
	while (len(unmatched_boys) > 0):
	    for boy in unmatched_boys:
	        begin_matching(boy)


def main():
	init_unmatched_boys()
	print(unmatched_boys)
	stable_matching()
	print(tentative_engagements)


main()
