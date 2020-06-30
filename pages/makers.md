---
layout: default
---


<h1>Exhibits (generated from JSON)</h1>

<ul>
{% for exhibit in site.data.exhibits %}
    <li><a href="{{ exhibit.project_name | datapage_url: 'exhibits' }}">{{exhibit.project_name}}</a></li>
{% endfor %}
</ul>
