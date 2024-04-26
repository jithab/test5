---
layout: post
title: "Largest Number in an array using Python"
date: 2023-08-21 11:38:21 +0530
categories: interview python coding
type: coding
---

- **Input**: [2, 14, 5, 53, 26, 33, 12, 8, 9]
- **Output**: 53
- *Assumption*: Input contains at least one number.
<p>&nbsp;</p><hr/><p>&nbsp;</p>

- Quick code using max() or list sort()
{% highlight python %}
numbers = [2, 14, 5, 53, 26, 33, 12, 8, 9]
largest = max(numbers)
print(largest)
{% endhighlight %}
<p>&nbsp;</p><hr/><p>&nbsp;</p>

- **Interviewer**: Rewrite without max().
{% highlight python %}
numbers = [2, 14, 5, 53, 26, 33, 12, 8, 9]
largest = -math.inf
for num in numbers:
    if num > largest:
        largest = num
print(largest)
{% endhighlight %}
