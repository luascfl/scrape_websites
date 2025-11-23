---
title: Add Contacts to a Sequence
url: https://docs.apollo.io/reference/add-contacts-to-sequence
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
post

https://api.apollo.io/api/v1/emailer_campaigns//add_contact_ids

Use the Add Contacts to a Sequence endpoint to add contacts to the existing sequences in your team's Apollo account.

In Apollo terminology, a contact is a person that your team has explicitly added to your database. Only contacts can be added to sequences. To enrich a person's data, call the People Enrichment endpoint. Then, to add the person as a contact in your database, call the Create a Contact endpoint.

This endpoint requires a master API key. If you attempt to call the endpoint without a master key, you will receive a `403`

response. Refer to Create API Keys to learn how to create a master API key.