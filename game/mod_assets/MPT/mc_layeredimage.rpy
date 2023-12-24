


layeredimage mc turned:
    
    
    
    group outfit: #These attributes are here only to determine which set of "body" sprites to use later.  "null" is what lets us just use these attributes as logic and nothing else.
        attribute uniform default null
        attribute casual null
    
    
    
    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute cry null  #crying
        attribute curi null #curious
        attribute dist null #distant
        attribute doub null #doubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        #attribute lsur null #surprised (lightly)
        attribute nerv null #nervous
        attribute pani null #panicked
        #attribute pout null #pouting
        attribute sad null  #sad
        attribute sedu null #seductive
        #attribute shoc null #shocked
        attribute vang null #VERY angry
        #attribute vsur null #surprised (very)
        #attribute worr null #worried
        attribute yand null #yandere
        #attribute xxxx null #xxxx #Do you want to define a new mood?  Here, have a template!
    
    
    
    group blush: #Have to separate these out, they can't share moods.
        attribute nobl default null #No blush.
        attribute blus null #blushing.  defaults for n

    group sweat:
        attribute nosw default null
        attribute swea null
    
    group left:
        anchor (0,0)
        subpixel (True)
        #uniform
        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/mc/poses/uni_ldown.png"
        attribute lhip if_any(["uniform"]):
            "mod_assets/MPT/mc/poses/uni_lhip.png"
        
        #casual
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/mc/poses/cas_ldown.png"
        attribute lhip if_any(["casual"]):
            "mod_assets/MPT/mc/poses/cas_lhip.png"
        
        attribute cross:
            null

    group right:
        anchor (0,0)
        subpixel (True)
        #uniform
        attribute rdown default if_any(["uniform"]):
            "mod_assets/MPT/mc/poses/uni_rdown.png"
        attribute rhip if_any(["uniform"]):
            "mod_assets/MPT/mc/poses/uni_rhip.png"
        attribute rpen if_any(["uniform"]):
            "mod_assets/MPT/mc/poses/uni_rpen.png"
        attribute rup if_any(["uniform"]):
            "mod_assets/MPT/mc/poses/uni_rup.png"
        attribute cross if_any(["uniform"]):
            "mod_assets/MPT/mc/poses/uni_cross.png"
        
        #casual
        attribute rdown default if_any(["casual"]):
            "mod_assets/MPT/mc/poses/cas_rdown.png"
        attribute rhip if_any(["casual"]):
            "mod_assets/MPT/mc/poses/cas_rhip.png"
        attribute rpen if_any(["casual"]):
            "mod_assets/MPT/mc/poses/cas_rpen.png"
        attribute rup if_any(["casual"]):
            "mod_assets/MPT/mc/poses/cas_rup.png"
        attribute cross if_any(["casual"]):
            "mod_assets/MPT/mc/poses/cas_cross.png"

    group nose:
        
        anchor (0,0) subpixel (True)
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            "mod_assets/MPT/mc/expressions/face/base.png"
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            "mod_assets/MPT/mc/expressions/face/base_blush.png"
        attribute nose default if_any(["nosw"]):
            null
        attribute nose default if_any(["swea"]):
            "mod_assets/MPT/mc/expressions/face/sweat.png"
        
        
        ###All noses - truncated tags:
        attribute n1:
            "mod_assets/MPT/mc/expressions/face/base.png"
        attribute n2:
            "mod_assets/MPT/mc/expressions/face/base_blush.png"
    
    group mouth:
        
        anchor (0,0) subpixel (True)
        
        #Default Closed Mouths:
        attribute cm default if_any(["happ","laug", "nerv"]):
            "mod_assets/MPT/mc/expressions/mouth/smile.png"
        attribute cm default if_any(["neut","dist","anno","sad","angr","cry","doub","curi", "flus"]):
            "mod_assets/MPT/mc/expressions/mouth/neutral.png"
        attribute cm default if_any(["sedu"]):
            "mod_assets/MPT/mc/expressions/mouth/oval_teeth.png"
        attribute cm default if_any(["vang","pani"]):
            "mod_assets/MPT/mc/expressions/mouth/teeth_clenched.png"
        attribute cm default if_any(["yand"]):
            "mod_assets/MPT/mc/expressions/mouth/grin.png"
        
        #Open Mouths:
        attribute om if_any(["happ","laug","nerv","yand"]):
            "mod_assets/MPT/mc/expressions/mouth/smile_open.png"
        attribute om if_any(["anno", "dist"]):
            "mod_assets/MPT/mc/expressions/mouth/oval.png"
        attribute om if_any(["sedu"]):
            "mod_assets/MPT/mc/expressions/mouth/oval_tiny.png"
        attribute om if_any(["doub","neut","curi","angr","sad"]):
            "mod_assets/MPT/mc/expressions/mouth/oval_2.png"
        attribute om if_any(["flus"]):
            "mod_assets/MPT/mc/expressions/mouth/anxious.png"
        attribute om if_any(["cry","vang","pani"]):
            "mod_assets/MPT/mc/expressions/mouth/anxious.png"
        
        
        ###All mouths - truncated tags:
        attribute anxious:
            "mod_assets/MPT/mc/expressions/mouth/anxious.png"
        attribute grin:
            "mod_assets/MPT/mc/expressions/mouth/grin.png"
        attribute neutral:
            "mod_assets/MPT/mc/expressions/mouth/neutral.png"
        attribute oval:
            "mod_assets/MPT/mc/expressions/mouth/oval.png"
        attribute oval_teeth:
            "mod_assets/MPT/mc/expressions/mouth/oval_teeth.png"
        attribute oval_tiny:
            "mod_assets/MPT/mc/expressions/mouth/oval_tiny.png"
        attribute oval_2:
            "mod_assets/MPT/mc/expressions/mouth/oval_2.png"
        attribute smile:
            "mod_assets/MPT/mc/expressions/mouth/smile.png"
        attribute smile_open:
            "mod_assets/MPT/mc/expressions/mouth/smile_open.png"
        attribute teeth_clenched:
            "mod_assets/MPT/mc/expressions/mouth/teeth_clenched.png"

    group eyes:
        
        anchor (0,0) subpixel (True)
        
        #Default Opened eyes:
        attribute oe default if_any(["neut","sedu","happ","angr","curi","flus","laug"]):
            "mod_assets/MPT/mc/expressions/eyes/left/normal.png"
        attribute oe default if_any(["dist","nerv","doub","sad","anno"]):
            "mod_assets/MPT/mc/expressions/eyes/left/normal_lookaway.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/mc/expressions/eyes/left/normal_cry.png"
        attribute oe default if_any(["vang","pani"]):
            "mod_assets/MPT/mc/expressions/eyes/left/crazy.png"
        attribute oe default if_any(["yand"]):
            "mod_assets/MPT/mc/expressions/eyes/left/sick.png"
        
        #Default Closed eyes:
        attribute ce if_any(["neut","dist","anno","vang","sedu","flus","sad","angr","nerv","curi","doub","cry"]):
            "mod_assets/MPT/mc/expressions/eyes/left/closed_pensive.png"
        attribute ce if_any(["happ","yand","pani","laug"]):
            "mod_assets/MPT/mc/expressions/eyes/left/closed_excited.png"
            
        ###All eyes:
        attribute normal:
            "mod_assets/MPT/mc/expressions/eyes/left/normal.png"
        attribute normal_lookaway:
            "mod_assets/MPT/mc/expressions/eyes/left/normal_lookaway.png"
        attribute normal_cry:
            "mod_assets/MPT/mc/expressions/eyes/left/normal_cry.png"
        attribute crazy:
            "mod_assets/MPT/mc/expressions/eyes/left/crazy.png"
        attribute crazy_cry:
            "mod_assets/MPT/mc/expressions/eyes/left/crazy_cry.png"
        attribute sick:
            "mod_assets/MPT/mc/expressions/eyes/left/sick.png"
        attribute sick_cry:
            "mod_assets/MPT/mc/expressions/eyes/left/sick_cry.png"
        attribute closed_pensive:
            "mod_assets/MPT/mc/expressions/eyes/left/closed_pensive.png"
        attribute closed_excited:
            "mod_assets/MPT/mc/expressions/eyes/left/closed_excited.png"
    
    group eyebrows:
        
        anchor (0,0) subpixel (True)
        
        #Default Eyebrows:
        attribute brow default if_any(["neut","dist","sedu","happ"]):
            "mod_assets/MPT/mc/expressions/eyebrows/left/normal.png"
        attribute brow default if_any(["flus","laug","sad","nerv","cry","yand","pani"]):
            "mod_assets/MPT/mc/expressions/eyebrows/left/sad.png"
        attribute brow default if_any(["vang","angr","anno"]):
            "mod_assets/MPT/mc/expressions/eyebrows/left/angry.png"
        attribute brow default if_any(["curi","doub"]):
            "mod_assets/MPT/mc/expressions/eyebrows/left/confused.png"
        
        
        ###All eyebrows left:
        attribute brow_normal:
            "mod_assets/MPT/mc/expressions/eyebrows/left/normal.png"
        attribute brow_sad:
            "mod_assets/MPT/mc/expressions/eyebrows/left/sad.png"
        attribute brow_angry:
            "mod_assets/MPT/mc/expressions/eyebrows/left/angry.png"
        attribute brow_confused:
            "mod_assets/MPT/mc/expressions/eyebrows/left/confused.png"