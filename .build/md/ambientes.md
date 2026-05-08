# {{ name|upper }}

***Tier {{ tier }} {{ type }}***  
*{{ description }}*  
**Impulsos:** {{ impulses }}

> **Dificuldade:** {{ difficulty }}  
> **Adversários Potenciais:** {{ potential_adversaries }}

## CARACTERÍSTICAS
{% for feat in feats %}
***{{ feat.name }}:*** {{ feat.text }}
{% endfor %}
