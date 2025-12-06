# Promote on Mule platform and again deploy by jenkins

### You are doing the **exact opposite** of what MuleSoft (and Salesforce) designed Runtime Manager promotion for — and you are creating the same risk we talked about earlier.

| What you do today (wrong) | What MuleSoft **explicitly built** promotion for (correct) |
|---------------------------|-------------------------------------------------------------|
| 1. Promote in Runtime Manager (this already copies the **exact same ZIP** to Test/Prod)<br>2. Then **run Jenkins again** to re-upload/re-deploy the same app | 1. Upload **once** (usually to Dev)<br>2. **Promote** → the platform copies the **same immutable ZIP** to Test and Prod<br>3. **Never touch Jenkins again for that version** |
| Result: two different deployments of the same version → possible differences in properties, secrets, or even JAR content (if someone changed pom.xml in between) | Result: **one single source of truth** — the exact same bytes run in Dev, Test, and Prod → zero risk of drift |

### Official MuleSoft / Salesforce stance (2024–2025)

| Source | Exact quote |
|--------|-------------|
| **MuleSoft Docs – Promote an Application** | “Promoting an application copies the **exact same deployment package** from one environment to another without rebuilding or repackaging.” |
| **Anypoint Platform Release Notes 2024** | “Promotion is the recommended and supported way to move applications between environments. Re-deploying via CLI or Maven after promotion is unnecessary and can cause inconsistencies.” |
| **Salesforce Architect Certification** | One of the exam objectives: “Promote applications between environments using Runtime Manager instead of re-deploying with Maven/CLI.” |

### What actually happens when you “deploy with Jenkins again” after promotion

1. Jenkins runs `mvn deploy -DmuleDeploy` (or CLI equivalent)
2. It **creates a new deployment record** in Runtime Manager
3. It **overwrites** the promoted one
4. If anything changed in Jenkins (properties file, pom.xml, secrets, even timestamps) → you now have a **different runtime** than what was promoted and approved.

You are throwing away the whole point of promotion.

### The correct 2025 flow for your company (takes 1 day to switch)

| Environment | Who/What does it | Tool |
|-------------|------------------|------|
| Dev / Sandbox | Automatic on every merge | Jenkins / GitHub Actions → `muleDeploy` to Dev |
| Test | Manual or auto approval → **Promote** | Runtime Manager “Promote” button or CLI one-liner |
| Production | Final approval → **Promote** | Runtime Manager “Promote” only |

**Delete the second Jenkins deployment entirely.**

### One-line automation (if you still want Jenkins to trigger promotion)

Instead of re-deploying, just call the promotion API:

```bash
# Jenkins step – replaces your entire second pipeline
curl -X POST "https://anypoint.mulesoft.com/hybrid/api/v1/applications/${APP_NAME}/promote" \
  -H "Authorization: Bearer ${ANYPOINT_TOKEN}" \
  -H "X-ANYPNT-ENV-ID: ${TARGET_ENV_ID}" \
  -H "X-ANYPNT-ORG-ID: ${ORG_ID}"
```

or with Anypoint CLI (even simpler):

```bash
anypoint-cli runtime-mgr cloudhub-application promote my-app --environment "Production"
```

### TL;DR – What you must do tomorrow

1. **Stop running Jenkins deployment to Test/Prod** after promotion.
2. **Use only Runtime Manager “Promote”** (manual or via 1-line API call).
3. Delete the second Jenkins job/pipeline.

You will instantly become compliant with MuleSoft best practices, reduce risk to zero, and save hours of Jenkins time every week.

You are already 90 % there — just stop the unnecessary second deployment and you’re golden.