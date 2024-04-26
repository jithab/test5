---
layout: post
title:  Python else statement
date:   2024-02-13 12:34:56 +0000
categories: pronotes
type: pronotes
---
Else statment can be used in:

1. if else statment
2. loops
3. try-except statement


## If else statment

- if-else

{% highlight python %}
if random.randint(5, 15) > 10:
  print("Randome number was > 10.")
else:
  print("Randome number was <= 10.")
{% endhighlight %}


## Loops

- for-in loop

{% highlight python %}
for i in range(1, random.randint(5, 15)):
  if i > 10:
    break
  print(i)
else:
    print("Printed all the numbers!")
{% endhighlight %}

- while loop
{% highlight python %}
import random
i = 1
end = random.randint(5, 15)
while i < end:
  if i > 10:
    break
  print(i)
else:
    print("Printed all the numbers!")
{% endhighlight %}

<p>&nbsp;</p>

## Try except statement

- try-except
{% highlight python %}
try:
   pass
except:
  print("Unreachale code!")
else:
  print("First print!")
finally:
  print("Second print!")
{% endhighlight %}

<p>&nbsp;</p>

## Interview Questions
---
<p>&nbsp;</p>

**1. When will else-block be excuted in a loop?**

When no break occurs.

**2. When will else-block be excuted in a try-except statement?**

When no exception occurs.

**3. When will else-block be excuted in a try-catch statment - after or before finaly statment?**

Before finaly. 