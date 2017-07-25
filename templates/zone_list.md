**List of zones**

{% for zone in zones %}
- {{ zone.Id }}: {{ zone.Name }}
{% endfor %}
