# Challenge 4 - My Favorite Video Game

You're looking at your favorite video game website and you see some news that stops your heart. "The video game platform steam-origin is releasing `Cat Fight` next week". This has been your favorite game since childhood. You've got to have it. You continue reading the article and you see that there will be a free limited edition for the first hundred users who request the key. Oops, this is a big problem. You don't have a high-speed internet connection so there's no way you can be one of the first hundred users.

You're sad and you decide it's time to have dinner. You'll never be able to play `Cat Fight`. You turn on the TV and...

![steam-origin-security-problem.png](../assets/challenge-4/steam-origin-security-problem.png)

What? Does Steam-Origin have security problems? This is your chance. You're sure you can find a bug and get a key ahead of time. It's time to investigate. First of all, check the domain of the steam-origin API:

```
steam-origin.contest.tuenti.net:9876
```

The next step is to get the key for a free to play game and then try to get the key for `Cat Fight`. On the browser console debugger you can see the rest API is:

```
[GET] /games/<video_game_id>/get_key
```

The videogame_id is always the video game name with underscores instead of white space. We'll create a proof of concept using a video game where we know we can get the key - `Free Shoot` - and then we'll try with `Cat Fight`:

```
$ curl steam-origin.contest.tuenti.net:9876/games/free_shoot/get_key
{
  "game": "Free Shoot",
  "key": "9999-9999-9999"
}
$ curl steam-origin.contest.tuenti.net:9876/games/cat_fight/get_key
{
  "error": "Not available yet"
}
```

Wow... You're almost there. You keep looking around steam-origin engineering systems and you found gold.

[https://prezi.com/embed/vyi9c9pbl_42/](https://prezi.com/embed/vyi9c9pbl_42/)

## Server response:

The server response will be 200 HTTP response with a valid JSON. Example:

```
{
   "game": "Cat fight",
   "key": "XXXX-XXXX-XXXX"
}
```

## Result:

* Upload only the video game key.
* Don't upload the JSON response.
* The key is like `XXXX-XXXX-XXXX` where **X** is a digit

That's all folks