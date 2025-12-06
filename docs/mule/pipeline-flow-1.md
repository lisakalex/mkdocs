Here is a **perfectly valid Mermaid sequence diagram** (works in Mermaid 11.12.2 and newer) that clearly shows the **current risky approach** vs the **correct 2025 approach** side-by-side.

Just copy-paste into https://mermaid.live or any modern Markdown renderer:

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant Git as Git Repo
    participant Jenk as Jenkins
    participant JFrog as JFrog Artifactory
    participant Env as Dev / Test / Prod

    rect rgb(255,230,230)
    Note over Dev,Env: Current anti-pattern (dangerous)
    Dev->>Git: git push
    Jenk->>Git: checkout commit
    Jenk->>Jenk: Build JAR v1 (dev)
    Jenk->>JFrog: upload JAR + text file (commit + build#)
    Jenk->>Env: deploy JAR v1 → Dev
    Note right of Jenk: Manual trigger
    Jenk->>JFrog: download text file
    Jenk->>Git: checkout SAME commit again
    Jenk->>Jenk: REBUILD JAR → v2 (different!)
    Jenk->>Env: deploy JAR v2 → Test/Prod
    Note over Jenk,Env: Works in Dev, explodes in Prod
    end

    rect rgb(220,255,220)
    Note over Dev,Env: Correct 2025 way (ONE pipeline)
    Dev->>Git: git push
    Jenk->>Git: checkout commit
    Jenk->>Jenk: Build JAR once → v1
    Jenk->>JFrog: upload immutable JAR + Build-Info
    Jenk->>Env: deploy SAME JAR v1 → Dev
    Jenk->>Env: run integration tests
    Note right of Jenk: Manual or auto approval
    alt Approve promotion
        Jenk->>JFrog: download SAME JAR v1
        Jenk->>Env: deploy SAME JAR v1 → Test
        Note right of Jenk: Approval for Prod
        Jenk->>JFrog: download SAME JAR v1
        Jenk->>Env: deploy SAME JAR v1 → Prod
    end
    Note over Jenk,Env: 100% reproducible, safe, auditable
    end
```

### What this sequence diagram instantly proves to managers, architects, and auditors:

| Current way | Correct way |
|-------------|-------------|
| Build happens **twice** → two different JARs | Build happens **once** → one immutable JAR |
| Risky manual text-file logic | Clean, automatic Build-Info from JFrog |
| “It worked in Dev” = false confidence | “It worked in Dev” = real confidence |

Paste this into Confluence, Notion, GitHub PR description, or your internal wiki — everyone will understand in 10 seconds why you must switch to **one pipeline + artifact promotion**.

You now have both a **flowchart** (previous message) and a **sequence diagram** — perfect for any presentation or architecture review board.