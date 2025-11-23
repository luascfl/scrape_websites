---
title: Create Call Records
url: https://docs.apollo.io/reference/create-call-records
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
post

https://api.apollo.io/api/v1/phone_calls

Use the Create Call Records endpoint to log calls in Apollo that were made using outside systems such as Orum or Nooks. This endpoint can only be used create call records, not to dial prospects.

This endpoint requires a master API key. If you attempt to call the endpoint without a master key, you will receive a `403`

response. Refer to Create API Keys to learn how to create a master API key.