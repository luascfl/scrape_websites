---
title: Check Email Stats
url: https://docs.apollo.io/reference/check-email-stats
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
get

https://api.apollo.io/api/v1/emailer_messages//activities

Use the Check Email Stats endpoint to review the complete details for an email sent as part of an Apollo sequence. This includes the contents of the emails, stats related to the email such as opens and clicks, and details about the contact that received the email.

This endpoint requires a master API key. If you attempt to call the endpoint without a master key, you will receive a `403`

response. Refer to Create API Keys to learn how to create a master API key.