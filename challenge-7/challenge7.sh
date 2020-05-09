#!/usr/bin/env sh

# https://www.youtube.com/watch?v=P_1N6_O254g
# Dvořák: Symphony No. 9 "From the New World" / Karajan · Berliner Philharmoniker

QWERTY="-=qwertyuiop[]asdfghjkl;'zxcvbnm,./_+QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?"
DVORAK="[]',.pyfgcrl/=aoeuidhtns-;qjkxbmwvz{}\"<>PYFGCRL?+AOEUIDHTNS_:QJKXBMWVZ"

i=0
IFS=''
while read line
do
  if [[ ${i} -gt 0 ]]; then
    echo "Case #${i}: $(echo "$line" | tr -- "${DVORAK}" "${QWERTY}")"
  fi
  i=$((i+1))
done < "${1:-/dev/stdin}"