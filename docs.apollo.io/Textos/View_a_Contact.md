---
title: View a Contact
url: https://docs.apollo.io/reference/view-a-contact
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
get

https://api.apollo.io/api/v1/contacts/

Use the View a Contact endpoint to retrieve details for an existing contact in your team's Apollo database. In Apollo terminology, a contact is a person that your team has explicitly added to your database. A contact will have their data enriched in some way, such as accessing an email address or a phone number.

This endpoint requires a master API key. If you attempt to call the endpoint without a master key, you will receive a `403`

response. Refer to Create API Keys to learn how to create a master API key.