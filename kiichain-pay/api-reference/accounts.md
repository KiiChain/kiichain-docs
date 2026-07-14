# Accounts

{% openapi-operation spec="kiichain-pay-swagger" path="/accounts/v1/accounts/{accountId}/countries" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/accounts/v1/accounts/{accountId}/user" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/accounts/v1/countries" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/accounts/v1/levels" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/accounts/v1/limits" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/accounts/v1/limits/overrides" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/accounts/v1/rails/schemas" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/accounts/v1/users/{userId}/accounts" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/accounts/v1/users/{userId}/accounts/{accountId}" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/accounts/v1/users/{userId}/accounts/{accountId}/limits" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/accounts/v1/users/{userId}/accounts/{accountId}/withdrawal_destinations" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/accounts/v1/users/{userId}/accounts/{accountId}/withdrawal_destinations" method="post" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/accounts/v1/users/{userId}/accounts/{accountId}/withdrawal_destinations/{destinationId}" method="delete" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/accounts/v1/users/{userId}/accounts/{accountId}/withdrawal_destinations/{destinationId}" method="patch" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/accounts/v1/users/{userId}/accounts/{accountId}/withdrawal_destinations/{destinationId}:confirm" method="post" %}
{% endopenapi-operation %}
