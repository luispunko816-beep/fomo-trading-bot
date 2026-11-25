
import json
import urllib.request

def analyze_coin(token):
    url = f"https://api.dexscreener.com/latest/dex/tokens/{token}"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())

        pairs = data.get("pairs", [])

        if not pairs:
            print("Kein Coin gefunden")
            return

        pair = max(
            pairs,
            key=lambda p: float(p.get("liquidity", {}).get("usd") or 0)
        )

        print("\n--- FOMO AI ANALYZER ---")
        print("Coin:", pair.get("baseToken", {}).get("name"))
        print("Preis:", pair.get("priceUsd"), "USD")
        print("Market Cap:", pair.get("marketCap"))
        print("Liquidität:", pair.get("liquidity", {}).get("usd"))
        print("24h Volumen:", pair.get("volume", {}).get("h24"))
        print("24h Veränderung:", pair.get("priceChange", {}).get("h24"), "%")

    except Exception as e:
        print("Fehler:", e)


token = input("Solana Token-Adresse: ")
analyze_coin(token)
