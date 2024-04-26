---
layout: post
title:  Majority Element with Boyer–Moore majority vote algorithm
date:   2023-12-20 12:34:56 +0000
categories: coding python algorithm
type: coding
---
This algorithm finds **a majority element,** if there is one: that is, an element that occurs repeatedly **for more than half of the elements** of the input in linear time **O(n)** and a constant space **O(1)** .

{% highlight python %}
def majority_element(nums):
    answer = None
    count = 0

    for num in nums:
        if count == 0:
            answer = num
        count += (1 if num == answer else -1)

    return answer # assumes a majority element always exists
{% endhighlight %}

{% highlight python %}
def pr(ok): print("Ok" if ok else "Error")

pr(2 == majority_element([2, 2, 1, 1, 1, 2, 2]))
pr(3 == majority_element([3,2,3]))
{% endhighlight %}

<p>&nbsp;</p>

A majority element is not equal to the most frequent element.  

{% highlight python %}
majority_element([3, 2, 3, 2, 1, 3]) # Return: 1
{% endhighlight %}

<p>&nbsp;</p>

If you don't know whether there is a majority element and you want to return  the majority element if there exists; Otherwise return None. Make a second pass through the data to verify that the element is a majority. 

{% highlight python %}
    count = 0
    for num in nums:
        if num == answer:
            count += 1

    if count <= len(nums) // 2:
        answer = None
{% endhighlight %}

<p>&nbsp;</p>

**References:**
- <https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm>
- <https://www.geeksforgeeks.org/boyer-moore-majority-voting-algorithm/>
- <https://leetcode.com/problems/majority-element/>
- <https://walkccc.me/LeetCode/problems/0169/#__tabbed_1_3>