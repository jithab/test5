---
layout: post
title:  Singleton design pattern in Java
date:   2023-10-11 01:38:00 +0000
categories: java coding
---
{% highlight java %}
public class Main {
    public static void main(String[] args) {

        Singleton x = Singleton.getInstance();
        Singleton y = Singleton.getInstance();
        
        System.out.println("The same objects: " + (x == y)); // true
    }
}
{% endhighlight %}

{% highlight java %}
class Singleton {

    private Singleton(){};
    private static Singleton INSTANCE = new Singleton();

    public static Singleton getInstance() {
        return INSTANCE;
    }
}
{% endhighlight %}

<p>&nbsp;</p><hr/><p>&nbsp;</p>
- **Interviewer**: Go with Lazy initialization.
{% highlight java %}
class Singleton {

    private Singleton(){};
    private static Singleton INSTANCE;

    public static Singleton getInstance() {
        if (INSTANCE == null)
            INSTANCE = new Singleton();        
        return INSTANCE;
    }
}
{% endhighlight %}

<p>&nbsp;</p><hr/><p>&nbsp;</p>
- **Interviewer**: Support multi-threading.
{% highlight java %}
class Singleton {

    private Singleton(){};
    private static Singleton INSTANCE;

    public static Singleton getInstance() {

        if (INSTANCE == null) {
            synchronized (Singleton.class) {
                if (INSTANCE == null)
                    INSTANCE = new Singleton();
            }
        }
        return INSTANCE;
    }
}
{% endhighlight %}