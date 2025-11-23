---
title: Get a List of All Lists
url: https://docs.apollo.io/reference/get-a-list-of-all-lists
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
get

https://api.apollo.io/api/v1/labels

Use the Get a List of All Lists endpoint to retrieve information about every list that has been created in your Apollo account. This endpoint can be used to check the available lists before you use the Create a Contact endpoint.

This endpoint does not require any parameters.

This endpoint requires a master API key. If you attempt to call the endpoint without a master key, you will receive a `403`

response. Refer to Create API Keys to learn how to create a master API key.