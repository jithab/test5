---
layout: post
title:  Complete Guide to Python String
date:   2024-02-14 12:34:56 +0000
categories: pronotes
type: pronotes
---

## Initialization
{% highlight python %}
str1 = 'Text enclosed with single quotes.' 

str2 = "Text enclosed with double quotes."
{% endhighlight %}

<p>&nbsp;</p>

## Access

- The **in-operator** can be used to check a substring exists in a string.
{% highlight python %}
print("single" in str1)   # output: True
{% endhighlight %}

- The **subscript-operator** can be used for accessing a character using the correspoding index. IndexError-exception will be thrown for non-existing indices.
{% highlight python %}
print(str1[2])   # output: x
{% endhighlight %}

- The **slice-operator** [start:], [start:end], [:end]
  - Negative integer can be used to start from the last. [-start:], [-start:-end], [:-end]
{% highlight python %}
print(str1[2:7])   # output: xt en
{% endhighlight %}

- **Iteration** through characters.

{% highlight python %}
for c in str1:
  print(c)
{% endhighlight %}

<p>&nbsp;</p>

## Update
- You cannot modify a string since it is immutable.

## Methods

- str1.**format**().
{% highlight python %}
msg = "Hello {}!".format("John")
print(msg)   # output: Hello John!
{% endhighlight %}

- str1.**split**(delimeter_str).
{% highlight python %}
print(str1.split(" "))
# output: ['Text', 'enclosed', 'with', 'single', 'quotes.']
{% endhighlight %}

- str1.**replace**(search_str, replace_str).
  - It won't modify the existing string but return the modified string.

{% highlight python %}
new_str = str1.replace("enclosed with", "and")
print(new_str)   # output: Text and single quotes.
{% endhighlight %}

## Operators

- Concatenation operator: **+**
{% highlight python %}
userName = "John"
msg = "Hello " + userName
print(msg)   # output: Hello John
{% endhighlight %}


- Multiplication operator: **&nbsp;*&nbsp;**
{% highlight python %}
msg = 3 * "AB"
print(msg)   # output: ABABAB 
{% endhighlight %}

<p>&nbsp;</p>
<p>&nbsp;</p>

## Interview Questions
---
<p>&nbsp;</p>

**1. When you access a character using subscript operator, Do you get an element of type character or string?**

There is no character type in python. It is a string of length 1.