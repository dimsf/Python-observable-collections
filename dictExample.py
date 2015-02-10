from observabledict import ObservableDict

def dictHandler(event):
	print 'Event: ' + event.action
	
	for item in event.items:
		print(item)

myDict = ObservableDict()
myDict.attach(dictHandler)

#Add some key/values
myDict['akey1'] = 1
myDict['akey2'] = 2
myDict['akey3'] = 3

#Modify values
myDict['akey2'] = 'newValue'

del myDict['akey3']