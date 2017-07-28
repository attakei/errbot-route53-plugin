**Created new zone!!**

Hostname is `{{ zone_info.Name }}`
ID is `{{ zone_info.Id }}`

{% for ns in zone_info.NameServers -%}
- {{ ns }}
{% endfor -%}
