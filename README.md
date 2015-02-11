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
	print 'Event: ' + event.action + ' occurred'

observableList = ObservableList()
observableList.attach(handler)
```

# Event objects
Every collection emit an event containing a name, and one or more item arrays depending on the event.

ObservableList
--------------

The list emit 3 different events along with the parameters are:
* event.name = 'itemsAdded', event.items , event.index
* event.name = 'itemsUpdated', event.newItems, event.oldItems, event.index
* event.name = 'itemsRemoved', event.items, event.index

ObservableList event example
----------------------------

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

ObservableDict
--------------

ObservableDict emits two different events:
* event.name = 'itemsAdded', event.items
* event.name = 'itemsChanged', event.items
* event.name = 'itemsRemoved', event.items

The items arrays contains named tuples with the following fields:
* key
* value
* oldValue(only for itemsUpdatedEvent)

ObservableDict example
----------------------

```Python
from observabledict import ObservableDict

def dictHandler(event):
	if event.action == 'itemsUpdated':
		print 'The following items has been updated'
		
		for item in event.items:
			print 'Key: ' + str(item.key) + ', value: ' + str(item.value) + ', old Value: ' + str(item.oldValue)
```

In case of itemsAdded/itemsRemoved events the item.oldValue does not exists

ObservableSet
-------------

ObservableSet emits the same events as ObservableList with the exception that no index is included in the event object
since the set is no-ordered collection. The rest stays the same.
