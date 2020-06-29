---
title: Maker Faire Orlando Sponsors
layout: default
permalink: /sponsors
---

{% comment %}
  <img src="assets/images/sponsors/{{sponsor.logo}}" style="max-width:250px">
{% endcomment %}

{% for sponsor in site.data.sponsors.sponsors %}
  <div>{{sponsor.level}}: {{ sponsor.name }}</div>
{% endfor %}

<hr>
<div>
{% assign levels = (site.data.sponsors.sponsors | where: 'active', 'true' | group_by: 'level' | sort: 'name' %}

{% for level in levels %}
  {{level.level}}
    {% for sponsor in level.items %}
      <div>{{sponsor.level}}: {{ sponsor.name }}</div>
    {% endfor %}
{% endfor %}
</div>
