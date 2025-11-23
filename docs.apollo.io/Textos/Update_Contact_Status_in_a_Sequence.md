---
title: Update Contact Status in a Sequence
url: https://docs.apollo.io/reference/update-contact-status-sequence
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
post

https://api.apollo.io/api/v1/emailer_campaigns/remove_or_stop_contact_ids

Use the Update Contact Status in a Sequence endpoint to either mark contacts as having `finished`

a sequence, or to remove them from a sequence entirely.

This endpoint requires a master API key. If you attempt to call the endpoint without a master key, you will receive a `403`

response. Refer to Create API Keys to learn how to create a master API key.