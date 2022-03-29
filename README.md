# Blockchains Transactions Viewer
This project provides a visualized tool to view historical transactions on blockchain. The chart currently contains data from four blockchains, which are Bitcoin, Ethereum, Polygon, and Tezos. Users can choose which data to be shown on the chart by clicking the buttons below the plot.

## Usage
```
git clone https://github.com/jiyuntu/Blockchain-transactions.git
cd Blockchain-transactinos
echo "Date(UTC),Value" > tezos.csv
python3 plot.py
open index.html
```