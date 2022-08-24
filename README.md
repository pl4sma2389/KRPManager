# KRPManager

## Introduction
KRPManager is an AcTools Content Manager and/or GPL GEM-style mod installer, manager, and editor for Kart Racing Pro.

## Motivation - Standard
While Kart Racing Pro is (and was designed as) an end-user modifiable karting simulator, it does not have built-in mod management capability. 
Mods are installed by placing game-readable files (or optionally-encrypted ".pkz" files, which are just extension-swapped .zip files) in a predetermined folder structure inside the User/Documents/PiBoSo/Kart Racing Pro/Mods directory. This has proved confusing for new or less tech-savvy users, leading to confusion about normal mod installation procedures.
Additionally, users of Kart Racing Pro may need to update or uninstall mods, and with mod components being scattered in many places, this can leave some mod files orphaned if the user does not know how the Kart Racing Pro modification system works.

## Motivation - Actual
In practice, a user could just use JSGME or OvGME to do mod management if they want to, but these mod managers are overly generalized to work with nearly every game with or without a modding framework, as long as the game's data files are open and modifiable. This means that the user, to set up a mod to be managed by one of these mod managers, needs to have good knowledge of how Kart Racing Pro's modification system works, such as the file structure of a kart mod.
This tool could also be expanded to provide a more friendly GUI for changing user, video, and control settings, as well as creating single- and multi-player sessions, in the style of GPL GEM.

## Intended Base Functionality

### Existing Mods
 - [ ] Scan for installed mods and load them into a database
 - [ ] Allow users to uninstall loaded mods
 - [ ] Allow users to deactivate loaded mods, hiding them from the game but allowing them to be re-installed later

### New Mods
 - [] Allow the user to select a .zip or .pkz file containing a mod, and autodetect information about the type of mod (track, kart package (bodywork, chassis, engine, intake, seat, tyre), skin) if possible, and either detect the name of the mod, if possible, and/or allow the user to set the name of the mod
 - [] Allow the user to "update" existing mods by auto-detecting an older version of a mod and uninstalling it before installing the new version

## Settings Management
 - [] Scan the user's profiles folder and contained files for settings, and provide a friendly GUI for the user to edit and save profile parameters

## Extended Functionality

 - [] Enable "autoupdate" functionality by connecting to a "server", GitHub repository, or other data source, and check local mod versions against the latest mod versions; if a newer version is available, ask the user to update manually or, if possible, automatically download the latest version, extract, and update the mod