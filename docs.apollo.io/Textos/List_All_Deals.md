---
title: List All Deals
url: https://docs.apollo.io/reference/list-all-deals
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
get

https://api.apollo.io/api/v1/opportunities/search

Use the List All Deals endpoint to retrieve every deal that has been created for your team's Apollo account.

This endpoint also requires a master API key. If you attempt to call the endpoint without a master key, you will receive a `403`

response. Refer to Create API Keys to learn how to create a master API key.