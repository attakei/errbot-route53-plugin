**Record sets**

{% for record in records %}
- {{ record.Name }} : {{ record.Type }} : {{ record.ResourceRecords[0].Value }}
{% endfor %}
