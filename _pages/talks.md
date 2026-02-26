---
layout: page
title: talks
permalink: /talks/
description: Talks given at conferences and the like.
nav: true
nav_order: 3
display_categories: [2025, 2024, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013]
horizontal: false
---

<!-- pages/talks.md -->
<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized talks -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_talks = site.talks | where: "year", category %}
  {% assign sorted_talks = categorized_talks | sort: "year" | reverse %}
  <!-- Generate cards for each talk -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for talk in sorted_talks %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for talk in sorted_talks %}
      {% include talks.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display talks without categories -->

{% assign sorted_talks = site.talks | sort: "year" %}

  <!-- Generate cards for each talk -->

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for talk in sorted_talks %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for talk in sorted_talks %}
      {% include talks.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>
