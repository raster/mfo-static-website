---
title: Maker Faire Orlando Media Coverage
permalink: /media
layout: default
---

# Maker Faire Orlando Media Coverage
Please contact us at any time at [pr@makerfaireorlando.com](mailto:pr@makerfaireorlando.com) to coordinate interviews or event credentials for your features and stories and check out our [Press Kit](/press-kit) for logos, photos and more.

<div>
{%- for events in site.data.mediacoverage.mediacoverage -%}
  {%- for event in events -%}
    <h2>{{ event[1].title }}</h2>
    <ul>
    {%- for story in event[1].stories -%}
      <li> {{story.publisher}}, {{story.date}}: <a href="{{story.url}}">{{story.title}}</a></li>
    {%- endfor -%}
    </ul>
  {%- endfor -%}
{%- endfor -%}
</div>
