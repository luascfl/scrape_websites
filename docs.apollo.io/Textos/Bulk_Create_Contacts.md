---
title: Bulk Create Contacts
url: https://docs.apollo.io/reference/bulk-create-contacts
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
post

https://api.apollo.io/api/v1/contacts/bulk_create

Use the Bulk Create Contacts endpoint to create up to 100 contacts in a single API request. This endpoint supports intelligent deduplication and returns separated arrays for newly created and existing contacts.

Important: This endpoint creates new contacts but does NOT update existing ones (except for placeholder contacts from email imports). Existing contacts that match the criteria will be returned in the existing_contacts array without modification.

To update existing contacts, use the Bulk Update Contacts endpoint.