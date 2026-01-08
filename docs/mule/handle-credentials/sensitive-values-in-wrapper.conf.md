# Sensitive Values in wrapper.conf

### Best Practices for Securing Sensitive Values in wrapper.conf

If you're adding JVM system properties (e.g., `-Ddb.password=secret`) via `wrapper.java.additional.n` lines:

1. **Encrypt individual sensitive values** (recommended MuleSoft approach):
    - Use Mule's built-in decryption for specific properties like Anypoint Platform credentials (e.g., client_id/secret
      for Mule Gateway/API Autodiscovery).
    - Format: `wrapper.java.additional.n=-Danypoint.platform.client_secret=![encryptedValue]`
    - Provide the decryption key separately (e.g., via `-Danypoint.platform.encryption_key=myKey` or environment
      variable).
    - This uses AES/CBC and decrypts at runtime (see MuleSoft docs on Gateway Startup Encryption).

2. **Primary recommendation: Avoid plain-text secrets altogether**
    - Use **Mule Secure Configuration Properties module** for app-level secrets:
        - Encrypt values in your `.yaml`/`.properties` files with the Secure Properties Tool.
        - Pass the decryption key via OS **environment variable** (not wrapper.conf) — e.g.,
          `export MULE_SECRET_KEY=myMasterKey` before starting Mule.
        - This keeps the key out of files entirely and only in memory/process env.
    - For highly sensitive setups, integrate external vaults (e.g., HashiCorp Vault, Azure Key Vault) via custom
      properties providers.

3. **File-level protections** (basic but essential):
    - Restrict OS permissions: `chmod 600 $MULE_HOME/conf/wrapper.conf` (owner-read/write only).
    - Ensure only trusted admins have server access — anyone with shell can read the file or view process args (
      `ps -ef`).

In summary, rely on **encrypted property values + env vars for keys** + **file permissions** rather than trying to
encrypt the file. This aligns with MuleSoft best practices for on-premises security. See docs
on [Secure Configuration Properties](https://docs.mulesoft.com/mule-runtime/latest/secure-configuration-properties)
and [Configuring Properties](https://docs.mulesoft.com/mule-runtime/latest/configuring-properties) for details.
