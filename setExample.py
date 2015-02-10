from observableset import ObservableSet

def setHandler(event):
	if event.action == 'itemsRemoved':
		print 'Items removed: ' + str(event.items)
	elif event.action == 'itemsAdded':
		print 'Items added: ' + str(event.items)

		
mySet = ObservableSet()
mySet.attach(setHandler)

mySet.add(1)
mySet.add(2)
mySet.add(3)

mySet |= {4,5,6} #Union
mySet &= {3,5,1} #Intersection

mySet.remove(5)