import random
class database:
    Names=['BBT_SHELDON','BBT_RAJ_KOOTHRAPALLI','BBT_LEONARD','BBT_HOWARD_WOLOWITZ','BBT_AMY_FRRAH_FAWLER','VERONICA','UNQ_GAMER','I_M_RUTHLESS','SOUL_MORTAL','SPOUL_REGALTOS','8BIT_REBEL']
    Id=random.randrange(564748369,595874846)
    RATIO=random.uniform(1,5)
    Tier=['CONQUERER','ACE','CROWN','DIAMOND', 'PLATINUM', 'GOLD', 'SILVER', 'BRONZE']
    Server=['ASIA','MIDDLE_EAST','KRJP','NORTH_AMERICA']
    Win=random.randrange(10,30)
    Top_10=random.randrange(60,90)

 
    

class ans:
    def ans():
        return [random.choice(database.Names), 
        random.randrange(564748369,595874846),
        round(random.uniform(1,5), 2), 
        random.choice(database.Tier),
        random.choice(database.Server),
        random.randrange(10,30),
        random.randrange(60, 90),
        
         ]


