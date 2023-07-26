#!/bin/zsh
while : ; do
  echo  -n "请输入 1 到 5 之间的数字："
  read aNum
  case $aNum in
  1|2|3|4|5) echo "你数据的数字为 $aNum!"
    ;;
  *)echo "你输入的数字不是1到5之间的！"

    echo "游戏结束"
    break
    ;;
  esac

    
done