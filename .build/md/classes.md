# {{ name|upper }}

{{ description }}

> **• DOMÍNIOS:** [{{ domain_1 }}](../domains/{{ url_encode(domain_1) }}.md) & [{{ domain_2 }}](../domains/{{ url_encode(domain_2) }}.md)  
> **• EVASÃO INICIAL:** {{ evasion }}  
> **• PONTOS DE VIDA INICIAIS:** {{ hp }}  
> **• ITENS DE CLASSE:** {{ items }}

## CARACTERÍSTICA DE ESPERANÇA DO {{ name|upper }}

***{{ hope_feat_name }}:*** {{ hope_feat_text }}

## CARACTERÍSTICA{% if class_feats|length > 1 %}S{% endif %} DE CLASSE
{% for feat in class_feats %}
***{{ feat.name }}:*** {{ feat.text }}
{% endfor %}
## SUBCLASSES DE {{ name|upper }}

Escolha a subclasse **[{{ subclass_1 }}](../subclasses/{{ url_encode(subclass_1) }}.md)** ou **[{{ subclass_2 }}](../subclasses/{{ url_encode(subclass_2) }}.md)**.

## PERGUNTAS DE HISTÓRICO

*Responda a qualquer uma das seguintes perguntas de histórico. Você também pode criar suas próprias perguntas.*
{% for background in backgrounds %}
- {{ background.question }}{% endfor %}

## CONEXÕES

*Faça uma das seguintes perguntas a outro jogador para o personagem dele responder, ou crie suas próprias perguntas.*
{% for connection in connections %}
- {{ connection.question }}{% endfor %}

{{ extras }}
