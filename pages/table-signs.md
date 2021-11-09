---
title: Maker Faire Orlando Exhibit Table Signs
permalink: /table-signs/
redirect: /tablesigns/
layout: table-signs
sitemap: false
---

{% for exhibit in site.exhibits limit: page.limit %}

<div style="page-break-after: always">
<img style="margin-bottom:20px;" src="/assets/images/site-branding/2021/mfo_table_sign_header_2021_v1_1000.jpg" alt="Maker Faire Orlando">
  <div style="margin-bottom:20px; font-family:lato; font-weight:bold; font-size:50px">{{exhibit.title}}</div>
  <table>
    <tr>
      <td>
        <div style="height: 280px">
          <img style="float: left; max-width: 400px; max-height: 280px; margin-bottom:20px;" src='{{exhibit.image-primary.large}}'/></div>
      </td>
      <td valign="top" style="padding-left:30px; padding-right:20px; font-family:lato; font-size:25px">
        <div style="height:280px; overflow:hidden;">{{exhibit.description}}</div>
      </td>
    </tr>

  </table>

  <div style="margin-bottom:20px; font-family:lato; font-weight:bold; font-size:40px">About the Maker: {{maker.name}}</div>
   <table>
    <tr>
      <td>
        <div style="height: 280px">
<img style="float: left; max-width: 280px; max-height: 300px; margin-bottom:20px;" src='{{exhibit.maker.image-primary}}'/></div>
      </td>
      <td valign="top" style="padding-left:30px; padding-right:20px; font-family:lato; font-size:20px">
        <div style="height:280px; overflow:hidden;">{{exhibit.maker.description}}</div>
      </td>
    </tr>

  </table>



  <table>
    <tr>
      <td style="text-align:center; width:400px; font-family:lato; font-size:20px;">
        View this exhibit on<br>makerfaireorlando.com<br><br>
        <img src='https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://www.makerfaireorlando.com{{exhibit.permalink}}'/>
      </td>
      <td style="text-align:center;width:400px; font-family:lato; font-size:20px;">
        Maker Faire Orlando<br> Android App<br><br>
        <img width="150px" src='/assets/images/site-branding/android_qr_code_150px.png'/>
      </td>
      <td style="text-align:center;width:400px; font-family:lato; font-size:20px;">
        Maker Faire Orlando<br> iOS App<br><br>
        <img width="150px" src='/assets/images/site-branding/ios_qr_code_150px.png'/>
      </td>
    </tr>
  </table>
  <div style="padding:20px; text-align:right; margin-bottom:20px; font-family:lato; font-weight:bold; font-size:12px">{{exhibit.exhibit-zone}} {{exhibit.space-number}} - ID:{{exhibit.exhibit-id}}</div>

</div>

{% endfor %}
