#!/bin/bash
path=""
declare -A sizes
while read -r line; do
  if [[ $line = "$ ls" ]]; then
    sizes[$path]=0
    while read -r dirline; do
      if [[ ${dirline:0:1} == "$" ]]; then
        line="$dirline"
        break
      fi
      if [[ "${dirline:0:3}" == "dir" ]]; then
        continue
      fi 
      size=`echo "$dirline" | cut -f1 -d' '`
      for dir in "${!sizes[@]}"
      do
        if [[ $path == $dir ]] || [[ ${path:0:${#dir}} == ${dir} ]]; then
          sizes["$dir"]=$((sizes["$dir"] + $size))
        fi
      done
    done
  fi
  if [[ $line =~ "\$ cd" ]]; then
    dir=${line:5}
    if [[ $dir == ".." ]]; then
       path=$(dirname "$path")
    else
       path="${path%/}/${dir%/}"
    fi
  fi
done
need=$((${sizes["/"]} - 40000000))
rm tmp
for i in "${!sizes[@]}"
do
  if [[ ${sizes[$i]} -ge $need ]]; then
    echo ${sizes[$i]} $i >> tmp
  fi
done
sort -n tmp | head -n 1
