---
title: Bulk Organization Enrichment
url: https://docs.apollo.io/reference/bulk-organization-enrichment
hostname: apollo.io
description: Apollo.io provides API documentation for customers, partners, and developers. Documentation includes a Get Started guide, Apollo Marketplace information, endpoint documentation, tutorials, and API testing capabilities.
sitename: Apollo API Documentation
date: 2025-01-17
---
post

https://api.apollo.io/api/v1/organizations/bulk_enrich

Use the Bulk Organization Enrichment endpoint to enrich data for up to 10 companies with a single API call. To enrich data for only 1 company, use the Organization Enrichment endpoint instead.

Enriched data potentially includes industry information, revenue, employee counts, funding round details, and corporate phone numbers and locations.

This endpoint's rate limit is throttled to 50% of the Organization Enrichment endpoint's per-minute rate limit, and is 100% of the hourly and daily rate limits for the same individual endpoint.