---
layout: post
title:  Complete Guide to Python Comprehensions
date:   2024-02-15 12:34:56 +0000
categories: pronotes
type: pronotes
---

## List Comprehension 

- Print the cubes of the positive integers till 10. 
{% highlight python %}
cubes = [x**3 for x in range(11)]
print(cubes)   # [1, 8, 27, 64, ..., 1000] 
{% endhighlight %}

<p>&nbsp;</p>

- Print the two digit positive integers which are multiplication of 7 or/and 13. 
{% highlight python %}
nums = [x for x in range(10, 100) if x%7==0 or x%13==0]
print(nums)   # [13, 14, 21, 26, ..., 98] 
{% endhighlight %}

<p>&nbsp;</p>

## Dictionary Comprehension
{% highlight python %}
ks = [2, 3, 4, 5, 6, 7]
vs = [8, 27, 125]
p = {k:v for k in ks for v in vs if k**3==v}
print(p)   # {2: 8, 3: 27, 5: 125}
{% endhighlight %}
<p>&nbsp;</p>

## Set Comprehension
- Print unique odd numbers from the list.
{% highlight python %}
nums = [2, 3, 2, 5, 4, 3, 7]
odds = {n for n in nums if n%2==1}
print(odds)   # {3, 5, 7}
{% endhighlight %}
<p>&nbsp;</p>
<p>&nbsp;</p>

<!--- todo: Generator Comprehensions -->

## Interview Questions
---
<p>&nbsp;</p>

**1. Rewrite the following code using list comprehension..**
{% highlight python %}
xs = [2, 4, 6, 8] 
ys = [1, 2, 3, 4]
xys = []
for x in xs:
  for y in ys:
    if x > y:
      xys.append((x, y)) 
print(xys)   # [(2, 1), (4, 1), ..., (8, 4)]
{% endhighlight %}

Answer:
{% highlight python %}
xys = [(x, y) for x in xs for y in ys if x > y] 
{% endhighlight %}

<p>&nbsp;</p>

**2. Transpose the following matrix with list comprehension.**
{% highlight python %}
matrix = [
    [1,2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
{% endhighlight %}
Answer:
{% highlight python %}
transpose = [
  [row[colIndex] for row in matrix] 
  for colIndex in range(len(matrix))
]
print(transpose)
{% endhighlight %}
