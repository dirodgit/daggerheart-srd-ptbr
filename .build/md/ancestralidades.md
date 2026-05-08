# {{ name|upper }}

{{ description }}

## CARACTERÍSTICAS DE ANCESTRALIDADE
{% for feat in feats %}
***{{ feat.name }}:*** {{ feat.text }}
{% endfor %}
