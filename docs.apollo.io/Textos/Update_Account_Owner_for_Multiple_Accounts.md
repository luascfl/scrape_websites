---
title: Update Account Owner for Multiple Accounts
url: https://docs.apollo.io/reference/update-account-ownership
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
post

https://api.apollo.io/api/v1/accounts/update_owners

Use the Update Account Owner for Multiple Accounts endpoint to assign multiple accounts to a different user in your team's Apollo account.

To update more than the account owner, such as domains or phone numbers, use the Update an Account endpoint instead.

This endpoint requires a master API key. If you attempt to call the endpoint without a master key, you will receive a `403`

response. Refer to Create API Keys to learn how to create a master API key.