# ONE Jenkins pipeline

Yes — in 2025, **the best-practice answer is: use exactly ONE Jenkins pipeline** (or one GitHub Actions workflow, one GitLab CI file, etc.) — not two.

This is what every mature team (Google, Netflix, Amazon, Salesforce, MuleSoft, etc.) does today.

### The correct modern pattern: **Single pipeline with stages and manual/automated gates**

```yaml
# Jenkinsfile (or .github/workflows/deploy.yml)
pipeline {
    stages {
        stage('Build & Test') { … }                     # runs on every commit
        stage('Upload Artifact') { … }                  # to Artifactory/Nexus
        stage('Deploy to Dev') { … }                    # auto
        stage('Integration Tests in Dev') { … }         # auto
        stage('Deploy to Test') { 
            when { expression { env.BRANCH_NAME == 'main' } }
            input { message "Promote to Test?" }        # manual approval
            steps { … }                                 # same artifact!
        }
        stage('Deploy to Prod') { 
            input { message "Promote to Production?" }
            steps { … }                                 # same artifact again!
        }
    }
    post {
        always { cleanWs() }
    }
}
```

Key points:
- **Only one `mvn package` / `mvn deploy`** → one immutable JAR
- **Same exact JAR** moves from Dev → Test → Prod
- No rebuild, no git clone again, no risk of drift
- Approvals are just **input steps** or external tools (ServiceNow, OpsGenie, etc.)

### Real-world examples that already do this (2025)

| Company / Tool              | How they do it with one pipeline / workflow                              |
|-----------------------------|--------------------------------------------------------------------------|
| **Google**                  | Monorepo + single Bazel build + promotion via Release Please            |
| **Netflix**                 | Spinnaker + single immutable AMI/Docker image                           |
| **Salesforce / MuleSoft**   | One Jenkins/GitHub Actions → build → upload to Artifactory → Runtime Manager promotion (no rebuild) |
| **GitHub Actions users**    | `workflow_dispatch` + reusable workflows + `environment` approvals     |
| **GitLab CI**               | One `.gitlab-ci.yml` with `rules:` and `when: manual`                    |

### Why one pipeline beats two pipelines

| Problem with two pipelines                     | Solved by one pipeline                              |
|------------------------------------------------|-----------------------------------------------------|
| Risk of different builds                       | Only one build ever happens                         |
| Harder to audit who promoted what              | Single source of truth in one run                   |
| Twice the maintenance (two Jenkinsfiles)      | One file to maintain                                |
| Text file / custom metadata hacks              | JFrog Build Info or Git tags give you everything   |

### Quick migration plan for your team (1–2 days max)

1. Merge your two Jenkinsfiles into one.
2. Keep the build + upload stages at the top.
3. Add `input { message "Promote to Test?" }` and `input { message "Go to Prod?" }` steps.
4. Change the higher-environment stages to **download the artifact from Artifactory** instead of git-clone + rebuild.
5. Delete the custom text file logic (JFrog already stores git commit, build number, etc.).

That’s it.  
You go from “risky & outdated” to “2025 industry best practice” in one afternoon.
