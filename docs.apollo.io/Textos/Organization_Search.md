---
title: Organization Search
url: https://docs.apollo.io/reference/organization-search
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
post

https://api.apollo.io/api/v1/mixed_companies/search

Use the Organization Search endpoint to find companies in the Apollo database. Several filters are available to help narrow your search.

Calling this endpoint does consume credits as part of your Apollo pricing plan.

To protect Apollo's performance for all users, this endpoint has a display limit of 50,000 records (100 records per page, up to 500 pages). Add more filters to narrow your search results as much as possible. This limitation does not restrict your access to Apollo's database; you just need to access the data in batches.