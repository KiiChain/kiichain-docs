---
description: >-
  This page explains how to securely connect to our API using an API Key. It
  outlines the required authentication details and how to generate a digital
  signature to ensure safe and verified communicatio
---

# Authenticate with API Key

## Step by step

1. Create your user API Key and add permissions
   1. [#create-api-key](authenticate-with-api-key.md#create-api-key "mention")
2. Create a Signature
   1. [#create-a-signature](authenticate-with-api-key.md#create-a-signature "mention")
3. Authenticate via API
   1. [#authenticate-via-api](authenticate-with-api-key.md#authenticate-via-api "mention")

## Create API KEY

Navigate through the admin UI to your user profile.

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

Click on the API KEYS option.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

Click on 'Create your API KEY'. You will see the following:

Depending on how you plan to use your API KEY, please choose from the available options. If you want to restrict usage by IP address, you can add the allowed IP in the designated field. Remember, you can always modify this later.

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

When you click on 'Create API Key', you will see your API KEY, API SECRET, and NONCE displayed on screen only once. You can download them using the 'Export to JSON' button. It's very important to store them in a safe place, as you will need them later.

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

To save, click the button confirming that you've securely stored your credentials, then close the modal. Your new API KEY will now appear in the list, and you can edit or delete it as needed.

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

## Create a Signature

To generate a signature, you will need the API Secret, Nonce, User ID, and API Key, which are all generated, You can generate a signature by using a tool such as [https://codebeautify.org/hmac-generator](https://codebeautify.org/hmac-generator) The algorithm will be SHA256, the Key will be the API Secret, and the plain text message will be composed of a combination the Nonce, User ID, and API key, in that exact order with no spaces. An example is listed below.

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

## Authenticate via API

Follow the example in the image, add the APIKEY, Signature, UserId, and Nonce to the request headers, and call the `AuthenticateUser` endpoint. This will successfully authenticate you.

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

{% openapi-operation spec="swap-kiiex" path="/AuthenticateUser" method="post" %}
[OpenAPI swap-kiiex](https://4401d86825a13bf607936cc3a9f3897a.r2.cloudflarestorage.com/gitbook-x-prod-openapi/raw/35214ac23d9928896910cf1474dfa48f9fd7d2585cd1675c58f2332c1cf63386.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=dce48141f43c0191a2ad043a6888781c%2F20260725%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20260725T013652Z&X-Amz-Expires=172800&X-Amz-Signature=c6dd076c13115393ae6b70c1cfb312c5223aef4e9cc459184e1b3feaed338020&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
{% endopenapi-operation %}

In the response, you will receive a session token. Use it in all subsequent requests by including it in the headers as the value of `aptoken`.
