---
layout: default
permalink: /makers
---

<h1>Exhibits</h1>

<ul>

{% for exhibit in site.exhibits %}
    {% if exhibit.status == 1 %}
      <li><a href="{{ exhibit.url }}">{{ exhibit.name }}</a></li>
    {% endif %}
{% endfor %}
</ul>
