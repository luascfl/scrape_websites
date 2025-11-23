---
title: Create a Contact
url: https://docs.apollo.io/reference/create-a-contact
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
post

https://api.apollo.io/api/v1/contacts

Use the Create a Contact endpoint to add a new contact to your team's Apollo account.

In Apollo terminology, a contact is a person that your team has explicitly added to your database. A contact will have their data enriched in some way, such as accessing an email address or a phone number.

By default, Apollo does not apply deduplication processes when you create a new contact via the API. If your entry has the same name, email address, or other details as an existing contact, Apollo will create a new contact instead of updating the existing contact. To enable deduplication and prevent duplicate contacts, set the `run_dedupe`

parameter to `true`

.

To update an existing contact, use the Update a Contact endpoint instead.