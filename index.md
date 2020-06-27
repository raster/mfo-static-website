---
title: MFO Static Website test
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


<section class="cta-panel">
<div class="container">
<div class="row text-center">
<div class="col-xs-12">
<h3><a href="/attend">{{ site.event_date_descr }} – {{ site.event_location_descr }} <i class="fa fa-chevron-right"></i></a></h3>
</div>
</div>
</div>
</section>

{% include what-is-maker-faire.html %}

{% include makey-border.html %}

{% include call-for-makers-widget.html %}
{% include sponsors-carousel.html %}

<section class="cta-panel" style="margin-top:40px"><div class="container">
          <div class="row text-center">
            <div class="col-xs-12">
              <h3><a href="{{site.cta_footer_url}}">{{site.cta_footer_text}} <i class="fa fa-chevron-right" aria-hidden="true"></i></a></h3>
            </div>
          </div>
        </div>
      </section>
