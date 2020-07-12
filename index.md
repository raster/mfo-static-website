---
title: Welcome to Maker Faire Orlando!
permalink: /
layout: full-width


carousel: true
carousel-delay: 5000
carousel-controls: true
carousel-slides:
  - image: /assets/images/slider/welcome-to-maker-faire.jpg  
    caption: Welcome to Maker Faire!
    url: /welcome-to-maker-faire/

  - image: /assets/images/slider/retro-computers-kid-cropped.jpg  
    caption: Inspire the future!
    url: /makers/

  - image: /assets/images/slider/muralist-cropped.jpg
    caption: See art in action!
    url: /makers/

  - image: /assets/images/slider/Ghost-busters-cropped.jpg
    caption: Meet like minded makers!
    url: /makers/

  - image: /assets/images/slider/mold-a-makey-cropped.jpg
    caption: Make stuff!
    url: /makers/?category=workshop
---

{% capture cta_event_text %}{{ site.event_date_descr }} – {{ site.event_location_descr }}{% endcapture %}
{% include cta-panel-widget.html cta_text=cta_event_text cta_url=site.cta_event_url %}


{% include what-is-maker-faire.html %}
{% include makey-border.html %}

<section class="Maker Faire Orlando 2020">
  <div class="container">
    <div class="row text-center">
      <div class="title-w-border-y">
        <h2>Maker Faire Orlando 2020</h2>
        </div>
        </div>
        <div class="row">
        <div class="col-md-6 col-md-offset-3">
        <p class="text-center">2020 has been a year of unprecedented challenges that have affected all facets of life including events and gatherings.
        The Maker Faire Orlando team continues to monitor local and state guidelines while planning for an event in late 2020. We've shifted the event into December in order to have even better outdoor temperatures, and we are exploring new ways to use the outdoor spaces at the Central Florida Fairgrounds. </p>
        <BR><br>
        <p class="text-center">Stay tuned to the Maker Faire Orlando social channels and to our email newsletter for news and updates as the year unfolds.</p>
      </div>
    </div>
  </div>
</section>

<div style="margin-bottom:40px"></div>
---

{% include sponsors-carousel.html %}
