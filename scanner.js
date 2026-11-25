
async function scanCoins() {
  const result = document.getElementById("result");
  result.innerHTML = "Scanning Solana coins...";

  try {
    const response = await fetch(
      "https://api.dexscreener.com/token-boosts/latest/v1"
    );

    const coins = await response.json();

    const solanaCoins = coins
      .filter(coin => coin.chainId === "solana")
      .slice(0, 10);

    result.innerHTML = solanaCoins.map(coin => `
      <div style="padding:12px;border-bottom:1px solid #444">
        <b>${coin.tokenAddress}</b><br>
        <a href="https://dexscreener.com/solana/${coin.tokenAddress}" target="_blank">
          View on DexScreener
        </a>
      </div>
    `).join("");
  } catch (error) {
    result.innerText = "Scanner error";
  }
}
