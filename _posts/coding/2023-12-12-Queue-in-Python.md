---
layout: post
title:  Queue in Python
date:   2023-12-12 01:23:45 +0000
categories: coding python
type: coding
---
{% highlight python %}
class Item:
    def __init__(self, data):
        self.data = data
        self.next = None
{% endhighlight %}

{% highlight python %}

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):

        item = Item(data)
        if self.rear is None:
            self.rear = item
            self.front = self.rear
        else:
            self.rear.next = item
            self.rear = item

    def dequeue(self):

        if self.front is None:
            return None

        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None

        return data
{% endhighlight %}

{% highlight python %}
queue = Queue()
print(queue.dequeue())  # None
queue.enqueue(3)
queue.enqueue(4)
print(queue.dequeue())  # 3
queue.enqueue(5)
print(queue.dequeue())  # 4
print(queue.dequeue())  # 5
print(queue.dequeue())  # None
queue.enqueue(6)
print(queue.dequeue())  # 6
print(queue.dequeue())  # None
{% endhighlight %}