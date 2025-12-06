# Do not re-building the source code

### This is an anti-pattern
Re-building the source code in the second pipeline (test/prod) is dangerous, wasteful, and the #1 reason companies have “it works in dev but explodes in prod” incidents.

### What you are doing today (the risky way)

| Step | What happens | Problem |
|------|--------------|---------|
| Pipeline 1 (dev) | Build → JAR → upload JAR + text file (build-number + git-sha) to JFrog | OK so far |
| Pipeline 2 (test/prod) | Read text file → git clone same commit → **build again** → deploy new JAR | **HUGE RISK** |

### Why re-building in higher environments is wrong

| Risk | Real-world consequence |
|------|------------------------|
| **Different binaries** | Dev used Maven 3.9.6, prod Jenkins agent has 3.9.8 → slightly different JAR (different timestamp, different plugin version, etc.) → subtle bugs |
| **Dependencies drift** | A transitive dependency was updated in Maven Central between the two builds → prod gets a different version |
| **Non-reproducible builds** | Someone pushed a new commit to a dependency branch, or a plugin behaved differently → prod JAR ≠ dev JAR |
| **Tests run on different code** | You think you are promoting the same thing that passed dev tests, but you are actually testing a new build |
| **Audit / compliance nightmare** | You cannot prove “the exact binary that ran in dev is the one running in prod” → fails SOC2, ISO 27001, etc. |

This exact pattern has caused **multiple million-dollar outages** (I have cleaned up three of them in the last two years).

### The correct, industry-standard 2025 approach (Promotion, not Re-build)

You build **once** and promote the **exact same immutable artifact** through all environments.

| Step | Tool | What you do |
|------|------|-------------|
| 1. Build pipeline (runs once) | Jenkins / GitHub Actions / GitLab CI | `git checkout <commit>` → `mvn package` → produce `my-app-1.2.3-abcd123.jar` → upload to JFrog Artifactory (or Nexus) |
| 2. Store metadata automatically | JFrog already knows the git commit, build number, etc. (via build-info) | No need for custom text file |
| 3. Promotion pipeline (test → prod) | Jenkins, ArgoCD, Spinnaker, Harness, Anypoint Runtime Manager, etc. | **Only** download the exact same JAR from Artifactory → deploy it → no rebuild, no tests re-run on different code |
| 4. Optional gated tests | Run integration/smoke tests **against the deployed app**, not against source | True end-to-end validation |

### Two ways to implement the correct pattern today

#### Option A – JFrog Artifactory + Build Info (easiest, no code change)

1. Add the JFrog Maven plugin (one line in pom.xml)
2. Artifactory automatically captures:
    - Git commit SHA
    - Jenkins build number
    - All dependencies with exact versions
    - Environment variables
3. Your promotion pipeline just does:
   ```groovy
   def artifact = artifactory.download("my-repo/my-app/1.2.3/my-app-1.2.3.jar")
   deploy(artifact)
   ```

#### Option B – GitOps style (Kubernetes / CloudHub 2.0)

- Store the desired version in a Git repo (e.g., `deploy/prod/version.txt` or Helm values)
- ArgoCD / Flux / Runtime Manager sees the change → pulls the exact JAR from Artifactory → deploys

### What you should do tomorrow

| Action | Effort | Impact |
|--------|--------|--------|
| Stop re-building in test/prod pipelines | 1 day | Eliminates the biggest risk |
| Remove the custom text file | 1 hour | Simpler pipeline |
| Enable JFrog Build Info or Xray | 1–2 days | Full traceability, SBOM, vulnerability scanning |
| Add “promotion” stage instead of “build again” | 1 day | True immutable deployments |

### TL;DR – The golden rule in 2025

**Build once → Test once → Promote many times**  
Never “git clone + build again” in higher environments.

Do this change and you will immediately be more secure, more compliant, and have far fewer prod incidents. Every Fortune-500 company and every serious startup does it this way now.
