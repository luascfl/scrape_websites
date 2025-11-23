---
title: Add Your Integration to the Apollo.io Marketplace
url: https://docs.apollo.io/docs/add-your-integration-to-apollos-marketplace
hostname: apollo.io
description: If you're building an integration for Apollo.io using APIs, make sure that people know it's available and can use it by having it listed on the Apollo Marketplace.
sitename: Apollo API Documentation
date: 2025-09-17
---
# Feature Your Integration

## Overview

Apollo’s Marketplace is a directory that features approved integrations to more than a million Apollo users.

## Marketplace Requirements

Apollo is excited to add your integration to the Marketplace. Before you submit an application to join, please ensure that your integration meets the following requirements.

Your organization must:

- Have an integration with Apollo’s REST API.
- Use the OAuth 2.0 flow as the sole authorization method.
- Have at least 3 unique Apollo teams connected to your integration. An Apollo team is defined as an organization with its own unique Apollo account.
- Meet Apollo’s brand guidelines, including the use of approved logos.
- Abide by Apollo’s Terms of Service. This agreement is required when you set up API access.
- Abide by Apollo’s security requirements . This agreement is required when submitting the application to join the Marketplace.

When you’re confident that your integration meets all the requirements, submit your application to join the Apollo Marketplace.

### Security Requirements

Apollo’s objective is to cultivate trust and ensure security within the Apollo Marketplace for our users. All integrations featured on the Apollo Marketplace are required to abide by the Terms of Service. As a Marketplace Partner, it is your duty to consistently assess and enhance your applications to guarantee compliance and fulfill the security criteria specified below.*

❗*A violation to these can result in delisting of the application from the marketplace.


**Authentication & Authorization**

An application must authenticate and authorize every request on all endpoints exposed. *Anonymous access to application endpoints and resources can be allowed in scenarios where it is needed.*

**Data Protection**

Any Apollo End User Data:

- stored by an application
**outside of the Apollo product or users' browser**must ensure full disk encryption at-rest. - accessed by an application or a service should be authenticated and authorized appropriately.

An application must use TLS version 1.2 (or higher) to encrypt all of its traffic, and enable HSTS with a minimum age of one year.

An application must securely store and manage secrets, which include API keys, and encryption keys. They cannot be stored in places that are easily accessible. Examples of places include:

- Source code and code repository tools, such as Bitbucket and Github
- URL strings
- Referrer headers
- Application logs

Ensure that the keys are dynamic and rotated on a regular basis: sensitive keys should not be static.

**Application Security**

The onboarding document should present clear instructions for customers to generate a unique API key with the unique app name, with access strictly limited to the functionality that the application needs in order to run.

It’s recommended to rotate API keys every 90 days.

An application must maintain and securely configure domains where the application is hosted.

When applicable, an application must enable security headers and cookie security attributes.

An application must validate and sanitize all untrusted data and treat all user input as unsafe to mitigate injection-related vulnerabilities. Untrusted data is any input that can be manipulated to contain a web attack payload.

Encode all output. Ensure data is treated as data and not as code, especially in different browser contexts.

An application must not use versions of third-party libraries and dependencies with known critical or high vulnerabilities. When vulnerabilities in these libraries and dependencies are discovered, application developers must remediate them as quickly as possible.

Periodically scan for vulnerabilities in third-party dependencies using tools such as OWASP Dependency-Check, Dependabot, etc.

Perform regular threat modeling of your apps to identify attack vulnerabilities that could have a high impact.

Perform static analysis of your app to identify patterns of insecure code.

Perform dynamic analysis using tools. such as Burp Suite or OWASP Zed Attack Proxy (ZAP). to identify any OWASP top 10 vulnerabilities

**Privacy**

An application must not insecurely store or share credentials belonging to Apollo user accounts such as user passwords or user API tokens.

The application must only access the data/functionality which is required for it to be functional.

**Vulnerability Management**

The recommended vulnerability’s timeframe for resolution by severity type is outlined below:

*Severity / CVSS Score / Timeframe for resolution*

- Critical / CVSS v3 >= 9.0 / Must be fixed within
**4 weeks**of being reported or triaged. - High / CVSS v3 >= 7.0 / Must be fixed within
**6 weeks**of being reported or triaged. - Medium / CVSS v3 >= 4.0 / Must be fixed within
**8 weeks**of being reported or triaged. - Low / CVSS v3 < 4.0 / Must be fixed within
**25 weeks**of being reported or triaged.

**Incident Response**

You must promptly (and no later than 24 hours) notify Apollo of all security incidents via dedicated Apollo contact (if applicable) and by dropping an email at [email protected] describing incident type, status, what information was involved, tasks identified/completed to mitigate the incident and point of contact of your security/IT team.

Maintain proper logs for events and activities that can help investigate security incidents. Monitor and alert on anomalies in logs. Examples include low privileged users performing a high privileged action and malicious traffic detected from a bad IP.

Establish an incident response plan, so you are better prepared to respond to security breaches and incidents.

Establish a disaster recovery and business continuity plan to minimize or eliminate interruptions to the functioning of your apps during an incident.

## Submit Your Marketplace Application

Submit this application to add your integration to the Apollo Marketplace. Apollo’s Partner team will review your application and contact you within 5 business days with the next steps to take in the process.

If approved, Apollo will invite you to set up your Marketplace listing and manage its content. Apollo must review and approve your completed listing before it is published.

## Earn $ for promoting your integration to new Apollo users

If you're promoting and recommending your integration to users who are not yet Apollo customers, we'd love to reward you for these referrals to Apollo!

Join our Referral Program and earn commission for the first 12 months of every paying customer you refer to Apollo:

- Earn 15% commission on monthly paid plans
- Earn 20% commission on annual paid plans

## Have Questions?

If you’d like to learn more about Apollo’s Marketplace, Referral Program or have questions that are not answered here, please reach out to the Apollo Partnerships team via the web form at the bottom of the Apollo Partners page.

Updated 2 months ago