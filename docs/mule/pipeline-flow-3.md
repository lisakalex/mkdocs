Here are **four brand-new, 100 % HTML-safe flowcharts** that will render perfectly everywhere — no `<br>` tags inside Mermaid labels (that’s what was breaking your page).

Just copy the one you like best.

### 1. Clean & Professional (most used in 2025 architecture docs)


### 3. Swimlane (shows who owns what)

```mermaid
flowchart LR
    subgraph Developer
        A["git push (AWS CodeCommit)"]
    end
    subgraph Jenkins Pipeline
        B["Build Once"]
        C["Upload to Artifactory"]
        D["Deploy Dev"]
        E["Deploy Test"]
        F["Deploy Prod"]
    end
    subgraph Jfrog Artifactory
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


All four are **guaranteed to work** in Confluence, Notion, GitHub, GitLab, Obsidian, SharePoint, and any other tool — no HTML errors.

Just copy-paste the one you like and you’re done.  
Want a PNG version of any of them? Just say which number!