# Business idea research

## Constraints (why ideas get filtered the way they do)

- Time: evenings/weekends, not full-time
- Budget: $200-2,000 self-funded, no outside investment
- Edge: technical — can build the whole product solo (Django + Claude API stack)
- Want: something owned long-term, recurring revenue — not a one-off sale or a service trading time for money
- Heuristic that's emerged: competitors who are other indie/solo builders = healthy signal (proves demand, proves
  solo-buildable). Competitors who are VC-funded giants ($10M+) = avoid, can't compete on the same pitch with this
  budget.

## Realistic expectations (odds of a big exit)

Asked how realistic "solo dev writes program, sells for millions" stories are. Two things to keep separate:

**The stories are real, but outliers:**

- Markus Frind — Plenty of Fish: built solo in 2 weeks, ran as a one-man company
  clearing ~$10M/year profit by 2008, no VC ever, sold to Match Group for $575M cash in 2015, kept most of it (never
  diluted ownership).
- Markus "Notch" Persson — Minecraft: wrote it solo in Java starting 2009, grew Mojang into a small team, sold to
  Microsoft for $2.5B in 2014.

**The base rate is brutal:** 55% of indie developers work solo, solo projects have ~70% failure rate. On Steam, median
lifetime revenue for an indie game is just $4,000 total, and the top 1% of indie developers capture 90% of all indie
revenue. Classic survivorship bias — the visible community is dominated by rare winners.

**Two different targets, don't conflate them:**

1. "Sell for millions/billions" (Frind/Notch tier) — a lottery ticket. Requires skill + timing + luck/virality. Not a
   plan.
2. A realistic good outcome from the micro-SaaS pattern above (e.g. $10-50k MRR, like Notionlytics) — if sold later,
   typical small-SaaS multiples (~3-6x ARR) land in the low-to-mid six figures, maybe low seven in a strong case.
   Genuinely good money, not "millions of pounds" territory.

Conclusion: keep building toward the micro-SaaS/recurring-revenue plan already in progress — it's a good bet with real
historical outcomes at the modest end. Don't plan around hitting the Frind/Notch outcome specifically.

## Chances of attracting VC (general, not idea-specific)

Asked what the odds actually are of attracting VC funding at all, given the solo/self-funded situation.

- Only ~0.05% of startups ever raise VC (~100 out of 100,000 ventures). Even top-tier firms (a16z) fund only ~0.7% of
  what they see.
- Solo founders are structurally disadvantaged: made up 35% of startups launched in 2024 but only 17% of VC rounds
  closed that year — investors prefer teams (redundancy, complementary skills). Solo founders also raise ~60% less on
  average than teams when they do get funded, and the gap widens at Series A.
- First-time founders: ~18% overall startup success rate, below repeat founders.
- Counterpoint: 94% of eventual billion-dollar-outcome entrepreneurs actually bootstrapped their initial takeoff without
  VC — most big eventual successes didn't start with venture money as the plan.
- What actually moves the odds (per this data): build real traction first (revenue, users, retention) before approaching
  anyone; target angels/pre-seed before large VCs; sell "solo" as a speed/focus advantage rather than hide it.

Conclusion: consistent with the B2B-AI-agent section above — VC is not a starting strategy here, it's something to
reconsider only after the bootstrapped micro-SaaS plan shows real traction, if ever.

## Reality check: does "people make money in crypto" hold up?

Asked whether the perception that many people make/keep making money in crypto (via trading or startups) matches
reality. Separated into three distinct activities with very different odds:

**Trading — a losing game for most participants:**

- 97% of retail crypto traders lose money within 3 months (2024 CoinGecko study)
- 84% lost money in their first year, 58% lost nearly all starting capital (Aug 2025 survey, n=1,005)
- ~75% of retail Bitcoin investors lost money (Bank for International Settlements study)
- Top causes: poor research (55%), FOMO (44%), day trading specifically (54% — leading cause for new traders)

**Crypto startups — worse odds than tech startups generally (already bad):**

- ~95% failure rate for crypto/blockchain startups specifically, the highest of any tech subsector checked (healthcare
  tech and ecommerce both ~80%)
- Stacks on top of general VC odds already in this doc (~0.05% of all startups get VC + succeed) — crypto + startup
  combines two of the worst-odds categories in business

**The real fortunes are mostly long-term holding, not trading or founding:**

- ~241,700 people globally hold $1M+ in crypto (+40% YoY), 450 hold $100M+, 36 are billionaires — out of 560 million
  total crypto users worldwide. That's ~0.04% of all participants.
- Absolute numbers are large because the total market ($3.3T) is enormous, not because individual odds are good.
- Best explained by early/long-term holding through a rising market (buy-and-hold years ago), not active trading or
  founding a company — and isn't really repeatable today the way it was in 2011-2017.

Conclusion: perception is grounded in real numbers (hundreds of thousands of real crypto millionaires exist), but
overstates the odds specifically for trading and for founding a crypto startup — both are currently
worse-than-their-non-crypto-equivalent bets. Reinforces the plan already in this doc: a boring, non-custodial B2B SaaS
tool sold *to* the crypto industry, not speculating *in* it.

## Crypto/blockchain field survey

Explored "all possible ways" into crypto/blockchain, filtered against the constraints above. Hard pattern that emerged:
**the moment a business model touches/holds user funds, it hits money-transmitter licensing** — $250K-$435K+ for all US
states, $10K-$1M+ per individual state, 6-18 months, ~$225K/yr to maintain. That alone rules out custodial wallets,
centralized exchanges, and crypto payment processors regardless of any other factor.

Ruled out (see Candidates section below for full detail on the first three):

- Token generator SaaS — saturated, free trusted competitors (55,000+ projects served by one alone)
- ICO/launchpad — personal SEC liability risk (Do Kwon precedent: $110M+ owed personally, on top of $3.586B company
  disgorgement)
- AMM/DEX (Uniswap/PancakeSwap-style) — $50-100k+ security audits, liquidity network effects near-impossible to
  bootstrap solo
- Custodial wallets / centralized exchanges / crypto payment processors — money-transmitter licensing wall above
- Stablecoins, cross-chain bridges, custodial staking-as-a-service — same licensing wall; bridges are additionally the
  most-hacked category in crypto history (Ronin $625M, Wormhole $325M)

**Priority queue — non-custodial, software-only crypto ideas, to research separately, one at a time:**

1. Smart contract security scanning tool — B2B SaaS sold to dev teams, scan code not funds. Real market exists (MythX,
   SolidityScan). Caveat: automated tools only catch 60-80% of known bug patterns, miss most of the
   business-logic/economic exploits that cause actual dollar losses — reputational risk if oversold as "an audit."
2. On-chain analytics dashboard for one narrow ecosystem — read-only, no custody. Needs real narrowness (a specific
   small chain/protocol) to avoid competing head-on with Dune/Nansen.
3. DAO governance/coordination tooling — B2B SaaS, mostly non-custodial (voting/coordination infra, not holding treasury
   funds directly).

Also flagged as the strongest candidate by market data (not yet in the queue above, worth remembering): **crypto tax
software** — $6.04B market in 2026, growing 19.8% CAGR to $12.33B by 2030, clean recurring-ish SaaS model (pay per tax
report by transaction volume), never touches custody since it just reads transaction data. Crowded (Koinly, CoinTracker,
TokenTax, ZenLedger, ~15+ others) but market growing fast enough it's not zero-sum — would need a wedge (underserved
country's tax rules, or a DeFi/chain ecosystem the big players handle badly).

#### Crypto tax software — competitor landscape (detailed, checked Aug 2026)

Note: myip.ms gave a wildly wrong traffic number for CoinTracker (<200 visitors/day) — it's an unreliable tool for any
site behind Cloudflare, since it infers traffic from shared IP ranges rather than real analytics. Numbers below use
SimilarWeb/Semrush traffic snapshots (mostly mid-late 2024, directional not exact) plus company funding data instead.

| Company                    | Scale signal                                  | Segment                              |
|----------------------------|-----------------------------------------------|--------------------------------------|
| Koinly                     | ~1.5-2M visits/mo                             | Consumer — traffic leader            |
| CoinTracker                | 3M+ users, $1.3B valuation, $102M+ raised     | Consumer — funding leader            |
| CoinLedger                 | ~600K visits/mo                               | Consumer — mid-tier                  |
| CryptoTaxCalculator        | ~280K visits/mo                               | Consumer — DeFi/on-chain strong      |
| CoinTracking (GmbH)        | 1.5M+ customers, 25K+ corporate               | Consumer — oldest platform           |
| ZenLedger                  | ~125K visits/mo                               | Consumer — smaller                   |
| TokenTax                   | below ZenLedger                               | Consumer — full-service/CPA angle    |
| KoinX                      | 1.5M+ users claimed, only ~$1.5M raised       | Consumer — numbers look inconsistent |
| Blockpit                   | acquired Accointing in 2024                   | Consumer — Europe-focused            |
| Coinpanda                  | 65+ countries, 800+ integrations              | Consumer — broad geo coverage        |
| TaxBit                     | $237M raised, $1.3-1.5B valuation, $25.2M ARR | Enterprise — leader                  |
| Bitwave                    | —                                             | Enterprise — self-described leader   |
| Ledgible (formerly Verady) | —                                             | Enterprise + accountant tools        |
| Cryptoworth                | smallest funding of enterprise group          | Enterprise — oldest (2017)           |
| NODE40                     | —                                             | Enterprise — smaller                 |

#### Crypto tax software — wedge analysis (checked Aug 2026)

**Geographic wedge — Brazil stands out.** Progressive capital gains (15%/17.5%/20%/22.5%) above R$35,000/month, mining/staking taxed up to 27.5%, monthly e-CAC reports for off-exchange volume over R$30,000, and brand new "DeCripto" reporting rules taking effect **July 1, 2026** for foreign-exchange/P2P transactions — a real, recent regulatory shift that US/UK/EU-first incumbents may not have caught up on yet. (India, by contrast, already has dedicated local players — Descrypt, Catax — so less open than it first looks.)

**Product wedge — DeFi transaction classification is a documented weak spot even for leaders.** Even top platforms inconsistently handle wallet-to-wallet cost-basis continuity (a transfer misread as a "new" deposit gets falsely taxed at zero cost basis) and complex DeFi positions — LP tokens, rebasing tokens, liquid staking derivatives, bridging. "Some platforms excel at exchange imports but fail on DeFi." A tool that supports only a handful of chains but classifies DeFi transactions *correctly* could beat broad-but-shallow incumbents there.

**Legal/licensing — better than expected.** Building tax *calculation* software requires no license at all — PTIN/state-preparer regulation (CA, MD, NY, OR, CT, NV, IL) only applies if you personally prepare/file returns *for* someone. Staying in the "generate a report the user or their own accountant files" lane (how Koinly/CoinTracker actually work) avoids licensing entirely. Skip direct IRS e-filing specifically — that requires passing IRS Modernized e-File Assurance Testing, a real compliance hurdle not worth taking on for an MVP.

**The real technical moat to respect — integration breadth.** Koinly's 800+ exchange/wallet integrations is the actual defensibility incumbents have built over years; a solo MVP can't match it and shouldn't try. Scope to a handful of exchanges/chains relevant to one specific niche (Brazil-specific exchanges, or one DeFi ecosystem) instead of "support everywhere."

**Where the technical edge actually helps**: DeFi transaction classification is inherently ambiguous ("is depositing into a liquidity pool a disposal event?") — a good fit for LLM-assisted classification via the Claude API, a real current advantage over incumbents whose classification logic predates LLMs.

**Risk that survives even without a licensing requirement**: shipping wrong tax numbers creates real user harm and reputational/civil liability. Needs the same "informational only, not tax advice, consult a professional" disclaimer every incumbent uses, and eventually E&O insurance if it gets real usage.

Status: wedge identified (Brazil-specific compliance, or narrow DeFi-classification specialist), not yet scoped into an MVP.

Takeaway for the wedge search: Koinly and CoinTracker dominate consumer traffic; TaxBit and CoinTracker dominate enterprise valuation. The mid-tier (CoinLedger, CryptoTaxCalculator, ZenLedger, KoinX, Blockpit, Coinpanda) is where smaller/regional/DeFi-specific players survive — consistent with the wedge above needing to be a specific underserved country's tax rules or a specific DeFi/chain ecosystem the big players handle badly, not a general-purpose competitor to Koinly/CoinTracker.

### On-chain analytics dashboard — wedge analysis (checked Aug 2026)

**Competitor landscape**: Six platforms dominate — Dune Analytics (community SQL-query dashboards, the default place "most on-chain analysis happens"), Nansen (500M+ labeled addresses, real-time smart-money alerts), Arkham Intelligence (broader entity coverage, AI identification engine "Ultra," plus an analyst intelligence marketplace), DeFiLlama (free, open-source, most extensive DeFi protocol/chain coverage, added natural-language querying via "LlamaAI" in 2026), Flipside Crypto, Footprint Analytics (no-query structured data), plus Token Terminal, Artemis, Allium, Glassnode.

**Critical structural problem, bigger than for any other candidate so far**: Dune's own business model shows exactly why a public-facing paid dashboard is hard to sell. [Dune gives away community dashboards for free (financially rewarding contributors to build them) and monetizes instead via Plus/Pro subscriptions ($400-1,000/month for private queries, exports, no watermark), a usage-based API, and enterprise/protocol-bounty deals — institutional subscriptions + API now make up ~65% of Dune's revenue](https://dune.com/blog/thoughts-on-dunes-business-model). In plain terms: **if you build a public dashboard for a niche chain, someone can just build the same thing for free on Dune and share the link** — the free-community-dashboard layer is a real, standing competitor to any "look at my dashboard" product, not just Dune-the-company.

**What that structural fact implies for the wedge**: the viable version of this idea isn't "public dashboard site," it's the same shape Dune itself monetizes — sell to **protocol teams or power users who need something bespoke**, not to casual public viewers. Two concrete angles:
- **Bespoke analytics-for-hire for small/new protocols** — mirrors Dune's own "protocol bounty" revenue line, but targeted at long-tail chains/protocols too small to attract Dune's bounty-funded analyst community's attention.
- **Depth on a specific gap named directly by the market**: [Glassnode is explicitly weaker on "fine-grained protocol-level data... or small-cap altcoins on niche chains"](https://crystalintelligence.com/explainers/best-blockchain-analytics-tools-in-2026/) — a real, sourced gap at the high end of the market. Separately, [most analytics tools are built for one use case (market analysis, DEX research, or compliance) and teams commonly hit "unresolved identity gaps and a backlog of custom integration work" when trying to stitch multiple tools together](https://blocsys.com/enterprise-blockchain-analytics-complete-guide-2026-3/) — a real B2B integration-pain point a narrow, well-integrated tool for one specific ecosystem could solve.

**Legal/risk profile**: the safest of everything explored in this field — purely read-only, public data, no custody. The one thing to watch: if the product frames itself as generating buy/sell "signals" (not just descriptive data), it drifts toward the same "not licensed investment advice" disclaimer territory as the finance-influencer-persona idea earlier in this doc. Staying descriptive (what happened) rather than prescriptive (what to do) avoids that.

**Fit check**: matches the technical edge well (read/query/visualize public data, no custody-related engineering complexity), but the realistic version is **B2B/bespoke, not a consumer SaaS dashboard people self-serve subscribe to** — closer in shape to freelance/contract work for specific protocol teams than to the recurring-revenue-product goal in the constraints section. Worth being honest about that mismatch before scoping further.

Status: wedge identified (bespoke long-tail-protocol analytics, or Glassnode's stated small-cap/niche-chain depth gap), but the business-model shape (B2B bespoke vs. self-serve product) needs resolving against the "recurring revenue, owned long-term" goal before this becomes an MVP.

### Smart contract security scanning tool — wedge analysis (checked Aug 2026)

**Competitor landscape — squeezed from both directions at once, which is the core problem:**

*Free/open-source below:* Slither (Trail of Bits, 92+ vulnerability detectors, CI-integrated), Mythril, Semgrep, Aderyn — all free, all mature, all already in the standard developer stack.

*VC-funded AI entrants above:* AuditAI ($20M round led by a16z, Feb 2026), Octane ($6.75M seed led by Archetype + Winklevoss Capital, with Gemini/Circle also participating — "continuously review on-chain code, one-click fixes"), Almanax ($1M pre-seed from Defy, "AuditLLM"), Veritas Protocol (custom model trained on 30,000+ contracts), Olympix (proprietary compiler + IR + symbolic execution engine; customers include Uniswap Labs, Li.Fi), QuillAudits (1,500+ audits completed).

*The cheap-SaaS slot is already occupied:* SolidityScan sells at $9.99/mo (Developer), $49.99/mo (Professional), automated audits from $30. ContractScan already runs five engines in parallel (Slither, Mythril, Semgrep, Aderyn, + AI).

This directly violates the heuristic at the top of this doc. Unlike the GitHub build-in-public idea (competitors = other indie builders = healthy signal), here the competitors are **free open-source tools below and a16z-funded startups above**, with the budget-SaaS tier already taken. There is no comfortable middle to occupy.

**The killer finding — the obvious solo approach is the one with documented terrible accuracy.** The natural build for this stack (Claude API + Solidity source = "AI security scanner") is exactly the approach academic benchmarks show performing badly:
- [GPT-4 found 32 of 73 vulnerabilities across 52 real DeFi attacks — but produced **740 false positives**, a precision of **4.15%**](https://arxiv.org/html/2605.11163v1).
- GPT-3.5 and GPT-4 reach only 19.7% and 22.6% precision on the 9 most common vulnerability categories.
- GPT-4 and Claude correctly identify the vulnerability type in ~40% of cases, but with false-positive rates high enough that the papers conclude manual auditors remain necessary.
- Root causes are structural, not prompt-fixable: hallucinated vulnerabilities, lexical bias (judging by identifier names rather than semantics), no execution context, inability to track cross-file call relationships.
- Mitigations exist but raise the build bar sharply: careful prompt engineering cuts false alarms 60%+, and **fine-tuning or combining the LLM with symbolic analysis** is what actually moves accuracy — i.e. the serious players (Olympix's custom compiler/IR/symbolic engine, Veritas's model trained on 30k contracts) are doing real compiler engineering, not prompting.

This matches the caveat already noted in the priority queue, but is worse than assumed: automated tools catch 60-80% of *known pattern* bugs, and the business-logic/economic exploits they miss cause 80%+ of actual dollar losses.

**Liability — the worst risk profile of the three crypto candidates.** Not a licensing problem (no license needed to sell a scanner), but a "you told me it was safe" problem. Standard practice is a disclaimer that the audit is not legally binding and guarantees nothing, and that it is a point-in-time assessment only — but the reputational reality is unforgiving: [Wormhole was audited and still lost $320M after an upgrade introduced unchecked edge cases](https://coin98.com/blog/what-a-smart-contract-audit-does-and-doesnt-cover/). A tool with 4% precision that green-lights a contract which then loses user funds is an extinction-level reputational event for a solo product, and the market knows it — the honest framing in the space is that free static analysis and AI review "include no professional accountability," which is precisely why they're free.

**Is there a real underserved segment?** Yes, but it's the hardest one to monetize. Audits run $1,000 (simple ERC-20) → $25,000-100,000 (typical DeFi protocol) → $150,000+ (multi-chain enterprise), plus $5,000-20,000 per remediation pass. That leaves genuinely underserved pre-funding founders — but their existing options are *free* static analysis, audit contests, bug bounties, or a time-boxed senior human session at $500-2,500. The segment that can't afford audits also can't afford much software, and the free tier is already good.

**Fit check — the weakest of the three crypto candidates.** Technical edge doesn't apply the way it does elsewhere: winning here requires compiler/symbolic-execution engineering (Olympix's moat), not Django + Claude API. The LLM angle that would be the natural advantage is the documented weak spot. Competitors violate the doc's own heuristic in both directions. And the liability profile punishes exactly the kind of imperfect-but-cheap product a solo builder would ship first.

Status: **recommend dropping**, or reframing entirely — the only defensible solo angle would be something adjacent that avoids making safety claims (e.g. a developer-workflow tool around existing free scanners rather than a scanner competing on detection quality). Ranked below both crypto tax software and on-chain analytics.

### DAO governance tooling — wedge analysis (checked Aug 2026)

**The category leader shut down five months ago. That is the whole analysis, but the details matter.**

[Tally — which powered more on-chain DAOs than any other platform — announced its shutdown on March 17, 2026, after six years](https://thedefiant.io/news/defi/tally-dao-governance-platform-shuts-down-38m3d2). It did not fail from lack of traction:
- 1M+ users
- $1B+ in payments processed
- helped secure $80B+ in protocol assets
- had already completed a 60-day US ICO registration process — then killed the token sale and wound down anyway

CEO Dennison Bertram's stated reasons are the important part: **demand for DAO governance tooling never grew enough to sustain a venture-backed company**, and easing US crypto regulation (Digital Asset Clarity Act, GENIUS Act, SEC-CFTC joint interpretation) made decentralization "optional." The uncomfortable conclusion drawn across the coverage: much DAO adoption was **regulatory camouflage** — projects adopting DAO structures defensively to avoid securities treatment — rather than genuine demand for decentralized coordination. When the regulatory pressure eased, the demand evaporated with it.

This is a category-level demand signal, not a competitive one. Every other candidate in this doc failed on "too many/too well-funded competitors." This one fails on **the customers themselves going away**.

**Surviving competitors, for completeness:** Snapshot (off-chain, gasless voting — processes 96%+ of major DAO votes, the de facto standard, free), Snapshot X (its newer on-chain protocol), Aragon OSx (most flexible, for teams with real dev capacity), Agora (acquired Boardroom in Jan 2025 and pivoted to institutional governance clients like Uniswap and Optimism), plus XDAO, Squads, DAO Lens. Four platforms cover ~90% of real-world use cases. Note the shape of the survivors: the dominant one is **free**, and the one that found revenue did so by **pivoting away from DAOs toward institutional clients**.

**Business model is the known-unsolved problem in this space.** The standard pattern is free core features plus enterprise services — and the reporting is blunt that "sustainable business models remain elusive for many providers." Tally is the proof: leading market position, $80B in assets secured, still not a viable business.

**The underlying user data is also weak.** ~10,000+ active DAOs and $25B+ in collective treasury sounds large, but engagement is poor and structurally so: average voter participation ~17% (top DAOs reach 28% on major proposals), turnout frequently below 10%, [the top 10% of token holders control 76.2% of voting power, and less than 1% of holders control ~90% of voting power in some analyses](https://lopetaku.medium.com/dao-governance-failures-whales-low-turnout-attacks-d1375c556384). Tooling that improves participation is solving a problem most DAOs have already revealed they don't care enough about to fix — and [research indicates DAOs keep centralizing regardless](https://www.forbes.com/sites/digital-assets/2026/04/04/daos-keep-centralizingdecades-of-governance-research-explain-why/).

**Fit check:** legally clean (non-custodial voting/coordination infra — the original reason it made the queue), and technically well within reach. But that's irrelevant when the market leader with 1M users just concluded the market doesn't support the business. There's no wedge to find in a category whose demand driver was regulatory and has been removed.

Status: **drop.** Ranked last of the four. Not a competition problem or an execution problem — a demand problem, evidenced by the category leader's own shutdown.

### Crypto candidate ranking (after all four analyses)

1. **Crypto tax software** — real growing market ($6.04B → $12.33B by 2030), clear paid-product norms, two concrete wedges (Brazil's DeCripto rules effective July 2026; DeFi-classification depth), no licensing requirement, and LLM classification is a genuine edge rather than a liability. **Best candidate.**
2. **On-chain analytics** — safest legally, but the free-community-dashboard layer undercuts any self-serve product; viable version is B2B/bespoke, which conflicts with the recurring-revenue goal.
3. **Smart contract security scanning** — squeezed between free open-source and a16z-funded startups; the natural LLM build has ~4% precision in benchmarks; worst liability profile.
4. **DAO governance tooling** — category demand collapsed; market leader shut down March 2026.

## Candidates

### GitHub commits → build-in-public content tool — ACTIVE CANDIDATE

Turns a solo dev's GitHub activity (commits/PRs/releases) into social posts / progress logs for X, LinkedIn, etc.

- Fits: uses GitHub (tool I already use daily), technical build, recurring subscription, I'd be my own first user.
- Competitive landscape: crowded, but with *other indie builders* — LaunchLogs, gittomarket, ShipToPost, Postgit,
  oidapost, poster.ly, Build in Public. All small SaaS tools, not funded startups.
- Open question: needs a differentiated angle (specific audience — e.g. open-source maintainers, a specific framework
  community — or a specific output format/platform the others don't nail) rather than competing head-on.
- Next step: pick the wedge/angle, then scope an MVP.

### Micro-SaaS / "narrow tool for users of a platform I already use" — pattern, not a specific idea yet

General strategy that fits the constraints well. Real proof points:

- Notionlytics — analytics tool for Notion users, $43,160 MRR, 75% margin, solo-built.
- PDF-to-Excel bank statement converter for accountants — $16K MRR, one narrow painful workflow.
- Pattern: "surgical instrument, not Swiss Army knife" — one recurring task, one specific user group, subscription
  pricing.

### AI persona / "AI content for influencers" — explored deeply, parked

Landed on: an AI-generated persona (sample built: "Ava Sterling", finance/money-tips niche) + later an AI agent to
handle brand outreach ("agency of one").

- Sample persona + 3 example Instagram carousel posts mocked
  up: https://claude.ai/code/artifact/231f0a23-7353-47ac-a0eb-0b8586f393e6
- Real precedent for AI personas: Aitana Lopez (~350k
  followers, $3-10k/mo, lifestyle/fitness/gaming), Lil Miquela (currently ~$70-96k/yr, much lower than peak-hype figures
  often quoted), Shudu Gram, Seren Ay, Olivia C.
- Real precedent for finance-content creators (human-run, not AI): @herfirst100k / Tori Dunlap (2.2M followers, company
  grossed $3.4M+ in 2021, ~$7M personal net worth — but this is a full media company built over 6+ years: courses,
  coaching, book, podcast, not just Instagram).
- Gap found: no one is running an *openly-AI* persona specifically in the finance niche — AI personas cluster in
  fashion/travel/lifestyle/gaming (visual/aesthetic niches), because finance content sells on personal credibility,
  which is harder for a disclosed-AI persona to establish.
- Legal note: finance-content angle must stay educational/informational (budgeting, saving, habits) — giving specific
  investment recommendations without being a registered investment adviser (RIA) is illegal in the US. Same category of
  risk as the Hindex issue below, just avoidable by staying descriptive rather than prescriptive.
- Status: parked while exploring other directions, not rejected.

### B2B "AI agent" categories (sales, customer support, recruiting, back-office ops) — REJECTED for now

Explored because of interest in VC fundability. Every function checked is dominated by heavily-funded players as of Aug
2026:

- Sales/outreach: 11x ($74M), Clay ($46M), Artisan ($12M), Monaco ($35M). Also: fully-autonomous AI SDRs haven't
  actually worked at scale — companies reverted to hybrid/human models.
- Customer support: Sierra ($950M), Parloa ($350M), Decagon ($250M), Netomi ($110M). 97% of 2026 capital in this
  category went to Series B+ — almost no seed-stage room.
- Recruiting/HR: less capital-concentrated but consolidating fast (Workday acquired Paradox/Olivia); some seed
  activity (Tezi $9M, Contrario).
- Back-office/ops: most total capital ($2.66B in 2026 YTD), but reward goes to *very* vertical-specific workflows (
  legal, healthcare claims, logistics) — not generic "ops automation."
- Conclusion: "AI agent" as a pitch is a big-money, later-stage category in every function right now — not matched to a
  self-funded solo budget. Confirmed the "competitors are giants" heuristic above.

### Beauty ecommerce — parked, unexplored

Legitimate, no legal issues. Stripe Checkout or Shopify. Open question never answered: new project or bolted onto
existing Django codebase. No further research done.

### Hindex real card payments — BLOCKED

Hindex is styled as an "HYIP index" (fixed daily/annual return investment). Accepting real card payments into that
structure risks looking like unregistered securities/Ponzi-scheme facilitation *unless* there's an actual licensed
entity behind it. Question of whether such an entity exists was never answered — this is a hard blocker, not a technical
problem (Stripe integration itself would be moderate effort).
