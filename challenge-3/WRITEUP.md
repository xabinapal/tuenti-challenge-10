# Write-up 3 - Fortunata and Jacinta

This challenge has no complexity at all (even though I f***** it up and it submitted the wrong answer...). The given file has to be read one character at a time and parsed with the specified rules. There is only edge case that is not specified in the rules: when two words with the same frequency, and the characters in the shortest one are the same starting characters of the largest one, they must be ordered as ```shortest, largest```. For example, `trocar` and `trocara` have the same frequency, so, `trocar` comes before `trocara`.