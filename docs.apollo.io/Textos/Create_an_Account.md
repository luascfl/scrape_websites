---
title: Create an Account
url: https://docs.apollo.io/reference/create-an-account
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
post

https://api.apollo.io/api/v1/accounts

Use the Create an Account endpoint to add a new account to your team's Apollo account.

In Apollo terminology, an account is a company that your team has explicitly added to your database.

Apollo does not apply deduplication processes when you create a new account via the API. If your entry has the same name, domain, or other details as an existing account, Apollo will create a new account instead of updating the existing account. To update an existing account, use the Update an Account endpoint instead.

This endpoint requires a master API key. If you attempt to call the endpoint without a master key, you will receive a `403`

response. Refer to Create API Keys to learn how to create a master API key.