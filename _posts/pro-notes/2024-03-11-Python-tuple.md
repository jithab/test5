---
layout: post
title:  Complete Guide to Python Tuple
date:   2024-02-11 12:34:56 +0000
categories: pronotes
type: pronotes
---

## Initialization
{% highlight python %}
t = ()   # an empty tuple

t = ("value1", )   # the comma is mandatory for a single value.
t = "value1",      # same as the above

t = ("value1", "value2")   # t = "value1", "value2"
{% endhighlight %}

<p>&nbsp;</p>

## Access

- The **in-operator** can be used to check an element exists in a tuple.
{% highlight python %}
print("value1" in t)   # output: True
{% endhighlight %}

- The **subscript-operator** can be used for accessing an element using the correspoding index. KeyError-exception will be thrown for non-existing indices.
{% highlight python %}
print(d["key1"])   # output: value1
{% endhighlight %}

- Unpack a Tuple
{% highlight python %}
x, y, z = (12, 34, 56)
{% endhighlight %}

- Iteration.
{% highlight python %}
for e in t:
  print(e)
{% endhighlight %}

<p>&nbsp;</p>

## Update
- You cannot insert or modify a tuple since it is immutable.

## Methods

- t.**index**(element): the index of the element.
- t.**count**(element): the count of the element in the tuple.
<p>&nbsp;</p>
<p>&nbsp;</p>

## Interview Questions
---
<p>&nbsp;</p>

**1. Difference between list and tuple?**
Tuples are immutable whereas lists are mutable. The semantic distinction between them is that tuples are heterogeneous data structures while lists are homogeneous sequences. Tuples have structure, lists have order.
