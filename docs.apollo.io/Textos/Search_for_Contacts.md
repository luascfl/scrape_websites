---
title: Search for Contacts
url: https://docs.apollo.io/reference/search-for-contacts
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
Use the Search for Contacts endpoint to search for the contacts that have been added to your team's Apollo account.

In Apollo terminology, a contact is a person that your team has explicitly added to your database. A contact will have their data enriched in some way, such as accessing an email address or a phone number.

This endpoint only returns contacts in the search results. To search for people in the Apollo database, call the People API Search endpoint.

To protect Apollo's performance for all users, this endpoint has a display limit of 50,000 records (100 records per page, up to 500 pages). Add more filters to narrow your search results as much as possible. This limitation does not restrict your access to Apollo's database; you just need to access the data in batches.

post

https://api.apollo.io/api/v1/contacts/search