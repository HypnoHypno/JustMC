## Affection
Like other After Story mods, Just MC uses an affection system.

It's a value which represents how much MC likes the player. It, combined with the mood system, sanity, and trust, will dictate MC's dialog. For instance, if you do something bad to MC at the highest level of affection, he will be a lot more forgiving to you than if he was at the lowest level of affection.

Affection on it's own will also dictate what types of interactions you can do with MC. For instance, more questions are unlocked over time as affection increases.

There will also be a daily cap of 8 affection per day, which will not increase at any point.

At the start of the game, the player will have 0 affection.

Here are the affection levels:

- Loving: 550 and above (1.75*) (37.5 Days from Friendly) (2 Months from Neutral)

- Friendly: 250 to 549 (1.5*) (18.75 Days from Warm) (1 Month from Neutral)

- Warm: 100 to 249 (1.25*) (8.875 Days from Neutral)

- Neutral: -29 to 99 (1.00*) (8.75 Days from Cold) (1 month from Antagonistic)

- Cold: -99 to -30 (0.75*) (18.75 Days from Hostile)

- Hostile: -249 to -100 (0.5*) (12.625 Days from Antagonistic)

- Antagonistic: -350 to -250 (0.25*)

The numbers in parenthesis are the affection multiplier, and how much time it'd take to get to this level of affection respectively, assuming you're playing perfectly and are at the lowest affection value of the level stated.

### Affection Gain
Using jm_add_affection(affection) will add a certain amount of affection, however it will be multiplied by the affection multiplier, to make it so that if MC already likes you, you have to put in less work to keep things on good terms, but if he hates you, you need to put a lot more work in.

For instance, an interaction which would gain you 4 affection on a 1* multiplier will give you 1 point on Ruined affection.

And on Hopeful affection, you'll gain 7 affection points using that same interaction.

Any value that would give you more affection than the daily cap will give you enough to equal the daily cap, assuming that "bypass" isn't set to True in jm_add_affection.

### Affection Loss
Using jm_remove_affection(affection) will remove a percentage of total perfection. For example, jm_remove_affection(5) will remove 27.5 affection if you have 550 affection, as it will remove 5% of your affection.

If your affection is less than 100, the percentage will be calculated assuming you have exactly 100 affection, meaning you will lose 5 affection given the above example.
