# Conclusion: Best Practices for Secrets Management in MuleSoft Deployments

Throughout our discussion on configuring properties in MuleSoft—an overview of manual vs. runtime interfaces, deployment
properties in Runtime Manager, and security considerations across deployment types—we've highlighted the challenges and
options for handling sensitive credentials like passwords, API keys, and tokens.

Key takeaways:

- **CloudHub (1.0 and 2.0)** offers strong built-in protection: Properties can be marked as "protected," masking values
  irretrievably in the UI and storing them encrypted in MuleSoft's vault.
- **Hybrid/on-premises standalone deployments** lack this hiding feature in Runtime Manager (values remain visible for
  operational transparency in customer-controlled infrastructure), so alternatives like Mule's Secure Configuration
  Properties module (with decryption keys via environment variables), JVM system properties, or restricted file
  permissions are essential—but they still require careful server-level safeguards.
- Bundled encrypted properties or system/env vars help, but managing keys securely and avoiding exposure remains a
  manual effort.

For robust, enterprise-grade secrets management—especially in **hybrid or multi-environment setups**—we should strongly
consider integrating an external **secrets manager** such as **AWS Secrets Manager** (or equivalents like HashiCorp
Vault, Azure Key Vault, or Google Secret Manager).

#### Why AWS Secrets Manager?

- MuleSoft provides an official **Amazon Secrets Manager Properties Provider** connector (available in Anypoint
  Exchange), allowing Mule apps to dynamically retrieve secrets at runtime/startup using placeholders like
  `${aws-secrets::secretName.key}`.
- Secrets are fetched securely (supports IAM roles, default credential chains, or assume-role for least-privilege
  access), cached for performance, and never hardcoded or bundled.
- Benefits include automatic rotation, fine-grained access controls, auditing, and environment segregation—addressing
  limitations in hybrid deployments where Runtime Manager properties are visible.
- Works seamlessly across CloudHub, Runtime Fabric, and hybrid (with proper IAM configuration on on-premises servers).

This approach aligns with MuleSoft best practices for production security, reduces risk of credential leakage,
simplifies compliance, and scales across environments without redeployment. If your infrastructure involves AWS (common
for many organizations), start by adding the connector to your projects and migrating sensitive properties. For non-AWS
environments, similar providers exist for other clouds.

Refer to MuleSoft docs on
the [Amazon Secrets Manager Properties Provider](https://docs.mulesoft.com/amazon-secrets-manager-properties-provider-connector/latest/)
for implementation details. This elevates your MuleSoft deployments to a more secure, maintainable standard.
