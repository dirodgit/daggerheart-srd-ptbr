# {{ name|upper }}

{{ description }}

*{{ note }}*

## CARACTERÍSTICA DE COMUNIDADE
{% for feat in feats %}
***{{ feat.name }}:*** {{ feat.text }}
{% endfor %}
