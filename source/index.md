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
        <span class="first-text">Check out</span>
        <ul class="sec-texts">
            <li><span><a href="content/overview/materials/index.html">new teaching materials</a></span></li>
            <li><span><a href="content/overview/teachers/index.html">who's teaching what and where</a></span></li>
            <li><span><a href="content/overview/programmes/index.html">various study programmes</a></span></li>
            <li><span><a href="content/overview/conferences/index.html">upcoming conferences</a></span></li>
        </ul>
    </div>
</div>


```{toctree}
---
hidden:
maxdepth: 1
---
content/overview/index
content/contributing/index
content/contact/contact
content/about/index
```
