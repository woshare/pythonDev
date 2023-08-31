#!/bin/bash
json_file="nodesName.json"

columns=("前1" "前2" "前3" "前4" "前5" "后1" "后2")
rows=("01" "02" "03" "04" "05" "06" "07" "08" "09")
for i in {10..35}; do
    rows+=("$i")
done
echo "[" >> $json_file
for column in "${columns[@]}"; do
    for row in "${rows[@]}"; do
        id="${column}-${row}"
        echo "  {\"id\":\"$id\"}," >> $json_file
    done
done
echo "]" >> $json_file

echo "JSON文件生成完毕！"
