# Users

{% openapi-operation spec="kiichain-pay-swagger" path="/users/v1/api/create" method="post" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/users/v1/api/{apiKeyId}" method="patch" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/users/v1/api/{apiKeyId}/delete" method="delete" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/users/v1/api/{apiKeyId}/rotate" method="patch" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/users/v1/api/{apiKeyId}/scopes" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/users/v1/api/{userId}/api-keys" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/users/v1/users/me" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/users/v1/users/me/change_profile" method="patch" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/users/v1/users/{userId}" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/users/v1/users/{userId}/language" method="patch" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/users/v1/users/{userId}/roles" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/users/v1/users/{userId}/settings" method="get" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/users/v1/users/{userId}/settings" method="patch" %}
{% endopenapi-operation %}

{% openapi-operation spec="kiichain-pay-swagger" path="/users/v1/{userId}/mfa/methods" method="get" %}
{% endopenapi-operation %}
