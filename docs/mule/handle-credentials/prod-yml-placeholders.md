# Using prod.yml with Placeholders

### Using prod.yml with Placeholders and Anypoint Security Secrets Manager for Credential Injection

Yes, you can absolutely set this up in MuleSoft! This is a secure, best-practice approach to avoid hard-coding
credentials in your YAML files. Placeholders (e.g., `${my.db.password}`) in your `prod.yml` file will be resolved at
runtime by injecting values from **Anypoint Security Secrets Manager** (ASM). ASM acts as a centralized vault for
secrets (passwords, API keys, etc.), and Mule runtime fetches them dynamically without exposing them in your code or
config files.

This works for deployments to CloudHub, Runtime Fabric (RTF), or on-premises Mule servers. ASM is part of Anypoint
Platform's premium security features and supports integration via the **Secrets Manager Connector** or **Properties
Provider**.

#### High-Level Flow

1. **Store Secrets in ASM**: Upload your credentials (e.g., DB password) to ASM via Anypoint Platform UI or API.
2. **Configure Your App**: Add ASM dependencies and config in your Mule app's `global.xml` (or `mule-config.xml`).
3. **Use Placeholders in prod.yml**: Reference secrets with a special prefix (e.g., `asm:my.secret.key`).
4. **Runtime Injection**: When the app starts, Mule resolves placeholders by pulling secrets from ASM over a secure
   connection.
5. **Deployment**: Deploy to prod environment; no secrets are bundled in your artifact.

#### Prerequisites

- Anypoint Platform account with ASM enabled (Premium tier; contact your admin if needed).
- Mule 4.4+ runtime (ASM support is robust here).
- Add the **Secrets Manager Connector** from Exchange:
    - In Anypoint Studio: Search "Secrets Manager Connector" in Palette → Add to your project.
    - In pom.xml: Include
      `<dependency><groupId>com.mulesoft.connectors</groupId><artifactId>mule-secrets-manager-connector</artifactId><version>1.0.0</version></dependency>` (
      check latest version in Exchange).

#### Step-by-Step Setup

1. **Store Secrets in Anypoint Security Secrets Manager**:
    - Log in to Anypoint Platform → **Anypoint Security** (under Access Management) → **Secrets Manager**.
    - Click **Create Secret**:
        - Name: e.g., `prod.db.password`.
        - Value: Your plain-text credential (e.g., `superSecretPass123`).
        - Type: Symmetric (for passwords) or Asymmetric (for certs/keys).
        - Assign to your organization/business group and environment (e.g., Production).
    - Save. The secret is now encrypted and accessible only to authorized apps/services.
    - Note the **Secret ID** (e.g., `asm://prod.db.password`)—this is your reference key.

2. **Configure ASM in Your Mule App (global.xml)**:
    - In `src/main/mule/global.xml` (or your main config), add the Secrets Manager config. This sets up the connection
      to ASM using your Anypoint credentials (via Connected App for security—see our previous discussion).

      ```xml
      <?xml version="1.0" encoding="UTF-8"?>
      <mule xmlns="http://www.mulesoft.org/schema/mule/core"
            xmlns:doc="http://www.mulesoft.org/schema/mule/documentation"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="
                http://www.mulesoft.org/schema/mule/core http://www.mulesoft.org/schema/mule/core/current/mule.xsd
                http://www.mulesoft.org/schema/mule/secrets-manager http://www.mulesoft.org/schema/mule/secrets-manager/current/mule-secrets-manager.xsd">
      
          <!-- Global Properties Config -->
          <configuration-properties file="prod.yml" />
      
          <!-- Secrets Manager Config -->
          <secrets-manager:config name="ASM_Config"
                                  doc:name="Secrets Manager Config"
                                  clientId="${asm.client.id}"  <!-- From Connected App -->
                                  clientSecret="${asm.client.secret}"  <!-- Encrypted in settings.xml -->
                                  environment="Production">  <!-- Your env -->
              <secrets-manager:basic-connection username="${anypoint.username}" password="${anypoint.password}" />
          </secrets-manager:config>
      
      </mule>
      ```
        - **Notes**:
            - Use placeholders for `clientId`, `clientSecret`, etc., and store them securely (e.g., in encrypted
              `settings.xml` or another secret).
            - The `<basic-connection>` uses your Anypoint Platform creds; prefer OAuth via Connected App for production.
            - Reference this config in your flows if needed (e.g.,
              `<secrets-manager:get id="#[vars.secretId]" config-ref="ASM_Config" target="payload" />`).

3. **Create/Update prod.yml with Placeholders**:
    - Place `prod.yml` in `src/main/resources`.
    - Use placeholders for injection. For ASM, prefix with `asm:` (or configure a custom prefix).

      ```yaml
      # prod.yml - Production Environment Config
      db:
        host: prod-db.totalenergies.com
        port: 5432
        name: myapp_db
        username: app_user
        password: ${asm:prod.db.password}  # Placeholder: Injected from ASM at runtime
      
      api:
        endpoint: https://api.totalenergies.com/v1
        key: ${asm:prod.api.key}  # Another secret from ASM
      
      logging:
        level: INFO
        appender: file
      ```
        - **How Injection Works**: At app startup, Mule's Properties Resolver scans for `${asm:...}` patterns and calls
          ASM to fetch/decrypt the value. The resolved `prod.yml` becomes available via `p('db.password')` in your
          flows.
        - For non-ASM properties, use standard `${key}`—they resolve from the file or deployment properties.

4. **Reference Properties in Your Flows**:
    - In a Mule flow (e.g., Database connector config):
      ```xml
      <db:config name="DB_Config">
          <db:postgresql-connection host="${db.host}" port="${db.port}" database="${db.name}"
                                    user="${db.username}" password="${db.password}" />
      </db:config>
      ```
    - This pulls from the injected `prod.yml`.

5. **Deploy and Test**:
    - **In Anypoint Studio**: Run locally (ensure ASM creds are set as env vars or in `mule-app.properties`).
    - **To CloudHub/RTF**: Deploy via Runtime Manager or Maven.
        - In deployment settings, add any non-secret props (e.g., `asm.client.id`).
        - Verify: Check app logs for resolution (no plain-text creds should appear).
    - **Security Check**: Secrets are fetched per-request or at startup (configurable); enable auditing in ASM for
      access logs.

#### Benefits and Security Notes

- **No Credentials in Artifact**: `prod.yml` ships with placeholders only—secrets are pulled runtime from ASM.
- **Least Privilege**: ASM enforces role-based access (e.g., only prod env can read prod secrets).
- **Encryption in Transit/Rest**: All ASM calls use TLS; secrets are encrypted at rest.
- **Fallbacks**: If ASM fetch fails (e.g., network issue), the app can fail-fast or use defaults (configure via error
  handlers).
- **Limitations**: ASM is for Runtime Fabric/CloudHub 2.0 primarily; for on-prem, consider Vault integration via the
  connector.

#### Troubleshooting Common Issues

- **Placeholder Not Resolving**: Ensure the prefix matches your config (default `asm:`) and secret ID is exact.
- **Auth Errors**: Double-check Connected App scopes (e.g., "Read Secrets").
- **Logs**: Set `logger.level=DEBUG` for `com.mulesoft.secrets` to trace fetches.

For more details, check these official sources:

- [Anypoint Security Secrets Manager Overview](https://docs.mulesoft.com/anypoint-security/index-secrets-manager)
- [Secure Configuration Properties](https://docs.mulesoft.com/mule-runtime/latest/secure-configuration-properties)
- [Configuring Properties](https://docs.mulesoft.com/mule-runtime/latest/configuring-properties)

If you share your current `global.xml` or `prod.yml` snippet (redacted), I can refine this further!