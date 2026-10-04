# Side curiosities

Tangents that came up while researching business ideas — interesting, but not directly business-planning relevant. See research.md for the actual idea evaluation.

## Who owns the most Bitcoin?
No single "winner" — splits across a few very different categories, and the picture has shifted a lot in the last two years.

- **Satoshi Nakamoto**: ~968,000-1.1 million BTC, spread across ~20,000 addresses, untouched since 2010 (~$90-100B+ at current prices). Nobody knows if the keys are even still accessible.
- **Wall Street, via ETFs — now the single largest aggregate holder category**: the 12 US spot Bitcoin ETFs collectively hold ~1.29 million BTC (~$93B) — more than Satoshi. BlackRock's IBIT alone holds ~785,000 BTC. Notable irony: Bitcoin was designed to route around institutions like BlackRock, and as of 2026 BlackRock's single fund outweighs the pseudonymous founder.
- **Exchanges** (custodial, holding client funds, not really "theirs"): Coinbase ~885k-981k BTC, Binance ~675k BTC, Fidelity custody ~426k BTC.
- **Corporate treasury**: Strategy (formerly MicroStrategy, Michael Saylor's company) — 713,502 BTC, a deliberate all-in corporate bet.
- **Governments**: US holds ~324k BTC, mostly from asset seizures — formalized into a "Strategic Bitcoin Reserve" by executive order in March 2025 rather than being auctioned off.
- **Concentration**: top 1% of Bitcoin holders control 87% of all Bitcoin. Only 94 wallets hold more than 10,000 BTC each; just 4 wallets hold more than 100,000 BTC each. On the other end, only ~950,000 wallet addresses hold even 1 whole BTC — owning a single Bitcoin puts you in the top 0.1% of all holders worldwide.

Sources: [CryptoSlate](https://cryptoslate.com/guides/who-owns-the-most-bitcoin/), [TipRanks](https://www.tipranks.com/news/exchange-traded-funds-now-hold-more-bitcoin-btc-than-satoshi-nakamoto), [Bitcoin ownership concentration](https://www.quantumrun.com/consulting/bitcoin-ownership-statistics/)

## Is crypto really "financial democracy" / "financial freedom" for the people?
A genuinely mixed picture — more nuanced than the ownership question above, because part of the claim holds up and part doesn't.

**Where it's real:**
- Stablecoins as a dollar-substitute in high-inflation economies: Argentina (30%+ inflation) had $34 billion in stablecoin transactions in 2024 and the highest crypto adoption rate in the Western Hemisphere.
- Cheaper remittances: sending $200 through traditional channels costs ~6.9% on average — crypto rails can undercut that meaningfully.
- Dollar access without a US bank account: over 40% of all crypto transaction volume in Africa is now stablecoins; stablecoin supply grew from $6.8B (2020) to $273B (2026).
- These are real, measurable, and match the "financial freedom" framing — for specific populations (high-inflation economies, the unbanked, remittance senders).

**Where it doesn't hold up:**
- The "democracy"/equality claim is directly contradicted by the ownership concentration data above (top 1% control 87% of Bitcoin). Academic research: ownership concentration among "whales" suggests crypto is "insufficiently different from traditional forms of capital" — the opposite of the egalitarian rhetoric.
- "Institutionalization" has arguably reversed the founding cypherpunk ideology — crypto was meant to route around institutions like Wall Street banks, yet BlackRock's single Bitcoin ETF now holds more BTC than Satoshi Nakamoto.
- Roosevelt Institute critique: "crypto — or any private, profit-driven enterprise — is never going to solve the entrenched problems of income or wealth inequality... in fact, it exacerbates these problems." Many projects are built around price speculation rather than user empowerment — matches the "97% of traders lose money" data in research.md.
- UNCTAD warning: heavy crypto/stablecoin adoption in developing countries can undermine a country's ability to manage its own monetary policy — a real downside the "freedom" framing skips over.

Honest synthesis: the *specific, narrow* financial-freedom use cases (inflation hedge, remittances, unbanked dollar access) are real and well-documented. The *broader* "crypto = democratized, equal-opportunity finance for everyone" framing is not supported by the ownership/concentration data — the space is trending toward more institutional capture, not less.

Sources: [Brookings — stablecoins in the Global South](https://www.brookings.edu/articles/stablecoins-can-transform-the-global-south-by-reimagining-digital-finance-trade-and-development/), [Oxford Journal — decentralization dilemma](https://www.oxjournal.org/the-decentralisation-dilemma/), [Roosevelt Institute](https://rooseveltinstitute.org/blog/cryptos-false-promises-and-what-true-financial-inclusion-looks-like/)

## How was Bitcoin actually designed to route around institutions like BlackRock?
Bitcoin's founding document is literally titled ["Bitcoin: A Peer-to-Peer Electronic Cash System"](https://bitcoin.org/bitcoin.pdf) (Satoshi Nakamoto, 2008) — the explicit goal in the opening line is a payment system that lets two people transact "without the need for a trusted third party." Before Bitcoin, sending digital money always required an intermediary (a bank, PayPal, a card network) to verify you weren't spending the same money twice (the "double-spend problem"). Bitcoin's actual invention (blockchain + proof-of-work) solves that *without* a central authority — thousands of independent computers verify transactions collectively instead of one trusted institution doing it.

Design choices that embody "no institution needed":
- **Self-custody** — you hold your own private keys, so no bank/custodian can freeze, seize, or lose your money on your behalf. "Be your own bank."
- **Permissionless** — anyone can use it without approval, a credit check, or KYC from a gatekeeper.
- **Fixed, algorithmic monetary policy** — a hard 21 million coin cap, written into the protocol. No central bank or committee can vote to print more, unlike fiat currencies.
- **Censorship resistance** — no central party can block or reverse a transaction, unlike a bank that can freeze an account.

Historical detail: the first Bitcoin block ever mined (Jan 3, 2009) has a text string embedded in it — *"The Times 03/Jan/2009 Chancellor on brink of second bailout for banks"* — a headline about the UK government bailing out banks during the 2008 financial crisis. Widely read as Satoshi's deliberate commentary: Bitcoin was a response to a financial system where trusted institutions had just needed public bailouts to survive.

**Why BlackRock is the pointed contrast**: BlackRock is the largest asset manager in the world — the quintessential centralized, regulated financial institution. Someone who buys BlackRock's IBIT ETF instead of Bitcoin directly holds no private keys — they own a share in a fund, and BlackRock's custodian (Coinbase Custody) holds the actual Bitcoin *for* them. That reintroduces exactly the "trusted third party" Bitcoin's design was built to make optional — custodial risk, institutional control, reliance on a regulated intermediary. So the ETF wrapper being the largest Bitcoin-holding category today is a real structural irony: most people's exposure to "the currency designed to not need banks" now flows through a bank-like institutional structure anyway.
