def rankEmoji(skill_rating):
    if skill_rating < 1500:
        emoji = '<:b_:559923570252447764>'
    elif skill_rating < 2000:
        emoji = '<:s_:559923570357305354>'
    elif skill_rating < 2500:
        emoji = '<:g_:559923570268962816>'
    elif skill_rating < 3000:
        emoji = '<:p_:559923570105647107>'
    elif skill_rating < 3500:
        emoji = '<:d_:559923570323488768>'
    elif skill_rating < 4000:
        emoji = '<:m_:559923570378276889>'
    elif skill_rating >= 4000:
        emoji = '<:gm:559923570369626142>'
    else:
        emoji = ""
    return emoji

hero_dict = {
        "ana" : "<:Ana:591708294477905952>",
        "ashe" : "<:Ashe:591714749486465045>",
        "baptiste" : "<:Baptiste:591708294951862413>",
        "bastion": "<:Bastion:591708294826164225>",
        "brigitte": "<:Brigitte:591708295182680065>",
        "d.va": "<:DVa:591709680632594437>",
        "dVa" : "<:DVa:591709680632594437>",
        "doomfist" : "<:Doomfist:591708295396458498>",
        "genji" : "<:Genji:591708295484407818>",
        "hanzo" : "<:Hanzo:591708295501185034>",
        "junkrat" : "<:Junkrat:591708295409172521>",
        "lúcio" : "<:Lucio:591708295383744513>",
        "lucio" : "<:Lucio:591708295383744513>",
        "mccree" : "<:McCree:591708295673151509>",
        "mei" : "<:Mei:591708296092712971>",
        "mercy" : "<:Mercy:591708295555973140>",
        "moira" : "<:Moira:591708295287406603>",
        "orisa" : "<:Orisa:591708295551516672>",
        "pharah" : "<:Pharah:591708295522156544>",
        "reaper" : "<:Reaper:591708295388200992>",
        "reinhardt" : "<:Reinhardt:591708295509835807>",
        "roadhog" : "<:Roadhog:591708295589396480>",
        "sigma" : "<:Sigma:619259776144113664>",
        "soldier76" : "<:Soldier76:591708295719419922>",
        "sombra" : "<:Sombra:591708295484538892>",
        "symmetra" : "<:Symmetra:591708295413235717>",
        "torbjörn" : "<:Torbjorn:591708295249526815>",
        "torbjorn" : "<:Torbjorn:591708295249526815>",
        "tracer" : "<:Tracer:591708295471824906>",
        "widowmaker" : "<:Widowmaker:591708295555710995>",
        "winston" : "<:Winston:591708295769882624>",
        "wrecking ball" : "<:Wrecking_Ball:591708295715356692>",
        "wreckingball" : "<:Wrecking_Ball:591708295715356692>",
        "wreckingBall" : "<:Wrecking_Ball:591708295715356692>",
        "zarya" : "<:Zarya:591708295539195920>",
        "zenyatta" : "<:Zenyatta:591708295560036359>",
        "tank" : "<:Tank:619262646885154846>",
        "dps" : "<:Dps:619262646834692106>",
        "damage" : "<:Dps:619262646834692106>",
        "support" : "<:Support:619262646708863007>"
        }

teams = {
        ("ATL","atl","atlanta","reign") : ["Atlanta Reign",0x910f1b,"https://bnetcmsus-a.akamaihd.net/cms/page_media/32/32MTX0PLEDY31542673991836.png","<:reign:546095303909048340>","7698"],
        ("BOS","bos","boston","uprising") : ["Boston Uprising",0x174b97,"https://bnetcmsus-a.akamaihd.net/cms/page_media/43UINMGMA83X1513383982827.png","<:uprising:546095303598538773>","4402"],
        ("CDH","cdh","chengdu","hunters") : ["Chengdu Hunters",0xffa000,"https://bnetcmsus-a.akamaihd.net/cms/page_media/st/STKSER89UHKO1542674031469.png","<:hunters:546095303585955852>","7692"],
        ("DAL","dal","dallas","fuel") : ["Dallas Fuel",0x0072ce,"https://bnetcmsus-a.akamaihd.net/cms/page_media/NO44N7DDJAPF1508792362936.png","<:fuel:546095303867105280>","4523"],
        ("FLA","fla","florida","mayhem") : ["Florida Mayhem",0xfeda00,"https://bnetcmsus-a.akamaihd.net/cms/page_media/4GO273NATVWM1508792362854.png","<:mayhem:546095303732887553>","4407"],
        ("GLA","gla","gladiators","lag") : ["Los Angeles Gladiators",0x3c1053,"https://bnetcmsus-a.akamaihd.net/cms/page_media/3AEMOZZL76PF1508792362892.PNG","<:gladiators:546095303745601557>","4406"],
        ("GZC","gzc","guangzhou","charge") : ["Guangzhou Charge",0x67a2b2,"https://bnetcmsus-a.akamaihd.net/cms/page_media/sz/SZQVDGE3F1TE1542674048320.png","<:charge:546095303560921110>","7699"],
        ("HOU","hou","houston","outlaws") : ["Houston Outlaws",0x97d700,"https://bnetcmsus-a.akamaihd.net/cms/gallery/2YF5VLIMGZVA1546557680222.png","<:outlaws:546095303892140032>","4525"],
        ("HZS","hzs","hangzhou","spark") : ["Hangzhou Spark",0xfb7299,"https://bnetcmsus-a.akamaihd.net/cms/gallery/QQ8MNSYYJGDK1544640571357.png","<:spark:546095303757922305>","7693"],
        ("LDN","ldn","london","spitfire") : ["London Spitfire",0x59cbe8,"https://bnetcmsus-a.akamaihd.net/cms/page_media/NW461AQIYQMK1508792363133.png","<:spitfire:546095304332673034>","4410"],
        ("NYE","nye","nyxl","new york","excelsior") : ["New York Excelsior",0x0f57ea,"https://bnetcmsus-a.akamaihd.net/cms/page_media/9r/9RYLM8FICLJ01508818792450.png","<:excelsior:546095303678230529>","4403"],
        ("PAR","par","paris","eternal") : ["Paris Eternal",0x8d042d,"https://bnetcmsus-a.akamaihd.net/cms/page_media/qm/QM7JE0THABVT1542674071412.png","<:eternal:546095304206712855>","7694"],
        ("PHI","phi","philadelphia","fusion") : ["Philadelphia Fusion",0xf99f29,"https://bnetcmsus-a.akamaihd.net/cms/page_media/3JZTLCPH37QD1508792362853.png","<:fusion:546095303988740107>","4524"],
        ("SEO","seo","seoul","dynasty") : ["Seoul Dynasty",0xaa8a00,"https://bnetcmsus-a.akamaihd.net/cms/page_media/LHRSIW3NWH211508792362796.png","<:dynasty:546095303946797058>","4409"],
        ("SFS","sfs","san francisco","shock") : ["San Francisco Shock",0xfc4c02,"https://bnetcmsus-a.akamaihd.net/cms/page_media/YO24NN5KAOFL1508792362791.png","<:shock:546095303669973001>","4404"],
        ("SHD","shd","shanghai","dragons") : ["Shanghai Dragons",0xd22630,"https://bnetcmsus-a.akamaihd.net/cms/page_media/B0R64QSNCDLX1508792362793.png","<:dragons:546095303661584414>","4408"],
        ("TOR","tor","toronto","defiant") : ["Toronto Defiant",0x000000,"https://bnetcmsus-a.akamaihd.net/cms/page_media/g0/G05QL2P5A92E1542674081932.png","<:defiant:546095303728693258>","7695"],
        ("VAL","val","valiant","lav") : ["Los Angeles Valiant",0x004438,"https://bnetcmsus-a.akamaihd.net/cms/page_media/0D8BNUWVZP6B1508792362890.PNG","<:valiant:546095304139603978>","4405"],
        ("VAN","van","vancouver","titans") : ["Vancouver Titans",0x09226b,"https://bnetcmsus-a.akamaihd.net/cms/gallery/F1WE9LBKIGHD1543976752064.png","<:titans:546095303854391302>","7696"],
        ("WAS","was","washington","justice") : ["Washington Justice",0x990034,"https://bnetcmsus-a.akamaihd.net/cms/page_media/95UE5OJKSFQF1543968718489.png","<:justice:546095304030552074>","7697"],
        }