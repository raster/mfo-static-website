---
title: MFO Static Website test
permalink: /
layout: default


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

<section class="what-is-maker-faire">
<div class="container">
<div class="row text-center">
<div class="title-w-border-y">
<h2>What is Maker Faire?</h2>
</div>
</div>
<div class="row">
<div class="col-md-10 col-md-offset-1">
<p class="text-center">Maker Faire is a gathering of fascinating, curious people who enjoy learning and who love sharing what they can do. From engineers to artists to scientists to crafters, Maker Faire is a venue for these “makers” to show hobbies, experiments, projects.</p>
<p class="text-center">We call it the Greatest Show (&amp; Tell) on Earth – a family-friendly showcase of invention, creativity, and resourcefulness.</p>
<p class="text-center">Glimpse the future and get inspired!</p>
</div>
</div>
</div>
<div class="wimf-border"><div class="wimf-triangle"></div></div><img src="assets/images/site-branding/makey.png" alt="Maker Faire information Makey icon">
</section>


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
