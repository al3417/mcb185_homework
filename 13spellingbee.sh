cd ~/Code/MCB185/data

gunzip -c dictionary.gz | grep -E "^r+[zonica]{3,}$"
gunzip -c dictionary.gz | grep -E "^[zonica]+r+[zonica]{2,}$"
gunzip -c dictionary.gz | grep -E "^[zonica]{2,}r+[zonica]$"
gunzip -c dictionary.gz | grep -E "^[zonica]{3,}r+$"
gunzip -c dictionary.gz | grep -E "^r+[zonica]{2,}r+$"
gunzip -c dictionary.gz | grep -E "^r+[zonica]+r+[zonica]+$"
gunzip -c dictionary.gz | grep -E "^[zonica]+r+[zonica]+r+$"
gunzip -c dictionary.gz | grep -E "^r{2,}[zonica]{2,}$"
gunzip -c dictionary.gz | grep -E "^[zonica]{2,}r{2,}$"

