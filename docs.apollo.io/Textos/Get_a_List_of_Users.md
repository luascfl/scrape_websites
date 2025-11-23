---
title: Get a List of Users
url: https://docs.apollo.io/reference/get-a-list-of-users
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
get

https://api.apollo.io/api/v1/users/search

Use the Get a List of Users endpoint to retrieve the IDs for all of the users (teammates) in your Apollo account.

These IDs can be used for several other endpoints, including the Create a Deal, Create an Account, and Create a Task endpoints.

This endpoint requires a master API key. If you attempt to call the endpoint without a master key, you will receive a `403`

response. Refer to Create API Keys to learn how to create a master API key.