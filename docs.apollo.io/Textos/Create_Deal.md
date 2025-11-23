---
title: Create Deal
url: https://docs.apollo.io/reference/create-deal
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
post

https://api.apollo.io/api/v1/opportunities

Use the Create Deal endpoint to create new deals for an Apollo account. Deals enable you to track account activity, including monetary values of a deal, deal owners, and deal stages.

To update existing deals in your Apollo account, use the Update Deal endpoint instead.

This endpoint also requires a master API key. If you attempt to call the endpoint without a master key, you will receive a `403`

response. Refer to Create API Keys to learn how to create a master API key.