---
layout: post
title:  Minimum Number of Arrows to Burst Balloons
date:   2023-12-18 12:34:56 +0000
categories: coding python
type: coding
---
{% highlight python %}
import math

def num_of_shots(points):
    answer = 0
    arrow_x = -math.inf
    points = sorted(points, key=lambda x: x[1])

    for point in points:
        if point[0] > arrow_x:
            answer += 1
            arrow_x = point[1]

    return answer
{% endhighlight %}

{% highlight python %}
def pr(ok): print("Ok" if ok else "Error")

pr(num_of_shots([[10,16],[2,8],[1,6],[7,12]]) == 2)
pr(num_of_shots([[1,2],[3,4],[5,6],[7,8]]) == 4)
pr(num_of_shots([[1,2],[2,3],[3,4],[4,5]]) == 2)
{% endhighlight %}