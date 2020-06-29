---
title: Maker Faire Orlando Sponsors
layout: default
permalink: /sponsors
---
<div class="container sponsors-landing">

  <div class="row padbottom">
    <div class="col-xs-12">
      <h2 class="pull-left">2019 Sponsors</h2>
      <a class="sponsors-btn-top" href="/become-a-sponsor/">BECOME A SPONSOR</a>
    </div>
  </div>


  {% for level in site.data.sponsors.sponsorlevels %}
    {% assign sponsors = (site.data.sponsors.sponsors | where: 'active', 'true' | where: 'level', forloop.index | sort: 'name' %}
    {% if sponsors.size > 0 %}
      {% comment %}The next line has an intentional misspelling to match the maker faire theme css{% endcomment %}
      <div class="row spnosors-row">
        <div class="col-xs-12">
          <h2 class="text-center sponsors-type">{{level[forloop.index]}}</h2>
            <div class="faire-sponsors-box">
            {% for sponsor in sponsors %}
              <div class="sponsors-box-lg" id="{{sponsor.name}}"><a href="{{sponsor.url}}" target="_blank"><img src="/assets/images/sponsors/{{sponsor.logo}}" class="img-responsive" style="max-height:150px; width:auto;" alt="{{sponsor.name}}"></a></div>
            {% endfor %}
            </div>
        </div>
      </div>
     {% endif %}
  {% endfor %}


  <div class="row spnosors-row">
    <p style="margin-top: 20px;text-align: center">This project is funded in part by Orange County Government through the Arts &amp; Cultural Affairs Program.<br>
    <img class="alignnone size-full wp-image-25608" src="{{ 'assets/images/site-branding/leaper_150x150.jpg' | relative_url }}" alt="Orange County Arts & Cultural Affairs logo" width="150" height="150">
    </p>
  </div>

</div>
