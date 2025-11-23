---
title: People Enrichment
url: https://docs.apollo.io/reference/people-enrichment
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
Use the People Enrichment endpoint to enrich data for 1 person. To enrich data for up to 10 people with a single API call, use the Bulk People Enrichment endpoint instead.

Apollo relies on the information you pass via the endpoint's parameters to identify the correct person to enrich. If you provide more information about a person, Apollo is more likely to find a match within its database. If you only provide general information, such as a name without a domain or email address, you might receive a 200 response, but the response will indicate that no records have been enriched.

By default, this endpoint does not return personal emails or phone numbers. Use the `reveal_personal_emails`

and `reveal_phone_number`

parameters to retrieve emails and phone numbers.

Using this endpoint will consume credits based on your account's pricing plan. To view a summary of Apollo's pricing, visit the public pricing page ↗ For detailed information regarding API credit usage, see the API enrichment ↗ section on the *About Credits* page (login required).

post

https://api.apollo.io/api/v1/people/match