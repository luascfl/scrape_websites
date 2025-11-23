---
title: List Account Stages
url: https://docs.apollo.io/reference/list-account-stages
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
get

https://api.apollo.io/api/v1/account_stages

Use the List Accounts Stages endpoint to retrieve the IDs for the available account stages in your team's Apollo account. This endpoint does not require parameters.

Account stage IDs can be used to update individual accounts and update the account stages for multiple accounts via the Apollo API.

This endpoint requires a master API key. If you attempt to call the endpoint without a master key, you will receive a `403`

response. Refer to Create API Keys to learn how to create a master API key.