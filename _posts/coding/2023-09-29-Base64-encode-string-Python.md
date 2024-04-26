---
layout: post
title:  Base64 encode a string in Python
date:   2023-09-29 01:38:00 +0000
categories: python coding
type: coding
---
- **Input**: "Many hands make light work."
- **Output**: "TWFueSBoYW5kcyBtYWtlIGxpZ2h0IHdvcmsu"
- *Base64 alphabets order*: A-Z a-z 0-9 + /
<p>&nbsp;</p><hr/><p>&nbsp;</p>

{% highlight python %}
input = "Many hands make light work."

def base64(num):
    if num < 26:
        return chr(ord('A') + num)
    elif num < 52:
        return chr(ord('a') + num - 26)
    elif num < 62:
        return chr(ord('0') + num - 52)
    elif num == 62:
        return "+"
    elif num == 63:
        return "/"
    else:
        raise Exception(num)


inputBinaryString = ""

for letter in input:
    inputBinaryString += str(bin(ord(letter)))[2:].zfill(8)


base64Output = ""

for index in range(0, len(inputBinaryString), 6):
    base64Output += base64(int(inputBinaryString[index:index+6],2))

print(base64Output)
{% endhighlight %}