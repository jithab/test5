---
layout: post
title:  Merge Intervals
date:   2023-12-18 12:34:56 +0000
categories: coding python
type: coding
---
{% highlight python %}
def merge_interval(intervals):
    answer = []

    for interval in sorted(intervals):
        if answer and answer[-1][1] >= interval[0]:
            popped = answer.pop()
            interval = [popped[0], max(popped[1], interval[1])]

        answer.append(interval)

    return answer

{% endhighlight %}

{% highlight python %}
def pr(ok): print("Ok" if ok else "Error")

pr(merge_interval([[1, 3], [2, 6], [8, 10], [15, 18]])
   == [[1, 6], [8, 10], [15, 18]])
pr(merge_interval([[1, 4], [4, 5]])
   == [[1, 5]])
{% endhighlight %}