SMPL FRKS mint widget (self-hosted).

smpl-mint-widgets.js is the original custom element bundle (Thirdweb/React),
byte-identical to the Squarespace-era copy and to
https://smpl-frks-mint-btn.vercel.app/smpl-mint-widgets.js
sha256 560c047cd53138aa13a9921aaaef47b259ec0ffc2e0a7ce0aa57f0622748b9e9
Do not edit it. /smplfrks loads it only when the mint section is near the viewport.

Embed:
  <smpl-mint-button contract-address="0x409acDc2f42E12AB3AaC70D2a156aB55D31Df6Fe" chain-id="1">
  contract 0x409acDc2f42E12AB3AaC70D2a156aB55D31Df6Fe, Ethereum mainnet
  reads mintingEnabled(), totalSupply(), maxSupply()
  sends payable mint(address _to, uint256 quantity) to the connected wallet

The page restyles the widget only by adding a <style> to its open shadow root,
hides the widget's duplicate title/pitch/video (the page shows its own), and
removes the widget video's src so the 10.5 MB smpl.mov is not downloaded.
Hardcoded prices in the bundle matched the on-chain basePrice and tiers on
2026-11-14 (read-only check).
