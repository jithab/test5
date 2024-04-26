---
layout: post
title: "Left or Right rotation in-place using Python"
date: 2023-08-22 12:34:56 +0000
categories: interview python coding
type: coding
---
- **Input**: [1, 2, 3, 4, 5, 6, 7, 8, 9]
- **Output Left shift by 4**: [5, 6, 7, 8, 9, 1, 2, 3, 4]
- **Output Right shift by 5**: [5, 6, 7, 8, 9, 1, 2, 3, 4]
<p>&nbsp;</p><hr/><p>&nbsp;</p>
- **Interviewer**: Left shift by 4 and Right shift by 5
{% highlight python %}
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
left_shifts = 4
right_shifts = 5

left = data[left_shifts:]+ data[:left_shifts]
right = data[-right_shifts:]+ data[:-right_shifts]

print("left: ", left)
print("right: ", right)
{% endhighlight %}
<p>&nbsp;</p><hr/><p>&nbsp;</p>
- **Interviewer**: Left shift by 4 in-place, without slicing
{% highlight python %}
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shifts = 4

shifts = shifts % (len(data))

# Reverse entire array
for i in range(len(data)//2):
    tmp = data[i]
    data[i] = data[-i-1]
    data[-i-1] = tmp

shifts = len(data)-shifts

# Reverse first k items
for i in range(shifts//2):
    tmp = data[i]
    data[i] = data[shifts-i-1]
    data[shifts-i-1] = tmp

# Reverse the rest
for i in range((len(data)-shifts)//2):
    tmp = data[shifts+i]
    data[shifts+i] = data[-i-1]
    data[-i-1] = tmp

print(data)
{% endhighlight %}
<p>&nbsp;</p><hr/><p>&nbsp;</p>

- **Interviewer**: Right shift by 5 in-place, without slicing
{% highlight python %}
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shifts = 5

shifts = shifts % (len(data))

# Reverse entire array
for i in range(len(data)//2):
    tmp = data[i]
    data[i] = data[-i-1]
    data[-i-1] = tmp

# Reverse first k items
for i in range(shifts//2):
    tmp = data[i]
    data[i] = data[shifts-i-1]
    data[shifts-i-1] = tmp

# Reverse the rest
for i in range((len(data)-shifts)//2):
    tmp = data[shifts+i]
    data[shifts+i] = data[-i-1]
    data[-i-1] = tmp

print(data)
{% endhighlight %}
<p>&nbsp;</p><hr/><p>&nbsp;</p>