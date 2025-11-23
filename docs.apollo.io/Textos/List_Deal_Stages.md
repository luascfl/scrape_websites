---
title: List Deal Stages
url: https://docs.apollo.io/reference/list-deal-stages
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
get

https://api.apollo.io/api/v1/opportunity_stages

Use the List Deal Stages endpoint to retrieve information about every deal stage that is available in your team's Apollo account.

The `id`

value for each deal stage can be used to set the stage when creating a deal or updating a deal via the Apollo API.

This endpoint also requires a master API key. If you attempt to call the endpoint without a master key, you will receive a `403`

response. Refer to Create API Keys to learn how to create a master API key.