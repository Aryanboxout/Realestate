---
layout: default
title: About
---

## Project

{{ site.description }}

 ## Team

 The following people are members of our research team:
 {% for team_member in site.team_members %}
 - {{ team_member.name }}, role: {{ team_member.role }}
 {% endfor %}
