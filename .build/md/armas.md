# {{ name|upper }}

**Atributo:** {{ trait }}; **Alcance:** {{ range }}; **Dano:** {{ damage }}; **Carga:** {{ burden }}

**Característica:** {% if feat_name %}***{{ feat_name }}:*** {{ feat_text }}{% else %}—{% endif %}

*Arma {{ "Principal" if primary_or_secondary == "Primary" else "Secundária" }} - Tier {{ tier }}*
