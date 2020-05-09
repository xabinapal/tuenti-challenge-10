# Challenge 9 - Just Another Day on Battlestar Galactica

Humanity is in danger again. A horde of cylons is trying to capture Battlestar Galactica in order to finish off the last humans. *"It's just another day for me"*, says Adama. But, wait! Today is not just another day on Galactica. *Today we will fight!*.

We know that the cylons need to get some resources (some kind of radioactive isotope) for their batteries to work (they have a low battery warning in their internal processor). If we knew where these resources were stored, we could blow them up and possibly gain an advantage in the war, or even win it.

We don't know where the planet with the resources is, but we have some information that might give us its location. A year ago, Galactica engineers received the following ciphered message:

```
3633363A33353B393038383C363236333635313A353336
```

A few days later, the cylons horde landed on a lonely planet with a lot of the radioactive isotopes they need. Captain Apollo risked his life to get the coordinates of the planet, which are:

```
514;248;980;347;145;332
```

We're not 100% sure, but we think the ciphered message contains the real coordinates of the planet... And guess what! We've just captured another ciphered message.This time, the message is:

```
3A3A333A333137393D39313C3C3634333431353A37363D
```

If the information is right, the new message would tell us where to find the next planet that has the resources the cylons need. We could then go there and destroy the resources before the cylons arrive.

We don't know how to decode the message. But... Good news for humanity! We've captured a cylon communications system. After a lot of effort, we realized that the encrypt/decrypt routines were hardcoded in the firmware. We extracted some code just before the auto-memory-erase method removed all the information from the communications system. This is the code we found:

```
chr() {
    printf \\$(printf '%03o' $1)
}

function hex() {
    printf '%02X\n' $1
}

function encrypt() {
    key=$1
    msg=$2
    crpt_msg=""
    for ((i=0; i<${#msg}; i++)); do
        c=${msg:$i:1}
        asc_chr=$(echo -ne "$c" | od -An -tuC)
        key_pos=$((${#key} - 1 - ${i}))
        key_char=${key:$key_pos:1}
        crpt_chr=$(( $asc_chr ^ ${key_char} ))
        hx_crpt_chr=$(hex $crpt_chr)
        crpt_msg=${crpt_msg}${hx_crpt_chr}
    done
    echo $crpt_msg
}
```

We don't know if this would help. But we hope you can give us the coordinates of the next planet so we can blow up the radioactive isotope the cylons need.
We believe in you. Please, can you help us?

## Extra information:

Coordinates in the universe have 6 components with this format: `xxx;yyy;zzz;aaa;bbb;ccc`
where `x, y, z, a, b, c` are digits (from 0 to 9). For example, this is a valid coordinate: `433;657;876;313;563;789`
Therefore, a coordinate always has 23 characters: 18 digits and 5 `;`.

## Limits

Coordinates format: `xxx;yyy;zzz;aaa;bbb;ccc` (coordinates have exactly 23 characters)

## Input

None

## Output

The coordinates in the specified format