# Affection
Like other After Story mods, Just MC uses an affection system.

It's a value which represents how much MC likes the player. It, combined with the mood system, sanity, and trust, will dictate MC's dialog. For instance, if you do something bad to MC at the highest level of affection, he will be a lot more forgiving to you than if he was at the lowest level of affection.

Affection on it's own will also dictate what types of interactions you can do with MC. For instance, more questions are unlocked over time as affection increases.

There will also be a daily cap of 8 affection per day, which will not increase at any point. The maximum value that affection can be will be 10,000.

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

## Affection Gain
Using jm_add_affection(affection) will add a certain amount of affection, however it will be multiplied by the affection multiplier, to make it so that if MC already likes you, you have to put in less work to keep things on good terms, but if he hates you, you need to put a lot more work in.

For instance, an interaction which would gain you 4 affection on a 1* multiplier will give you 1 point on Ruined affection.

And on Hopeful affection, you'll gain 7 affection points using that same interaction.

Any value that would give you more affection than the daily cap will give you enough to equal the daily cap, assuming that "bypass" isn't set to True in jm_add_affection.

## Affection Loss
Using jm_remove_affection(affection) will remove a percentage of total perfection. For example, jm_remove_affection(5) will remove 27.5 affection if you have 550 affection, as it will remove 5% of your affection.

If your affection is less than 100, the percentage will be calculated assuming you have exactly 100 affection, meaning you will lose 5 affection given the above example.

## Affection Writing Guide
The following is a list of all affection levels and how MC should refer to the player when in said affection level.

Refer to this when writing dialog for MC.

### Neutral
This is MC at his base state. When writing Neutral dialog, don't do any tricks. Try to stick to canon as much as possible.

MC is a bit uneasy due to his epiphany, but isn't particularly swayed to feel much emotion, and is slightly excited about the fact that he can now control the world, but not much.

When the player does things to make MC happy, there will be dialog of him being thankful, but he'll be a bit hesitant, somewhat awkward, and he'll keep it short.

### Cold
MC isn't particularly happy with the player due to their actions towards him, assuming that MC is in a neutral or positive mood, but he doesn't quite hate the player yet.

MC should be colder towards the player, occasionally making jokes at their expense which are on the line between teasing and insulting. (The line will be even more blurred when MC is in a positive mood.)

He'll be a bit more to the point, but not too much so.

When at this affection level, there will be a 1 in 12 chance of him immediately closing the game on you when you try to open it.

### Hostile
Even when MC isn't in a negative mood, contempt is starting to show.

When in a neutral mood, MC shouldn't joke at all unless the player is at the butt of the joke.

However, the above isn't true when MC is in a happy mood. Though he will never compliment the player, and will instead use his happiness as a "gotcha" against the player.

When at this affection level, there will be a 1 in 6 chance of him immediately closing the game on you when you try to open it.

### Antagonistic
MC will refuse to talk to the player in general, he hates the player as much as he humanly can.

He will intentionally steer any conversation towards insulting the player and talking about their mistreatment, and at low sanity levels, MC will have dedicated dialogs where he talks about ways that he wants to kill the player.

He will never tell jokes to the player at this level of affection, unless the jokes are specifically insulting to the player.

When at this affection level, there will be a 1 in 3 chance of him immediately closing the game on you when you try to open it.