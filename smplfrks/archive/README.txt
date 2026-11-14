Archived SMPL FRKS mint bundle. Not loaded by the site.

smpl-mint-widgets.js is the recovered custom element bundle (Thirdweb/React).
The review page does not reference it. Do not add a script tag for this file.
Wallet connection, signatures, and transactions stay off until the contract
and widget are checked read-only and explicitly approved.

Recovered embed:
  contract-address 0x409acDc2f42E12AB3AaC70D2a156aB55D31Df6Fe
  chain-id 1 (Ethereum mainnet)
  reads mintingEnabled(), totalSupply(), maxSupply()
  sends payable mint(address _to, uint256 quantity)

Hardcoded prices in the bundle matched the on-chain basePrice and tiers on 2026-11-14 (read-only check).
The page's mint animation (media/mint-loop.mp4) is a silent 480px re-encode of
the public animation https://smpl-frks-mint-btn.vercel.app/smpl.mov.
It plays muted. It does not connect a wallet.

sha256 smpl-mint-widgets.js: 560c047cd53138aa13a9921aaaef47b259ec0ffc2e0a7ce0aa57f0622748b9e9
(identical to the copy still hosted at smpl-frks-mint-btn.vercel.app as of 2026-11-14).
