
cd ~/Code/MCB185/data

gunzip -c dictionary.gz | grep 'r' | grep -v '[bdefghjklmpqstuvwxy]'| grep -E '.{4,}'

