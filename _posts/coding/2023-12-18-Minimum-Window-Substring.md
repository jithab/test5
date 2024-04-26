---
layout: post
title:  Minimum Window Substring
date:   2023-12-18 12:34:56 +0000
categories: coding python
type: coding
---
{% highlight python %}
import math

def min_window(s, t):

    min_len = math.inf
    min_index = 0
    left_pointer = 0
    valid_chars_count = 0
    tset = {}
    for char in t:
        tset[char] = tset.get(char, 0) + 1

    for right_pointer in range(len(s)):
        char = s[right_pointer]
        if char not in tset:
            continue

        tset[char] -= 1
        if tset[char] >= 0:
            valid_chars_count += 1
        if valid_chars_count != len(t):
            continue

        # increase the left_pointer if possible
        while True:
            schar = s[left_pointer]
            if schar in tset:
                if tset[schar] == 0:
                    break
                tset[schar] += 1
            left_pointer += 1

        new_min_len = right_pointer - left_pointer + 1
        if new_min_len < min_len:
            min_len = new_min_len
            min_index = left_pointer

    return "" if min_len == math.inf else s[min_index:min_index + min_len]
{% endhighlight %}

{% highlight python %}
def pr(ok): print("Ok" if ok else "Error")


pr("BANC" == min_window("ADOBECODEBANC", "ABC"))
pr("a" == min_window("a", "a"))
pr("" == min_window("a", "aa"))
{% endhighlight %}