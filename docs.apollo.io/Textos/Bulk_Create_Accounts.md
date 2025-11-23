---
title: Bulk Create Accounts
url: https://docs.apollo.io/reference/bulk-create-accounts
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
post

https://api.apollo.io/api/v1/accounts/bulk_create

Use the Bulk Create Accounts endpoint to create up to 100 accounts in a single API request. This endpoint supports intelligent deduplication and returns separate arrays for newly created and existing accounts.

Important: This endpoint creates new accounts but does NOT update existing ones. Existing accounts that match the criteria will be returned in the existing_accounts array without modification.

To update existing accounts, use the Bulk Update Accounts endpoint.