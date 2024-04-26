---
layout: post
title:  Minimum Size Subarray Sum
date:   2023-12-15 12:34:56 +0000
categories: coding python
type: coding
---
{% highlight python %}
import math

def subarray_length(target, nums):
    left_pointer = 0
    sum_of_nums = 0
    min_len = math.inf

    for right_pointer in range(len(nums)):
        sum_of_nums += nums[right_pointer]
        while sum_of_nums >= target:
            min_len = min(min_len, right_pointer - left_pointer + 1)
            sum_of_nums -= nums[left_pointer]
            left_pointer += 1
    
    return 0 if min_len == math.inf else min_len
{% endhighlight %}

{% highlight python %}
def pr(ok): print("Ok" if ok else "Error")


pr(2 == subarray_length(7, [2, 3, 1, 2, 4, 3]))
pr(1 == subarray_length(4, [1, 4, 4]))
pr(0 == subarray_length(11, [1, 1, 1, 1, 1, 1, 1, 1]))
{% endhighlight %}