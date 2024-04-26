---
layout: post
title:  Fibonacci Numbers in Java
date:   2023-10-12 03:38:00 +0000
categories: java coding
type: coding
---
{% highlight java %}
public class Main {
    public static void main(String[] args) {

        int count = 7;

        int a = -1, b = 1;
        for (int i = 1; i <= count; i++) {
            int next = a + b;
            a = b;
            b = next;
            System.out.println(b);
        }
    }
}
{% endhighlight %}
