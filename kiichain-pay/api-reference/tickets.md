# Tickets

{% openapi-operation spec="kiichain-pay-swagger" path="/tickets/v1/accounts/{accountId}" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/tickets/v1/offramp" method="post" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/tickets/v1/swap" method="post" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/tickets/v1/{ticketId}" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/tickets/v1/{ticketId}/pending_user_actions" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/tickets/v1/{ticketId}/user_txs" method="get" %}
{% endopenapi-operation %}
