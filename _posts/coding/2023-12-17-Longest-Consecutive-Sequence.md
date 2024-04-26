---
layout: post
title:  Longest Consecutive Sequence
date:   2023-12-17 12:34:56 +0000
categories: coding python
type: coding
---
- Store all items in a hash set 
- Go through each item in the hash set
- If the item is the begining of a sequence
- look for remaining items

{% highlight python %}
def longest(nums):
    items = set(nums)
    maxsize = 0

    for item in items:
        if (item - 1) not in items:
            length = 1
            while (current + length) in items:
                length += 1
            maxsize = max(maxsize, length)

    return maxsize

{% highlight python %}

{% endhighlight %}
def pr(ok): print("Ok" if ok else "Error")


pr(4 == longest([100, 4, 200, 1, 3, 2]))
pr(9 == longest([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
{% endhighlight %}
