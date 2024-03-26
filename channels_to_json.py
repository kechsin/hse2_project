import json
channels = {"music": [], "politics": [], "science": [], "art": [],
            "sport": [], "funny": [], "games": []}

channels["music"] = [
    "https://www.youtube.com/@aquarium1972",  # 1 Аквариум
    "https://www.youtube.com/@mmdcrew",  # 2 Моргенштерн
    "https://www.youtube.com/@queenhouse-7874",  # 3
    "https://www.youtube.com/@theBESTMUSICA",  # 4
    "https://www.youtube.com/@worldvideoview5742",  # 5
    "https://www.youtube.com/@mosconsvtv",  # 6 Консерватория
    "https://www.youtube.com/@VelvetMusicRu",  # 7
    "https://www.youtube.com/@muztv",  # 8 МузТВ
    "https://www.youtube.com/@karaokekalinka",  # 9
    "https://www.youtube.com/@gtrfmusic" # 10 из советских фильмов
]

channels["politics"] = [
    "https://www.youtube.com/@Popularpolitics",  # 1
    "https://www.youtube.com/@khodorkovskylive",  # 2
    "https://www.youtube.com/@Max_Katz",  # 3
    "https://www.youtube.com/@MackNack",  # 4
    "https://www.youtube.com/@LdprRuparty",  # 5
    "https://www.youtube.com/@NavalnyRu",  # 6
    "https://www.youtube.com/@ibertarian-party-ru",  # 7
    "https://www.youtube.com/@CommunistPartyRF",  # 8
    "https://www.youtube.com/@Ekaterina_Schulmann",  # 9
    "https://www.youtube.com/@SuperSharij"  # 10
]

channels["art"] = [
    "https://www.youtube.com/@Gleb_Oleinik",  # 1 музыка
    "https://www.youtube.com/@anna_vilenskaya",  # 2 музыка
    "https://www.youtube.com/@MusicwithMarie15",  # 3 музыка
    "https://www.youtube.com/@armenifedor",  # 4 литература
    "http://www.youtube.com/@samosoboymedia",  # 5
    "https://www.youtube.com/@user-kl6vv2do1v",  # 6 изобразительное
    "https://www.youtube.com/@TheArtsmuseum",  # 7 изобразительное
    "https://www.youtube.com/user/GARAGECCC",  # 8 современное искусство
    "https://www.youtube.com/user/TheBadComedian/videos",  # 9 кино
    "https://www.youtube.com/@kinopoisk"  # 10 кино
]

channels["science"] = [
    "https://www.youtube.com/@R_Nauka",  # 1
    "https://www.youtube.com/@childrenscience",  # 2
    "https://www.youtube.com/@NaukaPRO",  # 3
    "https://www.youtube.com/@getaclassmath",  # 4
    "https://www.youtube.com/@SciencePub",  # 5
    "https://www.youtube.com/@AcademiaNauk",  # 6
    "https://www.youtube.com/@user-wn9il6nl5l",  # 7
    "https://www.youtube.com/@postnauka",  # 8
    "https://www.youtube.com/@GTVscience",  # 9
    "https://www.youtube.com/@MadAstronomer"  # 10
]

channels["sport"] = [
    "https://www.youtube.com/@imagine_fitness",  # 1
    "https://www.youtube.com/@Mote",  # 2
    "https://www.youtube.com/@user-qy9zt7qv6o",  # 3
    "https://www.youtube.com/@IvanKrasavin",  # 4
    "https://www.youtube.com/@smartballet",  # 5
    "https://www.youtube.com/@delaytelo",  # 6
    "https://www.youtube.com/@MakeFitness",  # 7
    "https://www.youtube.com/@yogactivelife",  # 8
    "https://www.youtube.com/@YOGAwork",  # 9
    "https://www.youtube.com/@badassel17"  # 10
]

channels["funny"] = [
    "https://www.youtube.com/@standupclubru",  # 1
    "https://www.youtube.com/@vanya.usovich",  # 2
    "https://www.youtube.com/@improcom",  # 3
    "https://www.youtube.com/@fridaytv",  # 4
    "https://www.youtube.com/@barinthecity",  # 5
    "https://www.youtube.com/channel/UCA0Xum6Bxx-rhmrog1A1ISQ",  # 6
    "https://www.youtube.com/user/kvn",  # 7
    "https://www.youtube.com/user/SmetanaTV",  # 8
    "https://www.youtube.com/user/PrototypesLIVE",  # 9
    "https://www.youtube.com/channel/UCn9bv143ECsDMw-kJCNN7QA"  # 10
]

channels["games"] = [
    "https://www.youtube.com/@kuplinovplay",  # 1
    "https://www.youtube.com/@Compot",  # 2
    "https://www.youtube.com/@windy31LetsGoodPlays",  # 3
    "https://www.youtube.com/@DTFru",  # 4
    "https://www.youtube.com/user/IgromaniaVideo",  # 5
    "https://www.youtube.com/user/StopGameRu",  # 6
    "https://www.youtube.com/channel/UCOxQWb-OuyCSZadzWqrKTCQ",  # 7
    "https://www.youtube.com/channel/UCYF2mxg48E5c3-jKpZoZSJA",  # 8
    "https://www.youtube.com/channel/UCx02EI6ZIgxyg2MgdE_HM-g",  # 9
    "https://www.youtube.com/user/YogusFirst"  # 10
]

f = open("channels.json", "w")
f.write(json.dumps(channels))
f.close()