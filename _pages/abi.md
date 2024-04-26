---
layout: page
title: Abi Perwad
permalink: /abi/
---

<ul>
{% for post in site.categories.abi %}
  <li>
    <a href="{{ post.url }}">
      <b>{{ post.title }} </b></a> 
      <i>{{ post.date | date: "%b %d, %Y" }}</i>
  </li>
{% endfor %}
</ul>
