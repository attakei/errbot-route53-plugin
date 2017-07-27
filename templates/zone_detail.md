**Record sets**


```
{% for record in records -%}
- {{ record.Name }} : {{ record.Type }}
    {% for res in record.ResourceRecords -%}
    - {{ res.Value }}
    {% endfor %}
{%- endfor %}
```
