# Connected App

### What is a "Connected App" in the MuleSoft / Anypoint Platform world?

In MuleSoft terminology, a **Connected App** is a feature of **Anypoint Platform** (not the Mule runtime itself) that
lets an external application or system securely authenticate and interact with Anypoint Platform APIs and resources
using OAuth 2.0.

It is the MuleSoft equivalent of what you see in Salesforce (“Connected App”), Okta (“OAuth App”), or GitHub (“OAuth
App”).

### Why do you need a Connected App?

You create one whenever you want something outside of Anypoint Platform to call its APIs securely, for example:

| Use case                                                                              | Typical Connected App type                       |
|---------------------------------------------------------------------------------------|--------------------------------------------------|
| CI/CD pipeline (Jenkins, GitHub Actions, Azure DevOps, Bitbucket) deploying Mule apps | Client Credentials flow                          |
| External monitoring tool pulling metrics from CloudHub or RTF                         | Client Credentials flow                          |
| Custom portal or script that manages APIs, environments, VPCs, etc. via Anypoint API  | Client Credentials or Authorization Code         |
| Internal tool that needs user context (who is doing the action)                       | Authorization Code or JWT flow                   |
| Partner or third-party system accessing your APIs through API Manager                 | Client Credentials or External Identity Provider |

### The 4 most common OAuth 2.0 grant types you can choose when creating the Connected App

| Grant Type                | When to use                                                                | Credentials you get back     |
|---------------------------|----------------------------------------------------------------------------|------------------------------|
| **Client Credentials**    | Machine-to-machine (most common for CI/CD and automation)                  | Access token (no refresh)    |
| **Authorization Code**    | When you need a real user’s identity and permissions (browser-based tools) | Access token + refresh token |
| **JWT**                   | When an external Identity Provider (IdP) asserts the identity              | Access token                 |
| **Password** (deprecated) | Direct username/password – avoid if possible                               | Access token + refresh token |

### How to create a Connected App (step-by-step – 2025 UI)

1. Log into Anypoint Platform → **Access Management** (left menu)
2. Go to **Connected Apps** (under the “Authentication” section)
3. Click **Create application**
4. Choose the scope:
    - **Act on behalf of users** (Authorization Code / JWT) → pick specific users or user groups
    - **Act on your own behalf** (Client Credentials) → pick the organization/business groups and the permissions (
      environments) it can access
5. Select the exact permissions (scopes) you need, e.g.:
    - Deploy API Manager Assets
    - View Runtime Manager
    - Deploy to CloudHub
    - Read Design Center, etc.
6. Save → you get:
    - **Client ID**
    - **Client Secret** (one-time view – store it safely)

### Example: Using it with Maven or Anypoint CLI for deployments

```xml
<!-- In your ~/.m2/settings.xml -->
<servers>
    <server>
        <id>anypoint.platform</id>
        <username>my-username</username>
        <password>my-password</password>
    </server>
    <server>
        <id>connected-app</id>
        <username>~~~~client_id~~~~</username>
        <password>~~~~client_secret~~~~</password>
    </server>
</servers>
```

Then in your Mule project pom.xml:

```xml

<plugin>
    <groupId>org.mule.tools.maven</groupId>
    <artifactId>mule-maven-plugin</artifactId>
    <version>4.0.0</version>
    <configuration>
        <cloudHubDeployment>
            <uri>https://anypoint.mulesoft.com</uri>
            <server>connected-app</server>        <!-- uses Client Credentials -->
            <applicationName>my-api-prod</applicationName>
            <environment>Production</environment>
        </cloudHubDeployment>
    </configuration>
</plugin>
```

### The credentials never leave your local machine / CI-CD runner

When you use a **Connected App** (with **Client Credentials** flow) for deployments or automation, **the actual
sensitive credentials never leave your local machine / CI-CD runner**. They are **never uploaded to Anypoint Platform,
never stored in Git, and never appear in logs**.

Here’s precisely what happens and what stays where:

| Item                                                    | Where it lives                                  | Ever uploaded to MuleSoft servers or Git?                      |
|---------------------------------------------------------|-------------------------------------------------|----------------------------------------------------------------|
| Client ID                                               | Your local `~/.m2/settings.xml` or CI secret    | Never                                                          |
| Client Secret                                           | Your local `~/.m2/settings.xml` or CI secret    | Never                                                          |
| Your Anypoint username/password (if you ever used them) | No longer needed at all                         | Never (deprecated method)                                      |
| Access token (Bearer token)                             | Generated at runtime, valid 1 hour (by default) | Only sent in HTTPS headers during the API call, then discarded |
| Refresh token                                           | Not used in Client Credentials flow             | N/A                                                            |

### How the secure flow actually works (2025)

1. Your laptop or Jenkins/GitHub Actions runner reads the **Client ID + Client Secret** from a protected location (
   encrypted `settings.xml`, GitHub secret, Jenkins credential store, Azure Key Vault, etc.).
2. The Mule Maven Plugin (or Anypoint CLI) makes a single HTTPS POST to  
   `https://anypoint.mulesoft.com/accounts/api/v2/oauth2/token`
3. MuleSoft validates the Client ID + Secret and returns a short-lived **access token** (JWT).
4. That token is used in the `Authorization: Bearer …` header for all subsequent calls (deploy, start, stop, etc.).
5. After ~60 minutes the token expires and a new one is fetched automatically. The secret itself is never sent again in
   that session.

### Result

- No human username/password anywhere
- No Client Secret in the pom.xml
- No Client Secret in the Git repository
- No Client Secret in CloudHub or Runtime Manager logs
- Nothing for an attacker to steal from the MuleSoft side even if they breach a worker node

This is exactly why MuleSoft and all major clients (including TotalEnergies) now **mandate** Connected Apps instead of
the old username/password method for any production or shared environments.

**the real credentials never leave your secure build environment**. That’s the whole
point and the current security standard.

### Summary – Connected App in one sentence

A Connected App is the secure, OAuth 2.0–based way for any external tool or script to authenticate to Anypoint Platform
and perform actions (deploy, monitor, manage APIs, etc.) with exactly the permissions you grant it — and it has almost
completely replaced the old username/password approach in modern MuleSoft projects.

#### Official MuleSoft Documentation

These provide the definitive explanations, including setup, grant types, and security features like temporary access
tokens that prevent credential exposure.

| Source Title                                   | Description                                                                                                                                  | Link                                                                                                                                       |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Secure API Integration with Connected Apps     | Overview of how Connected Apps enable secure OAuth 2.0 integration without sharing sensitive credentials, including auditing and revocation. | [docs.mulesoft.com/access-management/connected-apps-overview](https://docs.mulesoft.com/access-management/connected-apps-overview)         |
| Connected Apps for Developers                  | Details on implementing Connected Apps for programmatic access, including supported OpenID Connect capabilities and scope management.        | [docs.mulesoft.com/access-management/connected-apps-developers](https://docs.mulesoft.com/access-management/connected-apps-developers)     |
| Creating Connected Apps                        | Step-by-step guide to registration, client ID/secret handling, and ensuring no credential expiration risks.                                  | [docs.mulesoft.com/access-management/creating-connected-apps-dev](https://docs.mulesoft.com/access-management/creating-connected-apps-dev) |
| Connected Apps for Organization Administrators | Admin controls for allowlisting, user authorization policies, and business group scoping.                                                    | [docs.mulesoft.com/access-management/connected-apps-org-admin](https://docs.mulesoft.com/access-management/connected-apps-org-admin)       |

#### Security Best Practices References

These emphasize why credentials aren't uploaded (e.g., via short-lived tokens and encrypted local storage) and align
with MuleSoft's standards.

| Source Title                                           | Description                                                                                                                      | Link                                                                                                                       |
|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Anypoint Platform Security                             | Comprehensive guide on managing access for Connected Apps, including API policies and monitoring to prevent unauthorized access. | [docs.mulesoft.com/general/security](https://docs.mulesoft.com/general/security)                                           |
| MuleSoft Security: Tutorial, Best Practices & Examples | Practical advice on OAuth 2.0 in Connected Apps, TLS, and tools like Mule Credentials Vault for zero credential exposure.        | [www.curietech.ai/mulesoft-integration/mulesoft-security](https://www.curietech.ai/mulesoft-integration/mulesoft-security) |
| API Security                                           | Anypoint Security                                                                                                                | Overview of enforcing policies at the gateway level, including best practices for Connected Apps to mitigate breaches.     | [www.mulesoft.com/platform/api-security](https://www.mulesoft.com/platform/api-security) |
| Anypoint Security Overview                             | Layered security for Runtime Fabric, focusing on policy enforcement and threat mitigation without credential sharing.            | [docs.mulesoft.com/anypoint-security/](https://docs.mulesoft.com/anypoint-security/)                                       |
