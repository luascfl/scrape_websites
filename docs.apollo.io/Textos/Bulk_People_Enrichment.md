---
title: Bulk People Enrichment
url: https://docs.apollo.io/reference/bulk-people-enrichment
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
Use the Bulk People Enrichment endpoint to enrich data for up to 10 people with a single API call. To enrich data for only 1 person, use the People Enrichment endpoint instead.

Apollo relies on the information you pass via the endpoint's parameters to identify the correct people to enrich. When you provide more information, Apollo is more likely to find matches within its database. If you only provide general information, such as a name without a domain or email address, you might receive a `200`

response, but the response will indicate that no records have been enriched. The details for each person should be passed as an object with the `details[]`

array.

By default, this endpoint does not return personal emails or phone numbers. Use the `reveal_personal_emails`

and `reveal_phone_number`

parameters to retrieve emails and phone numbers. If you set either of these parameters to `true`

, Apollo will attempt to provide emails or phone numbers for all matches.

Using this endpoint will consume credits based on your account's pricing plan. To view a summary of Apollo's pricing, visit the public pricing page ↗ For detailed information regarding API credit usage, see the API enrichment ↗ section on the *About Credits* page (login required).

This endpoint's rate limit is throttled to 50% of the People Enrichment endpoint's per-minute rate limit, and is 100% of the hourly and daily rate limits for the same individual endpoint.

post

https://api.apollo.io/api/v1/people/bulk_match