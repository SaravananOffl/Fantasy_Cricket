class cricketers:
    id = 0

    def __init__(self, player_name, scored, faced, fours, sixers, bowled, maiden, given, wkts,
                 catches, stumpings, ro, value, matches
                 , runs, hundreds, fifties, ctg):
        self.ctg = ctg
        self.fifties = fifties
        self.hundreds = hundreds
        self.runs = runs
        self.matches = matches
        self.value = value
        self.ro = ro
        self.stumpings = stumpings
        self.catches = catches
        self.wkts = wkts
        self.given = given
        self.maiden = maiden
        self.bowled = bowled
        self.sixers = sixers
        self.fours = fours
        self.faced = faced

        self.player_name = player_name
        self.scored = scored
        id = id + 1
