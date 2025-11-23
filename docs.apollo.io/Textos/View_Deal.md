---
title: View Deal
url: https://docs.apollo.io/reference/view-deal
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
get

https://api.apollo.io/api/v1/opportunities/

Use the View Deal endpoint to retrieve complete details about a deal within your team's Apollo account.

Deal information can include the ID of the deal owner, the monetary value of the deal, the deal stage, and general details about the account.

This endpoint also requires a master API key. If you attempt to call the endpoint without a master key, you will receive a `403`

response. Refer to Create API Keys to learn how to create a master API key.