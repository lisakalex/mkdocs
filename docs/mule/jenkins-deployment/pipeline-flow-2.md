# Secure Mule Deployment Pipeline

This Jenkins-based CI/CD process securely deploys a MuleSoft application to Anypoint Platform (CloudHub / Runtime
Fabric). Sensitive credentials are encrypted using Blowfish in YAML files. The encryption key is managed securely in
Jenkins during build and added to Runtime Manager properties for runtime decryption. The Mule API then uses the
decrypted credentials to connect to databases or external APIs.

### Process Steps

1. Retrieve `dev.yml` from source control (AWS CodeCommit)
2. Use the key file (with credentials) to create `test.yml`
3. In Jenkins pipeline, fetch the Blowfish encryption key from secure credentials store
4. Build the Mule application (Maven) and deploy it to Anypoint Platform via Runtime Manager
5. In Runtime Manager, add the Blowfish key as a secure application property
6. At runtime, Mule uses the Secure Configuration Properties module + Blowfish key to decrypt credentials
7. The application starts and securely connects to databases or other APIs using the decrypted values

This approach keeps credentials encrypted in source control and artifacts, with decryption only happening at runtime on
the Mule platform.

```mermaid
sequenceDiagram
    participant J as Jenkins Pipeline
    participant AR as Jfrog Artifactory
    participant RM as Mule Runtime Manager
    participant Mule as Mule Application<br>(Runtime)
    J ->> J: 1. Get dev.yml<br>and read credentials
    J ->> J: Read Blowfish encryption key<br>from Jenkins credentials store
    J ->> J: 2. Get key file / key value
    J ->> J: Generate test.yml<br>(inject key / prepare credentials)
    J ->> AR: Upload Mule app JAR<br>+ test.yml (optional)
    AR -->> J: Artifacts stored
    J ->> RM: 4. Deploy application<br>to Mule platform<br>(CloudHub / RTF / On-prem)
    activate RM
    RM ->> Mule: Start application on worker
    RM ->> RM: 5. Add Blowfish encryption key<br>to application properties<br>(secure / normal property)
    deactivate RM

    loop API receives requests
        Mule ->> Mule: Load Blowfish key<br>from Runtime Manager properties
        Mule ->> Mule: 6. Decrypt encrypted credentials<br>(from YAML / properties)
        Mule ->> Mule: 7. Use decrypted credentials<br>to connect to external<br>APIs / Databases / Services
    end
```
