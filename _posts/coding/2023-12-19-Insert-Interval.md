---
layout: post
title:  Insert Interval
date:   2023-12-19 12:34:56 +0000
categories: coding python
type: coding
---
{% highlight python %}
def insert_interval(intervals, new_interval):
    answer = []

    for inter in intervals:
        # insert new interval if current interval ends 
        # on or after new after interval starts  
        if new_interval and new_interval[0] <= inter[1]:
            answer.append(new_interval)
            new_interval = None

        # Combine current interval with last interval if required. 
        if answer and inter[0] <= answer[-1][1]:
            popped = answer.pop()
            inter = [min(inter[0], popped[0]), max(inter[1], popped[1])]

        answer.append(inter)

    if new_interval:
        answer.append(new_interval)

    return answer
{% endhighlight %}

{% highlight python %}
def pr(ok): print("Ok" if ok else "Error")

pr(insert_interval([[1, 3], [6, 9]], [2, 5])
   == [[1, 5], [6, 9]])
pr(insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
   == [[1, 2], [3, 10], [12, 16]])
{% endhighlight %}