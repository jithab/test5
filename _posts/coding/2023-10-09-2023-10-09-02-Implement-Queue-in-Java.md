---
layout: post
title:  Implement Queue in Java
date:   2023-10-09 02:38:00 +0000
categories: java coding
type: coding
---

{% highlight java %}
package in.perwad.queue;

public class Main {
    public static void main(String[] args) {

        Queue<Integer> queue = new Queue<>();

        for(int item : new int [] {321, 123, 231})
            queue.enqueue(item);

        while (!queue.empty())
            System.out.println(queue.dequeue());
            // output: 321, 123, 231
    }
}
{% endhighlight %}

{% highlight java %}
class Queue<ItemDataType>  {
    Item<ItemDataType> front = null;
    Item<ItemDataType> rear = null;

    public void enqueue(ItemDataType data) {
        Item<ItemDataType> item = new Item<>(data, rear);
        if(rear != null)
            rear.setFrontItem(item);
        rear = item;
        if(front == null)
            front = rear;
    }

    public ItemDataType dequeue() {
        ItemDataType data = front.getData();
        front = front.getFrontItem();
        return data;
    }

    public boolean empty() {
        return front == null;
    }
}
{% endhighlight %}

{% highlight java %}
class Item<DataType>  {

    private final DataType data;
    private Item frontItem;
    private final Item backItem;

    public Item(DataType data,  Item nextItem) {
        this.data = data;
        this.backItem = nextItem;
    }

    public DataType getData() {
        return data;
    }

    public void setFrontItem(Item prevItem) {
        this.frontItem = prevItem;
    }

    public Item getFrontItem() {
        return frontItem;
    }
}
{% endhighlight %}