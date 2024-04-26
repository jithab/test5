---
layout: post
title:  Implement Stack in Java
date:   2023-10-09 01:38:00 +0000
categories: java coding
type: coding
---

{% highlight java %}
package in.perwad.stack;

public class Main {
    public static void main(String[] args) {

        Stack<Integer> stack = new Stack<>();

        for(int item : new int [] {321, 123, 231})
            stack.push(item);

        while (!stack.empty())
            System.out.println(stack.pop());
            // output: 231 123 321
    }
}
{% endhighlight %}

{% highlight java %}
class Stack<StackDataType>  {
    Item<StackDataType> top = null;

    public void push(StackDataType data) {
        top = new Item<>(data, top);
    }

    public StackDataType pop() {
        StackDataType data = top.getData();
        top = top.getNextItem();
        return data;
    }

    public boolean empty() {
        return top == null;
    }

}
{% endhighlight %}

{% highlight java %}
class Item<DataType>  {

    private final DataType data;
    private Item nextItem;

    public Item(DataType data, Item nextItem) {
        this.data = data;
        this.nextItem = nextItem;
    }

    public Item getNextItem() {
        return nextItem;
    }

    public DataType getData() {
        return data;
    }
}
{% endhighlight %}