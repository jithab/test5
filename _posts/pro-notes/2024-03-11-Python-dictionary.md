---
layout: post
title:  Complete Guide to Python Dictionary
date:   2024-02-11 12:34:56 +0000
categories: pronotes
type: pronotes
---

## Initialization
{% highlight python %}
d = {
    "key1": "value1", 
    "key2": "value2"
}
{% endhighlight %}

<p>&nbsp;</p>

## Access

- The **in-operator** can be used to check a key exists in a dictionary.
{% highlight python %}
print("key3" in d)   # output: False
{% endhighlight %}

- The **subscript-operator** can be used for accessing existing keys. KeyError-exception will be thrown for non-existing keys.
{% highlight python %}
print(d["key1"])   # output: value1
{% endhighlight %}

- The **get-method** can also be used to access values with support for a default value. The default value is for non-existing keys.
{% highlight python %}
print(d.get("key3", "default-value"))   # output: default-value
{% endhighlight %}

- d.**keys**() : The list of keys, in arbitrary order.
{% highlight python %}
print(d.keys())   # output: dict_keys(['key1', 'key2'])
{% endhighlight %}

- d.**values**() : The list of values.
{% highlight python %}
print(d.values())   # output: dict_values(['value1', 'value2'])
{% endhighlight %}

- d.**items**(): The list of (key, value) tuple pairs.
{% highlight python %}
for k, v in d.items():
  print(k, v)
{% endhighlight %}

<p>&nbsp;</p>

## Update
- Use the subscript-operator for updating any value or adding new value.
{% highlight python %}
d["newkey"] = "newkeyValue"
d["exisitngKey"] = "newValue"
{% endhighlight %}

- d.**update**(anotherDict): Adds anotherDict's key-values pairs to d.

{% highlight python %}
d = { "k1": "v1", "k2": "v2" }
anotherDict = { "k2": "nv2", "k3": "nv3" }

d.update(anotherDict)

print(d)   # output: {'k1': 'v1', 'k2': 'nv2', 'k3': 'nv3'}
{% endhighlight %}

<p>&nbsp;</p>
<p>&nbsp;</p>

## Interview Questions
---
<p>&nbsp;</p>

**1. What are characteristics of the dictionary key?**

- keys can be any immutable type; strings and numbers can always be keys.
- Tuples can be used as keys if they contain only immutable items like strings, numbers, etc. If a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.
- You can’t use a list as a key, since lists are mutable.


**2. What is the difference between using subscript-operator and the get-method in a dictionary?**

Both can be used to access the value of a key. However, subscript operator will throw  KeyError if the key doesn't exist whereas get-method will return None if the key doesn’t exist. Moreover, the second argument to get-method is the default value if the key doesn’t exist.