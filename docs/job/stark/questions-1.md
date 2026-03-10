# Questions 1

Here are thoughtful, structured answers to the interview questions/topics you listed. These are phrased in a natural,
first-person way so you can adapt them directly for your responses (e.g., during a behavioral or technical discussion).
They align with the role's focus: **Platform Engineering** mindset, heavy emphasis on **Developer Experience (DevEx)**
within a software development team, on-prem/hybrid environment (80% on-prem), standardization, and influencing practices
without being purely infra/cloud-heavy.

### 1. Tell me what you know about Git.

Git is a **distributed version control system** created by Linus Torvalds in 2005, designed for speed, efficiency, and
handling everything from small to massive projects (like the Linux kernel). Unlike centralized systems (e.g., older
SVN), every developer gets a full local copy of the repository, including history, branches, and commits—this enables
offline work, fast operations, and powerful branching/merging.

Key features I rely on daily:

- **Commits** as atomic snapshots with messages for traceability.
- **Branching** — cheap and fast, core to workflows (create, switch, merge, rebase).
- **Merging** strategies (fast-forward, recursive, squash) and conflict resolution.
- **Distributed nature** — push/pull to remotes (GitHub, GitLab, Azure Repos), remotes for collaboration.
- Tools like **.gitignore**, submodules, hooks, stash, cherry-pick, bisect for debugging history.

For branching strategies (very relevant to standardizing practices):

- I prefer **trunk-based development** or simplified **GitHub Flow** for most teams—short-lived feature branches off
  main, frequent merges via pull requests (PRs) with reviews, to keep integration fast and reduce merge hell.
- In more release-heavy environments, **GitFlow** (with develop, release, hotfix branches) works well, but I avoid it if
  it slows velocity unless needed for strict versioning.
- Best practices: Small, focused commits; meaningful messages (Conventional Commits style); rebase for clean history
  before PR; protect main branch; use PR templates/checks.

In a team, I'd advocate evaluating the current strategy and proposing one that fits release cadence, team size, and
on-prem constraints (e.g., self-hosted GitLab runners for CI).

### 2. Tell me about a time you’ve investigated/recommended a technology for use within the team.

**Example scenario** (adapt to your real experience; this is a strong, realistic one for a platform-focused role):

In a previous mid-sized team (~15–25 devs, hybrid on-prem/cloud setup), we had fragmented CI/CD: some used Jenkins
on-prem, others manual scripts or basic GitHub Actions. Builds were slow, inconsistent, and lacked visibility—devs spent
too much time waiting or debugging pipelines.

I took ownership to investigate alternatives. I:

- Surveyed the team on pain points (slow feedback, no standardized environments, hard to reproduce issues).
- Evaluated options: Stick with Jenkins (mature but heavy maintenance), move to GitLab CI (self-hosted runners fit our
  on-prem needs), Azure DevOps (good Microsoft integration), or GitHub Actions (cloud-first but we had data concerns).
- Built a quick PoC with self-hosted GitLab Runners on our existing infra—demonstrated faster parallel jobs, better
  caching, and integrated artifact handling.
- Presented pros/cons in a team session (cost, maintenance, DevEx impact, security for on-prem data).
- Recommended GitLab CI + self-hosted runners, with a migration plan phased over 2 sprints.

We adopted it, reduced build times ~40%, improved consistency, and devs loved the YAML-based pipelines + built-in MR
reviews. It became the standard, and I later mentored others on it.

This shows opinionated evaluation, focus on DevEx, and driving adoption—key for this role.

### 3. Experience with CI/CD.

I've built and maintained CI/CD pipelines extensively, focusing on reliability, speed, and developer
productivity—especially in hybrid/on-prem environments.

- Tools: Azure DevOps Pipelines (YAML, classic), GitLab CI/CD (self-hosted runners), GitHub Actions.
- Patterns: Multi-stage pipelines (build → test → deploy), parallel jobs, caching (Docker layers, dependencies),
  artifact promotion.
- Branching integration: PR-triggered builds, protected branches, status checks before merge.
- Automation: IaC with Terraform for env provisioning, PowerShell/Bash for custom tasks (e.g., data obfuscation in test
  envs).
- Observability in pipelines: Logging outputs, notifications (Teams/Slack), dashboards for pipeline health.
- On-prem specifics: Self-hosted runners/agents for compliance (no cloud egress for sensitive data), handling air-gapped
  setups if needed.

In one project, I standardized pipelines across squads, adding automated security scans (e.g., container vuln checks)
and environment promotion—cut deployment friction and gave devs faster feedback loops.

### 4. Platform engineering mindset, and how you differentiate between Platform, DevOps, and SRE roles.

(Emphasize DevEx focus, as the role sits in SW Development team—not pure infra.)

**Platform Engineering mindset** (what I'd bring here): Treat internal tools, environments, and workflows as **products
** for developers. The goal is golden paths that are self-service, secure-by-default, observable, and reduce cognitive
load—so devs focus on features, not fighting infra. It's about abstraction, standardization, and long-term enablement (
e.g., "inner dev loop" improvements like fast local envs, consistent CI, easy tracing).

**Differentiation**:

- **DevOps** — Cultural/practice shift: Break silos between dev and ops, automate delivery, emphasize collaboration and
  velocity (CI/CD, IaC). It's broad—"how we ship software faster and more reliably together."
- **SRE** — Applies software engineering to operations for **reliability**. Focus: Production systems uptime, SLOs/error
  budgets, incident response, toil reduction. Metrics-driven (MTTR, availability), often "you build it, you run it" with
  on-call.
- **Platform Engineering** — Builds the **internal developer platform** (IDP): Reusable tools, frameworks, self-service
  portals, golden paths. Primary stakeholder: Developers (improve productivity, happiness, onboarding). Less about
  running production 24/7, more about enabling squads to deliver. In 2026, it's the "how to scale DevEx" layer—often
  sits closer to dev teams.

In this role (inside SW Development), it's classic Platform Eng: Standardize practices/tooling, embed
observability/security, improve workflows—prioritizing DevEx over heavy ops/SRE duties.

### 5. Discussion around observability, logging approaches, and how you would approach improving developer workflows in an on-prem environment.

**Observability** (three pillars: metrics, logs, traces) is essential for understanding system behavior without
guessing—especially in distributed/on-prem setups where debugging is harder.

**Logging approaches** I'd advocate:

- **Structured logging** (JSON over plain text): Easy to parse/query (e.g., via ELK, Grafana Loki, or on-prem tools).
- Levels: DEBUG (local/dev), INFO (normal ops), WARN/ERROR (actionable).
- Context-rich: Correlation IDs (trace/span), service name/version, env, user/session if relevant—no PII.
- Semantic events: "payment_failed" vs generic "error."
- Best practices: Avoid logging secrets, rate-limit noisy logs, sample high-volume ones.

**Improving developer workflows in on-prem** (80% focus here):

1. **Start with assessment** — Audit current logging (scattered files? No central view?), tracing (none?), metrics (
   basic server CPU?).
2. **Embed observability by default** — Push libraries/standards (e.g., OpenTelemetry for auto-instrumentation in .NET
   apps) so devs get traces/logs with minimal code.
3. **Centralized, on-prem-friendly stack** — Self-hosted Prometheus + Grafana for metrics/dashboards; Loki or EFK for
   logs; Jaeger/Tempo for traces. Avoid cloud-only if data sovereignty matters.
4. **DevEx wins**:
    - Fast local envs with Docker Compose + pre-configured observability (e.g., local Grafana).
    - Automated test env refresh/obfuscation (scripted via pipelines).
    - Unified dashboards per service—devs see their app's health without ops tickets.
    - Tracing across services (e.g., RabbitMQ message correlation).
5. **Iterate** — Pilot with one squad, gather feedback, roll out standards via templates/docs/mentoring.
6. **Security** — RBAC on dashboards, encrypt logs in transit/rest.

Goal: Make "what broke?" answerable in minutes, not hours—boosting velocity and reducing frustration in on-prem
constraints.

These should position you as thoughtful, experienced, and aligned with their emphasis on DevEx, standardization, and
on-prem realities. Practice delivering them conversationally, and tie back to their context (e.g., post-acquisition
growth, energy data platforms). Good luck with the interview! If you want tweaks or more examples, just say.
