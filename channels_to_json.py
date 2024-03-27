import json
channels = {"music": [], "politics": [], "science": [], "art": [],
            "sport": [], "funny": [], "games": []}

channels["music"] = [
    "UCawVzkkGUvxTvwn_c_WJ-lA",  # 1 Аквариум
    "UCWnqnojAgMdN0fQpr_xByJw",  # 2 Моргенштерн
    "UC18bHNKD21woNT7G0F4PN7Q",  # 3
    "UCSGRPrxhTRVMvmvqP4cXSjQ",  # 4
    "UCljnQxyQFCELOb7A9v1t66w",  # 5
    "UCDmgUB1w5SJVdIgVqy-Kgwg",  # 6 Консерватория
    "UCTvLTz1K83pEOZucc04Hbwg",  # 7
    "UC2eH4vw5JuVpzLDrCkxW2pQ",  # 8 МузТВ
    "UC2XLrPeYgf0n1W2HG4XgXpA",  # 9
    "UC7QX724vt3YwVnkMwtmdqNA"  # 10 из советских фильмов
]

channels["politics"] = [
    "UC7Elc-kLydl-NAV4g204pDQ",  # 1
    "UCBzDAjLfvBUBVMMP6-K-y0w",  # 2
    "UCUGfDbfRIx51kJGGHIFo8Rw",  # 3
    "UCgpSieplNxXxLXYAzJLLpng",  # 4
    "UCUT0cgd_Ru_Zykp4nP9B42g",  # 5
    "UCsAw3WynQJMm7tMy093y37A",  # 6
    "UCOu7RZ6qGjdFEeMiZQVtMXA",  # 7
    "UCbNYBIHgdRw5LX_NK5-9qDA",  # 8
    "UCL1rJ0ROIw9V1qFeIN0ZTZQ",  # 9
    "UCtO0TzSAoIOzTnTsQeywSSw"   # 10
]

channels["art"] = [
    "UC68e0hrTENfQkhSxpnw2GMQ",  # 1 музыка
    "UC9KFvnvWDmKAQhfxxDI0DHQ",  # 2 музыка
    "UCkWGIBcWtSuJ7xu72tLCV4A",  # 3 музыка
    "UCGzg7kiBe7AiTJQYg4TN1jQ",  # 4 литература
    "UCoFIica17mSL70pXNFRHCWQ",  # 5 литература
    "UCFs57_AuDKT02x9YaOEQ8Ww",  # 6 изобразительное
    "UCw-SvnADFRiC87aKAuzZcXQ",  # 7 изобразительное
    "UCSZujkjLtAKbTCieGdpDP5Q",  # 8 современное искусство
    "UC6cqazSR6CnVMClY0bJI0Lg",  # 9 кино
    "UC4tlrTXCBw6NPZ9nCA3_s9w"  # 10 кино
]

channels["science"] = [
    "UCDK8SFd2iuF_h4kklUoueJw",  # 1
    "UCf053FwQD-hnTY7aaaWTaVQ",  # 2
    "UClk8C-ve3vb96jSqltT05wA",  # 3
    "UChE2sc5N7PfdV-yN2_ctvtg",  # 4
    "UCl4goMIACgEkjZZAAiaWwJw",  # 5
    "UC5yvMRG0e_3jl9xo5rr0DnA",  # 6
    "UC_ruhy05BA2V_oxWjgTMlmA",  # 7
    "UCSPd93is2UQsd_jZ6yHBfqQ",  # 8
    "UCzWnF-3UWAGNeK5fIkBmahg",  # 9
    "UCdVX4yIGECc9q4eKjKVoJKQ"  # 10
]

channels["sport"] = [
    "UCjYicQAYfN_MTzHbKqvL_dA",  # 1
    "UCrZkmVymFwJDcttvHnsLxvA",  # 2
    "UC-ANf8CYk6gfCUW8UzoJptw",  # 3
    "UCNOo2oB5YJmaVsGzMv4VHxw",  # 4
    "UCWpjKglD29XizsdYQCCEJRg",  # 5
    "UCFFsQwmidm9iTyCwKgMh8bQ",  # 6
    "UCmmvrWZAHC9OPivFncPjTfws",  # 7
    "UCXA22L0X3bdXwHpufPuRv-w",  # 8
    "UCdwRBTP5LBk86EtX5Iv_6ow",  # 9
    "UCdEW3rqePdRGxvgnKkOmyxw"  # 10
]

channels["funny"] = [
    "UC3cJiUuZlpF-pkzqvSskTpg",  # 1
    "UC1uS4JFcc8KXZVoBSh3XVHA",  # 2
    "UCpTuLPXfIOcsPbvb2SIwD8w",  # 3
    "UCsk9ntn2afzIqInnx2jB8gw",  # 4
    "UCUbJYQmp_gAQWtaZn0ddO1w",  # 5
    "UCA0Xum6Bxx-rhmrog1A1ISQ",  # 6
    "UCSZ69a-0I1RRdNssyttBFcA",  # 7
    "UCqRwbeXjkNd2f5ExFJXAZxQ",  # 8
    "UC5sSL56GJWCi4wsMpobTrAw",  # 9
    "UCn9bv143ECsDMw-kJCNN7QA"  # 10
]

channels["games"] = [
    "UCdKuE7a2QZeHPhDntXVZ91w",  # 1
    "UC0cWWruNMb95iCBEOzPnjRA",  # 2
    "UCZUrS0zDszsXI_5ir_tI3cg",  # 3
    "UCBDLWj5X5D9bvBa3JIMMTIQ",  # 4
    "UC_Q1vhf7wcR_zGlc5ahAg0A",  # 5
    "UCq7JZ8ATgQWeu6sDM1czjhg",  # 6
    "UCOxQWb-OuyCSZadzWqrKTCQ",  # 7
    "UCYF2mxg48E5c3-jKpZoZSJA",  # 8
    "UCx02EI6ZIgxyg2MgdE_HM-g",  # 9
    "UCOmAtwe8UxKuj-qIdV77Iog"  # 10
]

f = open("channels.json", "w")
f.write(json.dumps(channels))
f.close()