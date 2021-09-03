---
title: Exhibits
layout: full-width
permalink: /makers/
isotope: true
redirect-from:
  - /exhibits/
scrolltop: true
---
<div class="container">
<h1>Maker Exhibits</h1>
<p>Our "Call for Makers" is open until August 31st. <a href="/exhibit-at-maker-faire-orlando/">Learn more about exhibiting!</a> </p>

<p>Want to see all the BattleBots participating in <a href="https://robotruckus.org">Robot Ruckus</a>? Head over to the <a href="https://robotruckus.org">Robot Ruckus website</a> for details!</p>
</div>

<div class="mtm">
  <div class="mtm-search">
    <div class="container">
	   <div class="row">
      <div class="col-md-8">
      	<label class="search-filter-label">Search:</label>
      	<input type="text" class="quicksearch form-control" id="maker-search-input" placeholder="Looking for a specific Exhibit or Maker?">
      </div>

    	<div class="col-md-4">
    		<label class="search-filter-label">Filter by category:</label>
    		<select class="filters-select form-control" id="makers-category-select">
     		<option value="*" selected="">show all</option>

    		<option value=".3d-printing">3D Printing</option><option value=".3d-scanning">3D Scanning</option><option value=".arcade">Arcade</option><option value=".arduino">Arduino</option><option value=".art">Art</option><option value=".automation">Automation</option><option value=".battlebot">BattleBot</option><option value=".cnc">CNC</option><option value=".combat-robots">Combat Robots</option><option value=".comics">Comics</option><option value=".cosplay">Cosplay</option><option value=".craft">Craft</option><option value=".drones">Drones</option><option value=".education">Education</option><option value=".electric-vehicles">Electric Vehicles</option><option value=".electronics">Electronics</option><option value=".engineering">Engineering</option><option value=".fabric-arts">Fabric Arts</option><option value=".fiber-arts">Fiber Arts</option><option value=".first-robotics">FIRST Robotics</option><option value=".food">Food</option><option value=".gaming">Gaming</option><option value=".glass">Glass</option><option value=".hackathon">Hackathon</option><option value=".hackerspace">Hackerspace</option><option value=".handmade">Handmade</option><option value=".workshop">Hands-On Workshop</option><option value=".illustration">Illustration</option><option value=".indie-gaming">Indie Gaming</option><option value=".internet-of-things">Internet of Things</option><option value=".invention">Invention</option><option value=".jewelry">Jewelry</option><option value=".kits">Kits</option><option value=".laser-cutting-engraving">Laser Cutting &amp; Engraving</option><option value=".lego">LEGO</option><option value=".maker-community">Maker Community</option><option value=".makerspace">Makerspace</option><option value=".manufacturing">Manufacturing</option><option value=".metalworking">Metalworking</option><option value=".midi">MIDI</option><option value=".music">Music</option><option value=".photography">Photography</option><option value=".power-racing">Power Racing</option><option value=".props">Props</option><option value=".puppets">Puppets</option><option value=".raspberry-pi">Raspberry Pi</option><option value=".robotics">Robotics</option><option value=".science-fair">Science Fair</option><option value=".screenprinting">Screen Printing</option><option value=".sewing">Sewing</option><option value=".software">Software</option><option value=".solar">Solar</option><option value=".space">Space</option><option value=".special-effects">Special Effects</option><option value=".steampunk">SteamPunk</option><option value=".sustainability">Sustainability</option><option value=".talk">Talk</option><option value=".tools">Tools</option><option value=".upcycling">Upcycling</option><option value=".vehicles">Vehicles</option><option value=".virtual-reality">Virtual Reality</option><option value=".woodworking">Woodworking</option><option value=".writing-publishing">Writing and Publishing</option>								</select>
    	</div><!-- #col -->
	   </div><!-- #row -->
   </div><!-- #container -->
 </div><!-- #mtm-search -->
</div>

<div class="exhibits-container" id="exhibits">
  {% for exhibit in site.exhibits %}

      <div class="item{% for category in exhibit.categories -%}
                        {% if category.name %}
                          {{- category.slug | prepend: " "-}}
                        {% endif %}
                        {%- endfor -%}">

        {%comment%}<div class="excerpt-container">{{exhibit.description}}</div>{%endcomment%}
        <div class="img-container"><a href="{{exhibit.url}}">
          <img src="{{exhibit.image-primary.medium}}" style="width:300px; height:auto"></a>
        </div>
        <div class="title-container"><a href="{{exhibit.url}}">{{exhibit.title}}</a></div>
      </div>


{% comment %}
        <div id="{{ exhibit.slug }}">
          <img src="{{ exhibit.image-primary.small }}">
        <a href="{{ exhibit.url }}">{{ exhibit.name }}</a>
        </div>
{% endcomment %}

{% endfor %}
</div>
