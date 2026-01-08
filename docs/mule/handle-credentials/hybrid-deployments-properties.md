# Hybrid deployments properties

Yes, that's correct—for **hybrid deployments** (on-premises Mule servers registered with Anypoint Runtime Manager), when you set or override properties (including credentials) in the Runtime Manager **Settings > Properties** tab, the **values remain visible** in the UI, even after saving, applying changes, restarting the app, or redeploying.

### Why This Happens
- This is a deliberate design difference from CloudHub (1.0 or 2.0):
    - In **CloudHub**, you can "protect" or hide sensitive properties (values become masked/irretrievable after deployment, stored in an encrypted vault).
    - In **hybrid/on-premises**, there is **no equivalent "protect/hide" feature** in Runtime Manager. Property values are displayed plainly in the Settings page for operational transparency, as the infrastructure is customer-controlled.
- Transmission is secure: Values are encrypted over HTTPS when sent from Runtime Manager to the on-premises Mule runtime.
- Storage in Runtime Manager's database is encrypted, but the UI shows the clear-text value (only visible to authorized Anypoint Platform users).

This is explicitly documented in MuleSoft's guides (e.g., "Safely Hide Application Properties" and hybrid properties management sections).

### Recommendations for Handling Credentials in Hybrid Deployments
To avoid exposing sensitive values in Runtime Manager:
1. **Preferred: Use Secure Configuration Properties module** (bundled in the app):
    - Encrypt credentials in a separate `.yaml` or `.properties` file using the Secure Properties Tool.
    - Reference with `secure::` prefix in your config.
    - Provide the decryption key securely at runtime (e.g., as a system property in `$MULE_HOME/conf/wrapper.conf` or via environment variable—protect access to the server).
    - These encrypted values **do not appear** in Runtime Manager Properties tab at all.

2. **Alternative approaches**:
    - Use external secret managers (e.g., HashiCorp Vault, AWS Secrets Manager) via custom connectors or runtime extensions.
    - Set sensitive values as JVM system properties or environment variables directly on the server (bypassing Runtime Manager entirely).
    - For Runtime Fabric (RTF, a containerized on-premises/hybrid option), you **can** protect properties (values hidden via Runtime Manager or `rtfctl`).

If you're dealing with highly sensitive credentials, avoid Runtime Manager overrides for hybrid and lean toward bundled encrypted properties or external vaults. Refer to MuleSoft docs on [Secure Configuration Properties](https://docs.mulesoft.com/mule-runtime/latest/secure-configuration-properties) and [Hybrid Properties Management](https://docs.mulesoft.com/runtime-manager/hybrid-manage-props) for full details.
