---
layout: page
title: Pro Notes
permalink: /pro-notes/
---

<ul>
{% for post in site.categories.pronotes %}
  <li>
    <a href="{{ post.url }}">
      <b>{{ post.title }} </b></a> 
      <i>{{ post.date | date: "%b %d, %Y" }}</i>
  </li>
{% endfor %}
</ul>
