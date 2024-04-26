---
layout: post
title: "Highest frequency characters in a string using Python"
date: 2023-08-22 11:38:21 +0530
categories: interview python coding
type: coding
---
- **Input**: "the quick brown fox jumped over the lazy dog"
- **Output**: ['e', 'o']
<p>&nbsp;</p><hr/><p>&nbsp;</p>
{% highlight python %}
text = "the quick brown fox jumped over the lazy dog"

letters = {}
for letter in text:
    if letter == " ":
        continue
    if letter not in letters:
        letters[letter] = 0
    letters[letter] = letters[letter] + 1

top_frequency = max(letters.values())

frequent_letters = [l for l, f in letters.items() if f >= top_frequency]
print(frequent_letters)
{% endhighlight %}
<p>&nbsp;</p><hr/><p>&nbsp;</p>

- **Interviewer**: Rewrite without max().
- **Me**: You wanna test my knowledge of such a silly max algorithm? 
- **Interviewer**: 🤓