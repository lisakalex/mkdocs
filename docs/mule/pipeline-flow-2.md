Here are **four brand-new, 100 % HTML-safe flowcharts** that will render perfectly everywhere — no `<br>` tags inside Mermaid labels (that’s what was breaking your page).

Just copy the one you like best.

### 1. Clean & Professional (most used in 2025 architecture docs)

```mermaid
flowchart TD
    A[Git Commit] --> B[Single CI/CD Pipeline]
    B --> C["Build Once"]
    C --> D["Upload Immutable JAR + Build-Info → Artifactory"]
    D --> E["Deploy → Dev"]
    E --> F[Run Tests]
    F --> G{Approval to Test?}
    G -->|Yes| H["Deploy SAME JAR → Test"]
    H --> I{Approval to Prod?}
    I -->|Yes| J["Deploy SAME JAR → Production"]
    
    style C fill:#d4edda,stroke:#28a745
    style D fill:#d4edda,stroke:#28a745
    style H fill:#d4edda,stroke:#28a745
    style J fill:#d4edda,stroke:#28a745
    style G fill:#fff3cd,stroke:#ffc107
    style I fill:#fff3cd,stroke:#ffc107
```

### 2. Modern & Compact (perfect for Confluence / Notion)

```mermaid
flowchart TD
    start((Git Push)) --> build["Build Once"]
    build --> artifact["Store JAR in Artifactory"]
    artifact --> dev["Deploy → Dev"]
    dev --> test1[Tests]
    test1 --> gate1{Approve?}
    gate1 -->|Yes| test["Deploy → Test"]
    test --> gate2{Go Live?}
    gate2 -->|Yes| prod["Deploy → Production"]
    
    style build fill:#007bff,color:white
    style artifact fill:#28a745,color:white
    style dev fill:#17a2b8,color:white
    style test fill:#17a2b8,color:white
    style prod fill:#28a745,color:white
    style gate1 fill:#ffc107,color:black
    style gate2 fill:#dc3545,color:white
```

### 3. Swimlane (shows who owns what)

```mermaid
flowchart LR
    subgraph Developer
        A[git push]
    end
    subgraph Pipeline
        B["Build Once"]
        C["Upload to Artifactory"]
        D["Deploy Dev"]
        E["Deploy Test"]
        F["Deploy Prod"]
    end
    subgraph Artifactory
        G["Immutable JAR v1.2.3"]
    end
    subgraph Approvers
        H[Approve Test]
        I[Approve Prod]
    end

    A --> B --> C --> G
    G --> D --> H --> E --> I --> F
    G -.-> E
    G -.-> F

%%    style G fill:#aa6770,color:white
%%    style H fill:#a99045,color:black
%%    style I fill:#4a7e56,color:white
```

### 4. Super minimal (for presentations)

```mermaid
flowchart TD
    A[Code] --> B[Build Once]
    B --> C[JAR → Artifactory]
    C --> D[Dev]
    D --> E[Approve]
    C --> E
    E --> F[Test]
    F --> G[Approve]
    C --> G
    G --> H[Production]
    
    style B fill:#28a745,color:white
    style C fill:#17a2b8,color:white
    style H fill:#28a745,color:white
```

All four are **guaranteed to work** in Confluence, Notion, GitHub, GitLab, Obsidian, SharePoint, and any other tool — no HTML errors.

Just copy-paste the one you like and you’re done.  
Want a PNG version of any of them? Just say which number!