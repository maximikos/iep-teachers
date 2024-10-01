---
html_theme.sidebar_secondary.remove:
sd_hide_title: true
#html_sidebars.remove: true
---

<!-- CSS overrides on the homepage only -->
<style>
.bd-main .bd-content .bd-article-container {
  max-width: 70rem; /* Make homepage a little wider instead of 60em */
}
/* Extra top/bottom padding to the sections */
article.bd-article section {
  padding: 2rem 0 8rem;
}
/* Override all h1 headers except for the hidden ones */
h1:not(.sd-d-none) {
  font-weight: bold;
  font-size: 48px;
  text-align: center;
  margin-bottom: 4rem;
}
/* Override all h3 headers that are not in hero */
h3:not(#hero h3) {
  font-weight: bold;
  text-align: center;
}
</style>

# IEP: Industrial Ecology Platform for sustainability literacy

<div id="hero-writer">
    <div class="wrapper">
        <span class="first-text">What is</span>
        <ul class="sec-texts">
            <li><span><a href="content/theory/methods/lca.html">life cycle assessment?</a></span></li>
            <li><span><a href="..">Norway's carbon footprint?</a></span></li>
            <li><span><a href="content/theory/concepts/sem.html">socio-economic metabolism?</a></span></li>
            <li><span><a href="..">the impact of recycling?</a></span></li>
        </ul>
    </div>
</div>

<div id="hero">

<div id="hero-left">  <!-- Start Hero Left -->
  <h2 style="font-size: 60px; font-weight: bold; margin: 2rem auto 0;">Hello there &#128075</h2>
  <h3 style="font-weight: bold; margin-top: 0;">Curious about sustainability?</h3>
  <p>Look no further! We open the box of all-things sustainability to everyone, including hopefully YOU. So, if you have ever wondered about any of the above or similar questions, you're at the right place! &#129412</p>

<div class="homepage-button-container">
  <div class="homepage-button-container-row">
      <a href="./get_started/index.html" class="homepage-button primary-button">Get Started</a>
      <a href="./about/index.html" class="homepage-button secondary-button">About us</a>
  </div>
  <div class="homepage-button-container-row">
      <a href="mailto:students@is4ie.org" class="homepage-button-link">Drop us a message &#x1F48C;</a>
  </div>
</div>
</div>  <!-- End Hero Left -->

<div id="hero-right">  <!-- Start Hero Right -->

  <div style="text-align: center;">
    <iframe src="https://giphy.com/embed/igsVfO6Sro82xBQP8I" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
  </div>

<!-- grid ended above, do not put anything on the right of markdown closings -->

</div>  <!-- End Hero Right -->
</div>  <!-- End Hero -->


```{toctree}
---
hidden:
maxdepth: 1
---
content/theory/index
content/insights/index
content/resources/index

content/contributing/index
content/contact/contact
content/about/index
```
