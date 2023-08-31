#!/bin/bash

json_file="linkDatas.json"
rows=("01" "02" "03" "04" "05" "06" "07" "08" "09")
columns=("前1-" "前2-" "前3-" "前4-" "前5-" "后1-" "后2-")

for i in {10..35}; do
    rows+=("$i")
done

for ((c=0;c<6;c++))
do
	col1=$((c+3))
	col2=$((c+4))
	for ((r=0;r<35;r++))
	do
		
		#echo $col1","$col2
		#cat lottery.csv|awk -v c1="$col1" -v c2="$col2"  -v val="${rows[$r]}" -F ',' '{ if($c1==val) print $c2}'|sort|uniq -c|awk -F' ' '{print $1","$2}'

		cat lottery.csv|awk -v c1="$col1" -v c2="$col2"  -v val="${rows[$r]}" -F ',' '{ if($c1==val) print $c2}'|sort|uniq -c|awk -F' ' '{print $1","$2}' | while IFS=',' read -r -a line
		do
    		# for ((i=0; i<${#line[@]}; i++))
    		# do
      	 	# 	echo "Value at index $i: ${line[$i]}"
    		# done
    		echo "{\"source\":" "\""${columns[$c]}${rows[$r]}"\", \"target\": \""${columns[$c+1]}${line[1]}"\", \"value\":"${line[0]}"}," >>$json_file
		done
	done
done

# csv_file="lottery.csv"

# char_to_int() {
#   local char=$1
#   local num=0

#   case "$char" in
#     "01") num=1 ;;
#     "02") num=2 ;;
#     "03") num=3 ;;
#     "04") num=4 ;;
#     "05") num=5 ;;
#     "06") num=6 ;;
#     "07") num=7 ;;
#     "08") num=8 ;;
#     "09") num=9 ;;
# 	"10") num=10 ;;
#     "11") num=11 ;;
#     "12") num=12;;
#     "13") num=13 ;;
#     "14") num=14;;
#     "15") num=15 ;;
#     "16") num=16 ;;
#     "17") num=17 ;;
#     "18") num=18;;
# 	"19") num=19;;
#     "20") num=20 ;;
#     "21") num=21 ;;
#     "22") num=22;;
#     "23") num=23 ;;
#     "24") num=24 ;;
#     "25") num=25 ;;
#     "26") num=26 ;;
#     "27") num=27 ;;
# 	"28") num=28 ;;
#     "29") num=29 ;;
#     "30") num=30 ;;
#     "31") num=31 ;;
#     "32") num=32;;
#     "33") num=33;;
#     "34") num=34 ;;
#     "35") num=35 ;;
#        *) num=-1 ;;  
#   esac

#   echo $num
# }

# columns=("前1" "前2" "前3" "前4" "前5" "后1" "后2")
# rows=("01" "02" "03" "04" "05" "06" "07" "08" "09")

# for i in {10..35}; do
#     rows+=("$i")
# done
# for ((c=0;c<1;c++))
# do
# 	declare -A my_array
# 	while IFS=',' read -r -a line
# 	do
#     	# Access each value in the line using array index
#     	# for ((i=0; i<${#line[@]}; i++))
#     	# do
#       	# 	echo "Value at index $i: ${line[$i]}"
#     	# done
#     	# echo ${line[$c+2]},${line[$c+3]}
#     	lr=$(char_to_int ${line[$c+2]})
#     	lc=$(char_to_int ${line[$c+3]})
#     	#echo $lr $lc
#     	((my_array[$lr,$lc]++))
#     	echo  $lr,$lc, ${my_array[$lr,$lc]}
# 	done < $csv_file
# 	echo my_array
# done


