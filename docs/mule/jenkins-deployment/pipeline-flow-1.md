This Jenkins pipeline automates deployment of a MuleSoft API while ensuring credential security.
Jenkins retrieves dev.yml from the repository and extracts credentials.
It reads a key file to generate a new test.yml configuration dynamically.
The Blowfish encryption key is securely fetched from Jenkins credentials.
The API package is deployed to the Mule runtime platform.
Jenkins sets the Blowfish key as a runtime property in Mule Runtime Manager.
At runtime, the API decrypts its credentials using the Blowfish key.
The decrypted credentials are used to connect securely to other APIs or databases.

Would you like me to render this diagram visually (as an image swimlane chart) for presentation or documentation use?

sequenceDiagram
participant J as Jenkins Pipeline
participant AR as Artifact Repo<br>(Nexus/Artifactory)
participant RM as Mule Runtime Manager
participant Mule as Mule Application (Runtime)

[//]: # (![mermaid-diagram.svg]&#40;img/mermaid-diagram.svg&#41;)

```mermaid
sequenceDiagram
    participant J as Jenkins Pipeline
    participant AR as Artifact Repo<br>(Nexus / Artifactory)
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
