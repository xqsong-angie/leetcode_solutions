class SquirrelResearch:
    def __init__(self, locations: dict[str, int]) -> None:
        self.locations=locations# all available hiding locations {loc_id1:levels1,loc_id2:levels2,...}
        self.hidden_nuts={}#(nut_id1,nut_id2,nut_id3,...)
        self.location_full={}#{loc_id1:False,loc_id2:True,...}
        self.timestamp=0
        

    def HideNut(self, timestamp: float, location_id: str, nut_id: str, nut_weight: float, time_to_expire: float) -> bool:
        if nut_id in self.hidden_nuts.keys() or location_id not in self.locations.keys() or self.location_full[location_id]==True:
            return False
        self.hidden_nuts[location_id]={"timestamp":timestamp,"nut_weight":nut_weight,"time_to_expire":time_to_expire,"expired":False}
        if self.timestamp>=timestamp+time_to_expire:
            self.hidden_nuts[location_id]["expired"]=True
        return True

    def RetrieveNuts(self, timestamp: float, location_id: str, max_squirrel_capacity_in_nuts: int) -> list[str]:
        retrieved_nuts=[]#[nut_id1,nut_id2,nut_id3,...]

        return retrieved_nuts

