---
layout: post
title:  Count of the digits of a number in Java
date:   2023-10-12 02:38:00 +0000
categories: java coding
type: coding
---
{% highlight java %}
public class Main {
    public static void main(String[] args) {

        int number = -123456;

        if(number < 0)
            number = -number;

        int count = number == 0 ? 1 : 0;
        while (number > 0) {
            number /= 10;
            count++;
        }
        System.out.println(sum);
    }
}
{% endhighlight %}

- Time Complexity: O(log₁₀N) ; N is the number.
- Space Complexity: O(1).
