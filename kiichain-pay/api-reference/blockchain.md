# Blockchain

{% openapi-operation spec="kiichain-pay-swagger" path="/blockchain/v1/chains" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/blockchain/v1/chains/tokens" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/blockchain/v1/chains/tokens/all" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/blockchain/v1/chains/{chainId}" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/blockchain/v1/chains/{chainId}/tokens/{tokenSymbol}" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/blockchain/v1/tokens" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/blockchain/v1/tokens/{symbol}" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/blockchain/v1/transactions/execute" method="post" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/blockchain/v1/wallets/internal" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/blockchain/v1/wallets/internal/send" method="post" %}
{% endopenapi-operation %}
