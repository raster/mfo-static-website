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
{% include cta-panel-widget.html cta_text=cta_event_text cta_url=site.cta_footer_url %}


{% include what-is-maker-faire.html %}
{% include makey-border.html %}

{% include call-for-makers-widget.html %}
{% include sponsors-carousel.html %}
