---
title: Retrieve Mobile Phone Numbers for Contacts
url: https://docs.apollo.io/docs/retrieve-mobile-phone-numbers-for-contacts
hostname: apollo.io
description: Overview By default, Apollo does not provide mobile phone numbers for contacts. However, with basic details such as an email address or name, the Enrichment API enables you to retrieve all of a contact's phone numbers, including those highly valued mobile phone numbers. 🚧CreditsUsing the API to pul…
sitename: Apollo API Documentation
date: 2023-08-15
---
# Retrieve Mobile Phone Numbers for Contacts

## Overview

By default, Apollo does not provide mobile phone numbers for contacts. However, with basic details such as an email address or name, the Enrichment API enables you to retrieve all of a contact's phone numbers, including those highly valued mobile phone numbers.


CreditsUsing the API to pull phone numbers consumes your account’s credits. Refer to Apollo’s API pricing page for more details.


The following sections detail how to pull phone numbers for a contact via the API.

## Before You Start: Check Out Reference Docs

Apollo’s API reference docs show the query parameters available for you to use with the Enrichment API. Apollo is going to walk through a specific scenario in this article, but you can address your own cases by combining these examples with the reference information.

## Example: Retrieve Mobile Phone Numbers


1 Person OnlyFor this example, Apollo is going to show how to retrieve phone numbers for a single person.

To pull phone numbers for up to 10 people with a single API call, check out the Bulk People Enrichment endpoint. The same query parameters are available whether you are retrieving numbers for a single person or multiple people.


To pull phone numbers for a contact via the Apollo API:

- Call the People Enrichment endpoint:

`POST https://api.apollo.io/api/v1/people/match`


- Add the following query parameters:

Parameter | Value for this Example | Notes |
|---|---|---|
| For this example, Apollo is providing an email address for a query parameter as it is the easiest way to identify the correct contact. | |
|
| This value must be set to |
|
| Provide the URL where you want Apollo to deliver the data for the contact's phone numbers. The webhook delivery occurs separately, usually several minutes after a successful API request. You still receive the typical API response, but it does not include mobile phone numbers. If you fail to provide a valid URL, you receive the following error response:
|

- Add the following keys and values to the header of your request:
**Content-Type**:`application/json`

**Cache-Control**:`no-cache`

**X-Api-Key**: Enter your Apollo API key.


### cURL Request

The following shows the example as a cURL request:

```
curl --request POST \
--url 'https://api.apollo.io/api/v1/people/match?email=josh.garrison%40apollo.io&reveal_personal_emails=false&reveal_phone_number=true&webhook_url=https%3A%2F%2Fwebhook-test.com%2F5b112b64ff0f4104d003444e843c161a' \
--header 'Cache-Control: no-cache' \
--header 'Content-Type: application/json' \
--header 'accept: application/json' \
--header 'x-api-key: YOUR_API_KEY'
```


### Postman Request

The following image shows how the request can be formatted in Postman. If you prefer to pass the parameters via the body of the request, use the `raw`

option, not `form-data`

.

### Webhook Response Details

A successful request first returns a `200`

response status and the typical JSON data from the People Enrichment endpoint, but the API response only includes a phone number for the person's employer.

The webhook from Apollo is typically triggered several minutes after your successful API request, and the data includes all possible phone numbers for the contact:

```
{
"status": "success",
"total_requested_enrichments": 1,
"unique_enriched_records": 1,
"missing_records": 0,
"credits_consumed": 1,
"people": [
{
"id": "587cf802f65125cad923a266",
"status": "success",
"phone_numbers": [
{
"_id": "64dbe6d172c24f00017b9b71",
"confidence_cd": "high",
"created_at": null,
"direct_dial_source_cd": "contact_trusted",
"dnc_other_info": {
"country": "United States"
},
"dnc_status_cd": "not_found",
"dnc_status_updated_at": "2023-08-15T20:57:53.108+00:00",
"position": 0,
"raw_number": "+1 555-123-4567",
"sanitized_number": "+15551234567",
"status_cd": "valid_number",
"type_cd": "other",
"updated_at": null,
"id": "64dbe6d172c24f00017b9b71",
"key": "64dbe6d172c24f00017b9b71"
},
{
"_id": "64dbe6d172c24f00017b9b72",
"confidence_cd": "high",
"created_at": null,
"direct_dial_source_cd": "contact_trusted",
"dnc_other_info": {
"country": "United States"
},
"dnc_status_cd": "not_found",
"dnc_status_updated_at": "2023-08-15T20:57:53.267+00:00",
"position": 1,
"raw_number": "+1 415-971-3487",
"sanitized_number": "+14159713487",
"status_cd": "valid_number",
"type_cd": "other",
"updated_at": null,
"id": "64dbe6d172c24f00017b9b72",
"key": "64dbe6d172c24f00017b9b72"
}
]
}
]
}
```


The following table details some key elements of the webhook response:

Element | Description |
|---|---|
| The value in this object shows many of your mobile credits were consumed by the request. As this example only retrieved phone numbers for a single person, there was only 1 credit consumed. If you use the Bulk People Enrichment endpoint to request phone numbers for multiple people, you could consume multiple mobile credits. Refer to the API pricing page for more details. |
| This array provides all of the phone numbers Apollo has for the contact. |
| This is the phone number formatted with hyphens and spaces. |
| This is the phone number formatted without hyphens and spaces. |

Updated 10 months ago