# Python-observable-collections
This is an implementation of observable collections for Python, in order to attach handlers to be notified when change in the underlying data occurs. Currently ObservableSet, ObservableList and ObservableDict are supported.

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
