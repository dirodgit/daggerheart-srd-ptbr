# {{ name|upper }}

{{ description }}
{% if spellcast_trait %}
## CARACTERÍSTICA DE CONJURAÇÃO

{{ spellcast_trait }}
{% endif %}
## CARACTERÍSTICA DE FUNDAÇÃO{% if foundations|length > 1 %}S{% endif %}
{% for feat in foundations %}
***{{ feat.name }}:*** {{ feat.text }}
{% endfor %}
## CARACTERÍSTICA DE ESPECIALIZAÇÃO{% if specializations|length > 1 %}S{% endif %}
{% for feat in specializations %}
***{{ feat.name }}:*** {{ feat.text }}
{% endfor %}
## CARACTERÍSTICA DE MESTRIA{% if masteries|length > 1 %}S{% endif %}
{% for feat in masteries %}
***{{ feat.name }}:*** {{ feat.text }}
{% endfor %}
{{ extras }}
