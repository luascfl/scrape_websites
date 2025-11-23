---
title: Get a List of Email Accounts
url: https://docs.apollo.io/reference/get-a-list-of-email-accounts
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
get

https://api.apollo.io/api/v1/email_accounts

Use the Get a List of Email Accounts endpoint to retrieve information about the linked email inboxes that your teammates use in your Apollo account.

In particular, this endpoint returns IDs for each of your team's linked email accounts, which can be used with the Add Contacts to a Sequence endpoint.

This endpoint does not require any parameters.

This endpoint requires a master API key. If you attempt to call the endpoint without a master key, you will receive a `403`

response. Refer to Create API Keys to learn how to create a master API key.