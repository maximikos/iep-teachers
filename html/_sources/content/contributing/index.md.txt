---
html_theme.sidebar_secondary.remove:
sd_hide_title: true
html_sidebars.remove:
---

# Contributing

> This page is adapted from the excellent [Brightway documentation](https://docs.brightway.dev). We simply couldn't formulate it better.

This section contains contains information on how to contribute to IEP. This might be reporting specific errors or bugs, or contributing directly to the source code. It also specifies the style in which documentation and code should be written.


```{note}
We are happy to find you on this page! Let's improve the documentation together. Please follow the steps below to start your contribution.
```


### 🥉 Request new Content

```{admonition} Prerequisites
:class: important
1. A [GitHub account](https://github.com/signup)
```

Create a documentation request in the _Discussion_ section of the [iep-novice](https://github.com/maximikos/iep-novice) or [iep-advanced](https://github.com/maximikos/iep-advanced) repositories, detailing your request and all relevant information. A member of the Brightway developer community will evaluate your request. Please note that all developments are undertaken on a voluntary basis, so it may take some time for your issue to be resolved.

### 🥈 Write new Content

```{admonition} Prerequisites
:class: important
1. A [GitHub account](https://github.com/signup)
2. Basic knowledge of [Markdown](https://www.markdownguide.org/basic-syntax/)
```

Write your content in [Markdown](https://en.wikipedia.org/wiki/Markdown), using the formatting options described in the [Formatting Guide](./formatting.md) and save it to a single file. Now create a new issue in the _Issues_ section of the [iep-novice](https://github.com/maximikos/iep-novice/issues/new) and [iep-advanced](https://github.com/maximikos/iep-advanced/issues/new) repositories, describing your request and attaching the Markdown file. A member of the IEP community will integrate your contribution into the documentation. Please note that all developments are undertaken on a voluntary basis, so it may take some time for your issue to be resolved.

### 🥇 Write and add new Content

```{admonition} Prerequisites
:class: important
1. A [GitHub account](https://github.com/signup)
2. Basic knowledge of [the GitHub contribution workflow (fork, branch, PR)](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests)
3. A [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks) of the [`iep-novice`](https://github.com/maximikos/iep-novice) or [`iep-advanced`](https://github.com/maximikos/iep-advanced) repositories
4. Basic knowledge of [Markdown](https://www.markdownguide.org/basic-syntax/)
```

In order to fix add new content to the documentation by yourself, follow the ususal GitHub contribution workflow:

1. Use the `✏️ Edit on GitHub` button on the top right of the page to open the corresponding file in the GitHub repository. This shows you which file you need to edit.
2. Edit the file in your fork of the repository. Finally, create a pull request.
3. As soon as a member of the Brightway developer community has merged your pull request, the changes will be visible on the IEP website.


```{toctree}
---
hidden: true
maxdepth: 1
---
self
formatting
```