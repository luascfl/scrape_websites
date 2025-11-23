---
title: View an Account
url: https://docs.apollo.io/reference/view-an-account
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
get

https://api.apollo.io/api/v1/accounts/

Use the View an Account endpoint to retrieve details for an existing account in your team's Apollo database. In Apollo terminology, an account is a company that your team has explicitly added to your database.

This endpoint requires a master API key. If you attempt to call the endpoint without a master key, you will receive a `403`

response. Refer to Create API keys to learn how to create a master API key.