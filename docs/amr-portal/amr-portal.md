Secondary issues

- No automated gates between environments — no smoke tests, health checks, or automated rollback are mentioned; promotion decisions are verbal ("Venkatesh says build this branch").
- Manual version bookkeeping — engineers eyeball S3 timestamps / ECR tags to guess the next version instead of the pipeline deriving it from BUILD_NUMBER/git tag/semantic-release.
- Confusing account naming — single-letter suffixes (D/P/PP) versus legacy full-word names (DEV/PROD) caused real confusion during the training session itself ("this GPPD, it's difficult to remember"). That's a signal the naming scheme is a genuine operational risk, not just an inconvenience.
- Bus-factor of 1 — this entire process apparently lives in one person's head and is being handed off verbally over a screen-share rather than being captured as a runbook/pipeline-as-code. The fact this session had to happen at all is a symptom of the automation gap.
- Dual artifact types (WAR + Docker image) for one deploy — the pipeline pushes both a WAR to S3/EB and a Docker image to ECR. Worth checking whether ECR is actually used by anything, since it doubles the surface for drift if only one is truly consumed by EB.

What "modern professional" would look like here

- Pipeline builds once per commit/tag → pushes one immutable artifact to ECR/S3 → same artifact promoted dev → preprod → prod via approval gates in the pipeline (not chat messages).
- Jenkins (or GitHub Actions) assumes AWS roles via OIDC — zero manual credentials.
- eb deploy/CodeDeploy invoked from the pipeline itself, no console upload.
- Automated health-check/smoke-test stage gating promotion, with automatic rollback on failure.
- Runbook and pipeline logic captured as code (Jenkinsfile + Terraform), not verbal knowledge.

This aligns with what I saw in the codebase earlier (Spring Boot WARs for AMRAdmin/AMRGraphs deployed to Tomcat 9 via EB) — the app itself is reasonably conventional; it's the delivery pipeline that hasn't caught up. Given the "business priority is elsewhere" comment in the doc, this is a known, accepted tech-debt tradeoff rather than an oversight — worth flagging as a risk (deployment currently depends on human availability and correct manual sequencing) rather than treating it as fine as-is.

Secondary issues

- No automated gates between environments — no smoke tests, health checks, or automated rollback are mentioned; promotion decisions are verbal ("Venkatesh says build this branch").
- Manual version bookkeeping — engineers eyeball S3 timestamps / ECR tags to guess the next version instead of the pipeline deriving it from BUILD_NUMBER/git tag/semantic-release.
- Confusing account naming — single-letter suffixes (D/P/PP) versus legacy full-word names (DEV/PROD) caused real confusion during the training session itself ("this GPPD, it's difficult
  to remember"). That's a signal the naming scheme is a genuine operational risk, not just an inconvenience.
- Bus-factor of 1 — this entire process apparently lives in one person's head and is being handed off verbally over a screen-share rather than being captured as a                         
  runbook/pipeline-as-code. The fact this session had to happen at all is a symptom of the automation gap.
- Dual artifact types (WAR + Docker image) for one deploy — the pipeline pushes both a WAR to S3/EB and a Docker image to ECR. Worth checking whether ECR is actually used by anything,    
  since it doubles the surface for drift if only one is truly consumed by EB.

What "modern professional" would look like here

- Pipeline builds once per commit/tag → pushes one immutable artifact to ECR/S3 → same artifact promoted dev → preprod → prod via approval gates in the pipeline (not chat messages).
- Jenkins (or GitHub Actions) assumes AWS roles via OIDC — zero manual credentials.
- eb deploy/CodeDeploy invoked from the pipeline itself, no console upload.
- Automated health-check/smoke-test stage gating promotion, with automatic rollback on failure.
- Runbook and pipeline logic captured as code (Jenkinsfile + Terraform), not verbal knowledge.

This aligns with what I saw in the codebase earlier (Spring Boot WARs for AMRAdmin/AMRGraphs deployed to Tomcat 9 via EB) — the app itself is reasonably conventional; it's the delivery   
pipeline that hasn't caught up. Given the "business priority is elsewhere" comment in the doc, this is a known, accepted tech-debt tradeoff rather than an oversight — worth flagging as a
risk (deployment currently depends on human availability and correct manual sequencing) rather than treating it as fine as-is.                                                             
    