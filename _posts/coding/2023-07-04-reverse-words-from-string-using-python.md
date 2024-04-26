---
layout: post
title: "Reverse words from a string using Python"
date: 2023-08-21 10:38:21 +0530
categories: interview python coding
type: coding
---

- **Input**: "Here goes what you want in life"
- **Output**: "life in want you what goes Here"
- *Assumption*: Input contains at least one word.
<p>&nbsp;</p><hr/><p>&nbsp;</p>

- Quick code using all buit in functions.
{% highlight python %}
text = "Here goes what you want in life"

words = text.split()
reversed_words = words[::-1] # OR = reversed(words)
reversed_text = " ".join(reversed_words)

print(reversed_text)
{% endhighlight %}
<p>&nbsp;</p><hr/><p>&nbsp;</p>

- **Interviewer**: Rewrite without join().
{% highlight python %}
text = "Here goes what you want in life"

words = text.split()
reversed_words = words[::-1]

reversed_text = reversed_words[0]
for word in reversed_words[1:]:
    reversed_text += " " + word

print(reversed_text)
{% endhighlight %}
<p>&nbsp;</p><hr/><p>&nbsp;</p>

- **Interviewer**: Rewrite without slicing.
{% highlight python %}
text = "Here goes what you want in life"

words = text.split()

reversed_words = []
for reversed_index in range(len(words)-1, -1, -1):
    reversed_words.append(words[reversed_index])

reversed_text = reversed_words[0]
for index in range(1, len(reversed_words)):
    reversed_text += " " + reversed_words[index]

print(reversed_text)
{% endhighlight %}
<p>&nbsp;</p><hr/><p>&nbsp;</p>

- **Interviewer**: Rewrite without split().
{% highlight sh %}
text = "Here goes what you want in life"

reversed_text = ""
next_word = ""
for letter in text:
    if letter == " ":
        reversed_text = " " + next_word + reversed_text
        next_word = ""
    else:
        next_word += letter
reversed_text = next_word + reversed_text

print(reversed_text)
{% endhighlight %}
<p>&nbsp;</p><hr/><p>&nbsp;</p>

- **Interviewer**: Couldn't figure out any other rewrites. Will ask another question.
- **Me**: 😳 