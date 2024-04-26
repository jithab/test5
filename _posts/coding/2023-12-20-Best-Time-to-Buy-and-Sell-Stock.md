---
layout: post
title:  Best Time to Buy and Sell Stock
date:   2023-12-20 12:34:56 +0000
categories: coding python
type: coding
---
<p>&nbsp;</p>
#### Leetcode [#121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
<hr /><p>&nbsp;</p>

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

{% highlight python %}
def max_profit(prices):
    profit = 0
    lowest_price = math.inf

    for price in prices:
        profit = max(profit, price - lowest_price)
        lowest_price = min(lowest_price, price)

    return profit
{% endhighlight %}

{% highlight python %}
def pr(ok): print("Ok" if ok else "Error")

pr(5 == max_profit([7,1,5,3,6,4]))
pr(0 == max_profit([7,6,4,3,1]))
{% endhighlight %}

<p>&nbsp;</p><p>&nbsp;</p>
#### Leetcode [#122](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii)
<hr /><p>&nbsp;</p>

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

{% highlight python %}
def max_profit(prices):
    profit = 0
    price_yesterday = math.inf

    for price in prices:
        profit += max(0, price - price_yesterday)
        price_yesterday = price

    return profit
{% endhighlight %}

{% highlight python %}
def pr(ok): print("Ok" if ok else "Error")

pr(7 == max_profit([7,1,5,3,6,4]))
pr(4 == max_profit([1,2,3,4,5]))
pr(0 == max_profit([7,6,4,3,1]))
{% endhighlight %}

<p>&nbsp;</p><p>&nbsp;</p>
#### Leetcode [#123](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii)
<hr /><p>&nbsp;</p>

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

{% highlight python %}
def max_profit(prices):
    delta = math.inf
    buy1 = math.inf
    profit1 = 0
    total_profit = 0

    for price in prices:
        # total_profit= (sell2 - buy2) + (sell1 - buy1)
        total_profit = max(total_profit, price - delta)
        # delta= buy2 - (sell1 - buy1)
        delta = min(delta, price - profit1)
        profit1 = max(profit1, price - buy1)
        buy1 = min(buy1, price)

    return total_profit
{% endhighlight %}

{% highlight python %}
def pr(ok): print("Ok" if ok else "Error")

pr(6 == max_profit([3,3,5,0,0,3,1,4]))
pr(4 == max_profit([1,2,3,4,5]))
pr(0 == max_profit([7,6,4,3,1]))
{% endhighlight %}

<p>&nbsp;</p><p>&nbsp;</p>
#### Leetcode [#188](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv)
<hr /><p>&nbsp;</p>

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

{% highlight python %}
def max_profit(k, prices): # Time:O(nk). Space:O(k)
    sell = [0] * (k + 1)
    delta = [math.inf] * (k + 1)

    for price in prices:
      for i in range(k, 0, -1):
        sell[i] = max(sell[i], price - delta[i])
        delta[i] = min(delta[i], price - sell[i - 1])

    return sell[k]
{% endhighlight %}

{% highlight python %}
def pr(ok): print("Ok" if ok else "Error")

pr(2 == max_profit(2, [2,4,1]))
pr(7 == max_profit(2, [3,2,6,5,0,3]))
{% endhighlight %}