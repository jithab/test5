---
layout: post
title:  Sum of digits of a number in Java
date:   2023-10-12 01:38:00 +0000
categories: java coding
type: coding
---
{% highlight java %}
public class Main {
    public static void main(String[] args) {

        int number = -123456;

        if(number < 0)
            number = -number;

        int sum = 0;
        while (number > 0) {
            sum += number % 10;
            number /= 10;
        }
        System.out.println(sum);
    }
}
{% endhighlight %}
- Time Complexity: O(log₁₀N) ; N is the number.
- Space Complexity: O(1).