---
layout: post
title: "Second and third largest Numbers in an array using Python"
date: 2023-08-21 12:38:21 +0530
categories: interview python coding
type: coding
---

- **Input**: [2, 14, 5, 53, 26, 33, 53, 33, 12]
- **Output**: 33 (second largest), 26 (third largest)
- *Assumption*: Input contains at least two or three numbers.

- **Interviewer**: Find second largest number.
<p>&nbsp;</p><hr/><p>&nbsp;</p>

- Quick code using list sorted() and set()
{% highlight python %}
numbers = [2, 14, 5, 53, 26, 33, 53, 33, 12]
sorted_unique_numbers = sorted(set(numbers))
second_largest = sorted_unique_numbers[-2]
print(second_largest)
{% endhighlight %}
<p>&nbsp;</p><hr/><p>&nbsp;</p>

- **Interviewer**: Rewrite without sorted() and set().
{% highlight python %}
numbers = [2, 14, 5, 53, 26, 33, 53, 33, 12]
largest = second_largest = -math.inf
for num in numbers:
    if num == largest:
        continue
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest:
        second_largest = num
print(second_largest)
{% endhighlight %}
<p>&nbsp;</p><hr/><p>&nbsp;</p>

- **Interviewer**: Rewrite the code to find the third largest.
{% highlight python %}
numbers = [2, 14, 5, 53, 26, 33, 53, 33, 12]
largest = second_largest = third_largest = -math.inf
for num in numbers:
    if num == largest:
        pass
    elif num > largest:
        third_largest = second_largest
        second_largest = largest
        largest = num
    elif num == second_largest:
        pass
    elif num > second_largest:
        third_largest = second_largest
        second_largest = num
    elif num > third_largest:
        third_largest = num

print(third_largest)
{% endhighlight %}

- **Interviewer**: Why did you use *pass* instead of *continue* ?
- **Me**: pass 
- **Interviewer**: What? My question is: why did you use *pass*?
- **Me**: I said **pass**, which means move to the next question!  
- **Interviewer**: 🤓
