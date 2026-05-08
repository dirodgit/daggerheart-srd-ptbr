# {{ name|upper }}

***Tier {{ tier }} {{ type }}***  
*{{ description }}*  
**Motivações & Táticas:** {{ motives_and_tactics }}

> **Dificuldade:** {{ difficulty }} | **Limiares:** {{ thresholds }} | **PV:** {{ hp }} | **Estresse:** {{ stress }}  
> **ATQ:** {{ atk }} | **{{ attack }}:** {{ range }} | {{ damage }}  {% if experience %}
> **Experiência:** {{ experience }}{% endif %}

## CARACTERÍSTICAS
{% for feat in feats %}
***{{ feat.name }}:*** {{ feat.text }}
{% endfor %}
