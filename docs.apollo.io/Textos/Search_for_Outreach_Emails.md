---
title: Search for Outreach Emails
url: https://docs.apollo.io/reference/search-for-outreach-emails
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
get

https://api.apollo.io/api/v1/emailer_messages/search

Use the Search for Outreach Emails endpoint to find emails that your team has created and sent as part of Apollo sequences.

To protect Apollo's performance for all users, this endpoint has a display limit of 50,000 records (100 records per page, up to 500 pages). Add more filters to narrow your search results as much as possible. This limitation does not restrict your access to Apollo's database; you just need to access the data in batches.

This endpoint requires a master API key. If you attempt to call the endpoint without a master key, you will receive a `403`

response. Refer to Create API Keys to learn how to create a master API key.