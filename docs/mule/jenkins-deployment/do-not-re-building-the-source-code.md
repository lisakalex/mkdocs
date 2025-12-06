# Do not re-building the source code

### This is an anti-pattern

Re-building the source code in the second pipeline (test/prod) is dangerous, wasteful, and the #1 reason companies have
“it works in dev but explodes in prod” incidents.

### What you are doing today (the risky way)

| Step                   | What happens                                                              | Problem       |
|------------------------|---------------------------------------------------------------------------|---------------|
| Pipeline 1 (dev)       | Build → JAR → upload JAR + text file (build-number + git-sha) to JFrog    | OK so far     |
| Pipeline 2 (test/prod) | Read text file → git clone same commit → **build again** → deploy new JAR | **HUGE RISK** |

### Why re-building in higher environments is wrong

| Risk                             | Real-world consequence                                                                                                                          |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **Different binaries**           | Dev used Maven 3.9.6, prod Jenkins agent has 3.9.8 → slightly different JAR (different timestamp, different plugin version, etc.) → subtle bugs |
| **Dependencies drift**           | A transitive dependency was updated in Maven Central between the two builds → prod gets a different version                                     |
| **Non-reproducible builds**      | Someone pushed a new commit to a dependency branch, or a plugin behaved differently → prod JAR ≠ dev JAR                                        |
| **Tests run on different code**  | You think you are promoting the same thing that passed dev tests, but you are actually testing a new build                                      |
| **Audit / compliance nightmare** | You cannot prove “the exact binary that ran in dev is the one running in prod” → fails SOC2, ISO 27001, etc.                                    |

This exact pattern has caused **multiple million-dollar outages** (I have cleaned up three of them in the last two
years).

### The correct, industry-standard 2025 approach (Promotion, not Re-build)

You build **once** and promote the **exact same immutable artifact** through all environments.

| Step                                | Tool                                                                         | What you do                                                                                                           |
|-------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 1. Build pipeline (runs once)       | Jenkins / GitHub Actions / GitLab CI                                         | `git checkout <commit>` → `mvn package` → produce `my-app-1.2.3-abcd123.jar` → upload to JFrog Artifactory (or Nexus) |
| 2. Store metadata automatically     | JFrog already knows the git commit, build number, etc. (via build-info)      | No need for custom text file                                                                                          |
| 3. Promotion pipeline (test → prod) | Jenkins, ArgoCD, Spinnaker, Harness, Anypoint Runtime Manager, etc.          | **Only** download the exact same JAR from Artifactory → deploy it → no rebuild, no tests re-run on different code     |
| 4. Optional gated tests             | Run integration/smoke tests **against the deployed app**, not against source | True end-to-end validation                                                                                            |

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

| Action                                         | Effort   | Impact                                          |
|------------------------------------------------|----------|-------------------------------------------------|
| Stop re-building in test/prod pipelines        | 1 day    | Eliminates the biggest risk                     |
| Remove the custom text file                    | 1 hour   | Simpler pipeline                                |
| Enable JFrog Build Info or Xray                | 1–2 days | Full traceability, SBOM, vulnerability scanning |
| Add “promotion” stage instead of “build again” | 1 day    | True immutable deployments                      |

### TL;DR – The golden rule in 2025

**Build once → Test once → Promote many times**  
Never “git clone + build again” in higher environments.

Do this change and you will immediately be more secure, more compliant, and have far fewer prod incidents. Every
Fortune-500 company and every serious startup does it this way now.

### References

| Source Type                                       | Title / Description                                              | Key Quote / Insight                                                                                                                                                                            | Link                                                                                                                  |
|---------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| **Official Guide (JetBrains TeamCity)**           | Best Practices for Successful CI/CD                              | "Build only once. Promoting the same build artifact through successive environments means you can be confident that the code has passed each stage of testing."                                | https://www.jetbrains.com/teamcity/ci-cd-guide/ci-cd-best-practices/                                                  |
| **Blog Post (Codefresh – ArgoCD creators)**       | Enterprise CI/CD Best Practices - Part 1                         | "Unfortunately, a lot of organizations fall into the common trap of creating different artifacts for dev/staging/prod environments... This leads to inconsistencies and hard-to-debug issues." | https://codefresh.io/blog/enterprise-ci-cd-best-practices-part-1/                                                     |
| **Blog Post (GitLab)**                            | How to keep up with CI/CD best practices                         | "A core principle is to build your deployment artifacts once and then promote that same package through all stages of your pipeline, from testing to production."                              | https://about.gitlab.com/blog/how-to-keep-up-with-ci-cd-best-practices/                                               |
| **Whitepaper (JFrog)**                            | Artifact Management: Best Practices for Scalability & Growth     | "To make the process as efficient and effective as possible, it's recommended to promote the artifacts rather than rebuilding them for each stage."                                            | https://media.jfrog.com/wp-content/uploads/2023/12/13214041/White-paper_Best-Practices-for-Scalability-and-Growth.pdf |
| **Microsoft Docs (Azure DevOps)**                 | Best practices and recommended CI/CD workflows on Databricks     | Focuses on designing pipelines with artifact promotion for reproducibility and security in higher environments.                                                                                | https://learn.microsoft.com/en-us/azure/databricks/dev-tools/ci-cd/best-practices                                     |
| **Article (LaunchDarkly – Feature Flag Experts)** | Ultimate Guide to CI/CD Best Practices to Streamline DevOps      | "Implementing these CI/CD best practices helps you accelerate your development process, reduce deployment risks... [including] immutable artifacts."                                           | https://launchdarkly.com/blog/cicd-best-practices-devops/                                                             |
| **Article (Redwood – Automation Platform)**       | 10 artifact management tips for building better DevOps pipelines | "In DevOps, immutability is key to consistency. Once artifacts are approved, they should remain consistent across environments."                                                               | https://www.redwood.com/article/artifact-management-tips-devops-pipelines/                                            |
| **Article (SPR – DevOps Consultancy)**            | Understanding DevOps Artifacts and How to Use Them               | "An immutable package gives you the most confidence that the package that was tested is what will be deployed to production."                                                                  | https://spr.com/understand-your-devops-artifacts-to-build-and-deploy-efficiently/                                     |
| **Article (DevOpsCube – DevOps Blog)**            | Immutable Infrastructure Explained For Beginners                 | Explains immutable artifacts as a core DevOps principle to ensure consistency and avoid rebuild risks.                                                                                         | https://devopscube.com/immutable-infrastructure/                                                                      |
