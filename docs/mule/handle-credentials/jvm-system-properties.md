# JVM system properties

In **hybrid/on-premises Mule deployments** (standalone Mule runtime registered with Anypoint Runtime Manager), you can set sensitive values (e.g., passwords, API keys, tokens) directly as **JVM system properties** or **OS environment variables** on the server. This completely bypasses Runtime Manager's Properties tab, avoiding visibility of clear-text values in the Anypoint Platform UI.

### Why Use This Approach?
- **Security**: Sensitive values never appear in Runtime Manager (where they remain visible in hybrid mode). They load directly into the Mule runtime's memory at startup.
- **Control**: You manage secrets at the OS/server level (e.g., via secure env vars, secret managers, or restricted files), ideal for compliance in on-premises environments.
- **Precedence**: These override lower-priority sources (e.g., bundled properties files) per Mule's property hierarchy:
   1. Deployment properties (e.g., Runtime Manager)
   2. System properties (JVM -D flags)
   3. Environment properties (OS env vars)
   4. Application properties (e.g., .yaml files)
   5. Global properties
- **Common for secrets**: Often combined with Secure Configuration Properties module (for encrypted bundled files) by passing the decryption key this way.

### How to Set JVM System Properties
These are Java -D arguments passed to the Mule runtime JVM.

1. **Via command line** (temporary, for testing or one-off starts):
   ```
   $ mule start -M-Ddb.password=superSecretPass -M-Dapi.key=abc123
   ```
   - The `-M-` prefix ensures Mule processes it correctly.
   - Values exist only in memory; must re-provide on restart.

2. **Persistently via wrapper.conf** (recommended for production; located at `$MULE_HOME/conf/wrapper.conf`):
   Add lines like:
   ```
   wrapper.java.additional.10=-Ddb.password=superSecretPass
   wrapper.java.additional.11=-Dapi.key=abc123
   ```
   - Use sequential unused numbers (e.g., 10, 11) to avoid conflicts.
   - Set `wrapper.ignore_sequence_gaps=TRUE` if gaps exist.
   - Restart Mule for changes to apply.
   - **Security tip**: Restrict file permissions (e.g., chmod 600) since values are clear-text in the file.

### How to Set OS Environment Variables
Mule automatically reads standard OS environment variables at startup.

1. **Set in the shell** before starting Mule:
   ```
   export DB_PASSWORD=superSecretPass
   export API_KEY=abc123
   $ mule start
   ```

2. **Persistently**:
   - On Linux/Unix: Add to `/etc/environment`, user profile (~/.bash_profile), or the Mule startup script.
   - Integrate with secret managers (e.g., HashiCorp Vault, AWS Secrets Manager) to inject vars dynamically.
   - For Secure Properties: Commonly used for the decryption key, e.g., `export MULE_SECRET_KEY=myMasterKey`.

### Referencing in Your Mule App
Use standard placeholders:
```xml
<db:config>
    <db:connection host="${db.host}" password="${db.password}" />  <!-- From system prop or env var -->
</db:config>
```
Or for secure properties:
```xml
<secure-properties:config key="${mule.secret.key}" file="encrypted-prod.yaml"/>
```

### Best Practices and Considerations
- **Protect the server**: Lock down OS access—anyone with shell access can view env vars (via `ps -ef` for command-line args) or the wrapper.conf file.
- **Combine with other tools**:
   - Use Mule's Secure Configuration Properties module for bundled encrypted values, overriding the key via env var/system prop.
   - For advanced setups, integrate external vaults (e.g., Azure Key Vault Properties Provider connector).
- **Avoid for non-sensitive**: Use Runtime Manager for non-secrets to leverage central management.
- **Testing**: In Anypoint Studio, set via Run Configurations > Arguments (VM arguments: `-Ddb.password=...`).

This method is a MuleSoft-recommended practice for on-premises/hybrid secrets management. See docs on [Configuring Properties](https://docs.mulesoft.com/mule-runtime/latest/configuring-properties) and [System Properties](https://docs.mulesoft.com/mule-runtime/latest/mule-app-properties-system) for latest details.
