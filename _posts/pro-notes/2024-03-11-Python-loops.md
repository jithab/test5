---
layout: post
title:  Complete Guide to Python Loops
date:   2024-02-13 12:34:56 +0000
categories: pronotes
type: pronotes
---
There are two loop statments in python.

1. while
2. for-in


## while

- Print the sequence 1, 5, 13, 29, ... 8189.
{% highlight python %}
num = 1
while num <= 8189:
  print(num)
  num = 2*num + 3
{% endhighlight %}

<p>&nbsp;</p>

## for-in

- Print the sequence 3, 7, 11, 15, ... 99.
{% highlight python %}
for i in range(3, 100, 4):
  print(i)
{% endhighlight %}

<p>&nbsp;</p>


## Interview Questions
---
<p>&nbsp;</p>

**1. What are the three python keywords related to python loops?**
1. break
2. continue
3. else

<p>&nbsp;</p>

**2. When will else-block be excuted in a loop?**

when no break occurs.
{% highlight python %}
import random

for i in range(1, random.randint(5, 15)):
  if i > 10:
    break
  print(i)
else:
    print("Printed all the numbers!")
{% endhighlight %}