Hello

This github is dedicated to the mod upgrade station on Age of empire 02
This is a script you have to execute to add the triggers into your scenario
Version 0-3

- Fix the issue where chinese civ had infinite upgrade and tickets because of their civ bonus.
- Added the holy potion of steroid to buff units stat
- Change LOS bonus to area of damage for cavalry
- Added description for rams into te siege techs


Version 0-2

- Added the demonic technologie, available at town-center, playe rcan research it, they get a great bonus at the cost of fighting a boss or loosing a type of unit
- Each demon tech are available during a specific age...
- Added reward after killing a x number of units, player either get resource of tickets to exchange for resource
- Fix, rams getting more projectile
- Fix, ram getting ranged attack from tech


Version 0.1

- First version of the mod
- The wonder is now an upgrade station, each ugrade can be done 3 times
- with the upgrade station, you can upgrade: economy, infantry, cavalry, archery and siege
- Player 8 is not included in this mod because, this is for the gamemode 7 VS 1

How to use :
You have to download both file from this github
You need pycharm or any way to make a python environement on your machine
Have a AOE2 scenario 

On the main script Upgrade station.py line 74 and 75, you will find the two variables input and output path

Change the path folder to your scenario so the python script edit it.

BE WARNED ! This current version has "no way" to remove the trigger, every time you execute the script every trigger between start pluging and end pluging are removed (both header included) and replaced

You can modify stats and tech effect in the Upgrade_station_dictionnary.py

but do not touch the unused resource you will break the mod...

You are completely free to use this code and modify for your own need, just credit me, it's not much but it's help ;)
