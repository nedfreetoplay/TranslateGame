import os
import weakref
from collections import defaultdict

print("start")

class KeepRefs():
    __refs__ = defaultdict(list)
    def __init__(self):
        self.__refs__[self.__class__].append(weakref.ref(self))

    @classmethod
    def get_instances(cls):
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if inst is not None:
                yield inst

class Location(KeepRefs):
    def __init__(self, name, **kwargs):
        self.name = name
    @property
    def formatted_name(self):
        name = self.name
        name = name.lower()
        name = name.replace("'", "")
        name = name.replace(" ", "_")
        return name

def mkdir(path):
    try:
        os.mkdir(path)
    except:
        pass
    try:
        f = open(path + "\\_dummy", "a")
    except:
        pass
    finally:
        f.close()

print("locations")
L_map = Location("Town Map", unlock_popup="unlock14", locked=True)
L_NULL = Location("NULL", locked=True)

###SCHOOL###
L_school_hall = Location("School Hall", unlock_popup="unlock13", background="school_day", parents=L_map, locked=True)
#school hall children
L_school_frenchclassroom = Location("French Classroom", background="school_french_day", parents=L_school_hall)
L_school_scienceclassroom = Location("Science Classroom", background="school_science_day", parents=L_school_hall)
L_school_musicclassroom = Location("Music Classroom", background="school_music_day", parents=L_school_hall)
L_school_track = Location("School Courtyard", background="school_gym_day", parents=L_school_hall)
L_school_lefthallway = Location("School Left Hallway", background="school_lefthall_day", parents=L_school_hall)
L_school_floor2 = Location("School Second Floor", background="school_second_day", parents=L_school_hall)
L_school_righthallway = Location("School Right Hallway", background="school_right_hall_day", parents=L_school_hall)
L_school_locker_MC = Location("School Locker", background="school_locker_mc_day", parents=L_school_hall)
#left hallway children
L_school_girlsroom = Location("School Girl's Lockerroom", background="school_locker_room_broken_day", parents=L_school_lefthallway, locked=True)
L_school_boysroom = Location("Boy's Lockerroom", background="school_locker_room_day", parents=L_school_lefthallway)
L_school_locker_roxxy = Location("Roxxy's Locker", background="school_locker_roxxy_day", parents=L_school_lefthallway, locked=True)
L_school_locker_judith = Location("Judith's Locker", background="school_locker_judith_day", parents=L_school_lefthallway, locked=True)
L_school_artclassroom = Location("Art Classroom", background="school_art_day", parents=L_school_lefthallway)
L_school_utilitycloset = Location("Utility Closet", background="", parents=L_school_lefthallway, locked=True) # Not a reachable location yet so no background
#locker room children
L_school_shower = Location("Boy's Locker Shower", background="school_lockershowers_day", parents=L_school_boysroom)
L_school_stall = Location("Bathroom Stall", background="school_locker_room_broken_stall", parents=L_school_girlsroom)
#right hallway children
L_school_assemblyhall = Location("Assembly Hall", background="school_assembly_hall_day", parents=L_school_righthallway)
L_school_bridgetoffice = Location("Coach Bridget's Office", background="school_gym_office_day", parents=L_school_righthallway)
L_school_locker_annie = Location("Annie's Locker", background="school_locker_annie_day", parents=L_school_righthallway, locked=True)
L_school_locker_eve = Location("Eve's Locker", background="school_locker_eve_day", parents=L_school_righthallway, locked=True)
L_school_locker_dexter = Location("Dexter's Locker", background="school_locker_dexter_day", parents=L_school_righthallway, locked=True)
L_school_locker_erik = Location("Erik's Locker", background="school_locker_erik_day", parents=L_school_righthallway, locked=True)
L_school_locker_kevin = Location("Kevin's Locker", background="school_locker_kevin_day", parents=L_school_righthallway, locked=True)
L_school_locker_ronda = Location("Ronda's Locker", background="school_locker_ronda_day", parents=L_school_righthallway, locked=True)
L_school_locker_mia = Location("Mia's Locker", background="school_locker_mia_day", parents=L_school_righthallway, locked=True)
#2nd floor children
L_school_computerlab = Location("Computer Lab", background="school_computer_day", parents=L_school_floor2)
L_school_cafeteria = Location("Cafeteria", background="school_cafeteria_day", parents=L_school_floor2)
L_school_teacherslounge = Location("Teacher's Lounge", background="school_lounge_day", parents=L_school_floor2)
L_school_floor3 = Location("School Third Floor", background="school_third_day", parents=L_school_floor2)
#3rd floor children
L_school_bissetteoffice = Location("Mrs Bissette's Office", background="school_office1_day", parents=L_school_floor3)
L_school_dewittoffice = Location("Mrs Dewitt's Office", background="school_office2_day", parents=L_school_floor3)
L_school_rossoffice = Location("Mrs Ross' Office", background="school_office3_day", parents=L_school_floor3)
L_school_okitaoffice = Location("Mrs Okita's Office", background="school_office4_day", parents=L_school_floor3)
L_school_smithoffice = Location("Principal Smith's Office", background="school_office_day", parents=L_school_floor3)

###DIANE'S HOUSE###
L_diane_yard = Location("Diane's Front Yard", unlock_popup="unlock15", background="diane_front", parents=L_map, locked=True)
L_diane_garden = Location("Diane's Garden", background="diane_garden", parents=L_diane_yard)
L_diane_home = Location("Diane's Lobby", background="diane_entrance", parents=L_diane_yard, locked=True, label="dianelobby_dialogue")
L_diane_kitchen = Location("Diane's Kitchen", background="diane_kitchen", parents=[L_diane_garden, L_diane_home], locked=True, label="dianes_kitchen_dialogue")
L_diane_bedroom = Location("Diane's Bedroom", background="diane_bedroom", parents=L_diane_home)
L_diane_shed = Location("Diane's Shed", background="diane_shed01", parents=L_diane_garden, locked=True, label="shed")
L_church_graveyard = Location("Church Graveyard", background="church_graveyard", parents=L_diane_garden)

###DIANE'S BARN###
L_diane_barn_building = Location("Diane's Barn Building", background="barn_build_frontyard", parents=L_map)
L_diane_barn = Location("Diane's Barn", unlock_popup="popup_diane_barn", background="barn_frontyard", parents=L_map, locked=True)
L_diane_barn_interior = Location("Diane's Barn Interior", background="barn", parents=L_diane_barn)
L_diane_barn_garden = Location("Diane's Barn Garden", background="barn_garden", parents=L_diane_barn)

###MC'S HOUSE###
L_home = Location("Home Front", background="home_front", parents=L_map)
L_home_mailbox = Location("Mailbox", background="mailbox_player", parents=L_home)
L_home_garage = Location("Garage", background="home_garage", parents=L_home)
L_home_car = Location("Car Engine", background="home_garage_car", parents=L_home_garage)
L_home_entrance = Location("Entrance", background="home_entrance", parents=L_home)
L_home_kitchen = Location("Kitchen", background="home_kitchen", parents=L_home_entrance)
L_home_diningroom = Location("Dining Room", background="home_diningroom", parents=L_home_kitchen)
L_home_backyard = Location("Backyard", background="home_backyard", parents=L_home_diningroom)
L_home_livingroom = Location("Living Room", background="home_livingroom", parents=L_home_entrance)
L_home_basement = Location("Basement", background="home_basement", parents=L_home_livingroom)
L_home_mombedroom = Location("Master Bedroom", background="home_debbiebedroom", parents=L_home_livingroom, locked=True)
L_home_hallway = Location("Hallway", background="home_hallway", parents=L_home_entrance)
L_home_shower = Location("Shower", background="home_shower_02", parents=L_home_hallway)
L_home_attic = Location("Attic", background="home_attic", parents=L_home_hallway, locked=True)
L_home_sisbedroom = Location("Upstairs Bedroom", background="home_jennybedroom", parents=L_home_hallway)
L_home_bedroom = Location("Bedroom", background="home_bedroom", parents=[L_home_hallway, L_map])

###ERIK'S HOUSE###
L_erikhouse = Location("Erik's House", unlock_popup="unlock12", background="erik_house", parents=L_map, locked=True)
L_erikhouse_mailbox = Location("Erik's Mailbox", background="mailbox_erik", parents=L_erikhouse)
L_erikhouse_backyard = Location("Erik's Backyard", background="erik_house_backyard", parents=L_erikhouse)
L_erikhouse_entrance = Location("Erik's House Entrance", background="erik_house_inside", parents=[L_erikhouse, L_erikhouse_backyard])
L_erikhouse_basement = Location("Erik's Basement", background="erik_basement01", parents=L_erikhouse_entrance)
L_erikhouse_basement_backroom = Location("Erik's Basement Backroom", background="erik_basement_back", parents=L_erikhouse_basement)
L_erikhouse_basement_backroom_cabinet = Location("Erik's Basement Backroom Cabinet", background="erik_basement_aquarium", parents=L_erikhouse_basement_backroom)
L_erikhouse_erikroom = Location("Erik's Room", background="erik_house_bedroom", parents=L_erikhouse_entrance)
L_erikhouse_erikunderbed = Location("Under Erik's Bed", background="erik_house_bedroom_under", parents=L_erikhouse_erikroom) #- needed for .15?
L_erikhouse_mrsjroom = Location("Mrs Johnson's Room", background="erik_house_upstairs", parents=L_erikhouse_entrance)

###MIA'S HOUSE###
L_miahouse = Location("Mia's House", unlock_popup="unlock1", background="mia", parents=L_map, locked=True)
L_miahouse_mailbox = Location("Mia's Mailbox", background="mailbox_mia", parents=L_miahouse)
L_miahouse_entrance = Location("Mia's House Entrance", background="mia_house", parents=L_miahouse)
L_miahouse_upstairs = Location("Mia's House Upstairs", background="mia_house_upstairs", parents=L_miahouse_entrance)
L_miahouse_miaroom = Location("Mia's Bedroom", background="mia_bedroom", parents=L_miahouse_upstairs)
L_miahouse_helensbedroom = Location("Helen's Bedroom", background="mia_house_helen", parents=L_miahouse_upstairs)
L_miahouse_helensstatue = Location("Helen's Statue", background="mia_house_statue", parents=L_miahouse_helensbedroom) #- needed?
L_miahouse_haroldsoffice = Location("Harold's House Office", background="mia_house_office", parents=L_miahouse_upstairs)
L_miahouse_lockedroom = Location("Helen's Locked Room", background="mia_house_locked", parents=L_miahouse_upstairs)

###BEACH###
L_beach = Location("Beach", unlock_popup="unlock48", background="beach", parents=L_map, locked=True)
L_beach_water = Location("Beach Water", background="beach_water", parents=L_beach)
L_beach_showers = Location("Beach Showers", background="beach_shower", parents=L_beach_water)
L_beach_cabin = Location("Beach Cabin", background="beach_cabin", parents=L_beach_water)
L_beach_tower = Location("Beach Tower", background="beach_tower", parents=L_beach)
L_beach_island = Location("Beach Island", background="beach_island", parents=L_beach)
L_beach_island_chest = Location("Treasure Chest", background="beach_treasure", parents=L_beach_island)# - required? in hide/backgrounds not images/backgrounds

###CHURCH###
L_church_front = Location("Church Front", unlock_popup="unlock30", background="church_outside", parents=L_map, locked=True)
L_church = Location("Church", background="church", parents=L_church_front)
L_church_stairs = Location("Church Stairs", background="church_stairs", parents=L_church)
L_church_bell = Location("Church Cloister Bell", background="church_bell", parents=L_church_stairs)
L_church_bell_closeup = Location("Church Bell Closeup", background="church_bell_closeup", parents=L_church_bell) #probably not needed, in hide/backgrounds not images/backgrounds
L_church_angelica = Location("Angelica's Room", background="church_nun", parents=L_church_stairs)

###FOREST###
L_forest = Location("Forest", unlock_popup="unlock42", background="forest", parents=L_map, locked=True)
L_forest_shrine = Location("Forest Shrine", background="forest_puzzle", parents=L_forest)# - required? _day and _night in hide/backgrounds not images/backgrounds
L_waterfall = Location("Waterfall", background="forest_waterfall", parents=L_forest)
L_cave = Location("Cave", background="forest_cave", parents=L_waterfall)

###GYM###
L_gym_front = Location("Gym Front", unlock_popup="unlock3", background="gym_front", parents=L_map, locked=True)
L_gym = Location("Gym", background="gym", parents=L_gym_front)
L_yoga_room = Location("Yoga Room", background="gym_yoga", parents=L_gym)

###MALL###
L_mall = Location("Mall", unlock_popup="unlock16", background="mall", parents=L_map, locked=True)
L_movie_theatre = Location("Movie Theatre", background="movie_lobby", parents=L_mall)
L_mall_toilets = Location("Mall Toilets", background="mall_washroom", parents=L_mall)
L_comicstore = Location("Comic Store", background="comic", parents=L_mall)
L_consumr = Location("Consumr", background="consumr", parents=L_mall)
L_mall_floor2 = Location("Mall Second Floor", background="mall_upstairs", parents=L_mall)
L_mall_photobooth = Location("Mall Photo Booth", background="mall_upstairs_booth", parents=L_mall_floor2)
L_cupid = Location("Cupid", background="mall_cupid", parents=L_mall_floor2)
L_cupid_dressroom = Location("Cupid Dressingroom", background="mall_cupid_closeup_stall", parents=L_cupid)
L_cupid_necklace = Location("Cupid Necklace Display", background="", parents=L_cupid)# - not a separate location/screen ingame currently, no background exists, will probably be a UI element instead
L_pink = Location("Pink", background="pink", parents=L_mall_floor2)

###DONUT SHOP###
L_donutshop = Location("Donut Shop", unlock_popup="unlock50", background="donut", parents=L_map, locked=True)
L_donutshop_interior = Location("Donut Shop Interior", background="donut_inside", parents=L_donutshop)

###PIZZERIA###
L_pizzeria_exterior = Location("Pizzeria Exterior", unlock_popup="unlockpizza", background="pizza_outside", parents=L_map, locked=True)
L_pizzeria_interior = Location("Pizzeria Interior", background="pizza", parents=L_pizzeria_exterior)
L_pizzeria_kitchen = Location("Pizzeria Kitchen", background="pizza_kitchen", parents=L_pizzeria_interior)
L_pizzeria_storage = Location("Pizzeria Storage", background="pizza_storage", parents=L_pizzeria_kitchen)

###TRAILER PARK###
L_trailerpark = Location("Trailer Park", unlock_popup="unlock39", background="trailer_park", parents=L_map, locked=True)
L_trailer = Location("Trailer", background="trailer", parents=L_trailerpark)
L_trailer_shack = Location("Shack", background="trailer_shack", parents=L_trailerpark)
L_trailer_tractor = Location("Tractor", background="trailer_tractor", parents=L_trailerpark)
L_trailer_shack_interior = Location("Shack Interior", background="trailer_shack_inside", parents=L_trailer_shack, locked=True)
L_trailer_interior = Location("Trailer Interior", background="trailer_interior", parents=L_trailerpark)
L_trailer_bedroom = Location("Trailer Bedroom", background="trailer_bedroom", parents=L_trailer_interior)

###TREEHOUSE###
L_treehouse = Location("Treehouse", unlock_popup="unlock46", background="treehouse", parents=L_map, locked=True)
L_treehouse_closeup = Location("Treehouse Closeup", background="treehouse_closeup", parents=L_treehouse)
L_treehouse_interior = Location("Treehouse Interior", background="treehouse_inside", parents=L_treehouse_closeup)

###POLICE STATION###
L_police_lobby = Location("Police Lobby", unlock_popup="unlock32", background="police_lobby", parents=L_map, locked=True)
L_police_office = Location("Police Office", background="police_office", parents=L_police_lobby)
L_police_basement = Location("Police Basement", background="police_basement", parents=L_police_lobby)

###HOSPITAL###
L_hospital = Location("Hospital", unlock_popup="unlock40", background="hospital_first", parents=L_map, locked=True)
L_hospital_keystorage = Location("Hospital Key Storage", background="hospital_box", parents=L_hospital) #- not sure if this is needed as well?
L_hospital_floor2 = Location("Hospital 2nd Floor", background="hospital_second", parents=L_hospital)
L_hospital_floor3 = Location("Hospital 3rd Floor", background="hospital_third", parents=L_hospital, locked=True)
L_hospital_lab = Location("Hospital Laboratory", background= "hospital_lab", parents=L_hospital_floor3)
L_hospital_elevator = Location("Hospital Elevator", background="hospital_elevator", parents=[L_hospital, L_hospital_floor2])
L_hospital_room = Location("Hospital 2nd Floor Room", background="hospital_room", parents=L_hospital_floor2)
L_hospital_room_bathroom = Location("Hospital 2nd Floor Bathroom", background="hospital_bathroom", parents=L_hospital_room)
L_hospital_storageroom = Location("Hospital Storage Room", background="hospital_storage", parents=L_hospital_floor2)
L_hospital_storagecabinet = Location("Hospital Storage Cabinet", background="hospital_cabinet", parents=L_hospital_storageroom)

###LIBRARY###
L_library_front = Location("Library Front", unlock_popup="unlock5", background="library_front", parents=L_map, locked=True)
L_library = Location("Library", background="library", parents=L_library_front)
L_library_bookshelf = Location("Library Bookshelf", background="library_shelf", parents=L_library)
L_library_backroom = Location("Library Backroom", background="library_backroom01", parents=L_library)
L_library_meetingroom = Location("Library Meeting Room", background="library_meeting", parents=L_library) # No blur

###PARK###
L_park = Location("Park", unlock_popup="unlock2", background="park", parents=L_map, locked=True)
L_park_fountain = Location("Park Fountain", background="park_fountain", parents=L_park)
L_park_bushes = Location("Park Bushes", background="park_bushes", parents=L_park)
L_park_bushesbag = Location("Park Bushes Bag", background="park_bag", parents=L_park_bushes)

###TATTOO PARLOR###
L_tattooparlor = Location("Tattoo Parlor", unlock_popup="unlock47", background="tattoo", parents=L_map, locked=True)
L_tattooparlor_interior = Location("Tattoo Parlor Interior", background="tattoo_indoor", parents=L_tattooparlor)

###DEALERSHIP###
L_dealership_front = Location("Dealership Front", unlock_popup="unlockdealership", background="dealership", parents=L_map, locked=True)
L_dealership = Location("Dealership", background="dealership_indoor", parents=L_dealership_front)

###BEACH HOUSE###
L_beachhouse_front = Location("Beach House Front", background="beach_house", parents=L_map, locked=True)
L_beachhouse_entrance = Location("Beach House Entrance", background="beach_house_entrance", parents=L_beachhouse_front)
L_beachhouse_bedroom = Location("Beach House Bedroom", background="beach_house_bedroom", parents=L_beachhouse_entrance)
L_beachhouse_patio = Location("Beach House Patio", background="beach_house_patio", parents=L_beachhouse_bedroom)

###SMITH'S HOUSE###
L_smith_front = Location("Smith's Frontyard", unlock_popup="unlocksmith", background="smith_frontyard", parents=L_map, locked=True)
L_smith_entrance = Location("Smith's Entrance", background="smith_entrance", parents=L_smith_front)
L_smith_hallway = Location("Smith's Hallway", background="smith_hallway", parents=L_smith_entrance)
L_smith_bedroom = Location("Smith's Bedroom", background="smith_bedroom", parents=[L_smith_hallway, L_smith_front])
L_smith_basement = Location("Smith's Basement", background="smith_basement", parents=L_smith_entrance, locked=True)

###ANNIE'S HOUSE###
L_annie_front = Location("Annie's House Front", background="annie_frontyard", parents=L_map, locked=True, unlock_popup="unlockannie")
L_annie_livingroom = Location("Annie's House Livingroom", background="annie_livingroom", parents=L_annie_front)
L_annie_daycare = Location("Annie's House Daycare", background="annie_daycare", parents=L_annie_front)

###BOAT###
L_boat_bridge = Location("Boat Bridge", background="boat", parents=L_map, locked=True)
L_boat_cabin = Location("Boat Cabin", background="boat_interior", parents=L_boat_bridge)

###RUMP HOUSE###
L_rump_front = Location("Mayor Rump's Frontyard", background="rump_front", parents=L_map, locked=True)

###SINGLE LOCATIONS WITH NO CHILDREN###
L_bank = Location("Bank", unlock_popup="unlock6", background="bank", parents=L_map, locked=True)
L_basketball_court = Location("Basketball Court", unlock_popup="popup_basketball", background="basketball", parents=L_map, locked=True)
L_beach_house = Location("Beach House", background = "beach_house", parents = L_map)
L_hill = Location("Hill", unlock_popup="unlock49", background="hill", parents=L_map, locked=True)
L_lair = Location("Lair", unlock_popup="popup_lair", background="lair", parents=L_map, locked=True) # in hide/backgrounds not images/backgrounds
L_pier = Location("Pier", unlock_popup="unlockpier", background="pier", parents=L_map, locked=True)
L_pool = Location("Pool", unlock_popup="unlock4", background="pool", parents=L_map, locked=True)
L_warehouse = Location("Warehouse", unlock_popup="popup_warehouse", background="warehouse", parents=L_map, locked=True)

print("loop")
print([l for l in Location.get_instances()])
print(globals())

locs = [v for k, v in globals().items() if k.startswith("L_")]

folders=("backgrounds", "doors", "item_buttons")

for v in locs:
    path = os.getcwd() + "\\" + v.formatted_name
    print(path)
    mkdir(path)
    for f in folders:
        mkdir(path + "\\" + f)
