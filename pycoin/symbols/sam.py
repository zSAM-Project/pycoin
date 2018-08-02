
from pycoin.networks.bitcoinish import create_bitcoinish_network

network = create_bitcoinish_network(
    netcode="SAM", network_name="STAMP", subnet_name="mainnet",
    wif_prefix_hex="bf", address_prefix_hex="3f", pay_to_script_prefix_hex="8b",
    bip32_prv_prefix_hex="0221312b", bip32_pub_prefix_hex="022d2533")
