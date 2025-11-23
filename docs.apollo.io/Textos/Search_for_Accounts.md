---
title: Search for Accounts
url: https://docs.apollo.io/reference/search-for-accounts
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
post

https://api.apollo.io/api/v1/accounts/search

Use the Search for Accounts endpoint to search for the account that have been added to your team's Apollo account.

In Apollo terminology, an account is a company that your team has explicitly added to your database.

This endpoint only returns accounts in the search results. To search for companies in the Apollo database, call the Organization Search endpoint.

To protect Apollo's performance for all users, this endpoint has a display limit of 50,000 records (100 records per page, up to 500 pages). Add more filters to narrow your search results as much as possible. This limitation does not restrict your access to Apollo's database; you just need to access the data in batches.