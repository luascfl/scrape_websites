---
title: Convert Enriched People to Contacts
url: https://docs.apollo.io/docs/convert-enriched-people-to-contacts
hostname: apollo.io
description: Overview When you use the Apollo API to enrich your own people data and pull mobile phone numbers, you've likely already consumed email, export, or mobile credits as part of your Apollo pricing plan. If you call the API to enrich data for the same people in the future, you potentially consume more c…
sitename: Apollo API Documentation
date: 2025-04-04
---
# Convert Enriched People to Contacts

## Overview

When you use the Apollo API to enrich your own people data and pull mobile phone numbers, you've likely already consumed email, export, or mobile credits as part of your Apollo pricing plan. If you call the API to enrich data for the same people in the future, you potentially consume more credits to access the same data you've previously accessed.

To avoid consuming your account's credits unnecessarily, use the Create a Contact endpoint to convert enriched people into contacts. A contact is a person that you have added to your organization's Apollo account, which means their data becomes permanently accessible to your organization.


New ContactsApollo does not run any deduplication during this process. If your record contains the same email address, or name and company, as an existing contact, Apollo will create a new contact instead of updating the existing contact.


The following sections detail how to use the Contacts API to create new contacts in Apollo.

## Before You Start: Check Out Reference Docs

Apollo’s API reference docs show the query parameters available for you to use with the Contacts API. Apollo is going to walk through a specific scenario in this article, but you can address your own cases by combining these examples with the reference information.

## Example: Create a Contact

First, ensure that you can access the person data that you have pulled via the Enrichment API. For this example, Apollo is going to pass the following information to the Contacts API:

- First name
- Last name
- Email address
- Company name
- Company domain
- Direct phone
- Mobile phone

To create a contact via the API for your Apollo account:

- Call the Create a Contact endpoint:

`POST https://api.apollo.io/api/v1/contacts`


- Add the following query parameters:

| Parameter | Value for this Example |
|---|---|
`"first_name"` | `"Mark"` |
`"last_name"` | `"Twain"` |
`"organization_name"` | `"Great American Writers Co."` |
`"email"` | `"[email protected] "` |
`"website_url"` | `"https://www.greatamericanwriters.com"` |
`"direct_phone"` | `"555-123-4567"` |
`"mobile_phone"` | `"555-765-4321"` |

- Add the following keys and values to the header of your request:
**Content-Type**:`application/json`

**Cache-Control**:`no-cache`

**X-Api-Key**: Enter your Apollo API key.


### cURL Request

The following shows the example as a cURL request:

```
curl --request POST \
--url 'https://api.apollo.io/api/v1/contacts?first_name=Mark&last_name=Twain&organization_name=Great%20American%20Writers%20Co.&email=themarktwain%40greatamericanwriters.com&website_url=https%3A%2F%2Fwww.greatamericanwriters.com&direct_phone=555-123-4567&mobile_phone=555-765-4321' \
--header 'Cache-Control: no-cache' \
--header 'Content-Type: application/json' \
--header 'accept: application/json' \
--header 'x-api-key: YOUR_API_KEY'
```


### Postman Request

The following image shows how the request can be formatted in Postman. If you prefer to pass the parameters via the body of the request, use the `raw`

option, not `form-data`

.

### Response Details

A successful request returns a `200`

response status and JSON data similar to the following response:

```
{
"contact": {
"contact_roles": [],
"id": "668463fe9709b70afd54fb5a",
"first_name": "Mark",
"last_name": "Twain",
"name": "Mark Twain",
"linkedin_url": null,
"title": null,
"contact_stage_id": "6095a710bd01d100a506d4ae",
"owner_id": "60affe7d6e270a00f5db6fe4",
"creator_id": "60affe7d6e270a00f5db6fe4",
"person_id": null,
"email_needs_tickling": null,
"organization_name": "Great American Writers Co.",
"source": "api",
"original_source": "api",
"organization_id": null,
"headline": null,
"photo_url": null,
"present_raw_address": null,
"linkedin_uid": null,
...
"phone_numbers": [
{
"raw_number": "555-123-4567",
"sanitized_number": "+15551234567",
"type": "work_direct",
"position": 0,
"status": "no_status",
"dnc_status": null,
"dnc_other_info": null,
"dialer_flags": null
},
{
"raw_number": "555-765-4321",
"sanitized_number": "+15557654321",
"type": "mobile",
"position": 1,
"status": "no_status",
"dnc_status": null,
"dnc_other_info": null,
"dialer_flags": null
}
],
...
}%
```


### Confirm Contact Status

To confirm that a contact has been created for your Apollo account:

- Call the People Enrichment endpoint:

`POST https://api.apollo.io/api/v1/people/match`


- Add the
`email`

query parameter, and provide the email value from the API response. For this example, the email address is`[email protected]`

. - Add the following keys and values to the header of your request:
**Content-Type**:`application/json`

**Cache-Control**:`no-cache`

**X-Api-Key**: Enter your Apollo API key.


The API response provides the details you used when creating the contact, including the email address and phone numbers. This means you don't need to consume credits from your Apollo account to reveal this information again.

Updated 8 months ago