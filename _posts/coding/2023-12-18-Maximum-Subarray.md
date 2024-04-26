---
layout: post
title:  Maximum Subarray
date:   2023-12-18 12:34:56 +0000
categories: coding python
type: coding
---
{% highlight python %}
import math

def max_sub_array(nums):
    ans = -math.inf
    summ = 0

    for num in nums:
        summ = max(num, summ + num)
        ans = max(ans, summ)

    return ans
{% endhighlight %}

{% highlight python %}
def pr(ok): print("Ok" if ok else "Error")

pr(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]) == 6)
pr(max_sub_array([1]) == 1)
pr(max_sub_array([5,4,-1,7,8]) == 23)
{% endhighlight %}