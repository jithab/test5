---
layout: page
title: Cmd
permalink: /cmd/
---
<ul>
{% for post in site.categories.cmd %}
  <li>
    <a href="{{ post.url }}"><h3>{{ post.title }}</h3></a>
    <!--{{ post.date | date: "%B %d, %Y" }}-->
  </li>
{% endfor %}
</ul>
