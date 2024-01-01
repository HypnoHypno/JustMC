init -990 python:
    memory.writeToPersistent("topics", {})
    memory.writeToPersistent("affection_daily_cap", 8)
    
    affection_map = {
       "loving": {
            "range": (550, 10000),
            "multi": 1.75
        },
        "friendly": {
            "range": (250, 549),
            "multi": 1.5
        },
        "warm": {
            "range": (100, 249),
            "multi": 1.25
        },
        "neutral": {
            "range": (-29, 99),
            "multi": 1.00
        },
        "cold": {
            "range": (-99, -30),
            "multi": 0.75
        },
        "hostile": {
            "range": (-249, -100),
            "multi": 0.5
        },
        "antagonistic": {
            "range": (-10000, -250),
            "multi": 0.25
        },
        # This isn't an affection level, but instead a reserved value incase anything goes wrong.
        "invalid": {
            "range": (float("-inf"), float("inf")),
            "multi": 0.00
        }
    }

    class MC:
        """
        Class used for anything related to MC. (Affection/Sanity/Trust, Idle, Sentence Generation, Mood)

        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWX0Okdooooodxk0XNWMMWWNXK0kkkkkO0KKKXXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNX0kdc:;,'',,,,,,,,,;cloolc:;;,,,,,,;;::::cllodkOKXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0Oxol:;'''.......................'''''''',,,;;;;;;;;;:cldk0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0xl:;,'''.................''''',,,,,,,;;;;;;,,,,,,,;;;;;;;;;;;:cdk0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxc,'''''............'''',,,;;;;;;;;;;;;;;,,,,,,;;;;;;;;;;;;;;;;;;;;;:cokKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOd:,''''''''''''...'',,,;;;;;;;;;;;;;;;;;;;;;,,,,,,,,,,,,;;;;;;;;;;;:;;;;;;:lx0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOdc;;;;;,'''''''''''',,;;::::;;::;;;;;;;;;;;;;;;;;;;;;;;;,,''',;;;;;;;;;;;;;;;:;;;cxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOoc:;;;:;;;,,,,,,,;,,,,;;:::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::;;;;,,,,;;:;;;;;;;;:;;:;;;:oONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxc;;;:;;;;;;,,;::::::::;;::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:;;:;;,,;;;;;;;;,;;;::;;;:;:lONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOo:;::;;;;;;;;,,;::::::::::;;::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:;;;;;;;;;;;;;;:;;;;;;:;;:;;;:lONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOl:;;;;;;;;;;;;,,,;::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::::;;;;;;;;;;;;,,;;;;;;;;;:o0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0o:;;;;;;;;;;;;:;,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:;::::::::cc:::;;;;;;;;;:;,,,;;;;;;;;;:xXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKd:;;;;;;;;;;;;;;;;,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::ccccccc::::::::::;;;;;;;;;;;,,;;;;;;;;;;lOWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkc;;:::::;;;;;;;;;;;,,;::;;;;;;;;;;;;;;;;;;;;;;;;:;;;:::::;;;:::::;;:ccllcccc::;;;;;;;;;;;;;;;;;;;,',;;;;;;::;:dXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKo:;;;::ll:;;:::;;;;:;,;:;::;;;;;;;;;;;;;;;;;;;;;:::;;;;;:cll:;;::lllc:;:ccc::;:;;;;;;;:;;;;;;;;;;;;;;,',;;;;;;:;;l0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkc;;;;;:clc;;cllc:;;:c;,:l:::::::;:::;;;;:cc::ccc:::clcccllloooc:;;:lllc:;;;;;;;;;;;;;;;;;:;;;;;;;;;;;;;,'';;;;;;;;;:kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKo:;::;;;:::;;clooc;:loo:,:olcc::ll::lolc:;codddddoc:;:lodddddoolol:;;;cc:;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;'',;;;;;;;;:kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOc;;;;:;;;;;;;:lool:;lodoc;:oddoc:odl:coddo::oddddddoc:;:cloolcc::::c:;;,;:;;:;;;;,;;;;;;;;;;,;;;;;;;;;;;;;;;,'.,;;;;;;;;:OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWkc;;:;;;;;;;;;;:cllc;:loddl:;ldddl:odoc:cdxdl;:llcccccc:;;;::::;;;;;;;::;,,;;;;;;;;;,,;;;;;;;;;;;;;;;;;;;;;;;;;;'.';;;;;;;;cOWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk:;;;;;;;;;;;;;;;:cc;;:cloooc;coool:clol::cooc;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,;;;::;;;;,,;;;;;;;;;;;;;;;;;;;;;;;;;'..,;;;;;;;c0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOc;;;;;:;;;;;;;;;:;:;;;;;::clc;;:::c;;::c:;;:::;;;;;;;;;:;;;;;;;;;:;;;;;;:;;:;,,;;;;;;;;;;,;;;;;;;;;;;;;;;;;:;;;;;;;'..','';;;;lKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0l;;;;;;;;:;;;;;;;;;;;;;;;;;;::;,;;:;;;;;:;;;;;:;;;;;;::;;;;;;;;,,,;;;;;;;;;;;:;'';;;;;;;;;;,,;;;;;;;;;;;;;;;;;;;,,;;;'......,;;;dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo;;;;;;;;:;,',;;:;;;;;;;;;;;;;;;;,;;;;;;;;;;,;;;;;;;;;;;;;;;;;:;;,',;;;;;:;;;;;;,..,;;;;;;;;;,,;;;;;;;;;;;;;;;;;;;',;;,.......';;;kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx;;;;;;;;:;,..;:;:;;;;;,,;;;:;;;;;,;;;;,;;;:;,'',;;;;;;,,;;;;;;;;:;'.',;;;;;;;;;;;'..;;,,,;;;:;,,;;;;;;;;;;;;;;;;;;,.';;,.......';,:0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOc;;;;;;;:;'..,;:;;;;;,',,,:;;;;;;,,,;:;,;;;;:;'..,;;;;,'.';;;;;;;;;;'..',;;;;:;;:;'..';,'.,;;;;;,,;;;;;;;;;;;;;;;;;;'..,;,.......','lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXl,;;:;::;;'...,;;;;;:;'.,',:;;;;;;,;,;;;;,;;;:;'...;:;;;'...,;;:;;::;,.....,;;;;::;'...',....,;;;;,,;;;;;;;;;;;;;;;;;'...','.........,OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx,',;:::;,....';;:;;;:,..'',;:;;;;;,,;,;:;,,;;;;,...';::;'....,;;;;;;;;,.....,;;;;:;'....'.....';;:;,,;;;;;;;;;;;;;;;;,................oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:..,::;:;'....';;;'';;'..'',;;;;;;;;,,;,;;;,;;;;;'...';;;'.....,;;;;;;:;'.....';;;;;.............;;;;,,;:;;;;;,,;;;;;;;................:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo...,;;:;'.....';;,.';,....',;;;;;;;;,,;,,;;,,;;:;,....';:,......';;;;:;;,......';:;;..............;:;,,;:;;;;;;,,;;;;;;'.....''........,kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO;...,;;;,......,;;..,;,.....';:;;;;;:;,,,'.,;,,;;;;'....,;,.......';;;:;;;,.......;:;..............';:;',;:;;;;;;,,;;;;;'......''.....'.'dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXl....,::;'......,;,..,;'......';::;:;;:;'',...',;;;;,.....''..........';;;;;.......';,...............,;;,';:;;;;;;;,;;;;;'..'....'''...'''oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk,....,:;,.......,,'.',,........,;;;;:;::;'',....';;:;...........',......';:;'.......'.................;:;',;;;;;;;;,',;;;'..'......'''...'lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMXc.....,:;........''..',,.........,;;;:;;:;,'.......;;;,..........':c,......';,..............'..........,;;,,;;;;;;;;'..;;;'..''...''.......,dKWMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMM0;.....,;,........'...','.....''..';;;;:::;;;'......';:;...........,oo;'.....................''''........;;,,;;;;;;;;'...,;'...'...'''''''..,cdkKNMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMM0;.....','............','.....;;...';;;,;;:;;;'......';;'..........'cxxdc'...............''..'''''.......,;,';;;;;;;;'....'.........'''''''.:KWNNWMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMM0;......'............''''.''''lo,...,;,..',;;:;,.......,,..........':xkkko;...........'''''...'''''......';'.,;;;;;;;'..............''''''''cKMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMM0;.............'''''''',''''';oxl'...,,......',;;'......''........'';d0K0kxl,.....''...''''...''''''......,'..;;;;;:,...............''''''''lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMM0;.'..'.......'''''''';;''''':dxxc'...''........'','..............'',o0XXKOkdl,'.''''..''''...''''''..........';;;;;,....''''''.....''''''''oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMWk,''..''....'''''''''':c''''':dxxd:'...........................'...''l0KXXK0kkxl;'''''..'''',,''''''...''......';;;;'....''''''......'..''''oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMNo''...''''''''''''''''co;'''':dOOkd:'.........................'''...'cOKXXXXK0Okxoc;''..''''cc,'''''...''.......,;;;..'..''''''......'...'''dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMWO;',;'.''''''''''''''''cdc,''':d0K0kd:''.....''''..............''''...cOKXXXXXXKK0Okxoc;'.'''ld:'''''...'''.......,;,..'..''''''..........'';OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMKl':xk:.''''''''''''''''cxo;''';dOKX0Odc,'''...''''''''..........'''...;xkkxxdddodxxddddoc,'',oxl,''''....''''.....',..''...'''''........ .'.:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMNo;oKWXc'''''''''''''''''cxxc,'.,lOKXXKOkl;''''...'''''.''''............':cllodxkO00K00Okkxc'.,oko;''''....''''......'..'''..''''........  ..'cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMWkoOWMMXl''''''''''''.....,cll;'''ckKXNXX0Od:'''''....''...''''..........'xXXXNNNNNNNNNNNNNXk;.;dkd:''''....'''''........'''..''''.....     ..'oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMNKNMMMMNd'''''.'''''......':cc:'..;oOXNNNXX0Oo;''''''..''....'''....''''.'kNNNNNNNNNNNNNNNNNKl';xOkc'''''..''''''...'....''..''''.....      ..'dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMWk,''''..'''''..''';dkk0d,.,:lkXNNNNXXKOo;'''''';ol:....''''',;''.'xXXXXXXXXXXXXXXXXXXx,:k00o''''.,;,'''''..''...'''..''''.  .        .'dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO;'''''..''''...'',oOOKKo':kOOKNNNNNNXXKOo;'''''ck0kdc,'..''';::,;xK0kxdlc:::::::ccll:':xOKx,''''cc,'''''..''''''''..'''..           ..dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKc''''''...'''...''lO0KXKll0XXNNNNNNNNNNNX0o:'''':OXXXKOxlc;,',;;,''......             ..:dd;.'';dl'''''...''''''''..''..         .. ..dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXl'''''''...''....':kKKKX0xOXXXXXNNNNNNNNNNXKxl;'';kXNNNXK0Okd:......',:;........''...,c;.':,.',okl'''''...'''''''...'',,.       ... ..oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx,'''''''......  ..,::;:::lkKKK0KXNNNNNNNNNNNX0xl;,oKNNNXXXKd;:dOOO0kldo'.......''''.,kk;,c;.,lkOd'''''...'''''''...''ox;      ...  ..lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKc''''''''.... .'::cc:,'....,:okKXNNNNNNNNNNNNNNX0kxOXNNNNNKxokKXNNNO:...............;Od;dx;'ck0Kd''''....'''''''...'l0Kc.    ...'. ..cKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx,''''''''',''o0KKXNW0xx;...'':ONNNNNNNNNNNNNNNNNNNNNNNNNNNK0KXXkc;'..':,.....ll;,.'kXxxKx,ck0XXo''''...'''''''...'l0XKo.    ..,dl...:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKc''''''''',cclkKKXXk:,,......,kNNNNNNNNNNNNNNNNNNNNNNNNNNNNNWMMKd:,clcdkocldk0kO0kOXXXNXdlOKXNKl''''...'''''''...cOXXKo... ..'lXKc..,kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO;''''...'';odkXWMWd..','..'''dNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNWWWWKookO0KXXXXK0Oxx0NNNNN0x0XXNN0:.'',,.'''''''...cdk0XKl... ..;kWMKc..lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx;''''..''';dkOKNMXdcloxdxkkk0NNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXNNNN0xdxxkkkkkkkOOKNNNNNNKKNNNNXx,'',:;'''''''...lxxkKKk,... .'oXMMMXl.,0MMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk;''''..''';okO0NNX0xxO000kk0NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXXXXKK00KKKXNNNNNNNNNNNNNNNNNKl'''cc,''''''..'lxkk0Kx,......:0WMMMMXl'oNMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO:''''...'';o0KKKOOOOxxxkOKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNk;'':o:'''''''.,okkkO0o'. ....'dNMMMMMMXoc0MMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0c'''.....',lOXXX00XXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN0c'';oo;''''''';oxxxOk:.   ....cKMMMMMMMMXxkNMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo,''....,;,:xXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXXXXXXXXXXXXNNNNNNXx,.,okl'''''';oddxO0x,...   ..'dWMMMMMMMMMNKNMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx;''...'ldold0NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXXXXXXXXXXXXXXXNNNNNN0:',oOx:''''',d000K0o'....   ...lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOc''...'xXX00KXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXXXXXXXXXXXXXXXXXNNNNNKl',oOOo,'''',dKXXKk:..... ..  ..'dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd;''..c0NNXXXXXXXXXNNNNNNNXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXXXXXXXXXXXXXNNNNNNNNXd',d0Kk:'''',o00kd:'..... ....'lc',kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOc''.;xKNNNXXXXXXXNNNNNWNKKXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXNNNNNNNNNNNNXx;ckKK0o,'''..,;'...........'',xNN0olkNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXd,''cOXNNNNNNNNNNNNNNWXKXNXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNkldKNNXO:''.................'',dNMMMWX0XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXc..'cOXNNNNNNNNNNNNNNXKXNNXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKkOXNNNXd'...................',oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx'...cOXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXNNNNN0:..................'''lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0;'...:kXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKl..................'''cKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXl';oc';kXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKkc....... .......,:,.'':0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdc0WKc.;kXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKkc'...............;kx,.';OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0KWMW0c.,dKXNNNNNNNNNNNNNNXKO0KKKKKKKKKK000000KXNNNNNNNNNNNNNNNNNNNNNNNNKOo'. ..............;OWO;.;kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMMMM0:.'lOXNNNNNNNNNNNNXOc,:::coxkkkkkxxxxxxkXNNNNNNNNNNNNNNNNNNNNNNKOxo,. .............'c0WMO;'dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0:.':xKNNNNNNNNNNNNKd;,,;coxxxxxxxxxddOXNNNNNNNNNNNNNNNNNNNNNKOxxko'...........''',oXMMMKllXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0c'.'lOXNNNNNNNNNNNXkllxkkkkkkkkkxkOKXNNNNNNNNNNNNNNNNNNNXKOxk0K0o......'';,.''';xNMMMMWXXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKl'.,ok0XNNNNNNNNNNNXKOkkkkkkkkO0XNNNNNNNNNNNNNNNNNNNNX0kkk0KKKKd......'ckc.'':OWMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd,:OKOO0KXNNNNNNNNNNNXXKK00KXNNNNNNNNNNNNNNNNNNNNXK0kkOKKKKKXKx,....':0Kc.'l0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNklkWWX000KXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNX0OkO0KXXXKKKKXx;.''';OWXc'oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNMMMMWXK00KXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNX0OkO0KXXXKKKKKKKKk:''';kWMNOkXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXK00KXNNNNNNNNNNNNNNNNNNNNNNXKOkkO0KXXXXXXXKKKKKKK0o,',dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXK00KXNNNNNNNNNNNNNNNK0Okxxk0KXXXXXXXXKKKKKKKKKKOo,:0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXK00KNNNNNNNNNXKOxdddxO0KXXXXXXXXXXKKKKKKKKKKKklxNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0xk0KKKK0OkxdodkO00KXXXXXXXXXXKKKKKKKKKKKK0OkKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxdddddooodxkO0KKKXXXXXXXXXXXKKKKKKKKKKK0O0K0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkdddddxxkO00KKXXXXXXXXXXXXKKKKKKKKKKK0O0XXXKKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0xxxkkO00KKKXXXXXXXXXXKKKKKKKKKKKKK000KXXXXXKKKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKKkxk0KKKKXXXXXXXXXXXXKKKKKKKKKKKKK0OKXXXXXXXXXKKXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNK0XX0xx0KXXXXXXXXXXXXXXXKKKKKKKKKK0OO0XXXXXXXXXXXXKKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX0KXK0xxOKXXXXXXXXXXXXXXXXXXXXXXXK0O0XXXXXXXXXXXXXXKXWNXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKKK00kxOKXXXXXXXXXXXXXXXXXXXXXK0O0XXXXXXXXXXXXXXXXXNMMWNXNNNNNNNNNNNNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXK0kxkXX00kxkKXKKKXXXXXXXXXXXXXXXK0O0XXXXXXXXXXXXXXXXXXNMMMMMWXOdollllllllldxOKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWNXXXXKKK0OOOO0K0dccc;:kXXK0kdkKXKKXXXXXXXXXXXXXK0OO0KXXXXXXXXXXXXXXXXXXNMMMMMMMXdclccc:::::::;,:dO00KKKKXXXXNNNNNNWWWWWWWWMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXX00Okkkxddoolcccccc:::::::;,;:cc:dKXXK0kdkKXXXXXXXXXXK00OOO00KXXXXXXXXXXXXXXXXXXXXNWMMMMMMWOlcccc::::::;'..';:::::ccccccllllllooooooddxxxkkO000KXXNNWWM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKkxolc::::::::::::::::::::::::;,;:cc:ckXXXK0kdkKXXXXXXNK0OkkO0KXNNXXXXXXXXXXXXXXXXXXKXNMMMMMMMMNx:cccc:::::,...';::::::::::::::::::::::::::::::::::cllloxkOK
        """

        # Idle
        def addTopic(topic_name, category, unlocked, playersays):
            """
            Will add a new random chatter topic to the database.

            Conditions:
                1. The topic set isn't already in the database.

            In:
                1. A string containing the label name of the topic that you want to add.
                2. A list containing the categories that you want it to be in, in string format. 
                    Categories can be anything.
                3. Do you want this topic to be unlocked or not?
                4. Does the player say it (pool topic) or is it a random chatter topic?
            
            Out:
                A boolean representing whether or not we were successfully able to add it to the database.
            """
            topic_database = persistent.data.get("topics", {})
            if topic_name not in topic_database:
                new_topic = {topic_name: {"category": category, "seen": renpy.seen_label(topic_name), "unlocked": unlocked, "pool": playersays}}
                topic_database.update(new_topic)
                memory.writeToPersistent("topics", topic_database)
                return True
            else:
                return False

        def getIdleTime():
            """
            Will return an amount of seconds to wait during idle.

            Conditions:
                1. The random chatter frequency set.

            In:
                Nothing.

            Out:
                An integer representing how many seconds should be waited until the next random chatter.
            """
            try:
                return random.randint(25, 45)
            except:
                return 0

        # Affection
        def isAffection(affection="neutral", higher=False, lower=False):
            """
            Will return if MC is the affection level specified, or higher/lower if stated so.

            Conditions:
                1. If higher/lower is set to true.

            In:
                1. The affection level you wish to check for, in lowercase. (Default "neutral".)
                2. Whether or not you want to count the player being above this level of affection. (Default False.)
                3. Whether or not you want to count the player being below this level of affection. (Default False.)

            Out:
                A boolean representing whether or not MC is at/above/below this level of affection.
            """
            try:
                global affection_map
                affmap = affection_map[affection]["range"]
                highercheck = persistent.data.get("affection", 0) >= affmap[0]
                lowercheck = persistent.data.get("affection", 0) <= affmap[1]
                if not (higher or lower) or (higher and lower):
                    return highercheck and lowercheck
                elif higher:
                    return highercheck
                else:
                    return lowercheck
            except:
                return False

        def getAffection():
            """
            Will return the level of affection MC is at. Prefer using MC.isAffection(affection, higher, lower) over this if you can.

            Conditions:
                1. For every level of affection, is MC that affection level?

            In:
                Nothing.

            Out:
                A string which is MC's current affection level in lowercase.
            """
            global affection_map
            try:
                for afflevel in list(affection_map.keys()):
                    if MC.isAffection(affection=afflevel):
                        return afflevel
            except:
                pass
            return "invalid"

        def gainAffection(affectiongain=0.00, override=False):
            """
            Will earn the affection set above to MC. Will be multiplied by the "multi" value in affection_map for the current affection level.

            Conditions:
                1. Is override set to true?
                2. If override is set to false, will the amount of affection added make the amount gained today higher than the daily cap.
                3. Gaining the amount of affection, will our affection be higher than the high hard cap?
            
            In:
                1. A floating point number representing the amount of affection you want to gain. (Default 0.00.)
                2. Do you want to override the daily cap? (Default False.)

            Out:
                MC's current affection now.
            """
            global affection_map
            affection_hard_cap = affection_map["loving"]["range"][0]
            affectionlvl = MC.getAffection()
            multiplier = affection_map[affectionlvl]["multi"]
            affectiongain *= multiplier
            affgaintoday = persistent.data.get("affection_gain_today", 0)
            affcap = persistent.data.get("affection_daily_cap", 8)
            aff = persistent.data.get("affection", 0)
            if affgaintoday + affectiongain > affcap and not override:
                affectiongain = affcap - affgaintoday
            aff += affectiongain
            if not override:
                memory.writeToPersistent("affection_gain_today", affgaintoday + affectiongain)
            if aff > affection_hard_cap:
                aff = affection_hard_cap
            memory.writeToPersistent("affection", aff)
            renpy.save_persistent()
            return aff

        def loseFloatAffection(affectionloss=0.00):
            """
            Will lose an amount of affection determined by the float passed.

            Conditions:
                1. Losing the amount of affection, will our affection be less than the low hard cap?

            In:
                A floating point number representing how much affection you want to lose. (Default 0.00.)

            Out:
                MC's current affection now.
            """
            affection_hard_cap = affection_map["antagonistic"]["range"][0]
            aff = persistent.data.get("affection", 0)
            aff -= affectionloss
            if aff < affection_hard_cap:
                aff = affection_hard_cap
            memory.writeToPersistent("affection", aff)
            renpy.save_persistent()
            return aff
        
        def losePercentageAffection(affectionloss=0.00):
            """
            Will lose a percentage of affection determined by the float passed. (If affection is less than 100, will assume that MC has exactly 100.0 affection.)

            Conditions:
                1. Is MC's affection less than 100.0?
                2. Losing the amount of affection, will our affection be less than the low hard cap?

            In:
                A floating point number representing how much percentage of total affection you want to lose. (Default 0.00)

            Out:
                MC's current affection now.
            """
            affection_hard_cap = affection_map["antagonistic"]["range"][0]
            aff = persistent.data.get("affection", 0)
            if aff >= 100.0:
                total_affection = aff
            else:
                total_affection = 100.0
            affectionloss = (affectionloss / 100) * total_affection
            aff -= affectionloss
            if aff < affection_hard_cap:
                aff = affection_hard_cap
            memory.writeToPersistent("affection", aff)
            renpy.save_persistent()
            return aff
        
        # Mood
        def getMood():
            return persistent.data.get("mood", "fine") #not done obviously lol

        # Dialog
        def getTalkMenuQuip():
            pname = persistent.data.get("player_name", "Player")
            quipmap = { #TODO: in the future, have there be defined quips for every mood, and have variations for different affection levels.
                "fine": [
                    "Hey.",
                    "Yeah?",
                    "What's up?",
                    "What's going on, " + pname + "?",
                    "Oh, me?",
                    "Ah, hi " + pname + ".",
                    "Yo."
                ]
            }
            chosen_quip = random.choice(quipmap["fine"])
            return chosen_quip