---
layout: page
title: Coding
permalink: /coding/
---
<ul>
{% for post in site.categories.coding %}
  <li>
    <a href="{{ post.url }}"><h3>{{ post.title }}</h3></a>
    <!--{{ post.date | date: "%B %d, %Y" }}-->
  </li>
{% endfor %}
</ul>