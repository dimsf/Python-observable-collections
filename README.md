# Python-observable-collections

Introduction
------------
This is an implementation of observable collections for Python, which allows attaching handlers to Python collections in order to be notified when change in the underlying data occurs. Currently ObservableSet, ObservableList and ObservableDict are supported. 

All three collecitons raise a custom event object containing an action string and one or more item arrays depending on the action.

Usage
-----

In order to be notified for a data change in an observable collection you call the attach method.

```Python
from observablelist import ObservableList

def handler(event):
	print 'An event occured'

observableList = ObservableList()
observableList.attach(handler)
```

# Event objects
Every collection emit an event containing a name, and one or more item arrays depending on the event.

List events
-----------
The list emit 3 different events with event action name as:
* itemsAdded
* itemsUpdated
* itemsRemoved

In itemsUpdated and itemsRemoved an array is passed in event.items containing the items added/removed along with the event.index containing the index here the items added/removed.

In itemsUpdated event, arrays event.newItems and event.oldItems are passed representing the new and old items.

An ObservableList example
-------------------------

```Python
from observablelist import ObservableList

def listHandler(event):
	if event.action == 'itemsUpdated':
		print event.action + ', old items: ' + str(event.oldItems) + ' new items: ' + str(event.newItems) + ' at index: ' + str(event.index)
	elif event.action == 'itemsAdded' or event.action == 'itemsRemoved':
		print(event.action + ', items: ' + str(event.items) + ' at index: ' + str(event.index))

myList = ObservableList()
myList.attach(listHandler)

#Do some mutation actions, just like normal lists.
myList.append(10)
myList.insert(3, 0)

myList.extend([11,12,13])
myList[0:4:2] = [50,51]

del myList[1]
myList.reverse()
```
