cd ~/Code/MCB185/data

gunzip -c dictionary.gz | grep -E "^r+[zonica]{3,}$"
gunzip -c dictionary.gz | grep -E "^[zonica]+r+[zonica]{2,}$"
gunzip -c dictionary.gz | grep -E "^[zonica]{3,}r+$"
