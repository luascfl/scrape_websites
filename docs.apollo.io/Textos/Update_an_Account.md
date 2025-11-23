---
title: Update an Account
url: https://docs.apollo.io/reference/update-an-account
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
patch

https://api.apollo.io/api/v1/accounts/

Use the Update an Account endpoint to update existing accounts in your team's Apollo account.

In Apollo terminology, an account is a company that your team has explicitly added to your database.

To create a new account, use the Create an Account endpoint instead. To update the account stage for multiple account, use the Update Account Stage for Multiple Accounts endpoint.

This endpoint requires a master API key. If you attempt to call the endpoint without a master key, you will receive a `403`

response. Refer to Create API Keys to learn how to create a master API key.