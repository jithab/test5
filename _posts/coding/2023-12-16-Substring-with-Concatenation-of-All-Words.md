---
layout: post
title:  Substring with Concatenation of All Words
date:   2023-12-16 12:34:56 +0000
categories: coding python
type: coding
---
{% highlight python %}
def find_substring(s, words):

    num_of_words = len(words)
    word_length = len(words[0])
    permuted_words_length = word_length * num_of_words
    answer = []

    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    for i in range(len(s) - permuted_words_length + 1):
    
        found_words_freq = {}
        j = i
        while j < i + permuted_words_length:
            word = s[j: j + word_length]
            if word not in word_frequency:
                break
            found_words_freq[word] = found_words_freq.get(word, 0) + 1
            if found_words_freq[word] > word_frequency[word]:
                break
            j += word_length

        if j - i == permuted_words_length:
            answer.append(i)

    return answer
{% endhighlight %}

{% highlight python %}
def pr(ok): print("Ok" if ok else "Error")


pr([0, 9] == find_substring("barfoothefoobarman", ["foo", "bar"]))
pr([] == find_substring(
    "wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
pr([6, 9, 12] == find_substring(
    "barfoofoobarthefoobarman", ["bar", "foo", "the"]))
{% endhighlight %}