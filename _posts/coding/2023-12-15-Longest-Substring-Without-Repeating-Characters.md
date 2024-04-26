---
layout: post
title:  Longest Substring Without Repeating Characters
date:   2023-12-15 12:34:56 +0000
categories: coding python
type: coding
---
{% highlight python %}
def longest_substring_len(s):
    track = {}
    left_pointer = 0
    max_len = 0

    for right_pointer in range(len(s)):
        letter = s[right_pointer]
        index = track.get(letter, -1)
        if index >= left_pointer:
            left_pointer = index + 1
        max_len = max(max_len, right_pointer - left_pointer + 1)
        track[letter] = right_pointer

    return max_len
{% endhighlight %}

{% highlight python %}
def pr(ok): print("Ok" if ok else "Error")


pr(3 == longest_substring_len("abcabcbb"))
pr(1 == longest_substring_len("bbbbb"))
pr(3 == longest_substring_len("pwwkew"))
{% endhighlight %}