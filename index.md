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

  - image: /assets/images/slider/jedi.jpg  
    caption: Use the Force!
    url: /cosplay/

  - image: /assets/images/slider/neon-cowboy-hats.jpg
    caption: Make Cool Stuff!
    url: /make-cool-stuff/

  - image: /assets/images/slider/button-making-girl.jpg  
    caption: Make-a-Button!
    url: /make-a-button/
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
        <div class="col-md-10 col-md-offset-1">
        <p class="text-center">2020 has been a year of unprecedented challenges that have affected all facets of life including events and gatherings.
        The Maker Faire Orlando team continues to monitor local and state guidelines while planning for an event in late 2020. We've shifted the event into December in order to have even better outdoor temperatures, and we are exploring new ways to use the outdoor spaces at the Central Florida Fairgrounds. </p>
        <p class="text-center">Stay tuned to the Maker Faire Orlando social channels and to our email newsletter for news and updates as the year unfolds.</p>
      </div>
    </div>
  </div>
</section>


{% include sponsors-carousel.html %}
