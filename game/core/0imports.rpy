
# 0imports.rpy
# This file imports certain python modules at runtime for DDLC and template
# features.

python early:
    # For DSR/DSP, Effects
    import math 

    # For Credits
    import datetime

    # For Glitchtext
    import random

    # For Splash
    import re
    import os

    # For BSOD
    import subprocess
    import platform

    import datetime
    from datetime import datetime, timedelta
    import pyautogui
    import pymsgbox
    import pypresence

init -1 python:
    # Achievements/Gallery
    try:
        from store.achievements import achievementList, Achievement, AchievementCount
    except ModuleNotFoundError:
        pass
    
    try:
        from store.gallery import GalleryImage, galleryList
    except ModuleNotFoundError:
        pass
