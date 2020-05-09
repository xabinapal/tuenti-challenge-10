#!/usr/bin/env sh

curl --silent -H "Host: pre.steam-origin.contest.tuenti.net" steam-origin.contest.tuenti.net:9876/games/cat_fight/get_key | jq -r .key