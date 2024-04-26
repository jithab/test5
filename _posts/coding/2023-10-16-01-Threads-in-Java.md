---
layout: post
title:  Threads in Java
date:   2023-10-16 01:00:00 +0000
categories: java coding
type: coding
---
{% highlight java %}
public class Main {
    public static void main(String[] args) {
        Thread thread = new MyThread();
        thread.start();
    }
}
{% endhighlight %}

{% highlight java %}
class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Thread started running.");
    }
}
{% endhighlight %}

<p>&nbsp;</p><hr/><p>&nbsp;</p>
- **Interviewer**: Create an empty class called *MyThreadParent*. 
{% highlight java %}
public class Main {
    public static void main(String[] args) {
        Thread thread = new Thread(new MyThread());
        thread.start();
    }
}
{% endhighlight %}

{% highlight java %}
class MyThreadParent {}

class MyThread extends MyThreadParent implements Runnable {
    @Override
    public void run() {
        System.out.println("Runnable started running.");
    }
}
{% endhighlight %}

<p>&nbsp;</p><hr/><p>&nbsp;</p>
- **Interviewer**: What are commonly used Thread class methods?
<p>&nbsp;</p>
**You:**
- **isAlive**(): Tests if the thread is alive.
- **yield**(): Causes the currently executing thread object to temporarily pause and allow other threads to execute.
- **join**(): Waits for a thread to die.

