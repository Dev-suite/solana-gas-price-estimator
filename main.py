# main.py

from utils.quicknode import get_fee_estimate
import config

def main():
    fee_estimate_lamports = get_fee_estimate(config.QUICKNODE_URL)
    fee_estimate_sol = fee_estimate_lamports / 1_000_000_000  # Convert lamports to SOL
    print("Estimated Gas Price (in lamports per signature):", fee_estimate_lamports)
    print(f"Estimated Gas Price (in SOL per signature): {fee_estimate_sol:.8f}")

if __name__ == "__main__":
    main()
