from web3 import Web3

# Connect to Ethereum node (Infura, Alchemy, or your own)
node_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(node_url))

if web3.isConnected():
    # Get the latest base fee per gas from the latest block (EIP-1559)
    latest_block = web3.eth.get_block('latest')
    base_fee = latest_block.get('baseFeePerGas', None)
    print(f"Base fee per gas: {web3.fromWei(base_fee, 'gwei')} Gwei")

    # Set a priority fee (miner tip), e.g., 2 Gwei
    priority_fee = web3.toWei(2, 'gwei')
    print(f"Priority fee: {web3.fromWei(priority_fee, 'gwei')} Gwei")

    # Total max fee per gas = base fee + priority fee
    max_fee = base_fee + priority_fee
    print(f"Max fee per gas: {web3.fromWei(max_fee, 'gwei')} Gwei")

    # Estimate gas limit for a simple ETH transfer
    tx = {
        'to': '0xReceiverAddress',
        'from': '0xYourAddress',
        'value': web3.toWei(0.01, 'ether'),
    }
    gas_limit = web3.eth.estimate_gas(tx)
    print(f"Estimated gas limit: {gas_limit}")

    # Calculate approximate gas cost in ETH
    gas_cost = max_fee * gas_limit
    print(f"Approximate gas cost: {web3.fromWei(gas_cost, 'ether')} ETH")

else:
    print("Failed to connect to Ethereum node")
