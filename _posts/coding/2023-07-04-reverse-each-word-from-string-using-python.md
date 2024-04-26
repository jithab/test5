---
layout: post
title: "Reverse each word from a string using Python"
date: 2023-08-21 13:38:21 +0530
categories: interview python coding
type: coding
---
- **Input**: "Here goes what you want in life"
- **Output**: "ereH seog tahw uoy tnaw ni efil"
- *Assumption*: Input contains at least one word.
<p>&nbsp;</p><hr/><p>&nbsp;</p>

- Quick code using all buit in functions.
{% highlight python %}
text = "Here goes what you want in life"

words = text.split()
reversed_words = [word[::-1] for word in words]
reversed_text = " ".join(reversed_words)

print(reversed_text)
{% endhighlight %}
<p>&nbsp;</p><hr/><p>&nbsp;</p>

- **Interviewer**: Rewrite without join().
{% highlight python %}
text = "Here goes what you want in life"

words = text.split()

reversed_text = words[0][::-1]
for word in words[1:]:
    reversed_text += " " + word[::-1]

print(reversed_text)
{% endhighlight %}
<p>&nbsp;</p><hr/><p>&nbsp;</p>

- **Interviewer**: Rewrite without slicing.
{% highlight python %}
text = "Here goes what you want in life"

reversed_text = ""
next_word = ""
for letter in text:
    if letter == " ":
        reversed_text += next_word + " "
        next_word = ""
    else:
        next_word = letter + next_word
reversed_text += next_word

print(reversed_text)
{% endhighlight %}

