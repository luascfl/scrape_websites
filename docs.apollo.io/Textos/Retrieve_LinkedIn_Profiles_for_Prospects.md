---
title: Retrieve LinkedIn Profiles for Prospects
url: https://docs.apollo.io/docs/retrieve-linkedin-profiles-for-prospects
hostname: apollo.io
description: Learn how to identify LinkedIn profiles for prospects via Apollo's APIs.
sitename: Apollo API Documentation
date: 2021-05-27
---
# Retrieve LinkedIn Profiles for Prospects

## Watch the Video

## Overview

Modern sales methodologies emphasize the importance of multi-touch, multi-channel campaigns across phone, email, and social media. In B2B sales, LinkedIn is a powerful platform to use to connect and build meaningful relationships with prospects.

By using Apollo's People API, you can quickly access LinkedIn profile links for your prospects while you search for them using demographics filters.


CreditsUsing this endpoint does consume your account’s credits. Refer to Apollo’s API pricing page for more details.


The following section describes how to search for and filter prospects using Apollo's People API.

## Before You Start

Check out Apollo's API reference docs first to view the query parameters available with the People API. In the following section, Apollo walks through a specific scenario. However, you can address your own cases by combining these examples with the reference information.

## Example Use Case: Identify LinkedIn Profiles for Sales Leadership at a Specific Company

To show how the People API can be used to uncover LinkedIn profiles, let’s walk through a scenario: finding people that are currently in sales leadership roles at Apollo.io.

To find people matching these demographics:

- Call the People API Search endpoint:

`POST https://api.apollo.io/api/v1/mixed_people/api_search`


- Add the following query parameters:

Parameter | Value for this Example | Notes |
|---|---|---|
| ["sales", "revenue"] | Your search filters need to be added as an array of strings. Use the |
| ["c-suite", "head", "director", "manager"] | Your search filters need to be added as an array of strings. Use the |
| "apollo.io" | Your search filters need to be added as an array of strings, such as Use the |

- Add the following keys and values to the header of your request:
**Content-Type**:`application/json`

**Cache-Control**:`no-cache`

**X-Api-Key**: Enter your Apollo API key.


### cURL Request

The following code sample shows the example as a cURL request:

```
curl --request POST \
--url 'https://api.apollo.io/api/v1/mixed_people/api_search?person_titles[]=sales&person_titles[]=revenue&include_similar_titles=true&person_seniorities[]=c_suite&person_seniorities[]=head&person_seniorities[]=director&person_seniorities[]=manager&q_organization_domains_list[]=apollo.io' \
--header 'Cache-Control: no-cache' \
--header 'Content-Type: application/json' \
--header 'accept: application/json' \
--header 'x-api-key: YOUR_API_KEY'
```


### Postman Request

The following image shows how to format the request in Postman. If you prefer to pass the parameters via the body of the request, use the `raw`

option, not `form-data`

.

### Response Details

A successful request returns a `200`

response status and JSON data similar to the following response:

```
...
"contacts": [
{
"contact_roles": [],
"id": "60b00154e86fd7000191773c",
"first_name": "Henry",
"last_name": "Mizel",
"name": "Henry Mizel",
"linkedin_url": "http://www.linkedin.com/in/henrymizel",
"title": "SVP of Revenue Operations & Partnerships",
"contact_stage_id": "6095a710bd01d100a506d4ae",
"owner_id": "60affe7d6e270a00f5db6fe4",
"creator_id": "60affe7d6e270a00f5db6fe4",
"person_id": "66fa05751c88bb0001b13f1c",
"email_needs_tickling": null,
"organization_name": "Apollo.io",
"source": "search",
"original_source": "search",
"organization_id": "5e66b6381e05b4008c8331b8",
"headline": "SVP Revenue Operations at Apollo.io",
"photo_url": "https://media-exp1.licdn.com/dms/image/C5603AQHSGwLwfdkOoQ/profile-displayphoto-shrink_400_400/0/1619618854362?e=1627516800&v=beta&t=TC5BQo7yMoTyIqX14IgqpEAlWPw9F0V69EOXuevtbdo",
"present_raw_address": "New York, New York, United States",
"linkedin_uid": "117048921",
"extrapolated_email_confidence": null,
"salesforce_id": null,
"salesforce_lead_id": null,
"salesforce_contact_id": null,
"salesforce_account_id": null,
"crm_owner_id": null,
"created_at": "2021-05-27T20:30:12.325Z",
"emailer_campaign_ids": [
"624b4d82f6a95501165cafcc"
],
"direct_dial_status": null,
"direct_dial_enrichment_failed_at": null,
"email_status": "verified",
"email_source": null,
"account_id": "63f53afe4ceeca00016bdd7b",
"last_activity_date": null,
"hubspot_vid": null,
"hubspot_company_id": null,
"crm_id": null,
"sanitized_phone": "+5551234567",
"merged_crm_ids": null,
"updated_at": "2024-12-19T14:23:00.920Z",
"queued_for_crm_push": false,
"suggested_from_rule_engine_config_id": null,
"email_unsubscribed": null,
"person_deleted": null,
"call_opted_out": null,
"label_ids": [
"6711547abf291a0510704450",
"671170bcf3555f03ee4a8bce"
],
"has_pending_email_arcgate_request": false,
"has_email_arcgate_request": false,
"existence_level": "full",
"email": "[email protected]",
"email_from_customer": true,
"typed_custom_fields": {
"671152f6bf291a01b0706011": [
"671152f6bf291a01b070600f"
],
"6711743816d0c001b195b4fd": "1) Apollo Closes Second Vintage Large Cap Direct Lending Fund with $4.8 Billion of Assets\nDate: 2024-10-15\nApollo announced the closure of Apollo Origination Partnership Fund II (AOP II) with approximately $4.8 billion of investable assets. This brings the total assets raised for the Apollo Large Cap Direct Lending business to $13.3 billion in just over 12 months. The fund aims to invest in senior corporate debt of large-cap issuers in the U.S. and Western Europe.\n\n2) Apollo Sees $75 Trillion Gap in Private Credit's 'Next Frontier'\nDate: 2024-10-16\nApollo Global Management is ramping up its high-grade capital-solutions business, aiming to address a $75 trillion gap in private credit. The company is increasing resources for this unit as part of its strategy to double its size by 2029.\n\n3) Wolfspeed Announces $750M in Proposed Funding from U.S. CHIPS Act and Additional $750M From Investment Group Led By Apollo\nDate: 2024-10-15\nWolfspeed announced proposed funding of $750 million from the U.S. CHIPS Act and an additional $750 million from an investment group led by Apollo. This funding will support Wolfspeed’s expansion of silicon carbide manufacturing in the U.S.\n\n4) Apollo to Announce Third Quarter 2024 Financial Results\nDate: 2024-10-08\nApollo will release its financial results for the third quarter of 2024 on October 29, 2024. The management team will discuss the financial outcomes through a public webcast.\n\n5) SemiCab Wins Contract with Apollo Tyres for Transportation Services in India\nDate: 2024-10-17\nSemiCab, a subsidiary of Algorhythm Holdings, has entered into a master service agreement with Apollo Tyres, India's largest tire manufacturer, to provide AI-powered transportation services. The contract aims to reduce service costs and improve delivery accuracy for Apollo Tyres in India.",
"67509ed5dec9e101b0e88b6b": "Hi Henry,\n\nAs a Revenue Operations leader, I imagine tracking and engaging potential buyers across complex sales cycles can be challenging. Apollo's comprehensive platform connects you with 270M+ verified contacts, simplifying prospect identification and outreach.\n\nOur tools help sales teams build precise target lists, personalize communication, and automate sequences - all within one intuitive system. We're trusted by teams at Autodesk, Rippling, and other high-growth companies.\n\nWould you be open to a 15-minute conversation about optimizing your sales engagement strategy? I'd love to share how Apollo can support your revenue goals.\n\nDavid",
"67509ed6dec9e101b0e88b6f": "Your sales engagement strategy (Revenue ops)"
},
"custom_field_errors": {},
"crm_record_url": null,
"email_status_unavailable_reason": null,
"email_true_status": "Verified",
"updated_email_true_status": true,
"source_display_name": "Requested from Apollo",
"twitter_url": null,
"contact_campaign_statuses": [
{
"id": "63c196a2c30b570001419ff7",
"emailer_campaign_id": "624b4d82f6a95501165cafcc",
"send_email_from_user_id": "60affe7d6e270a00f5db6fe4",
"inactive_reason": "Sequence archived",
"status": "finished",
"added_at": "2023-01-13T17:36:34.911+00:00",
"added_by_user_id": "60affe7d6e270a00f5db6fe4",
"finished_at": "2023-11-29T17:28:56.781+00:00",
"paused_at": null,
"auto_unpause_at": null,
"send_email_from_email_address": "[email protected]",
"send_email_from_email_account_id": "60c0ebc48c520800a4dc4742",
"manually_set_unpause": null,
"failure_reason": null,
"current_step_id": null,
"in_response_to_emailer_message_id": null,
"cc_emails": null,
"bcc_emails": null,
"to_emails": null
}
],
"state": "New York",
"city": "New York",
"country": "United States",
"account": {
"id": "63f53afe4ceeca00016bdd7b",
"name": "Apollo",
"website_url": "http://www.apollo.io",
"linkedin_url": "http://www.linkedin.com/company/apolloio",
"twitter_url": "https://twitter.com/meetapollo/",
"facebook_url": "https://www.facebook.com/MeetApollo",
"primary_phone": {
"number": "+1 202-374-1312",
"source": "Account",
"sanitized_number": "+12023741312"
},
"alexa_ranking": 3514,
"phone": "+1(202) 374-1312",
"linkedin_uid": "18511550",
"founded_year": 2015,
"logo_url": "https://zenprospect-production.s3.amazonaws.com/uploads/pictures/67976ca8d115490001e45ffc/picture",
"primary_domain": "apollo.io",
"sanitized_phone": "+12023741312",
"domain": "apollo.io",
"team_id": "6095a710bd01d100a506d4ac",
"organization_id": "5e66b6381e05b4008c8331b8",
"source": "salesforce",
"original_source": "salesforce",
"owner_id": "60affe7d6e270a00f5db6fe4",
"created_at": "2023-02-21T21:43:26.354Z",
"phone_status": "no_status",
"account_playbook_statuses": [],
"existence_level": "full",
"label_ids": [],
"typed_custom_fields": {},
"custom_field_errors": {},
"modality": "account",
"source_display_name": "Imported from Salesforce",
"crm_record_url": null
},
"contact_emails": [],
"organization": {
"id": "5e66b6381e05b4008c8331b8",
"name": "Apollo.io",
"website_url": "http://www.apollo.io",
"linkedin_url": "http://www.linkedin.com/company/apolloio",
"twitter_url": "https://twitter.com/meetapollo/",
"facebook_url": "https://www.facebook.com/MeetApollo",
"primary_phone": {
"number": "+1 202-374-1312",
"source": "Account",
"sanitized_number": "+12023741312"
},
"alexa_ranking": 3514,
"phone": "+1 202-374-1312",
"linkedin_uid": "18511550",
"founded_year": 2015,
"logo_url": "https://zenprospect-production.s3.amazonaws.com/uploads/pictures/67976ca8d115490001e45ffc/picture",
"primary_domain": "apollo.io",
"sanitized_phone": "+12023741312"
},
"employment_history": [
{
"_id": "6799f5e8fb7a0b0001a0886a",
"created_at": null,
"current": true,
"degree": null,
"description": null,
"emails": null,
"end_date": null,
"grade_level": null,
"kind": null,
"major": null,
"organization_id": "5e66b6381e05b4008c8331b8",
"organization_name": "Apollo.io",
"raw_address": null,
"start_date": "2023-07-01",
"title": "SVP Revenue Operations",
"updated_at": null,
"id": "6799f5e8fb7a0b0001a0886a",
"key": "6799f5e8fb7a0b0001a0886a"
},
...
],
],
"people": [
{
"id": "6583076babc9680001db23d4",
"first_name": "Jeremy",
"last_name": "Boyd",
"name": "Jeremy Boyd",
"linkedin_url": "http://www.linkedin.com/in/jeremy-s-boyd",
"title": "Senior Product Led Sales and Outbound Operations Manager",
"email_status": "verified",
"photo_url": "https://media.licdn.com/dms/image/v2/D5603AQG5IzLl3wRhFQ/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1731599535482?e=2147483647&v=beta&t=jBSKPIqNJpxzCC2bWWGqSjvobYen3qmmrOy8K3DP4Uk",
"twitter_url": null,
"github_url": null,
"facebook_url": null,
"extrapolated_email_confidence": null,
"headline": "Better Every Day",
"email": "[email protected]",
"organization_id": "5e66b6381e05b4008c8331b8",
"employment_history": [
{
"_id": "6799baab4bb54d00019251c5",
"created_at": null,
"current": true,
"degree": null,
"description": null,
"emails": null,
"end_date": null,
"grade_level": null,
"kind": null,
"major": null,
"organization_id": "5e66b6381e05b4008c8331b8",
"organization_name": "Apollo.io",
"raw_address": null,
"start_date": "2024-11-01",
"title": "Senior Product Led Sales and Outbound Operations Manager",
"updated_at": null,
"id": "6799baab4bb54d00019251c5",
"key": "6799baab4bb54d00019251c5"
},
],
...
],
"state": "Ohio",
"city": "Cincinnati",
"country": "United States",
"organization": {
"id": "5e66b6381e05b4008c8331b8",
"name": "Apollo.io",
"website_url": "http://www.apollo.io",
"linkedin_url": "http://www.linkedin.com/company/apolloio",
"twitter_url": "https://twitter.com/meetapollo/",
"facebook_url": "https://www.facebook.com/MeetApollo",
"primary_phone": {
"number": "+1 555-123-4567",
"source": "Account",
"sanitized_number": "+15551234567"
}
...
},
]
```


The following table details some key elements of the API response:

Element | Description |
|---|---|
and
| Contacts are people in the Apollo database whose data is already enriched. Each of these arrays is formatted differently, and contacts include more information, but the |
| This field provides a link to the prospect's LinkedIn profile, if it is available in the Apollo database. |

Updated 4 days ago

Now that you know how to find LinkedIn profiles for your prospects, hop in to People API Search endpoint reference docs and start testing immediately!