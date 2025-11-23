---
title: Bulk Update Accounts
url: https://docs.apollo.io/reference/bulk-update-accounts
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
post

https://api.apollo.io/api/v1/accounts/bulk_update

Use the Bulk Update Accounts endpoint to simultaneously update multiple accounts in your team's Apollo account.

This endpoint allows you to update common fields across multiple accounts efficiently, such as account stages, owners, names, and custom fields.

You can update up to 1000 accounts per request. **Important:** Asynchronous processing (async parameter) is only supported when using account_ids to apply the same updates to all accounts. If you attempt to use async with account_attributes (individual updates per account), the request will fail with a 422 error.