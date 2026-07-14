# Market

{% openapi-operation spec="kiichain-pay-swagger" path="/market/v1/dex/quote" method="post" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/market/v1/fiat-assets" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/market/v1/fiat-assets/{code}" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/market/v1/instruments" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/market/v1/instruments/{id}" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/market/v1/instruments/{id}/limits" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/market/v1/instruments/{id}/quote" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/market/v1/products" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/market/v1/products-providers" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/market/v1/products-providers/{id}" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/market/v1/products-providers/{id}/limits" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/market/v1/products-providers/{id}/onramp" method="post" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/market/v1/products-providers/{id}/quote" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/market/v1/products/{productId}" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/market/v1/providers" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/market/v1/providers/{providerId}" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/market/v1/providers/{providerId}/kyc/{accountId}" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/market/v1/providers/{providerId}/kyc/{accountId}/start" method="post" %}
{% endopenapi-operation %}
