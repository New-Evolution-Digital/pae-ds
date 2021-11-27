import random
import pandas as pd
import numpy as np
import string
from shapely.geometry import Point
from webapp.utilities.map_info.json_map_data import polys, county_names, scale, refs

VIN_Bits = list(string.ascii_lowercase) + ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
or_regions = """Agate Flat
Beaver Basin
Camp Creek
East Fork Beaver Creek
Edge Creek
Fall Creek
Goose Lake
Klamath Strait Drain
Mallard Gulch
Monkey Creek Ridge
North Fork Willow Creek
Raymond Gulch
Rock Creek
Rocky Gulch
Salt Creek
Beaver Creek
Lake Miller
Rowdy Creek
Stein Gulch
West Fork Althouse Creek
West Fork Beaver Creek
Pacific Ocean
Fourmile Creek
Coast Ranges
Blue Creek
North Fork Diamond Creek
Lone Pine Ridge
Thompson Creek
Six Rivers National Forest
Modoc National Forest
Barrington Creek
Bean Gulch
Bear Creek
Bee Flat
Bill Fruit Trail
Camp Gulch
City Gulch
Cow Creek
Diamond Creek
Dry Creek Rim
East Branch Lost River
East Fork Illinois River
East Fork Indian Creek
East Fork Ridge
Elliott Creek
Gillum Creek
Green Creek
Grouse Creek
Hatfield
Jenny Creek
Long Prairie Creek
Low Gap Trail
Lower Klamath National Wildlife Refuge
Nicks Spring
North Fork Dunn Creek
North Fork Smith River
Packers Creek
Pine Flat Mountain
Russell Canyon
Silver Fork
Slide Creek
Cottonwood Creek
Elk Creek
Elk Valley
Hutton Creek
Klamath River
North Hungry Creek
P1 Canal
Renner Lake
Rock Creek
Steve Fork Trail
Thompson Ridge
Traverse Creek
Two Bit Gulch
Whisky Creek
White Lake
Wimer Creek
Siskiyou Mountains
Cattle Creek
Central Alkali Drain
Cherry Creek
Chicken Creek
Cow Creek
Field Creek
Five and Seventenths Canal
Five Pine Rapids
Hooker Creek
Horse Creek
Imbler Drain
Little Poison Creek
Lone Tree Creek
Middle Fork Owyhee River
North Fork Owyhee River
Owyhee Mountains
Palmer Creek
Pleasant Valley
Pole Creek
Pole Creek Breaks
Purser Ridge
Schoolhouse Gulch
Soldier Creek
South Canal
Squaw Creek
Stove Creek
Succor Creek
Tent Creek
Trout Creek
Whiskey Creek
Wolf Creek Rapids
Highrange Rapids
Cottonwood Rapids
Big Sulphur Rapids
Brownlee Reservoir
Copper Creek Rapids
Davis Creek Rapids
Deep Creek Rapids
Dry Creek
Dug Creek Rapids
Hells Canyon
McBride Creek
Robinson Gulch Rapids
Roland Bar Rapids
Upper Pleasant Valley Rapids
Warm Springs Rapids
Zigzag Rapids
Nez Perce National Historical Park
Snake Wild and Scenic River
Coyote Creek
Squaw Creek Vee
Strode Basin
Sage Creek
Oxbow Reservoir
The Oxbow
Farewell Bend
Deer Flat National Wildlife Refuge
Payette National Forest
Nez Perce National Forest
Lewis and Clark National Historic Trail
Bilk Creek Mountains
Cold Creek
Coleman Creek
Cottonwood Creek
Crow Creek
Hawksy Walksy
Horse Creek
Long Canyon
Long Draw
McDermitt Creek
North Rock Springs Table
Pueblo Slough
Rincon Creek
State Line Canyon
Wilder Creek
Sage Hen Hills
The Slough
Twin Peak
Mosquito Mountain
Coleman Valley
Riser Creek
South Fork Cottonwood Creek
Big Spring Table
Antelope Flat
Long Meadow Creek
Deer Creek
East Fork Quinn River
Fort McDermitt Indian Reservation
Kings River
Sage Creek
Humboldt National Forest
Saint Martin Creek
Sheldon National Wildlife Refuge
Mc Dermitt Post Office
Marion Forks Forest Service Station
Marion Forks Recreation Site
Switch Back Creek
Flunky Creek
Dearborn Island
Gold Basin Springs
Cedar Camp
Pollard Gulch
Riverside Spring
Tarter Spring
Sage Hen Flat
Guyer Gulch
Sparta Cemetery
Deer Flats
Gulch Reservoir
Densley Reservoir
Serpentine Gulch
Spring Gulch
De Witt Well
Stauffer Reservoir
Stauffer Well
Sand Hollow
Mislatnah Peak
Jacks Camp
Humboldt Spring
Upper Mislatnah Prairie
Six Mile Meadow
Wilson Creek
Bolivar Mine
Crissey Airport (historical)
Rogue River Ranch
Half Moon Riffle
Tucker Flat
Narrows
Coffeepot
Paradise Riffle
Gleason Bar
Tichenor Riffle
Camp Tacoma
Mule Creek Cemetery
Van Pelt Cemetery
Pioneer Cemetery
McVay Rock
Tuttle Creek
Rimrock Spring
Babyfoot Mine
Cold Spring
Nuthatch Springs
McQuinn Strip (historical)
Palouse Slough
Silver Fork Basin
Dutchman Spring
Squaw Creek Gap
Kenney Meadows
Ash Creek
Fourbit Ford Recreation Site
Mud Spring
Mulligan Bay
Mulligan Bay Campground (historical)
Mingo Gap
Hanley Gap
Buck Gulch
Jackson Recreation Site
Placer Recreation Site
Flumet Flat Recreation Site
Ash Flat
Empire Cemetery
Pole Creek
Shaw Creek
Parker Creek
Thomas Cavender Reservoir
Tip Top Lookout Tower
Slide Creek
Potter Ditch
Oriental Creek Recreation Site
Lake County Fairgrounds
Jay Bird Mine
Pitch Log Spring
Mineral Prairie
Alberg Mine
Sasser Landing Strip (historical)
Nickel Creek
Foster - Illahe Cemetery
Illahe Lodge
Widow Meadow
Morning Creek
Woodward Recreation Site
Tollgate
Reservoir Number Two (historical)
Reservoir Number One (historical)
Stemple Creek
Emerick Cemetery
East Fork Falls
Last Chance Mine
Queen of the West Mine
Zollman and Wells Mine
Lick Creek Recreation Site
Target Spring
Wayside Spring
Densley Spring
Cave Creek
Greenhorn Cemetery
Mosquito Creek
Bear Spring
Spring Creek
Suttle Lake Forest Service Station
Columbia Gorge Work Center
Hunters Camp
Ridge Camp
Deadwood Camp
Summer Lake Cemetery
Officer Butte
Road Canyon
Road Mountain
Winans
Chamberlin Ditch
Union Cemetery
Wisnor Place
Bull Creek Spring
Thursday Spring
Frankies Cabin Spring
Green Mountain
Little Funny Butte
Brushy Creek
Magpie Spring
Catherine Creek Cabin
Granite Lake
Fox Prairie
Rugg Cabin
Horse Creek
South Fork Long Branch
Hanley North Canal
Hanley South Canal
Slinger Rock
Poverty Hill
West Fork Lake Creek
Warner Family Cemetery
Tie Camp Spring
Case Spring
Meadow Brooks Falls
Brandenburg Reservoir
Ditch Creek
Roberts Mine
McCalpine Meadow
Lemon Cabin
Sunrise Spring
Homestead Spring
Link Lake
Hell Creek
Satan Creek
Fall River Fish Hatchery Airport (historical)
Obsidian Falls
Squeeksville Spring
Bear Valley Lake
Minto Lake
Camp Creek Reservoir
Long Prairie Slough
Cook Well
Jack Reservoir
Kitteredge Reservoir
Last Cabin Spring
Mud Spring
Uncle Tom Well
Pon Well
Looney Spring
Kline Spring
Elkhorn Microwave Station
Long Meadow
Modesty Spring
Guernsey Pond
Skull Creek Reservoir
South Bullrun Creek
Antone Burn
Forseer Spring
Sand Creek
Fox Valley
Yellowjacket Field
Chalk Reservoir
South Fork Canal
South Fork Dam
Manley Reservoir
Daley Creek Dam
Danley Creek Canal
Deadwood Prairie
Breiten Guard Station
Porcupine Flat
The Pyramid
West Reservoir
Squaw Butte Well
Ludi Well
South Reservoir
The Blowouts
Box Canyon Reservoir
Marble Creek Recreation Site
Encina
Coyote Hills
Mount Harris Lookout Tower (historical)
Moody Ditch
River Recreation Site
Johnson Rock Lookout Tower
Park Gulch
Blue Spring
Strip Spring
Skid Seep
Wildhorse Spring
Sedge Reservoir
Sedge Two Reservoir
South Fork Falls
Porcupine Reservoir
Porcupine Creek
Delore Place
Suplee Butte
Bernard Mill
Suplee Spring
Little Frazier Creek
Stump Spring
Frazier Creek
Little Fir Creek
Trail Creek
Santa Claus Spring
Wildcat Spring
Ellingson Mill
Cougar Creek
Santa Claus Stream
North Fork Clark Creek
Hamilton Cemetery
Viewpoint Reservoir
Blue Pot Spring
Hobble Spring
Hobnail Reservoir
Cayuse Reservoir
Art Reservoir
Robinson Homestead
Deer Creek Flats
Davis Creek
Davis Creek Reservoir
Frazier Recreation Site
Big Mowich Reservoir
Hardscrabble Reservoir
Negro Cabin
Elk Reservoir
Buck Spring
Fort Creek
Coyote Reservoir
Fort Reservoir
Cinnabar Flat
Greenwater Reservoir
Murray Flat
Dual Reservoir
Willow Spring
Three M Spring
Imperial Eagle Mine
Balanced Rocks
Prairie Farm Guard Station (historical)
Bridge 99
Paulina Spring
Black Crater Lake
Nye Cemetery
Nye Ditch
Prospect Power Plant
Peyton Reservoir
Payton (historical)
Davis Well
Sweek Spring
Merrill Springs
Round Spring
Leather Spring
Chambeam Ditch
Dead Horse Creek
East Side Canal
Gearhart Mountain Wilderness
Labish Center School (historical)
Morrison School (historical)
Mud Flat Creek
Big Muddy Creek
Naef (historical)
Norton Creek
Oregon Trail
Tunnel Number 6
Salt Springs Canyon
Sheep Creek
Red Waterhole
The Basin
Warm Springs Creek
Westlake Island
A and M Ridge
A Canal
A Line Canal
A P Spring
AP Well
Abbot Lake
Abernethy Creek
Abernethy Island
Abernethy Elementary School
Abert Rim
Lake Abert
Abiqua Creek
Acty Cow Camp
Acty Mountain
Acty Spring
Adair Tract State Forest
Page Creek
Adams
Adams Butte
Adams Cemetery
Adams Creek
Adams Creek
Adams Creek
Adams Creek
Adams Lake
Adams Point
Adams Elementary School
Adams Spring
Adams Spring
Lake Adams
Adel
Adel Elementary School
Adkisson Creek
Adobe Flat
Adobe Gulch
Adobe Point
Adobe Reservoir
Agate Beach
Agate Beach
Agate Desert
Agency Mountain
Agency Valley
Agency Valley Cemetery
Agency Valley Dam
Ahavai Sholom Cemetery
Ainsworth Elementary School
Ajax Gulch
Ajax Mine
Alameda
Alameda Elementary School
Albany
Albany Channel
Albany Santiam Canal
West Albany High School
Albert Lake
Albert Philippi Park
Saxton County Park
Alberta City Park
Albertson Spring
Albina Yard
Alder Branch
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek Meadow
Alder Creek Reservoir
Alder Grove School
Alder Creek Spring
Alder Creek Spring
Alder Loop Spring
Alder Mountain
Alder Spring
Alder Spring
Alder Spring
Alder Springs
Alderwood State Park
Aldrich Park
Aldrich Point
Alex Small Creek
Alex Spring Reservoir
Alexander Creek
Alexander Creek
Alexander School
Alfalfa
Alford Cemetery
Alford Gulch
Alford Pond
Alforja Lake
Alger Lake
Algoma Incline
Alkali Canyon
Alkali Canyon
Alkali Creek
Alkali Draw Reservoir
Alkali Flat
Alkali Flat Corrals
Alkali Lake
Alkali Lake
Alkali Lake Station
Alkali School (historical)
Alkali Spring
Alkali Spring
Alkali Spring
Alkali Springs
Alkali Springs
All Saints School
Allegany
Allegany School (historical)
Allen Canyon
Allen Creek
Allen Creek
Allen Ditch
Allen Drain
Allen Reservoir
Allen Ridge
Allison Bar
Allison Canyon
Allison Creek
Allotment Four Reservoir
Allotment Reservoir Number Three
Allphin Cemetery
Alma
Aloha
International School of Beaverton
Alpine
Alpine Cemetery
Alpine Junction
Altamont
Altnow Gap
Altnow Gap Reservoir
Altnow Ranch
Altnow Spring
Alvey Substation
Alvord Creek
Alvord Desert
Alvord Hot Springs
Alvord Lake
Alvord Peak
Aman Ranch Placer
Amazon Creek
Amazon Creek Diversion Channel
Amazon Mine
Amazon City Park
Amberson Creek
Amelia Butte
American Bottom
American Legion Cemetery
Ames Cemetery
Ames Creek
Amine Canyon
Amine Peak
Amity Creek
Ammunition Point
Anaconda Mine
Analulu Mine
Anawalt Drain
Anawalt Lake Ranch
Anawalt Reservoir
Anderson Cabin
Anderson Camp
Anderson Creek
Anderson Creek
Anderson Creek
Anderson Creek
Anderson Creek
Anderson Creek
Anderson Gulch
Anderson Lake
Anderson Mountain
Anderson Mountain
Anderson Ranch
Anderson Reservoir
Anderson Ridge Trail
Anderson Spring
Anderson Valley
Andrews
Andrews Creek
Andrews Creek
Andy Wilson Reservoir
Angel Camp
Angel Point
Angel Spring
Angel Wells Reservoir
Angell Basin
Angell Peak
Angie Canyon
Angie Potholes
Angle Reservoir
Ankeny Bottom
Ankeny Hill
Ankeny National Wildlife Refuge
Ankle Creek
Comstock Cemetery
Anna Drain County Park
Annex Canal
Annex Elementary School
Annies Reservoir
Ant Flat
Ant Hill
Antelope
Antelope Butte
Antelope Cemetery
Antelope Creek
Antelope Creek
Antelope Creek
Antelope Creek
Antelope Creek
Antelope Feeder Canal
Antelope Flat
Deer Flat
Antelope Flat
Antelope Flat
Antelope Flat
Antelope Flat Reservoir Number One
Antelope Flat Reservoir Number Two
Antelope Lake
Antelope Lake
Antelope Peak
Antelope Ranch
Antelope Reservoir
Antelope Reservoir
Antelope Reservoir
Antelope Reservoir
Antelope School
Antelope Spring
Antelope Spring
Antelope Spring
Antelope Spring
Antelope Spring
Antelope Spring
Antelope Spring
Antelope Spring Reservoir
Antelope Springs
Antelope Swale
Antelope Swale Reservoir
Antelope Swale Reservoir
Antelope Swale Spring
Antelope Valley
Antelope Waterhole
Anthony Butte
Anthony Creek
Anthony Lake
Anthony Lakes
Anthony Springs
Antler Springs
Antoken Creek
Antone Creek
Antone Creek
Anunde Island
Apiary
Apilton Creek
Apple Valley
Applegate
Applegate Family Cemetery
Applegate Elementary School (historical)
Applegate Spring
Aquatic Gardens
Arago
Arbor Lodge City Park
Arcade Cemetery
Arcadia Beach
Arcadia Lake
Arch Cape
Arch Cape
Arch Cape Creek
Arch Rock
Archer Cemetery
Archibald Creek
Argonaut Mine
Argue Creek
Arkansas Flat
Arkansas Reservoir
Arkansas Spring
Armitage County Park
Armstead Memorial
Armstrong Canyon
Armstrong Canyon
Armstrong Cemetery
Arock
Arock Diversion Dam
Arrastra Butte
Arrastra Canyon
Arrien Reservoir
Arrien Reservoir Number Six
Arritola Ranch
Sow Creek
Arrow Lake
Arsenic Canyon
Arthur Jones Creek
Asbahr Lake
Asbury Creek
Portland Arthur Academy Charter School
Ascot City Park
Ash
Ash Creek
Ash Island
Ash Slough
Ash Valley
Ashby Creek
Ashwood
Asker Creek
Aspen Cabin
Aspen Creek
Aspen Creek
Aspen Reservoir
Aspen Reservoir
Aspen Spring
Astoria Column
Astor Elementary School
Astoria
Astoria Air Marine Service
Astoria Megler Ferry (historical)
Athena Cemetery
Athey Creek
Atkins Butte
Atkinson Elementary School
Atterbury Reservoir
Auburn Creek
Auburn Elementary School
Auger Creek
Augur Creek
Augur Creek Meadows
August Meyer Gulch
Augustine Canyon
Aumsville
Aumsville Cemetery
Aurelia Mine
Aurora
Ausmus Canal
Adair Point
Avenue Creek
Averill Lake
Avery Creek
Avery Gulch
Avery Reservoir
Avery Spring
Awbrey Falls
Awbrey City Park
Axe Creek
Axehandle Butte
Axehandle Mine
Axehandle Ridge
Axehandle Spring
Axle Canyon
Ayers Canyon
Ayers Creek
Ayers Creek
Azalea
B Canal
B K Corral
Babes Canyon
Babes Canyon Spring
Baboon Creek
Baby Mine
Baca Lake
Bachelor Creek
Bachelor Creek
Bachelor Flat School (historical)
Bachelor Spring
Bacher Creek
Back Creek
Backbone Ridge
Bacon Camp
Bacon Camp Draw
Badger Butte
Badger Canyon
Badger Creek
Badger Creek
Badger Flat
Badger Hole Flat
Badger Mountain
Badger Reservoir
Badger Spring
Badger Spring
Badger Spring
Badsky Pond
Bailey Butte
Bailey Hill
Bailey Hill Instructional Center
Bailey School (historical)
Baiseley Creek
Bakeoven Creek
Baker Cabin
Baker Canyon
Baker Canyon
Baker Creek
Baker Creek
Baker Creek
Baker Creek
Baker Flat
Baker Island
Baker Lake
Baker Mine
Baker Pass
Baker Point
Baker Ranch
Bakers Bridge
Balanced Rocks
Balancing Rock
Balch Canyon
Bald Barney Creek
Bald Butte
Bald Butte
Bald Butte Spring
Bald Gap
Bald Headed Camp
Bald Hill
Bald Hill
Bald Mountain
Bald Mountain
Bald Mountain
Bald Mountain
Bald Mountain
Bald Mountain
Bald Mountain
Bald Mountain
Bald Mountain Mine
Bald Mountain Reservoir
Bald Mountain Spring
Bald Peak
Bald Peak State Park
Scott Mountain
Bald Peter
Bald Peter Creek
Bald Point
Bald Ridge
Baldwin Creek
Baldwin Gulch
Baldy
Baldy
Baldy
Baldy Butte
Baldy Creek
Baldy Lake
Baldy Mountain
Baldy Ridge
Bales Canyon
Bales Creek
Ball School (historical)
Ballard Creek
Bullet Spring
Ballew Lake
Ballew Lake Spring
Balls Lake
Bally Camp
Bally Canyon
Bally Mountain
Bally Mountain Spring
Balm Creek
Balm Hollow
Baltimore Creek
Baltimore Rock
Bandon
Bandon Reservoir
Bandon State Park
Banks Creek
Banks Ditch
Bannock Corral Spring
Bannock Gulch
Bannock Gulch Spring
Bannock Ridge
Bannock Spring
Bar Creek
Bar Creek
Bar Heart Reservoir
Barber Canyon
Barber Flat
Barber Pole Butte
Barber Reservoir
Barclay School (historical)
Bare Flat
Bargfeld Creek
Bark Shanty Creek
Bark Shanty Creek
Barlow Point Channel
Barlow Cutoff
Barlow Reservoir
Barlow School (historical)
Barlow Well
Barnes Creek
Barnes Elementary School
Barnes Valley
Barnes Valley Creek
Barnes Valley Guard Station
Barnes Yard
Barnet Canyon
Barney Reservoir
Barney Waterhole
Barnum Canyon
Barrel Spring
Barrel Spring
Barrel Spring
Barrel Spring
Barrett Creek
Barren Basin Reservoir
Barren Valley
Barrett Creek
Barrett Creek
Barrett Creek
Barrett Slough
Barry Cabin
Barry Ranch
Barry Ranch
Barry Spring
Barth Falls
Bartlett
Bartlett Cemetery
Bartlett Landing
Bartlett Mountain
Barton
Barton Bridge
Barton County Park
Barton Lake
Barton Lake Well
Barton Park (historical)
Barton Ranch
Barton School (historical)
Barview State Wayside (historical)
Bas Reservoir
Basche Ditch
Basco Spring Reservoir
Baseline Ridge
Tualatin Valley Junior Academy
Basey Canyon
Bashaw Creek
Basin Creek
Basin Creek
Basin Creek
Basin Creek
Basin Gulch
Basin Mine
Basin Spring
Basque Canyon
Basque Creek
Basque Flat
Basque Flat Well
Basque Pit Reservoir
Bass Haines Place
Bassey Creek
Bastard Creek
Batch Lake
Bateman Creek
Bath Canyon
Bathtub Creek
Bathtub Spring
Bathtub Spring
Battle Creek
Battle Creek
Battle Creek
Battle Creek
Battle Creek
Battle Creek
Battle Creek Slough
Battleground Buttes
Batts Camp Lake
Bauer Creek
Bauers Creek
Baughaman Lookout
Bauman Draw
Bauman Reservoir
Baxter Creek
Baxter Creek Reservoir
Bay Horse Creek
Bay Stud Reservoir
Bayney Creek
Bazine Creek
Beach Elementary School
Beacon Number Two
Beacon Number Four
Beacon Number Five
Beagle Creek
Beagle Creek
Beals Creek
Beals Mountain
Bean Spring
Bear Branch
Bear Branch
Bear Butte
Bear Camp Creek
Bear Canyon
Bear Creek
Bear Creek
Bear Creek
Bear Pen Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek Butte
Bear Creek Cemetery
Bear Flat
Bear Flat
Bear Flat
Bear Gulch
Bear Gulch
Bear Gulch
Bear Gulch
Bear Gulch
Bear Gulch
Bear Hill
Bear Hollow
Bear Hunt Gulch
Bear Island
Bear Meadow
Bear Mountain
Bear Mountain
Bear Pan Spring
Bear Pass
Bear Ridge
Bear Ridge
Bear Ridge Well
Bear Spring
Bear Spring
Bear Valley
Bear Valley Gulch
Bear Wallow
Bear Wallow Spring
Bear Wallow Spring
Beard Canyon
Beartrap Spring
Bearwallow Spring
Bearwallow Spring
Bearway Meadow
Beatty Creek
Beatty Creek
Beatty Creek Trail
Beaty Creek
Beatys Butte
Beaumont Middle School
Beaver Acres Elementary School
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek School (historical)
Beavercreek Elementary School
Beaver Dam
Beaver Dam Picnic Ground (historical)
Beaver Eddy
Beaver Falls
Beaver Hill
Beaver Hill
Beaver Island
Beaver Lake
Beaver Lake School (historical)
Beaver Marsh
Beaver Meadow
Beaver Ridge
Beaver Slough
Beaver Slough
Beaver Spring
Beaver Tables
Beaver Valley
Beaverdam Branch
Beaverdam Buttes
Beaverdam Creek
Beaverdam Lake
Beaverdam Pond
Beaverton Creek
Beber Ranch
Bechdoldt Flat
Bechdoldt Reservoir
Becker Creek
Becker Horse Camp
Beckley
Beckley Spring
Beckley Well
Bedfield Cemetery
Bee Ranch
Beecher Flat Canyon
Beecher Flat
Beef Hollow
Beer Garden Spring
Beeres Pond
Beerman Creek
Beers Spring
Beirman Spring
Cheldelin Middle School
Belding Creek
Belfort Creek
Belieu Creek
Belknap Camp
Belknap Creek
Bell Camp Spring
Bell Canyon
Bell Creek
Bell Mountain
Bell Ridge
Belle of Baker Mine
Belle Passi School
Belle Vue Point
Bellfountain
Bellfountain Cemetery
Bellfountain County Park
Bellinger Cemetery
Bellinger Landing County Park
Bellville Sanatorium
Belshazzar Creek
Belzar Spring
Ben and Kay Dorris County Park
Ben Branch
Ben Glenn Canyon
Ben Glenn Ridge
Ben Hall Creek
Ben Odell Reservoir
Ben Point
Bench Canyon
Bench Creek
Bench Reservoir
Bench Reservoir
Benchmark Waterhole
Bend Creek
Benefiel Creek
Beneke Creek
Benham Slough
Benjamin Gulch
Benjamin Lake
Bennet Creek
Bennett Peak
Bennett Butte
Bennett Canyon
Bennett County Park
Bennett Creek
Bennett Lake
Bennett Point
Bennett Reservoir
Bennett Rock
Bens Reservoir
Bensley Flat
Benson Creek
Benson Gulch
Benson Lake
Benson Lookout
Benson Polytechnic High School
Benson Trail
Benton Mine
Bentonite Spring
Berglund Gulch
Bergsvik Creek
Berkeley City Park
Berkshire Slough
Powell Cemetery
Berlin Union Church
Berrenth Quarry
Berry Creek
Berry Creek
Berry Creek
Berry Creek Falls
Beshell Grade
Bessey Creek
Best Rock
Beth Israel Cemetery
Bethany
Bethany Pioneer Cemetery
Bethany Charter School
Lark Park
Bethel Cemetery
Bethel Creek
Bethel Elementary School
Bethel Substation
Beulah Butte
Beulah Creek
Beulah Reservoir
Beulahland School (historical)
Beverly Beach
Beverly Beach State Park
Bibby Pond
Biddle Canyon
Bieler Ranch (historical)
Bierce Creek
Big Adobe Reservoir
Big Alvord Creek
Big Baldy
Big Baldy
Big Basin
Big Basin
Big Basin
Big Basin Reservoir
Big Bedground
Big Bend
Big Bend
Big Bend School (historical)
Big Boulder Creek
Big Boulder Reservoir
Big Bridge Creek
Big Canyon
Big Canyon
Big Canyon
Big Cove
Big Cove
Big Cove Creek
Big Creek
Big Creek
Big Creek
Big Creek
Big Creek
Big Creek
Big Creek
Big Creek
Big Creek
Big Creek
Big Creek Ditch
Big Creek Spring
Big Curve Reservoir
Big Deacon Creek
Big Devil Gulch
Big Dipper Spring
Big Dry Creek
Big Eddy Park
Big Eddy Substation
Big Elk Creek
Big Elk Guard Station
Big Falls
Big Field Pit
Big Fir Creek
Big Fir Spring
Big Fish Fin
Big Flat
Big Flat
Big Granite Creek
Big Green Mountain
Big Gulch
Big Gulch
Big Hill
Big Hill
Big Hill Spring
Big Hole Canyon
Big Hole Reservoir
Big Hole Reservoir
Big Indian Creek
Big Juniper Flat
Big Lake
Big Lake Reservoir
Big Lick
Big Lookout Mountain
Big Meadow
Big Meadows
Big Mosquito Canyon
Big Mud Flat
Big Noise Creek
Big Pasture Creek
Big Pine Hollow
Big Pines
Big Pipe Spring
Big Poison Butte
Big Rattlesnake Creek
Big Rayborn Canyon
Big Red S Field
Big Reservoir
Big Ridge
Big Ridge Reservoir
Big River
Big Rock
Big Rock Creek
Big Saddle
Big Saddle
Big Saddle Canyon
Big Sage Flats
Big Service Creek
Big Slide Lode
Big Sourdough Canyon
Big Spring
Big Spring
Big Spring
Big Spring
Big Springs
Big Spring
Big Spring
Big Spring Branch
Big Spring Draw
Big Spring Reservoir
Big Springs
Big Springs Campground (historical)
Big Springs Pump
Big Stewart Canyon
Big Swale Reservoir
Big Swamp Creek
Big Swamp Creek
Big Swamp Reservoir
Big Tank Creek
Big Tip
Big Whetstone Creek
Biggs Junction
Biglow Canyon
Bigs Creek
Biley Spring
Bilger Creek
Bill Creek
Bill Lewis Creek
Bill Nye Mine
Bill Peak
Bill Spring
Bill Taber Cabin
Billfold Waterhole
Billie Creek
Bills Creek
Bills Pass
Billy Burr Lake
Billy Canyon
Billy Creek
Billy Creek
Billy Mountain
Billy Small Meadow
Bilquist Elementary School
Binder Slough
Bingham Creek
Binkey Lake
Harrison Park School
Birch Canyon
Birch Creek
Birch Creek
Birch Creek
Birch Creek
Birch Creek
Birch Creek
Birch Creek
Birch Creek
Birch Creek
Birch Creek
Birch Creek Meadow
Birch Creek Reservoir
Birch Spring
Bird Point
Birdseye Creek
Birkenfeld
Biscuit Butte
Bishop Creek
Bishop Creek
Black Bar
Black Bull Spring
Black Bull Spring
Black Bull Springs
Black Butte
Black Butte
Black Butte
Black Butte
Black Butte
Black Butte
Black Butte
Black Butte Mine
Black Butte Reservoir
Black Butte Ridge
Black Canyon
Black Canyon
Black Canyon
Black Canyon
Black Canyon
Black Canyon Camp
Black Canyon Reservoir
Black Cap
Black Creek
Black Creek
Black Lake
Black Mountain
Black Pine Spring
Black Point
Black Point Well
Black Ranch
Black Rim
Black Rim
Black Rim Dam
Black Rock
Black Rock
Black Rock
Black Rock
Black Rock
Black Rock
Black Rock Canyon
Black Rock Creek
Black Rock Spring
Oregon End Table
Black Slough
Black Snag Spring
Black Snag Springs
Black Springs
Black Springs Creek
Black Top
Black Willow Gulch
Blackberry Canyon
Blackcanyon Way
Blackhorse Canyon
Blackjack Butte
Blacklock Point
Blacksmith Canyon
Blacksmith Shop Well
Blackwell Creek
Blackwell Hill
Blackwell County Park
Blair Canyon
Blair Canyon Reservoir
Blair Creek
Blake Gulch
Blalock Canyon
Blan Cemetery
Blanco Reef
Bland Mountain Cemetery
Blattner Creek
Blaylock Canyon
Blaylock Canyon Spring
Bledsoe Canyon
Peninsula Childrens Center
Blevins Reservoir
Blind Cabin Ridge
Blind Canyon
Blind Creek
Blind Creek
Blind Gulch
Blind Slough
Blitzen
Blizzard Gap
Blizzard Ridge
Blizzard Ridge
Blocks Canyon
Blonde Spring
Blood Creek
Blooming
Blooming Cemetery
Blossom Gulch
Blossom Gulch Elementary School
Blowfly Canyon
Blowout Reservoir
Bluch Creek
Blue Buck Spring
Blue Bucket Spring
Blue Canyon
Blue Canyon
Blue Canyon Reservoir
Blue Channel Placer
Blue Creek
Blue Creek
Blue Creek
Blue Creek
Blue Creek
Blue Creek Meadows
Blue Heron Bay
Blue Hole Creek
Blue Jay Reservoir
Blue Lake
Blue Lake
Blue Lake
Blue Lake
Blue Lake Guard Station
Blue Monday Spring
Blue Mountain
Blue Mountain
Blue Mountain
Blue Mountain Community College
Blue Mountain Charter School (historical)
Blue Mountain School (historical)
Blue Reservoir
Blue Ridge
Blue Ridge Creek
Blue River
Blue River
Blue Rock
Blue Sands Canyon
Blue Sky Hotel Camp (historical)
Blue Spring
Blue Spring
Blue Spring
Blue Spring
Blue Spring Gulch
Blue Trigger Gulch
Bluejoint Ranch
Bluff Creek
Bluff Creek
Blume Zilkey Ditch
Board Corral Gulch
Board Corral Mountain
Board Corral Reservoir
Board Corral Spring
Board Creek
Board Tree Creek
Boardtree Canyon
Boot Creek
Boat Rock
Bob Creek
Bob Flat
Bobby Creek
Bobcat Reservoir
Bobcat Spring
Bobier Meadow
Bobier Slide
Bobs Creek
Bobs Lake
Bodnar Ranch
Bodnar Springs
Boeckman Creek
Boeing Well
Bog Spring
Boggs Lake
Boggy Lake
Bogus Bench
Bogus Bench Reservoir
Bogus Creek
Bogus Creek Well
Bogus Lake
Bogus Ranch
Bogus Rim
Bogus Rim Reservoir
Bohemian Spring
Boiler Bay
Boiler Bay State Park
Boiler Spring
Boiling Point (historical)
Boiling Spring
Boise-Eliot Elementary School
Bonanza
Bonanza Memorial Park
Bonanza Mine
Bond Butte
Bond Creek
Bone Canyon
Bone Creek
Bone Creek
Boner Flat
Boner Gulch
Boney Basin
Boney Canyon
Boneyard Gulch
Bonner Creek
Bonnie Falls
Bonnie Lure State Park
Book Spring
Booker Creek
Boomer Hill School
Boone Canyon
Boone Canyon
Boone Creek
Booners Creek
Booneville
Booten Creek
Booth Hill
Booth Park
Bootleg Spring
Booze Creek
Borax Lake
Borax Works
Borden Gulch
Borderline Spring
Boren Creek
Boring
Boston Horse Camp
Boswell Creek
Boswell Mountain
Boswell Spring
Bottger Creek
Bottle Creek
Bottle Creek
Rock Creek
Bottle Creek
Bottle Spring
Bottom Creek
Bolton School Park
Boughey Creek
Boulder Camp
Boulder Canyon
Boulder Corral
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek Meadows
Boulder Lake
Boulder Park Resort (historical)
Boulder Pass
Boulder Reservoir
Boulder Ridge
Boulder Springs
Boulevard Trail
Boundary Creek
Boundary Creek
Boundary Creek Forest Service Station
Boundary Reservoir
Bowden Ranch
Bowen Valley
Bowersox Lake
Bowlus Cemetery
Bowlus Hill
Bowman Flats
Box Canyon
Box Canyon
Box Canyon
Box Canyon
Box Canyon
Box Canyon
Box Canyon
Box Canyon
Box Canyon Creek
Box Canyon Reservoir
Box Canyon Reservoir
Box Creek
Box D Ranch
Box Elder Canyon
Box Elder Canyon
Box Elder Spring
Box Lake
Box Spring
Box Spring
Box Spring
Box Spring Creek
Box Spring Reservoir
Box Springs
Box Springs Butte
Boyd
Boyd Creek
Boykin Creek
Earl Boyles Elementary School
Boys Forest Ranch
Braden Mine
Bradford Warden Station
Bradley Corner
Bradley Creek
Bradley Lake
Bradley Lake
Bradley State Park
Brads Creek
Bradshaw Drop
Brady Creek
Brandis Creek
Brandon Well
Brandt (historical)
Brannan Gulch
Branson Creek
Brass Cap Reservoir
Brass Nail Gulch
Braton Hollow
Brattain Cemetery
Brattain Elementary School
Braun
Brazos Mine
Bread Spring
Breakdown Creek
Sugarloaf
Breathing Spring
Brenner Canyon
Brentano Bar
Brenton Cabin
Breo Flat
Brewery Spring
Brewster Canyon
Brewster Ranch
Brewster Reservoir
Brewster Rock
Brezniak Ranch
Brian Creek
Bridge
Bridge Creek
Bridge Creek
Bridge Creek
Bridge Creek
Bridge Creek
Bridge Creek Canal
Bridge Creek Draw Reservoir
Bridge Forty Creek
Bridge Gulch
Bridge Gulch
Bridgeport Valley
Bridlemile Elementary School
Briem Creek
Briggs Middle School
Briggs Spring
Brights Spring
Brimstone Gulch
Brinker Creek
Brinker Creek
Bristol Reservoir
Britt Creek
Britt Nichols County Park
Broad Hollow
Broad Slough
Broadbent
Broadway Bridge
Brocher Creek
Brockman Gulch
Brockway Creek
Brogan
Brogan Cemetery
Brogan Ditch
Broken Back Ridge
Broken Pipe Spring
Broken Shovel Spring
Brokendown Waterhole
Brome Creek
Bronco Creek
Bronson Creek
Browns Reservoir
Bronx Canyon
Brooke Creek
Brooklyn Mine
Brooklyn City Park
Winterhaven School
Brooks
Brooks Cabin
Brooks Creek
Brosman Ditch
Brosman Mountain
Brouchaux Gulch
Broughton Bluff
Broumbaugh Cemetery
Browder Creek
Brown Bear Spring
Brown Butte
Brown Canyon
Brown Canyon
Brown Canyon
Brown Cemetery
Brown Creek
Brown Draw
Brown Loennig Ditch
Brown Mountain
Brownell Ditch
Browning Creek
Brownlee School (historical)
Browns Bridge (historical)
Browns Gulch
Browns Island
Browns Landing State Park
Brownsboro
Brownsville
Brownsville Ditch
Bruce Hollow
Bruckert Canyon
Bruno Cemetery
Bruno Lakes
Mount Bruno
Brush Canyon
Brush Creek
Brush Creek
Brush Creek
Brush Creek
Brush Creek
Brush Creek
Brush Creek
Brush Hollow
Brush Island
Brush Mountain
Brush Spray Spring
Brush Spring
Lake in the Brush
Brushy Butte
Brushy Creek
Brushy Gulch
Brushy Gulch
Brushy Hollow
Brushy Lake
Brushy Valley
Bryant Cemetery
Bryant Creek
Bryant Lake
Bryant Mountain
Bryant Park
Bryce Lake
Bubbling Spring
Buchanan Creek
Buchanan Springs
Buck Butte
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Gulch
Buck Gulch
Buck Gulch
Buck Gulch Mine
Buck Gulch Reservoir
Buck Hollow
Buck Hollow
Buck Hollow Creek
Buck Hollow
Buck Hollow
Buck Island
Buck Meadows
Buck Meadows Trail
Buck Mountain
Buck Mountain
Buck Mountain
Buck Mountain
Buck Mountain
Buck Mountain
Buck Mountain Fire Break
Buck Pasture
Buck Point
Buck Prairie
Buck Reservoir
Buck Ridge
Buck Ridge
Buck Rock
Buck Rock
Buck Rock
Buck Spring
Buck Spring
Buckaroo Cabin
Buckaroo Spring
Buckaroo Spring
Buckboard Creek
Buckboard Spring
Buckbrush Reservoir
Buckbrush Creek
Buckbrush Springs
Bucket Lake
Buckeye Mine
Buckheaven
Buckhorn
Buckhorn Camp
Buckhorn Canyon
Buckhorn Canyon
Buckhorn Canyon
Buckhorn Creek
Buckhorn Mine
Buckhorn Mine
Buckhorn Mountain
Buckhorn Ranch
Buckhorn Spring
Buckhorn Spring
Buckhorn Spring
Buckhorn Springs
Buckley Spring
Buckman Field
Buckman Elementary School
Buckmaster Flat
Buckmaster Spring
Buckner Creek
Bucks Corners
Buckskin Canyon
Buckskin Flat
Buckwilder Pass
Budd Creek
Budd Mountain
Budworm Creek
Buena Crest School (historical)
Buena Vista Butte
Buena Vista Canal
Buena Vista Creek
Buena Vista Patrol Station
Buena Vista Spring
Buffalo Gulch
Buffalo Reservoir
Bulck Canyon
Bulger Ditch
Bulger Flat
Bulger Hill
Bull Basin
Bull Canyon
Bull Canyon
Bull Canyon
Bull Canyon
Bull Canyon
Bull Canyon
Bull Canyon Reservoir
Bull Canyon Reservoir
Bull Creek
Bull Creek
Bull Creek
Bull Creek Pond
Bull Creek Reservoir
Bull Spring
Bull Flat Lake
Bull Heifer Creek
Bull Lake
Bull Meadow
Bull Prairie
Bull Run
Bull Run Canyon
Bull Run Creek
Bull Spring
Bull Spring
Bull Spring
Bull Spring
Bullards Beach State Park
Bullards Family Cemetery
Bulldozer Creek
Bullock Bridge
Bullock Drain
Bulls Eye Butte
Bully Creek School (historical)
Bully Creek Siphon
Bulmer Creek
Bum Canyon
Bummer Creek
Bummer Gulch
Bummer Gulch
Bumphead Reservoir
Bunch Grass Reservoir
Bunchgrass Creek
Bunchgrass Ridge
Bunker Creek
Bunker Hill
Bunker Hill
Bunker Hill Cemetery
Bunker Hill Mine
Bunker Hill Elementary School
Bunyard Creek
Buoy Creek
Burg Mountain
Burgdorfer Flat
Burgess Canyon
Burgess Gulch
Burgett Hill
Burgholzer Creek
Burke Lake
Burkhart Creek
Burkhart Park
Burke Spring
Burlingame Spring
Burlington
Burma Creek
Burmester Creek
Burn Canyon
Burn Creek
Burned Out Canyon
Burns
Burns Cemetery
Burns Paiute Indian Colony
Burns Park
Burns Paiute Cemetery
Burns High School
Burnside Bridge
Burnt Cabin Gulch
Burnt Canyon
Burnt Canyon
Burnt Corral Creek
Burnt Creek
Burnt Creek
Burnt Creek Ranch
Burnt Flat
Burnt Flat
Burnt Flat Creek
Burnt Flat Reservoir
Burnt Log Spring
Burnt Mountain
Burnt Ranch
Burnt Ridge
Burnt River Canyon
Burnt River Spring
Burnt River Valley
Burnt Stump Butte
Burnt Stump Reservoir
Burntwood Creek
Burris Creek
Burro Spring
Burton Creek
Burton Prairie
Bushnell Creek
Bushnell Rock
Buskirk Spring
Busse Canal
Busse Dam
Buster Camp
Buster Creek
Buster Creek
Butch Reservoir
Butcher Butte
Butcher Flat
Butler Basin
Butler Canyon
Butler Hill
Butler Mountain
Butler Spring
Butte Creek
Butte Creek
Butte Creek
Butte Creek
Butte Creek
Butte Creek
Butte Creek
Butte Creek
Butte Creek Pass
Butte Disappointment
Butte Waterhole Reservoir
Butter Creek Junction
Buttercup Spring
Butterfield Springs
Butterfly Spring
Butterfly Spring
Buttermilk Canyon
Buttermilk Canyon
Buttermilk Creek
Buttermilk Lake
Butternut Creek
Butteville Cemetery
Butteville Station
Buttin Creek
Button Hollow
Buxton Community Cemetery
Buxton Creek
Buzan Cemetery
Buzzard Butte
Buzzard Canyon
Buzzard Creek
Buzzard Lake
Buzzard Ridge
Buzzard Rock
Buzzard Rock
Buzzard Roost Creek
Buzzard Roost Spring
Buzzard Spring
Buzzard Spring
Bybee Lake
Bybee Peak
Byrds Point
Byron Creek
C Canal
Arts and Communication High School
C-G Cutoff
CCC Reservoir
Cabbage Hill
Cabbage Hill School (historical)
Cabbage Spring
Cabin Sixty-nine
Cabin Canyon
Cabin Creek
Cabin Creek
Cabin Creek
Cabin Creek
Cabin Creek Spring
Cabin Waterhole
Cable Cove
Cache Camp
Cactus Ridge
Cadenza Creek
Cahill Creek
Cahill Reservoir
Cairo
Cairo Elementary School
Cal Smith Spring
Calahan Meadow
Calamity Creek
Calapooia River
Calapooya Creek
Calderwood Reservoir
Caleb Cemetery
Calendar Slough
Calf Creek
Calf Gulch
Calhoun Reservoir
Muslin Creek
California Gulch
California Gulch
California Gulch
California Mine
California Mine
California Mountain
Callahan
Callahan Creek
Callahan Creek
Callahan Spring
Calloway Creek
Mount Calvary Cemetery
Camas Creek
Camas Lookout
Camas Mountain
Camas Mountain State Park (historical)
Camas Swale
Camas Swale
Camas Swale Creek
Camas Valley
Camas Valley
Camel Hump
Cameron School (historical)
Camous Creek
Camp Twenty-six
Camp Four
Camp Adams
Browns Camp OHV Staging Area
Camp Cabin
Camp Carson Mine
Camp Collins
Camp Colton
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek Cemetery
Camp Creek Reservoir
Camp Creek Ridge
Camp Creek Elementary School
Camp Crunch Spring
Camp Fifteen
Camp Hancock
Camp Kettle Creek
Camp Kettle Reservoir
Camp Kilowan
Camp Lee
Camp Lyons (historical)
Camp Magruder
Camp McGregor
Camp Melakwa
Camp Millard (historical)
Camp Olson
Camp One Trail
Camp Four Reservoir
Camp Russell
Camp Smith
Camp Spring
Camp Tapawingo
Camp Tawanka
Camp Twelve
Camp Tyee
Camp Wilkerson
Camp Yamhill
Campbell Canyon
Campbell Creek
Campbell Creek
Campbell Creek
Campbell Gulch
Campbell Lake
Campbell Lake
Campbell Reservoir
Campbell Elementary School
Campbell Spring
Campbell - Grier Cemetery
Campspot Spring
Can Spring
Canaan
Canby
Canby Ferry
Candalaria Park
Candalaria Elementary School
Candiani Bar
Cane Creek
Caufield Creek
Canfield Hill
Cannery Light
Cannon Beach
Cannon Beach Junction
Cannon Gulch
Cannon Gulch
Cannon School (historical)
John Day Fossil Beds National Monument Cant Ranch Museum
Cantell Creek
Cantor Creek
Cannon Beach Trail
Canyon Creek
Canyon Creek
Canyon Creek
Canyon Creek
Canyon Creek
Canyon Creek
Canyon Creek
Canyon Creek
Canyon Creek
Canyon Creek Meadow
Canyon Creek Pass
Canyon Mountain
Canyon Number 1
Canyon Number 2
Canyon Number 3
Canyon Reservoir
Canyon Springs
Canyonville
Cap Martin Mine
Cape Arago State Park
Cape Blanco
Cape Creek
Cape Falcon
Cape Foulweather
Capitol Hill
Capon Flat
Captain Jack Lake
Car Reservoir
Carcus Creek
Cardwell Creek
Carey Bend
Carey Creek
Carey Ranch
Carey Reservoir
Carey Spring
Caribou Bar
Caris Creek
Carl Spring
Carlisle Creek
Carlson Creek
Carlson Creek
Carlson Creek
Carlton Canyon
Carlton Reservoir
Carmel of Maria Regina Monastery
Carnahan
Carnes Creek
Carney Canyon
Carnine Canyon
Carolina Creek
Caroline Bar Creek
Carpenter Butte
Carpenter Creek
Carpenter Mountain
Carr Creek
Carr Slough
Carrie Fork
Carson Trail
Carter Creek
Carter Creek
Carter Creek
Carter Creek
Carter Homestead
Carter Reservoir
Carter Spring
Carton Ranch
Cartwright Creek
Carus
Carvix Reservoir
Cary Creek
Cary Spring
Portland Community College Cascade
Cascade Middle School
Cascades Gateway City Park
Cascades School
Cascadia Ranger Station (historical)
Case Knife Creek
Case Knife Ridge
Case Ridge
Casebeer Ranch
Casebeer Ranch
Casey Slough
Cash Creek
Cash Gulch
Cash Hollow
Cason Canyon
Cason Canyon
Casteel Spring
Castle Creek
Castle Ridge
Castle Rock
Castle Rock
Castle Rock
Castle Rock
Castle Rock Creek
Castle Rock Creek
Castle Rock Fire Station
Castle Rock Spring
Castle Slough
Castle Spring
Castle View Spring
Castor Creek
Castro Ridge
Castro Spring
Cat and Kittens Rock
Cat Butte
Cat Lakes
Cat Reservoir
Catching Creek
Catching Creek
Catching Creek
Catching Creek Cemetery
Catching Slough
Caterpillar Butte Reservoir
Cates Canyon
Cathedral Rock
Cathedral School
Catherine Creek
Catherine Creek Guard Station
Catherine Creek State Park
Catherson Cabin
Cathlamet Bay
Catlin-Hillside School (historical)
Catlow
Catlow Rim
Catlow Valley
Catterson Creek
Cattle Creek
Cattle Creek
Cattle Guard Spring
Cattle Rapids (historical)
Cattrill Creek
Cauthorn Spring
Cavanaugh Creek
Cave Canyon
Cave Canyon
Cave Creek
Cave Creek
Cave Hollow
Cave Hollow Spring
Cave Reservoir
Cave Reservoir
Cayuse Canyon
Cazadero Dam
Cedar Butte
Cedar Butte
Cedar Butte
Cedar Buttes
Cedar Camp
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Flat
Cedar Grove School
Cedar Gulch
Cedar Hollow
Cedar Island
Cedar Island
Cedar Meadow
Cedar Mill
Cedar Mill Creek
Cedar Mill Elementary School
Cedar Mount Reservoir
Cedaroak Park Primary School
Cedar Point
Cedar Spring
Cedar Spring
Cedar Swamp
Cedar Swamp Creek
Celia Spring
Celilo Converter Station
Celilo Light
Celilo Park
Lake Celilo
Cellar Reservoir
Cement Spring
Cemetery Spring
Centennial High School
Centennial Island
Centennial Elementary School
Center Canal
Central Alkali Drain
Central Catholic High School
Central Howell Elementary School
Central Line Creek
Central Linn High School
Central Point
Central Point
Central Reservoir Number One
Central Reservoir Number Two
Central Elementary School (historical)
Christ's Center School
Central Elementary School
Central Middle School
Central School (historical)
Central Valley Christian School
Chadwell School (historical)
Chadwick Canyon
Chain Canyon
Chain Lake
Chalk Basin
Chalk Butte
Chalk Creek
Chalk Gulch
Chalk Reservoir
Chalk Spring
Chalk Spring
Chalk Spring
Chalk Spring
Chamber Spring
Chambers Ranch
Champagne Creek
Champion Creek
Champoeg Cemetery
Chance Lateral
Chandler Bridge
Chandler Cabin
Chandler Canyon
Chandler Mountain
Chandler Pass
Chandler State Park
Chaney Reservoir
Chanis Rock
Channel Creek
Chanticleer Point
Chapel Spring
Chapman
Chapman Beach
Chapman Canyon
Chapman Hollow
Chapman Landing
Chapman Point
Chapman Reservoir
Chapman Reservoir
Chapman Elementary School
Chapman Slough
Chapman Spring
Charley Corral
Charlie Creek
Chastain Spring
Chasteen Meadow
Chatham Island
Chautauqua Lake
Cheadle Lake
Cheat Creek
Chehulpum Creek
Chemawa Substation
Chenoweth Creek
Cherokee Creek
Cherry Creek
Cherry Creek
Cherry Creek
Cherry Creek
Cherry Creek
Cherry Creek
Cherry Creek
Cherry Creek
Ham Bunch - Cherry Creek County Park
Cherry Creek Ranch
Cherry Creek Reservoir
Cherry Creek Reservoir
Cherry Park Elementary School
Cherry Spring
Cherry Spring
Cherry Spring
Cherry Spring
Cherry Spring
Cherry Spring
Cherry Spring
Cherry Spring
Cherry Spring
Cherry Spring Creek
Chester Spring
Chevally Reservoir
Cheviot Creek
Chichester Gulch
Chickahominy Creek
Chicken Creek
Chicken Creek
Chicken Creek
Chicken Creek
Chicken Creek
Chicken Creek
Chicken Creek Reservoir
Chicken Feed Lake
Chicken Flat
Chicken Gulch
Chicken Peak
Chicken Spring
Chicken Spring
Chicken Spring Canyon
Chico Guard Station (historical)
Chief Joseph Elementary School
Child Service Center
Children Hospital School (historical)
Chimney Creek
Chimney Creek
Chimney Creek
Chimney Rock
Chimney Rock
Chimney Rock
Chimney Rock
Chimney Springs
Chimney Springs Canyon
China Camp Spring
China Creek
China Ditch
China Creek
China Creek
China Creek Corral Pond
China Gap
China Gulch
China Gulch
China Hill Reservoir
China Hollow
China Peak
China Rock
Chinaman Hat
Chinatown Pump
Chinook Dike Light
Chinquapin Mountain
Chinquapin Point
Chipmunk Ridge
Chipmunk Spring
Chisholm Canyon
Chitsey Spring
Chloride Mine
Chloride Ridge
Chokecherry Spring
Christensen Creek
Christensen Slough
Christie School
Christmas Lake
Christmas Lake Valley
Chrome
Chrome Lake
Chrome Reservoir
Chukar Spring
Church Creek
Churchill Canyon
Churchill High School
Chutes
Cincha Lake
Cinder Butte
Cinderella Mine (historical)
Cinnabar Creek
Cipole School (historical)
Circle Bar
Circle Bar Ranch
Circle Bar Ranch
Circle Butte
Circle Creek
City Creek
City Farm
City Gulch
City Gulch
City View Reservoir
Civil Bend Cemetery
Clabber Creek
Alder Creek Middle School
Clackamas Rapids
Claggett Cemetery
Clapp Meadow
Clark Branch
Clark Canyon
Clark Canyon
Clark Canyon Reservoir
Clark Canyon Reservoir Number Two
Clark Creek
Clark Creek Guard Station
Clark Ranch
Clark Elementary School
Clark Slough
Clarke Springs
Clarks Butte
Clarks Canyon
Clarks Creek
Clarks Creek Ditch
Clarnie (historical)
Clarno Cemetery
Clatskanie
Clatskanie Mountain
Clatskanie River
Clatsop Plains
Clatsop Plains School (historical)
Clatsop Ridge
Clatsop State Forest
Claude Reservoir
Clay Creek
Clayton Point
Clayton Spring
Clear Creek
Clear Creek
Clear Creek
Hembre Creek
Clear Creek
Clear Creek
Clear Creek
Clear Creek
Clear Creek Reservoir
Clear Lake
Clear Lake
Clear Lake
Clear Lake
Clear Lake
Clear Lake Elementary School
Clear Spring
Clearing Creek
Cleary Ditch
Cleghorn Creek
Cleighton Creek
Cleland Spring
Clement Ditch
Cleo Lake
Cleveland
Cleveland High School
Cleveland Mine
Clevenger Creek
Cliff Mine
Cliff Ranch
Cliff Ranch
Cliff Spring
Clifton
Clifton Channel
Cline Buttes
Cline Falls State Park
Clinton City Park
Clough Gulch
Clover Creek
Clover Creek
Clover Creek
Clover Creek
Clover Creek
Clover Creek
Clover Creek
Clover Creek Ranch
Clover Creek Valley
Clover Ridge Elementary School
Clover Swale
Clover Swale
Cloverdale Cemetery
Clubfoot Hollow
Chickahominy Reservoir
Clymer Spring
Coak Creek
Coal Creek
Coal Creek
Coal Creek
Coal Creek
Coal Creek
Coal Creek
Coal Creek
Coal Creek
Coal Mine Basin Creek
Coal Pit Spring
Coalbank Slough
Coaledo
Coarse Gold Creek
Coast Fork Willamette River
Coates Canyon
Coates Drain
Coates Spring
Cobb Creek
Cobb Saddle
Cobb Spring
Cobb Springs
Coburg
Coburg Ridge
Coburn Creek
Cochran Creek
Cochran Gulch
Cochran Pond
Coffee Creek
Coffee Creek
Coffee Creek
Coffee Creek
Coffee Creek
Coffee Gap
Coffee Island
Coffee Lake
Coffee Pot Reservoir
Coffee Pot Spring
Coffeepot Crater
Coffeepot Reservoir
Coffeepot Spring
Coffenbury Lake
Coffin Canyon
Coffin Rock
Coglan Buttes
Coglan Canyon
Cogswell Creek
Coker Butte
Colby Gulch
Cold Camp
Cold Camp Creek
Cold Creek
Cold Creek
Cold Creek
Cold Creek
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring Canyon
Cold Spring Canyon
Cold Spring Creek
Cold Spring Creek
Cold Spring School (historical)
Cold Springs
Cold Springs
Cold Springs
Cold Springs Canyon
Cold Springs Junction
Cold Springs National Wildlife Refuge
Cold Springs Reservoir
Cold Springs Wash
Coldwater Creek
Cole Creek
Cole Creek
Cole Ditch
Cole Island
Cole Island
Cole Mountain
Cole Slough
Coleman Creek
Coleman Creek
Coleman Lake
Coleman Mountain
Coleman Point
Coleman Ranch
Coleman Ridge
Coleman Spring
Coleman Spring
Coles Valley
Kelly Middle School
College Heights City Park
College Hill
Collins Creek
Collins Creek
Collins Lake
Riverdale High School
Collumbaugh Reservoir
Collusion Point
Collver Point
Colorado Lake
Coles Valley Cemetery
Colt Creek
Colt Spring
Colton
Columbia Beach
Historic Columbian Cemetery
Cascade College (historical)
Columbia City Channel
Columbia Hall
Columbia Heights School (historical)
Columbia Mine
Columbia Mine
Columbia City Park
Columbia Placer
Colvard Station
Colvert Spring
Colvin Creek
Colvin Lake
Colvin Timbers
Combine Canyon
Combs Creek
Commodore Lake
Commodore Ridge
Lane Community College (historical)
InterMountain Education Service District
Company Hollow
Company Hollow Spring
Company Lake
Company Spring
Company Springs
Campground Reservoir
Compton Spring
Comstock Basin
Con-Virginia Mine
Concomly (historical)
Concord Elementary School
Concordia University
Condon
Condon Canyon
Condon School (historical)
Cone Creek
Cone Reservoir
Conger Creek
Conical White Rock
Conklin Creek
Conley Creek
Conley Lake
Conner Creek
Connolly Basin
Connor Creek
Connor Creek Mine
Conroy Canyon
Conroy Canyon Reservoir
Conroy Creek
Conway Reservoir
Conyers Creek
Cook Creek
Cook Creek
Cook Creek
Cook Creek
Cook Creek
Cook Reservoir
Cook Slough
Cook Spring
Cook Spring
Cook Stove Basin
Cook Stove Reservoir
Cookhouse Creek
Cooks Butte
Cool Spring
Cooley Creek
Coolie Spring
Coombs Canyon
Coon Canyon
Coon Creek
Coon Creek
Coon Creek
Coon Creek
Coon Creek
Coon Creek
Coon Gulch
Coon Hollow
Coon Hollow
Coon Island
Coon Point
Coon Spring
Coon Spring
Coonskin Creek
Cooper Bridge
Cooper Creek
Cooper Creek
Cooper Creek
Cooper Creek
Cooper Draw
Cooper Mountain Elementary School
Cooper Spring
Cooperage Slough
Coos City Bridge
Coos County Forest
Coos Mountain
Coos Ridge
Coos River Fish Hatchery
Coos River School (historical)
Cope Canyon
Copeland Butte
Copeland Reservoir
Copeland Reservoirs
Copeleys Rock
Copeland Butte
Copper Buttes
Copper Creek
Copper Creek
Copper Creek
Copper Creek Falls
Copper Queen Mine
Copperhead Creek
Copsey Camp
Copsey Creek
Coquille
Coquille Rock
Coquille Valley
Coquille Valley Hospital
Cordwood Canyon
Corey Gulch
Corless Spring
Corley Creek
Cornelius Pass
Cornet Creek
Cornucopia Mines
Cornucopia Peak
Cornutt
Corporation Lake
Corral Canyon
Corral Canyon
Corral Creek
Corral Creek
Corral Creek
Corral Creek
Corral Creek
Corral Creek
Corral Gulch
Corral Hollow
Corral Lake
Corral Mountain
Corral Spring
Corral Waterhole
Corrigal Spring
Corporation Rim
Corta Reservoir
Coryell Pass
Cote Grade
Cote Lake
Cotton Creek
Cotton Spring
Cottonwood Bend
Cottonwood Cabin Spring
Cottonwood Canyon
Cottonwood Canyon
Cottonwood Canyon
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Little Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Glades
Cottonwood Gulch
Cottonwood Gulch
Cottonwood Gulch
Cottonwood Gulch
Cottonwood Gulch
Cottonwood Island Lower Range
Cottonwood Island Upper Range
Cottonwood Lake
Cottonwood Meadow Lake
Cottonwood Pond
Cottonwood Ridge
Cottonwood Spring
Cottonwood Spring
Cottonwood Spring
Cottonwood Spring
Cottonwood Spring
Cottonwood Spring
Cottonwood Spring
Cottonwood Spring
Cottonwood Spring
Cottonwood Springs
Cottonwood Springs
Cottrell Elementary School
Couch Creek
Kautz Mansion
Metropolitan Learning Center
Cougar Basin
Cougar Bend
Cougar Canyon
Cougar Canyon Reservoir
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cottonwood Complex Campground
Cougar Meadows
Cougar Mine
Cougar Mountain
Cougar Mountain
Cougar Mountain
Cougar Pass
Cougar Peak
Cougar Pond
Cougar Ridge
Cougar Ridge
Cougar Ridge
Council Creek
Council Creek
Council Crest City Park
Country Lane City Park
County Creek
County Trough Spring
Court Spring
Courthouse Rock
Courthouse Rock
Courtney Creek
Courtney Creek School (historical)
Courtney Ditch
Courtrock School (historical)
Cove Beach
Cove Camp
Cove Cemetery
Cove Creek
Cove Creek
Cove Creek
Cove Creek
Cove Creek
Cove Creek
Cove Point
Covington Point
Cow Camp Spring
Cow Camp Spring
Cow Canyon
Cow Canyon
Cow Canyon
Cow Canyon
Cow Creek
Cow Creek
Cow Creek
Cow Creek
Cow Creek
Cow Creek
Cow Creek
Cow Creek Game Refuge
Cow Hollow
Cow Hollow Siphon
Cow Hollow Spring
Cow Lakes
Cow Lakes Recreation Area
Cow Valley
Cow Valley Butte
Cowan Creek
Cowgill Well
Cowhorn Trail
Cowley Creek
Cox Butte
Cox Canyon
Cox Creek
Cox Creek
Cox Creek
Cox Creek
Cox Creek
Cox Creek
Cox Spring
Coxcomb Hill
Coyote Butte
Coyote Canyon
Coyote Canyon
Coyote Canyon
Coyote Corner
Coyote Coulee
Coyote Creek
Coyote Creek
Coyote Creek
Coyote Creek
Coyote Creek
Coyote Creek
Coyote Creek Reservoir
Coyote Flat
Coyote Flat
Coyote Flat
Coyote Gap
Coyote Gap Corral
Coyote Gulch
Coyote Gulch
Coyote Holes Reservoir
Coyote Hollow
Coyote Mine
Coyote Mountain
Coyote Mountain
Coyote Point
Coyote Rim
Coyote Spring
Coyote Spring
Coyote Springs
Coyote Spring
Coyote Spring
Coyote Springs
Coyote Waterhole
Coyote Well
Coyote Wells
Coyote Wells Reservoir
Crabapple Lake
Crabtree
Crabtree Guard Station
Crabtree Hill
Crabtree Lake
Crabtree Lake Trail
Crabtree Mountain
Cracker Camp
Craft Canyon
Crag Creek
Craggy Rock
Craig Creek
Craig Gulch
Craig Lake
Craig Lake
Craig Mountain
Cram Ditch
Cramer Canyon
Crane
Crane Creek
Crane Creek Gap
Crane Creek Mountains
Crane Creek Reservoir
Crane Lake
Crane Prairie
Crane Slough
Crane Spring
Crater Lake
Crater Lake Well
Crates Point
Crates Point Light
Crawford Branch
Crawford Creek
Crawford Hollow
Crawfordsville
Crazy Creek
Crazy Creek
Crazy Fork
Crazy Hollow
Crazy John Spring
Crazy Spring
Crazyman Creek
Crazyman Flat
Creamery Creek
Cremo Creek
Crescent Beach
Crescent Grove Cemetery
Crescent Lake
Crest Drive Elementary School
Creston City Park
Creston Elementary School
Creston Waterhole
Creswell
Creswell Butte
Creswell Canyon
Crevice Creek
Crews Creek
Crib Point
Cricket Flat
Criminal Creek
Crims Island
Cripple Creek
Cripple Gulch
Crisman Hill
Criterion (historical)
Crocker Spring
Croft Lake
Croisan Creek
Croisan Ridge
Cronin Creek
Crook Peak
Crooked Creek
Crooked Creek
Crooked Creek
Crooked Creek
Crooked Creek
Crooked Creek
Crooked Creek Ranch
Crooked Creek Spring
Crooked Creek State Park
Crooked Creek Valley
Crooked Finger School (historical)
Crooks Creek
Crosby Bridge
Crosel Creek
Cross Canyon
Cross Canyon Trail
Cross Hill
Cross Ranch
Crosswhite Butte
Crosswhite Canyon
Crow
Crow Creek
Crowcamp Creek
Crowcamp Mountain
Crowcamp Reservoir
Crowfoot Creek
Crowley
Crowley Creek
Crowley Guard Station
Crowley Mine Creek
Crowley Ranch
Crowley Reservoir
Crown Point
Crown Point
Crown Point Mine
Crown Rock
Crows Nest Reservoir
Cruiser Creek
Cruiser Creek
Crump Geyser
Crump Lake
Crump Ranch
Crump Reservoir
Crump Spring
Crutchfield Creek
Crystal Creek
Crystal Lake
Crystal Palace Gulch
Crystal Palace Mine
Crystal Spring
Crystal Spring
Crystal Springs Creek
Crystal Springs Lake
Cub Spring
Cucamonga Creek
Cullaby Creek
Cullaby Lake
Cullaby Slough
Cullen Cabin
Cultus Creek
Culver Creek
Cummings Hill Summit
Cunha Canyon
Cunningham Canyon
Cunningham Cove
Cunningham Reservoir
Cunningham Saddle
Cunningham Slough
Cup Gulch
Cupola Rock
Currey Canyon
Currant Creek
Currant Spring
Currey Canyon
Currey Reservoir
Currey Spring
Currie Canyon
Currin Creek
Curry Gordon Creek
Curry Gulch
Curry Lake
Curtin
Curtis Creek
Curtis Creek
Curtis Slough
Cushing Falls
Cushman Canyon
Cusick Creek
Custer City Park
Cys Branch
D M Spring
D Canal
Bobcat Creek
D L Spring
Dabney State Park
Dads Creek
Daggett Creek
Daggett Point
Dahle Spring
Dairy
Dairy Creek
Dairy Creek
Dairy Creek Guard Station
Dairy Point
Dairy Pump
Dairy Siding
Daisy Basin
Daisy Basin Spring
Daisy Creek
Daisy Mine
Dalreed Butte
Daly Reservoir
Daly Spring
Daly Spring
Damascus
Damascus Middle School
Dammasch State Hospital (historical)
Dan Cold Spring
Danebo Elementary
Daniels Creek
Daniels Creek
Danish Cemetery
Danner Valley
Danny Boy Spring
Darby Creek
Darius Creek
Dark Canyon
Dark Hollow
Darling Canyon
Darr Flats
Darrow Bar
Darrow Rocks
Darrows Islands
Dart Cemetery
Dart Creek
Daugherty Canyon
Dave Busenbark County Park (historical)
Davenport Pond
Daves Slough
David Douglas County Park
David Hill
David Hill Elementary School (historical)
Davidson Hill
Davidson Reservoir
Davies Gulch
Davis Canyon
Davis Creek
Davis Creek
Davis Creek
Davis Creek
Davis Dam
Davis Lake
Davis Lake
Davis Reservoir
Davis Ridges
Davis Slough
Davison Butte
Day Basin
Day Cemetery
Day Creek
Forty Day Creek
Day Creek
Day Memorial Park
Days Creek
Days Creek Cutoff
Dayton Station
De Armond Mountain
De Garmo Canyon
DeVaul Lake
DeVore Mountain
Deacon Flat
Dead Cow Creek
Dead Cow Spring
Dead Dog Canyon
Dead Dog Canyon
Dead Horse Canyon
Dead Horse Canyon
Dead Horse Canyon
Dead Horse Creek
Dead Horse Gap
Dead Horse Lake
Dead Horse Ridge
Dead Horse Rim
Dead Horse Spring
Dead Indian Mountain
Dead Ox Canal
Dead Ox Flat
Dead River
Dead Bull Waterhole
Dead Horse Recreation Site
Deadhorse Creek
Deadhorse Creek
Deadhorse Spring
Deadman Canyon
Deadman Canyon
Deadman Canyon
Deadman Creek
Deadman Creek
Deadman Gulch
Deadman Gulch
Deadman Gulch
Deadman Pass
Deadman Pass Canyon
Deadman Point
Deadman Reservoir
Deadman Water Hole
Deadman Well
Deadmans Bedground
Deadwood Gulch
Deady (historical)
Dean Creek
Dean Point
Dear Creek
Dean Mountain
Deary Reservoir
Deary Pasture
Deathball Rock
Debenger Gap
Dedman Canyon
Dedrick Slough
Deep Canyon
Deep Canyon
Deep Canyon
Deep Canyon Lake
Deep Creek
Deep Creek
Deep Creek
Deep Creek
Deep Creek
Deep Creek
Deep Creek
Deep Creek
Deep Creek
Deep Creek
Deep Creek
Deep Creek County Park
Deep Creek Falls
Deep Draw Reservoir
Deep Hole
Deep Lake
Deer Butte
Deer Butte
Deer Butte Reservoir
Deer Butte Reservoir Number One
Deer Butte Reservoir Number Two
Deer Butte Spring
Deer Butte Trail
Deer Canyon
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek Recreation Site
Deer Creek County Park
Deer Gulch
Deer Gulch
Deer Gulch
Deer Island
Deer Island Point
Deer Island Slough
Deer Spring
Deer Spring
Deer Spring
Deer Spring
Deer Spring
Deerhorn
Degner Canyon
Degner Spring
Del Monte Mine
Delake
Delco Creek
Delena
Delight Valley Elementary School
Dell Creek
Dellwood
Delta Park East
Dement Creek
Dempsey Spring
Denio Creek
Denis Cabin
Denmark
Dennis Creek
Dennison Reservoir
Denny Creek
Denny School (historical)
Denny Spring
Denson Canyon
Dent Creek
Denver Point
Deyoe Creek
Depoe Bay
Depoe Bay City Park
Depot Creek
Deppy Creek
Derby Creek
Derby School
Derby Station
Derrick Lake
Deschutes Junction
Deschutes River State Park
Desdemona Sands
Desdemona Sands Light
Desert Field
Desert Lake
Desert Meadow
Despain Gulch
Destruction Creek
Deton Creek
DeVaul Ranch
Dever School (historical)
Devil Canyon
Devil Lake
Devils Backbone
Devils Backbone
Devils Butte
Devils Canyon
Devils Canyon
Devils Canyon
Devils Canyon
Devils Club Creek
Devils Creek
Devils Elbow
Devils Elbow
Devils Gap
Devils Garden
Devils Gate
Devils Graveyard
Devils Heel
Devils Kitchen
Devils Punch Bowl
Devils Punchbowl State Park
Devine Flat
Devine Flat Springs
Devine Rock
Dew Valley
Dew Valley
Dewey Creek
Dexter
Dexter Canyon
Dexter Reservoir
Diamond Butte
Diamond Butte
Diamond Canal
Diamond Craters
Diamond Drain
Diamond Head
Diamond Elementary School
Diamond Spring
Diamond Swamp
Diamond Valley
Dibblee Point
Dice Creek
Dick Creek
Dick Creek
Dicker Reservoir
Dickey Prairie
Dickey Prairie
Dickey Prairie Elementary School
Dicks Creek
Dicks Spring
Dicks Well
Dillion Lake
Dillon Ditch
Dingle Creek
Dingus Spring
Dinner Creek
Dinner Creek Reservoir Number One
Dinner Creek Reservoir Number Two
Dinner Creek Reservoir Number Three
Dinwiddie Valley
Dippen Rig Creek
Dipping Vat Canyon
Dipping Vat Creek
Dipping Vat Spring
Dipping Vat Spring
Dipping Vat Spring
Dirt Reservoir
Discovery Gulch
Dishrag Canyon
Dishrag Spring
Ditch Creek
Ditmar Bend
Divide
Division Canyon
Division Gulch
Division-Powell Park
Division Reservoir
Dixie Canyon
Dixie Creek
Dixie Creek
Dixie Gulch
Dixie Mountain
Dixie Ranch
Dixie School (historical)
Dixon Creek
Dixon Creek
Dixon Spring
Dixons Rock
Dixons Rock Reservoir
Dixonville
Doak Creek
Bear Creek
Doane Creek
Doane Lake
Doane Point
Dobbin Creek
Dobyns Lake
Dodds Hollow
Dodge Bridge
Dodge Canyon
Dodge Canyon
Dodge Cemetery
Dodge Island
Dodge Slough
Dodson Butte
Dodson Slough
Doe Camp
Doe Canyon
Doe Creek
Doe Creek
Doe Creek
Doe Creek
Doe Gulch
Doe Island
Doe Reservoir
Doe Spring
Doerner Creek
Dog Creek
Dog Creek
Dog Creek
Dog Creek
Dog Creek
Dog Creek Meadow
Dog Hollow Reservoir
Dog Lake
Dog Lake Reservoir
Dog Mountain
Dog Spring
Dog Spring
Dogtown Creek
Dogwood Creek
Doherty Ranch
Doherty Slide
Dolph Corner
Domogalla Canyon
Domogalla Ridge
Donaldson Canyon
Donnelly Basin
Donner und Blitzen River
Dooley Mountain
Dooley Summit
Doolittle Creek
Dooly Creek
Dorena Lake
Dorena School
Dorman Pond
Dorn Peak
Dorothea Mine
Doty Hill
Double Falls
Double Mount Spring
Double Mountain
Doug Canyon
Douglas Cemetery
Douglas Creek
Douglas Creek
Douglas Gardens Elementary School
Douglas High School
David Douglas High School South
Douglas Hollow
Douglas Hollow School
David Douglas High School
Dove Hollow
Dovre Campground
Dowell Butte
Dowell Ranch
Dowell Reservoir
Dowell Reservoir
Downey Canyon
Downey Canyon Spring
Downey Creek
Downey Creek Reservoir
Downie Lake
Downing (historical)
Downing Creek
Downs
Drace Hollow
Drain Creek
Drain Hill
Drake Creek
Drake Creek
Drake Crossing
Drake Falls
Drake Peak Lookout
Drake Ranch
Drake Spring
Drake Spring
Draper Canyon
Draperville
Draw Creek
Drews Ranch
Drews Valley Ranch
Drewsey
Drewsey Reclamation Company Ditch
Drewsey Table
Drewsey Valley
Drift Creek
Drift Creek
Drift Fence Waterhole
Drill Box Canyon
Drindarry Gulch
Drinkwater Pass
Drinkwater Reservoir Number Two
Dripping Springs
Driscol Spring
Driscoll Range
Driscoll Slough
Driscoll Spring
Driver Valley
Dropoff Waterhole
Drought Creek
Drue Creek
Druggs Creek
Drum Hill
Drury Butte
Drury Creek
Drury Creek
Dry Ayers Canyon
Dry Beaver Creek
Dry Beaver Ridge
Dry Boulder Creek
Dry Buttes
Dry Canyon
Dry Canyon
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek Buttes
Dry Creek Buttes Reservoir
Dry Creek Horse Camp
Dry Creek Cemetery
Dry Creek Gorge
Dry Creek Pass
Dry Creek Reservoir
Dry Creek Reservoir
Dry Creek Rim
Dry Fork
Dry Fork Hay Creek
Dry Fork Jordan Creek
Dry Fork Thirtymile Creek
Dry Grouse Creek
Dry Gulch
Dry Gulch
Dry Gulch
Dry Gulch
Dry Gulch
Dry Gulch
Dry Hog Hollow
Dry Hole Reservoir
Dry Hollow
Dry Hollow
Dry Hollow
Dry Hollow
Dry Krumbo Creek
Dry Lake
Dry Lake
Dry Lake
Dry Lake
Dry Lake
Dry Lake Reservoir
Dry Lake Reservoir
Dry Lake Waterhole
Dry Morris Canyon
Dry Mud Creek
Dry Muddy Creek
Dry Prairie
Dry Valley
Dry Valley
Dry Valley Rim
Dry Well
Dry Well
Dryland
Duck Club
Duck Creek
Duck Creek Butte
Duck Creek Flat
Duck Creek Lakebed
Duck Creek Spring
Duck Pond Reservoir
Duck Slough
Dudes Canyon
Duffy Butte
Duffy Lake
Duffy Lake Trail
Duffy Prairie
Dufur
Dugger Creek
Dugout Canyon
Dugout Creek
Duhaime Flat
Duke Bar
Dumas Gulch
Duncan Creek
Duncan Ditch
Duncan Island
Duncan Spring
Duncan Spring
Dundon Flat
Dune
Duniway City Park
Duniway Elementary School
Dunlap Canyon
Dunn Dam
Opportunity Center
Dunnigan Spring
Dunns Bluff
Dupee Valley
Durbin Creek
Durham
Durkee Creek
Durkee Valley
Dusenberry Lake
Dust Bowl
Dutch Canyon
Dutch Flat
Dutch Flat
Dutch Flat
Dutch Flat Creek
Dutch Flat Lake
Dutch Flat Saddle
Dutch Gulch
Dutch John Cabin
Dutch John Creek
Dutch John Ravine
Dutch John Section
Dutch Oven
Dutch Oven Creek
Dutch Oven Flat
Dutch Waterhole
Dutchman Butte
Dutton Canyon
Dwayne Spring
Dye Creek
Dyer Creek
Dyer State Park
E and E Mine
E Canal
Emigrant Hill
Eads Hill Trail
Eads Springs
Eagle Butte
Eagle Canyon
Eagle Creek
Eagle Creek
Eagle Creek
Eagle Creek
Eagle Creek
Eagle Creek
Eagle Fern Park
Eagle Point
Eagle Rock
Eagle Rock
Eagle Spring
Eagle Springs
Eagle Springs Corral
Eagle Valley
Eakin Canyon
Eames Creek
East Bench
East Berlin School (historical)
East Birch Creek
East Branch Wildhorse Creek
East Burnt Corral Creek
East Camp Creek
East Chain Lake
East Channel South Santiam River
East China Spring
East Copeland Reservoir
East Corral Spring
East Cow Hollow
East Cow Hollow Reservoir
East Creek
East Creek
East Crockett Branch
East Foley Creek
East Ford
East Fork Alder Creek
East Fork Bales Creek
East Fork Billy Creek
East Fork Birch Creek
East Fork Boundary Creek
East Fork Cook Creek
East Fork Coquille River
East Fork Cornet Creek
East Fork Corral Creek
East Fork Crow Creek
East Fork Deer Creek
East Fork Dry Creek
East Fork Evans Gulch
East Fork Floras Creek
East Fork Grande Ronde River
East Fork Horse Creek
East Fork Indian Creek
East Fork Koontz Creek
East Fork Love Creek
East Fork McKay Creek
East Fork Millicoma River
East Fork Miners Creek
East Fork Nehalem River
East Fork Pine Creek
East Fork Pole Creek
East Fork Rat Creek
East Fork Rattlesnake Gulch
East Fork Rawhide Creek
East Fork Rock Creek
East Fork Rum Creek
East Fork Sain Creek
East Fork Silvies River
East Fork South Fork McKenzie River
East Fork Spring Hollow Creek
East Fork Tucker Creek
East Fork West Eagle Creek
East Fork Whisky Creek
East Fork Whitcomb Creek
East Gosage Creek
East Grain Camp Canal
East Gresham Elementary School
East Gulch Waterhole
East Harper Basin Spring
East Humbug Creek
East Island
East Lakes Reservoir
East Light
East Malone Lateral
East Maupin
East Prong Dry Creek
East Prong Little Walla Walla River
East Road Gulch
East Road Gulch Spring
East Road Springs
East Rock Creek
Davis Elementary School
East Spring
East Spring
East Spring
East Square Mountain Reservoir
East Swamp Creek
East Trinity Creek
East Vidler Creek
East Weed Lake Butte Waterhole
East Willis Creek
Easterday Reservoir
Eastern Oregon Livestock Exposition Grounds
Blue Mountain Recovery Center
Alliance Charter School
Eastman Gulch
Easton Canyon
Eastside
Eastside Elementary School (historical)
Eastside School (historical)
Ebell Creek
Ebell Creek Divide
Ebell Picnic Area
Eber Creek
Eby School (historical)
Howard Eccles Elementary School
Echart Creek
Echave Reservoir
Echave Well
Echo
Echo Lake
Echo Meadows
Echo Valley
Eckesley Creek
Ecola Creek
Ecola Point
Ecola State Park
Eddy Creek
Eddy Spring
Eddyville
Eden Cemetery
Eden Community Hall
Eden Ridge
Edgewood City Park
Edgewood Ranch
Edgewood Community Elementary School
Edison Elementary School
Edler Spring
Edris Creek
Edward Grenfell County Park
Edwards Butte
Edwards Butte
Edwards Canyon
Edwards Creek
Edwards Creek
Edwin Brown High School
Egan Cabin
Egert Spring
Egg Lake
Eighteenmile Island
Eightmile Canyon
Eightmile Cemetery
Eightmile Reservoir
Eiguren Reservoir
Eiguren Reservoir Number One
Eiguren Reservoir Number Two
Eiguren Spring
Eilertsen Creek
Eilertson Meadow
Elbow Canyon
Elbow Canyon
Elbow Creek
Elbow Creek
Elbow Spring
Elde Flat
Elder Creek
Elder Ranch
Elder Rocks
Elder Spring
Eldorado School
Eldriedge Bar
Eldriedge Slough
Electric Creek
Eleven Horse Reservoir
Elf Lake
Tubman Middle School (historical)
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek Guard Station
Elk Creek Settling Tank
Elk Creek Tunnel Forest State Park
Elk Flat
Elk Flats
Elk Heaven Mine
Gould Lake
Elk Mountain
Elk Mountain
Elk Mountain
Elk Peak
Elk Point
Elk Prairie
Elk Prairie School (historical)
Elk Rock Island
Elk Spring
Elk Spring
Elk Valley
Elk Valley Creek
Elk Wallow Spring
Elkhead Mines
Elkhorn Creek
Elkhorn Creek
Elkhorn Creek
Elkhorn Crest Trail
Elkhorn Peak
Elkhorn Ridge
Elkhorn Spring
Elkton
Ella Butte
Ella Creek
Ellenburg Creek
Ellie Spring
Elliot Ditch
Elliot Mine
Elliott Springs
Ellis Ditch
Ely Canyon
Ely Creek
Emanuel Cemetery
Embree Slough
Emele Ditch
Emerald Park
Emerson Ridge
Emery Canyon
Emery Spring
Emery Spring
Emigrant Buttes
Emigrant Canyon
Emigrant Creek
Emigrant Lake
Emigrant Springs (historical)
Emma Lake
Emma Mine
Endicott Creek
Endicott Creek
Engels Creek
Englewood School (historical)
Ennis Creek
Enright
Ensign Creek
Enterprise Point
Entrance Rear Range Light
Eola Hills
Erickson Lake
Erin Creek
Erin Meadow
Ernie Spring
Esau Canyon
Eskeline Creek
Esmeralda Mine
Esmond Lake
Esplin Reservoir
Essex Springs
Estes Creek
Etna Cemetery
Euchre Butte
Eugene
Eugene Field Elementary School
Sacred Heart Medical Center University District
Eugene Junior Academy (historical)
Eugene Water and Electric Board Canal
Eusabio Ridge
Evans Butte
Evans Creek
Evans Creek
Evans Creek
Evans Gulch
Evans Reservoir
Evans Slough
Evans Valley
Evans Valley Elementary School
Evans Valley School (historical)
Evergreen Cemetery
Evergreen Elementary School
Ewauna Camp
Ewing Creek
Ewing Young Elementary School
Excuse Mine
F Canal
Face Rock
Fadeaway Spring
Fahys Creek
Fahys Lake
Fairbanks Gap
Fairchild Creek
Fairchild Spring
Fairdale (historical)
Fairfield Bar
Fairfield Grange
Fairfield Elementary
Fairhaven Elementary School
Fairmount City Park
Albany Options School
Corvallis Waldorf School
Fairview
Fairview
Fairview Bar
Fairview Bridge
Fairview Cemetery
Fairview Cemetery
Fairview Cemetery
Fairview Cemetery
Fairview Creek
Fairview Creek
Fairview Home
Fairview Home Prigg Cottage
Fairview Lake
Fairview School (historical)
Fairy Flat
Fake Creek
Fake Creek Trail
Falcon Park
Falcon Rock
Falice Creek
Fall Canyon
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek Falls
Fallen Field
Falls City Reservoir
Falls Creek
Falls Creek
False Face Mountain
Fan Creek Campground
Fandango Canyon
Fandora Mine
Fannie Meadows
Fanno
Fanno Creek
Fanno Creek
Fanno Peak
Fanno Ridge
Mount Fanny
Faraday Lake
Farewell Bend
Farewell Bend State Park
Fargher Spring
Farman Creek
Farmer Gulch
Farmers Butte
Farmers Creek
Farmers Ditch
Farmers Ditch
Farmington
Farmington View Elementary School
Farragut City Park
Farrin Camp
Fat Elk Creek
Faubion Elementary School
Faun Creek
Favorite Slough
Fawn Creek
Fawn Creek
Fawn Creek
Fawn Creek
Fawn Peak
Fawn Rock
Fawn Spring
Fawn Spring
Fay Canyon
Fay Lake
Fayetteville
Feather Bed Lake
Feed Canal
Fehrenbacker Reservoir
Feldheimer Ferry
Fells Spring
Felton Creek
Fence Creek
Fence Line Reservoir
Fenceline Spring
Fendall School
Fennell Lake
Fenton Flat
Fenton Flat Reservoir
Fenton Reservoir
Fenton Spring
Ferguson Bridge
Ferguson Elementary School
Ferguson Spring
Fern Creek
Fern Hollow
Fern Ridge
Fern Ridge
Fern Ridge Lake
Fern Spring
Ferndale Elementary School
Fernhill City Park
Fernhill School
Fernvale
Beverly Cleary School
Ferris Creek
Ferry Canyon
Ferry Canyon
Ferry Creek
Ferry Creek
Ferry Creek Reservoir
Ferry Grade
Ferry Springs
Ferry Springs Canyon
Ferry Street Bridge
Fertile Valley Creek
Fichter Canyon
Field Creek
Field Creek
Field Creek Reservoir
Field Spring
Fielder Creek
Fielder Mountain
Fields
Fields Basin Seep Reservoir
Fields Creek
Fields Creek
Fifteenmile Creek
Filler Creek
Filmore School (historical)
Findley Reservoir
Finger Creek
Fingerboard Prairie
Fingers Canyon
Finland Cemetery
Finley Buttes
Finley Corrals
Finn Creek
Finn Rock
Finnegan Canyon
Finnegan Creek
Finney and Egan Lake
Finns Corner
Finster Canyon
Finucane Spring
Fir Butte
Fir Creek
Fir Grove
Fir Grove Primary School
Fir Grove School
Fir Grove School (historical)
Fir Grove Elementary School
Fir Gulch
Fir Hollow
Fir Lake
Fir Point
Fir Spring
Fir Tree Canyon
Fir Tree Spring
Fircrest Cemetery
Fircrest City Park
Fireline Creek
First Canyon
First Creek
First Creek
First Creek
First Creek
First Creek
First Lake
First Pines Hollow
First Sheep Camp Spring
First Swale Creek
Fischers Mill
Fish Creek
Fish Creek
Fish Creek
Fish Creek
Fish Creek
Fish Creek
Fish Creek
Fish Creek
Fish Creek
Fish Creek
Fish Eddy
Fish Fin Rim
Fish Lake
Fish Lake
Fish Lake
Fish Lake
Fish Lake Campground
Fish Lake Guard Station
Fishback Hill
Fisher Canyon
Fisher Creek
Fisher Flat
Fisher Hot Springs
Fisher Lake
Fisherman Camp
Fishers Corner
Fishery Point
Fishhawk Cemetery
Fishhawk Creek
Fishhawk Creek
Fishhawk Falls
Fishhole Guard Station
Fishhole Mountain
Fishing Rock
Fishtrap Cemetery
Fishtrap Creek
Fishtrap Shoal
Fitch Creek
Fitzgerald Lake
Fitzgerald Ranch
Fitzgerald Reservoir
Fitzpatrick Island
Fitzwater Canyon
Fitzwater Spring
Five and Seventenths Canal
Five Cent Lake
Five Dollar Spring
Five Foot Rock
Five Islands Bar
Five Islands
Five Point Canyon
Fivebit Gulch
Fivemile Creek
Fivemile Creek
Fivemile Dam
Fivemile Lake
Fivemile Lock Light
Fivemile Reservoir
Fivemile Spring
Fizzleout Creek
Flag Island
Flagler Creek
Flagpole Ridge
Flagstaff Butte
Flagstaff Gulch
Flagstaff Hill
Flagstaff Lake
Flagstaff Mine
Flanagan
Flannery Gulch
Flat Black Rock
Flat Creek
Flat Creek
Flat Iron Mountain
Flat Rock
Flat Rock Forest Camp
Asa Fleetwood Family Cemetery
Fleming Spring
Fletcher Gulch
Flimflam Creek
Flint Creek
Flint Ridge
Floater Waterhole
Floating Prairie
Flock Mountain
Floeter Pond
Floodwater Flats
Flook Lake
Flook Ranch
Floras Creek
Floras Lake
Florence Creek
Florene Mine
Flournoy Valley
Flowing Well
Flowing Well
Flume Gulch
Fly Creek
Fly Valley
Flybee Lake
Flying M Ranch
Flynn Lake
Fogarty Creek
Fogarty Creek State Park
Foley Creek
Foley Creek
Foley Gulch
Foley Lake
Foley Lakes Reservoir
Foley Peak
Foley Slough
Folly Farm
Folly Farm Flat
Fones Canyon
Fools Hollow
Foot of the Trail Corral
Foots Creek
Foots Creek Chapel
Fopiano Creek
Force Lake
Ford Branch
Ford Cemetery
Lindgren Creek
Ford Ingram Ditch
Fordice Creek
Forest Crossing
Forest Hills Elementary School
Forest Lawn Memorial Park
Forest Park
Forest Peak
Forest Queen
Forrester Cemetery
Forked Canyon
Forks Forest Camp
Forks School (historical)
Forman Canyon
Fort Clatsop National Memorial (historical)
Fort Creek
Fort Rock State Park
Camp Warner (historical)
Fort William Bend
Fortier Field
Fortune Branch
Fortune Branch
Forty-one Ranch
Fortyfour Lake
Foskett Spring
Foss
Fossil
Fossil Park
Fossil Point
Foster Cemetery
Foster Creek
Foster Creek
Foster Lake
Foster Spring
Four Bit Creek
Four Bit Gulch
Four Corners
Four Corners
Four Corners
Four Corners
Four Point Ridge
Four Points Reservoir
Four Seven Ridge
Fourmile
Fourmile Canyon
Fourmile Canyon
Fourmile Gap
Fourmile Spring
Fourth of July Creek
Fourth of July Creek
Fourth of July Spring
Fourth Creek
Fourth Creek Reservoir
Fourth Lake
Fowler Creek
Fowler Junior High School (historical)
Fox Bridge
Fox Canyon
Fox Creek
Fox Creek
Fox Creek
Fox Creek
Fox Creek
Fox Creek
Fox Creek Ridge
Fox Hollow
Fox Lake
Fox Rock
Fox Valley Cemetery
Lake Frances
Francis Creek
Frank Creek
Frank Maher Flat
Frank Schmidt Lake
Franklin Butte
Franklin Butte Cemetery
Franklin High School
Franklin Hill
Franklin City Park
Frantz Spring
Franzen Reservoir
Fraser Canyon
Fraser Canyon
Frazer Creek
Early Head Start Family Center of Portland (historical)
Frazier Creek Ditch
Frazier Mountain
Frazier Spring
Fred Pond
Frederick Butte
Freeman Butte
Freeway Lakes County Park
Freeze Out Gulch
Freezeout Basin
Freezeout Creek
Freezeout Gulch
Freezeout Gulch
Freezeout Lake
Freezeout Reservoir
Freezeout Spring
Freezeout Spring
Freezeout Summit Reservoir
Eagleridge High School
French Cabin
French Canyon
French Charlie Canyon
French Creek
French Creek
French Gulch
French Gulch
French Gulch
French Mountain
French Spring
Frenchie Creek
Frenchy Rapids
Fretwell Reservoir
Frickey Canyon
Friday Meadow
Friday Mine
Friendly City Park
Friendly Reach
Frigid Spring
Frisco Canyon
Frissell Creek
Frissell Point Trail
Fritz Creek
Frog Creek
Frog Creek
Frog Creek
Frog Creek Ditch
Frog Hollow
Frog Spring
Frona County Park
Front Range Light
Frozen Creek
Fruit Creek
Fruit Spring
Fruit Springs
Fruitland
Fruitvale School (historical)
Fry Creek
Fry Gulch
Fry Island
Frying Pan Ranch
Fryingpan Creek
Fuller Canyon
Fulton Canyon
Fulton Ridge
Funnel Canyon
Fir Mountain
G Canal
G I Ranch
G-Three Canal
Gabriel Cemetery
Gacey Spring
Gage Reservoir
Galagher Canyon
Galagher Ridge
Gale Creek
Gales Creek
Gales Creek Cemetery
Gales Creek Childrens Camp
Gales Creek Campground
Galesvale School (historical)
Galesville
Gall Creek
Gallagher Canyon
Gallagher Reservoir
Gallagher Slough
Gallon House Bridge
Galloway (historical)
Galls Creek
Gamber Spring
Gamble Reservoir
Gamebird Park
Game Spring
Games Reservoir
Gammans City Park
Gap
Gap Spring
Garage Creek
Garden Valley
Garden Valley School (historical)
Gardiner Middle School
Gardner Mill Race Ditch
Garibaldi
Garlinghouse Lake
Garlow Butte
Garlow Butte Reservoir
Garlow Butte Spring
Garner Creek
Garrison Lake
Gartin Reservoir
Gary Island
Gasset Bluff
Gassy Creek
Gaston Reservoir
Gooch Falls
Gate Creek
Gate Creek
Gate Spring
Gate Spring Canyon
Gates
Gates Guard Station
Gateway City Park
Catlin Gabel School
Gawley Creek
Gearhart
Gearhart Creek
Gearhart Marsh
Gedney Creek
Gee Creek
Geiger Creek
Geiger Creek Reservoir
Gem (historical)
Gem Mine (historical)
Gene Creek
George Canyon
George Creek
George Creek
George Creek
George Creek
George Henry Gulch
George Middle School
George Spring
George Washington Gulch
Gerber Dam
Gerber Ranch
Gerber Reservoir
Gerber Rim
Gerking Canyon
Gerking Creek
Gerking Flat
Gerlinger County Park
German Cemetery
Gervais
Gethsemani Cemetery
Gettings Creek
Gettys Creek
Guerin Creek
Ghost Camp
Gibbs Cemetery
Gibraltar Mountain
Gibson Canyon
Gibson Canyon
Gibson Drain
Gibson Gulch
Gibson Island
Gift Butte
Gilbert Heights Elementary School
Gilbert River
Gilbreath Creek
Giles Creek
Gilham Elementary School
Gilkey Creek
Gill Creek
Gillespie Butte
Gillespie Cemetery
Gillespie Corners
Gillespie Spring
Gilliam Canyon
Gilmore Creek
Gilmore Peak
Gin Basin
Gin Spring
Ginger Creek
Ginger Creek
Ginger Peak
Ginsberg Point
Girand Homestead
Girds Creek
da Vinci Arts Middle School
Giveout Mountain
Glasgow Butte
Glass Hill
Glass Spring
Glaze Lake
Gleason Butte
Glen Aiken Creek
Glen Avon
Glen Creek
Glencoe Elementary School
Glendale Junction
Glendenning Creek
Gleneden Beach
Glenfair Elementary School
Glengarry Gulch
Glenhaven City Park
Glenhaven School (historical)
Glenn Creek
Glenns Hole
Glide
Glory Hole Placer
Glover Cemetery
Glover Ranch
Glover Reservoir
Glutton Falls
Gnat Creek
Goat Creek
Goat Creek
Goat Point
Goat Ranch
Gobblers Knob
Gobblers Knob
Gobel Draw
Goble Creek
Goble School (historical)
Godfrey Creek
Gods Valley Creek
Goff Mine
Goff Placer
Golconda Mine
Gold Bluff Mine
Gold Bug Gulch
Gold Bug Mine
Gold Bug-Grizzly Mine
Gold Center
Gold Center Meadow
Gold Center Spring
Gold Cliff Gulch
Gold Creek
Gold Creek
Gold Creek
Gold Creek
Gold Creek Reservoir Number One
Gold Creek Reservoir Number Two
Gold Cup Placer
Gold Gulch
Gold Hill
Gold Hill
Gold Hill
Gold Hill Spring
Gold Hill Trail (historical)
Gold Peak
Gold Ray Dam
Gold Ridge
Gold Ridge Mine
Gold Spring
Golden and Silver Falls State Park
Golden Canyon
Golden Eagle Mine
Golden Falls
Golden Gate Canal
Golden Ring Mine
Golden Valley
Goldy Reservoir
Golf Creek
Gooch Meadow
Good Place Reservoir
Goodlow Mountain
Goodlow Rim
Goodman Creek
Goodman Lake
Goodman Spring Branch
Goodpasture Island (historical)
Goodrich Creek
Goodrich Lake
Goods Bridge
Goodwin Peak
Goodwin Tomb
Goodyear Reservoir
Goop Spring
Goose Creek
Goose Creek
Goose Island
Goose Lake
Goose Ranch
Goose Ranch Slough
Goose Rock
Gooseberry Canyon
Gooseberry Cemetery
Gooseberry Creek
Gooseberry Creek
Gooseberry Mountain
Gooseberry Spring
Gooseberry Spring
Gopher Mine
Gordon Butte
Gordon Canyon
Gordon Gulch
Gordon Lakes
Gordon Meadows
Gordon Ridge
Gordon Spring
Gore School (historical)
Gorham Gulch
Gorman Creek
Gosage Creek
Gossett Creek
Gourlay Creek
Government Corral Spring
Government Flat
Government Gulch
Government Hill
Government Island
Government Point
Government Well
Governors Park
Grady Creek
Grafton Well
Graham Canyon
Graham Creek
Graham Lake
Grahams Hill
Grain Camp Dam
Grand Central Mine
Grand Island School (historical)
Grand Prairie School (historical)
Grand Trunk Mine
Grande Ronde Guard Station
Grande Ronde Lake
Grandview Creek
Granite Creek
Granite Creek
Granite Creek Reservoir
Granite Spring
Grant Applegate Bridge
Grant Butte
Grant High School
Grant Island
Grant Meadow
Martin Luther King Junior City Park
Grant Spring
Grant Spring
Grass Butte
Grass Canyon
Grass Valley
Grass Valley Canyon
Grasshopper Flat
Grasshopper Flat
Grasshopper Flat
Grasshopper Spring
Grasshopper Spring
Grasshopper Spring
Grassy Mountain
Grassy Butte
Grassy Butte Reservoir
Grassy Lake
Grassy Lake
Grassy Lake
Grassy Lake Creek
Grassy Mountain
Grassy Mountain
Grassy Mountain
Grassy Mountain Reservoir
Grassy Mountain Spring
Grassy Reservoir
Grassy Ridge
Grassy Spring
Grater Butte
Grave Creek
Grave Creek Bridge
Gravel Creek
Gravel Flat
Gravel Spring
Gravel Spring
Gravel Waterhole
Gravelford
Gravelford Cemetery
Gravelly Cove
Gravelly Gulch
Graves Creek
Graveyard Canyon
Graveyard Point
Gray Buttes
Gray Creek
Gray Creek
Gray Eagle Mine
Gray Park
Gray Ridge
Gray Middle School
Gray Stud Reservoir
Grayback
Grayback Trail
Grays Gulch
Grays Peak
Greaser Basin
Greaser Canyon
Greaser Lake
Greaser Reservoir
Greaser Ridge
Greasewood Canyon
Greasewood Cemetery
Greasewood Creek
Great Spring
Grebe Creek
Greeley Bar
Greeley Reservoir
Green Acres School (historical)
Green Acres School
Green Butte
Green Butte
Green Creek
Green Creek
Green Creek
Green Flat Reservoir
Green Gulch
Green Gulch
Green Gulch Spring
Green Hollow
Green Island
Green Lake
Green Mountain
Green Mountain
Green Mountain
Green Mountain
Green Mountain
Green Mountain Creek
Green Mountain Creek
Green Mountain School (historical)
Green Peak
Green Peak
Green Peak Lake
Green Peter
Green Peter Creek
Green Point
Green Ridge
Green Ridge Creek
Green Elementary School
Green Slough
Green Spring
Green Spring
Green Spring Draw
Green Springs Mountain
Green Timber Creek
Green Top
Green Valley
Green Valley Reservoir
Greenback Mine
Greenberry
Greener Road Trail
Greenhorn Gulch
Greens Gulch
Greenshaw Creek
Greenville (historical)
Greenwood Cemetery
Greenwood Cemetery
Greenwood Hill Cemetery
Gregory Creek
Gregory Creek Reservoir
Roseway Heights School
Gregory Spring
Greiner Canyon
Grenet Lake
Gresham
Gribble Creek
Gribble Prairie
Gribble Spring
Grieb Canyon
Griffin Basin
Griffin Canyon
Griffin Canyon
Griffin Creek
Griffin Creek Elementary School
Griffith Placer
Griffith Reservoir
Griffith Spring Reservoir
Grigsby Rock
Grimes Canyon
Grindy Creek
Helix School
Grizzly Bear Ridge
Grizzly Butte
Grizzly Butte
Grizzly Creek
Grizzly Creek
Grizzly Flat
Grizzly Mountain
Grizzly Mountain
Grizzly Peak
Grizzly Peak
Grizzly Slough
Grohe Creek
Gross Creek
Gross Mountain
Groundhog Falls
Groundhog Gulch
Groundhog Reservoir
Grouse Canyon
Grouse Creek
Grouse Creek
Grouse Creek
Grouse Flat
Grouse Flat
Grouse Gulch
Grouse Prairie
Grouse Springs
Grouse Spring
Grout Elementary School
Grove Creek
Grove Creek
Grove Gulch
Grub Hollow Creek
Guano Canyon
Guano Creek
Guano Reservoir
Guano Rim
Guano Slough
Guano Valley
Guiles Lake
Guiley Creek
Gull Island
Gull Island Turn and Channel
Gull Rock
Gull Rock
Gull Rock
Gum Creek
Gun Club Canyon
Gunkel Ranch
Gunners Lakes
Gunsight Mountain
Gunsight Pass
Gunter
Gurdane Cemetery
Gus Creek
Guthrie Community Park
Guyton Canyon
Gwendolen
Gwendolen Canyon
H J Andrews Monument
H L Creek
H L Ranch
H Taylor Creek
Hadleyville School (historical)
Hagerty Ridge
Hahn Canyon
Haight Creek
Haines
Haines Falls
Haines Lake
Haines Pond Number One
Haines Pond Number Two
Hale Butte
Hale Ridge
Haley
Half Moon Bend
Halfway Creek
Pine Ranger Station
Halfway Reservoir
Hall Creek
Hall Creek
Hall Creek
Hall Creek
Halladay Gulch
Halladay Spring
Halls Ferry
Halo Creek
Halo Valley
Halsey
Ham Brown Lake
Ham Waterhole
Hamaker Canyon
Hamaker Spring
Hambrick Creek
Hamer Spring
Hamilton Creek
Hamilton Creek
Hamilton Creek School
Hamilton Ranch
Hamlet Grange
Hamlin Middle School
Hammel Lateral
Hammer Creek
Hammersly Mine
Hammon Creek
Hammond
Hammond Camp
Hammond Creek
Hancock Canyon
Hancock Creek
Hancock Creek
Hand Lake Trail
Hands Creek
Handy Creek
Haney Creek
Haney Creek
Haney Ridge
Hanging Rock Spring
Hanks Marsh
Hanley Hill
Hanlon Creek
Hanna Creek
Hanna Reservoir
Hannafin Canyon
Hannavan Creek
Hanns Creek
Hanover (historical)
Hansen Gulch
Hanson Canyon
Hanson Canyon Reservoir
Hanson Creek
Hanson Reservoir Number Two
Hanson Waterhole
Hantz Creek
Happy Camp Recreation Site
Happy Camp Creek
Happy Camp Creek
Happy Canyon
Happy Hollow
Happy Jack Canyon
Happy Valley
Happy Valley
Happy Valley
Happy Valley
Happy Valley Cemetery
Happy Valley Reservoir
Happy Valley Elementary School
Harbison Spring
Hard Rock Reservoir
Hard Time Reservoir
Hard Up Point
Hardenbrook Creek
Hardin Spring
Hardman Cemetery
Hardscrabble Creek
Hardscrabble Quarry
Hardscrable Creek
Hardtack Island
Hardy Creek
Hargadine Spring
Harkens Lake
Harlan
Harliss Creek
Harmony
Harmony School (historical)
Harms Creek
Harness Mountain
Harney Lake
Harper Basin Reservoir
Harper Basin Spring
Harper Creek
Harper Mountain
Harper Road Reservoir
Harper Valley
Harrington Canyon
Harrington Creek
Harrington Point Range
Harris Bridge
Harris Canyon
Harris Canyon
Harris Cemetery
Harris Creek
Harris Creek
Harris Gulch
Harris Island
Camas Ridge Community School
Harris Private School
Harrisburg
Harrisburg Substation
Harrison Creek
Harry Creek
Harry Page Reservoir
Harry Spring
Harshman Canyon
Hart Canyon
Hart Creek
Hart Creek Reservoir
Hart Lake
Hart Spring
Hart Spring
Hart Spring
Hartman Reservoir
Hartman Slough
Hartwick Reservoir
Harvey Canyon
Harvey Creek
Haskell Reservoir
Haskins Creek
Haskins Creek Reservoir
Hastings Peak
Hat Butte
Hatt Butte
Hat Butte Waterhole
Hat Rock
Hat Rock
Hat Rock State Park
Hat Top
Hatcher Creek
Hatchery Creek
Hatchery Creek
Hatchet Slough
Hathaway Slough
Hatley Springs
Hauser Canyon
Haven Island
Hawk Canyon
Hawk Spring
Hawkins Hill Reservoir
Hawkins Lake
Hawkins Lake
Hawkins Pit
Hawkins Spring
Hawks Nest Reservoir
Hawks Valley
Hawley Canyon
Hawley Creek
Hawley Creek
Hawthorne Bridge
Pendleton Education Center
Hawthorne Springs
Haxel Creek
Hay Bottom Canyon
Hay Canyon
Hay Canyon
Hay Corral Spring
Hay Creek
Hay Creek
Hay Creek
Hay Creek Butte
Hayden Bridge
Hayden Creek
Hayden Island
Hayden Island
Hayden Mountain
Hayes Butte
Hayes Canyon
Hayes Creek
Hayes Creek
Hayes Creek
Hayes Ranch
Hayes Ridge
Hayhurst Elementary School
Hayhurst Valley
Haynes Creek
Hays Cemetery
Haystack Meadows
Haystack Rock
Haystack Rock
Haystack Rock
Hayward Creek
Hazel Green
Hazel Green Elementary School
Hazeldale Elementary School
Head of the Creek Waterhole
Head of Keeney Creek Reservoir
Head of River Spring
Head of Hoodoo Reservoir
Heads Waterhole
Headwater Reservoir
Healy Heights City Park
Heany Spring
Heart Lake
Heart Lake
Heath Creek
Heath Lake
Heaton Creek
Hebron Church (historical)
Heceta Beach
Heckard Creek
Heddin Creek
Heedie Spring
Hefty Creek
Hehe Butte
Hehe Mountain
Heidtmann Canyon
Heidtmann Mountain
Heifer Creek
Heiney Creek
Helix
Helix Cemetery
Hellgate
Helloff Creek
Hellroaring Canyon
Hells Half Acre
Hells Hill
Helm Springs
Helpful Spring
Helvetia
Hemmy Cabin
Henderson Creek
Henderson Hollow
Henderson Pioneer Cemetery
Hendricks Bridge County Park
Hendricks City Park
Hendrickson Creek
Hendrix Siphon
Henrici Lake
Henry Basin
Henry Creek
Henry Creek
Henry Gulch
Henrys Falls
Heppner
Heppner City Well
Herculean Mine
Hereford Spring
Hergert Quarry
Herlihy Canyon
Herman Creek
Hermann Cemetery
Hermiston Butte
Hermiston Ditch
Hermiston Junction
Hermiston State Game Farm
Herndon Canyon
Hervey Bridge
Hervey Gulch
Hervey Quarry
Hess Creek
Hess Ranch
Hibbard Creek
Hibbard Gulch
Hibbert Cemetery
Hickerson Gulch
Hickey Basin
Hickey Creek
Hickey Spring
Hicks Creek
Hidden Lake
Hidden Lake
Hidden Reservoir
Hidden Reservoir
Hidden Seep
Hidden Spring
Hidden Spring
Hidden Treasure Mine
Hidden Valley
Hidden Valley
Hidden Valley
Hide and Seek Creek
Higgins Reservoir
High Butte
High Butte Reservoir
High Line Canal
High Line Canal
High Line Ditch
High Line Ditch
High Mountain
High Point
High Point
High Ridge
High Rim Waterhole
High Rock
Estacada High School
High Summit Spring
High Up Spring
High Valley
Highland Butte
Highland Cemetery
Highland Cemetery
Highland Mine
King Elementary School
Highland Spring
Highland Trail
Highline Ditch
Highview Cemetery
Highway Spring
Hilario Spring
Hilgard Cemetery
Hill Camp Spring
Hill - Dunn Cemetery
Hill Creek
Hill Creek
Hill Creek
Hill Spring
Hill Spring
Robert S Farrell High School
Hills
Hills Creek
Hillsboro Reservoir
Hilltop Reservoir
George Himes City Park
Hines
Hinkle Butte
Hinkle Creek
Hinkle Yards
Hinton Creek
Hinton Creek
Hinton-Ward Ranch
Hirsch Reservoir
Hitching Post Water Hole
Hiway Spring Number One
Hoacum Island
Hobart Bluff
Hobart Butte
Hobart Creek
Hobart Lake
Hobson Creek
Hobson - Whitney Cemetery
Hobsonville
Hobsonville Point
Hodge Pass
Hodges Creek
Hodgson Canyon
Hofer Pond
Hoffer Lakes
Hoffman Dam
Hoffman Hill
Hoffman Memorial State Park
Hog Creek
Hog Creek
Hog Creek
Hog Creek
Hog Creek Reservoir Number One
Hog Gulch
Hog Hollow
Hog Leg Reservoir
Hog Mountain
Hog Ranch Creek
Hog Ridge
Hog Wallow Spring
Hogan
Hogan Creek
Hogback Creek
Hogback Mountain
Hogback Ridge
Hogback Well
Hoghouse Canyon
Hogum Creek
Holbrook Reservoir
Holbrook School (historical)
Holcomb Springs
Holcomb Creek
Holcomb Creek
Holcomb Lake
Holcomb School (historical)
Holcomb Spring
Holden Creek
Holdman
Holdman Cemetery
Holdout Reservoir
Holdridge Creek
Holdup Rock
Hole in the Ground
Hole in the Ground
Hole in the Ground
Hole in the Ground
Hole in the Ground Lake
Hole in the Ground
Hole in the Ground
Hole in the Ground
Hole in the Rock
Hole in Rocks
Hole in the Ground
Hole in the Ground
Hole Creek
Hole in Ground
Hole in Wall Rock
Holladay School (historical)
Holley
Hollowfield Canyon
Holly Drain
Hollywood Camp OHV Staging Area
Holman Creek
Holman Guard Station
Holman Spring
Holmes Canyon
Holmes Creek
Holmes Creek
Holmes Gap
Holmes Hill
Holmes Meadow
Rose City Cooperative Preschool
Holy Cross Catholic School
Holy Family School
Holy Redeemer School
Holy Rosary Church
Home Creek
Home Creek Butte
Home Creek Ranch
Home Sweet Home Spring
Homeli Cemetery
Homestead
Homestead Creek
Homestead Gulch
Homestead Hole
Homestead Reservoir
Homestead Ridge
Homestead Spring
Homestead Spring
Homestead Spring
Hon Gulch
Honey Creek
Honeyman Creek
Honeymoon Lake
Honeysuckle Creek
Hood River Mountain
Hood View Junior Academy
Hoodlum Canyon
Hoodoo Butte
Hoodoo Creek
Hoodoo Creek
Hoodoo Ridge
Hoodoo Spring
Hoodoo Spring
Hoodoo Trail
Hoogie Doogie Mountain
Hooker Gulch
Hoot Owl Canyon
Hoot Owl Spring
Hoover Creek
Hoover Elementary School
Hope Butte
Hope Drain
Hope Flat
Hope School (historical)
Hopkins Canal
Hopper Hill
Hopville
Horn Butte
Horn Creek
Horn Creek
Horn Spring
Horn Waterhole
Horncrist Spring
Horse Camp Rim
Horse Creek
Horse Creek
Horse Creek
Horse Creek
Horse Creek
Horse Creek Group Camp
Horse Creek Spring
Horse Flat
Horse Flat Reservoir
Horse Glade
Horse Heaven
Horse Heaven Mine
Horse Heaven Mountain
Horse Hill
Horse Hollow
Horse Hollow
Horse Lake
Horse Meadow
Horse Mountain
Horse Mountain
Horse Mountain
Horse Pasture Spring
Horse Prairie
Horse Prairie
Horse Range
Horse Range Camp (historical)
Horse Ridge
Horse Rock
Horse Spring
Horse Spring
Horse Spring
Horse Trap Spring
Horsefly Mountain
Horsehead Lake
Horsehead Spring
Horseshoe Island
Horseshoe Ridge
Horsepasture Lake
Horsepasture Mountain
Horsepasture Pass Shelter (historical)
Horseshoe Basin
Horseshoe Bend
Whistlers Bend
Horseshoe Bend
Horseshoe Bend
Horseshoe Bend
Horseshoe Creek
Horseshoe Creek
Horseshoe Curve
Horseshoe Falls
Horseshoe Falls Light
Horseshoe Island
Horseshoe Lake
Horseshoe Lake
Horseshoe Lode
Horseshoe Reservoir
Horseshoe Spring
Horsetail Reservoir
Hortill Creek
Horton Creek
Hosford Middle School
Hoskins Canyon
Hoskins Spring
Hot Creek
Hot Spring
Hot Spring
Crane Hot Springs
Hot Spring
Hot Spring
O'Neil Hot Springs
Hot Spring
Hot Springs Slough
Hot Springs
Hot Springs
Borax Hot Springs
Hot Springs
Hot Springs Campground (historical)
Hot Springs Creek
Hotchkiss Ranch
Houghton Creek
A C Houghton Elementary School
House Butte
House Creek
Houselog Creek
Howard Canyon
Howard Canyon
Howard Creek
Howard Creek
Howard Meadow
Howard Meadow Trail
Howard Elementary School
Howard Elementary School
Howell Canyon
Howell Cemetery
Howell Creek
Howell Lake
Howell Lake
Howell Prairie
Hoyt Arboretum
Hoyt Creek
Hoyts Hole
Hubbard Cemetery
Hubbard Lake
Hubbard Creek
Hubble Ditch
Huber County Park
Huckleberry Creek
Huckleberry Creek
Huckleberry Mine
Huckleberry Spring
Huckleberry Trail
Hudson Bay Canal
Hudson Country Park
Hudson Creek
Hudson School (historical)
Hudspeth Corral
Hudspeth Cow Camp
Huff Creek
Huffman Camp
Huffman Island
Hufford Bridge (historical)
Hug Point
Hugg Creek
Hughes Canyon
Hughes Gulch
Hughes Ranch
Hughet Creek
Hughet Lake
Hughet Spring
Hulbert Lake
Hulburt School (historical)
Hull Mountain
Hull Spring
Hultin Cemetery
Humboldt Mine
Humboldt Elementary School
Humbug Creek
Humbug Creek
Humbug Point
Hummingbird Spring
Humphrey Ranch
Hungry Hill
Hungry Hill
Hungry Hollow
Hungry Hollow
Hungry Mountain
Hunt Butte
Hunt Canyon
Hunt Creek
Hunt Creek
Hunt Ditch
Hunt Mountain
Hunt Ranch
Hunter Bar
Hunter Cabin (historical)
Hunter Campground
Hunter Creek
Hunter Creek
Hunter Creek
Hunter Creek Reservoir
Hunter Gulch
Hunter Lake
Hunter Peak
Hunter Ranch
Hunter Ranch Reservoir
Hunter Spring
Hunter Spring
Hunter Spring
Hunter Spring
Huntington
Huntington Creek
Huntit Spring
Huntley Canyon
Huntley Creek
Hunts Mill Point
Hurlburt Flats
Hurley Flat
Hurley Reservoir
Hurley Spring
Hurley Spring Creek
Huskey Flat
Huston Canyon
Hutchinson Ditch
Hutchinson Hill
Hutchinson State Park
Hyatt Reservoir
Hyde Ridge
Hyline Hall
Ibex Mine
Icecap Spring
Ickes School (historical)
Idlewild Creek
Idleyld Park
Igo Butte
Igo Cemetery
Iler Creek
Illingsworth Creek
Ilwaco Channel
Imnaha Falls
Muddy Creek Charter School
Independence Creek
Independence Rock
Indian Agency Headquarters
Indian Arrows
Indian Beach
Indian Camp Reservoir
Indian Canyon
Indian Canyon
Indian Canyon Reservoir
Indian Ceremonial Ground
Indian Cove
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek Buttes
Indian Creek Camp
Indian Flat
Indian Fort
Indian Fort Cabin
Indian Fort Flat
Indian Fort Reservoir
Indian Fort Ridge
Indian Garden
Indian Grade Spring
Indian Gulch
Indian Head
Indian Head Canyon
Indian Hollow
Indian Hollow
Indian John Island
Indian Lake
Indian Point
Indian Prairie
Indian Prairie Creek
Indian Prairie Lake
Indian Rocks
Indian Spring
Indian Spring
Indian Spring
Indian Spring
Indian Spring Canyon
Indian Spring Flat
Indian Spring Ridge
Indian Spring Ridge
Indian Springs
Indigo Creek
Industry Creek
Ingram Camp
Ingram Guard Station
Ingram Island
Ingram Slough
Ingram Spring
Inman Cemetery
Inman Creek
Interstate Bridge
Ireland Spring
Irish Bend
Irish Bend School (historical)
Irish Camp Lake
Irish Lake
Irish Spring
Iron Door Mine
Iron Gulch
Iron King Mine
Iron Mountain
Iron Mountain
Iron Mountain
Iron Mountain
Iron Mountain
Iron Mountain
Iron Mountain
Iron Mountain Creek
Iron Mountain Flat
Iron Mountain Canyon
Iron Point
Iron Point Reservoir
Irrigon Cemetery (historical)
Irving City Park
Irving Elementary School
Irving Spring
Irwin Rocks
Irwins Pump
Mount Isaac
Mount Isabelle
Ish Tish Creek
Isham Spring
Island Branch
Island Creek
Island Lake
Island Park
Island Ranch
Island Reservoir
Island Windmill
Israel Well
Isthmus Slough
Iven Stephens Homestead
Ivers Spring
Ivy Creek
Ivy May Mine
J C L Mine
J Canal
JD Reservoir
Jennie B Harris County Park
J N Bishop Spring
J Spring
J-H Canal
J-1 Canal
Jaca Reservoir
Jack Canyon
Jack Canyon
Jack Creek
Jack Creek
Jack Creek
Jack Creek
Jack Creek
Jack Creek
Jack Creek
Jack Falls
Jack Flat
Jack Frost Spring
Jack Hays Creek
Jack Horner Creek
Jack Lake
Jack McCord Spring
Jack Mountain
Jack Slough
Jack Spring
Jack Well
Jack Wilson Spring
Jackass Butte
Jackass Canyon
Jackass Mountain
Jackass Prairie
Jackass Spring
Jackass Spring
Jackies Butte
Jackknife Canyon
Jackknife Spring
Jackman Park
Jackpot Mine
Jacks Canyon
Jacks Spring
Jackson Bend
Jackson Bottom
Jackson Family Cemetery
Jackson Creek
Jackson Creek
Jackson Creek
Jackson Creek
Jackson Creek
Jackson Creek Reservoir
Jackson Falls
Jackson Gulch
Jackson Hole
Jackson Reservoir
Jackson Reservoir
Jackson Elementary School
Jackson Slough
Jacksonville
Jacktown
Jacobs Reservoir
Jacobsen Ditch
Jacobsen Gulch
Jacoby Creek
Jade Creek
Jake Hughes Reservoir
James Butte
James Canyon
Madison Middle School
James Park
James Spring
James Wood Park
Jameson Canyon
Jameson Creek
Jamieson Gulch
Jamison Gulch
Janssen Ranch
Janssen Spring
January Creek
Jasper Creek
Jaycee Park
Jean
Jean Baptiste Charbonneau Grave
Jeep Ride Spring
Jeeter Creek
Jeff Davis Creek
Jeffers Creek
Jeffers Slough
Jefferson High School
Arts and Technology Academy
Jefferson School (historical)
Jefferson School (historical)
Jeffries Creek
Jenkins Creek
Jenkins Reservoir
Jennette Spring
Jennies Peak
Jennies Peak Canyon
Jennings Creek
Jennison Gulch
Jenny Spring
Jenkins Ranch
Jenkins Reservoir Number One
Jerry Canyon
Jerry Creek
Jerry Flat
Jersey School Spring
Jerusalem Creek
Jessie Flat
Jessie Hill School (historical)
Jesuit High School
Jett Creek
Jetty Creek
Jetty Sands
Jewell Junction
Jewit Lake
Jim Blaine Mine
Jim Belieu Creek
Bridger Elementary School
Jim Creek
Jim Crow Sands (historical)
Jim Hunt Creek
Jimmy Creek
Jimmy Creek
Jims Reservoir
Jims Valley
Jo Jo Lake
Joaquin Reservoir
Jockey Cap
Joe Creek
Joe Dyer Butte
Joe Huff Spring
Joes Camp Canyon
Joes Creek
John B Creek
John Cabin Spring
John Day Creek
John Day Dam
John Day Gulch
John Day Point
John Day River
John Day Substation
John Day Wildlife Management Area
John F Kennedy High School
Kennedy Middle School
Astor Elementary School
John Spring
John Tuck Elementary School
Johney Creek
Johnny Creek
Johnny Creek
Johnny Kirk Spring
Johns Canyon
Johns Creek
Johns Peak
Johnson Boulder Creek
Johnson Canyon
Johnson Canyon
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek City Park
Johnson Draw
Johnson Gulch
Johnson Gulch
Johnson Heights
Johnson Hollow
Johnson Island
Johnson Landing
Johnson Ranch
Johnson Ranch
Johnson Ranch
Johnson Ridge
Johnson Rock
Johnson Saddle
Johnson Slough
Johnson Spring
Johnson Spring
Jonas Creek
Jones and Ausmus Flat
Jones Butte
Jones Canyon
Jones Canyon
Jones Canyon
Jones Canyon
Jones Canyon
Jones Creek
Jones Creek
Jones Creek
Jones Creek
Jones Creek
Jones Ditch
Jones Hill
Jones Horse Camp
Jones Reservoir Number One
Jones School (historical)
Jones Springs
Jordan
Jordan Butte
Jordan Canyon
Jordan Canyon
Jordan Craters
Jordan Creek
Jordan Creek
Jordan Creek
Jordan Creek
Jordan Creek
Jordan Creek
Jordan Creek
Jordan Creek Canyon
Jordan Drain
Jordan Guard Station
Jordan Ranch
Jordan Spring
Jordan Valley
Jordan Valley
Jory Basin
Jory Canyon
Jory Cemetery
Jory Creek
Jory Hill
Joryville County Park
Joseph Lane Middle School
Joy Creek
Joyce Creek
J S Burres State Park
Judah Parker County Park
Judd Creek
Judkins Point
Judson College (historical)
Judson Landing
July Spring
Jumbo Ridge
Jumbo Springs
Jump Off Joe Canyon
Jumpoff Canyon
Jumpoff Joe
Jumpoff Joe
Jumpoff Joe Creek
Jumpoff Joe Mountain
Junction City Substation
Junction Lake
June Spring
Juniper Basin
Juniper Basin Creek
Juniper Basin Reservoir
Juniper Bed Grounds
Juniper Canyon
Juniper Canyon
Juniper Canyon
Juniper Canyon
Juniper Canyon
Juniper Canyon
Juniper Canyon
Juniper Canyon
Juniper Canyon
Juniper Canyon
Juniper Canyon
Juniper Canyon Reservoir
Juniper Creek
Juniper Creek
Juniper Creek
Juniper Creek
Juniper Creek
Juniper Creek
Juniper Creek
Juniper Creek
Juniper Creek Reservoir
Juniper Flat
Juniper Grade
Juniper Gulch
Juniper Gulch
Juniper Gulch
Juniper Gulch
Juniper Gulch
Juniper Hill Spring
Juniper Lake
Juniper Mountain
Juniper Mountain
Juniper Mountain Ranch
Juniper Park Ranch
Juniper Point
Juniper Point Reservoir
Juniper Ranch Reservoir
Juniper Reservoir
Juniper Ridge
Juniper Ridge
Juniper Ridge
Juniper Ridge
Juniper Spring
Juniper Spring
Juniper Spring
Juniper Spring
Juniper Spring
Juniper Spring
Juniper Spring
Juniper Spring Draw
Juniper Spring Reservoir
Juniper Tree Reservoir
Junkins Cemetery
Juntura Cemetery
Juntura Valley
Jurries Springs
Kaiser Creek
Kalama Lower Range
Kalama Upper Range
Kane Creek
Kane Creek
Kane Creek
Kane Spring Gulch
Kane Spring Reservoir
Kane Springs
Kangaroo Basin
Kanine Ridge
Kansas Creek
Kanutchan Creek
Karlen Draw
Karlson Island
Kaser Butte
Kaser Ridge
Katsuk Butte
Keating
Keck Canyon
Keck Slough
Keene Reservoir
Keeney Creek
Keeney Creek Reservoir Number Two
Keeney Creek Reservoir Number Three
Keeney Creek Reservoir Number Four
Keeney Creek Spring
Keeney Ridge
Keenig Creek
Keesneck Lake
Keeton Spring
Kegler Butte
Kegler Lake
Keller Bridge
Kelley Field
Kelley Point
Kellogg
Kellogg Creek
Kellogg Grange
Kellogg Lake
Kellogg Middle School (historical)
Kelly Butte
Kelly Butte
Kelly Butte
Kelly Creek
Kelley Creek
Kelley Creek
Kelly Creek
Kelly Creek
Kelly Mine
Albert Kelly City Park
Kelly Elementary School
Kelly Slough
Kellys Bluff
Kelsay Canyon
Kelsey Spring
Kelsey Wilson Ditch
Kelso
Kenilworth City Park
Kennedy Creek
Kennedy Ditch
Kennedy Gulch
Kennedy School (historical)
Kenneth Spring
Kenny Spring
Kenny Spring
Keno
Keno Guard Station
Keno Reservoir
Keno Springs Ranch
Kent
Kent Creek
Kenton City Park
Kenton Elementary School (historical)
Kenton Yard
Kentucky Butte
Kentucky Canyon
Kentucky Flat
Kentucky Ridge
Kenusky Creek
Kenyon Mountain
Kern Basin
Kern Creek
Kern Reservoir
Kerns School (historical)
Kerns Waterhole
Kernville
Kerr Canyon
Kaseberg Canyon
Kessler Creek
Keuny Cabin (historical)
Key Cemetery
Keystone Creek
Keystone Mine
Kibby Canyon
Kid Flat Reservoir
Kidney Lake
Kiger Creek
Kiger Cutoff
Kiger Gorge
Kilchis Lookout (historical)
Kilchis River County Park
Kilgore Reservoir
Kilgore Spring
Kilkenny Fork
Killamacue Creek
Killamacue Lake
Kimball Creek
Kimball Flat
Kimball Hill
Kincaid Canyon
Kincaid City Park
Kincheloe Point
King Brown Cabin (historical)
King Cabin Canyon
King Camp
King Canyon
King Canyon
King Canyon
King Creek
King Creek
King Creek
King Creek
King Creek
King Creek
King Drain
King Mountain
King Mountain Truck Trail
King of Peace Cemetery
King Ranch
King Ranch
King Elementary School
King Spring
King Spring
King Well
Kingman Drain
Kingman Lateral
Kingry Marsh
Kings Corner
Kings Heights
Kings Valley
Kings Valley
Kings Valley Cemetery
Kingsbury Gulch
Kingsley
Kingsley Cemetery
Kingsley City Park
Kingston
Kink Creek
Kinney Canyon
Kinney Creek
Kinney Park
Kinsey Creek
Kinton
Kirby Reservoir
Kirk Creek
Kirkbride Canyon
Kirkendall Branch
Kist Creek
Kit Canyon
Kitchen Creek
Kitchen Gulch
Kitts Mill
Kiwanis Camp
Kiwanis Park
Kizer Creek
Kizer Slough
Klamath Creek
Klamath Junction (historical)
Klamath Memorial Park
Klaskanine River
Klaus Ranch
Klickitat Creek
Klindt Point
Klines Creek
Klipple Lake
Kloan (historical)
Klooqueh Rock
Klootchie Creek
Kloster Mountain
Klum Cemetery
Knapp Creek
Knappa Guard Station
Knappa Junction
Knappa Slough
Knickerson Creek
Knieriem Canyon
Knife Creek
Knight Creek
Frank L Knight City Park
Knighten Creek
Knights of Pythias Cemetery
Knights of Pythias Cemetery
Knob Reservoir
Knobs Sheep Camp
Parkrose Knott Street School (historical)
Knottingham Butte
Knottingham Reservoir
Knowland Slough
Knox Butte Cemetery
Knox Butte School (historical)
Knox Canyon
Knox Pond
Knox Ranch
Knox Spring
Knucklebone Reservoir
Kokel Corner
Kool Spring
Koontz Creek
Koontz Creek
Koontz Homestead
Koosah Falls
Kotzman Butte
Kramer Canyon
Krewson Creek
Kronenberg Cemetery
Krueger Field
Krueger Spring
Krugur Park
Krumbo Butte
Krumbo Canal
Krumbo Creek
Krumbo Mountain
Krumbo Reservoir
Krumbo Ridge
Krumbo Springs
Krumbo Springs
Kuckup Spring
Kuder Creek
Kueny Canyon
Kueny Ditch
Kueny Ranch
Hunegs Reservoir
Kuhnert Quarry
Kuitan Lake
Kuks Canyon
Kundert Reservoir
Kutch Creek
Kuykendahl Gulch
Kyhoya Waterhole
Kyle Creek
Kyle Lake
Kyle Spring
La Bleu School (historical)
La Clair Spring
La Grande Reservoir
La Marr Gulch
Louse Canyon
La Toutena Mary Creek
La Toutena Mary Spring
La Voy Lakes
La Voy Tables
LaFollette Butte
Lace Camp
Lacomb
Lacomb Cemetery
Lacomb Irrigation Canal
Ladd Canyon
Ladd Canyon Pond
Ladd Creek
Ladd Creek Pickup Ditch
Lafayette Elementary School
Lake Bed Waterhole
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek School (historical)
Lake Grove Park
Lake Grove Elementary School
Lake Labish
Lake Labish Elementary School
Lake Oswego Junior High School
Lake Oswego Senior High School
Lake Owyhee State Park
Lake Ridge
Lake Ridge
Lake Ridge Reservoir
Lake Ridge Spring
Lake Slough
Lake Spring
Lake Yard
Lakebed Waterhole
Lakebed Waterhole
Lakebrook
Lakewood Bay
Lakewood School (historical)
Lamb Butte
Cecil Lake
Lamb Ranch
Lamb Spring
Lamberson Canyon
Lambert Bend
Lambert Gardens
Lambert Rocks
Lambert Slough
Lambing Camp Canyon
Lambing Canyon
Lampa Creek
Ben Hur Lampman State Park
Lancaster
Lancaster Creek
Landers Canyon
Landrith Bridge (historical)
Lane College (historical)
Lane Community College (historical)
Lane Creek
Lane Creek
Lane Creek
Lane Creek
Lane Creek
Lane Memorial Gardens - Lane Memorial Funeral Home
Lane Ranch
Lane Middle School
Lane Spring
Lane Substation
Lang Canyon
Langdon Creek
Langel Creek
Langell Ridge
Langell Valley
Langlois
Langlois Creek
Langrell Gulch
Langslet Monument Rest Area
Lantern Flat
Lapham Creek
Lapham Ranch
Lapham Reservoir
Larch Mountain
Large Brown Rock
Larsen Creek
Larsen Creek
Larson Cove
Larson Creek
Larson Spring
Last Chance Creek
Last Chance Mine
Last Chance Spring
Last Chance Reservoir
Lateral C
Lateral F
Latigo Lake
Laughlin Creek
Laughlin Hollow
Laurel
Laurel Creek
Laurel Grove
Laurel Hill Cemetery
Laurel Hill City Park
Laurel Hill School (historical)
Laurel Hollow
Laurel Lake
Laurel Mountain
Laurel Ridge
Laurel Elementary School
Laurelhurst City Park
Laurelhurst Elementary School
Lauserica Camp
Lava Butte
Lava Creek
Lava Reservoir
Lava Rock School (historical)
Lava Sinks Reservoir
Lava Trail
Lava Well
LaVerne County Park
Laverne Falls
Lawhorne Creek
Lawler Canyon
Lawrence Creek
Lawrence Creek
Lawrence Ranch
Laxson Park
Laxstrom Gulch
Laycock Creek
Lazarus Island
Lazy Creek
Lazy Man Reservoir
Le Duc Well
Leaburg
Leaburg Dam
Lead Lode Mine
Leaky Reservoir
Leary Lake
Lebanon Santiam Canal
Lebanon Substation
Lee Creek
Lee Creek
Lee Falls
Lee Morris Spring
Guy Lee Elementary School
Lee Elementary School
Lee Thomas Recreation Site
Lee Valley
Leep Creek
Lees Camp
Lees Creek
Lees Peak
Leewood Camp
Left Fork Fielder Creek
Left Fork Foots Creek
Left Fork Sardine Creek
Left Hand Canyon
Left Hand Creek
Leinenweber Lake
Lelliot Spring
Lemon Island
Leniger Spring
Lents
Lents Junction (historical)
Lents Park
Lent Elementary School
Lenz Lateral
Leonard Canyon
Leonard Creek
Leppy Reservoir
Lequerica Trap
Leslie Gulch
Levanger Well
Levens Gulch
Levens Ledge Mine
Levi Spring
Lewis and Clark River
Lewis and Clark Elementary School
Lewis and Clark College
Lewis and Clark State Park
Lewis Creek
Lewis Creek
Lewis Pond
Lewis Elementary School
Lexington Cemetery
Libby Arm
Libby Mine
Liberal
Liberty (historical)
Liberty Cemetery
Liberty School (historical)
Liberty School (historical)
Liberty School (historical)
Lick Creek
Lick Creek
Lick Creek
Lick Creek
Lick Spring
Licklider Reservoir
Liechti Pond
Lifesaving Creek
Light Peak
Lightle Flat
Lillian Creek
Lilly Pump
Lily Lake
Lilypad Lake
Limber Jim Creek
Limber Jim Meadow
Limber Jim Ridge
Limber Jim Trail
Limberlost Recreation Site
Limekiln Creek
Limestone Butte
Lincoln Bar
Lincoln Bench
Lincoln Bench Reservoir
Lincoln Creek
Lincoln High School
Lincoln Memorial Cemetery
Lincoln Rocks
Lincoln Elementary School
Lincoln School (historical)
Lincoln Primary School
Lincoln School (historical)
Lindbergh
Lindbergh School (historical)
Linder Basin
Lindsay Lake
Lindsley Creek
Line Bluff
Line Canyon
Linebaugh Ranch (historical)
Linglebeck Creek
Link (historical)
Link Lake
Linton Falls
Linton Lake
Lion Rock
Lions Lake
Little Abiqua Creek
Little Alder Creek
Little Alkali Spring
Little Alvord Creek
Little Antelope Reservoir
Little Antone Creek
Little Bald Mountain
Little Baldwin Creek
Little Baldy
Little Bear Creek
Little Bear Creek
Little Bear Creek
Little Beaver Creek
Little Beaver Creek
Little Beaver Creek
Little Beaver Ridge
Little Black Canyon
Little Blind Spring
Little Blitzen River
Little Boulder Creek
Little Boulder Creek
Little Boulder Creek
Little Bridge Creek
Little Buck Canyon
Little Bull Creek Reservoir
Little Bull Run
Little Butcher Flat
Little Butte Creek Siphon
Little Butter Creek
Little Camp Creek
Little Carlisle Creek
Little Catherine Creek
Little Catherine Meadows
Little Cedar Creek
Little Cherry Creek
Little Cincha Lake
Little Clatskanie River
Little Clear Creek
Little Coffeepot Creek
Little Coffeepot Spring
Little Cottonwood Creek
Little Cottonwood Creek
Little Cougar Creek
Little Cove
Little Cove Creek
Little Cow Creek
Little Coyote Canyon
Little Cracker Creek
Little Crane Creek
Little Crater Reservoir
Little Creek
Little Creek
Little Creek
Little Creek
Little Creek Spring
Little Crowley Creek
Little Crowley Springs
Little Dads Creek
Little Deacon Creek
Little Dead Dog Canyon
Little Dean Creek
Little Deer Creek
Little Deer Creek
Little Deer Creek
Little Doe Creek
Little Draw
Little Dry Creek
Little Dry Creek
Little Duffy Lake
Little Elk Creek
Little Elk Creek
Little Falls
Little Fawn Spring
Little Ferris Creek
Little Ferry Canyon
Little Fir Creek
Little Fish Creek
Little Fishhawk Creek
Little Fishtrap Creek
Fruin Creek
Little Granite Creek
Little Grassy Mountain
Little Graves Creek
Little Greasewood Creek
Little Groundhog Reservoir
Little Grouse Creek
Little Hay Creek
Little Hells Canyon
Little Honey Creek
Little Hyatt Reservoir
Little Indian Creek
Little Indian Creek
Little Jack Creek Reservoir
Little Jack Falls
Little Joe Creek
Little Joe Reservoir
Little John Reservoir
Little Juniper Canyon
Little Juniper Mountain
Little Juniper Mountain
Little Juniper Spring
Little Kiger Creek
Little Lake
Little Lake
Little Lake Creek
Little Lee Falls
Little Lick
Little Lookout Mountain
Little Marble Creek
Little Matson Creek
Little McCoy Creek
Little McKay Creek
Little Meadow Creek
Little Mill Creek
Little Minam Meadow
Little Mosquito Canyon
Little Mud Flat
Little Mud Flat Reservoir
Little Mud Spring
Little Muddy Creek
Little Muddy Creek
Little Muddy Creek
Little Muley
Little Nash Crater
Little North Fork Nehalem River
Little North Fork Silver Creek
Little North Fork Wilson River
Little Oak Creek
Little Owyhee Butte
Little Paradise Creek
Little Park
Little Pigeon Prairie
Little Pine Canyon
Little Pine Creek
Little Pine Hollow
Little Pine Hollow Ridge
Little Poison Butte
Little Pudding River
Little Rail Creek
Little Rattlesnake Creek
Little Rattlesnake Creek
Little Rayborn Canyon
Little Red S Fields
Little Reservoir
Little Riddle Mountain
Little Ridge Lake
Little River
Little Rock Creek
Little Rock Creek
Little Rock Creek
Little Rock Spring
Little Russell Creek
Little Salmon Creek
Little Salt Reservoir
Little Sand Creek
Little Sandrock Gulch
Little Sandy Reservoir
Little Sandy Reservoir
Little Savage Creek
Little Selle Gap
Little Selle Gap Reservoir
Little Selle Spring
Little Service Creek
Little Sevenmile Creek
Little Sinker Creek
Little Skookum Lake
Little Skull Creek
Little Sourdough Canyon
Little South Fork Kilchis River
Little South Fork Lewis and Clark River
Little South Fork Smith River
Little Squaw Flat
Little Squaw Flat Reservoir
Little Stewart Canyon
Little Stinkingwater Basin
Little Stinkingwater Creek
Little Summit Lake
Little Tank Creek
Little Thorn Hollow
Little Timber Canyon
Little Tom Folley Creek
Little Trout Creek
Little Trout Creek
Little Valley
Little Valley
Little Valley
Little Valley
Little Valley Lateral
Little Walla Walla River
Little Wallooskee River
Little Walls Lake
Little Whetstone Creek
Little Whiskey Creek
Little Whitehorse Creek
Little Wildhorse Creek
Little Wildhorse Lake
Little Wiley Creek
Little Willamette River
Little Willow Creek
Little Willow Creek Reservoir
Little Wolf Creek
Little Wood Hollow
Little Yaquina River
Littlefield Cemetery
Littlefield Ditch
Littlefield Reservoir
Littlefield Spring
Live Oak Mountain
Livingstone Adventist Academy
Lizzie Creek
Llewellyn Creek
Llewellyn Elementary School
Lob Fork
Lobo Creek
Locken Meadow
Locket Gulch
Locket Gulch Siphon
Lockit
Lockwood Canyon
Locust Grove Canyon
Lodge Creek
Lodge Ranch
Lodge Reservoir Number One
Lodge Reservoir Number Two
Lodgepole Trail
Lofton Lake
Lofton Reservoir
Loftus Creek
Log Cabin Spring
Log Creek
Log Creek Basin Reservoir
Log House Spring
Log Pond
Log Spring
Log Town Cemetery
Log Town Creek
Logan
Springwater Environmental Sciences School
Logan Slough
Loggerhead Canyon
Loggerhead Spring
Logging Creek
Lois Island
Lon Eakin Flat
London Peak
London School
London Springs
Ione
Lone Cedar School (historical)
Lone Elder
Anderson Lone Fir Pioneer Cemetery
Lone Fir Cemetery
Lone Grave Butte
Lone Grave Waterhole
Lone Jack Waterhole
Lone Juniper
Lone Juniper Canyon
Lone Juniper Spring
Lone Mountain
Lone Oak Cemetery
Lone Pine Bridge
Lone Pine Canyon
Lone Pine Creek
Lone Pine Gulch
Lone Pine Mountain
Lone Pine Ridge
Lone Pine Trail
Lone Rabbit Water Hole
Lone Ridge
Lone Rock
Lone Rock Bridge
Lone Star Mine (historical)
Ione Substation
Lone Tree Bridge
Lone Tree Lake
Lone Tree Ranch
Lone Tree Reservoir
Lone Willow Creek
Lone Willow Spring
Lonesome Bottom
Long Branch Creek
Long Branch Spring
Long Brown Rock
Long Butte
Long Canyon
Long Canyon
Long Creek
Long Creek
Long Creek
Long Creek
Long Draw
Long Field
Long Gulch
Long Gulch
Long Gulch
Long Gulch
Long Gulch Reservoir
Long Gulch Spring
Long Haul Reservoir
Long Hollow
Long Hollow
Long Hollow
Long Hollow
Long Hollow
Long Hollow
Long Hollow
Long Hollow Creek
Long Hollow Creek
Long Hollow Reservoir
Long Hollow Summit
Long Island
Long John Creek
Long Lake
Long Lake
Long Lake
Long Lake
Long Lake Valley
Long Meadows
Long Mountain
Long Mountain
Long Point
Long Point
Long Prairie
Long Prairie
Long Prairie
Long Prairie Creek
Long Ridge
Long Ridge
Long Ridge
Long Spring
Long Tom Creek
Long Tom River
Long Valley Creek
Long Walk Reservoir
Long Water Holes
Lookingglass Creek
Lookingglass Valley
Lookout Butte
Lookout Butte
Lookout Butte Reservoir
Lookout Creek
Lookout Lake
Lookout Mountain
Lookout Mountain
Lookout Mountain
Lookout Mountain Lookout
Lookout Mountain Trail
Lookout Point
Lookout Point Dam
Lookout Ridge
Lookout Rock
Lookout Spring
Lookout Spring
Loon Lake
Looney Butte
Looney Cemetery
Looney Spring
Loowit Creek
Lorane Guard Station
Lords Trail
Lorella
Lost Basin
Lost Cabin Creek
Lost City Spring
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek Falls
Lost Creek Reservoir
Lost Creek School
Lost Creek Spring
Lost Dog Rock
Lost Fawn Creek
Lost Lake
Lost Lake
Lost Lake
Lost Lake
Lost Lake
Lost Lake
Lost Lake
Lost Lake
Lost Lake
Lost Lake Creek
Lost Lake Saddle
Lost Pin Creek
Lost River
Lost River Diversion Channel
Lost Spring
Lost Tom Creek
Lost Tom Mountain
Lost Valley
Lost Valley
Lost Valley Creek
Lost Watch Creek
Louie Hughes Spring
Louies Draw
Louis Juvenile Hospital
Louise Creek
Louse Island
Lousey Hollow
Lousignont Creek
Lousignont Creek
Love Creek
Love Creek
Love Lake
Love Reservoir
Love Reservoir
Loveland Canyon
Loveland Canyon Reservoir
Loveland Horse Camp
Loveless Creek
Loveless Homestead
Low Creek
Low Divide Creek
Low Line Ditch
Lowder Mountain
Lowe Creek
Lowe Reservoir
Lowe Spring
Lowell
Lowen Spring
Lower Alder Slope Ditch
Lower Alder Springs Forest Camp (historical)
Lower Bacon Camp
Lower Baisley-Elkhorn Mine
Lower Bennett Dam
Lower Borax Lake Reservoir
Lower Clark Reservoir
Lower Cow Lake
Lower Cow Reservoir
Lower Deacon Flat Reservoir
Lower Ditch
Lower Elk Meadows
Lower Fisher Long Ditch
Lower Fishhole
Lower Fort Creek Reservoir
Lower Horse Lake
Lower Kiger Island
Lower Lambert Bar
Lower McCain Springs
Lower McNulty Reservoir
Lower Miller Reservoir
Lower Morton Spring
Lower Mud Spring
Lower Mud Spring
Lower North Fork
Lower Peavine Flat
Lower Pine Creek School (historical)
Lower Pitt Lake
Lower Pittsburg Rapids
Lower Pleasant Valley
Lower Point
Lower Powder Valley
Lower Pump Canal
Lower Rugg Spring
Lower Sand Spring
Lower Sands Light
Lower Selle Spring
Lower Sizemore Spring
Lower Slaughter Gulch Reservoir
Lower Slim and Fatty Reservoir
Lower Sourdough Spring
Lower Spring
Lower Stockpile Reservoir
Lower Table Rock
Lower Timber Canyon
Lower Trail Canyon
Lower Turner Gulch
Lower Twomile Creek
Loy Mine
Lubbing Flat
Lucas Cabin
Lucas Creek
Lucas Creek
Luce Hot Springs
Luckman Canyon
Lucky Boy Mine
Lucky Camp
Lucky Queen
Lucky Queen Mine
Lucky Spring
Lucky Star Mine
Lucy Payne Canyon
Lucy Payne Spring
Lula Lake
Lunceford Canyon
Lunch Lake
Lundell Canyon
Lundgren Creek (historical)
Luther School (historical)
Lutsinger Creek
Layne Creek
Lyda Creek
Lyle Creek
Lyle Gap
Lyman Creek
Lynch Flat
Lynch Gulch
Franciscan Montessori Earth School and Saint Francis Academy
Lynch School (historical)
Lynch Spring
Lynch Spring
Lynchs Rim
Lynch View Elementary School
Lynch Wood Elementary School
Lynde Reservoir
Lynns Ditch
Lynns Ditch
Lynx Hollow
Lynx Hollow School (historical)
Lyons
Lyons Canyon
Lyons Canyon
Lyons Meadow
Lyons Ridge
Lyons School (historical)
Lytle Creek
Lake Lytle
M C Ranch
M C Reservoir
M Canal
M S Davies Ranch
Mabel
Mabel Creek
MacLaren Forestry Camp
MacAbee Mine
MacDonald Canyon
Mack Brown Park
Mack Creek
Mack Creek
Macken Canyon
Mackin Gulch
Macks Canyon
Macksburg
Macleay
Macleay City Park
Macs Draw
Macs Reservoir
Macy Mine
Madarieta Cabin
Madison High School
Madison School (historical)
Madrona City Park
Magladry School (historical)
Magpie Gulch
Mahogany Butte
Mahogany Butte
Mahogany Creek
Mahogany Creek
Mahogany Flat
Mahogany Gap
Mahogany Long Draw Reservoir
Mahogany Mountain
Mahogany Mountain
Mahogany Point
Mahogany Reservoir
Mahogany Ridge
Mahogany Rim
Mahogany Spring
Mahogany Spring
Mahogany Spring
Mahon Creek
Mahon Creek
Mahon Creek Reservoir
Mahoney Meadows
Maiden Gulch
Maidens Dream Mine
Maiers Butte
Mail Canyon
Mail Creek
Main Channel
Malabon Elementary School
Malarky Lake
Malheur Butte
Malheur Butte Church
Malheur Canyon
Malheur Gap
Malheur Field Station
Malheur Lake
Malheur National Wildlife Refuge
Malheur Reservoir
Malheur Siphon
Malheur Slough (historical)
Malheur Slough
Mallett
Mallett Drain
Mallory Reservoir
Malloy Cabin
Malloy Ranch
Malone Dam
Maloney Peak
Mammoth Mine
Manhattan Spring
Mann Creek
Mann Creek
Mann Creek
Mann Home
Mann Lake
Mann Spring
Manning Creek
Manning Gulch
Manning Ridge
Manns Pond
Mansfield Ditch
Mansfield Lookout
Mansfield Pond
Manzanita
Mapes Creek
Maple Creek
Maple Grove Elementary School
Maple Gulch
Maple Lane School (historical)
Maple Elementary School
Maple School (historical)
Maple Spring
Maplewood Pioneer Cemetery
Maplewood Cemetery
Maplewood Elementary School
Marble Creek
Marble Creek
Marble Creek
Marble Creek
Marble Point
Mari - Linn Elementary School
Maria C Jackson State Park
Lake Marie
Marion Creek
Marion Creek
Marion Ditch
Marion Falls
Marion Forks
Marion Jordan Trail
Marion Point
Markham Creek
Markham Elementary School
Markham School Annex (historical)
Marking Corral Springs
Marks Creek
Marks Memorial Park
Marks Prairie
Marks Ridge
Marley Creek
Marlin Canyon
Marlin Spring
Marlin Spring
Marlin Spring
Marlow Creek
Maroney Creek
Marquam Creek
Marquam Dry Lake Canal
Marquam Gulch
Marsh Creek
Marsh Creek
Marsh Island
Marsh Island Light
Marsh Spring
Marshall Butte
Marshall Creek
Marshall Creek
Marshall Island
Marshall Lake
Pauling Academy of Integrated Sciences
Marshfield Senior High School
Resource Link Charter School
Marshland
Marsters Creek
Marsters Rock
Mart Davis Creek
Marten Creek
Marter Lake
Martha Mine
Martha Rice Bridge (historical)
Martin Canyon
Martin Creek
Martin Creek
Martin Creek
Martin Creek
Martin Creek
Martin Creek
Martin Island Channel
Martin Lake
Martin Spring
Martin Spring
Martindale Cemetery
Martins Lake
Mary Ann Draw
Mary McKinley Draw
Mary Moore Bridge (historical)
Marylhurst University
Marys Creek
Marys Lake
Marysville Elementary School
Mascall Ranch
Mason Creek
Mason Dam
Masonic Cemetery
Masonic Cemetery
Masonic Cemetery
Masonic Cemetery
Massinger Corner
Mast Creek
Mathas Creek
Matheny Creek
Mathieson Spring
Mathieu Creek
Mathis Spring
Matlock Canyon
Matney Flat
Matson Creek
Matson Creek
Matthew Gulch
Matties Ark
Mattingly Spring
Maud Williamson State Park
Maude Lake
Maupin
Maupin Butte
Maupin Butte
Maupin Cemetery
Maupin Trail Canyon
Maxfield Creek
Maxwell Butte
Maxwell Canal
Maxwell Ditch
Maxwell Lake
Maxwell Mine
Maxwell Pond
Maxwell Ranch
Maxwell Spring
Maxwell Trail
May Basin
May Canyon
May Creek
May Lake
May Lake
May Spring
Mayer State Park
Mayes Cabin (historical)
Mayfield Ranch (historical)
Mayflower Meadow
Mayger
Mayger Downing Cemetery
Maynard Creek
Mays Canyon
Mays Canyon Creek
Mays Grade Canyon
Mays Reservoir
Mays Rock
Mayville
Mayville Cemetery
McCoon Creek
McAllister Slough
McBain Flat
McBain Flat Spring
McBee Island
McBee Lake
McBride Creek
McBride School (historical)
McBurney Well
McCain Creek
McCain Creek Reservoir
McCain Reservoir Number One
McCain Reservoir Number Two
McCall Canyon
McCarthy Creek
McCarthy Ridge
McCarthy Spring
McCartie Ranch
McCartie Reservoir
McCarty Spring
McCauley Creek
McClanahan Meadow
McClellan Creek
McClellan Gulch
McClellan Mountain
McClendon Spring
McClintock Creek
McCloud Spring
McCloud-Field Reservoir
McClung Canyon
McClure Creek
McClure Lake
McCollum Creek
McConnell Reservoir
McConnell Springs
McConville Gulch
McCorkle Spring
McCormmach Creek
McCornack Point
McCoy Creek
McCoy Ridge
McCoy Spring
McCulloch Cemetery
McCullough Creek
McCully Recreation Site
McCully Mountain
McCune Junior High School (historical)
McCurry Creek
McCutcheon Flat
McDade Cache
McDade Springs
McDaid Springs
McDevitt Springs
McDonald Camp
McDonald Canyon
Tri-Creek Ranch
McDonald Spring
McDonald Spring
McDonald Waterhole
McDowell Butte
McDowell Creek
McDowell Creek School (historical)
McDowell Peak
McDowell Spring
McElligott Canyon
McEwen Creek
Weston - McEwen High School
McEwen Ranch
McEwen Reservoir
McEwen Spring
McFall Creek
McFarland Butte
McFarland School (historical)
McFee Creek
McGee Canyon
McGee Creek
McGee Slough
McGilvery Canyon
McGinnis Creek
McGinnis Creek
McGowan Creek
McGraw Creek
McGregor Island
McGuire Island
McGuire Reservoir
McHenry Flat
McHenry Spring
McInnes Norton Ridge
McInnes Spring
McIntosh Spring
McIntyre Ridge
McIntyre Spring
McKay Creek Cemetery
McKay Creek National Wildlife Refuge
McKay Creek Elementary School
McKay Reservoir
McKay Elementary School
McKay Well
McKee School (historical)
McKeever Mountain
McKendree Reservoir
McKenna City Park
McKenzie Bridge
McKenzie Elementary School
McKenzie Salmon Hatchery
McKenzie Trout Hatchery
McKinley
McKinley Corral
McKinley Creek
McKinley Elementary School
McKinney Bottom
McKinney Creek
McKnight Creek
McLafferty Creek
McLaughlin School (historical)
McLean Point
McLean Slough
McLennan Canyon
McLeod Ridge
McLoughlin High School
McLoughlin Substation
McMillan Canyon
McMillan Creek
McMullen Creek
McMullen Creek
McNab
McNabb Creek
McNary Branch
McNary Lake
McNulty
McNulty Creek
McNulty Reservoir
McPherson Canyon
McPherson Ditch
McPherson Gulch
McPhersons Island
McRae Creek
McRae Homestead
McSheery Creek
McTimmonds Creek
Meadow Creek
Meadow Creek
Meadow Flat Reservoir
Meadow Lake
Meadow Lake
Meadowlark Elementary School
Meadow Park
Meadow Spring
Meadow Spring
Meadow View
Meadowbrook Creek
Meadowbrook School (historical)
Meadowlark Spring
Meadows School (historical)
Medford
Medical Springs
Alliance High School
Meeker Mountain Reservoir
Mehama
Mehl Creek
Meissner Lookout
Melakwa Lake
Meldrum Canyon
Melendy Ridge
Mehlhorn Reservoir
Melrose
Melrose Elementary School
Melvina Creek
Memaloose Overlook
Memaloose State Park
Memorial Coliseum
Memorial Middle School
Memory Gardens Cemetery
Mendell Ranch
Mendenhall Creek
Mendiola Spring
Menefee County Park
Menlo Park
Menlo Park Elementary School
Meridian Cemetery
Meridian Lake
Merle Davies School (historical)
Merlin Sanitarium
Merrill
Merrill Canyon
Merrill Creek
Merrill Springs
Merrill Springs Rim
Merritt Creek
Mesa Reservoir
Messhouse Creek
Messner (historical)
Meteer Spring
Meter Station
Metteer Canyon
Metzger Elementary School
Michigan Cemetery
Michigan Heights Trail
Mickey Springs
Middle Bridge
Middle Camp
Middle Camp Baisley-Elkhorn Mine
Middle Canyon
Middle Canyon
Middle Channel Dike
Middle Creek
Middle Creek
Middle Creek
Middle Creek
Middle Creek County Park
Middle Creek Warden Station
Middle Ditch
Middle Fishhole
Middle Fork North Fork Klaskanine River
Middle Fork Berry Creek
Middle Fork Brummit Creek
Middle Fork Calapooya Creek
Middle Fork Camp Creek
Middle Fork Catching Creek
Middle Fork Clark Creek
Middle Fork Cold Springs Canyon
Middle Fork Corral Creek
Middle Fork Cottonwood Creek
Middle Fork Cronin Creek
Middle Fork Crow Creek
Middle Fork Foots Creek
Middle Fork North Fork Trask River
Middle Fork Pine Creek
Middle Fork Reservoir
Middle Fork Rim Reservoir
Middle Fork Sardine Creek
Middle Fork Stell Creek
Middle Fork Swayze Creek
Middle Grove
Middle Horse Lake
Middle Lake
Middle Lake Waterhole
Middle Mountain
Middle Mud Creek
Middle Reservoir
Middle Ridge
Middle Ridge
Middle Rim Reservoir
Middle Rugg Spring
Middle Spring
Middleswart Spring
Midway
Midway Reservoir
Mikkalo
Mile High Mine
Miler Spring
Miles Crossing
Military Creek
Military Reservoir
Military Slough
Military Spring
Milk Canyon
Milk Creek
Milk Creek
Milk Ranch Boulder Creek
Mill Boulder Creek
Mill City
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek Canal
Mill Creek Falls
Mill Creek Flat
Mill Creek Lateral
Mill Ditch
Mill Ditch
Mill Flat
Mill Flat Creek
Mill Gulch
Mill Hollow
Mill Park Elementary School
Mill Slough
Millard School (historical)
Millard School (historical)
Miller
Miller Cabin
Miller Canyon
Miller Cemetery
Miller Cemetery
Miller Cemetery
Miller Creek
Miller Creek
Miller Creek
Miller Creek
Miller Creek
Miller Creek
Miller Creek
Miller Creek
Miller Ditch
Miller Ditch
Miller Flat
Miller Flat
Miller Flat
Miller Gulch
Miller Gulch
Miller Gulch
Melvin Miller City Park
Miller Ranch
Miller Sands
Miller Sands Range
Miller Spring
Miller Spring
Miller Spring
Miller Spring
Miller - Coon Cemetery
Millers Gulch
Millersburg School (historical)
Millican Creek
Millicoma Intermediate School
Millicoma Myrtle Grove State Park
Millicoma River
Milliorn Cemetery
Mills Creek
Mills Elementary School
Milltown Hill Bridge
Milo McIver State Park
Milton Creek
Milton Ditch
Milton City Park
Milton Stateline Seventh Day Adventist School
Milton Substation
Milwaukie Pioneer Cemetery
Milwaukie Elementary School
Minam Lodge
Miner Creek
Miner Creek
Mineral Spring
Mineral Springs
Miners Creek
Miners Creek
Miners Draw
Minich Creek
Mink Creek
Minnehaha Creek
Minnehaha Spring
Minney Creek
Minnie Creek
Minnie May Mine
Minor Gulch
Minor Spring
Mint Creek
Minto Island
Minto Mountain
Minton Cove
Miranda Creek
Dust Bowl
Mount Misery
Mission
Mission Bottom
Mission Creek
Missouri Flat
Missouri Gulch
Missouri Ridge
Mitchell
Mitchell Butte
Mitchell Butte Hot Spring
Mitchell Butte Lateral
Mitchell Corner
Mitchell Creek
Mitchell Creek
Mitchell Monument
Mitchell Point
Mitten Spring
Mitzi Reservoir
Mixup Spring
Moar Lake
Mocks Bottom
Mocks Crest
Modeville
Moe Creek
Moffitt Elementary School
Mogul Mine
Mohawk River
Mohawk High School
Mohler
Molalla
Mollenhour Creek
Molly Gibson Mine
Molly Hill Mine
Mona Creek
Monahan Canyon
Monahan Creek
Monahan Lake
Monkey Ranch Gulch
Monohon Tunnel Mine
Monroe
Monroe Cemetery
Monroe Creek
Monroe Creek
Monroe Middle School
Monroe City Park
Monroe Roughs
Montavilla
Montavilla City Park
Montgomery Creek
Montgomerys Cabin
Monty Lake
Monument Peak
Monument Peak Reservoir
Monument Point
Monument Reservoir
Monument Reservoir
Monument Spring
Monument Springs
Monumental Mine
Moody Basin
Moody School
Moody Spring
Moolack Beach
Moolack Creek
Moon Creek
Moon Dam
Moon Hill
Moon Lake
Moon Lake
Moon Lake
Moon Ranch
Moon Reservoir
Moonlight Lake
Moonrise Spring
Moonshine Canyon
Moonshine Creek
Moonshine Spring
Moonshine Spring
Moonshine Spring
Moore Flat
Moore Park
Moore Spring
Moorehouse Creek
Moores Creek
Moores Hollow
Moores Island
Moores Valley
Mooreville
Moose Creek
Moosmoos Creek
Morcom Cow Camp
Morcom Reservoir
Morcom Reservoir Number Two
Saint Thomas More School
Morgan Canyon
Morgan Cemetery
Morgan Creek
Morgan Creek
Morgan Creek
Morgan Creek
Morgan Creek
Morgan Island
Morgan Lake
Morgan Lake
Morgan Landing
Morgan Lower Range
Morgan Mountain
Morgan Spring
Morgan Upper Range
Mount Moriah
Mormon Basin
Mormon Boy Mine
Morning Mine
Morningside Hospital (historical)
Moro
Morris Butte
Morris Canyon
Morris Canyon
Morris Creek
Morrison Bridge
Morrison Eddy
Morrison Reservoir
Mortar Point
Mortimore Canyon
Morton Butte
Morton Creek
Morton Island
Morton Spring
Mosetown Creek
Mosier
Mosier Cemetery
Mosier Creek
Mosier Spring
Mosier Springs
Mosquito Creek
Mosquito Creek
Mosquito Flat
Mosquito Mountain
Mosquito Mountain Reservoir
Moss Creek
Moss Creek
Moss Flat
Moss Gulch
Moss Meadow
Moss Pass
Moss Spring
Moss Springs Recreation Site
Moss Waterhole
Mott Island
Mound Lake
Mount Calvary Cemetery
Mount Calvary Cemetery
Mount Fanny Spring
Mount Hope School
Mount Laki Cemetery
Mount Pleasant Elementary School
Mount Ruth Cove
Mount Scott Creek
Mount Scott City Park
Y Child Care
Mount Tabor Hospital
Mount Tabor City Park
Mount Tabor Middle School
Mount Vernon Cemetery
Mount Vernon Elementary School
Mount Ireland
Mountain Belle Mine
Mountain Creek
Mountain Home
Mountain Home
Mountain King Mine
Mountain Lion Mine
Mountain View Cemetery
Mountain View Cemetery
Mountain View Cemetery
Mountain View Cemetery
Mountain View Cemetery
Mountain View Memorial Gardens
Mountain View Mine
Mountain View School (historical)
Mount Zion Cemetery
Mountainside Cemetery
Mouse Lake
Mouse Spring
Mouse Trap Reservoir
Mowich Lake
Moyina Hill
Muckle Lake
Mucky Flat
Mud Creek
Mud Creek
Mud Creek
Mud Creek
Mud Creek
Mud Creek
Mud Creek
Mud Creek
Mud Creek Reservoir Number One
Mud Creek Spring
Mud Flat
Mud Flat Creek
Mud Flat Creek Reservoir
Mud Flat Spring
Mud Fork
Mud Hollow
Mud Lake
Mud Lake
Mule Lake
Mud Lake
Mud Lake
Mud Lake
Mud Lake
Mud Lake Reservoir
Mud Lake Reservoir Number Two
Mud Lake Well
Mud Slough
Mud Slough
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring Canyon
Mud Spring Mountain
Mud Spring Reservoir
Mud Springs
Mud Springs Canyon
Mud Springs Gulch
Mud Springs Gulch
Muddy Canyon
Muddy Creek
Muddy Creek
Muddy Creek
Muddy Creek
Muddy Creek School (historical)
Muddy Ranch
Muddy Reservoir
Muddy Valley
Mudhole Spring
Muesial Creek
Mugwump Lake
Muir Creek
Muir Creek
Muir Reservoir
Mule Canyon
Mule Draw
Mule Hill
Mule Hollow
Mule Lake Reservoir
Mule Spring
Mule Springs Valley
Mule Tit
Muleshoe Creek
Muleshoe Ridge
Mulino
Mulkey Canyon
Mulkey Cemetery
Mulkey Wells Draw
Mulky Meadow
Mullen Spring
Mullen Spring
Muller Cemetery
Muller Ponds
Multnomah College (historical)
Multnomah Channel
Multnomah School (historical)
Multnomah Bible College and Biblical Seminary
Red Slough
Jeld - Wen Field
Muns Creek
Munson (historical)
Murder Creek
Murderer Gulch
Murdock Reservoir
Murphy Bar
Murphy Canyon
Murphy Corral
Murphy Creek
Murphy Creek
Murphy Gulch
Murphy Ranch
Murphy Reservoir
Murphy Waterholes
Murray Field
Murray Hill
Murray Hill Cemetery
Murray Junior High School (historical)
Murray Park
Mussel Creek
Mustang Basin
Mustang Basin
Mustang Butte
Mustang Butte
Mustang Spring
Mustang Water Hole
Mutton Mountain
Mutton Mountain Corral
Mutton Mountain Spring
Mutton Mountains
Myers Butte
Myers Canyon
Myers Creek
Myers Gulch
Myrtle Creek
Myrtle Creek
Myrtle Creek Elementary School
Myrtle Crest Memorial Gardens
Myrtle Crest School
Myrtle Point
Umpqua Myrtle State Park
Mystic Creek
N Canal
N G Creek
N G Creek Reservoir
N G Horse Camp
Nachter Butte
Nails Creek
Nan Creek
Nan-Scott Lake
Nanny Reservoir
Nannys Nipple
Nansene Community Hall
Napton
Narrows
Nash Crater
Nashville
Nat Wheat Canyon
Natal
Nate Creek
Natron
Natural Corral
Natural Pasture
Whorehouse Meadow
Naylox (historical)
Naylox Mountain
Neacoxie Creek
Neahkahnie Beach
Neahkahnie Creek
Neahkahnie Lake
Neahkahnie Mountain
Neah - Kah - Nie Middle School
Bilyeu Creek
Neals Hill
Neals Lake
Neathammer Creek
Neawanna Creek
Nebo Creek
Mount Nebo
Mount Nebo
Necanicum Picnic Area
Necanicum River
Necarney Creek
Neece Canyon
Needham Well
Needy
Neely Creek
Neer City Cemetery
Neer City School (historical)
Negro Jack Creek
Negro Flat
Negro Gulch
Negro Rock
Negro Rock
Negro Rock Canyon
Negro Rock Reservoir
Nehalem Bay
Nehalem Falls
Nehalem River
Nehalem Valley
Neil Creek
Neil Creek
Neil Rock
Nellie Spring
Nellies Point
Nells Canyon
Nelson Canyon
Nelson Creek
Nelson Creek
Nelson Ditch
Nelson Spring
Nelsons Pond
Nesika County Park
Nettle Spring
Neubert Spring
Nevada Canal
Sunset Hills Cemetery
New Era Bar
New Juniper Spring
New Place Reservoir
New Visher Reservoir
Floras Lake State Park
Newell Creek
Newell Creek
Newland Creek
Newman Canyon
Newman Slough
Newport
Newport Reservoir
Newton
Newton Cabin
Newton Clark Glacier
Newton Creek
Newton Spring
Newts Waterhole
Nice Creek
Nichols Canyon
Nichols Creek
Nichols Gap
Nichols Pump
Nicholson Spring
Nickel Mountain
Nicolai Mountain
Nicolai Ridge
Nielson Canyon
Nimrod
Nine Point Creek
Ninemile Mountain
Ninemile Slough
Ninemile Spring
Ninety-one
Ninety - One School
Nip and Tuck Pass
No Catchum Reservoir
No Name Springs
Noah Cemetery
Noble Cemetery
Noble Creek
Noble Hill
Noble Ranch
Noble Reservoir
Nodine Creek
Noel Creek
Noisy Creek
Noisy Creek
Noon Reservoir
Noonan Springs
Nora Pond
Norcross Spring
Normandale City Park
Normandin Spring
Norris Creek
Norris Creek
North Albany
North Alkali Creek
North Alkali Draw Reservoir
North Alkali Lake
North Alkali Spring
North Arm
North Beede Reservoir
North Branch Camp Kettle Creek
North Butte
North Canal
North Canal
North Canal
North Canal Lateral
North Canyon
North Catholic High School (historical)
North Cedar Creek
North Clackamas Central Park
North Clover Creek
North Coyote Canyon
North Coyote Creek
North Creek
North Creek
North Creek Campground
North Creek Reservoir
North Depoe Bay Creek
North Desert Waterhole
North Dixie Lake
North Drip Reservoir
North Eugene High School
North Fork Gales Creek
North Fork North Fork Gate Creek
North Fork North Fork Klaskanine River
North Fork Anthony Creek
North Fork Augur Creek
North Fork Berry Creek
North Fork Bottom Creek
North Fork Boulder Creek
North Fork Boulder Creek
North Fork Brownie Creek
North Fork Butte Creek
North Fork Calapooia River
North Fork Calapooya Creek
North Fork Clatskanie River
North Fork Cold Springs Canyon
North Fork Coquille River
North Fork Corral Creek
North Fork Cottonwood Creek
North Fork Cox Creek
North Fork Cronin Creek
North Fork Crooked Creek
North Fork Daly Creek
North Fork DeGarmo Canyon
North Fork Deep Creek
North Fork Deer Creek
North Fork Dixie Creek
North Fork Dry Creek
North Fork Ecola Creek
North Fork Floras Creek
North Fork Gate Creek
North Fork Gettings Creek
North Fork Gold Creek
North Fork Green Timber Creek
North Fork Griffin Creek
North Fork Hinkle Creek
North Fork Hunter Creek
North Fork Indian Creek
North Fork Jacobsen Gulch
North Fork Juniper Canyon
North Fork Klaskanine River
North Fork Limber Jim Creek
Little North Fork Coquille River
North Fork Little Willow Creek
North Fork Lousignont Creek
North Fork Mill Creek
North Fork Mohawk River
North Fork Necanicum River
North Fork Nehalem River
North Fork North Powder River
North Fork Pedee Creek
North Fork Pine Creek
North Fork Quartz Creek
North Fork Quartz Creek
North Fork Ranger Station
North Fork Reese Creek
North Fork Reservoir
North Fork Rock Creek
North Fork Rock Creek
North Fork Rock Creek
North Fork Rock Spring Canyon
North Fork Ruckles Creek
North Fork Salmonberry River
North Fork Spencer Creek
Hu Tsi Tehaga Creek
Ha-ng isa Reservoir
North Fork Stell Creek
North Fork Teal Creek
North Fork Tom Folley Creek
North Fork Trask River
North Fork Walker Creek
North Fork Warm Springs Creek
North Fork Wilson River
North Fork Wolf Creek
North Fourmile Creek
North Grassy Mountain Reservoir
North Gresham Elementary School
North Highland School (historical)
North Highland Spring
North Howell
North Howell Elementary School (historical)
North Lakes
North Logan School (historical)
North Loggerhead Reservoir
North Myrtle Park
North Oakander Drain
North Pole Mine
North Pole Ridge
North Portland Harbor
North Powder
North Powder Pond Number One
North Powder Pond Number Two
David Douglas High School South Childrens Services
Multisensory Learning Academy
North Scappoose Creek
North Side Canal
North Sister Creek
North Spring
North Spring
North Star Mine
North Whitehorse Reservoir
Northrup Creek
Northwest Christian University
Northwest Rock
Norton Creek
Norton Gulch
Norton Ranch
Norton Spring
Norway Cemetery
Norway Creek
Norwegian Cemetery
Norwegian Creek
Norwood Island
Notch Corrals
Noti Creek
Nottin Creek
Nowlin Creek
Noyer Creek
Numbers Creek
Nuss Lake
Nye Beach
Nye Creek
Nye Creek
Nyssa
Nyssa Cemetery
Nyssa Drain
O Canal
O Pipe
OA Lateral
OB Lateral
OK Creek
O'Black Pond
O'Brien Spring
O'Connor Reservoir
O'Connor Spring
O'Farrel Gulch
O'Hallihan Spring
O'Keefe Ranch
O'Keefe Reservoir
O'Keefe Spring
O'Keefe Springs
O'Leary Canyon
O'Leary Mountain
O'Leary Reservoir
O'Neil Creek
O'Neil Spring
O'Shea Cabin
O'Shea Creek
O'Toole Reservoir
O'Toole Spring
Oak Canyon
Oak Creek
Oak Creek
Oak Creek
Oak Creek
Oak Creek
Oak Creek School (historical)
Oak Creek Valley
Oak Flat
Oak Grove
Oak Grove Cemetery
Oak Grove Elementary School
Oak Grove Intermediate
Oak Hill Cemetery
Oak Island
Oak Park
Oak Ranch Creek
Oak Ranch Pit
Oak Ridge
Oak Ridge
Oak Ridge Lake
Elk Rock Island Park
Oak Springs Creek
Oakander Drain
Oakbrook
Oakhurst School (historical)
Oakland
Oaklawn
Oakmont City Park
Oakridge Cemetery
Oakville (historical)
Oakville Cemetery
Oat Creek
Oatman Lake
Obiaque Water Hole
Ocean Crest Elementary School
Ocean Home Farm
Ocean View Cemetery
Ochoco Gulch Creek
Ockley Green Middle School
Odell Spring
Odin Falls
Offatt Spring
Offield Creek
Oglesby Creek
Oil Well Spring
OK Gulch
Oke Reservoir
Oklahoma Hill
Olalla
Olalla Creek
Olallie Creek
Olallie Guard Station
Olallie Meadows
Olallie Mountain
Old Agency Cemetery
Old Armunger Cabin (historical)
Old Auburn Reservoir
Old Baldy
Old Blue
Old Blue Mountain
Old Buckhorn Ranch
Old Camp Warner
Old City Cemetery
Old Colony Cemetery
Old Colton
Old Fence Reservoir
Old Frizzell Ranch
Old Hotchkiss Road Jeep Trail
Old Jims Lake
Old Jims Open
Old Johnson Cabin (historical)
Old Maids Basin
Old Maids Creek
Old Maids Spring
Old Mill Camp
Old Oregon Trail Monument
Old Skipanon Creek
Old Tioga Camp
Old Watkins Cabin (historical)
Oldham Creek
Olene
Oler Spring
Olex
Olex Cemetery
Olive Lake
Oliver Butte
Oliver Drain
Oliver Lake
Oliver Ranch
Oliver Reservoir
Oliver Spring
Oliver Spring
Olalla Creek
Olney Cemetery
Olney G S
Olsen Creek
Olson Creek
One Doe Spring
Onehorse Slough
Onion Flat
Onion Gulch
Onion Peak
Onion Rock
Ontario
Ontario Heights Church
Ontario Island
Ontario Nyssa Canal
Opal Mine Draw
Opal Valley
Open Draw
Open Triangle Tee Ranch
Open Valley
Open Valley Waterhole
Open Valley Waterhole Number Three
Ophir Mine
Orchard Creek
Orchard Point Park
Ore Creek
Oreana Creek
Oregon Agricultural Experimental Station
Oregon Belle Creek
Oregon Belle Mine
Oregon Canyon Creek
Oregon Chief Mine
Oregon Chief Mine
Oregon Gulch
Oregon Butte
Oregon Hill
Oregon Institute of Marine Biology
Oregon King Mine
Oregon Lake
Oregon Slope
Oregon Slope Community Hall
Oregon State Fish Hatchery
Oregon State University Agriculture Experiment Station
Oregon State University Experimental Station
Oregon Technical Institute (historical)
Oregon Trail Historical Monument
Oreida Spring
Orejana Canyon
Orejana Rim
Oremite Mine
Orford Reef
Oriana Corrals
Orejana Flat
Oriano Spring
Orleans
Orofino Gulch
Orofino Mine
Orrs Corner
Orton Bridge
Osborn Creek
Osgood Creek
Oshkosh Creek
Oshkosh Mountain
Oswald West State Park
Osweg Creek
Oswego Canal
Oswego Creek
Oswego Park
Oswego Rock
Lake Oswego
Otis Spring
Otter Creek
Otter Creek
Otter Crest
Otter Crest State Park
Otter Rock
Otto Boye Flat
Our Lady of Sorrows School (historical)
Outerson Mountain
Outside Waterhole
Over the Top School (historical)
Overland Mine
Overlook Triangle
Overshoe Pass
Overshot Group Mine
Owen Butte
Owen Hill
Owens Rose Garden City Park
Round Grove Ranch
Owens Basin
Owens Creek
Owl Canyon
Owl Creek
Owl Creek
Owl Creek
Owl Creek
Owl Hollow Mine
Owl Ridge
Owl Spring
Lower Gap Creek
Owyhee Butte
Owyhee Butte Reservoir
Owyhee Butte Well
Owyhee Cemetery
Owyhee Dam
Owyhee Ditch
Owyhee Ridge
Owyhee Rim Reservoir
Lake Owyhee
Ox Head Spring
Oxbow Basin
Oxbow Regional Park
Oxbow Creek
Oxbow Reservoir
Oxbow School (historical)
Oxbow Spring
Oxley Slough
Oxman
Oxyoke Spring
P Hill
P Ranch
Pacific Grange Hall
Packard Creek
Packard Creek
Packard Gulch
Packsaddle Mountain
Packsaddle Mountain
Packsaddle Mountain Trail
Packsaddle Spring
Packwood Ditch
Paddock Butte
Paddys Lake
Page Dam
Page Place Reservoir
Page Reservoir
Elizabeth Page Elementary School
Paget Canyon
Painted Canyon
Painted Hills
Painted Hills State Park (historical)
Pointer Spring
Paisley Canyon
Paiute Creek
Paiute Reservoir
Palisades Elementary School
Palmer Creek
Palm Creek
Palmer Spring
Palmer Spring
Palomino Buttes
Palomino Creek
Palomino Hills
Palomino Lake
Palomino Lake
Palomino Rim
Palomino Rim Reservoir
Pancake Creek
Pankey Basin
Pankey Lake
Pankey Park Cemetery
Panning Gulch
Panter Creek
Panther Butte
Panther Canyon
Panther Creek
Panther Creek
Panther Creek
Panther Creek
Panther Creek
Panther Creek
Panther Creek
Panther Creek
Panther Creek
Panther Creek School (historical)
Panther Gulch
Panther Leap
Papersack Canyon
Paradise Canyon
Paradise Canyon
Paradise Creek
Paradise Creek
Paradise Mountain
Paradise Ranch
Paradise Recreation Site
Park Farms Creek
Park Place Elementary School
Park Saddle
Park Saddle Spring
Park Saddle Trail
Park School (historical)
Parker Creek
Parker Creek
Parker Creek
Parker Mountain
Parker Elementary School
Holy Family Academy
Parkrose
Portland Christian Junior and Senior High School
Parkrose High School
Parkrose Junior High School (historical)
Helensview High School
Parks Reservoir
Parks Spring
Parrish Creek
Parrish Gap
Parrott Creek
Parrott Creek
Parry Center
Parsnip Creek
Parsnip Lakes
Parsnip Peak
Parsons Creek
Parsons Creek
Pascual Reservoir
Pass Creek
Pass Gulch
Post Creek
Pasture Creek
Pat Creek
Pataha Creek
Patawa Creek
Patch Gulch
Patch Island
Pate Lake
Paterson Junction
Patill Canyon
Patjens Lakes
Dunning Creek
Patrick Mountain
Pats Cabin Canyon
Pats Canyon
Patten Creek
Patterson Basin
Patterson Cabin
Patterson Canyon
Patterson Cemetery
Patterson Creek
Patterson Ridge
César E Chávez Elementary School
Patterson Slough
Patterson Spring
Rattlesnake Canyon
Patton Cemetery
Patton Square City Park
Patton Spring
Paul Creek
Paul Well
Paulina Basin
Paulina Butte
Paulina Marsh
Pawnee Gulch
Paxton Meadows
Fay Canyon Reservoir
Payne Cliffs
Payne Creek
Payne Creek
Payne Placer
Payne Spring
Payton Ditch
Peach Canyon
Peach Cove
Peacock Creek
Peacock Lake
Peacock Pond Reservoir
Peanut Lake
Pearce Gulch
Pearcy Island
Pearl Creek
Pearl Wise Canyon
Pearl Wise Springs
Pearson Canyon
Peavine Creek
Pebble Creek
Pebble Springs Camp
Pecan Creek
Pecks Pond
Peddicord Point
Pedee Creek
Pedro Mountain
Pedro Spring
Peg Gulch
Peggy Butte
Pelican Island
Pelican Lake
Pelican Point
Pelland Creek
Pence Spring Reservoir
Pendair (historical)
Pendair Heights
Pendleton
Peninsula Drainage Canal
Peninsula Park
Peninsula Elementary School
Penland Meadow
Penland Ranch
Pennoyer Creek
Penny Creek
Penny Spring
Penny Spring
Penny Spring Guard Station (historical)
Penstock Olsen Ditch
Peoria
Pepper Canyon
Percy West Cabin
Perin Canyon
Periwinkle Creek
Perkins Creek
Perkins Creek
Perkins Creek
Perkins Peninsula County Park
Perkins Prairie
Pernot Creek
Pernot Trail (historical)
Perrault Canyon
Perrin Lateral
Perry Creek
Perry School (historical)
Perry Wilson Canyon
Perrydale
Petch Creek
Pete Enyart Canyon
Pete Lake
Peters Creek
Peters Ditch
Peterson Butte
Peterson Canyon
Peterson Creek
Peterson Creek
Peterson Creek
Peterson Creek
Peterson Creek
Peterson Gulch
Peterson Ranch
Peterson Ridge
Peterson Elementary School
Peterson Slough
Petes Mountain
Petes Mountain
Petes Puddle
Petre Meadows
Petrified Reservoir
Petroglyph Lake
Pettegrew Lateral
Petteys Cemetery
Phantom Bluff
Pheasant Creek
Pheasant Creek
Pheasant Creek
Phil Lewis School (historical)
Philippi Canyon
Phillips Canyon
Phillips Creek
Phillips Ditch
Phipps Creek
Phoenix Canal
Phys Point
Phys Slough
Piano Box Canyon
Pic Swale
Picket Spring
Pickett Spring Reservoir
Pickle Creek
Pickle Spring
Picnic Boulder Creek
Picnic Spring
Picnic Spring
Picture Flat
Picture Gorge
Pidgeon Falls
Pidgeon Park
Lake Pidgeon (historical)
Piper Canyon
Pier City Park
Pigeon Creek
Pigeon Prairie
Pigpen Creek
Pigtail Reservoir
Pika Lake
Pike Cemetery
Pike Creek
Pike Creek
Pikes Peak
Piledriver Creek
Pillar Rock Island
Pillar Rock Upper Range
Pilot Rock
Pilot Rock
Pilot Rock Cemetery
Pine Bench
Pine Butte
Pine Canyon
Pine City
Pine Cone Spring
Pine Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek Elementary School
Pine Flat
Pine Grove
Pine Grove Cemetery
Pine Grove Cemetery
Pine Grove Church
Pine Grove Elementary School
Pine Hollow
Pine Hollow
Pine Hollow
Pine Ridge
Pine Ridge
Pine Ridge Lake
Pine Spring
Pine Spring
Pine Spring Hollow
Pine Tree Canyon
Pine Tree Canyon
Pine Tree Creek
Pine Tree Ridge
Pinegrass Spring
Pinehurst
Pinet Lake
Ping Gulch
Pinhead Reservoir
Pinnacle Point
Pinnacle Reservoir
Pinochle Peak
Pinto Horse Reservoir
Pinto Lake
Pinto Spring
Pioneer Cemetery
Pioneer Cemetery
Pioneer Cemetery
Pioneer Cemetery
Pioneer Memorial Hospital
Eugene Pioneer Cemetery
Julia A Henderson Pioneer Park
Pioneer Park
Pioneer Park
Pioneer Park
Pioneer Elementary School
Pioneer Alternative Center (historical)
Pioneer Summit
Pioneers Cemetery
Pipe Spring
Piper Creek
Pirate Cove
Mount Pisgah
Pitch Fork Reservoir
Pitch Lake
Pitch Log Creek
Pitcher Creek
Pitt Lake
Pittenger Creek
Pittock Bird Sanctuary
Pittsburg
Pittsburg Bar
Pittsburg Gulch
Piute Creek
Piute Creek
Piute Lake Bed
Piute Reservoir
Piute Spring
Placer
Plainview Creek
Plank Creek
Plano School (historical)
Plateau Reservoir
Plateau Reservoir
Platt Canyon
Pleasant Creek
Pleasant Creek Guard Station
Pleasant Grove Church
Pleasant Hill
Pleasant Hill
Pleasant Hill Cemetery
Mount Olive Cemetery of Laurel
Pleasant Hill School
Pleasant Point Cemetery
Pleasant Valley
Pleasant Valley
Pleasant Valley
Pleasant Valley
Pleasant Valley
Pleasant Valley
Pleasant Valley Island
Pleasant Valley Rapids
Pleasant Valley School (historical)
Pleasant Valley Elementary School
Pleasant View Canal
Pleasant View Cemetery
Pleasant View School
Plentywater Creek
Plum Valley
Plunkett Creek
Plympton Creek
Pocahontas (historical)
Pocket Lake
Pocket Way
Poe Spring
Poe Valley
Pogue Gulch
Point Adams
Point Prominence
Poison Basin
Poison Basin Well
Poison Creek
Poison Creek
Poison Creek
Poison Creek Slough
Poison Root Gulch
Poison Spring
Poison Spring
Poison Springs
Poker Creek
Poker Jim Lake
Poker Jim Ridge
Poker Jim Spring
Polan Creek
Pole Canyon
Pole Creek
Pole Creek
Pole Creek
Pole Creek
Pole Creek
Pole Creek
Pole Creek
Pole Creek
Pole Creek
Pole Creek
Pole Creek
Pole Creek
Pole Creek
Pole Creek Camp
Pole Creek Reservoir
Pole Creek Ridge
Pole Creek Top
Pole Gulch
Pole Gulch
Pole Gulch
Pole Gulch
Poliwaski Canyon
Maurie Jacobs City Park
Pollack Memorial Field
Pollman Dam
Pollock Creek
Pollock Draw
Pollock Draw Reservoir
Pollock Draw Well
Polly Creek
Pond Spring
Pontius Creek
Pony Butte
Pony Creek
Poodle Canyon
Poodle Creek
Pool Spring
Poorman Creek
Pope Creek
Pope Reservoir
Pope Ridge
Porcupine Butte
Porcupine Canyon
Porcupine Canyon
Porcupine Creek
Porcupine Creek
Porcupine Guard Station
Porcupine Mountain
Porcupine Ridge
Port of Portland
Port of the Dalles
Porter Canyon
Porter Creek
Porter Creek
Porter Creek
Porter Field
Porter Gulch
Porter Hill
Porter Lake
Porter Ranch
Porter Ridge
Porter Spring
Porters Flat
Porters Island
Portland Christian Elementary School
Portland Sanatorium (historical)
Portland State University
Gately Academy
Oregon Zoo
Clarendon Portsmouth School
Portuguese Spring
Post Canyon
Post Creek
Post Creek
Post Gulch
Post Hollow
Post Meadows
Post Mountain
Post Mountain
Post Pile Rock
Postage Stamp Butte
Posthole Creek
Posy Valley
Pot Flat
Potato Hill
Potterf Creek
Pothole
Pothole Creek
Pothole Creek
Pothole Reservoir
Pothole Spring
Pothole Spring
Pothole Springs
Potholes Creek Reservoir
Potlatch Canyon
Potter
Potter Canyon
Potter Creek
Potter Creek
Potter Creek
Potter Reservoir
Potters Cemetery
Potters Creek
Potters Ponds
Potters Swamp
Potts Canyon
Potts Creek
Pounder Cemetery
Pounder Creek
Poverty Flat
Poverty Ridge
Poverty Ridge Well
Powder House Canyon
Powell Creek
Powell Creek
Powell Creek
Powell Creek
Powell Grove Cemetery
Powell Meadow
Powell City Park
Powell Spring
Powell Valley
Powell Valley
Powell Valley Elementary School
Powers Creek
Powers Ditch
Powers Marine Park
Prairie Channel
Prairie Ranch
Prati Island
Pratt School (historical)
Prava Peak Reservoir Number Two
Prava Peak Reservoir Number Three
Prava Peak Reservoir Number Four
Prentis Draw
Prentis Lake
Prescott
Prescott Gulch
Prescott Elementary School
Presley Lake
Preston Creek
Price Canyon
Price Creek
Price School (historical)
Prickett Creek
Priday Lake
Priday Reservoir
Priday Spring
Price Peak
Prince Albert Reservoir
Prince Lake
Prindle Peak
Prineville Gulch
Prineville Junction
Prineville Reservoir
Abiqua Academy
Pritchard Creek
Pritchard Flat
Privy Spring
Prong Creek
Prospect Reservoir
Providence Cemetery
Providence Portland Medical Center
Provolt
Proxy Creek
Proxy Falls
Proxy Point
Prunedale
Pudding Creek
Pudding River
Puderbaugh Ridge
Pueblo Mountain
Pueblo Mountains
Pueblo Valley
Puget Sound Gulch
Pugh Cemetery
Pugh Creek
Pugh Creek
Pulaski Creek
Pulp
Pumice Flat
Pump Ditch
Pump Spring
Pumphouse Canyon
Pumpkin Hollow
Puppydog Creek
Puppydog Spring
Purdin Cemetery
Purser Spring
Putnam Creek
Putnam Valley
Putt Canyon
Pyburn Hollow
Pyles Canyon
Pyles Creek
Pyramid Butte
Pyramid Mountain
Pyramid Rock
QT Spring
Quail Creek
Quail Gulch
Quaking Aspen Flat
Quaking Aspen Spring
Quaking Aspen Swamp
Quartz Butte
Quartz Creek
Quartz Creek
Quartz Creek
Quartz Creek
Quartz Creek
Quartz Gulch
Quartz Gulch
Quartz Gulch
Quartz Gulch
Quartz Mill Gulch
Quartz Mountain
Quartz Mountain
Quartz Mountain Basin
Quartz Mountain Pass
Quartz Valley
Quartz Valley Mountain
Quartzmill Peak
Queen of Peace School
Queen Mine
Queen Oregon Mines
Queens Branch
Quentin Creek
Quick Draw Spring
Quick Fill Reservoir
Quicksand Reservoir
Quicksand Spring
Quinaby
Quincy
Quincy School (historical)
Quines Creek
Quines Creek
Quinns Island
R Canal
R W Spring
R-3 Pipe
Rabbit Basin
Rabbit Creek
Rabbit Flat
Rabbit Mountain
Racetrack Lake
Racey Brothers Spring
Rachel Mine
Raddue Guard Station
Rader Creek
Radium Hot Springs
Raffety Cemetery
Ragged Butte
Ragged Gulch
Rail Canyon
Rail Creek
Rail Creek
Rail Gulch
Rainbow
Rainbow Creek
Rainbow Gulch
Rainbow Hollow
Rainbow Lake
Rainbow Lodge
Rainbow Mine
Rainbow Quarry
Rainie Falls
Rainier
Rainy Creek
Raleigh Park Elementary School
Ralph Spring
Ralphs Lake
Ralston Creek
Ramo Flat
Ramsey Canyon
Ramsey Canyon
Ramsey Gulch
Ramsey Hall
Ramsey Lake
Rancheria Creek
Rancheria Rock
Randall Creek
Randall Saddle
Randcore Pass
Randle Butte
Randleman Creek
Randolph Island
Randolph Slough
Rankin Flats
Raspberry Creek
Raspberry Creek
Raster Gulch
Rastus Waterhole
Rat Creek
Rat Creek
Rattlesnake Butte
Rattlesnake Butte
Rattlesnake Butte
Rattlesnake Butte
Rattlesnake Canyon
Rattlesnake Canyon
Rattlesnake Creek
Rattlesnake Creek
Rattlesnake Creek
Rattlesnake Creek
Rattlesnake Creek
Rattlesnake Creek
Rattlesnake Creek
Rattlesnake Creek
Rattlesnake Draw
Rattlesnake Gulch
Rattlesnake Gulch
Rattlesnake Hill
Rattlesnake Point
Rattlesnake Prairie
Rattlesnake Ridge
Rattlesnake Ridge
Rattlesnake Rock
Rattlesnake Spring
Rattlesnake Spring
Rattlesnake Spring
Rattlesnake Spring
Rattlesnake Spring
Rattlesnake Springs Wayside Park (historical)
Rattling Springs
Rawe Creek
Rawhide Canyon
Rawhide Creek
Ray Bar
Ray Creek
Ray Creek
Raymond Creek
Raymond Gulch
Raz Lewis Flat
Razor Back Ridge
Reagan Creek
Reallis Homestead
Rear Range Light
Rector Reservoir
Rector Ridge
Rector Spring
Red Bank Lakes
Red Basin Reservoir
Red Bluff Ridge
Red Bridge State Park
Red Butte
Red Butte
Red Butte Canyon
Red Butte Reservoir Number One
Red Butte Reservoir Number Two
Red Chief Mine
Red Cloud Ranch
Red Ditch
Red Drain
Red Elk Canyon
Red Elk Cemetery
Red Flat
Red Gap
Red Hawk Gulch
Red Head Reservoir
Red Hill School (historical)
Red Knoll Reservoir
Red Line Reservoir
Red Mountain
Red Mountain
Red Mountain
Red Mountain
Red Mountain Creek
Red Mountain Lake
Red Mountain Reservoir
Red Mountain Reservoir
Red Mud Creek
Red Ridge
Red Rim Spring
Red Rock
Red Rock Basin
Red Rock Creek
Red Rock Gulch
Red Rock Quarry
Red Rock Spring
Red Rock Spring
Red Slide Hill
Red Spring
Red Well
Red Well
Redford Creek
Redibaugh Creek
Redland
Redmond
Redmond Cemetery
Redmond Ranch
Redmond Substation
Reds Creek
Reds Horse Ranch
Reed College
Reed Creek
Reed Creek
Reed Ditch
Reed Lake
Reed Mine
Reed Spring
Reed Spring
Reeder Point
Reeds Basin
Reeds Basin Reservoir
Reeds Creek
Reehers Camp
Reese Creek
Reese Creek School (historical)
Reeves Mountain
Refuge Spring
Regis High School
Rehart Ranch
Reimer Reservoir
Reinecke Cabin
Reininger Spring
Reliance Creek
Remington Canyon
Remote
Renfrew Grave
Renfrew Spring
Renfro Creek
Renfro Springs
Renhaven Ridge
Rennie Landing
Reno Canyon
Reno Mine
Rentenaar Point
Renwick Canyon
Reser Creek
Reservoir Butte
Reservoir Lake
Reservoir Lake
Rest Lake
Resthaven Memorial Park
Resting Lake
Reston
Reuben Creek
Reynolds Middle School
Rhea Creek Cemetery
Rhem Creek
Rhinehart Buttes
Rhodes Canyon
Rhododendron Park
Rialto Mine
Ribbon Ridge
Rice (historical)
Rice Creek
Rice Flat
Rice School (historical)
Rice Valley
Rich Creek
Rich Creek
Rich Gulch
Yantis Park
Richards Butte
Richardson Creek
Richardson Creek
Richardson Gap
Richardson County Park
Richie Flat
Richmond Canyon
Richmond Cemetery
Richmond Elementary School
Riddle Creek
Riddle Mountain
Riddle Mountain Well
Riddle Ranch
Riddle Ranch
Rider Creek
Ridge Camp Spring
Ridge Creek
Ridge End Reservoir
Ridge Road Reservoir
Ridge Top Spring Number Two
Ridge Top Spring Number Three
Ridge Top Spring Number Four
Ridgeway Butte
Ridgeway Canyon
Ridgewood Park
Ridgewood Elementary School
Ridley Creek
Rieckens Corner
Rieth
Rieth Ridge
Rietmann Ranch
Rietmann Canyon
Riffle Canyon
Riffle Creek
Right Fork Fielder Creek
Right Fork Foots Creek
Right Fork Sardine Creek
Rigler Elementary School
Riley Butte
Riley Horn Point
Riley Horn Reservoir
Riley Peak
Riley Reservoir
Riley Spring
Riley Spring
Rim Basin
Rim Reservoir
Rim Reservoir
Rim Rock Reservoir
Rimrock Reservoir
Rimrock Spring
Rimrock Waterhole
Rimtop Spring
Rincon Lake
Rincon Springs
Rinearson Slough
Rinehart Canyon
Rinehart Creek
Rinehart Creek
Rinehart Creek Reservoir
Rinehart Ranch
Ring Corral Creek
Rink Creek
Rink Creek Reservoir
Rink Peak
Rio Canyon
Riser Lake
Risley Park
Ritchie Creek
Ritter Creek
Ritterbusch Flat
River Forest Lake
River Park
River Road/ - El Camino del Rio Elementary School
River View
Riverview Cemetery
Riverbed Butte
Riverbed Butte Spring
Riverdale Hill
Riverdale Grade School
Riverdale School (historical)
Riverside Recreation Site
Riverside Canal
Riverside Cemetery
Riverside Hall
Riverside Reservoir Number One
Riverside Reservoir Number Two
Riverside Elementary School (historical)
Riverside School (historical)
Riverside School (historical)
Riverview Cemetery
Riverview Community Hall
Riverview School (historical)
Riverwood Park
Road Bend Spring
Road Canyon
Road Canyon
Road Canyon
Road Canyon
Road Canyon
Road Canyon
Road Canyon
Road Canyon
Road Canyon
Road Canyon Creek
Road Gulch
Road Gulch
Road Gulch
Road Lake
Guy Lee Park
Road Spring
Road Spring
Road Spring
Roadside Spring
Roaring Creek
Roaring Creek
Roaring Creek
Roaring River
Roaring River State Fish Hatchery
Roaring Springs
Roaring Springs Ranch
Rob Roy Mine
Robbins Butte
Robert Bird Cemetery
Roberts Butte
Roberts Canyon
Roberts Creek
Roberts Creek
Roberts Creek School (historical)
Roberts Mountain
Roberts Pond
Robin Creek
Robin Park
Robinette
Tarter Gulch
Robinson Canyon
Robinson Canyon
Robinson Creek
Robinson Draw
Robinson Gulch
Robinson Gulch
Robinson Lake
Robinson Lake
Robinson Reservoir
Robinson Ridge
Robinson Ridge
Robinson Spring
Robinson Spring
Robinson Spring Creek
Robinson Valley
Roby Hill
Rock Bottom Reservoir
Rock Cabin Creek
Rock Cabin Spring Number 2
Rock Camp Draw
Rock Camp Lake
Rock Canyon
Rock Canyon
Rock Corral Canyon
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek Butte
Rock Creek Butte
Rock Creek Cemetery
Rock Creek Church
Rock Creek Community Hall
Rock Creek Fish Hatchery
Rock Creek Flat
Rock Creek Lake
Rock Creek Lake Trail
Rock Creek Point
Rock Creek Powerplant
Rock Creek Ranch
Rock Creek Reservoir
Rock Creek Reservoir
Rock Creek Reservoir
Rock Creek Reservoir
Rock Creek Reservoir
Rock Creek Trail
Rock Crusher Canyon
Rock Fence Reservoir
Rock Hill
Rock Hill Reservoir
Rock Island
Rock Knoll Reservoir
Rock Lake
Rock Mountain
Rock Mountain
Rock Pile Spring
Rock Pit Creek
Rock Point
Rock Prairie County Park
Rock Quarry Reservoir
Rock Reservoir
Rock Robinson Creek
Rock Spring
Rock Spring
Rock Spring
Rock Spring
Rock Spring
Rock Spring
Rock Spring
Rock Spring
Rock Spring
Rock Spring
Johnson Rock Spring
Rock Spring
Rock Spring
Rock Spring
Rock Spring Canyon
Rock Spring Reservoir
Rock Spring Siphon
Rock Spring Trail
Rock Springs Camp
Rockaby Creek
Rockie Four Corners
Rockne Gulch
Rockville Cemetery
Rockville Elementary School
Rockwall Spring
Rocky Bottom Reservoir
Rocky Butte
Rocky Butte
Rocky Butte Spring
Rocky Canyon
Rocky Canyon Creek
Rocky Creek
Rocky Creek
Rocky Creek State Park
Rocky Ford Campground
Rocky Gorge Reservoir
Rocky Hill
Rocky Hill Reservoir
Rocky Island
Rocky Plateau
Rocky Point
Rocky Point
Rocky Point
Rocky Prairie
Rocky Ridge
Rocky Spring
Rocky Top
Rocky Top
Roddy
Roderick Creek
Rodger Ranch
Rodger Reservoir
Rodgers Creek
Rodine Creek
Roger Spring
Rogers Canyon
Rogers Creek
Rogers Creek
Rogers Forest Park
Rogers Ranch
Rogue River Academy (historical)
Roland Canyon
Rollan Creek
Rollin Canyon
Rome
Rome Cliffs
Rondeau Butte
Roney Creek
Rood Canyon
Rood Hill
Rooke and Higgins County Park Boat Ramp
Rookie Canyon Spring
Rookie Creek
Rooper Ranch
Roosevelt High School
Roosevelt Elementary School
Roosevelt Elementary School
Rooster Comb
Rooster Comb Spring
Rooster Rock
Rooster Rock Spring
Roostercomb
Root Creek
Root Gulch
Rose Briar Canyon
Rose Brier Canyon
Rose Brier Spring
Rose City Cemetery
Rose City Park Elementary School (historical)
Rose Hill Cemetery
Rose Lake
Rosebriar Spring
Rosebud Mine
Rosebud Mountain
Roseburg
John C Fremont Middle School
Rosebush Canyon
Rosebush Creek
Rosedale
Rosedale Friends Cemetery
Rosemont
Rosenbaum Canyon
Rosenbaum Ridge
Rosey Creek
Ross Butte
Ross Canyon
Ross Creek
Ross Island
Ross Island Bridge
Ross Slough
Rotten Lake
Rouen Gulch
Rough and Ready Lakes
Rough Creek
Round Butte
Round Butte Lake
Round Grove
Round Lake
Round Lake
Round Meadow
Round Mountain
Round Mountain
Round Mountain
Round Mountain
Round Peak
Round Peak Spring
Round Prairie
Round Prairie
Round Prairie
Round Spring
Round Top
Round Top
Round Top
Round Top
Roundup Substation
Rouse Bridge
Row Gulch
Rowe Creek
Rowe Creek Reservoir
Rowe Williams Canyon
Rowena Creek
Rowena Dell
Rowland (historical)
Roxy Ann Peak
Roy Creek
Roy Reservoir
Royston Spring
Ruby Mine
Ruby Springs
Ruckles Creek
Rufino Butte
Rufino Butte Reservoir
Rufino Gulch
Rugg Canyon
Ruggs
Runaway Creek
Runyon Creek
Rural Dell
Rush Creek
Rush Spring
Russel Creek
Russel Creek
Russel Creek
Russel Creek
Russel Mountain
Russell Cemetery
Russell Creek
Russell Creek
Russell Creek
Russellville
Russellville Community Cemetery
Russian Creek
Russian Island
Mount Ruth
Ruthers Corners
Rutledge
Rutledge Canyon
Rutter Canyon
Ryan Cabin
Ryan Creek
Ryan Creek
Rye Field
Rye Flat
Rye Hill
Rye Valley
Ryegrass Creek
Ryegrass Hollow
Ryegrass Ranch
Ryegrass Spring
Ryegrass Valley
Ryestack Gulch
S Canal
S E Reservoir
Sabin Elementary School
Head Start Sacajawea
Sacchi Beach
Sack Canyon
Sack Canyon Reservoir
Sacramento Butte
Sacramento Hill
Sacramento Elementary School
Sacred Heart Academy (historical)
Sacred Heart Cemetery
Sacred Heart Cemetery
Sacred Heart Elementary School
Sacred Heart School (historical)
Saddle Butte
Saddle Butte
Saddle Butte
Saddle Butte
Saddle Butte
Saddle Butte
Saddle Butte
Saddle Butte
Saddle Butte Lava Field
Saddle Butte Lava Tube
Saddle Butte Reservoir
Saddle Butte Reservoir
Saddle Camp Spring
Saddle Mountain
Saddle Mountain
Saddle Mountain State Park
Saddle Reservoir
Saddle Trail
Saddlehorse Creek
Saddlehorse Spring
Sag Creek
Sage Creek
Sage Creek
Sage Flat
Sage Hen Butte
Sage Hen Pen
Sage Hollow
Sagebrush Flat
Sagebrush Gulch
Sagebrush Mountain
Sagebrush Spring
Sagebrush Spring
Sagehen Reservoir
Saginaw
Sahalie Falls
Saint Agatha School
Saint Alice School (historical)
Saint Andrews Mission Cemetery
Saint Andrew Nativity School
Saint Andrews School (historical)
Montessori Morningstar House of Children
Saint Anthony Hospital
Saint Anthonys Cemetery
Saint Anthonys School
Saint Anthony's School (historical)
Saint Benedicts Abbey
Lourdes School
Saint Boniface Old Cemetery
De La Salle North Catholic High School
Saint Cecilias School
Saint Charles School (historical)
Saint Clare School
Saint Edwards School (historical)
O'Hara Catholic School
Saint Helens Reservoir
Saint Helens
Saint Helens Bar
Saint Helens Range
Saint Ignatius Parish School
Saint John Creek
Saint John Fisher School
Saint John the Apostle School
Saint John the Baptist Catholic School
Saint Joseph Cemetery
Saint Joseph School (historical)
Saint Lawrence School (historical)
Madeleine School
Saint Marys Boys Home
Saint Marys School (historical)
Saint Marys Catholic School
Saint Mary Catholic School
Saint Mary of the Valley Elementary School
Saint Marys Substation
Saint Matthew Elementary School
Saint Patrick Mountain
Saint Paul Mine
Saint Paul Mountain
Saint Paul Lutheran School
Saint Pauls Cemetery
Saint Paul Parish School
Saint Pauls School (historical)
Saint Peter's Cemetery
Saint Peters School (historical)
Saint Peters School (historical)
Saint Philip Neri School (historical)
Mount Hood Community College - Maywood Park
Saint Rose Cemetery
Childswork Learning Center
Saint Therese School
Saint Wenceslaus Cemetery
Salander Creek
Salem Academy
Salem Ditch
Salem Vocational School (historical)
Saleratus Creek
Saling Spring
Salisbury Slough
Salmon Creek
Salmon Creek
Salmon Creek
Salmon Creek
Salmon Creek
Salmon Fork Thirtymile Creek
Salmonberry Creek
Salmonberry Creek
Salmonberry Guard Station
Salmonberry Reservoir
Salmonberry River
Salt Creek
Salt Creek
Salt Creek
Salt Creek
Salt Creek
Salt Creek
Salt Creek
Salt Creek
Salt Spring
Salt Spring
Salt Spring
Salt Spring Number One
Salt Springs
Sam Creek
Sam Daws Bend
Sam Jackson Park
Sampson Creek
Sampson Gulch
Sampson Mountain
Sampson Spring
Sams Creek
Sams Valley
Sams Valley
Samson Creek
San Salvador Beach
Sand Basin
Sand Canyon
Sand Canyon
Sand Creek
Sand Creek
Sand Creek
Sand Creek
Sand Gap
Sand Hills
Sand Hollow
Sand Hollow
Sand Hollow
Sand Hollow
Sand Hollow
Sand Hollow
Sand Hollow
Sand Hollow
Sand Hollow Creek
Sand Hollow Creek
Sand Hollow Well
Coffee Pot Island
Tri-Club Island
Sand Island
Sand Island Dike Light
Sand Island Dike Middle Light
Sand Lake
Sand Lake
Sand Mountain
Sand Mountain
Sand Ranch Well
Sand Ridge Cemetery
Sand Ridge School (historical)
Sand Spring
Sand Spring
Sand Spring
Sand Spring
Sand Spring
Sand Spring Butte
Sanderson Bridge (historical)
Sandhill Recreation Site
Sandrock Gulch
Sandrock Mountain
Sandrock Springs
Sandstone Point
Sandy Canyon
Sandy Creek
Sandy Island
Sanford Heights Playground
Santa Clara
Santiam Junction
Santiam Lake
Santiam River Safety Rest Area
Santiam School (historical)
Santiam Valley Grange
Santosh Slough
Sardine Creek
Sardine Creek
Sardine Gulch
Sardine Mountain
Sardine Spring
Garoutte Creek
Saturn Creek
Saum Creek
Saunders Lake
Sauvie Island
Sauvie Island School
Savage Rapids
Savage Rapids Dam (historical)
Savoy Lake
Sawmill Basin
Sawmill Butte
Sawmill Field
Sawmill Gap
Sawpit Canyon
Sawtooth Crater
Sawtooth Ridge
Sawtooth Ridge
Sawtooth Spring
Sawyer Bar
Sawyer Creek
Sayrs Canyon
Scab Gulch
Scab Gulch
Scab Spring
Scale Reservoir
Scaponia Campground
Scappoose
Scappoose Bay
Scappoose Creek
Schaffer Cabin (historical)
Schamberg Bridge
Scheuter Spring
Schieffelin Gulch
Schilling Spring
Schimanek Bridge
Schlinkman Creek
Schnable Creek
Schneider Butte
Schneider Meadows
Schnipps Valley
Schofield Flat
Scholey Gulch
School Hollow
School Number 26 (historical)
School Section Cabin
School Section Lake
School Section Lake
School Section Table
Schoolhouse Canyon
Schoolhouse Canyon
Schoolhouse Creek
Schoolhouse Creek
Schoolhouse Creek
Schoolhouse Creek
Schoolhouse Gulch
Schoolhouse Ranch
Schoolie Flat
Schoolie Pasture
Schooner Creek
Schott Canyon
Shultz Creek
Schweizer Reservoir
Scio
Scissors Cabin
Scott Butte
Scott Butte
Scott Butte
Scott Butte Creek
Scott Canyon
Scott Canyon
Scott Canyon
Scott Corral Creek
Scott Creek
Scott Creek
Scott Creek
Scott Creek
Scott Ditch
Scott Lake
Scott Mountain
Scott Mountain
Scott Reservoir
Scott Elementary School
Scott Spring
Scotts Cache Spring
Scotts Canyon
Scotts Valley
Scotty Creek
Scottys Springs
Scoubes Creek
Scout Creek
Scout Lake
Scratch Post Butte
Scravel Hill
Scribners Spring
Sea Lion Rock
Sea Lion View Point
Seaburn Reservoir
Seaburn Well
Seal Channel
Seal Island
Seal Lake
Seal Rock
Searcy Flat
Seaside Dam
Seaside Reservoir
Seattle Flat
Second Creek
Second Creek
Second Lake
Second Sheep Camp Spring
Second Swale Creek
Secret Valley
Section Creek
Section Line Reservoir
Section Line Spring
Seelander Creek
Seeley Creek
Segundo Spring
Seig Ponds
Selder Creek
Seldom Reservoir
Selle Gap
Selle Gap Reservoir
Selle Gap Reservoir Number Two
Sellers Butte
Sellwood
Sellwood Bridge
Sellwood City Park
Sellwood Middle School
Seneca Fouts Memorial State Natural Area
Senecal Spring
Sentinel Peak
Separation Creek Cutoff
Separation Lake
Salem Academy High School
Serrano Point
Serrano Point Ranch
Serrano Spring
Service Buttes
Service Canyon
Service Creek
Service Creek
Service Springs
Sesena Creek
Settler Point
Sevcik Pond
Seven Devils State Park
Seven Oak Middle School
Seven Springs
Seven Springs Ranch
Seven-up Creek
Sevenmile Creek
Sevenmile Creek
Sevenmile Hill
Sevenmile Hill
Sevenmile Ridge
Sewallcrest City Park
Multnomah Early Childhood Program
Seward Flat
Sexton Mountain
Sexton Mountain
Sexton Reservoir
Seymore Springs
Shadow Creek
Shadscale Flat
Shadscale Spring
Shady Creek
Shady Creek
Shady Spring
Shaeffer Butte Reservoir
Shafer Creek
Shaffner Creek
Shag Lake
Shake Butte
Shake Camp
Shake Creek
Shallow Lake
Shanghai School (historical)
Shangri-la School (historical)
Shangrila Creek
Shaniko
Shaniko Butte
Shaniko Junction
Shanks Creek
Shaplish Canyon
Shark Creek
Shasta Butte
Shasta Gap
Shasta Gulch
Shasta Middle School
Shasta Elementary School
Shattuck School (historical)
Shaw Burn
Shaw Canyon
Shaw Creek
Shaw Reservoir
Shaw Stewart Ditch
Shearing Plant Reservoir
Shedd Slough
Sheep Camp Reservoir
Sheep Camp Spring
Sheep Corral Creek
Sheep Corral Reservoir
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek Siphon
Sheep Dip Canyon
Sheep Gulch
Sheep Hollow
Sheep Hollow
Sheep Lake
Sheep Mountain
Sheep Mountain
Sheep Mountain
Sheep Mountain
Sheep Mountain
Sheep Ranch
Sheep Reservoir
Sheep Rock
Sheep Rock
Sheep Rock
Sheep Rock
Sheep Rock
Sheep Rock Reservoir
Sheep Rock Springs
Sheep Spring
Sheep Spring
Sheep Spring
Sheep Spring
Sheep Spring Creek
Sheep Springs
Sheephead Basin
Sheephead Reservoir
Sheephead Ridge
Sheephead Spring
Sheepherder Spring
Sheepshed Canyon
Sheepy Creek
Sheet Iron Jack Creek
Shelby Reservoir
Sheldon High School
Shell Island
Shell Rock Mountain
Shell Rock Reservoir
Shell Rock Spring
Shellburg Creek
Shellburg Falls
Shelley Corral
Shellrock Canyon
Shellrock Spring
Shelton Wayside County Park
Mount Shep
Shepard Camp
Shepherd Creek
Shepherd Gulch
Shepherd Spring
Sherars Bridge
Sherman Creek
Sherman Reservoir
Sherman Valley
Sherod Meadows
Sherwood
Sherwood Heights Elementary School
J Clyde Hopkins Elementary School
Shick Creek
Shields Creek
Shiloh Basin
Shiloh Basin School (historical)
Shingle Mill Creek
Shingle Reservoir
Shinglehouse Slough
Shipley Bridge
Shipley Spring
Shipley Springs
Shirk Lake
Shirk Rim
Shirks Lookout
Shirley Gap Lookout
Shirttail Creek
Shively Creek
Shively Park
Shoat Spring
Shobe Canyon
Shobe Creek
Shoeffer Reservoir
Shoesole Flat
Shoestring Creek
Shoestring Creek
Shoestring Ridge
Shoestring Ridge
Shoestring Trail
Shoestring Valley
Shone Spring
Shoofly Canyon
Shoofly Creek
Shoofly Ranch
Shore Acres State Park
Shores Waterhole
Short Canyon
Short Canyon Reservoir
Short Creek
Short Creek
Short Creek Reservoir
Short Lake
Short Mountain
Shortridge Creek
Short Sand Beach
Short Sand Creek
Shorthorn Gulch
Shorthorn Spring
Shot Mine
Shotgun Creek
Shotgun Creek
Shotgun Creek
Shotgun Hollow
Shoup Creek
Shovel Basin
Shovel Spring
Showalter Creek
Shuck Mountain
Shumway Creek
Shumway Lake
Shumway Ranch
Shumway Reservoir
Shurtz Field
Shutler (historical)
Shutler Flat
Shweeash Creek
Sibley Sands
Sickfoot Creek
Sidehill Reservoir
Sidehill Spring
Sidney
Sidney Power Ditch
Sidwalter Corral
Signal Buttes
Signal Hill
Sijota Creek
Silent Friend Mine
Siletz
Siletz Bay
Silk Creek
Silk Creek School (historical)
Silver Butte
Silver Creek
Silver Creek
Silver Creek
Silver Creek
Silver Creek
Silver Creek Camp
Silver Creek Valley
Silver Dick Mine
Silver Falls
Silver Falls
Silver Lake
Silver Lake
Yujin Gakuen Elementary School
Silver Point
Silver Crest Elementary School
Silverton
Silverton Hills Grange
Simison - Hale Cemetery
Simmonds Creek
Simmons Canyon
Simmons Cemetery
Simmons Creek
Simmons Slough
Simmons Spring
Simmons Spur
Simms Ranch
Simnasho
Simnasho Cemetery
Simon Flat
Simonis Spring
Simpson Canyon
Simpson Creek
Simpson Creek
Simpson Creek
Simpson Creek
Simpson Creek
Simpson Reef
Simpsons Camp
Sinamox
Singer Drain
Singleton Park
Singleton Valley
Sinker Creek
Echo Memorial Cemetery
Siskiyou
Siskiyou Pass
Sisley Creek
Sister Creek
Sisters
Sitkum
Sitton Elementary School
Sitz Reservoir
Siuslaw Falls
Six Dollar Canyon
Sixmile Canyon
Sixmile Canyon
Sixmile Creek
Sixmile Draw
Sixmile Lake
Sixshooter Ranch
Sixteen Canyon
Sixteenmile Creek
Skedaddle Spring
Skelley
Skelton Spring
Skidoo Spring
Skillet Handle
Skinner Butte
Skinner Dam
Skipanon River
Skipanon Waterway
Skipanon Waterway Light
Skookum Creek
Skookum Creek
Skookum Creek
Skookum Lake
Skull Creek
Skull Creek
Skull Creek Butte
Skull Creek Ranch
Skull Creek Reservoir
Skull Mountain
Skull Spring
Skull Springs Reservoir
Skunk Cabbage Ridge
Skunk Creek
Skunk Farm Canal
Skunk Gulch
Skunk Hollow
Sky Ranch
Skylight Spring
Skyline Memorial Gardens
Skyline Park
Skyline Reservoir
Skyline Elementary School
Sladden City Park
Slagle Creek
Slate Creek
Slate Slide Shelter (historical)
Slaughter Gulch
Slaughter Gulch
Slaughter Gulch Reservoir
Slaughterhouse Gulch
Slaughterhouse Range
Slaughters Channel
Slaughters Creek
Slayton Well
Sled Creek
Sleezer Creek
Slegman Spring
Slick Creek
Slick Hollow
Slickey Lake
Slide Creek
Slide Creek
Slide Creek
Slide Creek
Slide Creek
Slide Mountain Creek
Slide Out Creek
Slide Ridge
Slide Spring
Slide Waterhole
Slideout Creek
Slim and Fatty Reservoir
Slim and Fatty Spring
Slim Creek
Slimwater Creek
Slipper Reservoir
Slocum Creek
Sloop Creek
Slotted Pen Creek
Sluice Canyon
Slusher Canyon
Slusher Lake
Sluter Mine
Sly Creek
Small Spring
Smallman Creek
Smith Butte
Smith Canyon
Smith Canyon
Smith Canyon
Smith Canyon
Smith Creek
Smith Creek
Smith Creek
Smith Creek
Smith Creek
Smith Creek
Smith Creek
Smith Creek
Smith Creek
Smith Creek
Smith Creek
Smith Creek
Smith Creek
Smith Creek
Smith Creek
Smith Creek
Smith Creek Youth Camp
Smith Flat
Smith Gulch
Smith Hollow
Smith Lake
Smith Lake
Smith Lake
Smith McPhee Ditch
Smith Point
Smith Reservoir
Smith Elementary School (historical)
Smith Spring
Smiths Well
Smoky Hollow
Smyrna Church
Smyth Cemetery
Smyth Creek
Smyth Ranch
Smyth Reservoir
Smyth Wells
Snag Boat Bend
Snag Island Jetty
Snag Islands
Snag Spring
Snag Spring
Snaggy Bend
Snail Canyon
Snake Creek
Snake Creek
Snake Creek
Snake Eyes Spring
Snake River Mine
Snap Point
Snark Creek
Snedden Creek
Snell Hollow
Snider Creek
Snider Spring
Snip Waterhole
Sniption Canyon
Snively Gulch
Snively Hot Spring
Snow Basin
Snow Board Ridge
Snow Creek
Snow Peak
Snow Peak Camp
Snow Peak Mill City Trail
Snow Storm Reservoir
Snowmoody Ridge
Snowshoe Gulch
Snowslide Canyon
Snuff Shelter
Snyder Canyon
Snyder Creek
Snyder Creek
Snyder Meadow
Snyder Meadow Creek
Soap Creek School (historical)
Soap Spring
Soapstone Creek
Soapstone Lake
Social Ridge
Sock Creek
Sod House Dam
Sod House School (historical)
Soda Creek
Soda Lake
Soda Mountain
Soda Spring
Soda Spring
Soda Springs
Sodom Dam
Sodom Ditch
Solders Canyon
Solders Canyon Reservoir
Solders Spring
Soldier Creek
Soldier Creek
Soldier Creek
Soldier Lake
Soldier Meadows Creek
Soldier Spring
Soldier Spring
Solitude Canyon
Solomon Canyon
Solomon Canyon Reservoir
Somers Ranch
Songer Gap
Songer Butte
Soocup Canyon
Sorefoot Creek
Sorefoot Ranch
Sorenson Creek
Sorosis Park
Sorrel Spring
Soup Creek
Soup Lakes
Sourdough Basin
Sourdough Canyon
Sourdough Gulch
Sourdough Gulch
Sourdough Mountain
Sourdough Spring
South Alkali Creek
South Alkali Drain
Tugman City Park
South Ankle Creek
South Baldy
South Beede Reservoir
South Branch Camp Kettle Creek
South Bull Canyon
South Bull Canyon Reservoir
South Burn Guard Station
South Canal
South Catherine Ditch
South Chain Lake
South Channel
South Channel
South China Spring
South Clover Creek
South Corral Spring
South Coyote Canyon
South Coyote Creek
South Creek Reservoir
South Depoe Bay Creek
South Diamond Canal
South Dixie Lake
South Dry Creek Reservoir
South Eugene High School
South Falls
South Fork Battle Creek
South Fork Beaver Creek
South Fork Beaver Creek
South Fork Beaver Creek
South Fork Beaver Creek
South Fork Berry Creek
South Fork Black Creek
South Fork Boulder Creek
South Fork Brownie Creek
South Fork Buck Creek
South Fork Calapooya Creek
South Fork Camp
South Fork Carter Creek
South Fork Catching Creek
South Fork Catherine Creek
South Fork Cemetery
South Fork Clear Creek
South Fork Coffeepot Creek
South Fork Cold Springs Canyon
South Fork Cook Creek
South Fork Coos River
South Fork Corral Creek
South Fork Cottonwood Creek
South Fork Crabtree Creek
South Fork Cronin Creek
South Fork Crooked Creek
South Fork DeGarmo Canyon
South Fork Dixie Creek
South Fork Flagler Creek
South Fork Fourmile Creek
South Fork Gales Creek
South Fork Gate Creek
South Fork Goble Creek
South Fork Green Timber Creek
South Fork Guard Station
South Fork Hinkle Creek
South Fork Indian Creek
South Fork Jackson Creek
South Fork Jacobsen Gulch
South Fork Juniper Canyon
South Fork Keene Creek
South Fork Klaskanine River
South Fork Lawrence Creek
South Fork Lewis and Clark River
South Fork Lightning Creek
South Fork Limber Jim Creek
South Fork Little Willow Creek
South Fork Lobster Creek
South Fork Malheur River
South Fork Middle Creek
South Fork Mill Creek
South Fork Mohawk River
South Fork Neal Creek
South Fork Necanicum River
South Fork Nehalem River
South Fork Pedee Creek
South Fork Pete Enyart Canyon
South Fork Quartz Creek
South Fork Reese Creek
South Fork Reservoir
South Fork Rickreall Creek
South Fork Rock Creek
South Fork Rock Creek
South Fork Salmonberry River
South Fork Scott Creek
South Fork Siletz River
South Fork Silver Creek
South Fork Siuslaw River
South Fork Smith River
South Fork Spencer Creek
South Fork Spruce Run Creek
Ti-he-cha-paa nena Creek
South Fork Stell Creek
South Fork Teal Creek
South Fork Visher Creek
South Fork Youngs River
South Gregory Creek Reservoir
South Jetty
South Junction
South Lake Waterhole
South Oak Grove School
South Olsen Creek
South Patawa Creek
South Pole Mine
South Powellhurst School (historical)
South Prong Clear Creek
South Prong Pine Creek
South Quartz Mountain Reservoir
South Reservoir
Portland Lutheran School
South Scappoose Creek
South Sheep Creek
South Sheep Creek Reservoir
South Sheephead Spring
South Silver Creek Youth Camp
South Sister Creek
South Spring
South Spring Well
South Star Spring
South Trail Creek
South Twomile Creek
South Village City Park
South Wall Rock Reservoir
South Warner Rim
South Wolf Creek
South Yamhill Cemetery
Southeast Black Rock
Southport Mine
Spalding Ranch
Spalding Reservoir
Spanish Charlie Basin
Spanish Flat
Spanish Hollow
Spanish Lake
Spanish Lake
Sparks Gulch
Spatterdock Lake
Spaulding Creek
Spaulding Gulch
Spaulding Ridge
Spawning Channel
Speaker Placer
Spear Head Reservoir
Speare Canyon
Spearpoint Spring
Spears Canyon
Speelyai Creek
Spence Mountain
Spencer Butte
Spencer Butte Middle School
Spencer Creek
Spencer Creek
Spicer
Spiering Reservoir
Spikes Gulch
Spilde Creek
Spine Cob Butte
Spino Spring
Spire Rock
Spirit Hill
Spitzenberg
Split Tree Reservoir
Spodue Mountain
Sponge Spring
Spongs Bar
Spoon Creek
Spooner Ridge
Spotted Fawn Mine
Spout Creek
Spray
Spring Basin Canyon
Spring Branch
Spring Branch
Spring Branch
Spring Branch
Spring Branch Creek
Spring Brook
Spring Brook Creek
Spring Canyon
Spring Coyote Wells
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek Gulch
Spring Creek Meadow
Spring Creek Elementary School
Spring Flat
Spring Flat
Spring Gulch
Spring Gulch
Spring Gulch
Spring Hollow
Spring Hollow
Spring Hollow
Spring Hollow
Spring Hollow
Spring Hollow Creek
Spring Hollow Creek
Spring Lake
Spring Lake
Spring Mountain
Spring Mountain Way
Spring Valley
Spring Valley Community Center
Springfield
Springfield Junction
Springfield Memorial Cemetery
Springston Canyon
Sproul Canyon
Spruce Hollow
Spruce Run Creek
Spruce Run Lake
Spud Spring
Spurlock Ranch
Squally Point
Square Lake
Square Mountain
Square Mountain Creek
Square Well
Square Well Slough
Square White Rock
Squaw Butte
Táx̣špa Butte
Squaw Butte
Rettie Butte
Mulak Creek
Squaw Creek
Squaw Creek
Squaw Creek
Squaw Creek
Goose Creek
Háawpa Creek
Ede huudi Creek
Kaiba agai Creek
Yapaa Creek
Squaw Creek Reservoir
Kwii-na-a Spring
Sai-be Spring
tíkem Falls
Squaw Flat
aa-Tiipi Flat
Squaw Flat
Squaw Flat
Squaw Hollow
Qochyax Island
Squaw Lake
Latiwi Mountain
Sesti Tgawaals Point
Áatway Spring
Staats Creek
Stacey Reservoir Number One
Stacey Reservoir Number Two
Stacey Reservoir Number Three
Stacey Reservoir Number Four
Stack Creek
Stackhouse Canyon
Stafford
Stafford Cemetery
Stafford Creek
Stag Canyon
Stag Trail
Stage Gulch
Stage Gulch
Stage Road Gulch
Stage Road Pass
Stairstep Spring
Stakely Spring
Stallion Waterhole
Stalter Canyon
Standard Hollow
Standcliff Creek
Standley Cabin
Stanfield Branch Furnish Ditch
Stanfield Reservoir
Stanley Creek
Stanley Creek
Stanley Lake
Stanley Meadows
Stanley Rock
Star Creek
Star Creek Reservoir
Star Mine
Star Mine
Star Ranch
Starks Creek
Starr Spring
Starvation Point
Starvation Spring
Starveout
Starvout Creek
Stasel Falls
State Game Waterhole
State Line
State Line Spring
Stateline Reservoir
Station Canyon
Statz Spring
Stayton
Steagall Spring
Steam Beer Placer
Steamboat Point
Steamboat Ridge
Steamboat Rock
Steamboat Rock
Steamboat Rock
Stearns Butte
Stearns Dam
Stearns Ranch
Stearns Reservoir
Stebins Ridge
Stecker Canyon
Steel Bridge
Steel Creek
Steele Creek
Steelman Lake
Steens Mountain
Steep Creek
Steep Creek
Steep Slope Spring
Steer Canyon
Steer Ridge Reservoir
Steers Canyon
Steers Canyon
Steet Canyon
Stein Gulch
Steinberg Ridge
Steinhilber Creek
Steinnon Creek
Steiwer Hill
Steiwer Peaks
Stell Creek
Stella Range
Stemler Basin
Stemler Ridge
Stemler Ridge Reservoir
Roberts Field
Step Creek
Stephens
Sterling Forest Station
Stevens Gulch
Stevens Point
Stewart Carter Ditch
Stewart Creek
Stewart Homestead
Stewart Lake
Stewart School (historical)
Stewart Slough
Stewart Spring
Stewart Spring
Stices Gulch
Sticky Joe Spring
Stiles Spring
Still Gulch
Stillman Park
Stingel Canyon
Stinger Gulch
Stinkingwater Basin
Stinkingwater Creek
Stinkingwater Mountains
Stinkingwater Pass
Stinkingwater Reservoir Number Two
Stipp Memorial Cemetery
Stock Ditch
Stock Slough
Stockade Buttes
Stockade Creek
Stockade Creek
Stockade Creek
Stockade Mountain
Stockade Springs
Stockel Creek
Stone Bridge
Stone Cabin Creek
Stone Corral
Stone Corral Lake
Stone Gulch
Stonehouse Creek
Stonehouse Creek
Stony Creek
Stony Creek
Stony Mountain
Stony Point
Storm Mountain
Stout Creek
Stout Mountain
Stove Spring
Stovepipe Gulch
Stovepipe Spring
Stavebolt Creek
Stradley Drain
Straight Creek
Straight Creek
Strait Spring
Strassel Creek
Straw Fork Butte Creek
Straw Ranch Creek
Strawberry Canyon
Strawberry Lake
Strawberry Mountain
Strawberry Ridge
Stray Dog Reservoir
Street Canyon
Street Canyon Spring
Stringer Spring
Striped Mountain
Strubes Forest Camp (historical)
Struby Creek
Strum Creek
Stub Creek
Stub Mine
Stubb Hollow
Stubblefield Canal
Stubblefield Mountain
Stud Horse Reservoir
Studer Ridge
Studhorse Canyon
Stukel Bridge
Stukel Mountain
Stulls Falls
Stump Spring
Stump Spring
Stump Spring Butte
Penny Sturdivant Park
Sturdy Creek
Sturgeon Lake
Sturgis Mine
Sturtevant Creek
Sublimity
Submarine Rock
Sucker Creek
Sufferin Smith Spring
Sugar Creek
Sugar Pine Flat
Sugar Pine Ridge
Sugarloaf
Sugarloaf
Sugarloaf
Sugarloaf
Sugarloaf Butte
Sugarloaf Butte
Sugarloaf Canyon
Sugarloaf Canyon
Sugarloaf Mountain
Sugarloaf Mountain
Sugarloaf Mountain
Sugarloaf Mountain
Sugarloaf Mountain
Sugarloaf Mountain
Sugarloaf Reservoir
Suitter Creek
Sullivan Gulch
Sullivan Spring
Sulphur Spring
Sulphur Springs
Summit
Summit
Summit Cemetery
Summit Creek
Summit Creek
Summit Lake
Summit Mine
Summit Prairie
Summit Ranch
Summit Ridge
Summit Spring
Summit Spring Forest Camp (historical)
Sumner Pioneer Cemetery
Sumpter Reservoir
Sunflower Flat
Sunflower Flat Pond
Sunflower Flat Spring
Sunny Hill Cemetery
Sunny Valley
Sunnybrook Mine
Sunnycrest
Sunnydale School (historical)
Sunnyside
Sunnyside School (historical)
Sunnyside Environmental School
Sunnyslope Ditch
Sunnyslope Pit
Sunrise Cemetery
Sunrise Elementary School
Sunrise Spring
Sunrise Valley
Sunrise Waterhole
Sunset Bay State Park
Sunset Beach
Sunset Camp
Sunset High School
Sunset Highway State Park
Sunset Hills Memorial Gardens
Sunset Hills Memorial Park
Sunset Lake
Sunset Memorial Park
Sunset Mine
Sunset Prairie
Sunset Safety Rest Area
Sunset Primary School
Sunset Elementary School
Sunset Spring
Sunset Spring
Sunset Tunnel 2552
Sunset Valley
Sunset Valley School (historical)
Sunshine Canyon
Sunshine Valley
Sunstone Area
Suppah Windmill
Supply Creek
Surveyor Spring
Surveyors Lake
Surveyors Spring
Susan Creek
Sutherland Cabin
Sutherlin
Sutherlin Creek
Satter Creek
Sutton Creek
Sutton Mountain
Sutton Ranch
Suzy Island
Svensen
Svensen Island
Svensen Junction
Svensen School (historical)
Swaggart Buttes
Swain
Swallow Lake
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek Cow Camp
Swamp Creek Ranch
Swamp Creek Reservoir
Swamp Lake
Swamp Mountain
Swan Creek
Swan Island Basin
Swan Lake
Swan Lake
Swan Lake Valley
Swan Lakes
Swanson Canyon
Swanson Creek
Swartz Canyon
Swartz Creek
Swartz Creek
Swash Lake
Swayne Creek
Swayze Creek
Sweat Creek
Swede Creek
Swede Flat
Swede Flat Creek
Swede Flat Reservoir
Swede Reservoir
Sweeney Canyon
Sweeney Creek
Sweet Home
Sweet Home Creek
Sweet Home Creek
Gilliland Cemetery
Sweet Point
Sweet Spring Creek
Sweet Spring Mountain
Sweetbriar Creek
Sweetbriar Mine
Sweetmilk Canyon
Sweetwater Creek
Swegle Elementary School
Swigert Cow Camp
Swisher Reservoir
Sycamore
Sycan Fire Guard Station
Sykes Creek
Mount Sykes
Symbol Rock
Symentire Spring
Sypher Gulch
Syrup Spring
TC Reservoir
TC Spring
T Canal
T Canal
T P Spring
T V Ridge
TT Canyon
Table Creek
Table Creek
Table Land
Table Mountain
Table Mountain
Table Mountain
Table Mountain
Table Mountain
Table Mountain
Table Reservoir
Table Reservoir
Table Rock
Table Rock
Table Rock
Table Rock School (historical)
Table Top Reservoir
Tableland Reservoir
Tegart Bluff
Takena Park
Tamarack Creek
Tamarack Creek
Tamarack Creek
Tamarack Flat
Tamarack Mountain
Tamarack Spring
Tamolitch Falls
Tanawasher Spring
Tangent
Tangent Elementary School
Tangerman Creek
Tank Creek
Tank Spring
Tanner Creek
Tanner Creek
Tansy Creek
Tansy Point
Tap Horn Canyon
Tap Horn Gap
Tarheel Arm
Tarter (historical)
Tater Hill
Tater Patch Gulch
Taylor Butte
Taylor Butte
Taylor Castle
Taylor Creek
Taylor Creek
Taylor Green
Taylor Grove
Taylor Lake
Taylor Lake
Taylor Point
Taylor Ranch
Taylor Ranch
Taylor Ridge
Taylor Sands
Taylor Spring
Taylor Springs
Taylors Reservoir
Teal Creek
Teasel Creek
Teddy Spring Reservoir
Tee Wees Butte
Teepee Creek
Telephone Canyon
Tellurium Peak
Temple Lake
Ten Cent Lake
Ten Year Reservoir
Tenas Lakes
Tenasillahe Island
Tencent Placer Mine
Tenmile Canyon
Tenmile
Tenmile Creek
Tenmile Creek
Tenmile Creek
Tennessee Gulch
Tennessee Gulch
Tennessee Middle School (historical)
Terminal Number 1
Terry Ranch
Terry Reservoir
Terry Spring
The Portland French School
Tesch Draw
Tetherow Butte
Tex Martin Lake
Texaco Basin
Thatcher (historical)
Thayer Creek
The Basin
The Basin
The Beef Trail
The Big Slide
The Blue Banks
The Bumpheads
The Butte
The Butte
The Buttes
The Buttes
The Cliff
The Cove
The Dalles Bridge
The Dipper
The Dome
The Elbow
The Falls
The Flat
The Flatiron
The Flatirons
The Gap
The Gooseneck
The Heads
The Hogback
The Hogback
The Hole in the Ground
The Homestead
The Hunters Cabin
The Island
The Lakes Lookout
The Lakes Lookout Spring
The Lambing Ground
The Meadow
The Monuments
The Narrows
The Narrows
The Narrows
The Narrows
The Neck
The Needles
The Nook
The Oaks Amusement Park
The Oxbow
The Palisades
The Park School (historical)
The Pot
The Potholes
The Rafferty
The Sag
The Troughs
The Whitenburg
The Yellow Jacket
Theimer Spring
Roosevelt Middle School
Thesing Bar
Thicket Spring
Thief Valley
Thief Valley Dam
Thief Valley Reservoir
Thimbleberry Spring
Third Creek
Third Creek Reservoir
Third Lake
Thirsty Camp Trail
Thistle Creek
Thistleburn Creek
Thistleburn Ridge
Thistledew Spring
Thomas Cairn
Thomas Creek
Thomas Creek
Thomas Creek
Thomas Creek
Thomas Creek Basin
Thomas Creek Ridge
Thomas Mountain
Thompson Canyon
Thompson Canyon
Thompson Creek
Thompson Creek
Thompson Creek
Thompson Dam
Thompson Peak
Thompson Reservoir
Multnomah Early Childhood Program
Thompson Slough
Thompson Spring
Thompson Spring
Thompson Well
Thorn Creek
Thorn Creek
Thorn Flat
Thorn Hollow
Thorn Hollow
Thorn Hollow Creek
Thorn Lake
Thorn Spring
Thorn Spring
Thorn Spring
Thorn Spring
Thorn Spring
Thorn Springs
Thorne and Wisdom Lake
Thorne Bridge
Thornton Creek
Thornton Gulch
Thornton Lake
Thornton Spring
Thousand Acre Pasture
Thousand Springs Creek
Thousand Springs Ranch
Three Bucket Spring
Three Fingers Gulch
Three Fingers Rock
Three Fingers Spring
Three Lakes
Three Lakes Country
Three Pine Butte
Three Spring Ranch
Three Springs
Three Story Rim
Threemile Canyon
Threemile Creek
Threemile Creek
Threemile Creek
Threemile Falls Diversion Works
Threemile Hill
Threemile Ranch
Threemile Reservoir
Threemile Reservoir
Thrush Cemetery
Thunderbird Lake
Thurston
Thurston High School
Thurston Elementary School
Tibbett Spring
Tichenor Rock
Tidbits Creek
Tidbits Mountain
Tide Creek
Tietz Creek
Tiffin Reservoir Number One
Tiffin Reservoir Number Two
Tigard
Tigard High School
Charles F Tigard Elementary School
Tillamook Head
Tilley Canyon
Tillotson Cemetery
Tim Brown Spring
Tim Spring
Timber
Timber Canyon
Timber Canyon
Timber Culture Gulch
Timber Grove
Timber Gulch
Timber Gulch
Timber Mountain
Timber Substation
Timber-Linn Lake
Timber - Linn Memorial Park
Time and a Half Spring
Timene Canyon
Timothy Creek
Timothy Ridge
Tims Peak Reservoir
Tims Peak Spring
Tin Can Draw
Tin Can Draw Reservoir
Tin Can Reservoir
Tin Can Ridge
Tin Can Spring
Tin Cup Spring
Tinpan Mine
Tioga Creek
Tioga Guard Station
Tip Davis Creek
Tipsoo Butte
Tipsoo Creek
Tipsoo Peak
Tipsoo Trail
Tired Horse Reservoir
Tittie Butte
Titus Pond
Tivate Canyon
Tobias
Todd Canyon
Toe Island
Tohet Spring
Tokatee Lakes
Tolovana Park
Tom Creek
Tom East Creek
Tom East Creek
Big Tom Folley Creek
Tom Reservoir
Tom Rock
Tom Taylor Canyon
Tomahawk Island
Tombstone
Tombstone Canyon
Tommies Homestead
Tompkins Bar
Tompkins Pass
Toms Creek
Toms Lake
Tongue Neck
Tongue Point
Tongue Point Bar
Tongue Point Channel
Toni Lake
Toney Butte
Tooley Lake
Tooter Creek
Top of the Hill Waterhole
Top Hat Reservoir
Top Reservoir
Tope Spring
Tophill
Toppin Creek
Toppin Creek Butte
Toppin Creek Canyon
Torrey Lake
Totten Creek
Totten Creek
TouVelle State Park
Tower Rock
Tower Spring
Towne Gulch
Townsite Ditch
Trail Canyon
Trail Canyon
Trail Creek
Trail Creek
Trail Creek
Trail Creek
Trail Creek
Trail Creek
Trail Creek
Trail Creek Spring
Trail Creek Trail
Trail Fork Canyon
Trail Fork School (historical)
Trail Gulch
Trail Hollow
Trail Hollow Creek
Trail Reservoir
Trail Reservoir
Trail Reservoir
Trail Spring
Trail Spring
Train Lake
Tramway Spur
Trap Hole
Trap Springs
Trapp Creek
Trapper Creek
Trappers Camp
Trappist Abbey of Our Lady of Guadalupe
Trask Guard Station
Trask House
Trask Mountain
Traverse Lake
Treadwell Creek
Treharne
Trembley Lake
Trenholm
Trent
Trespass Reservoir
Treasure Valley Community College
Tri City
Triangle Lake
Triangle Lake
Triangulation Peak
Tricky Draw
Trimble Creek
Trimbly Creek
Trinity Guard Station
Trinity Lutheran Cemetery
Trinity Lutheran Church
Trinity Lutheran School
Tripp Canyon
Trippier Point
Trojan
Tronson Island
Trout Creek
Trout Creek
Trout Creek
Trout Creek
Trout Creek
Trout Creek
Trout Creek
Trout Creek
Trout Creek Camp
Trout Creek Mountains
Trout Lake
Troutdale
Troutdale Substation
Truax Creek
Truax Island
True Blue Gulch
Tryon Creek
Tualatin
Tualatin Elementary School
Tualatin View School (historical)
Tub Butte
Tub Mountain
Tub Run
Tub Spring
Tub Spring
Tub Spring
Tub Spring
Tub Springs
Tub Springs Canyon
Tubb Creek
Tubb Spring
Tuck Spring
Tucke Flat
Tucker Bridge
Tucker Canyon
Tucker Creek
Tucker Creek
Tucker Creek
Tucker Maxon Oral School
Tucker Slough
Tudor Canyon
Tudor Lake
Tuesday Reservoir
Tuffy Creek
Tulana Farms
Tule Lake
Tule Lake
Tule Pond
Tule Spring
Tule Spring
Tule Springs Rims
Tull Reservoir
Tuller Creek
Tulsa
Tumalo
Tumalum School (historical)
Tumble Spring
Tumtum Lake
Tunnel Canyon
Tunnel Creek
Tunnel Creek
Tunnel Creek
Tunnel Millrace
Tunnel Number 3
Tunnel Number 4
Tunnel Number 5
Tunnel Number 7
Tunnel Point
Tunnel Ridge
Tunnel Spring
Turnbow Creek
Turnbull Lakebed
Turnbull Mountain
Turnbull Peak
Turnbull Well
Turner Butte
Turner Canyon
Turner Creek
Turner Creek
Turner Reservoir
Turner Spring
Turpentine Creek
Turpentine Lake
Turpentine Peak
Turpentine Peak Trail
Turpin Lake
Turrell Canyon
Turtle Cove
Turtle Rock
Tuskan
Tutuilla Creek
Tutuilla Mission
Twality Middle School
Twelve O'Clock Mine
Twelvemile Creek
Twelvemile Peak
Twentymile Slough
Twentymile Springs
Twentythree Creek
Twickenham
Twin Buttes
Twin Butte Spring
Twin Buttes
Twin Buttes
Twin Cedar Spring
Twin Craters
Twin Falls
Twin Knolls Spring
Twin Lake
Twin Lakes
Twin Lakes
Twin Lakes
Twin Lakes
Twin Lakes
Twin Lakes
Twin Lakes
Twin Lakes Trail
Twin Meadows
Twin Mountain
Twin Mountain Creek
Twin Oaks Cemetery
Twin Oaks Memorial Gardens
Twin Oaks Elementary School
Twin Peaks
Twin Points
Twin Reservoir
Twin Sisters (historical)
Twin Sisters Trail (historical)
Twin Spring
Twin Springs
Twin Springs
Twin Springs
Twin Springs
Twin Springs
Twin Springs
Twin Tank Spring
Twin Wells
Cousins
Twisty Creek
Two Butte
Two Color Guard Station
Two Day Reservoir
Two Forks Check Dam
Two Girls
Two Girls Creek
Two Pipes Springs
Two Springs Ranch
Two Way Reservoir
Twomile
Twomile Creek
Twomile Ridge
Twomile Spring
Tybow Canyon
Tyee Camp
Tyee Mountain
Tygh Ridge
Tygh Ridge Summit
Tygh Valley
Tygh Valley Fairgrounds
Tyler Creek
Tyrell Spring
Grant City Park
Umatilla
Umatilla Butte
Umatilla Drain
Umatilla Meadows
Umbrite Lake
Umpcoos Ridge
Umpqua
Umpqua Gulch
Uncle Dan Mine
Uncle Sam Mine
Union
Union Cemetery
Union Creek
Union Creek
Union Creek Recreation Site
Union Gap
Fern Ridge Middle School
Lebanon High School
Stayton High School
Union High School (historical)
West Linn High School
Sandy High School
J B Thomas Middle School (historical)
Union Point Cemetery
Union School (historical)
Unionvale
Unit Reservoir
United States Creek
Unity Creek
Oregon Health Sciences University School of Dentistry
University of Oregon Housing
University of Oregon
University of Portland
University City Park
Upper Baisley-Elkhorn Mine
Upper Berley Lake
Upper Blaylock Canyon Spring
Upper Bridge Creek Draw Reservoir
Upper Buckbrush Reservoir
Upper Butler Reservoir
Upper Campbell Lake
Upper Cherry Creek Ranch
Upper Clark Reservoir
Upper Cow Lake
Upper Cow Reservoir
Upper Davis Dam
Upper Ditch
Upper Dry Lake Number 1
Upper Dry Lake Number 2
Upper Dugout Creek Reservoir
Upper Elk Meadows
Upper Fisher Long Ditch
Upper Fishtrap Cemetery
Upper Fort Creek Reservoir
Upper Gregory Creek Reservoir
Upper Hanley Canal
Upper Horse Camp Reservoir
Upper Jack Creek Reservoir
Upper Kane Spring Reservoir
Upper Lake
Upper Lambert Bar
Upper McCain Springs
Upper McNulty Reservoir
Upper Meadow Reservoir
Upper Midway Reservoir
Upper Mud Spring
Upper Mud Spring
Upper Mud Spring
Upper North Fork
Upper Peavine Flat
Upper Potter Reservoir
Upper Rugg Spring
Upper Saddle Butte Reservoir
Upper Sand Spring
Upper Sheep Creek Reservoir
Upper Sizemore Spring
Upper Slim and Fatty Reservoir
Upper Syrup Spring
Upper Timber Canyon
Upper Turner Gulch
Upper Walker Reservoir
Upset Spring
Upton Cabin
Upton Mountain
Upton Mountain Reservoir Number One
Upton Mountain Reservoir Number Two
Upton Pass
Utley Cabin
Utts Butte
V W McCormack Area
V Canal
V Lake
Vail Creek
Vale Butte
Valentine Creek
Valet Spring
Valley Falls
Valley Lane Hospital (historical)
Valley View Cemetery
Valley View Lutheran Cemetery
Valley View School (historical)
Van Brimmer Canal
Van Curen Creek
Van Derveer Reservoir
Van Dine Creek
Van Horn Creek
Van Meter Flat
Van Patten Butte
Van Patten Lake
Van Patten Ridge
Vancouver Lower Channel
Vancouver Range
Vanport City (historical)
Varco Well
Vaughn Canyon
Vaughn Creek
Vaughn Reservoir
Vaughns Creek
Vee Lake
Vee Springs
Velvet Creek
Venator Ranch
Venator Reservoir
Venta Spring
Ventura Park Elementary School
Vernon Elementary School
Vernonia
Vernonia Grange
Vernonia Lake
Vesper School
Vestal Butte
Vestal Elementary School
Vey Ranch
Vey Spring
Victor Mine
Victor Point Elementary School
Vida
Vidler Creek
Grave Island Memorial
Villa Ridge
Villwock Reservoir
Vincent Creek
Vincent Ranch
Vines Ditch
Vineyard Mountain
Vinson Canyon
Vinson Cemetery
Vinson Ranch
Viola
Virginia Lake
Virginia Valley
Virginia Valley School (historical)
Virtue Flat
Virtue Mine
Visher Creek
Visher Reservoir
Vitae Springs
Vitus Butte
Vogel Creek
Vogel Pond
Vogel Reservoir
Volmer Creek
Voltage Well
Vondergreen Hill
Vose Elementary School
Childrens Farm Home
Wade Creek
Waggoner Creek
Wagner Creek
Wagner Gulch
Wagner Mountain
Wagner Ranch
Wagon Reservoir
Wagon Wheel Creek
Wagon Wheel Flat
Wagonwheel Hole
Wagonwheel Park
Wahoo Gulch
The Dalles-Wahtonka High School (historical)
Wakefield Creek
Waldo Gulch
Waldo Middle School
Waldo Spring
Waldron School (historical)
Walker Canyon
Walker Island Channel
Walker Creek
Walker Creek
Walker Creek
Walker Creek
Walker Creek
Walker Creek
Walker Drain
Walker Island
Walker Lake
Walker Mountain
William Walker Elementary School
Walker Union School (historical)
Wall Creek
Wall Rock
Wall Rock Creek
Wall Rock Ridge
Wall Rock Springs
Wallace Canyon
Wallace Canyon
Wallace Creek
Wallace Creek
Wallace Island
Wallace School (historical)
Wallace Slough
Wallooskee River
Walls Lake
Walls Lake Canyon
Walls Lake Well
Walls Reservoir
Waln Creek
Walnut Eddy
Walnut Hill
Gresham Butte
Walters Spring
Walterville
Walterville Canal
Walterville Reservoir
Walterville Elementary School
Walton Cemetery
Walton Slough
Waluga Park East
Wampus Cat Canyon
Wankers Corner
Wapato Creek
Ward Butte
Ward Butte
Ward Creek
Ward Creek
Ward Creek
Ward Creek
Ward School (historical)
Wards Butte
Warfield Meadow
Warm Creek
Warm Lake
Warm Mineral Spring
Warm Spring
Warm Spring
Warm Spring
Warm Spring
Warm Spring Creek
Warm Spring Creek
Warm Springs
Warm Springs
Warm Springs Butte
Warm Springs Canal
Warm Springs Creek
Warm Springs Creek
Warm Springs Creek
Warm Springs Reservoir
Warm Springs Reservoir
Warm Springs Valley
Warm Springs Valley
Warner Cemetery
Warner Cemetery
Warner Creek
Warner Creek
Warner Lake
Warner Lakes
Warner Pacific College
Warner Peak
Warner Valley
Warnicke Creek
Warren
Warren Canyon
Warren Creek
Warren Creek
South Columbia Family School
Warren Slough
Warren Spring
Warren Stephens Homestead
Warrenton Dam
Warrenton High School
Warrenton Reservoir
Warrenton Grade School
Warrior Point
Warrior Rock
Wasco
Wasco Butte
Wasco Light
Wash Rock
Washboard Reservoir
Washboard Reservoir
Washburn Butte
Washburne City Park
Washburne State Park
Washing Machine Flat
Washington Gulch
Washington Monroe High School (historical)
Washington City Park
Washington City Park
Washington Elementary School
Washington School (historical)
Washington School (historical)
Holt Elementary School
Washington Elementary School
Washington Elementary School
Vernonia Elementary School
Washington Gulch
Washout Creek
Washpan Lake Waterhole
Wasson Creek
Watches Butte
Water Board Park
Water Branch
Water Gulch
Water Gulch
Water Gulch
Water Gulch
Water Hole Butte
Waterhole Reservoir
Water Pipe Gulch
Water Tank Creek
Water Tank Gulch
Water Trough Draw
Waterfall Canyon
Waterfalls Hollow
Waterhole Spring
Watering Trough Draw
Waterman
Waterman Flat
Watermelon Creek
Watermelon Trail
Waterspout Creek
Waterspout Gulch
Waterworks Creek
Watkins Spring
Watkins Spring
Watson (historical)
Watson Canyon
Watson Cemetery
Watson Spring
Waud Bluff
Wauna
Waverly Baby Home
Waverly Lake
Waverly Elementary School
Wawa Creek
Way Cemetery
Way Ranch
Weatherby Mountain
Weatherly Creek
Weatherly Spring
Weaver Creek
Weaver Gulch
Weaver Lake
Weaver Placer
Weaver Spring
Webb Lake
Webb Lake
Webb Spring
Webb Spring Creek
Webb Springs
Weber Gulch
Webfoot
Webfoot Creek
Webfoot Creek
Webfoot Meadow
Webster Flat
Wedeburg
Wednesday Reservoir
Weed Creek
Weed Lake
Weed Lake
Weed Lake Butte
Weed Lake Butte Waterhole
Weed Lake Flat
Weekly Creek
Wegner Creek
Wegner Creek
Wehmeyer Creek
Wehrli Canyon
Weir Ranch
Weiss Bridge
Welch Drain
Welch Island
Welch Island
Weldwood Park
Well Number Two
Well Number Three
Well Number Four
Well Number Five
Well Number Six
Well Number Seven
Well Spring
Well Spring Canyon
Wellington Butte
Wellington City Park
Wells Cemetery
Wells Creek
Wells Spring
Welsh Gulch
Welsh Spring
Wendling Glade
Wendt Ditch
Wendt Gulch
Wertz Draw
West (historical)
West Arm
West Bay
West Beaver Creek
West Bench
West Black Butte Reservoir
West Branch Falls Creek
West Branch Mulak Creek
West Branch West Crockett Branch
West Brush Creek
West Canal
West Chain Lake
Riverside Elementary School
West Conical Rock
West Cow Creek
West Crater
West Creek
West Creek
West Creek
West Crockett Branch
West Dry Creek Reservoir
West Eagle Creek
West Eagle Meadow
West Eagle Trail
West Extension Irrigation Canal
West Field Lake
West Ford
West Fork
West Fork Beaver Creek
West Fork Big Pasture Creek
West Fork Birch Creek
West Fork Boundary Creek
West Fork Butte Creek
West Fork Butte Creek Reservoir
West Fork Canyon Creek
West Fork Carcus Creek
West Fork Coal Creek
West Fork Little Cottonwood Creek
West Fork Cottonwood Creek
West Fork Deer Creek
West Fork Dry Creek
West Fork Ecola Creek
West Fork Evans Gulch
West Fork First Creek
West Fork Glenn Creek
West Fork Greasewood Creek
West Fork Horse Creek
West Fork Juniper Creek Reservoir
West Fork Koontz Creek
West Fork Lake Creek
West Fork Lake Creek
West Fork Little Bear Creek
West Fork Little Pudding River
West Fork Marys River
West Fork Mill Creek
West Fork North Fork Wilson River
West Fork Palmer Creek
West Fork Pebble Creek
West Fork Phipps Creek
West Fork Pine Creek
West Fork Russel Creek
West Fork Silver Creek
West Fork Silvies River
West Fork Spring Hollow Creek
West Fork Stack Creek
West Fork Sutton Creek
West Fork Tucker Creek
West Fork Upper Timber Canyon
West Fork Whisky Creek
West Gresham Elementary School
West Haven
West Hills Christian School
West Hills Intermediate
West Humbug Creek
West Hurlburt Camp
West Lake
West Lawn Memorial Park
West Light
West Linn
West Little Owyhee River
West Little Pine Hollow
West Olalla Creek
West Page Cabin Spring
West Park Elementary School
West Point Hill
West Powellhurst Elementary School
West Road Gulch
West Saint Helens
West Side
West Side School (historical)
West Slope
West Spring
West Stanfield School (historical)
West Stayton
West Sylvan Middle School
West Trinity Creek
West Tualatin View Elementary School
West Vidler Creek
West Weed Lake Butte Waterhole
West Well
West Whitehorse Reservoir
West Willis Creek
Wester Butte
Western Camp
Western Seminary - Portland Campus
Western Mennonite School
Western Union Basin
Western Union Mine
Westfall Butte
Westfield Pit
Westmoreland
Westmoreland City Park
Lane School
Weston
Weston Bar
Weston Bend
Weston Cemetery
Weston Station
Westport Channel
Westport Slough
Wetle Spring
Whale Cove
Wheaton Creek
Wheel Gulch
Wheeler
Wheeler Canyon
Wheeler Flat
Whetstone Creek
Whipple Gulch
Whiskey Canyon
Whiskey Creek
Whiskey Creek
Whiskey Creek
Whiskey Creek
Whiskey Creek
Whiskey Creek
Whiskey Flat
Whiskey Spring
Whiskey Spring
Whiskey Spring
Whiskey Spring Number Two
Whiskey Springs
Whiskey Springs
Whiskey Springs
Whisky Butte
Whisky Creek
Whisky Creek
Whiskey Creek
Whisky Creek Spring
Whisky Gulch
Whisky Gulch
Whisky Gulch
Whisky Gulch
Whisky Gulch Springs
Whisky Hill
Whisky Springs
Whistle Point
Whitaker Lake
Native American Youth Association Early College Academy
Whitcher Creek
Whitcomb Creek
Lot Whitcomb Elementary School
White Branch Youth Camp
White Canyon
White City
White Cow Pit Reservoir
White Creek
White Creek
White Creek
White Creek
White Ditch
White Door Canyon
White Fir Spring
White Horse Creek
White Horse Rapids
White Lake
White Mountain
White Mule Flat
White Pine Marsh
White Point
White Reservoir
White Reservoir
White Rock Creek
White Rock Creek
White Rock Creek
White Rock Gulch
White Rock Gulch
White Rock Ranch
White Rock Reservoir
White Rock Ridge
White Rock Spring
White Rock Spring
White Shield Home
White Swan Gulch
White Swan Mine
White Tail Ridge
White Wash Reservoir
Whiteaker Elementary School (historical)
Whitehorse Butte
Whitehorse Butte
Whitehorse Butte Reservoir
Whitehorse Creek
Whitehorse Creek
Whitehorse Creek
Whitehorse Ranch
Whitehorse Ridge
Whiteman Bar
Whitewater Campground (historical)
Whitewater Spring
Whiting Slough
Whitley Canyon
Whitley Creek
Whitman Elementary School
Whitmore Canyon
Whitney Creek
Whittaker Flats
Whitten Canyon
Whittier Lake
Whitts Cache Spring
Whitworth Creek
Whyte Park Rest Area
Wiard Park
Wickiup Creek
Wickiup Gulch
Wickiup Lake
Wickiup Ridge
Wickiup Springs
Wicks Reservoir
Widgeon Lake
Widow Spring
Widows Creek Burn
Wigrich Landing
Wilcox
Wilcox Canyon
Wilcox Elementary School
Wild Ace Lake
Wild Cheat Meadow
Wild Gal Spring
Wild Horse
Wild Horse Basin
Wild Horse Butte
Wild Horse Creek
Wild Rose Camp
Wild Rose Point
Wild Rose Reservoir
Wildcat Canyon
Wildcat Canyon Reservoir
Wildcat Creek
Wildcat Creek
Wildcat Creek
Wildcat Creek
Wildcat Creek
Wildcat Creek
Wildcat Creek
Wildcat Creek
Wildcat Creek Reservoir
Wildcat Glades
Wildcat Mountain
Wildcat Mountain
Sharp Top
Wildcat Point
Wildcat Ridge
Wildcat School
Wildcat Spring
Wildcat Waterhole
Wildhorse Basin
Wildhorse Basin Reservoir
Wildhorse Canyon
Wildhorse Creek
Wildhorse Creek
Wildhorse Creek
Wild Horse Lake
Wildhorse Lake
Wildhorse Spring
Wildhorse Spring
Wildhorse Spring
Wildhorse Valley
Wildwood School (historical)
Wilelada Creek
Wiley Creek
Wilhoit
Wilkerson Creek
Wilkerson Horse Camp Spring
Wilkes Elementary School
Willa Lake
Willakenzie School (historical)
Willamalane Park
Willamette Heights
Willamette Heights Park
Willamette High School
Willamette Memorial Park
Willamette National Cemetery
Willamette Park & Boat Ramp
Willamette Stone State Park
Ridgeline Montessori Public Charter School
William Creek
William L Finley National Wildlife Refuge
Williams Butte
Williams Canyon
Williams Canyon
Williams Charco
Williams Creek
Williams Creek
Williams Creek
Williams Creek
Williams Creek
Williams Creek
Williams Ditch
Williams Ditch
Williams Guard Station
Williams River
Williams Spring Number Two
Williams Spring Number Three
Williams Springs
Williamson Creek
Willis Creek
Willis Creek
Willis Creek
Willis Creek Cemetery
Willow Bar Islands
Willow Basin
Willow Canyon
Willow Canyon
Willow Creek
Willow Creek
Willow Creek
Willow Creek
Willow Creek
Willow Creek
Willow Creek
Willow Creek
Willow Creek
Willow Creek
Willow Creek
Willow Creek
Willow Creek
Willow Creek
Willow Creek Butte
Willow Creek Butte
Willow Creek Lake
Willow Flat
Willow Flat
Willow Hole
Willow Island
Willow Lake
Willow Point
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring Canyon
Willow Spring Canyon
Willow Spring Creek
Willow Spring Creek
Willow Spring Creek
Willow Springs
Willow Springs
Willow Springs Camp
Willow Springs School
Willow Valley Reservoir
Wills Canyon
Wilsey Reservoir
Wilshire City Park
Wilson Bridge
Wilson Canyon
Wilson Corner
Wilson Creek
Wilson Creek
Wilson Creek
Wilson Creek
Wilson Creek
Wilson Creek
Wilson Creek
Wilson Creek
Wilson Creek
Wilson Creek
Wilson Creek
Wilson Creek
Wilson Creek Spring
Wilson Draw
Wilson Junior High School (historical)
Wilson Lake
Wilson Lake
Wilson Lake
Rieke Elementary School
Wilson Reservoir
Wilson Spring
Wilson Spring
Wimer
Wimer Creek
Win Ridge
Winchester
Winchester Baldy
Wind Creek
Wind Creek Peak
Windfall Adverse
Windless Gulch
Windmill Canyon
Windmill Canyon
Windsor Bar
Windy Brown Spring
Windy Creek
Windy Gap
Windy Gap
Windy Gap Mine
Windy Hollow Draw
Windy Point
Windy Point
Windy Point
Windy Reservoir
Windy Ridge
Wingate Canyon
Wingate Spring
Wingville
Wingville Cemetery
Winkle Lake
Winnemucca Creek
Winona (historical)
Winona Cemetery
Winslow Gulch
Winston
Winston Dillard County Park
Winter Camp
Winter Canyon Spring
Winter Falls
Winter Range Well
Winter Ridge
Winter Spring
Winter Water Creek
Winterville
Wire Corral
Wire Corral Springs
Wire Reservoir
Wirth Lake
Wirth Reservoir
Wisdom Creek
Wise Creek
Wiseman Island
Wiser Creek
Wisner Cemetery
Witch Hazel
Witch Hazel Elementary School
Witzel Ranch
Witzel Reservoir
Witzel Spring
Witzel Well
Wocus
Wolf Creek
Wolf Creek
Wolf Creek
Wolf Creek
Wolf Creek
Wolf Creek
Wolf Creek
Wolf Creek
Wolf Creek
Wolf Creek
Wolf Creek
Wolf Creek
Wolf Creek
Wolf Creek Store (historical)
Wolf Hollow
Wolf Hollow
Wolf Hollow Falls
Wolf Meadow
Wolf Mountain
Wolf Rock
Wolf Run
Wolf Spring
Wolford Canyon
Wolverine Meadow
Wood Camp Creek
Wood Camp Reservoir
Wood Creek
Wood Creek
Wood Creek
Wood Creek
Wood Gulch
Wood Gulch
Wood Hollow
Wood Road Reservoir
Wood Spring
Woodchopper Spring
Woodcock Creek
Woodford Creek
Woodlawn Elementary School
Woodmansee City Park
Woodpecker Creek
Woodpecker Ridge
Woodroad Waterhole
Woodrow Wilson High School
Woodruff Creek
Woodruff Mountain
Woods Creek
Woods Creek
Woods Creek
Woods Hollow
Woods Memorial Natural Area
Woodstock City Park
Woodward Creek
Woody Island
Woody Island Channel
Wool Lake
Woolen Canyon
Ward Reservoir
Workman Cemetery
Worlow Meadow
Worsham Butte
Worthington Spring
Wrangle Basin
Wrangle Butte
Rhine Hollow
Wren Smith Creek
Wright Canyon
Wright Creek
Wright Elementary School
Wright Slough
Wright Spring
Wrights Point
Wyatt Elementary School (historical)
Wycoff Creek
Wyman Creek
Wyman Spring
Wynne Watts School (historical)
Y Spring
Y Spring
Yainax Butte
Lafayette Locks County Park
Yamsay Mountain
Yank Creek
Yank Gulch
Yankee Creek
Yankee Creek Siphon
Yankee Run
Yankey Sawmill
Yankton
Yankton - Hillcrest Cemetery
Yantis Canyon
Yaquina Head
Yarnell Canyon
Yellow Butte
Yellow Butte
Yellow Creek
Yellow Creek
Yellow Dog Canyon
Yellow Fingers Reservoir
Yellow Jacket Creek
Yellow Jacket Flat
Yellow Jacket Spring
Yellow Jacket Spring
Yellow Jacket Spring
Yellow Jacket Spring
Yellow Lake
Yellow Spot Reservoir
Yellow Spot Well
Yellowhorn Mine
Yellowjacket Mountain
Yellowjacket Reservoir
Yellowstone Creek
Yellowstone Guard Station
Yellowstone Mountain
Yergen Creek
Yew Ridge
Yew Spring
Yoder Quarry
Yolanda Elementary School
Yoncalla Creek
Mount Yoncalla
Young America Mine
Young Creek
Young Hill
Cal Young Middle School
Young School (historical)
Youngs Bay
Youngs Bay Bridge US-101 Alternate
Youngs Bay Entrance Light
Youngs Bay Light
Youngs Canyon
Youngs River
Youngs River Falls
Youngs River Falls School (historical)
Pioneer Special Education Program
Younker Point
Yunkers High Bridge
Z Canal
Zachary Canyon
Zell Pond
Zero Butte
Zero Waterhole
Zig Zag Creek
Zigzag Canyon
Zink Spring
Zion Memorial Park Cemetery
Mount Zion
Zoar Cemetery
Zog Creek
Zollner Creek
Zosel Hill
ZX Ranch
ZX Ranch Grain Camp
Sevenmile Spring
Nonose Creek
East Frickey Spring
Condon Water Supply Pump
Blalock Flat
Sandon
Lost Gulch
Wyatt Gulch
Long Gulch
Rich Creek
Skin-it Gulch
Wyatt Reservoir
Steward Ditch
Crenshaw Gulch
Miller Creek
Glasgow Creek
Love Family Cemetery
Goose Creek Cemetery
Thorn Gulch
Taylor Ditch
Heater Creek
Welch Reservoir
Iron Gulch
Taylor Reservoir
Olsen Gulch
Harrison Gulch
Buckhorn Gulch
Moore Reservoir (historical)
Island City Cemetery
Fruita
Spring Creek
McDougal Creek
Copperfield - Homestead Cemetery
Blackhorse Recreation Site
Clay Spring
Camp Carson (historical)
Rainbow Reservoirs
Friday Creek
Starkey Cemetery
Prescott Ditch
Kelly Springs Creek
Marion (historical)
Draper Creek
Park (historical)
Ames Creek
Benson (historical)
Nibley (historical)
Bobington Branch
Millard Branch
Hulick Branch
Cove Hot Springs
Twin Spring
Roulet Pond
Minam Hill
Elk Flat
Elk Flat (historical)
Owenby Hill
Maxwell Lake
Colpitts Spring
Bartlett Bench
McNeils Spring
Grouse
Cummings Spring
Eden
West Fork McGraw Creek
Hidden Ridge
Joy (historical)
Waller Reservoir 3
Elmers Reservoir 1
Elmers Reservoir 2
Elmers Reservoir 3
Chico (historical)
Rocky Hollow
Davis Spring
Donnely Creek
Burton Canyon
Rock Creek
Grassy Dell Creek
Town Gulch
Fort Creek Reservoir
Fopiano Reservoir
Burnt Corral Springs
Devils Gulch
McCarty Creek
Gus Creek
Byron Ditch
Schoolhouse Hill
Hot Lake Reservoir
Hohstadt Reservoir
Lodgepole Spring
Horseshoe Spring
Lower Falls Little Minam River
Fool Hen Spring
Ames Spring
Coyote Spring
Burnt Spring
Jim Spring
O A Lake
Tenino Cemetery
Tumalo Cemetery
Merrell Reservoir
Hampton Creek
Gibson Creek
Ammons Reservoir
Bench Reservoir
Swale Reservoir
Question Reservoir
Corner Reservoir
Reservoir Number Six
Big Bend Island
Sand Creek
Roberts Bay
Roberts Cemetery
Weatherspoon Ditch
Lost Lake Reservoir
Fish Lake Branch
Steele Reservoir
Stein Basin
Norway Basin
West Fork Clear Creek
East Fork Clear Creek
Pole Creek
Hole in the Wall Gulch
Murray Gulch
Dry Gulch
Blue Gulch
Aitken (historical)
Johnston Spring
Deer Gulch
McMullen Ditch
Timber Canyon Spring
Crow Reservoir
Laird Reservoir
Brady Creek
Badland Creek
Wilkins Creek
Siegle Ditch
Dean Pass
Oregon Island
Ferry Canyon
Summit Spring
Double Spring (historical)
Cement Spring (historical)
Johnson Spring
Parsons Spring
Waller Reservoir 2
Waller Reservoir 6
Rock Spring
Ram Lake Waterhole
Mud Springs Creek
Diatomite Mine Headquarters
Peoples Irrigation Company Ditch
Lateral J
Terrebonne Cemetery
Lateral E
Reynolds Pond
Gray Reservoir
Independent Order of Odd Fellows Cemetery
Davidson Spring
Kelly Cemetery
Buether Reservoir
Gert Canyon
Pioneer Spring
Hot Springs Cemetery
Borstel Pond
Wilcox Cemetery
Wilson Reservoir Number Two
Spring Creek
Bakeoven Cemetery
Coleman Point
Frog Springs Canyon
Jersey Spring
Schoolie Pasture Ranger Station
Warm Springs
Lasen (historical)
Douglas (historical)
Irving Slough
Walterville Bridge
Easton Spring
Fort Dobie (historical)
Skinner (historical)
Watson (historical)
Three Springs (historical)
Annalore (historical)
English (historical)
Grandview (historical)
Pine Grove
Sanford Spring
Alder Brook
Saint Mary's Cemetery
Conway (historical)
Duckwall Reservoir
Ferguson Creek
Duck Pond Ridge
Rapid Creek
Rocky Canyon
Road Canyon
Guttery Spring
Johnson Spring
Koberg Beach
Koberg Slough
Koberg Beach State Park
Frankton Cemetery
McGuire Spring
Rowena Crest
Wetland Spring
Rincon Spring
Red Mountain Reservoir
Hardin (historical)
Skinners Bar
Q Street Canal
Milorn (historical)
Old Springfield IOOF Cemetery
Two Sisters Bar
Third Slough
Harrisburg Bend
Harpers Bend
Horseshoe Bar
Pondexter Creek
Riverview
Bells Shute Bar
Marshall Slough
Crow Creek
Spring Creek
Smith Spring
Dry Gulch
Mount Jefferson IOOF Cemetery
Shelly Creek
Rhoades Creek
Power Canal
Carlisle Spring
Lower Mud Spring
Nolin Cemetery
Slusher Canal
Milton Hill
Irrigon Junior - Senior High School
McNary Beach
Pioneer Memorial Cemetery
Saxe
Spring Creek
Green Meadows
Stewart Bench
McKay Dam
Campbell
Harris Junior Academy
Glendale
Badger Springs
Waterman Gulch
Swartz Spring
Love Loney Ditch
Tumia (historical)
Hyatt Cemetery
Bowlus Canyon
Government Mountain
Brookhouse
Freebridge
Despain Gulch Cemetery
Wells Spring Cemetery
Sand Hollow Cemetery
Butter Creek (historical)
Lake Pit
Sheepshead Canyon Creek
Hornbeck Spring
North Quail Creek Reservoir
Louies Draw Reservoir
North Quail Creek
Oriana Creek
Road Canyon Creek
Quail Creek Reservoir
Upper Paul Creek Spring
Roadside Reservoir
Sheep L Ditch
Potato Hill Reservoir
Sage Hen Hill
Indian Brave Reservoir
Road Lake
Highline Ditch
Feed Canal
Cote Slough
Egli Canyon
Foster Spring
Murphy Waterhole
Summit Spring
Connolly Basin Spring
Mountain Ash Springs
Step Spring
Cold Springs
Deadman Creek Reservoir Number Three
Deadman Creek Reservoir Number Two
Deadman Creek Reservoir Number One
Little Flat
Little Flat Reservoir
Post Camp Reservoir
Mustang Reservoir
Goose Reservoir
B V Reservoir
South Indian Reservoir
Sherwood Lake
Penn Slough
Easterday Ditch
Needham Reservoir
Stacey Ditch
Biggs Ditch
Boston Drain
Johnston Gulch Reservoir
Russell Drain
Robbins Drain
Purvis Drain
Meadow Flat
Government Spring
Deer Spring
Willow Creek Well
Smith Wells
McLean Well
Stockwater Ditch
Roaring Springs Creek
Indian Spring Creek
Fred Riddles Reservoir
Warm Springs Creek
Paris (historical)
Payette Junction
Weiser Junction
Mosquite (historical)
Oregon Slope
Coyote Drain
Annex
Bruce Reservoir
Petersons Ponds
Rills Pond
Valby Cemetery
Sinks (historical)
Emigrant (historical)
Port of Morrow Harbor
Boardman Marina Park
Messner Marsh
McCormack Slough
Jack Mountain
Sherars Falls
Catholic Cemetery
Smith Ponds
Tygh Valley Cemetery
Gurley Canyon
Liechti Pond Number Two
Ketchum Pond
Chenoweth Flat
Chenoweth
Dodd Ponds
Hat Rock Drain
Cold Springs Drain
L Canal
Stanfield Drain
Tigard Evangelical Cemetery
Hedges Creek
King City
Summer Creek
Heard Reservoir
Stark Reservoir
Johnston Creek
Messinger Creek
Hall Creek
Ball Creek
Rock Creek Corner
Cow Creek
Baumgardner Cemetery
U S B Line Canal
Robinson Reservoir
Darr Grave
Doherty Reservoir
Patterson Grave
Cutsforth Reservoir
Sourdough Creek
Turner Reservoir
Lorraine Creek
Morgan Creek
Brandy Creek
Ewing Ditch
Ewing (historical)
Fort Henrietta (historical)
Westland Dam
Echo Memorial Cemetery
I Canal
Wink Pond
Butter Creek Junction
Westland F Canal
Westland A Canal
Black Rim Reservoir
Lambing Creek
Mud Spring
Cold Spring Creek
Webb Canyon
Antelope Creek
Crippled Horse Spring
Bald Mountain
Suntex
Smoky Hollow Rim
Seep Spring
Sage Butte
Mahogany Mountain
Buckaroo Pass
Allendale (historical)
Sunset Beach
Lewis and Clark Cemetery
Laws Creek
Stavebolt Landing (historical)
Walford Johnson Creek
Johnson Creek
Brower Creek
Chadwell (historical)
Sister Green Mountain
Pearse Creek
Rock Creek
Rogers Park
O-A Hill
Vernonia Cemetery
Kale Creek
Hopkins (historical)
Such Joja Reservoir
McGuire Dam
Mountain House (historical)
Beltview Reservoir
Fairdale Mineral Spring
Dawson Spring
Turek Reservoir
Moores Valley Cemetery
Von Reservoir
McCall Spring
Murray Creek
Camp Kiwanilong
Battery Russell (historical)
Creep and Crawl Lake
Potato Lake
Beaver Lake
Adair Slough
Flavel (historical)
Brallier Swamp
Taylor Ditch
Lithgow Creek
Hammond Boat Basin
David Creek
Riverview Cemetery
Pioneer Cemetery
Trotter
Jeffers Garden
Stewart Creek
Mott Basin
Astoria Bridge
Clatsop Plains Cemetery
North Fork Abercrombie Creek
Abercrombie Creek
Skookum Creek
Mill Creek
Surf Pines
West Lake
Multnomah Park Cemetery
Sunnyside Cemetery
Cristilla Pioneer Cemetery
Clackamas Cemetery
Veterans Creek
Alder Creek
Dean Creek
Beebe Island
Eda Creek
Schaber Reservoir
Shipley Creek
Carter Creek
Falling Creek
Ivey Creek
Nyberg Creek
Kelly Creek
Mark Reservoir
Dewdrop Reservoir
Forest Creek
Jewell Reservoir
Halfway Reservoir
Red Hen Reservoir
Carry Reservoir
Lost Reservoir
Johnson Reservoir
South Fork Waterhole
Horseshoe Rim
Turpin Canyon
Smith Reservoir
Woodville Cemetery
Foots Cemetery
Lucy Gulch
Big Bend Park
Snabel Creek
Moon Mountain
Ram Lake South Waterhole
Central Oregon Academy (historical)
Kelly Spring
Plummer Slough
Oak Park (historical)
Herinckx Pond
Rays Lake
Cunningham Lake
Aarons Lake
Columbia Memorial Gardens Cemetery
Independent Order of Odd Fellows Cemetery
Lutheran Cemetery
Ruley (historical)
Heinen Pond
Deep Creek
James O Fisher Reservoir
Woods Pond
South Channel
Arata Creek
Osburn Creek
Stone Reservoir
Dewey (historical)
Graver Creek
Hills Cemetery
Laurelwood Reservoir
Spangler Pond
South Reservoir
Meyers Pond
Weaver Reservoir
Koehnke Reservoir
Cook Reservoir
Popp Reservoir
Ettinger Reservoir
Saint Matthews Cemetery
Lewis Cemetery
Burkhalter Reservoir
Wandell Reservoir
Lindow Reservoir
Ayers Creek
Davis Creek
Abbey Creek
Bethany Pioneer Cemetery
Phillips Cemetery
Ennis Creek
Doane Creek
Springville (historical)
Bannister Creek
Ward Creek
Commonwealth Lake
Somerset West
Plainview (historical)
Dinihanian Reservoir
Neveh Zedek Cemetery
Sunset Log Pond
Messinger Creek
Seward - Curks Cemetery
Dicks Pond
Mullerleile Pond
Helvetia Cemetery
Maple Lane
Henrici
Mompano Reservoir
Skyline Reservoirs
Singer Creek
Holcomb
Tour Creek
Charman Creek
Saint Paul Lutheran Cemetery
Maple Lane Cemetery
Middleton Cemetery
Loewen Reservoir
Loewen Creek
Mill Creek
Tualatin Reservoir
Richter Pond
Tapman Creek
Murrays Pond
Hessel Reservoir
Bull Frog Reservoir
South Fork Tickle Creek
Dolan Creek
Welling Reservoir
Lights (historical)
Mabery (historical)
Lusted Reservoir
Lusted Creek
Sester Reservoirs
Glendale Pond
North Fork Beaver Creek
Middle Fork Beaver Creek
South Fork Beaver Creek
Belchers Reservoir
Skunk Hollow
Kruse (historical)
Aurora Reservoirs
Randall Creek
May Creek
Swanson Reservoir
Colton Lutheran Cemetery
Karney Reservoir
Clarkes Pioneer Cemetery
Bonney Cemetery
Heller Reservoir
Hudleson Spring
Scott Creek
Yamhill Reservoir
Severt Creek
Sorosis Reservoir
Sunset Cemetery
Ryan Corner
Lone Pine Island
Hazeldell Orchards Reservoir
Rick Reservoir
Card Reservoir
Trial Reservoir
Norton Creek
June Reservoir
Cottonwood Spring
High Point
White Sage Well
Bobcat Creek
Willow Spring
Little Alvord Well
Andrews Cemetery
Sand Gap
Saddle Spring
Nansene
Dufur Ranger Station
Rice Cemetery
Seufert Dam
Petersburg Cemetery
McDonald Reservoir
Wassen Pond
Wasco Guard Station
Trugg Reservoir
Pullens Pond
Obrist Cemetery
Dorin Branch
Earnest Reservoir
Phillips Reservoir
Brainerd Cemetery
Arthur (historical)
Haldeman Pond
McQuinn Cemetery
Patterson Creek
Neil Creek
Harrie Creek
Kinder Cemetery
Masonic Cemetery
Shiloh Basin Cemetery
Goble Cemetery
Burnt Mountain
Spring Creek Camp
Leslie Gulch Camp
Dago Gulch
Blackjack Butte Reservoir
Red Basin
Dry Reservoir
Poison Spring Reservoir
Tims Creek
Gordon Creek
Cabin Springs
Rock Spring Creek
Owyhee Dam Park
Anderson Spring
Pine Hollow
Lauronzon Canyon
Dufur Orchards Reservoir
Dufur Ditch
Chase Reservoir
Starveout Creek
Rinehart Spring
Dry Creek Camp
Hammond Hill
Osborn Pond
Jones Pond
Rossner Reservoir
Sexton Reservoir
Holman (historical)
Fidler Springs
Higgins Creek
Wintel (historical)
Dencer (historical)
Eoff Reservoir
River Bend Reservoir Number Two
Spring Reservoir
Roby (historical)
Porter Slough
Houston Cemetery
Waverly Memorial Cemetery
Conser (historical)
Leander (historical)
Joe Crow Reservoir
Downing Pond
Woods Reservoir
Evers Lake
Connor Lake
Weston (historical)
Meadowbrook Lake
Stockhoff Reservoir
Stringer Reservoir
Warner Creek
Michael Reservoir
Stringer Pond
Burlington (historical)
Jacobs Bend
Johnston Slough
Halsey Pioneer Cemetery
Nixon (historical)
Young Cemetery
Bowen Reservoir
Dejong Reservoir
Muller Reservoir
Swearingen Reservoir
Amity Cemetery
Haven Hill Pond
Mochettaz Reservoir
Middle Fork Muddy Creek
East Fork Muddy Creek
Wiley Creek
Markee Reservoir
Martin Brothers Flashboard Reservoir
Bowles Reservoir
Solle Ponds
Stephens Reservoir
Pine Tree Corner
Janzen Reservoir
Hills Reservoir
Schindler Reservoir
Deep Lake
Ryan Lake
Canyon Creek
Sander Reservoir
Parks Lake Reservoir
East Independence (historical)
Smith Cemetery
Neahr (historical)
Calloway Reservoir
Flickinger Reservoir
Adair Village
Claxtar (historical)
Riverbed Pond
Brush College Creek
Lenhard Reservoir
Alsip Reservoir
Garber Reservoir
Fisher Reservoir
Gilliams (historical)
Lamer Pond
Pringle Spring
Zink Reservoir
Bronson Creek
Dundee Pioneer Cemetery
Krono (historical)
Scottys Pond
Permaneer Log Pond
Priceboro (historical)
Twin Buttes (historical)
Marx Reservoir
Eagle Crest Spring
Eagle Crest Reservoir
North Fork Wade Creek
Wade Creek
Estacada Lake
Slow Springs Reservoir
Spring Creek
Delshazer Spring
Riverside Lake
Bald Mountain
Salmon Creek
Orchard Dale (historical)
Heesacker Reservoir
Howell Reservoirs
Soda Springs (historical)
Carstens (historical)
Crawford (historical)
Hayward Cemetery
Bateman Reservoir
Rails End Reservoir
Sunago Reservoir
Dam Site Reservoir
Dixie (historical)
Bump Reservoir
Spaniol Reservoir
Meadow Brook
Horning Reservoir
Welches Pond
East Gumm Creek
Coal Creek
North Cemetery of Clear Creek
Pioneer Park
Fish Ponds
Wilark Pioneer Cemetery
Rainier Reservoir
Owl Creek
Oasis Creek
East Branch Fox Creek
Fern Hill
Girt Creek
Neer City (historical)
Prescott Cemetery
Welter Creek
Neer Creek
Goble Beach
Bear Creek Reservoir
Whitehorse Mountain
Givens Slough
Baker Creek
Loveland Creek
Gallagher Reservoir
Cedar Creek
Dunaway
Richland
Kingman Kolony
Yellowstone Waterhole
Shroder Waterhole
Tommy Dean Cemetery
Tuu-Tiipi Flat
Rock Creek
Spring Branch
Cold Spring
Hooker Reservoir
Bennett Spring
Saddle Butte Reservoir 2
East Cow Creek
Lower Batch Lake
Azcuenaga Meadows
Rock Dam
Black Canyon Creek
McCollum Reservoir
Magerly Reservoir
Spring Gulch
Del Rio Reservoir
Hays-Gall Cemetery
Blossom Creek
Rooster Gulch
McDonald Pond
Seclusia Reservoir
Glasser (historical)
Maddys Pond
Froman (historical)
Went (historical)
Linn (historical)
Thompson's Mills State Heritage Site
Pleasant Butte Baptist Cemetery
Schneider Log Pond
Asbahr
Orleans Cemetery
Fisher Island Pond
Chemawa Cemetery
North Reservoir
Fruitland Creek
Swegle
Yeoman (historical)
Lachmund (historical)
Gesner (historical)
Rickey
Mack Reservoir
Secluded Lake Reservoir
Antioch Cemetery
Despain Reservoir
Bingham Reservoir
Buckskin Mountain
Crickett Creek
Denio Cemetery
Moores Hollow Reservoir
Nyssa Heights
White Settlement
Keanes Creek
Bonnie Brook
Crampton Reservoir
Crusher Creek
Rainbow Creek
Schaad Reservoir
Denison Reservoir
Handy (historical)
Fowler Reservoir
Hubbard Cemetery
Bronec Reservoir
Alkali Reservoir
Dead Horse Reservoir
Michigan (historical)
Day (historical)
Buckley (historical)
Coleman (historical)
Monumental Rock
West Fork Butte Creek
East Fork Kane Creek
China Gulch
Gregory Reservoir
Albright Gulch
Big Gulch
Cold Spring
Spring Canyon
Starvout Creek Mines
Hobbsford (historical)
Mud Springs
Onion Springs
Pease Spring
Nichols Cemetery
Eagle Point Meadows
Barton Reservoir
Eagle Point National Cemetery
Harper Reservoir
Hoover Reservoirs
Whetstone Pond
Swaggerty Reservoir
Rexrood Springs
Meadow Graves
Coulter Reservoir Number One
Simpson Reservoir
Coulter Reservoir Number Two
Straus Spring
Kirkham Reservoir
Price Reservoir
Gribble Reservoir
Eightmile Cemetery
Croy (historical)
Negro Ridge
Negro Hollow
Brown Cemetery
Condon Reservoir
Waldo Lake
Barclay (historical)
McBee Family Cemetery
Ale (historical)
Schumacher Reservoir
Saint Marys Cemetery
Walker Creek
Highberger Ditch
Young Lake
Mater Dolorosa Cemetery
Leffler (historical)
Kreilich Reservoir
Dozler Reservoir
Lackner Pond
Teal Spring
Glaze Creek
Jahn Reservoir
Schmid Reservoir
Selah (historical)
Campbell Reservoir
Kuenzi Reservoir
Barnes Brothers Reservoir
Quigley Reservoir
Valley View Reservoir
Willard (historical)
Grier Reservoir
Eliander Reservoir
Halstead Reservoir
Schierling Reservoir
Branson Reservoir
Winkle Family Cemetery
Irwin Family Cemetery
Hewitt Spring
Reeves Cemetery
Bishop Ditch
Sheephead Mountain
Big Elbow
Burnt Elbow
Sheephead Reservoir
Coyote Reservoir
Bar Cross Basin Reservoir
Acton Butte
Jimmy Spring Reservoir
Aspen Spring
Strode Ditch
Rock Creek
McKenzie-Greeley Ditch
Runaway Hill
Painted Canyon Reservoir
Arritola Ditch
Arock Cemetery
Nouque Ditch
South Fork Ryegrass Creek
Cone Ridge
Crutcher Ditch
Anderson Ditch
Tudor Ditch
Kanehinke Ditch
West Grassy Reservoir
Three Forks Rim
Urlezaga Ditch
Sharp Ditch
South Antelope Canal
North Antelope Canal
Hiebenthal Reservoir
Saint Paul Cemetery
Case Creek Reservoir
Spada Reservoir
Labish Center
Fitzpatrick Creek
Skunkville Cemetery
Skunkville
Belle Passi (historical)
Drescher Ditch
McLaughlin Pond
Townsend (historical)
McKee
Zach Reservoir
Dominic (historical)
Mount Angel Pioneer Cemetery
Bernice (historical)
Mount Angel Abbey Cemetery
Benedictine Sisters of Mount Angel Cemetery
Silverton Cemetery
Aarhus Reservoir
Saint Paul Catholic Cemetery
Holden Reservoir
Bethany
Hooter Creek
Hillside Reservoir
Big Rock Lake
Cedar Grove Lake
Barlow Flats
Irvin Family Cemetery
Bachert Creek
Netter Creek
Gribble Cemetery
Gut Creek
Gleason Cemetery
Blosser Cemetery
Zion Mennonite Cemetery
Wheeler Creek
Kyllo Reservoir
Smyrna Cemetery
Hamricks Corner
Yew Creek
Wills Creek
Murry Creek
Bremer Reservoir
Schneider Reservoir
Dove Creek
Monte Cristo (historical)
Drescher Reservoir
Dobbes Lake
Spring Reservoir
Loes Reservoirs
Hermans
Russellville
Little Teasel Creek
Beyer Reservoir
Minto Creek
Anderson Creek
Roland Creek
Chamberlain Creek
Bear Creek
Homestead Creek
Deardorf Ponds
Burnt Mountain
Marion Butte
Pilot Rock
Fall Creek
Clark Brook
Wendy Creek
Wade Creek
Drake Creek
Butte Lakes
Fibre Rock
South Fork Butte Creek
Hell Cat Rock
Rhody Lake
Fibre Creek
Rhody Creek
Copper Lake
South Gawley Ridge
Boar Camp
Dog Rock
Slide Creek
Trestle Creek
Mud Springs
Shoofly Creek
Escobar Cemetery
Saint Joseph Cemetery
Butler Creek Reservoir
Binford Reservoir
Butler Creek
Damascus Pioneer Cemetery
Burghardts Mill
Logan Pleasant View Cemetery
North Logan (historical)
Briscoe Reservoir
Martin Creek
Firgrove
Viola Douglass Denning Grave
Redland Pioneer Cemetery
Sprague Cemetery
Moehnke Cemetery
Fellows Cemetery
Isaackson Reservoir
Kromer Reservoir
Sandy Ridge Cemetery
Burglund Pond
Deep Creek Reservoir
Saling Creek
South Fork Wade Creek
Independent Order of Odd Fellows Cemetery
Inventory Creek
Gawley Meadow
North Gawley Ridge
Cow Creek
Picture Point
Fill Creek
Camp Creek
Murphy Camp
Pelkey Lake
McCredie Hot Springs
Beaver Creek
Hyland (historical)
Hughs Creek
Mystery Hills Reservoir
Calvins Pond
Berthelson Pond
Little Reservoir
Clarks Pond
Taylor Reservoir
Kirkpatrick Reservoir
Kotan Cemetery
Noble Spring
Bickmore Creek
Marcola Cemetery
Polly Creek
Rock Creek
Upper Mabel Cemetery
Bette Creek
Ethel Creek
Dorothy Creek
Carolyn Creek
Bolly (historical)
Log Creek
Crooked Creek
Dexter Creek
Baker Creek
Dinner Creek
Baker Bay
Hamblen Creek
Sellers Cemetery
Pleasant Hill Cemetery
Mulholland Cemetery
Unity
Jacoby Mountain
Green Reservoir
Sweeney Creek
Crawfordsville Union Cemetery
Brownsville Dam
Brownsville Pioneer Cemetery
Kearns Reservoir
Claypool Cemetery
Durlam Reservoir
Sawyer Creek
Ernests Pond
Roaring Creek
Rickmans Pond
Gabriel Creek
Little Creek
Bigbee Creek
Liberty
Hills Pond
Noble Creek
Nye (historical)
Sodaville Springs Park
Fairview
Smith Reservoir
Smith Dam
Bobby Creek
Payne Creek
Union - Turnbow - Mays Cemetery
Franklin Grange Cemetery
McLaden Creek
Blacktail Creek
Barrett Spring
Burp Hollow
Estrup (historical)
Dusky Creek
Goldson Cemetery
Neil Lake
Hendricks Branch
Liles Cemetery
Signal Island
Fern Ridge Dam
Jetson (historical)
West Fork Coyote Creek
Job Swale Creek
Middle Fork Coyote Creek
Griffith Reservoir
Davis Reservoir
Warren Slough
Sweet Creek
Nestucca Valley Community Cemetery
Tooze Creek
Remington (historical)
Rebart Reservoir
Hopewell Cemetery
Tangen Reservoir
Clark Reservoir
Crabapple Creek
Orchid Camp
Foley Hot Springs
Castle Creek
Lookout Creek
Basalt Creek
Horn Creek
Yankee Creek
Pothole Meadow
Dry Creek
Saddle Creek
Belknap Hot Spring
Blue Canyon
Kester Pond
Johnson Reservoir
Emory Moore Reservoir
Bounds Creek
Watson Creek
Jones Creek
Pedee Cemetery
Writsman Brook
Mud Creek
Fields Reservoirs
Round Mountain
Tennys Creek
Ninemeyer Spring
Tudor Warm Springs
Sweet Reservoir
Green Creek
Jones Creek
Evans Creek
Hale (historical)
Mill Valley Creek
Gold Run Creek
Wilson Creek
Little Hahnee Reservoir
Parker Creek
Vaughn Station
Parsley Creek
Langworthy Creek
Cram Creek
Spring Creek
Stephens S S Heirs Cemetery
Spring Creek
Village Creek Spring
Village Creek
Lower Hult Reservoir
Owl Creek
South Fork Ferguson Creek
Glenbrook Log Pond
Weaver Creek
Hull-Oakes Log Pond
Rambo Reservoir
Howell Creek
Cedar Swamp
Alsea Falls Recreation Site
Alsea Falls
Marsh Creek Pond
Scare Ridge Lookout
Pearl Lake
Twin Sisters Creek Camp (historical)
Jeff Creek
Coldwater Creek
Sweden Creek
Russell Creek
Herb Creek
Burn Creek
Yellow Lookout
Yellow Point
Lower Johnson Creek
Scare Ridge
Whittaker Creek Recreational Reservoir
Clay Creek Recreational Reservoir
Clay Creek Recreation Site
Hell Hollow
Farman Flat
Larue Creek
Cox Creek
Siuslaw Guard Station
Joler (historical)
Cougar Gulch
Haight Creek Picnic Area
Chickahominy Cemetery
Blachly Cemetery
Nelson Mountain
Spring Canyon Creek
Potato Patch Creek
Conrad Creek
Walton Guard Station
North Fork Cook Creek
Slipout Creek
Trapper Creek
Roberts Creek
Marten Rapids
Granite Creek
Miller Creek
Goose Creek
Montgomery Creek
Ward Creek
Wallace Creek
O'Brien Creek
Haagen Creek
Forest Creek
Alder Creek
Pernot Meadow
Doris Creek
Fern Creek
Clapper Creek
Saddle Dam
Scout Creek
H J Morton County Park
Sparks Creek
Strube Dam
Alder Creek
John Griffith Reservoir
Little Lake Spring
Triangle Lake
Bear Ridge
North Fork Fish Creek
Lake Creek Recreation Area
Lamb Creek
WOW Log Pond
Alexander Creek
Adams Creek
Olalla Reservoir City Park
Olalla Reservoir
Spencer Creek
Pioneer Mountain
Cattail Slough
Jack Creek
Chitwood Cemetery
Spring Brook
Toledo Cemetery
Sandy Creek
Crow Creek
Lorane Grange Cemetery
Pass Creek State Wayside (historical)
Kingman
Gun Creek
Cedar Flat
Summons (historical)
Yarnell (historical)
Taylor Creek
Browns Reservoir
Walker Reservoir
Renound Reservoir
Sharon Creek
Pilkens reservoir
Willamette Log Pond
Tollgate Reservoir
Peck Creek
Lewis Cemetery
Hughes Creek
Little Bottom Creek
Gates Cemetery
Jenkins Cemetery
Carrol Reservoir
Nighswander Creek
Hayes Branch
Powell Branch
Beaver Creek
Health Spring Branch
Smith Reservoir
Gates Creek
Hadleyville
Spring Creek
Gunter Recreation Site
Watering Trough Creek
Wolf Creek
Russell Creek
Gardner Creek
Lake Louise
Little Siuslaw Creek
Simpson Creek
Siuslaw Falls County Park
Shitten Creek
Jeans Creek
Doe Hollow Creek
Holland Creek
Swing Log Creek
Deer Creek
Cabin Creek
Fish Creek
Mound (historical)
Timber Ridge
Beaver Creek
Lewis Creek
Tunnel Creek
Panther (historical)
Wolf Point
Arell (historical)
Harris Creek
Kopplein Creek
Burchard Creek
Shingle Creek
Happy Hollow Creek
Ellmaker State Wayside
Rudder Creek
Spring Creek
Perry Creek
Whiskey Creek
Miller Creek
Bradish Lake
Peterson Creek
Little Wolf Creek
Coyote Creek
Cougar Creek
Beaver Dam Creek
Harlan Cemetery
Strout Spring
Sailor Pioneer - Noti Cemetery
Sackos Pond
Mount Carmel (historical)
Anthony Gorge
Catherine Creek Highline Canal
Thompson Spring
Kaylor Spring
Scott Ditch
Pond Slough
Grout Ditch
Parker Springs
Steiger Spring
Groover Spring
Boyce spring
Bacher Creek Reservoir
Bacher Spring
Deafy Creek
Billy Gulch
Ryan Gulch
Slaughterhouse Spring
Nagle (historical)
Blakes Junction (historical)
Farewell Bend (historical)
McBride Reservoir
McBride Ditch
Dry Gulch
Schuck Waterhole
Powell Creek Reservoir
Big Springs Creek
Conner Creek (historical)
Bear Creek
Tekpé Gulch
Timber Canyon Waterhole
Lady Frances Mine
Perry Creek
Stearns Ditch
Baldwin Dam
Dry Creek Reservoirs
Hoffman Ditch
Chimney Rock Campground
Eddyville Cemetery
South Fork Spencer Creek
Truman Creek
Rebel Creek
Moxley Cemetery
Goshen Grange 561 Cemetery
Stalder Slough
Scott Creek
Pembrook Reservoir
North Fork Hill Creek
Woodards Dam (historical)
Hawley Cemetery
Shields Cemetery
Fir Grove Cemetery
Mc Farland Cemetery
Turkey Run
Waterhouse Slough
Brown Creek
Snow Slough
Louis Slough
Nossaman Reservoir
Finney Creek
Kimwood
Fishbird Lake Reservoir
Taylor Creek
South Fork Gettings Creek
Silk Creek Cemetery
Fox Hollow (historical)
Siuslaw (historical)
Spencer Creek
Independent Order of Good Templars Cemetery
Willow Lake
Cabin Spring
Juniper Flat
Powell Reservoir
Boardman (historical)
Rose Hill
Humphreys Pasture
Black Canyon
Sage Plains
Dead Horse Lake Recreation Site
Soda Mine
Dukes Canyon Creek
Cheney Slough
Stephens Spring
Sixteen Mile Spring
Middle Pittsburg Rapids
Waller Reservoir Number One
Waller Reservoir 4
La Grande Aqueduct
Mammouth Spring
Silver Spring
Lookout Spring
Mud Spring
Barnes Spring
Hotchkiss Springs
Wilson Ditch
White Rock Reservoirs
Rehart-Salt Creek Ditch
Wilcox Ditch
Lower Reservoir
Upper Reservoir
Whitaker (historical)
Moss Flat Spring
Curtis Ditch
O V L Ditch
Reynolds Reservoir
High Line Ditch
Coyote Flat Reservoir
Woodchopper Spring
Angel Peak Mine
Angel Peak
Hidden Springs
Old Stage Station (historical)
Rosalite Mine
Collins Reservoir
Caleb (historical)
Wheeler Creek
North Fork Willow Creek
Sixshooter Creek
Low Gilchrist Spring
Straube Creek
Blann Creek
McKay Creek
Jerrys Draw
Jerrys Ridge
Burgen Creek
Wildwood Creek
Jordan Valley
Blue Creek
Humphrey Cemetery
John Shelton Cemetery
Our Lady of Lourdes Catholic Cemetery
Bear Creek
Bradshaw Creek
Jenkins Spring
Eddy (historical)
Polk County Fairgrounds
Paul Washington Indian Cemetery
Noti Creek Reservoir
Spring Creek
Jones - Kime - Brown Property Cemetery
Anidem (historical)
West Fork Quartzville Creek
Thomas Fork
DeFord Creek
South Roaring River
Milky Fork
Craft Creek
Sink School (historical)
South Green Mountain
Chimney Rock
Devils Canyon
Powder House Cove
Mitchell Guard Station (historical)
Seward Post Office (historical)
Bridge Creek (historical)
Emigrant Springs
Igo (historical)
Freezeout Canyon
Tompkins Butte
Stuckey Butte Reservoir
Cableville (historical)
Con Drum Reservoir
Drum Reservoir
Mule Spring Reservoir
Hole Waterhole
Mule Waterhole
Lake Bed Waterhole
North Desert Waterhole Number Thirty-Two
Con Reservoir
Speck Waterhole
Flyspeck Waterhole
Bed Rock Waterhole
North Desert Waterhole Number Nineteen
Mulehole Waterhole
Dooley Bedground Reservoir
Orejana Waterhole
Orejana Basin Waterhole
Lost Creek Reservoir
Bacon Camp Waterhole
Bacon Camp Lake Waterhole
West Bacon Waterhole
Kit Canyon Waterhole
Mule Spring Road Waterhole
Lakehole in the Ground Waterhole
West Draw Waterhole
Peters Waterhole
State Game Reservoir Number Eleven
Common Bedground Waterhole
Egan Cabin Waterhole
Lower Bedground Waterhole
Lynch Gulch Waterhole
Elmers Waterhole
Good Seep Waterhole
Fang Spring
Wickiup Reservoir
Abert Spring
Lone Reservoir
Abert Rim Viewpoint
Priday Ditch
Fitzgerald Ditches
North Coyote Hills Reservoir
Allen Ditch
Oregon Spring
Forward Spring
Upper Juniper Reservoir
Juniper Reservoir
Spring Reservoir
General Reservoir
South Fork Snyder Creek
Sheep Creek Spring
Juniper Waterhole
Spawn Reservoir
Boy Lake Waterhole
Feather Bed Lake Waterhole
Soup Lake Waterhole
Little Soup Lake Waterhole
Hard Pan Reservoir
Skookum Lake Waterhole
Ramsey Springs (historical)
Lost Forest Research Natural Area
Pilot Lake Reservoir
Depression Sump
Little Reservoir Number One
Little Reservoir Number Five
Little Reservoir Number Six
Lost Valley Creek
Wilson Creek
Wagoner Airport
Walker Airport
Wallace Airstrip (historical)
Wasco State Airport
Waynes Air Service Airport (historical)
West Buttercreek Airport
Westlog Airstrip (historical)
Whitehorse Ranch Airport
Willamette Center Heliport
Willamette Falls Community Hospital Heliport
Winn Airport
Woodland Park Hospital Helipad
Wooldridge Agstrip Airport
Workman Airpark
Wrights Airfield (historical)
KAGO - FM
KBKN-FM
KRSB-FM
KRVM-FM
KRWQ-FM
KSHR-FM
KSLC-FM
KSND-FM
KSOR-FM
KSOR-FM
KTJA-FM
KUGN-FM
KUMA - FM
KUPL-FM
KXLF-FM
KZEL-FM
KATU-TV
KECH-TV
KGW-TV
KMTR-TV
KOAC-TV
KOBI-TV
KOIN-TV
KPIC-TV
KPTX-TV
KCEL-FM
KCGB-FM
KCHC-FM
KCNR-FM
KEJO-FM
KFMT - FM
KGNW - FM
KGON-FM
KHPE-FM
KINK-FM
KIQY-FM
KJIB-FM
KLAD - FM
KLCC - FM
KMJK-FM
KNPT-FM
KNTL-FM
KOAP-FM
KOHU-FM
KPDQ-FM
KQFM-FM
KRBM-FM
KRKT-FM
KRNN-FM
Lassie Waterhole
Sidewinder Waterhole
Boulder Waterhole
Dudeck Ridge
Canterbury Reservoir
Sunstone Mine
Mine Draw Spring
Big Rock Reservoir
Miners Draw Waterhole
North Barry Reservoir
East Barry Reservoir
L J H Reservoir
Warner Lake (historical)
Six Pack Reservoir Number Four
Expand Reservoir Number Thirty
Crump Ditch
Squaw Creek
Bug Waterhole
Parker Ditch
Succor Creek Siphon
North Alkali Creek Siphon
The Tongue
Coyote Gulch Siphon
Snively Siphon
Owyhee Siphon
Black Willow Siphon
Silver Lake Cemetery
Crested Reservoir
KORE-AM
KPNW-AM
KQEN-AM
KRCO-AM
KRDR-AM
KRKT - AM
KSHR-AM
KTDO-AM
KTIX-AM
KUPL-AM
KVAS-AM
KWRC-AM
KFLS - AM
KFLY-AM
KGAL - AM
KHSN-AM
KIHR-AM
KLIQ-AM
KLWJ-AM
KNND-AM
KOHI-AM
KSYS-TV
KTVR-TV
KVAL-TV
KVDO-TV
KACI - AM
KBOY-AM
KCNR-AM
KEED-AM
KEX-AM
KFIR-AM
KYES-AM
Wiley's Seaplane Port
Willamette River Airstrip (historical)
Hanna Industries Airstrip (historical)
Hessel Tractor Airstrip (historical)
Hoffman Airstrip (historical)
Portland Auto Port Airstrip (historical)
Station L Airstrip (historical)
Town Concrete Pipe Airstrip (historical)
Portland General Electric Service Center Heliport
Twelve Mile Dam
Twelve Mile Reservoir
Maher Dam
Fred Riddles Dam
Jacksonville Dam
Jacksonville Reservoir
Higgins Dam
F M Crow Dam
Oron Thompson Dam
Oron Thompson Reservoir
Poplar Springs Dam
Poplar Springs Reservoir
Butte Reservoir
Butte Dam
Licklider Dam
Cottage Grove Dam
Fall Creek Dam
Anderson Dam
Beers Dam
McDade Reservoir
Van Derveer Dam
Parker Reservoir
G A Parker Dam
Arritola Dam
Riley Dam
Sitz Dam
Forcia and Larsen Dam
Forcia and Larsen Reservoir
Robinson Dam
Benson Dam
Salt Lick Dam
Deary Dam
Warm Springs Dam
Box Springs Dam
Shumway Dam
Greeley Reservoir Dam
Sommerville Dam
Little Grassy Reservoir
Clark Dam Number 1
Clark Dam Number 2
Oriana Dam
Weed Lake Dam
Becker Dam
Smith Dam
Beede South Dam
Beede North Dam
Stimmel Dam
Mills Dam Number 2
Mills Dam Number 1
Mills Dam Number 3
Veterans Dam
Van Raden Dam
Spalding Dam
Nick Barry Dam
Twelvemile Dam
Twelvemile Reservoir
Pole Creek Dam
Love Dam
Haskins Creek Dam
A E Brown Dam
Holbrook Dam
Sugarloaf Dam
Clear Creek Dam
Pine Creek Dam
Pine Creek Reservoir
Skull Creek Dam
Youngs Bay Lumber Company Dam
Youngs Bay Lumber Company Pond
Rock Creek Dam
Lillard Dam
Lillard Reservoir
J Reservoir
K Reservoir
L Reservoir
N Reservoir
O Reservoir
P Reservoir
Q Reservoir
S Reservoir
R Reservoir
T Reservoir
Ant Waterhole
Bug Waterhole
Cow Waterhole
Pierce Waterhole
Sheep Waterhole
Truscot Waterhole
Wendt Reservoir
Hindman (historical)
Norton (historical)
Virtue Hills
Van Patten Lake Dam
Echo Lake Dam
Traverse Lake Dam
Christmas Valley Airport
Rock Lake Dam
Antelope Dam
Lapham Dam
Lloyd Gift Dam
David Kent Dam
John McFall Dam
John McFall Reservoir
Worlow Dam
McCoy Dam
McCoy Reservoir
Rink Creek Dam
Johnson Log Storage and Storing Reservoir
Johnson Log Storage and Sorting Dam
Middle Lake Dam
Wickiup Lake Dam
Lost Lake Dam
Strong Dam
Threemile Dam
H L Dam
H L Reservoir
Willamette National Lumber Company Dam
Willamette National Lumber Company Reservoir
Chehalem Airpark
Clackamas County Redsoils Heliport
Clackamas Heights Airstrip (historical)
Astoria Regional Airport
Cline Falls Air Park
Compressor Station Number 10 Airstrip (historical)
Compressor Station 14 Airstrip (historical)
Condon State Pauling Field
Corvallis Municipal Airport
Country Squire Airpark
Crow-Mag Airport
Crowley Ranch Airstrip
Daniels Field LLC Airport
Davis Airstrip (historical)
Davis Airport Terminal
Hamel Reservoir Number 2 (historical)
Hamel Dam Number 2 (historical)
Woolfolk Dam
Skou Reservoir
Skou Dam
Nelson Dam
Stanley Dam
Corder Log Pond Dike
Corder Log Pond
Engler Huson Dike
Big Adobe Dam
Fort Rock Elementary School (historical)
Grade (historical)
Anderson Airfield (historical)
Amart Farms Airstrip (historical)
Alkali Lake State Airport
Albany Municipal Airport
Ajax Airport
Arlington Municipal Airport
Arnold Airstrip
Aurora State Airport
Ayres Airstrip (historical)
B F Goodlife Airstrip (historical)
Bandon State Airport
Barrett Field Airport (historical)
Barton Lake Ranch Airport
Beagle Sky Ranch Airport
Bend Municipal Airport
Big Sky Ranch Airstrip (historical)
Boardman Airport
Bohemia Incorporated Airfield (historical)
Boulder Park Resort Airstrip (historical)
Brothers Landing Strip (historical)
Burns Municipal Airport
Burrill Airport
Calvert Peak Airport
Fly 'N' W Airport
Alkali Spring
Mud Springs
Hereford Ditch
Cleary Ditch
Camp Creek Ditch
Mud Creek
Lander (historical)
True Blue Reservoir
Brattan Spring
Minersville (historical)
Miles Pond
Salisbury Marsh
Denny (historical)
Lockhart (historical)
Thompson (historical)
South Baker (historical)
Bowen (historical)
Bennehoff Reservoir
S V Reservoir
Moore Pratt Ditch
Pietrock Cemetery
Mulkey Creek
King (historical)
Hullt (historical)
Lower North Falls
Jeff Creek
Fox Reservoir
Koehler Reservoir
Pichette Reservoir
Willards Pool
Hammond Creek
Meyers Butte
Looney Creek
South Fork Cedar Creek
Middle Fork Cedar Creek
North Fork Cedar Creek
Priest Creek
Cedar Creek
Butte Creek Falls
Johnson Creek
Bucket Creek
Trinity Falls Creek
Abiqua Lake
Lower Shellburg Falls
Ayers Creek Falls
Stout Creek Falls
Noroma Creek
Walker Creek
South Forks Falls Creek
Cow Creek
Bodeen Lake
Bodeen Dam
Turner Creek Reservoir
Turner Creek Dam
Peter Dinsdale Dam
City of Portland Reservoir Number 1
City of Portland Reservoir Number 3
City of Portland Reservoir Number 4
City of Portland Reservoir Number 5
City of Portland Reservoir Number 6
Sester Reservoir Number 1
Sester Dam Number 1
Rohde Dam
Pearson Reservoir
Pearson Dam
Milwaukie Plywoood Corporation Dam
Milwaulie Plywood Corporation Log Pond
Pierson Dam
Bauer Dam
Bauer Reservoir
Kay Dam
Hollis Hartwick Dam
Walker Dam
Toney Reservoir
Inman Reservoir
Pearson Ditch
Travillion-Koester ditch
Spring Creek
Lynch Spring
Prescott Creek
Happy Spring
Universal Spring
Argenti Spring
Bazine Spring
Medical Hot Spring
Sunset (historical)
Little Park Creek
Robertson Ditch
Wright Ditch
Harmon Reservoir
Sagebrush Flat
Pondosa Pond
A Reservoir
F Reservoir
G Reservoir
Randall Dam Number 3
Randall Reservoir Number 3
Buck Butte Dam
Buck Butte Reservoir
White Rock Dam
Big Swamp Dam
Ana River Dam
Anderson-Rose Pool
Anderson-Rose Diversion Dam
Lost River Diversion Dam
Lost River Pool
Malone Pool
Round Valley Dam
Upper Midway Dam
Dog Hollow Dam
Silverfalls Timber Company Dam
Dober Dam
Ettinger Dam
Reservoir Number Two
Dam Number 2
Faraday Lake Dam
Lake Oswego Dam
Hickory Hill Farm Dam
Cole and Forrester Dam
Kuehne Dam
Walker Dam
Teasel Creek Dam
Lillie Walker Irrigation Pond Dam
Lillie Walker Irrigation Pond
Bailey Reservoir
Bailey Dam
Howard Schmidt Reservoir
Howard Schmidt Dam
Neil Beyer Dam
Stringer Dam
Unger Dam
Spada Dam
River Mill Reservoir
North Fork Dam
Trail Bridge Dam
Spring Lake Dam
Whispering Winds Dam
Funrue Reservoir
Funrue Dam
P M Delaubenfelds Reservoir
P M Delaubenfelds Dam
Wendell Kreder Reservoir
Big Creek Dam Number 2
Ollala Dam
Mission Creek Dam
Grabhorn's Airport
Green Acres Air Park
Grells Airport (historical)
Lafferty Field
Langmack Field (historical)
Lebanon Hospital Heliport
Lebanon State Airport
Lenhardt Airpark
Lexington Airport
Lone Oaks Ranch Airport
Long Ranch Airport
Mahlon Sweet Field
Malin Airport
Mason Airstrip (historical)
Mazama Timber Pad
McDermitt State Airport
McGill Airstrip (historical)
McKenzie Bridge State Airport
McNary Field
Rogue Valley International - Medford Airport
Legacy Meridian Park Hospital Heliport
Merle West Medical Center Helipad
Meyer Riverside Airpark
Mill Creek Field (historical)
Miller Airstrip
Miller Memorial Airpark
Millican Airstrip (historical)
Minam Lodge Airport
Morlan Airfield (historical)
Mountain View Air Park (historical)
Muddy Creek Airport
Mulino State Airport
Nehalem Bay State Airport
Nielsen Airport
Western Helicopter Services Airport
Hatch Airport
Hemmingson Airport
Hermiston Municipal Airport
Hines Airstrip (historical)
Hobby Field
Holiday Airport (historical)
Hollin Airport
Ken Jernstedt Airfield
Skydive Oregon Airport
Independence State Airport
Jensens Strip
Johnson Airstrip (historical)
Juniper Air Park
Juntura Airport
Karpens Airport
King's Airport
Crater Lake-Klamath Regional Airport
Kinzua Airport
Knox's Private Airstrip (historical)
Norway Airstrip (historical)
Oak Hill Airstrip (historical)
Olinger Airpark
Ontario Municipal Airport
Oregon City Airpark (historical)
Oregon Sky Ranch Airport
Owyhee Reservoir State Airport
Oxbow Airport
Pacific Communities Hospital Heliport
Harvey's Acres Airport
Pendleton Community Hospital Helipad (historical)
Eastern Oregon Regional Airport at Pendleton
Pinehurst State Airport
Pioneer Villa Airstrip (historical)
Poehler Airport (historical)
Pointers Airport
Port Arbour Seaplane Base (historical)
Portland Adventist Medical Center Heliport
Portland International Airport
Portland-Troutdale Airport
Prineville Airport
Propst Airport (historical)
Providence Hospital Heliport
Pugh Landing Strip (historical)
Putnams Airfield (historical)
Reds Wallowa Horse Ranch Airport
Reed Airstrip (historical)
Roaring Springs Ranch Airport
Rogue Valley Memorial Hospital Heliport
Shady Cove Airpark
Rome State Airport
Roppair Airport
Roseburg Lumber Company Airstrip (historical)
Roseburg Regional Airport
Rowena Dell Airstrip (historical)
S and E Farms Independence Airstrip (historical)
Sacred Heart Medical Center Heliport
Santiam Junction State Airport
Santiam Memorial Hospital Helipad
Scappoose Airport
Seaside Municipal Airport
Beaver Oaks Airport
Siletz Airport
Siletz Bay State Airport
Silverton Airfield (historical)
Simtag Farms Airstrip (historical)
Skyhill Airport
Snyder Ranch Airport
Spray Airstrip (historical)
Springbrook Airport
Springfield Airport (historical)
Providence Saint Vincent Hospital Heliport
Stark's Twin Oaks Airpark
Sutherlin Municipal Airport (historical)
The Green Trees Ranch Airport
The Pinnacle Ranch Airstrip (historical)
Top Line Helipad
Myrtle Creek Municipal Airport
Happy Valley Airport (historical)
Trojan Airstrip (historical)
Oregon Health Sciences University Heliport
Umpleby Ranch Airstrip (historical)
United Telephone System Airstrip (historical)
Venell Airport
Vernonia Municipal Airport
Vey Sheep Ranch Airport
Vons Airstrip (historical)
Wager Airstrip (historical)
Davis Airstrip (historical)
Decker Ranch Airstrip (historical)
Dietz Airpark
Drews Airstrip (historical)
Eagle Nest Ranch Airport
Elkton Airfield (historical)
Legacy Emanuel Hospital Heliport 1
Valley View Airport
Fairways Airport
Fargher Airfield (historical)
Lusardi Field
Flamingo Motel Heliport
Flying K Bar J Ranch Airport
Flying M Airport
George Felt Airport
George Wilson Ranch Airstrip (historical)
Gilmour Ag Air
Horseshoe Bend Spring
Harris Reservoir
Red Willow Spring
County Line Reservoir
Tunnel Reservoir
Boney Basin Reservoir
Currey Canyon Reservoir
Juntura Investment Company Canal
Joyce Reservoir
Dugout Reservoir
Grasshopper Flat Spring
Juniper Tree Reservoir
Forest Reservoir
Poverty Spring
Fan Spring
Baker Spring
Rodeo Spring
T J Spring
Beulah Creek Reservoir
Munkers Spring
Beulah Creek
Calf Creek Waterhole
Boulder Spring
Boulder Spring Number 2
Poverty Flat Spring
Rattlesnake Spring
Charcoal Spring
Dry Lake
Green Spot Spring
Fox Spring
Morrison Spring
Big Flat
Rimrock Spring
Peavine Reservoir
Trail Creek Spring
Hub Spring
Pole Reservoir
Muir Spring
Buck Spring
Big Flat Reservoir
Red Canyon Reservoir
Corral Reservoir
Big Flat Spring
Jones Reservoir
Jonesboro Canal
Zimmerman Ditch
Burnt Willow Spring
Rock Spring
Brown Reservoir
Tunnel Spring
Tumbleweed Spring
High Point
Bully (historical)
Washington Creek
Jim Ewing Creek
Hart Creek
Burnt Willow Creek
Gap Spring
Harper Springs
Wiser Creek
Corbett Creek
Harper Southside Canal
Hollow Reservoir
Horse Trail Reservoir
Sheep Trough Spring
David Kent Reservoir
Dry Canyon
Visher Feed Canal
Cables Ditch
Fister Ditch
Round Mountain Reservoir
Saddle Draw
Slide Ditch
A Drain
Halliday Drain
Blanton Drain
Butte Drain
Willow Reservoir
Henry Gulch Spring
Indian Spring
Pine Tree Ridge Creek
Wheel Gulch Basin Spring
Wheel Gulch Basin
Weatherby Spring
South Dixie Ditch
Storie Gulch
Reiber Creek
Bragg Creek
Jett (historical)
Trail Gulch
Dry Creek
Andersen Creek
Huntington Independent Order of Odd Fellows Cemetery
Huntington Old Cemetery
Lime - Dixie Cemetery
Rye Valley Cemetery
Rye Valley
Smith Gulch
Kivett Reservoir Number 3
Kivett Reservoir Number 2
Kivett Reservoir Number 1
Falkner Spring
Willow Springs Creek
Trail Creek (historical)
Vane Ranch Reservoir
North Dixie Ditch
Cottonwood Spring
Foster Spring
Hope Butte Spring
Hope Flat Reservoir
Willow Creek Waterhole
Willow Creek Reservoir 1
Willow Creek Reservoir
Lower Kern Creek Spring
West Tub Mountain Reservoir
Dry Gulch Reservoir (historical)
Mattock Gulch
Stone Quarry Spring
Stone Quarry Gulch
Dell (historical)
Stone (historical)
Road Gulch
Willow Creek Reservoir 2
Warm Springs (historical)
Dell Cemetery
Dry Creek
Davis Reservoir Three
Davis Reservoir Four
Morfitt Ditch
Birch Creek Ditch
Cube Spring
Mattie Spring
Miller (historical)
Tuesday Gulch
Shasta Spring
Kentucky Gulch
Brogan Hill
Beers Ditch
Glasscock Creek
Marble Creek
Humboldt Basin (historical)
Eddy Slough
Rich Gulch
Cake (historical)
Mine Spring
Bridgeport Cemetery
Rattlesnake Reservoir
Log Creek Basin
Poison Creek Reservoir
Lockett Reservoir
Wood Reservoir
Shell Rock Spring
Clara Spring
Rock Cabin Spring Number 1
Alkali Spring 2
Skelton Spring
Swede Spring
East Prong Spring
Grey Horse Spring
Willow Creek Reservoir Four
Upper Turner Creek Spring
Kern Creek Reservoir
Kern Creek Spring
Little Willow Creek Spring
Pritchard Reservoir
South Fork Pole Creek
Antelope Spring
Antelope Springs Creek
Wheaton Creek Reservoir
Hay Canyon Reservoir
Zotto Reservoir
Rock Creek
Clover (historical)
Stoney Gulch
Caviness (historical)
Hugg Spring
Ironside Valley
Miller Creek
Duncan Ditch
Ironside Cemetery
The Ponds Reservoir
Young Ditch
Moltham Reservoir Four
Moltham Reservoir Five
Moltham Reservoir Two
Moltham Reservoir Three
Moltham Reservoir One
Rose Creek
Indian Gulch
Camp Colfax (historical)
Pole Gulch Reservoir
Tub Spring
Reeds Ditch
Independence Creek Ditch
Gee Creek Swamp
Mink Creek
Butler Reservoir
Powderville (historical)
Palmer (historical)
Cranston Reservoir
McCann Spring
Constance Reservoir
Jamestown (historical)
Miles (historical)
Johnson Spring
Erwin (historical)
Burkemont (historical)
Cleveland (historical)
Belgian Gulch
West Fork Reservoir
Stices Gulch Reservoir
East Fork Reservoir
Station Spring
Tumbledown Spring
Tumbledown Creek
Anthony Lakes Sno-Park
Lard Lake
Ice Cap Creek
Cow Canyon Springs
Bostick Spring
Trout Creek Valley
Cross Keys (historical)
Shaniko Flats
West Eagle Horse Camp
Boulder Park Recreation Site
North Fork Anthony Campground
Sprague River Park Recreation Site
Kimsey Springs
King Creek
Alder Springs (historical)
Honey Creek Falls
Spruce Meadow
Malloy Spring
Hawley Creek
Currant Creek Reservoir
Currant Creek Dam
Spring Recreation Site
Ross Creek
Crown Rock (historical)
Willow Branch Spring
Willow Branch
Potter Peak
Schmidt Well
Pelican Point
Willams Ditch
Narrows
Bull Ditch
Baker Well
Big Red S Canal
Swan Lake Artesian Well
Graves Island
Sodhouse Spring
Green Reservoir
Rocky Reservoir
Barren Valley Reservoir
Browns Feed Canal
Indian Reservoir
Basin Reservoir
Barren Valley
Indian Creek Butte
Venator Reservoir Five
Big Gulch Reservoir
McRae Slough
Butte Ditch
Howes Well
Clemens Well
Sunset Valley Cemetery
Indian Spring
Byars Spring
Lost Lake Waterhole
Hughet Well
Campbell Reservoir
West Batts Camp Lake
One O'Clock Lake
Cheatgrass Reservoir
Harney Valley
Cow Creek Sink
Cave Gulch
Burns City Wells
Fenwick Canyon
Savage Slough
Arntz Reservoir
Mud Ridge
Charlie Creek
Parker Springs
Thousand Springs
Merrick Well
Ruh Creek
Davis Well
Crane Cut Creek
Cory Ditch
Windy Point Cemetery
Thompson Well
Scrub Bull Spring
Altnow Reservoir
Betum Spring
Glasgow Gulch
Griffin Creek
Horse Lakes
Leonard Creek
Fisher Island Channel
Goat Island
Harney Basin
Johnson Spring
Juniper Ridge
La Grande Watershed
Little Willow Creek
Lynch Gulch
Alvord Valley
Antelope Creek
Arizona Creek
Bourne Landing
Bone Canyon
Broughton Beach
China Hollow Creek
Coyote Spring
Bingen Gap
Canyon Meadows Lake
Captain Keeney Pass
Deadman Hill
D River
Drake Point
Montgomery Rapids
Old Slow and Easy Landing
Perkins Flat
Powell Creek
Rogers Peak
Salt Lick Creek
McKay Reservoir
Marquam Lake
Phillips Lake
Moffett Falls
Muleshoe Mountain
North Fork Willow Creek
Oxbow Dam
Ramsey Island (historical)
Rinearson Point
Rock Creek
Rocky Point
Rowena Gap
Rugged Crest
South Fork Willow Creek
South Fork Billy Creek
Starvout
Tyee Rapids
White Horse Mountains
Wildcat Rapids
Willamette National Forest
Strube Lake
Sand Hollow Battleground
Dry Creek Arm
Demoley Wilson County Park
Cedar Creek
Peninsula Day-Use Area
Trowbridge Creek
Little Rock Creek
Hanenkrat Creek
Hembre Lookout (historical)
Mining Creek
Siskeyville (historical)
Trask River County Park
Trask
Murphy Guard Station
Netarts Bay Campground
Frank Creek
Farmer Creek Rest Area
Yelkis Creek
Edstrom Reservoir
Eagle Mine
Polly Creek
Dufoe Creek
Beaver Lookout
Caufield Marsh
Beaverton (historical)
Randolph Cemetery
Hultin Creek
Caufield Gulch
Seestrom Creek
Cedar Creek
Woolsey Creek
Red Creek
Clear Creek
Hall Prairie
Kausen Creek
Phil Creek
Old Myrtle Point Cemetery
Brewer Cemetery
First Creek
South Branch Cut Creek
Waddington Creek
Lampa (historical)
Honcho Creek
Rock Crusher Creek
Farrin Creek
Albert H Powers Memorial State Park
Belding Point
Murphy Camp Creek
Batterson Creek
Diamond Creek
Tilden Bluffs
Whitney Creek
Tilton Creek
Dietz Creek
Gilmore Creek
Thomas Creek
Tillison Creek
Scotch Creek
Pigeon Creek
Mesabi Creek
Bloom Lake
Rector Creek
McPherson Creek
Clammer Creek
Starr Creek
Strahm Creek
Granite Creek
McKenny Creek
Schroeder Creek
French Creek
Triangulation Creek
Fick Creek
Western Creek
Kilchis Falls
Fossil Canyon
Mutt Creek
Schmitz Creek
Fitch Creek
Berry Creek
Anns Creek
Rose Creek
Gorge Creek
Morris Creek
Diamond Hill
Lehmam Creek
Wolf Point
Wilson Falls
Bridge Creek
Luebke Creek
Sargent Creek
Hann Creek
Spaur Creek
South Fork Jordan Creek
Pucket Creek
Bickford Creek
Denver (historical)
Gods Valley
East Fork Whitehorse Creek
Jones Creek
No Name Creek
Quartz Creek
Booth (historical)
Benjamin Gulch
Booth Gulch
Ramsey Creek
Long Fibre County Park
Albro Creek
Anchor (historical)
Dark Creek
Alice Creek
Turkey Creek
Weaver Creek
Clough Gulch
Beckworth Creek
Dietch Creek
Kennedy Creek
Porter Creek
Lavadoure (historical)
Short Creek
Devils Punch Bowl
Ninemile Camp
Goat Trail Creek
Knupp Creek
Susan Creek
Slip Creek
Jacob Creek
Rattail Creek
Valsetz Falls
Small Creek
Surprise Valley
Veatch Creek
Comer Brook
Copper Creek
Riddle Cemetery
Hilp Creek
Sanderson Brook
Lake Stomar Reservoir
Alder Creek
Glenbrook
China Creek
Lunsbury Creek
Deeds Creek
Windy Creek County Wayside
Mynott Creek
Blue Creek
Willingham Creek
Boulder Creek
Wagner Canyon
Applegate Gulch
McNair Creek
Harris Creek
Singletree Gulch
Meadow Creek Campground
Horseshoe Bend Campground
Russian Creek Campground
Argo County Park
Horseshoe Gulch
Calvert Slough
Rector Lookout
Howard Rierson Spruce Run County Park
Gold Creek
Cedar Creek
Furtado Creek
Josie Creek
Alder Creek
Tideport
Fishhawk Falls - Lee Wooden County Park
Knob Point
Snow Point
Davis Creek
Carmen Creek
Dogwood Creek
Little Bear Creek
Barrow Creek
Mill Creek
Klaskanine Summit
Uncle Tom Slough
Wood Creek
Fishhawk (historical)
Lyons Creek
Wrong Way Creek
North Fork Fishhawk Creek
Tunnel Mountain
Ford Creek
Favorite Creek
Kerry Island
Knotts Creek
Kelly Creek
Spear Creek
Hanson Slough
Perkins Creek
Merril Creek
Benson Point
Windy Mountain
Stewart Creek Cemetery
Swampy Lake
Larson Slough
Tank Creek
North Fork Stewart Creek
Stewart Creek
Flume Creek
Kyser (historical)
Hudson (historical)
Cries Creek
Helloff (historical)
Combs Creek
Haines Creek
Rhinehart Creek
Holm Creek
Hoyt Creek
Pennock Creek
Ryan Creek Reservoir
Wilson River Picnic Ground (historical)
Wilson (historical)
Bend Creek
Max Creek
Company Creek
Warner Creek
Necanicum (historical)
Wolf Creek
Alder Creek
C Z Picnic Ground
Davis Point
Hoover Spring
Haystack Hill State Park
Klootchy Creek County Campground
Waterfall Creek
Crescent Creek
Chapman Ponds
Rippet Mountain
Little Muddy Creek
Tillangora Creek
Mason Creek
Cedar Creek
Austin Creek
Hug Point State Park
Clayton Creek
Chisana Creek
Tolovana Beach State Park
Hug Creek
Devils Cauldron
Acey Creek
South Sugarloaf
Bailey Point
Struby Creek Reservoir
Electric Creek Reservoir
Barnegat (historical)
North Jetty
Brimmer Creek
Heitmiller Creek
Saltair Creek
Painted Rock
Green Hill
Crab Rock
Pearl Creek
Zaddach Creek
Kebbe Creek
Roy Creek Park
Foley (historical)
Crystal Creek
Dry Creek
Crag Mountain
Waldron Creek
Stuart Creek
Blue Star Creek
Shirley Creek
Iris Creek
School Creek
Slide Creek
Watertank Creek
Moroney Canal
Nedonna Lake
Nedonna Creek
Crescent Creek
Classic Ridge
Upper Nehalem
Tubessing Creek
Bayside Gardens
Nehalem Bay State Park
Crab Rock
North Jetty Nehalem Bay
South Jetty Nehalem Bay
Clear Creek
Japanese Creek
Gervais Creek
Zimmerman Creek
Fisher Creek
Pye Slough
Nehalem Spit
Gooseberry Creek
Eagle Rock
Yew Camp
Thompson Creek
Big Burn Camp
Bear Creek
Wilson Creek
Knepper Creek
Irwin Creek
Tenmile Cemetery
Dysert Creek
Flournoy Creek
Severt Iverson Memorial County Park
Murray Cemetery
Tichenor Cove
Tichenor Cemetery
Jim Creek
Lakeport (historical)
Joe Cox Creek
Jenny Creek
Mill Creek
Hare (historical)
Okietown
Ocean View Cemetery
Eastman Creek
Horseshoe Falls
Hawk Gulch
Ash Creek
Cliff Gulch
Lazy Creek
Coal Mine Creek
Bear Gulch
Alder Gulch
Lonesome Gulch
Rocky Creek
Water Gulch
Hence Creek
Oak Gulch
Maple Creek
Fort Birdseye (historical)
White Spring Branch
Sugarpine Gulch
Maple Gulch
Twomile Valley
Big Lake
Bybee Gulch
Harrison Creek
Charley Creek
Siletz Keys
Gleneden County Park (historical)
Salishan Lake
Gertulla Creek
Spring Creek
D River State Park
Taft Cemetery
Rabbit Rock
Pacific Palisades
Depoe Bay Creek
Otter Crest Rest Area
Dope Creek
Williams Creek
Lincoln Beach Wayside
North Depoe Bay Creek Reservoir
Finger Rock
Buford Hill
Kistler Spring
Agate Beach State Park
Bains Creek
Lucky Gap Creek
Little Schooner Creek
Nye Creek
Miner Creek
Rocky Top
Starfish Cove
Schooner Point
Cold Springs Reservoir
Martin Falls
Salmon Creek
Linkville Cemetery
Sky Creek
Millsite Creek
Home Creek
Paper Spring
Phillips Ditch
Worden Cemetery
Holland (historical)
Ady (historical)
Furber Marsh
Largent Pond
West Klamath (historical)
Botens Reservoir
Stewart Lenox
Bear Pan Creek
Nellie Creek
Brewster Valley
South Fork Camas Creek
Canyon Creek
Maple Creek
East Fork China Creek
Reeves Creek
Karl Creek
Skeeter Camp
Park Creek Recreation Site
Cherry Creek Recreation Site (historical)
South Fork Cherry Creek
North Fork Cherry Creek
Middle Creek County Park
4H Camp
Sixes Beach
Buffington Memorial Park
Cape Blanco Mine
Sullivan Creek
Park Creek
Moore Creek
Three Tree Camp (historical)
Spring Creek
Hawley Reservoir
Baker Creek
Dahl Log Pond
Dufort Creek
Rosa Creek
Mingus Park Creek
Mingus Park Lake
Boatman Gulch
Wallace Gulch
Newcastle Mine
Smith Reservoir
The Buttes
Southport Creek
Alder Spring
Maxwell (historical)
Kings Landing (historical)
Thirty Six Mine
Smith-Powers Mine
Lyons Reservoir
Masters Landing (historical)
Miller Reservoir
Watsonville (historical)
Delmar Creek
Coos City (historical)
Haynes Cemetery
Dunham Gulch
Fox Creek
Sunset (historical)
Haywood Inlet
Tarheel Creek
Storey Creek
North Fork Joe Ney Slough
South Fork Joe Ney Slough
Yoakam Hill
Day Inlet
Talbott Slough
Theodore Johnston Creek
Chard Creek
Cape Arago Lighthouse
South Slough Cemetery
Coalbank Creek
Gillis Creek
Seaman Creek
Bull Pasture
Contrary Bend
Blue Creek
North Fork Creek
Estelle Falls
Chute Creek
Hodson Creek
Coos River
Allegany Cemetery
Smith Creek
Franson Creek
Garden Gulch
Crystal Creek
George Reservoir
Harlin Creek
North Fork Glen Aiken Creek
Johnston Log Pond
Harlocker Hill
Anderson Creek
Reservoir Creek
Independent Order of Odd Fellows Cemetery
North Fork Wood Creek
Coos County Youth Camp
Middle Creek Falls
Fall Creek
Hatcher Creek
Morris - Baker Cemetery
Fox Bridge Cemetery
Twin Cedars Creek
Jerrys Flat (historical)
Pine Point Picnic Area
Hafner Creek
Kimball Bar
William Creek
Papoose Creek
Bagnell Ferry
Walen Creek
Hooter Scooter Prairie
McKinley Mine
Lake of the Woods
Long Prairie
Jackson Prairie
Jacks Prairie
Powell Bar
Murry Creek
Bryson Creek
Myrtle Island
Baskett Point
Steve Creek
Rock Creek
Branton Bar
Churchill Rapids
Coles Valley
Willow Creek
Day Creek
Grier Reservoir
Mill Creek
Callahan Guard Station
Blood Camp
Woods Camp
Sievers Creek
Skookum Spring
Thief Valley County Park
Mason Dam Recreation Site
Wagner Springs (historical)
Janssen Spring Creek
Whiteline Ditch
Brookside Spring
Whiteline Spring
Potter Mill (historical)
Pokegama (historical)
Klamath Canyon
Randolph Flats
Swan Lake Meadow
Hill Reservoir Number One
Hill Reservoir Number Two
Johnson Reservoir Number Two
Johnson Reservoir Number One
Modoc Ridge
Keyser Reservoir
Horton Rim
Shook Spring
Oreoil (historical)
Barton Reservoir
Olene Hot Springs
Eternal Hills Memorial Gardens Cemetery
F-1 Lateral
Crystal Spring
Dehlinger Reservoir
White Lake City (historical)
Clinton (historical)
Devils Gulch
Hartwell Draw
Dixie Spring
Cascade Springs
Sloan Springs
Swinning Spring
Shake (historical)
Lucky Hollow
The Meadows
Cinnabar Mountain
Reese Creek Cemetery
Conover Gulch
Red Blanket Reservoir
Derby (historical)
Daley Spring
Deer Lick Spring
North Fork Queens Branch
Brown Gulch
Rocky Gulch
Ladies Creek
Collins Gulch
A K Gulch
Evans Gulch
French Gulch
Potter Creek
Saddle Creek
Beaver Creek
Roth Creek
Slate Creek
Lick Creek
Beck Spring
Albright Creek
Gumbo Gulch
Hawkins Creek
Spring Creek
Schoolhouse Creek
Rushing Spring
Nygren Reservoir
Niday Branch Cow Creek
Clear Creek
Wildcat Creek
Panther Creek
Bonnie Creek
Coles Valley Creek
North Fork Byron Creek
East Fork Byron Creek
Mill Creek
Noah Creek
Molby Creek
Cardwell Creek
Dry Creek
Manis Creek
Messing Creek
Corral Creek
Little Coal Creek
Muddy Creek
Beaver Creek
West Fork Chicken Creek
Turnidge Creek
Gravel Creek
Bochsler Creek
Evans Creek
Mineral Creek
Kraus Creek
Howell Prairie Creek
Willamette Valley
Fossil Lake
Red Fir Spring
Julia Butler Hansen Refuge for the Columbian White-tailed Deer
Fort McDermitt Indian Reservation
Hart Mountain National Antelope Refuge
Santiam State Forest
Steens Mountain Wilderness
The Dalles Unit
Three Sisters Wilderness
Wenaha-Tucannon Wilderness
Martin Reservoir
Upton Slough
Middough Creek
Millionaire Mine
Dean Creek
Quackenbush Reservoir
Swanson Creek
Jacksonville Cemetery
Holman Gulch
Ice House Creek
Soda Creek
Helms Cove
Hannah Creek
Prairie Branch Cove Creek
South Branch Cove Creek
North Branch Cove Creek
Donsmore Spring
Hooper Springs
Toll Road Gap
McAllister Spring
Spring Creek
Powder Springs
West Branch Carter Creek
Dollarhide Spring
Steinman Creek
Bear Gulch
Viaduct Creek
Cougar Gulch
South Fork Barron Creek
Shady Spring
Angora Creek
Japanese Creek
Hades Gulch
Twin Harbor Loop Spring
Glendale Reservoir
Stranns Spring
Glendale Masonic Cemetery
Cindy Creek
Cedar Creek
Stevens Creek
Wolf Creek Cemetery
Rattlesnake Creek
Fisher Gulch
Dunbar Gulch
Spanish Gulch
Hog Eye Creek
Gillet Gulch
Taylor Gulch
Draper (historical)
Moore Gulch
Left Fork Birdseye
East Branch Galls Creek
West Branch Galls Creek
Max Gulch
Horn Gulch
Brushy Gulch
Lyons Gulch
Black (historical)
One Horse Town (historical)
Lucky Boy Mine
Winningham Reservoir
George Black Gulch
Rock Gulch
Right Fork Forest Creek
Cantrall Creek
Long Gulch
Balls Branch
Kane Gulch
Left Fork Kidney Gulch
Kidney Gulch
Bailey Gulch
Cove Creek
Myrtle Gulch
Missouri Flat Cemetery
Wooldridge Creek
Cherry Creek Myrtle Preserve
Lost Creek Ranger Station
Maple Creek
Kenny (historical)
Mabel Spring
Kennison Reservoir
Sexton Spring
Azalea Creek
Maple Spring
Canteen Spring
Olden Spring
Corliss Creek
Pine Gulch
Lozier Creek
Laundry Creek
Swanson Creek
Pickering Creek
Anderson Creek
Pleasant Valley Cemetery
Bannister Creek
Antler Creek
Walker Creek
Salt Lick Creek
Mary K Reservoir
Macks Creek
Cochran Gulch
Mountain Spring
Stites (historical)
Grandpa Gulch
Secesh Gulch
Benson Gulch
Brown Gulch
Whiskey Bottle Creek
Schoolhouse Gulch
Slagle Creek
Browning Spring
McCourtney Creek
Still Creek
King Gulch
Kettering (historical)
Corn Creek
West Fork High Prairie Creek
East Fork High Prairie Creek
Roseburg Creek
Stewart Gulch
Hamline Creek
Weaver Creek
Cox Gulch
Buck Fork (historical)
Left Fork Frozen Creek
Eleanor Reservoir
Hughes Creek
Stone Creek
Carson Creek
Sanderson Gulch
Rose Creek
Clayton Creek
Little River Log Pond
Pattersons Mills (historical)
Lone Rock Wayside County Park
Lone Rock Camp
West Fork Britt Creek
Hoaglin (historical)
Old Hatchery Creek
King Creek
Harvey Cemetery
Fair Oaks Cemetery
Fair Oaks County Park
Sutherlin Cemetery
Smith Canyon
Whistler Bend County Park
Bull Creek
Oak Creek Cemetery
Oak Creek (historical)
Paris Reservoir
Black Mud Summit
Livingston Cemetery
Livingston Creek
O C Brown County Park
Hatfield (historical)
Middle Fork of South Fork Deer Creek
Boggess Cemetery
Rock Creek Recreation Site
Millpond Campground
Weeping Rock Campground
Pine Point
Quartz Point
Steamboat Falls Recreation Site
Jack Canyon Creek
Madison County Wayside
Deep Gulch
Kellogg Cemetery
Dimmick Cemetery
Rattlesnake Gulch Reservoir
Fitzpatrick Creek
Smith Ferry (historical)
Tapp Creek
Haines Creek
Elkton Cemetery
Bower Creek
Henderer Cemetery
Saddle Butte Creek
East Fork Mosetown Creek
House Creek
Cedar Creek
Patterson Creek
Grabb Creek
Sawyer Rapids
Stony Brook
Long Prairie
Butler Creek
Bunch Bar
Sawyers Ferry (historical)
Fort Flournoy (historical)
Champagne Creek Valley
Wardton
Harrison Young Brook
Rock Creek
Gobblers Knob
Green Oaks County Park
Eugene Log Pond (historical)
Umpqua Log Pond
Shady Point Creek
Iverson Log Ponds
Alberson Creek
Alsea Log Pond
Dillard Log Pond
Civil Bend (historical)
Civil Bend
Roseburg National Cemetery
Lookingglass Hill
Sylman Valley
Barnes (historical)
Sleepy Hollow Creek
Barager Creek
Roseburg Masonic Cemetery
Roseburg Catholic Cemetery
Roseburg IOOF Cemetery
Eden Cemetery
Hestness Park
River Forks County Park
Cleveland Cemetery
Hidden Valley Creek
Cleveland Rapids
Burke Creek
Dodge Canyon Creek
Rice Hill State Safety Rest Area (historical)
Cabin Creek Safety Rest Area
Metz Hill Cemetery
Stearns City Park
Martin Mill Pond
Dimmick Creek
Fords Pond
Wilbur Cemetery
Short Creek
Mar-Linn Log Pond
Amacher County Park
Echo Butte
Davis Creek
Kopp Creek
Yoncalla Cemetery
Devore (historical)
Cold Creek
Drain IOOF Cemetery
Hendrick Creek
Drain Cemetery
Smith River Log Pond
Smith Creek
Green Creek
Putnam Cemetery
Burn Creek
Poodle Creek
North Fork Wilson Creek
Rock Canyon Creek
East Cinnabar Creek
Norman Creek
Weyerhaeuser Creek
Amos (historical)
Bemis Cemetery
Rouse Creek
Deer Creek
Massey Creek
Wallace (historical)
Lone Pine Cemetery
Indian Butte
Doolittle Butte
Sliter Butte
Cuttock Butte
Beck Creek
Rodgers Creek
Youngs Creek
Murray Creek
Harvey Creek
Whitney Creek
McWilliams Creek
Elkhorn Creek
Sheldon Creek
Whites Creek
Taylor - Lane Cemetery
Redford Butte
Chapman Butte
Kellys Butte
Schafer Creek
Pass Creek County Park
Anlauf Creek
Spike Buck Butte
Calvert (historical)
Schoolhouse Creek
Buck Creek
Lane Creek
Harris Family Cemetery
Buck Creek
Loon Lake Lookout
Cougar Pass
Surprise Creek
North Fork Soup Creek
Michigan Pass Creek
Craig Creek
Slideout Creek
Baker Creek
Upton Creek
Kelly Creek
Double Barrel Creek
Wooden Creek
Ralston Spring
Big Hot Spring
Wolf Flat
East Canal
Johns Waterhole
Warden Reservoir
Simms Creek
Easy Creek
Malin Cemetery
Capek Reservoir
Timber Hill Reservoir
Junction Waterhole
Willow Valley Campground
Lost River Spring
Antelope Spring
Rimrock Spring
Gerber Lower Division Reservoir
Twenty One Reservoir
Horse Camp Reservoir
O'Shea Spring
Mud Spring
Moonshine Spring
Casebeer Spring
Boundary Spring
Gerber Reservoir South Recreation Site
Lockey Flat
Noble Creek
Linsay Spring
Kent Reservoir
Noble Reservoir Number One
Meadow Spring
Pine Creek
Rock Canyon
Dobe Creek
Rattlesnake Creek
Black Canyon Creek
Woolen Canyon Spring
Sullivan Spring
Willow Valley Canal
Willow Valley
Gerber Spring
Horsefly Valley
Mortar Prairie
Milk Creek
Big Tank
Shroder Reservoir
Cherry Spring
Harper Reservoir
Summit Reservoir
East Beaver Charlie Reservoir
West Beaver Charlie Reservoir
Deafenbough Reservoir Number 1
Vance Ranch
Peffley Creek
Comegys Lake
Cox Grove Lake
Rehab Reservoir
Bay Duke Reservoir
Beasley Lake
Gold Hill Regional Park
Carroll Well
Upper Goose Egg Lake
Santy Reservoir
Grasshopper Spring
Hansen Flat Creek
Rosio Reservoir
Guadalupe Meadows
Egli Waterhole
Ryegrass Lake
Hakel Spring
Idlewilde Cemetery
May Street Elementary School
Andy Five Spring
Browns Horse Corral Waterhole
Badger Draw Reservoir
Clear Waterhole
Taylor Gulch
Independent Order of Odd Fellows Cemetery
Hoselton Creek
Segundo Ditch
Seven Spring
Modesto Creek
Saint Johns Cemetery
Grove Spring
Little Peacock Reservoir
Potato Lake
Studhorse Waterhole
Little Spring Creek
Little Spring Creek Reservoir
Cream Lake
Holmes Reservoir Number Two
Dolton Spring
Divide Waterhole
Division Waterhole
Lillard Lake
Pickett Lake
Flatiron
Mustang Reservoir
Double O Cold Spring
Shearing Corral Creek
Division Fence Reservoir
Overall Flat
Large Lake
McCarty Cabin Waterhole
On the Rim Waterhold
Rehart Lake
Woods Lake
Wolter Lake
Dobie Flat
Little Mud Creek
Little Depot Creek
Badger Draw
Boyce Ranch
Bugby Hole
Jetty Lagoon
Heceta Bank
East Mine Creek
East Fork Big Trout Creek
Mine Creek
Perrin Island
West Mine Creek
Misery Flat
Ice House Lake
Ice House Canyon
Hoodoo Butte
Barlow Creek
Low Pass
West Fork Rock Creek
Deadman Creek
Calico Creek
Deep Hollow
Grasshopper Flat
Rainbow Falls
Drury Lake
Mitchell Mountain
Big Canyon
Coburg Hills
Owl Creek
Lutton Pond
Johnson Reservoir
Tub Springs
Doe Island
Fawn Island
Hyatt Meadows
Keene Creek Reservoir
Rim Reservoir
Juniper Glade
Spring Creek
Schoolhouse Meadow
Buck Island
Highway Lake Waterhole
Toms Waterhole
Platt 1 Reservoir
Cook Creek
Big Glades
Eagle Butte
Lucky Canyon
Cold Spring Creek
Lake Creek Reservoir
Bradshaw Reservoir
Rocky Gulch
Long Branch Reservoir
Whiskey Creek
Rock Creek
Spring Creek
Rim Rock Springs
Francis Lake
Marsh Reservoir
Long Prairie Reservoir
Blue Creek Spring
Bitter Spring
Brush Spring
Rose Mary Pond
Rooster Comb
Casey Spring
Heffner Spring
Pre-exemption Spring
Pankey Reservoir
Lewis Spring
Nobel Pond
Gillette Spring
Goodlow Pond
Tillie Spring
Schnipps Valley Spring
Miller Creek Spring
Miller Diversion Dam
Hope Reservoir
R N A Spring
Gary Reservoir
Ben Hall Spring
Tule Lake Valley
Smith Reservoir
Lone Pine Reservoir
Simmons Ranch
Caseview Spring
Three C Spring
Coulter Spring
Wagon Road Spring
Horsefly Reservoir
Olive Reservoir
Rock Pond
Stump Pond
Rattlesnake Gulch
Surface Spring
Judd Creek
Iron Mountain Spring
Devils Spring
Orman Spring
South Guzzler Waterhole
Bedspring Flat Spring (historical)
McCullough Spring
Upper Nodine Spring
Ray Creek
Harrison Spring
Simonis Gulch
Cottonwood Gulch
Nelson Place
Barnes Spring
Hawks Nest Spring
Storie Spring Number Two
Walnut Spring
Washout Spring
Montezuma Spring
Smith Spring
Chaud Spring
Waterbirch Spring
Caviness Spring Number Two
Back Swimmer Spring
East Morgan Spring
Morgan Mountain Spring Number Two
Morgan Mountain Spring
Quick Step Spring
Benson Spring
Powell Spring
Nay Spring
Billy Gulch Spring
Bay Horse Spring
Tate Spring Number Two
Dyne Spring
Divide Spring
Jett Spring
Microwave Spring
Brush Spring Number Two
Juniper Mountain Waterhole Number Two
Sidehill Spring Number Two
Junkpile Spring
Y Reservoir
Pipeline Spring
E T Reservoir
Table Mountain Spring Number Two
Table Mountain Spring
Rim Spring
Marble Creek Spring
Willow Spring
Chukar Spring
Binder Spring Number Two
Binder Spring
Binder Gulch
Overhead Flat Spring
Brush Spring
Spring Gulch Spring
Boat Dock Spring
Juniper Mountain Waterhole
Triangle Reservoir
New Seeding Spring Number One
New Seeding Spring Number Two
New Seeding Spring Number Three
Lucky Spring
Porcupine Spring
Spring Gulch
McDowell Butte Reservoir
Cinder Butte Well
Suitter Spring
Fence Spring
Colton Spring
Cosens Spring
L T Spring
Juniper Spring
Mun Spring
Try Spring
Quaker Spring
Summit Spring
Dry Gulch Spring
First Canyon Spring
Bog Spring
Black Flat Spring
Abram Spring
Table Mountain Well
West Fork Road Spring
Rye Valley Spring
Cloverleaf Spring Number Two
Brown Gulch Spring
Little Willow Creek
Alkali Flat Reservoir
Alkali Gulch Reservoir
Tub Springs
Long Drain Reservoir
Bostic Lake Reservoir
Alkali Reservoir
Lower Hope Butte Reservoir
Lower Kern Spring
South Jacobsen Reservoir
Big Cut Reservoir
Little Cut Reservoir
Jordan Waterhole Reservoir
Hope Ditch
Fern Spring
Rocky Pond
May Reservoir
Aleys Spring
Sunset Prairie Reservoir
Rena Reservoir
J Pond
McCartie Spring
Horse Canyon Spring
Vinson Pond
Gully Pond
Dead Spring
Wild Spring
Dry Prairie Number One Pond
Prairie Pond
Horn Pond
Miner Pond
Dry Gulch Pond
Willow Flat Reservoir
Forty Pond
McCall Point
North Fork Lightning Creek
Rock Creek
Captain Gray Mountain
East Tarter Gulch
West Tarter Gulch
Geren Island
Bottle Creek
Shoofly Rapids
Karl Lake
Ruth Lake
Clover Creek
Hoevet Creek
Brownlee
Lewis and Clark National Wildlife Refuge
Umatilla National Wildlife Refuge
Warm Springs Reservation
John Day Fossil Beds National Monument
Ruckman Dam
Squaw Creek Dam
Aamodt Dairy Reservoir
Aamodt Flashboard Dam
Agate Dam
Agate Reservoir
Albertsons Dam
Albertsons Reservoir 'A'
Alder Creek Dam
Altnow Dam
Antelope Dam
Arkansas Dam
Arntz Dam
Bear Creek Dam
Bear Creek Dam
Bear Creek Reservoir
Benjamin Lake Dam
Bennett Dam
Betty Jane Deardorff Dam
Deardorff Reservoir
Bibby Dam
Big Creek Dam Number 1
Big Rock Dam
Bill Howell Dam
Bill Howell Reservoir
Black Canyon Creek Dam
Blevins Dam
Booth-Kelly Lumber Company Log Pond
Booth-Kelly Lumber Company Log Pond Dike
Buether Dam
Bully Creek Dam
Bumphead Dam
C A Smith Dam
C A Smith L and M Company Storage Reservoir
C C Porter Dam
C C Porter Reservoir
C C Porter Reservoir
Calderwood Dam
Campbell Dam
Canyon Creek Meadows Dam
Carty Reservoir
Carty West Dam
Case Creek Dam Number One
Chapman Dam
Cherry Creek Dam
Chevally Reservoir Dam
Clearwater Number One Forebay Dam
Cobb Creek Dam
Collins Dam
Cooper Creek Dam
Berry Creek Dam
Ben Irving Reservoir
Cottonwood Meadow Dam
Crowley Dam
Crump Dam
Dallas Lake Dam
Dam Number Three
Deep Canyon Dam
Deep Canyon Reservoir
Denley Brothers Dam
Dixonville Log Pond Dam
Drain Plywood Company Dam
Drain Plywood Company Log Pond
Dry Creek Number Two Dam
Dry Creek Number Two Reservoir
Dry Prairie Dam
Dry Prairie Reservoir
Duggan Dam
E R Baker Dam
Earl Kennel Dam
Earl Kennel Reservoir
East Lakes Dam
Easterday Dam
Echave Dam
Edward Wageman Dam
Edward Wageman Reservoir
Elmer Dam Number Three
Elmer Dam Number Four
Elmers Reservoir 4
Emory Moore Dam
Emigrant Dam
Evans Dam
Frog Pond Number One
F-P Reservoir
Farman Creek Dam
Fay Canyon Dam
Fehrenbacker Reservoir
Fish Lake Dam
Fishhawk Dam
Fishhawk Lake
Fitzgerald Dam
Fopiano Dam
Ford Farms Dam
Ford Farms Reservoir
Fort Creek Dam
Fox Dam
Franzen Dam
Fredericks Dam
Fredericks Reservoir
Goodrich Dam
Grays Slough Dam
Greaser Lake Dam
Griffin Creek Dam
Guano Canyon Dam
Hallinan Dam
Harrison Dam
Harrison Reservoir
Hart Lake Dam
Herman Nusbaum Dam
Hershiser Dam
Hershiser Reservoir
Hoover Dam Number 1
Hoover Dam Number 2
Horton Dam
Hult Log Storage Pond Dam
Hunter Reservoir Dam
Indian Lake Dam
Jaca Dam
James O Fisher Dam
Joe Crow Dam
Joseph Rogers Dam
Joseph Rogers Reservoir
Keno Dam
Kern Brothers Dam
Kilgore Dam
Killamacue Dam
Kinnan Dam
Kinnan Reservoir
Kivett Dam Number 3
Krumbo Dam
La Grande Dam
Laird Dam
Lake Koinenia
Lake Creek Dam
Layton Dam Number 2
Layton Reservoir Number 2
Leaburg Reservoir
Little Park Dam
Little River Log Dam
Little Willow Creek Dam
Lloyd Hill Dam
Lofton Dam
Logan Butte Dam
Logan Butte Reservoir
Lomoha Reservoir
Lorence Dam
Lower Chapman Dam
Lower Chapman Reservoir
Malheur Dam
Maple Headquarters Dam
Maple Headquarters Reservoir
Marvin Fast Dam
Marx Dam
Mar-Linn Timber Corporation Log Pond Dike
Medco Number 3 Dam
Medco Number 3 Pond
Merwin Dam Number 2
Millicoma River Rearing Pond Dam
Millicoma River Rearing Pond
Mission Creek Reservoir
Mompano Dam
Moores Hollow Dam
Morgan Brothers Dam
Morgan Lake Dam
Morrison Dam
Mount Baldy Log Pond Dam
Mud Lake Dam
Murphy Dam
Myrtle Point Veneer Company Log Dam
North Fork Indian Creek Dam
Nusbaum Farms Reservoir
Oregon End Dam
Oregon End Reservoir
Oregon Fibre Products Dam Number One
Osborne Creek Dam
Osborne Reservoir
Owen Dam
Oxbow Dam
Pacific Plywood Corporation Log Pond
Pacific Plywood Dam
Painted Hills Dam
Painted Hills Reservoir
Paiute Dam
Panther Creek Dam
Panther Creek Reservoir
Parsnip Creek Diversion Dam
Parsnip Creek Diversion Reservoir
Parsnip Dam
Parsnip Reservoir
Perkins Log Pond
Perkins Log Pond Dam
Petes Slough
Pettit Dam
Pitt Lake Dam
Piute Dam
Platt 1 Dam
Pole Creek Dam
Priday Dam
Randall Dam
Randall Reservoir
Radio Springs Dam
Radio Springs Reservoir
Raymond Dierickx Dam
Raymond Dierickx Reservoir
Reimer Dam
Waller Reservoir Number Three
River Bend Dam
Rock Creek Dam
Rock House Dam
Rockhouse Reservoir
Rodger Iverson Dam
Rodger Iverson Reservoir
Rowe Creek Dam
Sams Valley Dam
Sams Valley Reservoir
Sauvie Island Dam
Sevan Dam
Sevan Lake
Sevcik Dam
Shaw Dam
Sherlock Gulch Dam
Sherlock Gulch Reservoir
Silver Creek Dam
Silver Creek Reservoir
Simpson Dam
Smith River Lumber Company Dam
Little Reservoir Number Five
Smyth Dam
Star Creek Dam
Stinkingwater Dam
Fords Pond Dam
Sutherlin Log Pond
Sutherlin Log Pond Dam
Three Mile Falls Pool
Threemile Dam
Timber Products Company Dam
Trask River Dam
Updegrave Reservoir
Updegrave Dam
Vane Ranch Dam
Vaughn Dam
Vaughn Dam
Vaughn Log Dam
Vernonia Log Pond Dike
W A Woodard Lumber Company Log Pond (historical)
Walchli Dam
Walchli Reservoir
Waldo Lake Reservoir Dam
Walker Dam Number Two
Walker Reservoir Number Two
Walterville Dam
Weaver Dam
Thurman Weaver Reservoir
Werner Dam
Werner Reservoir
Western Veneer and Plywood Dam
Wheaton Creek Dam
Whistlers Bend Dam
Whistlers Bend Reservoir
Whiteline Dam
Widman Dam
Willamette Falls Dam
Willamette Falls Hydroelectric Power Reservoir
Willards Dam
Willow Creek Reservoir
Willow Valley Dam
Wilson Dam
Wilson Lake Dam
Winchester Reservoir
Wirth Dam
Woodrat Knob Dam
Worden Dam Number Two
Worden Reservoir
Yoncalla Log Pond
Yoncalla Lumber Company Log Pond Dam
Toppin Creek Reservoir
Manydraw Reservoir
Whisky Creek Cabin
Slate Slide Riffle
Telephone Hole Riffle
Plowshare Rapids
Bantam Mine
Reservoir Creek
Archer Mine
Victory Mine
China Gulch Rapids
McNary Creek
Nasty Pond
Vera Creek
Arrow Creek
Big Trout Creek
Austin Point
East Fork Camas Creek
Little Muley Creek
Point Meriwether
Suicide Creek
Hollys Ridge
Marion Flats
Womack Basin
Alder Spring
Saint Clair Canal
Goulden Canal
Saddle Butte Cemetery
Temple Spring
Loma
Black Spring
Black Canyon
Hart Ranch
Foley Creek
Fivemile Slough
East Fork/Echo Recreation Site
Slide Creek Recreation Site
McKenzie River National Recreational Trail
Cul de Sac Creek
Ludlum Place
Wheeler Creek Natural Research Area
Starvation Ridge
Hawk Ridge
Branson Canyon
Dark Canyon
Saint Katherine Catholic Church
Turner Meadow
Willow Creek Cemetery
Crowley Spring
Lick Spring
Howard Meadow
Howard Meadow Camp
Brush Spring
Mud Lake
Keeney Meadow
Bone Yard Canyon
Mahogany Ridge
Sheet Iron Jack Meadow
Iremonger Spring
George Iremonger Spring
High Gilchrist Spring
Dry Lake (historical)
Rose Creek
Bone Creek
Shirttail Creek
Saddle Camp
Goose Rock Bridge
Land's Inn Ranch Airport
Windy Point
L S Ranch
Sunken Mountain
Carter Park Safety Rest Area
Bly Creek
Coe Spring
Mud Spring
Belsham Spring
Fox Mine
Mine Creek Placer Mine
Big Nugget Mine
East Fork Mine Creek
Ennis Creek
Mountain Rest
Ogilvie Spring
Sky Scraper Spring
Ives Gulch
Ives Spring
Denny Spring
O'Rorke Ranch
Flat Camp
Balance Lake
Chapman Spring
Holloway Spring
Voight Spring
Reedville Creek
Bills Creek Rapids
Wisenor Place
North Fork Basin Creek
Haas Horse Troughs (historical)
Western Rim National Recreation Trail
Saddle Creek Recreation Site
Fivemile Viewpoint
Three Creek Rapids
Hells Canyon Creek
Bunch Point
Makin Creek
Park Cemetery
Rhodes Creek Ranch
Rock Spring
South Fork McGraw Creek
Horse Gulch
Devils Ridge
Little Horse Creek
Clear Lake Ridge
Bird Canyon
Downey Lake
Greener Ditch
Gobblers Knob
Fish Lake Recreation Site
Twin Lakes Recreation Site
Buchanan Ditch
Huff Ditch
Indian Crossing Recreation Site
Wolf Canyon
Hayden Butte
Hayden Lake
Nuxall Lake
Sprudy Lake
Marshman Lake
Lightning Creek Ranch
Joe Butte
Pringle Gulch
Hide Canyon
Brown Creek
Hamer Spring
Swamp Spring
Bobcat Spring
Skelton Spring
Cox Spring
Gibson Spring
Ferguson Spring
Rambo Spring
Hamer Creek
Little Deer Creek
Newsome Saddle
Shearing Spring
Knox Spring
Tom Vawn Spring
Double Cabin Pond
Ray Spring
Sand Spring
Mill Creek Wilderness
Marks Spring
Mahogany Spring
Buck Spring
Downs Spring
Koch Reservoir
Whistler Spring
Beoletto Ranch
Box Canyon
Willow Spring
Upper Cherry Spring
Simmons Gulch Spring
Coyne Spring
Ninety-Six Ranch
Holliday Ranch
Lowe Ranch
Wade Ranch
Purdy Ranch
Mud Flat
Willow Reservoir
Carlon Canyon
Basin Reservoir
Gunther Reservoir
Little Rock Spring
Groff Ranch
Pond Spring
Southworth Cemetery
Allison Ranch
Corral Ridge
Chapin Table
Gravelly Flat
Hankins Cemetery
Silvies Valley Ranch Airport
Pronghorn Reservoir
Old McKinney Mill (historical)
S B Spring
Bear Valley
Broken Pick Mine
Blue Mud Mine
East Side Ditch
North Salter Spring
Horse Camp Spring
Danger Point
Alkali Spring
Medlin Reservoir
Stinger Spring
Racehorse Flat
Racehorse Well
Hunter Creek
Helion Creek
Rimrock Creek
Dog Creek
Lockaby Recreation Site
Bedford Point Lookout
South Fork Water Board Intake
Oscar Creek
Button Creek
Cultus Creek
La Dee Flat
East Fork South Fork Clackamas River
Whiskey Lake
East Whiskey Lake
Bull Lake
Loco Lake
West Whiskey Lake
Murphys Lake
Twin Lakes
Walking Plow Lake
Dead Horse Lake
Joe Hostler Camp
Indian Rock
Miner Creek
Mule Prairie
Mutt Peak
Sawtooth Ridge
Klahn Creek
Sioux Reservoir
Saint Patrick Mountain Reservoir Number Two
Settlement Waterhole
Lower Juniper Waterhole
Coyote Bedground Reservoir
County Waterhole Number 2
Coffeepot Basin
Rocky Waterhole
County Waterhole Number 4
Black Points
County Waterhole Number 7
Bunker Hill
County Waterhole Number 9
Section Line Waterhole
Dead Reservoir
Saint Patrick Reservoir
Rocky Butte
County Waterhole Number 11
State Game Reservoir Number 7
State Game Reservoir Number 6
Dog Lake Waterhole
Emery Well
Brattain Reservoir Number 13
Forks Waterhole
Brattain Waterhole Number 10
Collins Waterhole
Button Waterhole
Shell Rock Canyon
Kelso Reservoir
Club Reservoir
XL Ranch
XL Spring
Sawed Horn
Duncan Place
Spur Rowel Lake
Saint Patrick Lake
Coffee Lake
Euchre Butte Well
Highway Well
Leehmann Well
Coleman Flat
Rock Spring Gulch Reservoir
Coleman Hills
Hogback Summit
State Block Well
Sand Rock
Vaughn Well
McQuade Creek Shelter
McNabb Falls
Hayden Mountain Summit
Horse Trap Waterhole
County Waterhole Number 3
Horsetail Waterhole
Square Waterhole
County Waterhole Number 15
Impossible Waterhole
Handy Waterhole
Z N Reservoir Number 5
Faber Waterhole
County Waterhole Number 18
Rocky Waterhole
Little Waterhole
Sand Hollow
Sprinkle Waterhole
Yankee Waterhole
Giant Waterhole
Wildcat Waterhole
Inter Mountain Waterhole
Between Rim Waterhole
Banta Well
Devil Well
Jackings Hole
Slim Reservoir
Fourmile Point
Bailey Waterhole
Tenmile Ridge
Fivemile Point
Horse Mountain Spring
Brim Well
Diablo Rim
Pumice Castle
Bingham Meadow
Effie Lake
Contorta Point
Eppenbaugh Reservoir
Harrison Elementary School
Sears Cemetery
Cardwell Hills
Boswell Mine
Rabbit Lake
Paradise Mine Number 1
Noyas Pass
Eagle Creek
Hodges Spring
Hoerauf Reservoir
Lowell Covered Bridge
Dexter State Park
Pengra Covered Bridge
Pengra
Pengra Mountain
Unity Covered Bridge
Parvin Butte
Halfway Recreation Site
Bentz Ponds
Rogers Mountain Ranch Reservoir
Zurfluhs Ponds
Ziebart Reservoir
Hafco Reservoir
Wilkes Reservoir
Larson Ponds
Jordan Bridge
Hannah Bridge
Larwood Bridge
Burgen Hollow
Papenfus Creek
Lightning Hollow
Crenshaw Hill
High Pass
The Hole
Target Canyon
Doris Stevens Ridge
Leibo Canyon
Rough Hole Reservoir
Funny Face Reservoir
South Willow Reservoir
Sherman Field
North Fork McDermitt Creek
Galesville Dam
Sunshine Bar Recreation Site
Minnehaha Camp
Muir Camp
Flag Crossing
New Road Spring
Castro Corral (historical)
Dry Canyon Reservoir
Little Dry Reservoir
Bobs Draw
Anderson Crossing
Cold Wind Reservoir
Chico Reservoir
West Side Reservoir
Happy Camp
Hannah Myers Ranch
Brink Reservoir
Horsehead Spring
Leehmann Reservoir
East Pass Reservoir
East Pass
Prospectors Reservoir
Lower Goose Egg Lake
Goose Egg Butte
Stormy Draw
Big Alder Creek
Menears Bend Campground
Calkins Park
South Fork McDowell Creek
Short Bridge
Mountain View Mine
Kendall Cabin
Horse Spring
Vaughn Log Pond
Schoolhouse Spring
Camp Elliff (historical)
Win Walker Reservoir
Rogue Cemetery
Curry County Rodeo and Fairgrounds
Big Prairie
Doyle Rock
Elephant Rock
Johns Hole
Racetrack Hill
Snag Patch
Smith Family Cemetery
Oro Grande Mine
Greenback (historical)
Secesh Reservoir
Woolfolk Reservoir
Hayward Pond (historical)
Smith Hill Summit
Whiskey Gulch
Four Points
Post Lake
O'Leary Reservoir Number 4
Oletay Reservoir
North Saint Patrick Reservoir
Juniper Reservoir
Saint Patrick Mountain Reservoir Number 4
Horse Corral Reservoir
Juniper Top
World Lake
Hatch Lake
Toothless Waterhole
Ripper Waterhole
Viewpoint
Viewpoint Ranch
Shull Well
Wagon Wheel
McCloskey Ridge
Miller Creek
Green Peak Falls
McCloskey Knob
The Saddle
Gardner Creek
Nye Creek
Walters Mountain
Coleman Creek
Davidson Creek
Pitney Creek
Eisenschmidt Ridge
Minert Ridge
Billy Tower Canyon
McDermitt Creek Reservoir
Zimmerman Ranch
Opalite Mine
Rose Spring Number 1
Rose Spring Number 2
Beaver Reservoir
West Mine Reservoir
Long Ridge Reservoir
Fifteenmile Reservoir
Mahogany Spring
West Cherokee Reservoir
Gopher Spring
Sheepline Canyon Spring
Dry Draw
Cherokee Canyon
Rattlesnake Canyon
Beaver Log Spring
Lasa Canyon
Dry Creek
Turner Creek
Minehole Creek
Turner Ranch
Dry Draw Reservoir
Pretty Rock Reservoir
Indian Creek Reservoir
Spring Creek Pit Reservoir
Pinky Reservoir
Bretz Reservoir
Cash Canyon
North Cottonwood Reservoir
Myers Reservoir
Upper Mitchell Spring
Little Cottonwood Creek
Spring Creek
Lasa Creek
Little Pink Reservoir
Rockaway Beach State Park
Twin Rocks State Park
Barview County Park
South Jetty
Bayocean Peninsula
Kilchis Point
Bayocean Dike
Corbia Lake
Fibre Lake
Gawley Basin
Sucker Creek
Whitehorse Falls
Bear Creek
Umpqua Landing
Crow Rapids
Hidden Valley Reservoir
Preacher Creek
Boardtree Creek
Briggs Hill
Jackson Creek
Round Mountain
Wood River Canal
Wood River Springs
Klamath State Fish Hatchery
Echave Ditch
Oregon Canyon Ranch
Schoolhouse Spring
Schoolhouse Pit Reservoir
Schoolhouse Spring Number 2
Buckaroo Spring
Ansotegui Place
Gavica Place
Jaca Place
Rock Canyon
Oregon Canyon
Schoolhouse Canyon
Island Canyon
Box Canyon
Fall Canyon
Moonshine Canyon
Angel Canyon
Poplar Spring
East Fork Oregon Canyon Creek
Buck Corral Canyon
West Fork Oregon Canyon Creek
Burro Spring
Ninety Five Reservoir
McDermitt Well Number 2
McDermitt Well Number 1
Bowden Waterhole
Simpson Creek
Fish Creek
Blue Mountain Draw
Bedground Reservoir
Short Draw Reservoir
Ledge Rock Reservoir
North Blue Reservoir
Ripplebrook Ranger Station (historical)
Ripplebrook Pond
Ripplebrook
Timber Lake Job Corps Center
Indian Henry Recreation Site
Mitchell Ranch (historical)
Rock Creek
Hot Spring
Bryson Spring
McCormick Ranch
Boghole Spring
Deafenbough Reservoir Number 2
Flattop Reservoir
Myers Waterhole
State Section Spring
Juniper Spring
Seep Spring
Myers Well
Little Queen Mine
Flattop
Harper Spring
Battle Creek Ranch
Isaac Canyon Spring
Woolhawk Reservoir
Tree Spring
Cherry Well
Box Canyon
Pole Creek Basin
Pole Creek Reservoir
The Difficulty
The Homestead Cabin
Dry Lakes
Deacon Crossing
Deacon Reservoir
State Line Reservoir
Dry Pit Lake
Deacon Field
Soldier Meadows
Sheep Creek Reservoir
Oregon Hill Reservoir
Northwest Oregon Hill Reservoir
South Oregon Hill Reservoir
North Oregon Hill Reservoir
Oregon Lake Reservoir
Oregon Lake Creek Reservoir
Beaver Charlie Breaks
Beaver Charlie Cabin
South Toppin Butte Pit
West Pasture Reservoir
Road Reservoir
Section Sixteen Reservoir
Harvey Cracker Reservoir
Bull Flat
Boundary Fence Reservoir
Bankofier Reservoir
Little Louse Canyon Spring
Bankofier Spring
Hot Spring Hills
Little Louse Canyon
Wood Spring
Chest Canyon Reservoir
Dry Corner Reservoir
Albisu Reservoir
Twomile Reservoir
Tenmile Ranch
Chicken Springs Canyon
Deadhorse Canyon
Mud Spring
Sugarloaf
Cottonwood Creek
Sunflower Canyon
High Peak
Cottonwood Spring
Upper Tenmile Reservoir
Jackson Summit Reservoir
Middle Fork Jackson Creek
North Fork Jackson Creek
Potato Water Spring
Jasper Spring
Bull Creek Reservoir
Oregon Lake Creek
Bull Creek
Sharon Creek Reservoir
Sharon Creek
Canyon Reservoir
Jackson Summit
Jackson Creek Ranch
Jackson Creek Spring
Callahan Place
Cathcart Place
Pole Creek Well
Colossal Reservoir
Long Canyon
Rawhide Pocket
Still Place
Rawhide Springs
Juniper Creek
Cave Creek
South Drummond Basin Reservoir
Drummond Basin
Five Bar Reservoir
Lower Drummond Waterhole
Upper Drummond Waterhole
Lower Crossing Big Antelope Creek
Brown Spring
Big Antelope - Pole Creek V
Overtime Reservoir
Dry Lake
Dry Lake Reservoir
Big Antelope Canyon
The Butte
Twin Springs Gorge
Brown Ridge
Whiskey Gulch
South Cross Canyon
Half Way Tree
North Cross Canyon
Five Bar
Goat Creek Reservoir
High Ridge Reservoir
Pug Allen Spring
Rocky Road Reservoir
Upper Bend Big Antelope Creek
Lucky Seven Reservoir
Brown Place
Lucky Seven Cow Camp
Steer Canyon Creek
Ballhizer Ridge
Anacabe Field
Echave Reservoir
Rock Spring
Mud Spring
Hole-in-the-Ground
Trail Creek Reservoir
Maiden Spring
Chicken Springs
Little Rattlesnake Creek
Little Antelope Creek
High Ridge
Horse Brush Reservoir
Flat Tire Reservoir
Lower Deer Creek Reservoir
Fearless Reservoir
Little Snake Reservoir
Rattlesnake Reservoir Number 2
Little Hole Reservoir
Lost Fork Reservoir
Hayes Hill
Link Creek
Cross Dike
Running Y Ranch
Double Creek
Whispering Falls Recreation Site
Phelps Creek
Diamond Mill OHV Staging Area
Jones Creek Campground
Ax Ridge
Archer Pond
Bonnie Creek
Dorgan Creek
Billy Lake
John Horton Canyon
Stakely Canyon
Spring Canyon
Rock Canyon
Michaels Creek
Short Jake Creek
Howard Branch
White Trail Well
McGinnis Ridge
Black Butte Lake Reservoir
Airplane Reservoir
Pigeon-toe Lake
South Willow Creek Butte Reservoir
Star Valley Knoll
East Side Reservoir
Rabbit Run Reservoir
Kimble Ridge Creek
Hatchery Creek
Creel Hill
Salmon Lake
Hambone Spring
High Rock Spring
Frazier Turnaround Campground
Rock Lakes Basin
Dinner Ridge
Ellmaker Creek
Goat Ridge
Beaver Creek
Austin Creek
Baldy
Bevens Creek
Little Creek
Big Elk Valley
Chapel of the Valley
Taylor Ridge
Leverage Creek
Chinquapin Ridge
Crawford Canyon
Cline Creek
Strom Boulder Ridge
Baker Creek
Rail Creek
Prindel Creek
Lord Creek
Taylor Ridge
Failor Ridge
Tombstone Pass
Toll Creek
Storm Creek
Rhodes Rearing Pond
Ayers Lake
Upper Drift Creek Slide
South Fork Drift Creek
North Fork Drift Creek
Oregon Hatchery Research Center
Burro Creek
Marking Corral Canyon
Middle Canyon
Coffee Creek
East Basin
Catlow Peak
Marking Corral Spring
Burro Spring
No Name Spring
Government Corral
Rock Cabin Creek
Stony Spring
Sagehen Spring
Horseshoe Corral
Amos Spring
The V
Rosebriar Canyon
Rosebriar Creek
Rosebriar Spring
Little Cole Spring
Lonely Reservoir
Stony Spring Reservoir
Dry Lake Reservoir
Cove Canyon
Pole Canyon
Little Table Seep
Stewart Reservoir Number 2
Stewart Reservoir Number 1
Grey Spring
Sheep Camp Spring
Pole Patch Springs
Center Ridge
Mahogany Ridge
Alkali Spring
Pole Patch
Smith Spring
Tadpole Spring Reservoir
Payne Reservoir
Chicken Spring
Evan Reservoir
Turner Spring Reservoir
Lower Boney Reservoir
Disaster Peak Reservoir
Turner Spring
Turner Reservoir
Upper McDermitt Creek Reservoir
Dunn Ridge
Ring Orchard
Fort Hoskins Spring
Bonner Lake
Foster Creek
Lick Creek
Trail Creek
Letsom Mountain
Beaver Dredge Cut
Palm Hill
Langfeld Creek
Vonberg Creek
The Billboard
Windy Ridge
Windy Gap
Twin Springs Campground (historical)
Landis Cabin
Flat Rock
North Reef
Guinee Reservoir Number 3
Look Reservoir
Upper Sheep Corral Reservoir
Blue Reservoir
Sheep Corral Reservoir
Coffee Pot Reservoir
Withers Reservoir
Boundary Reservoir
Black Hills
Century Ranch
Christmas Valley Lake
Elk Creek Falls
Blue Creek
Saddle A
Boundary Campground
ZX Well
Broken Coffee Pot Waterhole
Four Draws Waterhole
King Dogs Waterhole
Sheep Rock Waterhole
Brattain Waterhole Number 5
West Waterhole
Brownell Spring
Alder Reservoir
Coburns Pond
Fleshman Reservoirs
Hansen Well
Buffalo Well
Boilout Waterhole
Midway Well
South Buffalo Waterhole
Burma Rim
Sand Canyon
Biscuit Point
Keen Waterhole
Brattain Waterhole Number 7
Noble Acres Reservoir
Timothy Reservoir
Flashboard Reservoir
Todd Reservoir
Koch Ranch
Devils Flat
Manzanita Creek
Green Peter Peninsula
Lake Fork West Owyhee River
Bend Spring
Cold Spring
Horse Hill Spring
Lime Spring
Spare Spring
Jack Creek Spring
Pedroli Spring
Indian Spring
Cat Spring
Andersons Corral
Steamboat Ranch
Baker Flat
Cold Springs Creek
Two by Four Creek
Slide Creek
Carlton Prairie
Camp Five Ridge
Guerin Prairie
High Prairie
Bray Ridge
Ash Flat
Bear Pan Flat
Thompson Flat
Russian Mike Creek
Star Mountain
Blue Jay Mine
Little Dixie Creek
Murphy Canyon
County Line Canyon
Shirley Gap
Cluster
Brothers
Sisters
Lone Rock
Red Rock
Brown Rock
Gull Rocks
Pelican Rock
Couplets
Hump Rock
Diver Rock
Yellow Rock
Square Rock
Morrison Hole
Tide Rock
South Coast Log Pond
Oregon Coast Log Pond
Green Rock
Harris Beach
Lone Ranch Beach
Rainbow Rock
Bell Rock
Davidson Spring
Henkin Pond
Deer Creek
Bull Run
Geary Spring
Deer Creek
Martin Creek
Schoolhouse Spring
Dalton Point
Pillars of Hercules
Upper Latourell Falls
Dorena Bridge
Claire Prairie
Winnie Prairie
Fisher Prairie
Griffing Prairie
Delate Creek
Triangle Creek
Beaver Point
Punchbowl
Twin Rocks Shelter
Wildhog Mine
Crystal Lake
Evening Star Mine
Vesuvius Mine
Walton Creek
Mineral Recreation Site
Star Mine
Star Rock
Knott Creek
Gertrude Shelter
Silver King Lake
Lloyd Creek
Hand Ridge
Winburn Mountain
Virgin Flat
Three Corners
Gregory Loop
Mill Creek Plantation
The Flats
Y Creek
Mudusa Flat
Bull Gap Creek
Panther Peak
Yank Gulch Gap
Goose Creek
Kerby Reservoir
Wildcat Canyon
Jackson Hot Springs
Miller Ranch
Granite Street Reservoir
Crowson Reservoir
Black Swan Lake
Meyer Memorial Lake
Buffalo Flat
La Marre Reservoir
Dunn Butte
Clawson (historical)
Corp Reservoirs
Merriman Reservoir
Weasel Creek
Billings Reservoir
Belleview
Ropers Bunion
Roca Canyon
Clay Creek
Clawson Curve
Oregon Tourism Safety Rest Area (historical)
Lamb Saddle
Quartz Creek
Henley Middle School
Henley High School
Mazama High School
Altamont Elementary School
Klamath County Fairgrounds
Stearns Elementary School
Number One C-Drain
Salmon Creek
Gravel Creek
Arnold Creek
Spring Branch
Lewisburg Saddle
Wood River Valley
Chiloquin Ranger Station
Schoolhouse Lake
Carlon Ranch
Buckhorn Spring
The Rosebud
Turner Place
River Ranch
Lost Cabin
Thousand Springs Ranch
West Fork Feagles Creek
Connors Camp Recreation Site
Straus Reservoir
Korner Reservoir
Koellner Reservoir
Nelson Reservoir
Harrison Reservoir
Ken Denman State Game Management Reserve
Modoc Slough
Upton Lateral
Coker Butte Lateral
Petrehn Reservoir
Table Rock Canal
Modoc Reservoirs
Cliff Creek
Zana Creek
Hidden Valley
Gold Gulch
Salmon Rock
Table Rock Station (historical)
Morris Reservoir
Dean Reservoir
Hixson Reservoir
Bommers Flat
Panther Gulch
Agate (historical)
Modoc Pond
Schlesinger Reservoir
Brown Reservoir
Nelson Mountain
Nelson Meadow
Owl Gulch
House Mountain
The Maples Safety Rest Area
Talent Middle Canal
Buckhorn Gulch
Hefferman Reservoir
Medford Nursery Rogue River National Forest
Perrydale (historical)
Bybee Corner
Martin Reservoir
Britt Garden County Park
Minear Reservoir
Goodrich Reservoir
Nelson Reservoir
Camp Baker (historical)
Kane (historical)
Crooked Creek
Larson Creek Reservoir
Gas Works (historical)
Lowry Reservoir
Hilldale Reservoir
Holmes Reservoir
Francis L Reservoir
Gammill Reservoir
Rogue Valley
Sevenmile Ditch
Lower Sevenmile Ditch
Blue Springs Ditch
Threemile Cinder Pit
Enos Creek
Watkins Pond
Tatum Creek
Connection Creek
West Ridge
Hunter Creek
Deets Creek
Flory Spring
Bernstein Spring
Spring Creek
Grouse Flat
Gregg Spring
No Business Creek
Grays Gulch
McGee Spring
Sexton Mountain Pass
Thielsen Camp
Threemile Quarry
Ponderosa Picnic Area
Cedar Spring
Arch Rock
Beehive Rock
Saint Patricks Rock
Michigan Pass
Little Salander Creek
Salishan Spit
North Lagoon
South Lagoon
Round Mountain
Bald Butte
Lorane Mountain
Hawley Ridge
Maxwell Creek
Green Ridge
Mill Camp
Dead Ox Creek
Clearwater Powerplant Number 1
Watson Saddle
Deer Creek Diversion Dam
Davey Creek
No Tunnel Creek
Fish Creek Canal
Clearwater Canal Number 2
Cinder Prairie
Slide Creek Powerplant
Lemolo Powerplant Number 2
Ringtail Pond
Fish Creek Powerplant
Toketee Powerplant
Clearwater Powerplant Number 2
Watson Ridge
Lemolo Canal Number 1
Cascade Falls
Gobblers Knob
Harry Mountain
South Fork Packers Gulch
Maple Creek
Crash Creek
Twin Falls Creek
Sixes Creek
Edison Creek
Galena Ridge
Red Heifer Pass
East Fork Packers Gulch
Cave Creek
Elk Creek
Beverly Creek
Doe Creek
Rachel Creek
Fawn Creek
Dailey Creek
Clearwater Creek
Carpenter Creek
Oxbow Burn
Muddy Lake
Clear Creek
Johnson Creek
New Lake
Dome Spring
Mutton Meadow
Mac Creek
West Fork Tumblebug Creek
Chuckle Springs
Royal Creek
Fizz Creek
Indigo Springs
Sacandaga Recreation Site
Millie Creek
Shelter Creek
Kline Creek
Cabin Creek
Rujada Recreation Site
Bedrock Recreation Site
Clark Creek Group Camp
Broken Bowl Recreation Site
Winberry Recreation Site
Kiahanie Recreation Site
Manzanita Safety Rest Area
Oak Mine
Brush Prairie
Eightmile Prairie
Pacific High School
Saddle Rock (historical)
Koch Creek
Jenny Creek
Little Dry Creek
Poverty Ridge
Mill Creek
Suncrest Point
Jackass Creek
Iron Gulch
Blanket Ledge Mine
Gypsy Queen Mine
Red Rock
Sundown Prairie
Hunter Creek Bog
Parker Reservoir
Little Dome Creek
Avery Creek
West Fork Ella Creek
Hortense Creek
Upper Bennett Dam
Blacktail
Hawthorne Elementary School
Pleasant Valley
Berlin
Mills Bridge
The Dam Hole
Sheridan Creek
Trask River State Fish Hatchery
Bill Creek
The Peninsula
Stones Gap
Fish Corner
Blue Ridge
Sylvan Creek
The Blue Hole
Ming Creek
Ming Point
Bass Arms
Butterfly Lake
Jewitt Island
Carter Lake Creek
Merriam Cemetery
Rumley Hill Cemetery
Pickle Ranch
Coldiron Camp
Johnson Prairie
Pedro Gulch
Rumley Hill
Dobry Point
Bessie Shelter
Little Billie Creek
Saddle Campground (historical)
Whalen Island
Watson Draw
Sedora Well
Small Ranch
Klippel Point
Klippel Well
Johnson Creek
Johnson Creek Spring
Hinton Well
Hale Well
Harney Well
Deadhorse Spring
Swanton Well
Pattern Reservoir
Flatiron Point
Rock Lake
Juniper Lake
O'Leary Reservoir Number 3
Sheeplick Lake
New Waterhole
Muddy Waterhole
Guinee Reservoir Number 1
Peter Creek Reservoir
O'Leary Reservoir Number 1
Guinee Reservoir Number 2
Big Reservoir
Double Prairie
Hilltop Prairie
Brushy Prairies
Wilson Prairie
Hells Gate
Oneonta Gorge
Wahkeena Spring
Snow Bird Mine
Klippel Place
Twin Lakes
Fish Hatchery County Park
Kelli Slough
Randa Slough
Kerry Slough
Jones Beach
Ludviksen Slough
Whiskey Joe Slough
Hanna Mine
Haystack Reservoir Recreation Site
Crooked River Ranch
Meralle Spring
Devils Backbone
Arizona Beach
White Pine Lake
Cold Spring
Christis Spring
Pothole Well
Sunnydale
Whisky Camp (historical)
Mosser Mountain
Takelma County Park
Betts Hole
Canfield Riffle
Canfield Bar
Coyote Riffle
Coyote Bar
Wakeman Riffle
Wagontire Prairie
Gillespie Riffle
Libby Creek Pond
Ferguson Pond
Jimmy Davis Riffle
Thoms Point
William Miller Creek
Hawkins Riffle
Salt Spring
Fry Peak
Bear Wallow
Lick Creek
Elderberry Flat Recreation Site
Elderberry Creek
Horse Mountain
Cedar Creek
Peavine Ridge
Milo Adventist Academy
Dry Lakes Flat
Joe Gulch
Brown Res
Jamison Creek
Ruch Gulch
Ninemile Peak
Jim Mee Peak
No Name Creek
Bear Wallow Creek
Cinnabar Mountain
McKee Bridge
Palmer Ridge
O'Brien Spring
Mud Spring
Matney Gulch
O'Brien Gulch
Little Rackheap Creek
Joes Rock
Bean Cabin
Porcupine Reservoir
Dollarhide (historical)
Dollarhide Curve
Barrats Reservoir
Green Mountain
Foliage (historical)
Wall Creek (historical)
Soda Spring (historical)
Pine Spring Canyon
Pine Spring
Box Spring Reservoir
Juniper Spring Reservoir
Umbrella Pine Reservoir
Sage Hen Hill Reservoir
Military Reservoir
Pine Spring Canyon Reservoir
Twin Lakes
Blackie Butte
Twin Reservoirs
Powerline Reservoir
Bentonite Reservoir
Sundown Ridge
Lilly Prairie
Lennox Gulch
Norling Gulch
Marshall Gulch
Miller Mountain
Sailor Gulch
Rail Gulch
Baldy Mountain
Bunny Meadows
Westwood Village
Boulder Ridge
Snive Creek
Chief Creek
Manzanita City Park
Cascade Experimental Forest Headquarters
Neskowin Beach State Recreation Site
Harts Cove
Sanders Creek
Deep Creek
Dawson Creek
Webb County Park
Fisher Landing
Upton Creek
Coleman Creek
Baughman Creek
Oceanside Beach State Recreation Site
Cape Meares Lighthouse
Agate Beach
Hodgdon Creek
Dry Stocking Island
Snag Island
Frank Wade Park
Olson Creek
Center Slough
Sallys Slough
Weiser Point
The Bend
McCaffrey Island
North Fork Elkhorn Creek
Sallys Bend
Nonpareil Mine
English Settlement
Determination Creek
Camp Wilani
Clay Hill
Stoney Point
Star Camp
Elk Prairie
Green Mountain
Warden Creek
Point Adams
Shortridge Creek
Willamette Fish Hatchery
Oakridge Fish Hatchery
Larison Cove
CT Beach Recreation Site
Stony Cove
Recreation (historical)
Pelican Cut Canal
Pelican Cinder Pit
Mountain Lakes Organizational Camp
Long Rifle Cinder Pit
Odessa Cinder Pit
Odessa Recreation Site
Agate Beach
Port Orford Heads State Park
Linslaw Cemetery
Heceta Lodge Number 11 IOOF Cemetery
Gardiner Cemetery
Holy Rosary Cemetery
Lakeside Cemetery
Elk City Cemetery
Maplewood Cemetery
Prairie Cemetery
Pacific View Memorial Gardens
Dement Cemetery
Essen Family Cemetery
Apiary Cemetery
Central Point IOOF Cemetery
Griffin Creek Cemetery
Rock Point Cemetery
Gold Hill IOOF Cemetery
Maderis Grave
Eugene Masonic Cemetery
Mount Calvary Catholic Cemetery
Jackson Family Cemetery
Heatherly Cemetery
Rest Lawn Memorial Park
Whitcomb Island Cemetery
Huckleberry Knoll Cemetery
Gunter Cemetery
Fox Hill Cemetery
Wiley Cemetery
Merrill IOOF Cemetery
Phoenix Cemetery
Eastwood IOOF Cemetery
Davidson Cemetery
Crow Family Cemetery
Denmark Cemetery
Wigle Cemetery
Riverside VFW Cemetery
Taylor Cemetery
Falls City Odd Fellows Cemetery
Bay City IOOF Cemetery
Fall Creek Christian Church Cemetery
Our Lady of Lourdes Catholic Cemetery
Nortons Cemetery
Leslie Cemetery
Shotpouch Cemetery
Mays Strouts Cemetery
Claremont Cemetery
Spring Family Cemetery
Quines Creek Cemetery
Hells Gate
Gold Run Creek
Lookout Springs Campground (historical)
Cat Creek
Grouse Creek
Shining Lake Campground
Shining Creek
Sheepshead Rock
Three Week Spring
Coffeepot Spring
Exchange Spring
Horse Hill Reservoir
Lower Bell Spring
Chipmunk Reservoir
Chipmunk Creek
Steer Canyon Reservoir
Chipmunk Spring Reservoir
Chipmunk Spring
Chipmunk Basin
Bend-of-Pole Creek
Trobough Spring
Lobster Riffle
Lobster Creek Bridge
Scow Riffle
Jennings Riffle
William Miller Riffle
Turner Spring
South Highline Canal
South Main Canal
Gold Hill Irrigation District Canal
Evans Creek Lateral
Tokay Canal
Boyd Creek
South Fork Trimble Creek
Seaman Bar
Martin Spring
Fall Creek
Bee Creek
Foots Creek
Reservoir Gulch
Valley of the Rogue State Park
Bear Gulch
Little Bald Spot
Big Bald Spot
Owl Hollow
Shasta Mine
Cold Springs Creek
Cold Springs Reservoir
Domestic Spring
Crystal Spring
Shady Spring
Miller Mine
Eads Gulch
Watts and Topping Ditch
Bridgepoint Ditch
Johnsons Gulch
Cook Cove
Williams Creek (historical)
New Berryman Ditch
Left Fork Balls Branch
Oliver Creek
Sandpiper
Swede Fork Eckman Creek
Eckman Lake
Day Drainage Ditch
Quillwort Pond
Lodgepole Picnic Area
Stuart Falls
Red Blanket Falls
Lucky Meadows
Tom Mountain
Little Canyon Creek
Tyee Mountain Recreation Area
Hurst Family Cemetery
Blachly Lane Picnic Area
Narrows
Blue Bus Creek
Trask River Rearing Pond
The Crawdad Hole
Coal Creek Reservoir
Clarks Bar
Caufield Bar
Rock Spring
Cable Hole
Trail Creek Riffle
Boil Hole
Flood Rock
Old Mill Site Park
Hee Hee Illahee Park
Trout Cemetery
Balmer Hill
South Prairie
Tillamook Junior High School
Tillamook IOOF Cemetery
Trask Fairview Pioneer Cemetery
Sacred Heart Cemetery
Dick Point Dike
Sand Island
Silver Sands
Marie Creek
Barretts Landing
South Jetty
Umpqua River Lighthouse
Karlstrom Creek
Alpha Creek
Fawn Creek
McGuire Cemetery
Squaw Creek
Mount Obette
Cox Cemetery
Grassy Point
Green Point
City of Toledo Watershed
The Hogback
Strawberry Mountain
Sunny Ridge
Peterson Ridge
Mills Riffle Reservoir
Bellamy (historical)
Government Hill
Whitehouse Spring
Abbott Burn
Anvil Lake
Meditation Point
Strawberry Hill Picnic Area
Little Beamer Creek
Camp One (historical)
Camp Angell
Charles Applegate House
Camp Florence
Waldo Meadows
Islet Point
Dans Lake
Fields Lake
North Waldo Recreation Site
Jewell Meadows State Wildlife Management Area
Grand Rapids
Vinemaple Bridge
Boiler Ridge
Jewell Cemetery
Bolton Hill
Rocky Butte
Central Cemetery
Mounse Burial
Perkins Peninsula
Oak Island Park
Fern Ridge Shores
Demming Ridge
Richardson Cemetery
Richardson Point
Orchard Point
Howell Pond
Weltman Reservoir
Lane and Shephard Reservoirs
Military Slough Reservoirs
Crater Canal
Hoover Ponds County Park
Cable Reservoir
Stimpson Gulch
Eagle Point
Veterans Affairs Domiciliary
Rattlesnake Rapids
Jackson County Sports Park
Agate Lake County Park
Wellen (historical)
Dunlap Reservoir
Graves Reservoir
Ferber Reservoir
Cedar Pond
Kings Reservoir
Katzenbach Reservoir
Fiddlers Gulch
Williamsburg (historical)
Maple Springs Gulch
Holzhauser Reservoir
Remey Reservoir
Miller Reservoir
Trader Reservoir
Sunflower Gulch
Stone Sumps
FS Reservoir
Jones Marble Quarry
Red Rose Mine
Bear Trap Gulch
Oak Gulch
Neathammer Gulch
Miller Gulch
Devils Garden
Bokel Gulch
Cherry Flat
Lover Peak
Blair Reservoir
Fawn Spring
Fawn Creek
Lover Gulch
Carter Gulch
Williams and Whalen Ditch
Coker Gap
Jackson Reservoir
Zwan Reservoir
Shephard Basin Reservoir
Badcock Reservoir
Vroman Ditch
Steppe Reservoir
Rogue Community College
Robertson Bridge County Park
Arden Craig (historical)
Griffin County Park
Klose Pond
Lathrop County Park
Jerome Prairie Lateral
Jerome Prairie (historical)
Daily Reservoir
Chapin Creek
Wee Bonnie Loch Glen Reservoir
Klovdahl Creek
Edith Creek
Shadow Bay
Jo Ann Lake
Black Meadows
Chapman Creek
Buck Flat
Canon Creek
Coal Creek
Wolf Creek
Cold Spring
Railroad Gap Creek
Constants Creek
Mineral Creek
Hunt Reservoir
Patillo Ditches
Cinnabar Mountain Mine
War Eagle Mine
Schmidt Reservoirs
Chirgwin Reservoir
Wanoga Siding (historical)
Gates Reservoir
Todd Reservoir
Hammel Reservoir
Sims Reservoir
Humphrey Reservoirs
Robinson Reservoir
The Drain
Sparrowhawk Creek
Nelson Divide
Lils Lake
Arrowhead Lake
Hidden Lake
Bonnie Lake
Apple Rogue Reservoir
Ball Spring
Karen Lake
Timberline Lake
Gold Lake Sno-Park
Waldo Lake Sno-park
Eagle Rock
Sow Bug Lake
Soda Springs Power Plant
Marsters Bridge
Illahee Flats
Bear Camp
Boulder Creek Wilderness
Reynolds Shelter
Bingham Recreation Site
Youngs Rock
Butcherknife Creek
North Fork Indian Creek
Roberts Reservoirs
Coffee Creek
Lunch Creek
Cedar Creek
Oasis Creek
First Creek
Third Creek
Second Creek
South Fork Mountain
Shovel Creek
Wanderers Creek
Silk Creek
Gingham Creek
Cotton Creek
Wool Creek
Tweed Creek
Homestead Creek
North Falls
Niagara County Park
Silver King Mine
Packsaddle County Park
North Eel Campground (historical)
Salmon Falls County Park
Saunders Creek
Hatchery Creek
Robertson Creek
Cheyenne Creek
Franklin Ridge
Decker Ridge
Hells Canyon
Ridenour Creek
Bunker Hill
Branch Creek
Camp Creek
Gopher Ridge
Cape Horn
Cape Horn Ridge
Jackass Creek
Fairview Elementary School
Sacred Heart Academy (historical)
Joseph Conger Elementary School
Pelican Elementary School
Keno Canal
Klamath Falls
O'Neill School (historical)
Fairhaven
Reames Country Club
Oregon Institute of Technology
Bones Creek
Buckhorn Creek
Moser Pond
Pigeon Creek
Coon Creek
William Creek
Long Canyon Creek
Hays Creek
Cedar Creek
Dutch Creek
Millers Gap
Indian Gap
Steer Divide
Bailey Creek
Granite Canyon
Fisher Creek
Goat Knob
Blogett Creek
Humphrey Creek
School Hill
Tater Hill
Junction Reservoir
Isaac Canyon
Dawson Reservoir
Little Arrow Reservoir
Big Arrow Reservoir
Deer Creek Spring
Shearing Corral Spring
The Basin
Wild Rose Spring
The Water Fall
Hoppin Springs
Chato Spring
Chino Homestead (historical)
Edge Spring
Rock Creek
Lowry Canyon
Marie Lake
Goose Pasture
Waxmyrtle Recreation Site
Wimble Pass
Little Fall Creek Picnic Area
Fall Creek Reservoir State Park
Upper End Campground
Sky Camp
Gunn Creek
Black Tank Saddle
Joes Spring
Battle Mountain Reservoir
Deadhorse Spring
Muley Spring
Upper Rattlesnake Reservoir
Black Rock
Black Rock Spring
Willow Spring
Ryder Creek
Stokes Creek
Starks Creek
Fiddle Creek Ridge
Henderson Canyon
Big Canyon
Wildcat Ridge
Powderhouse Hole
Ellingson Creek
Sweet Creek Falls
Beaver Creek Falls
Rocky Point
Mules Ear Reservoir
Blue Mountain Reservoir Number 8
Sylvester Spring
Cascade Spring
Dead Cow Spring
Chest Canyon
Wood Canyon
Juans Forty
Bull Canyon
Morris Creek
Straddle Creek
Russian John Gulch
Noel Ranch Recreation Site
Smith River Marina
North Fork
Horse Gulch
Sulphur Creek
Green Springs
Murphy Creek
Sweathouse Canyon
Tom Spring Mountain
Chapman Lake
Black Rock
Rattlesnake Point
White Oak Spring
Middle Spring
Edwards Canyon
Rose Flat
Henry Ranch
Big Prairie
Little Prairie
Dosier Creek
Walker Sheep Camp
Little Craggy
Big Craggy
Canyon Ridge
Dosier Flat
Cold Spring
The Slide
Tom Spring
Bill Willis Flats
Henry Mountain
Hooper Meadows
School House Meadow
Cove Ranch
Big Creek
Acey Field
Salt Ridge
Bounds Reservoir
Burns Gulch
Barron Mine
Round Mountain
Right Fork Sampson Creek
Major Butte
Songer Wayside
Emigrant Lake County Park
Wagner Soda Spring
Barron (historical)
Emigrant Channel
Baber Butte
Pioneer City (historical)
Petite Creek
Lucas Lake
The Parks
Headquarters Camp Creek
Joes Creek
Cabinet Creek
Currin Bridge
Stewart Bridge
Taft Prairie
Coal Creek
Hooker Creek
Suicide Rock
Pyramid Rock
Ben Grant Ridge
Wilson Prairie
Horror Spring
Hutton Spring
Animal Bedground
Two by Four Well
Poor Jug Well
Venator Butte
Poverty Corners Waterhole
Saunders Well
Rim Waterhole
Knob Waterhole
ZX Reservoir Number 1
Brattain Reservoir Number 8
Brattain Reservoir Number 11
North DC Waterhole
Horse Mountain Well
Poverty Basin
Poverty Basin Well
Saunders Waterhole
West Saunders Waterhole
South DC Waterhole
Depaoli Lake
Saunders Rim
Fire Lake
Snipe Waterhole
Brattain Waterhole Number 5
Brattain Waterhole Number 4
ZX Waterhole Number 2
Camp Tank Waterhole
Diatomite Reservoir
Sammys Horse Pen Waterhole
Little Lobster Summit
Salmonberry County Park & Campground
Campbell County Park
Frozen Creek Mine
Wickiup Mountain
Sylvanite Mine
Lyman Mine
Kane Creek
Kell Mine
Jorden Creek
Gold Nugget County Recreation Area
Dillon Falls
Hardy Riffle
Granger Reservoir
Harris Gulch
Vincent Reservoirs
Wiwona Reservoir
Colvig Gulch
Estramado Reservoir
Gold Gulch
Little Giant Mine
Anderson Mine
Molly Mine
Pikes Peak
Dry Creek
Pony Bridge
Gleason Creek
Wildwood Falls
West Fork Williamson Creek
Klickitat Quarry
Cummins Peak Weather Station
Grizzly Ridge
Lawrence Creek
West Branch North Fork Siuslaw River
Taylor Creek
Deadman Creek
Deer Creek
Right Fork Drew Creek
Drew Ridge
Left Fork Wilhelm Creek
Garden Lake
Spencer Butte Park
Coyote Creek Bridge
Applegate Elementary School
Crow Hill
Agency Straits
Central Canal
Vidae Creek
Lawnridge Park
Croxton Pioneer Memorial Park
Fruitdale
Flannel Creek
Westholm Park
Josephine County Fairgrounds
Tom Pearce County Park
Spaulding Reservoir
Tokay Heights Cemetery
George H Eckstein Park
Riverside Park
Jewett Mine
Spring
Hawthorne Memorial Gardens Cemetery
The Twins
Chitwood Spring
Black Canyon
Lone Wolf Shelter
Scout Lake
Windy Pass
McLane Creek
Cooper Creek Reservoir Park
Otey Cemetery
Umpqua Community College
Youtlkut Pillars
Horn Prairie
Redman Creek
Skamokawa Channel Range
Fales Channel
Puget Island Range and Turn
Welch Island Reach
Little Crater Recreation Site
East Lake Recreation Site
Hot Springs Recreation Site
Cinder Hill Recreation Site
Hambone Springs Campground (historical)
High Rock Creek
Camp Victoria
Big Antelope Creek
Brewster Reservoir Number Two
Broken Rim Check Dam
Cemetery Lake
Hamar Lake
Hanson Flat
Houston Lake
Jim Fisk Creek
Little Steer Creek
Low Line Canal
Masiker Canyon
Masiker Mountain
Melton Creek
North Fork Swayze Creek
Olallie Creek
Bowman Dam
Hog Island
Myrtle Point Log Pond
Oregon Mine
Broken Rim Reservoir
Calf Ranch Prairie
Clatsop Spit
Walker Prairie
Bacona
Colony Ranch
Elk Butte
Hay Lake
Ladycomb Peak
Pickett Butte
Round Top Butte
Schaub Lake
Stinking Lake
Three Forks
Tired Horse Butte
Windy Point
Keeney Point
Pilot Butte
Alec Butte
Baker County
Clatsop County
Columbia County
Coos County
Douglas County
Gilliam County
Grant County
Harney County
Jackson County
Lake County
Lane County
Lincoln County
Linn County
Malheur County
Marion County
Morrow County
Multnomah County
Polk County
Sherman County
Tillamook County
Wheeler County
Yamhill County
South Channel
Coyote
Hayden Bay
Vancouver Upper Channel
Port of Portland Berth 301
Portland Yacht Club
Fisher Quarry Channel Range
Morgan Turn
Marquam Bridge
Port of Portland Berth 206
Port of Portland Berth 304
Port of Portland Berth 205
Port of Portland Berth 303
Port of Portland Berth 302
Berth One (historical)
Port of Portland Berth 308
Port of Portland Berth 204
Port of Portland Berth 203
Berth Two (historical)
Port of Portland Berth 307
Port of Portland Berth 306
Port of Portland Berth 305
Government Island Upper Range
Government Island Range
Rooster Rock Channel
Cascade Rapids Lower Range Light
Buchmans Landing (historical)
Mount Pleasant
Trotter Point
Tanner Creek Fishway
Entrance to Bonneville Lock
Multnomah Falls Bar Range
Airport Bar
Government Island Lower Range
Government Island Middle Range
Smith Hill
North Channel
Slaughters Dike
Dribblee Dike
West Rainier
Eureka Upper Channel
Oak Point Channel
Eureka Lower Channel
Walla Walla Valley
Warm Springs Canyon
Brookling Creek
Stark Reservoir
White Pine Trough Spring
Wildcat Recreation Site
Lone Pine Quarry
Steamboat Reach
Multnomah Channel
Sunset Beach
Carson Heights
Kellogg Park
Lakewood
Bingham Landing
Starweather Landing
Port Orford
Ocean Park
Yaquina Reef
South Reef
Guano Rock
Tituna Spit
Ocean Lake Park (historical)
Shorter Creek
Nostoc Creek
Cold Creek
Sparlin Cemetery
Eighteen Creek
Seventeen Creek
Westport Turn and Range
Washburn (historical)
Axford (historical)
Mineral (historical)
Abrams
Ace Williams Mountain
Adams Point
Adrian
Advance
Aemisegger Hill
Akerson Butte
Albina
Alderman Butte
Aldervale
Algoma
Alkali Buttes
Alpine
Alston
Alton Hill
Alvadore
Ambrose Hill
Amelia (historical)
Anderson (historical)
Angora Peak
Anlauf
Apex
Arcadia
Ardenwald
Ardgour (historical)
Arleta
Arnaud (historical)
Arrowhead Butte
Ash Butte
Ashdale (historical)
Auburn (historical)
Augustine Gilbert Place
Awbrey
Bade
Badger Corner
Bailey Junction
Bakeoven
Bald Hill
Bald Hill
Bald Mountain
Bald Mountain
Bald Mountain
Bald Mountain
Baldy
Baldy Mountain
Ball Bearing Hill
Barnesdale
Barnett Knoll
Barnhart
Barrett
Basque
Basque Hills
Batterson
Battin
Battle Mountain
Bay Park
Bayocean (historical)
Bear Creek Buttes
Bear Wallows
Beaver Creek
Beaver Homes
Beaver Mountain
Beaver Springs
Beavertail Butte
Belding (historical)
Belfort (historical)
Belknap Springs
Bell
Bellfountain Junction
Bellinger Hill
Bellrose
Ben More Mountain
Bethel
Bethel
Bethel Gospel Park
Bethel Heights
Beulah
Big Baldy
Big Dutchman Butte
Big Hill
Bill Neighbor Peak
Blachly
Black Butte
Black Butte
Black Butte
Black Butte
Black Butte
Black Hills
Black Place
Blaisdell
Blakeley (historical)
Blue Buck Mountain
Blue Mountain Pass
Boardman
Bolton
Bonita
Bonny Slope
Boomer Hill
Bourbon (historical)
Bourne
Bowden Hills
Bradwood (historical)
Brady Butte
Brewster (historical)
Briarwood
Brockway
Brookwild
Buck Creek
Buck Mountain
Buck Mountain
Buck Point
Buckboard
Buckbrush Poison Butte
Buckhorn Mountain
Bullards
Bunchgrass Butte
Bunchgrass Mountain
Bunker Hill
Bunker Hill
Burns Junction
Burnt Mountain
Butte Creek Summit
Butterfield (historical)
Bybee Springs
Cairo Junction
Calf Ranch Mountain
Calkins
Cambrai
Camp Elkanah
Canemah
Cannon Beach
Cape Horn
Captain Jack
Carey Tables
Carnes (historical)
Carson Point
Cartney
Carver
Castle
Cat Rock
Cayuse
Cedar Hills
Mount Cedara
Cedardale
Cedarhurst Park
Celilo Village
Cemetery Butte
Cemetery Hill
Centennial Butte
Chamberlain Hill
Chandler Mountain
Charleston
Charlestown
Chehalem
Chemawa
Cheney (historical)
Cherry Heights
Chicken Hills
Chimney Rock Butte
Chitwood
Christmas Valley
Cinder Cone
Cinnabar Mountain
Clackamas Heights
Clark Mountain
Clarno
Clatskanie Heights
Clem
Cleveland Hill
Climax
Cloverdale
Coalca
Cobb
Cochran (historical)
Coffin Butte
Coffin Rock
Columbia Hill
Concord
Condenser Peak
Conley
Connley Hills
Conrad Place
Cook
Cooper Mountain
Copeland Place
Corbett
Corey Hill
Cornell Place
Cornucopia
Cotton Butte
Cottonwood Mountain
Cottrell
Cove
Cox Butte
Coyote Butte
Coyote Buttes
Coyote Butte
Coyote Hill
Coyote Hills
Coyote Point
Crane Butte
Crates
Crescent Hill
Cribbins Hill
Criterion Summit
Crockett
Cross Hollows
Currinsville
Curtis
Cutsforth Corner
Dads Creek
Damewoods Place
Danebo
Danner
Davis Hill
De Bord Peaks
Dead Horse Butte
Dead Indian Hill
Deadman Butte
Deathball Mountain
Deer Butte
Deer Butte
Deer Island
Dehlinger (historical)
Dever (historical)
Devils Halfacre
Diablo Peak
Diamond
Diamond Peak
Dickerson Rocks
Dickinson Mountain
Dillard
Dixie
Dixon
Doctor Rankins Place
Doe Mountain
Dole
Donnybrook (historical)
Dora
Double Peak
Douglass Ridge
Dougren
Downing
Duck Pond
Dunnean
Dunthorpe
Durbin (historical)
Durkee
Eagle Crest Corner
Eakin
East Fork First Creek
East Portland
East Saint Johns
Eastmoreland
Echo Dell
Eddy Place
Edenbower
Edwards
Egert Place
Eightmile
Elgarose
Elgarose Creek
Elk Mountain
Elk Mountain
Elk Point
Elk Rock (historical)
Elkhead
Elkhorn Butte
Ella
Ellendale
Elmira
Elrus
Elsie
Emerson
Endersby
Englewood
Englewood
English Mountain
Enid
Erickson Mill
Errol (historical)
Errol Heights
Estacada
Estoos
Fair Oaks
Fairbanks
Fair Oaks
Fairview
Fairview
Fairview Point
Fallsview
Faraday
Fawn (historical)
Fern Hill
Fern Ridge (historical)
Ferndale
Fernwood
Finn
Fir
Firlock
Fisher Butte
Fisk Hill
Flagg (historical)
Flagstaff Butte
Flat Top Mountain
Flint Hills
Fords Mill
Forked Horn Butte
Fort Rock
Fort Stevens
Foster
Four Corners
Freezeout Mountain
Frenchglen
Friends Peak
Froud Hill
Fruitvale
Fry
Fulton
Fulton (historical)
Garden Home
Garfield (historical)
Gateway
Geer
Georges Knob
Gilbert
Gilbert Station
Gladstone
Gladstone Station
Glen Echo
Glenbrook
Glengary
Glenwood
Goble
Golden
Goldson
Golf Junction
Gooch
Gooseberry
Gorham Butte
Goshen
Graham
Granite Mountain
Grassy Butte
Grays Butte
Green Hills
Green Mountain
Green Mountain
Green Mountain
Green Mountain
Green Peak
Green Springs Summit
Green Top
Greenburg
Greenhorn Hill
Greenville
Grey Mountain
Gurdane
Mount Gurney
Mount Hagan
Hager
Haig
Hamlet
Hampton
Happy Valley
Harborton
Hardman (historical)
Harmony
Harmony Point
Harper
Harper Junction
Hart Mountain
Harvey Mountain
Hat Rock
Havana
Hawthorne
Hayesville
Haystack Rock
Hazeldale
Hazelia
Hemlock (historical)
Henley
Hereford (historical)
Hereford
Herrman
Hickland Butte
High Hill
Highland
Hilgard
Hillsdale
Hillsview
Hinkle
Hobart Peak
Hoffer Butte
Hogback Butte
Holbrook
Hollywood
Homly
Hood River
Hoodoo Mountain
Hoodview
Hoover Hill
Hopewell
Hornet Butte
Horse Butte
Horse Mountain
Horsehead Mountain
Horton (historical)
Horton
Hoskins
Hosley
Hot Lake
Hugo
Humbug Mountain
Hutchinson
Indian Crossing
Indian Spring Butte
Inglis
Interlachen
Iron Mountain
Iron Mountain
Iron Mountain
Ironside
Irving
Irvington
Irvinville (historical)
Ivers Peak
Jackson Hill
Jamieson
Jenne
Jennings Lodge
Jewell
Jimbo Mountain
Johnson Hill
Jordan (historical)
Judkins
Jug Mountain
Juniper Mountain
Juniper Mountain
Juntura
K Junction
Kah-Nee-Ta Resort
Kaskela
Keasey
Keel Mountain
Kendall (historical)
Kenton
Keyes Mountain
Keys Mountain
Kidders Butte
Kings Mountain
Kinzua Mountain
Kirkpatrick
Kishwalks
Kittleson Place
Klamath Falls
Klamath Hills
Knappa
Knight (historical)
Knob Hill
Knox Butte
Kopplein (historical)
Krewson (historical)
Kutch Mountain
La Butte
Labish Village
Ladd (historical)
Ladd Hill
Laidlaw Butte
Lampa Mountain
Langdon (historical)
Langell Valley
Latham
Laton Point
Laurel Butte
Laurelhurst
Lawen
Lawson Creek
Lebanon
Lee Thomas Crossing
Lee Thomas Meadow
Lena
Leneve
Lenon Hill
Lenz
Lewis Rock
Lexington
Libby
Lincoln
Lincoln
Lincoln Beach
Linnemann
Linnton
Little Alps
Little Baldy
Little Cowhorn Mountain
Little Edson Butte
Little Elk Mountain
Little Grass Mountain
Little Green Mountain
Little Pilot Peak
Little Valley (historical)
Locust Grove
Logan Butte
Logsden
Lone Pine Butte
Lone Rock Place (historical)
Long Pass
Long Tom
Low Pass
Lookingglass
Lookout Butte
Lorane
Lost River
Lukarilla
Luse (historical)
Luther (historical)
Lyman Mountain
Malheur Junction
Malin
Malone
Manhattan Beach
Maple Hill
Maplewood
Marble Mountain
Marcola
Marlene Village
Marquam
Marquam Hill
Marvin Hill
McConville Peak
McCormmach (historical)
McDonald
McEwen
McEwen Butte
McKay
McKenzie River
McLean Place
McNary
Mecca
Meeker Mountain
Melville
Metzger
Middle Mountain
Middleton
Midland
Midway
Miles Peak
Miller Hill
Miller Place
Millican
Millington
Milltown Hill
Millwood
Milwaukie Heights
Minthorn
Mist
Mohawk Junction (historical)
Monett
Monkland
Morris Hill
Moss Butte
Mount Angel
Mountain View
Mouse Trap Butte
Moyina (historical)
Mulloy
Multnomah
Munley
Munra (historical)
Murry Hill
Narrows
Navy Heights
Nedonna Beach
Nehalem
Nehalem Junction
Nelson (historical)
Nelson Butte
Nelson Place
Nesmith (historical)
New Era
New Princeton
Newport Heights
Nimrod Butte
Nolin
Nonpareil (historical)
North Butte
North Butte
North Portland
North Warner Viewpoint
Norton Hill
Nortons
Norway
Norwood
Noti
Nugget Butte
Nye
O'Neil (historical)
O'Neil Corners
Oak Grove
Oak Grove
Oak Hill
Oak Hill
Oak Springs
Oaks
Oasis Butte
Oatfield Hill
Obenchain Mountain
Olney
Ordnance (historical)
Oregon City
Orient
Ortley
Orville
Outlook
Overstreet
Owyhee
Owyhee Breaks
Pacific City
Palestine
Palisade Rocks
Panorama Point
Panther Rock
Paradise Park
Parker Place (historical)
Parkersburg
Peck
Peel
Pelican City
Pemberton Canyon
Peninsula Junction
Penney Hill
Pernot Mountain
Perry
Petersburg
Pharmacy Hill
Piedmont
Pine
Pioneer
Plank Hill
Pleasant Home
Plum Hills
Plush
Poe Place
Poindexter Place
Poison Creek (historical)
Poison Oak Hill
Polk Butte
Pollard (historical)
Pondosa
Pope Corner
Porter Butte
Portland
Portland Heights
Potato Hill
Powell Butte
Powell Buttes
Powell Hills
Powellhurst
Power City
Powwatka
Prahl (historical)
Prava Peak
Prava Peak Reservoir Number One
Prince Albert
Progress
Prospect Hill
Prosper
Prune Hill
Quartz
Quartz Mountain
Queen Anne Elementary School (historical)
Rabbit Hills
Rader Hills
Rafton (historical)
Rainy Peak
Ramapo (historical)
Mount Rambler
Rams Butte
Red Hill
Red Hill
Red Hills
Red Hills
Red Mountain
Redess
Reedville
Reuben (historical)
Reuben
Mount Reuben
Richardson Butte
Richmond
Rivergrove
River Junction
Riverdale
Riversdale
Riverside
Riverside
Riverton
Robe Hill
Roberts Mountain
Robertson
Robinwood
Rock Creek
Rock Hill
Rockford
Rockwood
Rocky Ford
Rogers
Rogers Mountain
Rooster Rock (historical)
Rosebush
Rosewood
Rothe
Round Butte
Round Lake Hill
Round Mountain
Round Mountain
Round Prairie
Round Timber
Rowena
Royal
Ruby
Ryegrass Table
Saddle Butte
Saddle Mountain
Safley
Sailor (historical)
Saint Johns
Saint Johns Junction
Saint Peter Mountain
Salem Hills
Salisbury (historical)
Salmonberry (historical)
Sand Hollow
Sandhill Crossing
Santiam Terrace
Sargent Place (historical)
Schmore Place (historical)
Scorpion Butte
Mount Scott
Seaside
Sentinel Hill (historical)
Serafin Point
Shadowood
Shady
Shady Dell
Shady Pine
Shaff
Shale City
Shaniko Summit
Shannon
Sharps Corner
Shaw Table
Shell Rock Butte
Sherar
Sheridan Peak
Shortridge Butte
Shot Pouch Butte
Sidney
Sidwalter Buttes
Siletz Hill
Silver Falls City (historical)
Silverton Hills
Six Corners
Skull Spring
Smith Hill
Smith Rock
Snake Hill
Soapgrass Mountain
Sodaville
South Lake Oswego
South Scappoose
South Table Mountain
Southport
Spangler Hill
Sparta
Speaker
Speece
Spofford
Spring Hill
Spring Mountain
Springdale
Sproul Point
Paiute Butte
Lone Butte
Stanfield
Stanfield Junction
Stanley
Stanton (historical)
Star Mountain
Starkey
Starvation Heights
Stauffer
Steamboat Mountain
Steet Mountain
Steinman
Stennett Butte
Stewarts
Strawberry (historical)
Stuckey Butte
Stukel
Sugarloaf
Sugarloaf Mountain
Sumner
Sunday Hill
Sunnyside
Sunnyside
Sunset
Swamp Creek Buttes
Swede Knoll
Swedetown
Sylvan
Mount Sylvania
Sylvester Place
Table Mountain
Table Mountain
Table Mountain
Table Rock
Table Rock
Mount Tabor
Mount Talbert
Tater Hill
Taylorville
Teeters Landing
Telocaset
Telocaset Hill
Tenmile Butte
Texum (historical)
The Knobs
Thirtymile
Thompson Butte
Thorn Hollow (historical)
Thornberry
Thors Hammer
Three Pines
Tidewater Summit
Timber Butte
Timber Butte
Tims Peak
Tolo
Tom Folley Mountain
Tongue Point Village
Tonquin
Tracy
Trece
Triangle Lake School
Troy
Tucke Place
Turkey Hill
Turkey Hill
Turner
Tuttle Point
Twelvemile Corner
Twelvemile Table
Twin Buttes
Twin Hills
Twin Knolls
Twin Prairie Buttes
Twin Rocks
Tygh Valley
Umapine
Union Mills
Union Point (historical)
University Park
Upper Highland
Valby
Vale
Valle Vista (historical)
Van Horn
Vaughn
Veatch
Venator
Veneta
Vermont Hills
Vinemaple
Vines Hill
Vinson (historical)
Voltage
Wagontire
Waldron (historical)
Wall Gulch
Wallace (historical)
Walton
Warner (historical)
Warrenton
Waterloo
Waverly Heights
Weatherby
Weatherby School (historical)
Weaver
Weldwood
Wendling
Wendt Butte
West Butte
West Portland
West Portland Park
West Scio
Westfall
Westland (historical)
Westport
Wetzels Corner
Wheatland
Wheeler Heights
Whiskey Dick
Whiskey Hill
Whitaker
Whitby Ditch
Whitely Landing County Park
Whitford
Whitwood Court
Wichita Station
Wilcox Peak
Willamette
Willow Butte
Willowdale
Willows (historical)
Wilson (historical)
Wilson Butte
Wilson Point
Wilsonia (historical)
Wilsonville
Wing
Winkle Butte
Witt Butte
Wood Village
Woodpecker Hill
Woodstock
Wooldridge Butte
Worden
Wrentham (historical)
Yampo
Yankee Mountain
Yellow Creek Mountain
Yoakum
Yoder
Yoncalla
Young
Youngs Butte
Deschutes (historical)
Fargher (historical)
Early (historical)
McMullins Landing
Hampton Butte
Howluk Butte
Cline Hill
Salishan Beach
West Hill
West Butte
Salishan
Coronado Shores
Tater Hill
Smoky Butte
Studhorse Butte
Juniper Butte
Shields Butte
Currant Peak
Sixmile Canyon
Threemile Canyon
Central (historical)
Western Log Pond
Snow Peak Log Pond
Batty School (historical)
Bridge Creek Meadow
Crain Prairie Trail
Eagle Tanner Trail
Elkhorn Gulch
Haskins Gulch
Highline Lateral
Hosmer Lake Trail
Jack Andy Creek
Kerby Peak Trail
McAlister Creek
McAlister Ridge
Mud Lake Trail
Roberts Ranch
Poormans Creek
Shelley Creek
New Idaho School (historical)
Spring Branch
Summer Lake State Wildlife Area
Sunflower Flat
The Maples
Wake Up Rilea Creek
A and M Spring
A-Y Spring
Abbey Creek
Abbot Butte
Abbot Butte Spring
Abbot Creek
Abbott Butte
Abbott Creek
Abbott Creek
Abbott Creek
Abbot Pass
Abbott Prairie
Abernethy Lake
Abes Mountain
Abraham Flat
Abraham Spring
Acker Divide Trail
Acker Rock
Ackerley Lake
Acorn Creek
Ada (historical)
Ada Station
Adam Creek
Adams Canyon
Adams Creek
Adams Creek
Adams Creek
Adams Creek
Adams Mountain
Adams Ranch
Adams Elementary School
Adams Spring
Adams Spring
Adams Spring
Adell Butte
Adobe Flat
Adobe Pond
Aerial Lake
Agate Creek
Agency
Agency Creek
Agency Creek
Agency Creek Quarry
Agency Hill
Agency Plains
Agnes Spring
Agness
Ahalapam Cinder Field
Ahalt Creek
Aims
Ainsworth State Park
Ajax Mine
Akers Butte
Al Sarena Buzzard Mine
Alameda Lake
Alamo
Alamo Gulch
Alamo Mine
Alarm Clock Spring
Albany Mine
Albee (historical)
Albee Meadow
Albertson Reservoir
Alco Creek
Alco Rock
Alco Trail
Alder
Alder (historical)
Alder Brook
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek
Alder Creek Meadow
Alder Creek Spring
Alder Flat Recreation Site
Alder Glen Campground
Alder Grove Cemetery
Alder Gulch
Alder Gulch
Alder Gulch
Alder Gulch
Alder Slope
Alder Slope Ditch
Alder Spring
Alder Spring
Alder Spring
Alder Spring
Alder Spring
North Alder Spring
Alder Spring
Alder Spring
Alder Spring
Alder Spring
Alder Spring
Alder Spring
Alder Spring
Alder Spring
Alder Spring
Alder Spring
Alder Spring Creek
Alder Spring Lookout
Alder Spring Ridge
Alder Swamp Shelter
Aldrich Gulch
Aldrich Mountains
Aldrich Spring
Alex Creek
Alexander Creek
Alexander Gulch
Alfred A Loeb State Park
Alfred Reservoir
Algoma Spring
Alice Lake
Lake Alice
Alicel
Alkali Butte
Alkali Canyon
Alkali Creek
Alkali Creek
Alkali Creek
Alkali Creek
Alkali Creek
Alkali Flats
Alkali Meadows
Walker Creek
Allen Canyon
Allen Canyon
Allen Canyon
Allen Creek
Allen Creek
Allen Creek
Allen Creek
Allen Creek
Allen Creek
Allen Creek
Allen Creek Reservoir
Allen Gulch
Allen School (historical)
Allen Spring
Allen Spring
Allen Spring
Allen Spring
Allen Spring Canyon
Allingham Guard Station
Allison Creek
Allison Spring
Alluvial Creek
Alma School (historical)
Almeda Mine
Alpha
Alpine Recreation Site
Alpine Lake
Alpine Ridge
Alpine Ski Trail
Alpine Spring
Alpine Trail
Alsea
Alsea Bay
Alsea Guard Station
Alsea River
Alsup Creek
Alsup Mountain
Alsup Spring
Alta Lake Trail
Lake Alta
Althouse Creek
Althouse Mountain
Althouse Trail
Altnow Spring
Amalgamated Mine
Amber Reservoir
Amelia Creek
Amelia Spring
Amity Mine
Andy Lake
Amota Butte
Ana Reservoir
Ana River
Ana River School (historical)
Anchor School (historical)
Anchor Spring
Anderson Bluffs
Anderson Butte
Anderson Cabin
Anderson Creek
Anderson Creek
Anderson Creek
Anderson Creek
Anderson Creek
Anderson Field
Anderson Gulch
Anderson Mountain
Anderson Mountain Trail
Anderson Point
Anderson Spring
Anderson Spring
Anderson Springs
Anderson Station
Andies Prairie
Andies Ridge
Andrew Spring
Andrews Mine
Andy Creek
Andys Rapids
Aneroid Lake
Aneroid Mountain
Angel Camp
Angel Gulch
Angels Rest
Angus Spring
Lake Ann
Anna Creek
Annie Creek
Annie Spring
Anns Butte
Anson Wright Memorial Park
Ant Creek
Ant Hill
Antelope Butte
Antelope Canyon
Antelope Cow Camp
Antelope Creek
Antelope Creek
Antelope Creek
Antelope Creek
Antelope Creek
Antelope Desert
Antelope Flat
Antelope Flat
Antelope Lake
Antelope Mountain
Antelope Mountain
Antelope Reservoir
Antelope Spring
Antelope Spring
Antelope Spring
Antelope Spring
Antelope Spring
Antelope Spring
Antelope Spring
Antelope Swale
Antelope Valley
Antelope Valley
Antelope Well
Anthony Creek
Antler Creek
Antler Point
Antler Prairie
Antler Spring
Antler Spring
Antler Spring Trail
Antlers Recreation Site
Antone (historical)
Antone Butte
Anvil Creek
Anvil Creek
Anvil Mountain
Lake Aphis
Apple Creek
Apple Creek Recreation Site
Applegate Butte
Applegate Canyon
Applegate Creek
Applegate Creek
Applegate Ford
Applegate Peak
Applegate River
Applegate Spring
Aqua Spring
Arant Point
Arbuckle Corral
Arbuckle Mountain
Arbuckle Ski Area
Arbuckle Spring
Arch Rock
Archie Creek
Argo Creek
Arkansas Hollow
Arlie Canyon
Armet Creek
Armstrong Creek
Armstrong Gulch
Armstrong Gulch
Army Hill
Arnica Spring
Arnold Canal
Arnold Creek
Arnold Mine
Arrah Wanna Trail
Arrastra Creek
Arrow Recreation Site
Arrowwood Point
Arrowhead Point
Art Moore Ranch
Aschoff Buttes
Aschoff Buttes Trail
Ash Creek
Ash Creek
Ash Flat
Ash Gulch
Ash Homestead
Ash Swale
Ash Swamp
Ashcraft Flume
Ashland
Ashland Creek
Ashland Lateral
Ashland Mine
Ashur Flat
Asinine Bridge
Aspen Butte
Aspen Recreation Site
Aspen Creek
Aspen Creek
Aspen Fork
Aspen Grove Spring
Aspen Reservoir
Aspen Spring
Aspen Spring
Aspen Spring
Aspen Spring
Aspen Spring
Aspen Spring
Association Corral (historical)
Aubrey Mountain
Auger Creek
Auger Valley
Augur Creek
Augusta Creek
Aurora Mine
Austin
Austin Creek
Austin Hot Springs
Austin Junction
Austin Meadow
Austin Point
Austin Ranch
Avalanche Creek
Avalanche Lake
Avery Creek
Avery City Park
Avery Pass
Avery Ranch
Mount Avery
Awbrey Butte
Awbrey Creek
Awbrey Mountain
Axe Gulch
Axtell Creek
Azalea Lake
B C Creek
B F Smith Ranch
B S Spring
BVD Trail
Babcock Cabin
Babe Lake
Baber Lookout
Baboon Creek
Baby McKee Mine
Baby Rock
Babyfoot Creek
Babyfoot Lake
Bachelor Butte
Mount Bachelor
Bachelor Canyon
Bachelor Creek
Bachelor Creek
Bachelor Mountain
Bachelor Mountain Trail
Backout Creek
Buckpasture Gulch
Bacon Creek
Bacon Spring
Bad Banks Creek
Bad Lands
Badger Butte
Badger Butte
Badger Cabin
Badger Canyon
Badger Creek
Badger Creek
Badger Creek
Badger Creek
Badger Creek Trail
Badger Flat
Badger Hole Spring
Badger Lake
Badger Spring
Badlands
Badley Gulch
Bagley Ditch
Bagley Spring
Bailey Butte
Bailey Butte
Bailey Cabin
Bailey Canyon
Bailey Creek
Bailey Creek
Bailey Creek
Bailey Creek
Bailey Flat
Bailey Gulch
Bailey Gulch
Bailey Mountain
Bailey Ridge
Bain Slough
Bain Station
Bainfield Mine
Baker Canyon
Baker Canyon
Baker Canyon
Baker City Gulch
Baker Creek
Baker Creek
Baker Creek
Baker Gardens
Baker Gulch
Baker Reservoir
Baker Spring
Balance Creek
Balance Spring
Bald Butte
Bald Butte
Bald Butte
Bald Butte
Bald Crater
Bald Hill
Bald Hill
Bald Hills
Bald Knob
Bald Knob
Bald Knob
Bald Mountain
Bald Mountain
Bald Mountain
Bald Mountain
Bald Mountain
Bald Mountain
Bald Mountain
Bald Mountain
Bald Mountain
Bald Mountain
Bald Mountain
Bald Mountain Creek
Bald Mountain Lookout
Bald Mountain Shelter
Bald Peter
Bald Peter Butte
Bald Peter Pasture Spring
Bald Ridge
Bald Ridge
Bald Top
Baldface Creek
Baldface Lake
Baldwin Area
Baldwin Creek
Baldwin Hills
Baldwin Spring
Baldy Creek
Baldy Creek
Baldy Creek
Baldy Mountain
Baldy Mountain
Baldy Mountain
Baldy Peak
Mount Baldy
Ball Butte
Ball Mountain
Ball Point
Ball Point Trail
Balm Canyon
Balm Creek
Balm Creek
Balm Creek Reservoir
Balm Creek Shaft
Balm Fork
Balm Mountain
Balsinger Prairie
Balter Creek
Baltimore Ditch (historical)
Bamboo Gulch
Bancroft
Bandit Spring
Bangor Elementary School (historical)
Banjo Spring
Banner Mine
Banning Creek
Bannister Creek
Bar Creek
Bar M Ranch
Bar S Reservoir
Barber Creek
Barber Creek
Barbie Lakes
Barclay Creek
Bare Island
Bare Lake
Bareface Butte
Barhaven Creek
Bark Creek
Bark Shanty Prairie
Barker Creek
Barkley Spring
Barklow Mountain
Barley Camp
Barley Camp Creek
Barlow Butte
Barlow Butte
Barlow Campground (historical)
Barlow Creek
Barlow Guard Station
Barlow Pass
Barlow Ridge
Barn Creek
Barnacle Rock
Barnard Creek
Barnard Gulch
Barnes Butte
Barnes Creek
Barnes Rim
Barnes Slough
Barnett Spring
Barney Creek
Barnhouse Spring
Barr Creek
Barr Mine
Barr Ranch
Barrel Spring
Barrel Spring
Barrett Spur
Barry Point
Bartley Headquarters
Barton Heights
Basco Spring
Basco Spring
Base of Mount Mazama
Basin Butte
Basin Camp
Basin Creek
Basin Creek
Basin Creek
Basin Creek
Basin Creek
Basin Creek
Basin Creek
Basin Creek
Basin Creek
Basin Creek
Basin Creek Trail
Basin Point
Basin Spring
Basket Butte
Basket Mountain
Basket Spring
Baskin Spring
Bass (historical)
Bossuot Cabin
Bastard Spring
Bates
Bates Butte
Bathtub Spring
Bathtub Spring
Battle Ax
Battle Ax Creek
Battle Bar
Battle Creek
Battle Creek
Battle Creek
Battle Creek
Battle Creek
Battle Creek
Battle Creek Camp
Battle Creek Guard Station
Battle Creek Mountain
Battle Creek Mountain Reservoir
Battle Creek Shelter
Battle Creek Trail
Battle Lake
Battle Mountain
Battle Mountain
Battle Mountain
Battle Mountain State Park (historical)
Battle Mountain Summit
Battle Peak
Battle Ridge
Battle Ridge Reservoir
Battle Rock
Batts Meadow
Baum Slough
Bare Creek
Baxter Creek
Bay Steer Creek
Bays Lake
Bayview
Beabe Creek
Beach Recreation Site
Beach Mountain
Beachie Saddle
Beachie Trail
Beachkomb Spring
Beachlers Union Trading Post
Beacon Hill
Beal
Beal Lake
Beal Prairie
Beale Canyon
Beales Butte
Beam Creek
Beamer Creek
Beamer Ranch
Bean Creek
Bean Creek
Bear Bluff
Bear Butte
Bear Butte
Bear Butte
Bear Butte
Bear Camp
Bear Camp (historical)
Bear Camp Pasture Recreation Site
Bear Camp Ridge
Bear Camp Spring
Bear Camp Trail (historical)
Bear Camp Trail
Bear Canyon
Bear Canyon Butte
Bear Canyon Campground
Bear Canyon Creek
Bear Claw Canyon
Bear Claw Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Bear Creek
Allen Canyon Ditch
Bear Creek Guard Station
Bear Creek Guard Station
Bear Creek Meadow
Bear Creek Trail
Bear Creek Trail
Bear Flat
Bear Flat
Bear Flat
Bear Flat Draw
Bear Flat Springs
Bear Flat Station
Bear Gulch
Bear Gulch
Bear Gulch
Bear Gulch
Bear Gulch
Bear Gulch
Bear Gulch
Bear Gulch
Bear Lake
Bear Lake
Bear Lake
Bear Lake
Bear Lake
Bear Lake Creek
Bear Meadows
Bear Mine
Bear Mountain
Bear Mountain
Bear Mountain
Bear Mountain
Bear Mountain
Bear Mountain Trail
Bear Paw Forest Camp (historical)
Bear Paw Meadow
Bear Paw Spring
Bear Point
Bear Point
Bear Ridge
Bear Ridge
Bear Skull
Bear Skull Rims
Bear Skull Spring
Bear Spring
Bear Spring
Bear Spring
Bear Spring
Bear Spring
Bear Spring
Bear Spring
Bear Springs Ranger Station (historical)
Bear Trap Canyon
Bear Trap Spring
Bear Tree Guard Station (historical)
Bear Tree Spring
Bear Valley
Bear Valley
Bear Valley
Bear Valley
Bear Valley Canyon
Bear Valley Creek
Bear Valley Work Center
Bear Wallow
Bear Wallow
Bear Wallow
Bear Wallow Creek
Bear Wallow Creek
Bear Wallow Creek Recreation Site
Bear Wallow Forest Service Station
Bear Wallow Lookout (historical)
Bear Wallow Spring
Bear Wallow Spring
Bear Wallow Spring
Bear Wallow Spring
Bear Wallow Spring
Bear Wallows
Bear Wallows Spring
Bear Wallow Spring
Bearbones Mountain
Bearcamp Ridge
Beard Creek
Beard Saddle
Beartrap Creek
Beartrap Meadow
Beartrap Trail
Beartree Creek
Bearwallow Butte
Bearwallow Reservoir
Bearwallow Ridge
Bearwallow Ridge
Bearwallow Spring
Bearwallows
Beatty
Beatty Station
Beaty Creek
Beaver
Beaver Butte
Beaver Butte Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek
Beaver Creek Driveway
Beaver Creek Forest Camp
Beaver Creek Prairie
Beaver Dam Creek
Beaver Dam Creek
Beaver Dam Spring
Beaver Fork
Beaver Lake
Beaver Lakes
Beaver Marsh
Beaver Marsh
Beaver Marsh
Beaver Meadows
Beaver Meadows
Beaver Meadows Trail
Beaver Ranch
Beaver Ridge
Beaver Rock Spring
Beaver Shelter
Beaver Slide Ridge
Beaver Spring
Beaver Spring
Beaver Spring
Beaver Sulphur Recreation Site
Beaver Swamp
Beaverdam Creek
Beaverdam Creek
Beaverdam Creek
Beaverdam Creek
Beaverdam Creek
Beaverdam Creek
Beaverdam Reservoir
Beaverdam Reservoir
Beaverdam Trail
Bed Spring
Bed Spring
Bedford Creek
Bedford Point
Bedpan Burn
Bedpan Spring
Bedrock Creek
Bedrock Creek
Bedrock Creek
Bedrock Spring
Bee Creek
Bee Creek
Bee Creek
Bee Reservoir
Bee Spring
Beech Creek
Beecher Creek
Beech Creek
Beecher (historical)
Beecher Creek
Beede Desert
Beekman Flat
Beekman Ridge
Beeler Creek
Beeler Ridge
Beeler Spring
Beeman Canyon
Beeman Creek
Beeman Junkens Trail (historical)
Beetle Creek
Beetle Spring (historical)
Belcher Mine
Belknap Crater
Belknap Creek
Bell Cow Creek
Bell Creek
Bell Creek
Bell Mountain
Bell Spring
Bell Spring
Bellows Creek
Bellows Spring
Bellwether Spring
Belshaw Creek
Belshaw Meadows
Beltz Dike
Ben Brown Spring
Ben Camp
Ben Harrison Mine
Ben Harrison Peak
Ben Young Creek
Bench Mark Butte
Bend
Bend Creek
Bend Glacier
Benefield Creek
Benham Falls
Benham Falls Recreation Site
Benjamin Spring
Benner Creek
Bennett Creek
Bennets Point
Bennett Cabin
Bennett Creek
Bennett Flat
Bennett Pass
Bennett Spring
Bennett Well
Benny Creek
Benson Creek
Benson Creek
Benson Gulch
Benson Plateau
Benson Spring
Benson State Park
Bentilla Creek
Bentonite Reservoir
Benz Spring
Berkley Spring
Berkshire Creek
Berland Ranch (historical)
Berland Reservoir
Berlin School (historical)
Lake Bernice
Berry Creek
Berry Creek
Berry Creek
Berry Creek
Berry Creek Trail
Berry Rock
Bert Creek
Bert Lake
Bessie Butte
Bessie Creek
Bessie Rock
Bessie Rock Trail
Betty Lake
Between Pond
Beverly Creek
Bewley Creek
Bible Creek
Biddle Pass
Bieberstedt Butte
Bieberstedt Creek
Bieberstedt Trail
Big Baldy
Big Bear Camp
Big Ben Creek
Big Bend
Big Bend
Big Bend
Big Bend Creek
Big Bend Ditch
Big Bend Mountain
Big Bend Trail
Big Bottom
Big Boulder Creek
Big Buck Spring
Big Bunchgrass
Big Bunchgrass
Big Burn
Big Burn Spring
Big Butte Creek
Big Butte Springs
Big Camp Canyon
Big Camp Ranger Station (historical)
Big Canyon
Big Canyon
Big Canyon
Big Canyon
Big Canyon
Big Canyon Spring
Big Canyon Spring
Big Cat Spring
Big Cedar Springs
Big Cliff
Big Cow Burn
Big Craggies
Big Creek
Big Creek
Big Creek
Big Creek
Big Creek
Big Creek
Big Creek
Big Creek
Big Creek
Big Creek
Big Creek Forest Camp (historical)
Big Creek Recreation Site
Big Creek Meadow
Big Creek Slough
Big Creek Trail
Big Dog Spring
Big Draw Creek
Big Dutch Canyon
Big Eddy Recreation Site
Big Elk Guard Station
Big Elk Mine
Big Finger Lake
Big Fir Spring
Big Fir Spring
Big Flat
Big Flat
Big Flat
Big Flat
Big Flat Ditch
Big Four Mine
Big Gordon Gulch
Big Happy Spring
Big Hole
Big Hole Butte
Big Howard Spring
Big Lake
Big Lake
Big Log Creek
Big Marsh
Big Marsh Creek
Big Meadow Camp
Big Meadow Canyon
Big Meadows
Big Meadows
Big Meadows
Big Meadows
Big Medicine Creek
Big Mountain
Big Mowich Mountain
Big Pine Opening
Big Pool Recreation Site
Big Prairie
Big Redwood Creek
Big Reservoir
Big Riner Basin
Big River Recreation Site
Big Rock
Big Rock
Big Rock Creek
Big Rock Flat
Big Rock Spring
Big Saddle
Big Sage Hen Spring
Big Sheep Ridge
Big Sheep Trail Stock Driveway
Big Sink
Big Slide Lake
Big Slide Mountain
Big South Fork Hunter Creek
Big Spread Spring
Big Spring
Big Spring
Big Spring
Big Spring
Big Spring
Big Springs Creek
Big Spring Creek
Big Springs
Big Springs
Big Springs
Big Springs
Big Springs
Big Springs
Big Squaw Mountain
Big Sugarloaf Peak
Big Summit Prairie
Big Swamp
Big Table
Big Tree
Big Tree
Big Trees Spring
Big Valley
Big Wall Creek
Big Washout Creek
Big Weasel Springs
Big Willow Creek
Big Willow Spring
Big Willow Spring Creek
Big Windy Creek
Bigelow Cabins
Bigelow Creek
Bigelow Lakes
Biggs Spring
Bighorn Campground (historical)
Bighorn Creek
Bill Brown Cove
Bill Creek
Bill Creek
Bill Gott Spring
Bill Moore Creek
Bill Pete Spring
Billick Burn Trail
Billie Creek
Billings Creek
Mount Billingslea
Bills Creek
Bills Spring
Lake Billy Chinook
Billy Creek
Billy Creek
Billy Jones Creek
Billy Jones Lake
Billy Meadows
Billy Meadows Guard Station
Billy Moore Creek
Billy Mountain
Billys Gulch
Binegar Butte
Bingham Basin
Bingham Camp
Bingham Creek
Bingham Lake
Bingham Lakes
Bingham Mountain
Bingham Prairie
Bingham Ridge
Bingham Ridge Trail
Bingham Spring
Bingham Spring
Bingham Spring
Bingham Springs
Binghams Shelter
Bingo Lake
Burch Creek
Birch Creek
Birch Creek
Birch Creek
Birch Creek
Birch Creek
Birch Spring
Birch Springs
Bird Butte
Birdie Creek
Birds Point
Biscuit Creek
Biscuit Hill
Biscuit Spring
Bishop Creek
Bishop Creek
Bishop Spring
Bismark Creek
Bissell
Bitter Creek
Bitter Lick
Bitter Lick Creek
Bittner Creek
Bixby Spring
Bjerkson Flat
Black Bear Mine
Black Bear Swamp
Black Butte
Black Butte
Black Butte
Black Butte
Black Butte
Black Butte
Black Butte Mine
Black Butte Ranch
Black Butte Elementary School
Black Canyon
Black Canyon
Black Canyon
Black Canyon
Black Canyon
Black Canyon Butte
Black Canyon Recreation Site
Black Canyon Creek
Black Canyon Creek
Black Canyon Creek
Black Canyon Ranch
Black Canyon Trail
Black Cap
Black Crater
Black Creek
Black Creek
Black Creek
Black Eagle Mine
Black Gorge
Black Hills
Black Lake
Black Mound
Black Mountain
Black Mountain
Black Mountain
Black Mountain
Black Mountain Spring
Black Pine Creek
Black Pine Spring Recreation Site
Black Rock
Black Rock
Black Rock
Black Rock
Black Rock
Black Rock Butte
Black Rock Canyon
Black Rock Creek
Black Rock Fork
Black Rock Ranch
Black Rock Spring
Black Rock Trail
Black Stump Canyon
Black Wolf Meadows
Blackberry Creek
Blackburn Canyon
Blackeye Creek
Blackhorse Butte
Blackhorse Creek
Blackhorse Draw
Blackjack Mine
Black Joe Spring
Blackmore Creek
Blacks Arm
Blacks Creek
Blacks Island
Blacktail Spring
Blackwell Trail
Blaine
Blair Creek
Blair Lake
Blair Lake Trail
Blair Meadows
Blake Flat
Blake Ranch Spring
Blake Spring
Blakesley Creek
Blalock Mountain
Blanchard Gulch
Blanchard Well
Bland Branch
Bland Mountain
Blanket Creek
Blarney Spring
Blaze Lake
Blazed Alder Butte
Blazed Alder Creek
Blazed Alder Way Trail
Bleakman Spring
Blevins Creek
Blevins Spring
Blind Sam Gulch
Blinn Spring
Blitzen Butte
Block and Tackle Spring
Blodgett
Blodgett Creek
Blodgett Peak
Blodgett Elementary School
Bloody Point
Bloody Point
Bloody Point
Bloody Run Creek
Blossom Bar
Blow Lake
Blowdown Lake
Blowdown Ridge
Blowfly Spring
Blowout Basin
Blowout Basin Creek
Blowout Cliff
Blowout Creek
Blowout Creek
Blue Box Pass
Blue Bucket Mine
Blue Bucket Spring
Blue Bucket Trail
Blue Canyon
Blue Canyon Lake
Blue Canyon Trail
Blue Cow Spring
Blue Creek
Blue Creek
Blue Creek
Blue Creek
Blue Creek
Blue Creek Work Center
Blue Eagle Spring
Blue Goose Spring
Blue Gulch
Blue Gulch
Blue Gulch
Blue Gulch
Blue Gulch
Blue Jay Mine
Blue Jay Spring
Blue Jay Creek
Blue Kettle Ridge
Blue Lake
Blue Lake
Blue Lake
Blue Lake
Blue Lake
Blue Lake
Blue Lake Camas Prairie Trail
Blue Lake Trail
Blue Mountain Camp
Sumpter Cemetery
Blue Mountain Hot Springs
Blue Mountain Mine
Blue Mountain Summit
Blue Mountain Work Center
Blue Pool Recreation Site
Blue Ribbon Mine
Blue Ridge
Blue Ridge
Blue Ridge
Blue Ridge Spring
Blue Rock
Blue Rock
Blue Rock Trail
Blue Slide Creek
Blue Spring
Blue Spruce Camp
Bluebill Lake
Bluebucket Creek
Bluegrass Butte
Bluegrass Ridge
Bluejay Spring
Bluejay Spring
Bluff Creek
Bly
Bly Mountain
Bly Ridge
Boag Creek
Boar Backbone
Board Creek
Board Creek
Board Creek
Board Gulch
Board Hollow
Board Mountain
Board Shanty Creek
Board Tree Spring
Boardtree Creek
Boat Ford Slough
Boat Rock
Boaz Gulch
Boaz Mountain
Bob Bennett Spring
Bob Butte
Bob Creek
Bob Creek
Bob Creek
Bob Creek
Bob Meadow
Bobbit Mine
Bobby Lake
Bobcat Creek
Bobs Bay
Bobs Garden Mountain
Bobs Garden Trail
Bobsled Creek
Bobsled Ridge
Bobsled Trail
Bog Spring
Bogg Canyon
Boggs Spring
Bogue Creek
Bogue Gulch
Bogus Creek
Bohannon Ranch
Bohemia Creek
Bohemia Mountain
Bohemia Trail
Boiler Draw
Bolan Creek
Bolan Creek Mine
Bolan Lake
Bolan Lake Trail
Bolan Mine
Bolan Mountain
Bolivar Creek
Mount Bolivar
Bologna Basin
Bologna Creek
Bologna Spring
Bolon Island
Bolon Island Tideways State Scenic Corridor
Bolt Mountain
Boly Bluff
Bona Fida Shelter
Bonanza Basin
Bonanza Mine
Bonanza Mine
Bonanza Trail
Bond Creek
Bonde Spring
Bone of Contention Mine
Bone Canyon
Bone Mountain
Bone Point
Bone Spring
Bone Spring Campground
Boneyard Canyon
Bonifer
Bonita Spring
Bonner Creek
Bonner Creek
Bonneville
Bonneville Dam
Bonneville Mountain
Bonney Butte
Bonney Creek
Bonney Crossing
Bonney Meadows
Bonney Meadows Trail
Bonnie Doone Number One Mine
Bonnieview Ranch
Bonny Lakes
Bookout Creek
Boomer Creek
Boomer Creek
Boone Creek
Boone Island
Boone Prairie
Boone Slough
Boot Hill Cemetery
Boot Hill Creek
Boot Lake
Booth (historical)
Booth Island
Booth Lake
Booth Ridge
Bootleg Spring
Bosley Butte
Bosonberg Creek
Boston Bluff
Boston Canyon
Boston Tunnel
Bottle Creek
Bottle Prairie
Bottle Prairie Trail
Bottle Rock
Bottle Spring
Bottle Spring
Bottle Spring
Bottleneck Spring
Boulder Butte
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek
Boulder Creek Trail
Boulder Lake
Boulder Lake Trail
Boulder Lake Way Trail
Boulder Peak
Boulder Point
Boulder Point
Boulder Pond
Boulder Ridge
Boulder Rock
Boulder Spring
Boulder Spring
Boulder Spring
Boulder Spring
Big Boulder Trail
Boundary Butte
Boundary Butte
Boundary Recreation Site
Boundary Creek
Boundary Creek
Boundary Spring
Boundary Spring
Boundary Spring
Boundary Springs
Boundary Trail
Boundary Trail
Bounds Creek
Bounty Lake
Bourbon Spring
Bow Creek
Bow Creek
Bow Spring
Bowen Creek
Bowerman Lake
Bowers Bridges Creek
Bowser Mine
Bowman Creek
Bowman Creek
Bowman Creek
Bowman Spring
Bowman Trail
Box Butte
Box Canyon
Box Canyon
Box Canyon
Box Canyon
Box Canyon
Box Canyon
Box Canyon
Box Canyon Creek
Box Canyon Dam
Box Canyon Horse Camp
Box Creek
Box Spring
Box Spring
Box Spring
Box Spring
Box Spring
Box Spring
Boxcar Flats
Boyce Corral
Boyd Creek
Boyd Spring
Boyer
Boyer Creek
Boynton Park
Boze Creek
Boze Shelter
Bracket Mountain
Bracket Spring
Brad Spring
Bradetich Well
Bradford Creek
Bradford Island
Bradley Creek
Bradley Creek
Bradley Creek Mine
Bradley Flat
Bradley Flat Spring
Bradley Lake
Bradley Ridge
Bradley Trail
Braham Meadows
Brahma Lake
Brainard Creek
Bramlet Memorial Cemetery
Brandon Spring
Brandy Bar
Brandy Creek
Brandy Peak
Branson Creek
Brattain Butte
Brattain Canyon
Brattain Canyon Spring
Brattain Hill
Brattain Ranch
Brattain Ridge
Bravo Creek
Bravo Ranch (historical)
Bray Mountain
Bray Point
Braymill
Breaks Reservoir
Breeds Flat
Breezy Creek
Breezy Point
Breitenbush Recreation Site
Breitenbush Hot Springs
Breitenbush Lake
Breitenbush Mountain
Breitenbush River
Brenham (historical)
Brewer Ranch
Brewer Reservoir
Briar Creek
Brice Creek
Brickpile Ranch
Bridal Veil
Bridal Veil Creek
Bridal Veil Falls
Bridge of the Gods
Bridge Creek
Bridge Creek
Bridge Creek
Bridge Creek
Bridge Creek
Bridge Creek
Bridge Creek
Bridge Creek
Bridge Creek
Bridge Creek
Bridge Creek
Bridge Creek
Bridge Creek
Bridge Creek
Bridge Creek Draw
Bridge Creek Flats
Bridge Creek Meadow
Silvies Valley Ranch
Bridge Spring
Bridges Creek
Bridgeview
Briggs Cabin
Briggs Creek
Briggs Ranch
Brigham Creek
Briley Canyon
Briley Mountain
Brisbois Gulch
Bristo Creek
Bristol Quarry
Bristow Prairie
Bristow Trail
Broadenaxe Gulch
Broadway Lava
Broadway Spring
Broady Creek
Brock Creek
Brock Meadows
Brockman Ranch
Brodie Creek
Brogan Creek
Broken Creek
Broken Leg Creek
Broken Ridge
Broken Top
Broken Top Spring
Broken Top Trail
Brokencot Creek
Bronco Creek
Brook Lake
Brookings
Brooks Ditch
Brooks Draw
Brooks Meadow
Brooten Mountain
Brophy Creek
Brothers
Browder Ridge
Browder Ridge Trail
Brown Cabin Spring
Brown Canyon
Brown Creek
Brown Creek
Brown Creek
Brown Creek
Brown Creek
Brown Meadows
Brown Mountain
Brown Mountain
Brown Mountain Trail
Brown Owl Mine
Brown Prairie
Brown Ranch
Brown Ranch (historical)
Brown Spring
Mount Brown
Brownie Basin
Brownie Creek
Brownie Creek
Brownie Creek Trail
Browns Creek
Browns Creek
Browns Mountain Recreation Site
Browns Gulch
Browns Mill
Browns Mountain
Browns Mountain Crossing
Browns Reservoir
Brownsworth Creek
Bruce Camp
Bruin Creek
Bruin Run Campground (historical)
Bruin Run Creek
Bruler Creek
Brum Spring
Bruner Spring Reservoir
Bruno Creek
Bruno Meadows
Bruno Meadows Trail
Brushy Bar
Brush Creek
Brushy Creek
Brush Creek
Brush Creek
Brush Creek
Brush Creek
Brush Creek
Brush Creek
Brush Creek
Brush Creek
Brush Creek
Brush Creek
Brush Creek
Brush Creek Camp
Brush Creek Trail
Brush Draw
Brush Lake
Brush Mountain
Brush Spring
Brushy Bald Mountain
Brushy Bar Creek
Brushy Draw Way
Brushy Gulch
Brushy Gulch
Brushy Hill
Brushy Mountain
Brushy Mountain
Henderson Creek
Buchanan
Buck Basin
Buck Basin
Buck Basin Burn
Buck Basin Fork
Buck Butte
Buck Butte
Buck Butte
Buck Butte
Buck Butte
Buck Cabin
Buck Cabin Creek
Buck Cabin Trail
Buck Creek Recreation Site
Buck Canyon
Buck Canyon Spring
Buck Canyon Trail
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek
Buck Creek Crossing
Buck Creek Trail
Buck Draw
Buck Falls
Buck Fork
Buck Fork Trail
Buck Gulch
Buck Gulch
Buck Gulch
Buck Gulch
Buck Hollow
Buck Hollow
Buck Hollow Creek
Buck Lake
Buck Lake
Buck Lake Trail
Buck Mountain
Buck Mountain
Buck Mountain
Buck Mountain
Buck Mountain
Buck Mountain
Buck Mountain
Buck Mountain
Buck Peak
Buck Peak
Buck Peak
Buck Peak
Buck Peak
Buck Peak Creek
Buck Point
Buck Point
Buck Point Creek
Buck Point Trail
Buck Point Troughs
Buck Prairie
Buck Reservoir
Buck Rock
Buck Rock
Buck Rock Creek
Buck Spring
Buck Spring
Buck Spring
Buck Spring
Buck Spring
Buck Spring
Buck Spring
Buck Spring
Buck Spring Creek
Buck Spring Guard Station (historical)
Buck Spring Reservoir
Buck Trough Spring
Buckaroo Creek
Buckaroo Creek
Buckaroo Flat
Buckaroo Gulch
Buckaroo Lake
Buckaroo Pass
Buckaroo Spring
Buckboard Creek
Buckboard Spring
Buckeye Butte
Buckeye Creek
Buckeye Creek
Buckeye Creek
Buckeye Lake
Buckeye Mine
Buckhead Creek
Buckhead Mountain
Buckhead Mountain
Buckhead Trail
Buckhorn Cabin
Buckhorn Creek
Buckhorn Creek
Buckhorn Creek
Buckhorn Lookout
Buckhorn Meadow
Buckhorn Mountain
Buckhorn Mountain
Buckhorn Ranch
Buckhorn Ridge
Buckhorn Spring
Buckhorn Spring
Buckhorn Spring
Buckhorn Spring
Buckhorn Springs
Buckley Creek
Buckmaster Point
Buckneck Mountain
Buckshot Creek
Buckskin Butte
Buckskin Butte
Buckskin Peak
Buckskin Spring
Bucksnort Creek
Budd Creek
Badger Lake
Buelah Creek
Buena Vista State Park
Buffalo Mine
Buffalo Rock
Buford Creek
Buford Ridge
Bug Butte
Bug Creek
Bug Spring
Bug Spring
Bugaboo Creek
Bugman Ranch
Bulger Creek
Bull Bend
Bull Canyon
Bull Creek
Bull Creek
Bull Creek
Bull Creek
Bull Creek
Bull Creek
Bull Creek
Bull Creek
Bull Creek
Bull Creek Dam
Bull Flat
Bull Gap
Bull Gulch
Bull Gulch Spring
Bull Jack Spring
Bull Mountain
Bull of the Woods Trail
Bull Pine Gap
Bull Pine Ridge
Bull Prairie
Bull Prairie Trail
Bull Run Creek
Bull Run Creek
Bull Run Creek
Bull Run Lake Trail
Bull Run Reservoir Number One
Bull Run Reservoir Number Two
Bull Run River
Bull Run Elementary School (historical)
Bull Run Trail
Bull Spring
Bull Spring
Bull Spring
Bull Spring Creek
Bull Swamp
Bullard Canyon
Bullard Creek
Bullard School (historical)
Bulldog Creek
Bulldog Prairie
Bulldog Rock
Bullfrog Spring
Bullock Creek
Bullock Gulch
Bullrun Creek
Bullrun Creek
Bullrun Mine
Bullrun Mountain
Bullrun Rock
Bullrun Spring
Bullrun Spring
Bullseye Spring
Bully Creek
Bulo Point
Bumblebee Spring
Bummer Creek
Bump Creek
Bump Lake
Bunchgrass Meadows
Bunchgrass Creek
Bunchgrass Ridge
Bunchgrass Trail
Buncom
Bunker Hill
Bunker Hill
Bunker Hill Mine
Bunny Butte
Bunton Creek
Burchard Creek
Burcher Canyon
Burford Canyon
Burger Butte
Burger Meadows
Burger Pass
Burke Spring
Burley Bluff
Burn Butte
Burn Canyon
Burn Creek
Burn Spring
Burned Timber Creek
Burned Tree Reservoir
Burns Butte
Burns Creek
Burnside Creek
Burnt Bridge Creek
Burnt Butte
Burnt Cabin Creek
Burnt Cabin Creek
Burnt Cabin Gulch
Burnt Canyon
Burnt Corral Creek
Burnt Corral Creek
Burnt Corral Spring
Burnt Creek
Burnt Creek
Burnt Creek
Burnt Creek
Burnt Granite
Burnt Hill Creek
Burnt Lake
Burnt Lake Trail
Burnt Mountain
Burnt Mountain
Burnt Mountain
Burnt Mountain
Burnt Mountain Creek
Burnt Mountain Meadows
Burnt Mountain Spring
Burnt Peak
Burnt Peak
Burnt Peak
Burnt Ridge
Burnt River
Burnt River School
Burnt Spring
Burnt Spring
Burnt Timber Mountain
Burnt Top
Burnt Woods
Burntcabin Creek
Burpee (historical)
Burro Creek
Burton Butte
Burton Butte
Burton Creek
Burton Hill
Burton Ridge
Burton Saddle
Burton Valley
Busby Spring
Bush Mill
Buster Butte
Buster Creek
Buster Spring
Buster Spring Shelter
Butch Foster Saddle
Butcher Bill Creek
Butcher Bill Meadow
Butcher Boy Mine
Butcher Creek
Butcher Creek
Butcher Gulch
Butcher Knife Ridge
Butcher Knife Spring
Butcher Knife Peak
Butcherknife Creek
Butcherknife Creek
Butcherknife Creek
Butcherknife Spring
Butler Butte
Butler Creek
Butler Creek
Butler Creek
Butler Creek
Butler Peak
Butler Spring
Mount Butler
Butte Creek
Butte Creek
Butte Creek
Butte Creek
Butte Creek
Butte Creek
Butte Creek
Butte Creek
Butte Falls
Butte Falls Cemetery
Butte Spring
Butte Spring
Butterfield Creek
Butterfield Lake
Butterfield Riffle
Butterfield Spring
Butterfly Island
Buttermilk Creek
Buttermilk Flat
Buttes of the Gods
Buttes Ranch
Button Creek
Button Flat Spring
Button Springs
Buzz Spring
Buzzard Butte
Buzzard Creek
Buzzard Creek
Buzzard Point
Buzzard Rock
Buzzard Rock
Buzzard Roost
Buzzards Roost
Byars Creek
Byars Gulch
Byars Peak
Bybee Creek
Byerle (historical)
Bypass Trail
Byram Gulch
Byrd Canyon
Byzandine Gulch
C and H Riders Camp
C 7 Reservoir
C W A Well
Cabell City
Cabell Meadow
Cabin Butte
Cabin Creek
Cabin Creek
Cabin Creek
Cabin Creek
Cabin Creek
Cabin Creek
Cabin Creek
Cabin Creek
Cabin Creek
Cabin Creek Trail
Cabin Guard Station
Cabin Lake Ranger Station (historical)
Cabin Meadow
Cabin Meadows
Cabin Spring
Cabin Spring
Cabin Spring
Cabin Spring
Cable Creek
Cable Creek Trail
Cabot Creek
Cabot Lake
Cabot Lake Trail
Cache Canyon
Cache Creek
Cache Creek
Cache Lake
Cache Lake Trail
Cache Meadow
Cache Mountain
Cachebox Creek
Cached Lake
Cactus Mountain
Cadle Butte
Cadle Creek
Cady Creek
Caesar Gulch
Cain Cabin Trail
Cain Creek
Cain Creek
Cairn Basin
Calahan Creek
Calamity Butte
Calamity Creek
Calamity Forest Camp (historical)
Calamut Lake
Calamut Way
Calapooya Divide
Calapooya Trail
Calapooya Way
Caldwell Creek
Calf Creek
Calf Creek
Calf Ridge
Calico Creek
Calico Spring
California Bar
California Gulch
California Gulch
California Gulch
Calimus Butte
Call Creek
Call Meadow
Call Meadow Trail
Callahan Creek
Callahan Lookout
Canyon Number Three Trail
Camas Butte
Camas Creek
Camas Creek
Camas Creek
Camas Creek
Camas Prairie
Camas Prairie
Camas Prairie
Camas Prairie
Camas Prairie
Camas Prairie Trail
Camas Spring
Camel Hump
Camel Hump
Camel Rock
Camelback Bluff
Camelot Lake
Camelsback
Cameron Creek
Camp
Camp One
Camp Fourteen
Camp Two
Camp Three Reservoir
Camp Four
Camp Four Creek
Camp Seventy-six
Camp Nine
Camp Abbot (historical)
Camp Arrah Wanna
Camp Baldwin
Camp Branch
Camp Canyon
Camp Clark
Camp Cleawox
Camp Coffee Pot
Camp Cooper
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek
Camp Creek Butte
Camp Creek Recreation Site
Camp Creek Forest Camp
Camp Creek Ranger Station (historical)
Camp Easter Seal
Camp Esther Applegate
Camp Faraway
Camp Five
Camp Flat
Camp Friend
Camp Grant
Grayback Campground
Camp Hope
Camp Howard
Camp Lane
Camp Makualla
Camp Marion
Camp McLoughlin
Camp Meeting Creek
Camp Meriwether
Camp Moreland Spring
Camp Morrow
Camp Namanu
Camp Number 2
Camp Noxage Spring
Camp One
Camp Polk
Camp Reservoir
Camp Sa-wa-li-na-is
Camp Sherman
Camp Simms
Camp Six
Camp Spring
Camp Spring
Camp Tamarack
Camp Three
Camp Baker
Camp Watson (historical)
Camp Watson Point
Camp Westwind
Camp Windy Recreation Site
Camp Yallani
Campbell Butte
Campbell Canyon
Campbell Creek
Campbell Creek
Campbell Creek
Campbell Falls
Campbell Hill
Campbell Ranch
Campbell Reservoir
Campbell Spring
Campers Flat
Campers Lake
Campground Number One (historical)
Campground Number Two (historical)
Camporee Spring
Canada Creek
Canadian Bench
Canal Creek
Canal Creek
Canal Creek
Canary
Candle Creek
Candle Creek Recreation Site
Canfield Gulch
Cannery Hill
Cannery Hill
Cannery Island
Cannery Mountain
Cannibal Mountain
Cannon Canyon
Cannon Spring
Canteen Creek
Canteeno Spring
Canton Creek
Canton Creek Trail
Canton Point
Canton Shelter
Cantrall Gulch
Cantrell Spring
Canyon City
Canyon City Cemetery
Canyon Creek
Canyon Creek
Canyon Creek
Canyon Creek
Canyon Creek
Canyon Creek
Canyon Creek
Canyon Creek
Canyon Creek
Canyon Creek
Canyon Creek
Canyon Creek
Canyon Creek
Canyon Creek Campground
Canyon Creek Recreation Site
Canyon Creek Trail
Canyon Mountain
Canyon Mountain Trail
Canyon Peak
Canyon Spring
Cap Box Spring
Cap Creek
Cap Healy Well
Cape Cove
Cape Creek
Cape Creek
Cape Ferrelo
Cape Horn
Cape Horn Creek
Cape Lookout
Cape Lookout State Park
Cape Meares
Cape Meares
Cape Meares State Scenic Viewpoint
Cape Mountain
Cape Perpetua
Cape Ridge
Cape Sebastian
Cape Sebastian State Park
Caplinger Creek
Capps Mountain
Cappy Mountain
Caps Creek
Capsuttle Creek
Captain Cook Point
Captain Creek
Captain Prairie
Carberry Creek
Carberry Recreation Site
Carey Creek
Carey Lake
Carey Ranch (historical)
Carey Stearns Ranch
Caribou Creek
Carl Lake
Carle Creek
Carlon Spring
Carlson Arm
Carlson Camp
Carlton Pasture
Carmichael Canyon
Mount Carmine
Carnes Ditch
Carney Butte
Carney Flat
Carns Canyon
Carpenter Gulch
Carpenter Pond
Carpenterville
Carpet Hill Creek
Carroll Butte
Carrol Campground
Carroll Creek
Carrol Creek
Carroll Glade
Carroll Glade Springs
Carson
Carson Cabin
Carson Cemetery
Carson Creek
Carson Creek
Carson Spring
Carson Spring
Carter Creek
Carter Creek
Carter Lake
Carters Hog Ridge
Cartwheel Ridge
Cartwright Creek
Carver Glacier
Carver Lake
Corwin Spring
Cary Reservoir
Cascade Canal
Cascade Creek
Cascade Creek
Cascade Creek
Cascade Creek
Cascade Divide Trail
Cascade Gorge
Cascade Gorge
Cascade Head
Cascade Locks
Cascade Spring
Cascade Summit
Cascadia
Cascadia State Park
Case Creek
Casey Creek
Cash Camp (historical)
Cashner Butte
Cashow Flat
Cashow Springs
Cass Ranch
Cassiday Butte
Cast Creek
Cast Creek Trail
Cast Lake
Castle Creek
Castle Creek
Castle Creek Trail
Castle Crest
Castle Point
Castle Rock
Castle Rock
Castle Rock
Castle Rock
Castle Rock Fork
Castle Rock
Castlerock Lodge
Cat Canyon
Cat Canyon
Cat Canyon Spring
Cat Creek
Cat Creek
Cat Creek
Cat Creek
Cat Creek
Cat Creek
Cat Hill
Cat Hill Way
Cat Mountain
Cat Mountain
Catalpa Lake
Cataract Creek
Catched Two Lake
Cathedral Ridge
Cathedral Rocks
Catherine Creek Meadow
Cathy Lake
Catlin Lake
Calkins Creek
Cave Creek
Cave Junction
Cave Mountain
Cave Rock
Cavern Creek
Caves Camp
Cavitt Creek
Cavitt Mountain
Cavitt Shelter
Cawlfield Ranch
Cayuse Crater
Cayuse Creek
Cayuse Flat
Cayuse Ridge
CCC Spring
CCC Spring
Cedar Camp
Cedar Camp
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Sallee Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek
Cedar Creek Recreation Site
Cedar Creek Spring
Cedar Flat
Cedar Guard Station
Cedar Gulch
Cedar Gulch
Cedar Lake
Cedar Lake
Cedar Log Creek
Cedar Mountain
Cedar Point
Cedar Spring
Cedar Spring
Cedar Spring
Cedar Spring
Cedar Spring
Cedar Springs
Cedar Springs Creek
Cedar Springs Mountain
Cedar Swamp
Cedar Swamp
Cedar Swamp Creek
Cedar Swamp Creek
Celebration Mine
Cemetery Ridge
Center Lake
Center Peak
Center Ridge
Central Lateral
Central Oregon Canal
Sears Flat
Cerine Creek
Chaffer Canyon
Chako Creek
Chalk Creek
Chalk Creek
Chalk Creek
Chamberlain Lake
Chamberlin Spring
Chambers Lakes
Chambers Mine
Chambers Spring
Champion Creek
Champion Mine
Champion Saddle
Champman Creek
Chance Creek
Chandler Creek
Chaparral Creek
Chapin Creek
Chapin Meadow
Chapman Creek
Chapman Creek
Dry Creek
Chapman Creek
Chappel Spring
Charcoal Point
Charity Spring
Charlie Buck Gulch
Charlie Mack Creek
Charlie Smith Butte
Lake Charline
Charlotte Creek
Charlton Butte
Charlton Creek
Charlton Lake
Chase Mountain
Chase Spring
Chaski Bay
Chatfield (historical)
Che Spring
Cheatem Holler Camp
Cheney Creek
Cherry Creek
Cherry Creek
Cherry Creek
Cherry Creek
Cherry Creek
Cherry Creek Ranch
Cherry Flat
Cherry Glade
Cherry Gulch
Cherry Gulch
Cherry Mountain
Cherry Peak
Cherry Spring
Cherry Spring
Cherry Spring Reservoir
Cherryville
Chesmore Spring
Chesnimnus Cow Camp
Chesnimnus Creek
Chestnut Spring
Chetco Bar
Chetco Cove
Chetco Divide Trail
Chetco Lake
Chetco Lookout (historical)
Chetco Pass
Chetco Peak
Chetco Peak Trail
Chetco Point
Chetco River
Lake Chetlo
Chev Spring
Cheval Lake
Chewaucan River
Chicago Cabin
Chicago Creek
Chicago Trail
Chichester Falls
Chickadee Spring
Chickahominy Creek
Chicken Creek
Chicken Hill
Chicken Spring
Chickenhouse Gulch
Chico Trail
Chief Creek
Old Chief Joseph Gravesite
Chief Joseph Monument
Chief Joseph Mountain
Chief Schonchin Cemetery
Chieftain Creek
Chieftain Mine
Chilcoot Junction Shelter
Chilcoot Creek
Chilcoot Mountain
Chilcoot Ridge
Chilcoot Trail
Chilly Creek
Chiloquin
Chiloquin Ridge
Chilson Creek
Chimney Creek
Chimney Gulch
Chimney Lake
Chimney Peak
Chimney Peak Trail
Chimney Rock
China Bar
China Cap
China Cap
China Cap Creek
China Cap Ridge
China Creek
China Creek
China Creek
China Creek
China Creek
China Creek
China Creek
China Creek
China Creek
China Creek Ditch
China Creek Spring
China Creek Trail
China Ditch
China Flat
China Garden
China Gulch
China Gulch
China Gulch
China Gulch
China Gulch
China Gulch
China Hat
China Hat Creek
China Hat Peak
China Hat Spring
China Lake
China Meadow
China Mountain
China Peak
China Rapids
China Spring
Chinaman Hat
Chinaman Trail
Chinidere Mountain
Chinook Bend
Chinook County Park
Chinquapin Butte
Chinquapin Point
Chintimini Creek
Chipman Gulch
Chipmunk Spring
Chipps Spring
Chinquapin Creek
Chiquito Lake
Chismore Butte
Chitwood Creek
Chitwood Trail
Chocktoot Creek
Chocktoot Spring
Chop Creek
Choptie Prairie
Chris Borg Spring
Christmas Creek
Christy Creek
Christy Flats
Chrome Camp
Chrome Creek
Chrome King Mine
Chrome Ridge
Chrome Ridge
Chrome Spring
Chucksney Mountain
Church in the Wildwood
Chute Gulch
Cigar Lake
Cinder Cone
Cinder Hill
Cinder Prairie Lookout
Cinder Prairie Way
Cinderella Spring
Cinge Creek
Cinnabar Gulch
Cinnabar Mine
Cinnabar Mountain
Cinnamon Butte
Cinnamon Peak
Circle Bar Spring
Circle Lake
Circle M Ranch
City Creek
City Creek Shelter
Clackamas Lake
Clackamas Lake Recreation Site
Claggett Lake
Clapboard Gulch
Clarence Creek
Clark Butte
Clark Creek
Clark Creek
Clark Creek
Clark Creek
Clark Creek
Clark Creek
Clark Glacier
Clark Lake
Clark Lake
Clark Meadow
Clark Spring
Clark Spring
Clark Spring
Clark Springs
Clarks Creek
Clarks Creek
Clarks Fork Creek
Claw Creek
Clay Creek
Clay Hill
Clay Hill Creek
Claypool Spring
Clayton Creek
Clayton Reservoir
Clear Branch
Clear Creek
Clear Creek
Clear Creek
Clear Creek
Clear Creek
Clear Creek
Clear Creek
Clear Creek
Clear Creek
Clear Creek
Clear Creek
Clear Creek
Clear Creek
Clear Creek
Clear Creek
Clear Creek
Clear Creek
Clear Creek
Clear Creek
Clear Creek Campground (historical)
Clear Creek Ditch
Clear Creek Crossing Recreation Site
Clear Creek Way Trail
Clear Fork
Clear Fork Butte
Clear Lake
Clear Lake
Clear Lake
Clear Lake
Clear Lake
Clear Lake
Clear Lake Butte
Clear Point
Clear Spring
Clear Water Ditch
Clearwater
Clearwater Falls
Clearwater River
Cleary Spring
Cleator Bend Recreation Site
Cleawox Lake
Cleetwood Cove
Clem Spring
Clemens Ranch
Clement Ranch
Cleopatra Lookout (historical)
Cleveland Creek
Cleveland Ridge
Clevenger Butte
Cliff Creek
Cliff Creek
Cliff Creek
Cliff Lake
Cliff Lake
Cliff Lake
Cliff Lake Shelter
Cliff Nature Trail
Cliff Spring
Cliff Spring Reservoir
Clifford
Cliffs Creek
Cline Creek
Cliney Flat
Clinger Spring
Cloud Cap Inn
Cloud Cap Saddle Recreation Site
Cloud Lake Group
Cloudcap Bay
Clover Butte
Clover Butte
Clover Butte
Clover Camp
Clover Creek
Clover Creek
Clover Creek
Clover Flat
Clover Lake
Clover Meadow
Clover Ridge
Clover Ridge
Cloverdale
Cloverdale
Cloverdale Ditch
Nestucca Valley Elementary
Cloverpatch Butte
Cloverpatch Trail
Lake Clovis
Clyde Holliday State Park
Coal Creek
Coal Creek
Coal Bank Creek
Coal Creek
Coal Creek Campground
Coal Mine Creek
Coal Pit Creek
Coal Pit Mountain
Coal Point
Coalmine Creek
Coalmine Hill
Coalmine Lick
Coalpit Springs
Coast Creek
Coast Creek Park
Cobleigh Ranch
Cochran Islands
Cochran Spring
Cockleburr Creek
Code Creek
Camp Cody
Coe Branch
Coe Glacier
Cofelt Ranch
Coffee Butte
Coffee Creek
Coffee Creek
Coffee Pot Trail
Coffeepot Creek
Coffeepot Creek
Coffeepot Creek
Coffeepot Flat
Coffeepot Spring
Coffeepot Spring
Coffeepot Trail
Coffin Butte Lookout
Coffin Creek
Coffin Mountain
Coffin Mountain Trail
Coffman Camp Trail
Cogswell Creek
Cohen Creek
Cohoe Creek
Cohoe Mine
Coin Spring
Colby Spring
Cold Canyon
Cold Creek
Cold Creek
Cold Creek
Cold Creek
Cold Creek
Cold Creek
Cold Creek
Cold Spring Creek
Cold Point
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring
Cold Spring Camp
Cold Spring Camp
Cold Spring Camp
Cold Spring Canyon
Cold Spring Canyon
Cold Spring Creek
Cold Spring Creek
Cold Spring Gulch
Cold Spring Ridge
Cold Spring Trail
Cold Spring Trail
Cold Spring Trail
Cold Spring
Cold Springs
Cold Springs
Cold Springs
Cold Springs Guard Station
Cold Springs Guard Station
Coldwater Spring
Cole Canyon
Cole Canyon
Cole Chuck Meadow
Cole Creek
Cole Creek
Cole Spring
Colebrook Butte
Colegrove Butte
Coleman Arm
Coleman Canyon
Coleman Spring
Collard Lake
Collawash Mountain
Collawash River
College Creek
College Creek Ranger Station (historical)
Collier Butte
Collier Cone
Collier Creek
Collier Glacier
Collier Glacier View
Collier Memorial State Park
Collier Bar
Collings Gulch
Collings Mountain
Collins Butte
Collins Cabin
Collins Camp
Collins Creek
Collins Creek
Collins Creek
Collins Lake
Collins Lookout
Collins Rim
Calo Spring
Colt Canyon
Colt Lake
Colton Dam
Columbia Gorge Recreation Area
Columbia Mine
Columbia River
Columbia Southern Canal
Colvin Creek
Combs Flat
Comer Creek
Comma Lake
Lake Como
Company Butte
Compass Creek
Conroy Creek
Conroy Spring
Conant Basin
Conant Creek
Conde B McCullough State Recreation Site
Conde Creek
Condon Butte
Condon Creek
Cone Creek
Cone Mill
Cone Peak
Congdon Creek
Congo Gulch
Conklin Creek
Conklin Spring
Conley Creek
Conley Creek
Conley Spring
Conn Creek
Connally Spring
Conner Creek
Conner Spring
Conners Place
Connor Canyon
Conroy
Consolidated Ditch
Centennial Gulch
Continental Mine
Continental Mine
Cook Burn
Cook Creek
Cook Creek
Cook Creek Trail
Cook Gulch
Cooks Canyon
Cooks Meadow
Cooks Mountain
Cool Camp
Cool Camp Trail
Cool Creek
Cool Creek Trail
Cooley Creek
Coon Canyon
Coon Creek
Coon Creek
Coon Creek
Coon Creek
Coon Creek
Coon Creek
Coon Creek
Coon Creek
Coon Creek
Coon Creek
Coon Hollow
Coon Hollow
Coon Lake
Coon Ridge
Cooper Creek
Cooper Creek
Cooper Spur
Cooper Spur Ski Trail
Coopers Ridge
Coopey Falls
Coos Bay
Coos River
Coos School (historical)
Cooston
Cooston Channel
Copeland Canyon
Copeland Creek
Copeland Creek
Copeland Creek Trail
Copeland Creek Trail
Copepod Lake
Copper
Copper Canyon
Copper Creek
Copper Creek
Copper Creek
Copper Creek
Copper Creek
Copper Creek
Copper Creek Trail
Copper Lake
Copper Mountain
Copperfield Draw
Copperhead Creek
Copperopolis Mine
Copple Butte
Copple Butte Trail
Copple Creek
Coquille Point
Corbell Butte
Corbett Cabin
Elliot R Corbett II Memorial State Park
Corcoran Reservoir
Cordelia Flat
Corey and Meadow Placer
Corey Gulch
Corn Creek
Corncob Creek
Corncob Ranch
Corner Creek
Cornez Creek
Corner Lake
Cornpatch Meadow
Cornwall Point
Corporation Guard Station
Corral Basin
Corral Basin
Corral Basin Creek
Corral Butte
Corral Camp
Corral Creek
Corral Creek
Corral Creek
Corral Creek
Corral Creek
Corral Creek
Corral Creek
Corral Creek
Corral Creek
Corral Creek Trail
Corral Draw
Corral Flat
Corral Flat
Corral Gulch
Corral Gulch
Corral Lake
Corral Reservoir
Corral Spring
Corral Spring
Corral Springs Trail
Corral Swamp
Corral Swamp Trail
Corrigal Spring Campground
Corrigan Lake
Corset Creek
Corvallis
Corvallis Reservoir
Corvallis Watershed Wild Animal Refuge
Cot Creek
Cotter Pond
Cottonwood Basin
Cottonwood Buttes
Cottonwood Camp
Cottonwood Recreation Site
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek
Cottonwood Creek Trail
Cottonwood Lake
Cottonwood Meadows
Cottonwood Meadows Trail
Cottonwood Reservoir
Cottonwood Reservoir
Cottonwood Spring
Cottonwood Spring
Cottonwood Spring
Cottonwood Spring
Cottonwood Spring
Cottonwood Spring
Cottonwood Spring
Cottonwood Spring
Cougar Bluffs
Cougar Butte
Cougar Butte
Cougar Camp
Cougar Canyon
Cougar Canyon
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek
Cougar Creek Trail
Cougar Flat
Cougar Flat
Cougar Gap
Cougar Gulch
Cougar Gulch
Cougar Lake
Cougar Lake
Cougar Meadow
Cougar Mine
Cougar Mountain
Cougar Mountain
Cougar Mountain
Cougar Mountain
Cougar Rapids
Cougar Ridge
Cougar Ridge
Cougar Ridge Trail
Cougar Rock
Cougar Rock
Cougar Rock
Cougar Rock
Cougar Spring
Cougar Spring
Cougar Spring
Cougar Trail
Coughanour Ditch
Coulee Creek
Council Butte
County Spring
Courier Mine
Courter Prairie
Courthouse Rock
Courtney Butte
Courtney Creek
Couse Creek
Cove Creek
Cove Creek
Cove Creek
Cove Creek
Cove Creek
Cove Spring
Cove Spring Work Center (historical)
Cover Recreation Site
Coverdale Guard Station
Cow Camp
Cow Camp
Cow Camp
Cow Meadow Recreation Site
Cow Canyon
Cow Creek
Cow Creek
Cow Creek
Cow Creek
Cow Creek
Cow Creek
Cow Creek
Cow Creek
Cow Creek Bridge
Cow Creek Road Reservoir
Cow Gulch
Cow Head Slough
Cow Hollow
Cow Hollow Spring
Cow Prairie
Cow Swamp
Cowbell Mountain
Cowboy Spring
Cowboy Spring
Cowhead Creek
Cowhorn Creek
Cowhorn Mountain
Cox Butte
Cox Creek
Cox Flat
Cox Island
Cox Tunnels
Coxie Meadow
Coye Ditch
Coyle Butte
Coyle Creek
Coyle Spring
Coyote Butte
Coyote Butte
Coyote Butte
Coyote Butte
Coyote Butte
Coyote Butte
Coyote Canyon
Coyote Canyon
Coyote Canyon
Coyote Creek
Coyote Creek
Coyote Creek
Coyote Creek
Coyote Creek
Coyote Creek
Coyote Creek
Coyote Creek
Coyote Creek
Coyote Flat
Coyote Gulch
Coyote Gulch
Coyote Gulch
Coyote Lake
Coyote Lake
Coyote Meadow
Coyote Mountain
Coyote Point
Coyote Ridge
Coyote Rock
Coyote Spring
Coyote Spring
Coyote Spring
Coyote Spring
Coyote Spring
Coyote Spring
Coyote Spring
Coyote Spring
Coyote Recreation Site
Crab Creek
Crabapple Creek
Crabapple Prairie
Cracker Creek
Craddock Meadows
Craddock Spring
Craft Point
Craft Spring
Carlton Creek
Craggie Creek
Craggy Creek
Craggy Mountain
Craig Grave
Craig Lake
Craig Mountain
Craigs Cabin
Crale
Crale Creek
Cram Creek
Cram Reservoir
Cram Spring
Crane Creek
Crane Creek
Crane Creek
Crane Creek
Crane Creek
Crane Creek
Crane Creek
Crane Creek
Boulder Creek
Crane Creek Campground
Crane Flats
Crane Flats
Crane Flats Forest Service Station
Crane Lake
Crane Mountain
Crane Prairie
Crane Prairie
Crane Prairie Recreation Site
Crane Prairie Guard Station
Crane Prairie Reservoir
Crater Butte
Crater Butte Trail
Crater Buttes
Crater Creek
Crater Creek
Crater Creek
Crater Creek
Crater Creek
Crater Creek Ditch
Crater Lake
Crater Lake Camp
Crater Lake Lodge
Crater Mountain
Crater Peak
Crater Peak Trail
Crater Rock
Crater Springs
Crater Trail
Crawfish Creek
Crawfish Creek
Crawfish Lake
Crawfish Lake
Crawfish Meadow
Crawford Butte
Crawford Creek
Crawford Creek
Crawford Gulch
Crawford Meadow
Crawford Meadow Spring
Crawford Point
Crawford Spring
Crazy Creek
Crazy Creek
Crazy Creek
Crazy Creek
Crazy Spring
Cree Spring
Creek Spring
Crapsey Gulch
Crescent
Crescent Siding
Crescent Butte
Crescent Recreation Site
Crescent Creek
Crescent Creek
Crescent Creek
Crescent Creek Recreation Site
Crescent Lake
Crescent Lake
Crescent Lake Junction
Crescent Lake Recreation Site
Crescent Mountain
Crescent Mountain Trail
Crescent Reservoir
Crescent Ridge
Cress Creek
Cressler Creek
Crevice Creek
Crew Canyon
Cricket Creek
Cripple Creek
Cripple Creek
Cripple Creek Trail
Crishook Canyon
Crockett Knob
Crockett Spring
Croft Forest Camp (historical)
Cronin Reservoir
Cronin Spring
Cronin Well
Crook County Middle School
Crook Creek
Crook Glacier
Crook Point
Crooked Bridge Creek
Crooked Canyon
Crooked Creek
Crooked Creek
Crooked Creek
Crooked Creek
Crooked Creek
Crooked Creek Meadows
Crooked Meadow
Crooked Neck Creek
Crooked Pine Ridge
Crooked Riffle
Crooked River
Crooked River Gorge
Crooked Trail
Crooked Tree Spring
Crooks Creek
Cross Country Ditch
Cross Hollow
Cross Reservoir
Crossing Way
Crossroads Reservoir
Crosswhite Creek
Crotchline Saddle
Crow Creek
Crow Creek
Crow Reservoir
Crow Ridge
Crowbar Spring
Crowley Creek
Crown Lake
Crown Mine
Crown Point
Crown Point State Park
Crowsfoot Creek
Cruikshank Butte
Cruikshank Spring
Cruiser Butte
Cruiser Spring
Crusher Creek
Crusher Spring
Crutcher Bench
Cruzatte
Cryder Butte
Crystal Castle Spring
Crystal Creek
Crystal Creek
Crystal Creek
Crystal Creek
Crystal Lake
Crystal Reservoir
Crystal Spring
Crystal Spring
Crystal Spring
Crystal Spring
Crystal Spring
Crystal Spring
Crystal Spring Creek
Crystal Springs
Crystalline Spring
Cub Cliff
Cub Creek
Cub Creek
Cub Creek
Cub Creek Trail
Cub Point
Cub Spring
Cuitan Creek
Cullen Creek
Cullens Reservoir
Culp Creek
Culp Creek
Culp Ranch
Cultus Creek
Cultus Creek
Cultus Creek
Cultus Lake
Cultus Lake Trail
Cultus Mountain
Cultus River
Culver
Culver Lake
Culvert Creek
Culvert Spring
Cumley Creek
Cumming Gulch
Cummings Creek
Cummings Creek
Cummins Creek
Cummins Peak
Cummins Ridge
Cunningham Creek
Cup Spring
Cup Spring
Cupit Mary Meadow Trail
Cupit Mary Mountain
Cupit Mary Trail
Cupper Canyon
Cur Creek
Curiosity Spring
Curley Creek
Curran Creek
Curran Mountain Spring
Currier Creek
Currier Creek
Currier Spring
Curup Spring
Curry Spring
Curtin Creek
Curtis Creek
Curtis Lake
Curtis Spring
Cushman
Cusick Mountain
Cutout Reservoir
Cutsforth County Park
Cyclone Canyon
Cynosure Forest Camp (historical)
Cyrus Hill Pond
Cyrus Spring
D M Spring
DK Spring
DaMotta Branch
Dad Spring
Daddy Lode Mine
Dads Creek
Daffodil Mine
Italian Spring
Dahl Creek
Dahl Fork
Dahl Pine
Dahlin Creek
Dailey Creek
Dailey Ranch
Dairy Creek
Dairy Creek
Dairy Creek
Dairy Meadow
Daisy Spring
Dale
Dale Canyon
Dale Work Center
Daley Creek
Daley Creek
Daley Prairie
Daly Creek
Daly Lake
Dam Observatory
Damon Creek
Damon Creek
Dams Canyon
Dams Meadow
Damsite Trail
Danger Bay
Daniel Creek
Daniel Spring
Daniel Spring
Daniel Spring
Danny Creek
Dans Creek
Dans Creek
Daphne Grove Recreation Site
Dark Canyon
Dark Canyon
Dark Canyon
Dark Canyon
Dark Canyon
Dark Canyon
Dark Canyon Creek
Dark Canyon Trail
Dark Lake
Dark Lake
Little Southworth Creek
Southworth Creek
Darling Creek
Darling Mountain
Darlingtonia State Natural Site
Darr Canyon
Darr Creek
Darrs Spring
Dartmouth Creek
Dave Ike Spring
Dave Spring
Davenport Cabin (historical)
Davenport Spring
Davey Lake
Mount David Douglas
David Hill Cemetery
Davidson Canyon
Davidson Park
Davidson Spring
Davis Creek
Davis Creek
Davis Creek
Davis Creek
Davis Creek
Davis Creek
Davis Creek
Davis Creek
Davis Creek
Davis Creek
Davis Creek Springs
Davis Flat
Davis Lake
Davis Lake Guard Station
Davis Mountain
Davis Spring
Davis Spring
Davis Spring Reservoir
Davis Trail (historical)
Dawson Mine
Day Canyon
Day Ridge
Day Spring
Days Creek
Days Gulch
Dayton-Grant Well
Dayville
Dayville Cemetery
DeWitt Creek
Dead Cow Gulch
Dead Dog Gulch
Dead End Reservoir
Dead End Spring
Dead End Trail
Dead Horse Basin
Dead Horse Butte
Dead Horse Canyon
Dead Horse Canyon Creek
Dead Horse Creek
Dead Horse Creek
Dead Horse Creek
Dead Horse Mountain
Dead Horse Reservoir
Dead Horse Ridge
Dead Horse Spring
Dead Horse Spring
Dead Horse Spring
Latgawa Creek
Dead Indian Rim
Latgawa Soda Springs
Dead Injun Creek
Deadlog Butte
Dead Mountain
Dead Mountain Trail
Dead Mule Canyon
Dead Mule Reservoir
Dead Mule Spring
Dead Point
Dead Soldier Trail
Deaddog Creek
Deadhorse Butte
Deadhorse Corral
Deadhorse Creek
Deadhorse Creek
Deadhorse Creek
Deadhorse Creek
Deadhorse Creek
Dead Horse Creek
Dead Horse Creek
Deadhorse Flat
Dead Horse Lake
Deadhorse Ridge
Deadhorse Spring
Deadhorse Spring
Deadhorse Spring
Deadline Creek
Deadman Bar
Deadman Canyon
Deadman Creek
Deadman Creek
Deadman Creek
Deadman Creek
Deadman Flat
Deadman Gulch
Deadman Gulch
Deadman Gulch
Deadman Gulch
Deadman Gulch
Deadman Gulch
Deadman Gulch
Deadman Lake
Deadman Mountain
Deadman Spring
Deadman Spring
Deadmond Place
Deadwood
Deadwood
Deadwood Creek
Deadwood Creek
Deadwood Creek
Deadwood Creek
Deadwood Creek
Deadwood Creek
Deadwood Mountain
Deadwood School (historical)
Deadwood Spring
Dealy Meadows
Dealy Way
Dealys Well
Dean Creek
Dean Creek
Dean Creek
Dean Spring
Dean Spring
Deardorff Creek
Deardorff Mountain
Death Ridge
Deboy Ranch
Deception Butte
Deception Creek
Deception Creek
Deception Creek
Deception Rock
Deception Way
Deduct Spring
Dee
Dee Flat
Dee Flat Ditch
Dee Lake
Dee Wright Observatory
Deely Creek
Deely Meadow
Deely Spring
Deep Canyon
Deep Canyon
Deep Canyon
Deep Canyon Spring
Deep Creek
Deep Creek
Deep Creek
Deep Creek
Deep Creek
Deep Creek
Deep Creek
Deep Creek
Deep Creek
Deep Creek
Deep Creek
Deep Creek
Deep Creek
Deep Creek
Deep Creek
Deep Creek Recreation Site
Deep Creek Recreation Site
Deep Creek Ranch
Deep Creek Spring
Deep Cut Creek
Deep Gulch
Deep Well
Deer Butte
Deer Butte
Deer Camp
Deer Cave Canyon
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek
Deer Creek Cemetery
Deer Creek Guard Station
Deer Draw
Deer Gulch
Deer Head
Deer Head Point
Deer Head Spring
Deer Lake
Deer Lake
Deer Leap Rock
Deer Lick Falls
Deer Lick Spring
Deer Meadows
Deer Mountain
Deer Point
Deer Ridge
Deer Scaffold Spring
Deer Spring
Deer Spring
Deer Spring
Deer Spring
Deer Spring
Deerhorn Creek
Deerhorn Creek
Deerhorn Ridge
Deerings Meadow
Deerlick Creek
Mount Defiance
Degner Well
Delintment Creek
Delintment Lake
Dell Creek
Dell Spring
Delles Creek
Delles Creek Camp
Delp Creek
Delp Creek Shelter
Delph Creek
Delta Creek
Demaris Cabin
Demaris Lake
Dement Ranch
Demeris Spring
Deming Creek
Deming Gulch
Democrat Gulch
Dempsey Creek
Dempsey Spring
Denman Cabin
Denning Spring
Dennis Creek
Dennis Lake
Denny Creek
Denny Flat
Denny Pond
Dent Creek
Dent Spring
Denude Lake
Denzer Bridge
Denzer Ridge
Depew Creek
Depot Slough
Deppy Creek
Derr Camp
Derr Guard Station (historical)
Derr Meadows
Derringer Spring
Desane Lake
Deschutes Bridge Guard Station (historical)
Deschutes Memorial Gardens
Deschutes River
Desert Cone
Desert Creek
Desert Ridge
Desert Spring
Desolation Butte
Desolation Canyon
Desolation Creek
Desolation Guard Station
Desolation Meadows
Desolation Saddle
Desolation Swamp
Detrick Ranch
Detroit
Detroit Dam
Detroit Lake State Park
Devil Canyon
Devil Creek
Devils Backbone
Devils Backbone
Devils Backbone
Devils Backbone
Devils Backbone
Devils Ball Diamond
Devils Canyon
Devils Canyon
Devils Canyon
Devils Canyon Trail
Devils Churn
Devils Club Canyon
Devils Creek
Devils Den
Devils Elbow
Heceta Head Lighthouse State Scenic Viewpoint
Devils Flat Guard Station
Devils Garden
Devils Garden
Devils Garden Forest Camp (historical)
Devils Garden Spring
Devils Gulch
Devils Half Acre Meadow
Devils Hill
Devils Horn
Devils Kitchen
Devils Knob Creek
Devils Knob Lookout
Devils Lake
Devils Lake
Devils Lake
Devils Meadow Campground
Devils Peak
Devils Peak
Devils Peak
Devils Peak Trail
Devils Pulpit
Devils Rest
Devils Run Creek
Devils Slide
Devils Slide
Devils Spring
Devils Stairway
Devils Well Creek
Devine Canyon
Devine Monument
Devine Ridge
Devine Ridge Spring
Devine Well
Devils Half Acre
Devitt Creek
Devore Arm
Dew Lake
Dewey Creek
Dewies Canyon
Diamond Camp
Diamond Creek
Diamond Creek
Diamond Creek
Diamond Dot Gulch
Diamond Dot Spring
Diamond J Spring
Diamond Jack Mine
Diamond Lake
Diamond Lake
Diamond Lake
Diamond Lake Junction
Diamond Peak
Diamond Peak
Diamond Peak
Diamond Peak Trail
Diamond Prairie
Diamond Rock Lookout
Diamond Rockpile
Diamond View Lake
Dice Crane Spring
Dicer Meadow
Dick Bluff
Dick Creek
Dick Nicholas Spring
Dick Point
Dick Spring
Dicks Camp Spring
Dicks Fork
Dicks Pond
Dicks Reservoir
Dicks Ridge
Dietrich Ranch
Dietrich Spring
Digger Creek
Digger Mountain
Digit Point Recreation Site
Diller Glacier
Dillon Butte
Dillon Creek
Dillon Falls
Dillon Falls Recreation Site
Dilman Meadows
Dimmick School (historical)
Dinger Creek
Dinger Creek Trail
Dinger Lake
Dinner Creek
Dinner Creek
Dinner Creek
Dinner Creek
Dinner Ridge Way
Dip Spring
Dipping Vat Creek
Dipping Vat Creek
Dipping Vat Spring
Discovery Point
Dishpan Spring
Dismal Creek
Dismal Spring
Dissel Creek
Disston
Ditch Cabin
Ditch Creek
Ditch Creek
Ditch Creek
Ditch Creek
Ditch Creek
Ditch Creek Forest Sevice Station
Ditch Spring
Divers Creek
Divide Butte
Divide Cow Camp
David Creek
Divide Creek
Divide Guard Station
Divide Pond
Divide Reservoir
Divide Spring
Divide Well
Divide Well Recreation Site
Dividend Bar
Division Spring
Dixie Butte
Dixie Creek
Dixie Creek
Dixie Creek
Dixie Flat
Dixie Recreation Site
Dixie Jett Gulch
Dixie Meadows
Dixie Meadows
Dixie Meadows Mine
Dixie Spring
Dixie Summit
Dixon Creek
Dixon Creek
Dixon Waterhole
Dixson Bar
Dobbin Cabin
Dobbin Creek
Dobbin Creek
Dobson Creek
Dobson Spring
Doby Spring
Doc Creek
Dockney Flat
Dodds Creek
Dodds Spring
Dodes Creek
Dodge
Dodge Creek
Dodge Park
Dodson Creek
Dodson Fork
Doe Butte
Doe Creek
Doe Creek
Doe Creek
Doe Creek
Doe Creek
Doe Gap
Doe Hollow
Doe Hollow
Doe Mountain
Doe Peak
Doe Point
Doe Reservoir
Doe Spring
Doe Spring Guard Station
Doe Swamp
Doehead Mountain
Doeskin Butte
Doeskin Creek
Doe Canyon
Dog Creek
Dog Creek
Dog Creek
Dog Creek
Dog Creek
Dog Creek
Dog Creek
Dog Fork
Dog Lake
Dog Lake Burn Spring
Dog Lake Work Center (historical)
Dog Mountain
Dog Mountain
Dog Mountain Creek
Dog Prairie
Dog Prairie
Dog Prairie Creek
Dog Prairie Trail
Dog River
Dog River Springs
Dog River Trail
Dog Tooth Rock
Doghouse Gulch
Doghouse Spring
Dogwood Spring
Dogwood Spring
Doherty Spring
Dole Spring
Dollar Basin
Dollar Basin Creek
Dollar Lake
Dollar Lake
Dollar Mountain
Dollar Spring
Dollarhide Pond
Dolly Spring
Dolly Varden Recreation Site
Dome Creek
Dome Rock
Dome Rock
Dompier Creek
Don Juan Mine
Donaca Creek
Donaca Lake
Donahue Creek
Donaldson Creek
Donaldson Mine
Donaldson Spring
Donegan Creek
Donegan Prairies
Donivan Creek
Donivan Mountain
Donna Creek
Donna Lake
Donnelly Butte
Donnelly Camp
Donnelly Creek
Donnelly Spring
Donomore Peak
Dons Butte
Dans Creek
Dons Spring
Dons Spring
Dooley Gulch
Dooley Gulch Pond
Dorena
Doris Creek
Doris Lake
Dorn Creek
Dorothy Creek
Dorr Canyon
Dorrance Cow Camp
Dorrance Ranch
Double Cabin Creek
Double Corral
Double Creek
Double Peaks
Double Peaks Lake
Double Rock
Doubleday Creek
Doug Ingram Tree
Dougherty Slough
Dougherty Recreation Site
Douglas Creek
Douglas Horse Pasture
Douglas Lake
Douthit Creek
Douthit Spring
Dove Creek
Dove Mountain
Dover
Dovre Peak
Dowell Spring
Dowells Peninsula
Downards Meadow
Downey Gulch
Downey Gulch
Downey Saddle
Doyle Creek
Dozer Spring
Drake Butte
Drake Creek
Drake Creek
Drake Peak
Draper Creek
Draw Creek
Dread and Terror Ridge
Drew
Drew Cemetery
Drew Creek
Drew Creek
Drew Lake
Drew School (historical)
Drews Creek
Drews Creek Recreation Site
Drews Reservoir
Drews Valley
Dribble Spring
Drift Campground
Drift Creek
Drift Creek
Drift Creek Shelter
Drift Creek Trail
Drift Fence Recreation Site
Driftwood Recreation Site
Driveway Creek
Driveway Spring
Driveway Spring
Driveway Trail
Dorn Spring
Drop Creek
Drowned Out Creek
Drumhill Ridge
Dry Butte
Dry Butte
Dry Butte
Dry Camas Creek
Dry Camp Mine
Dry Canyon
Dry Canyon
Dry Corner Spring
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek
Dry Creek Butte
Dry Creek Cabin
Dry Creek Camp
Dry Creek Island
Dry Creek Reservoir
Dry Creek Ridge
Dry Creek Spring
Dry Creek Spring
Dry Creek Spring
Dry Creek Trail
Dry Dam Reservoir
Dry Fivemile Creek
Dry Fork Brown Creek
Dry Fork Clear Creek
Dry Gulch
Dry Gulch
Dry Gulch
Dry Gulch
Dry Gulch
Dry Gulch
Dry Gulch
Dry Gulch
Dry Gulch Creek
Dry Gulch Ditch
Dry Gulch Reservoir
Dry Hollow
Dry Lake
Dry Lake
Dry Lake
Dry Lake Fork
Dry Matlock Creek
Dry Meadow
Dry Meadow
Dry Meadow
Dry Mountain
Dry Paulina Creek
Dry Porter Creek
Dry Prong
Dry Reservoir
Dry Ridge Trail
Dry River
Dry Run Bridge
Dry Run Creek
Dry Salmon Creek
Dry Soda Creek
Dry Soda Gulch
Dry Spring
Dry Swale Creek
Dry Well Creek
Dry Well Spring
Dryden
Dublin Creek
Dublin Lake
Dublin Spring
Dubois Creek
Dubuque Creek
Duck Creek
Duck Creek
Duck Lake
Dude Creek
Dudley Creek
Dudley Mountain
Duel Creek
Duff Meadows
Duffy Prairie
Dufur City Reservoir
Dug Bar
Dug Creek
Dug Spring
Dugout Butte
Dugout Creek
Dugout Creek
Dugout Lake
Dugout Spring
Duke Creek
Dukes Valley
Duley Creek
Dumbbell Lake
Dumbbell Lake
Dumont Creek
Dumont Ranger Station (historical)
Duncan
Duncan Butte
Duncan Canyon
Duncan Canyon
Duncan Creek
Duncan Creek
Duncan Gap
Duncan Guard Station
Duncan Hollow
Duncan Inlet
Duncan Reservoir
Dungeon Creek
Dunlap Creek
Dunlap Creek
Dunlap Lake
Dunn Creek
Dunn Creek
Dunn Ranch
Dunning Creek
Dunno Creek
Dunston Creek
Duprat Spring
Durham Creek
Durham Rapids
Dustbox Spring
Dustin Creek
Dustin Point
Dusty Camp Springs
Dusty Ridge
Dusty Saddle
Dusty Saddle Canyon
Dusty Spring
Dutch Creek
Dutch Creek Shelter
Dutch Gulch
Dutch Henry Trail (historical)
Dutch Oven Forest Camp
Dutch Oven Reservoir
Dutch Reservoir
Dutcher Creek
Dutchman Canyon
Dutchman Creek
Dutchman Creek
Dutchman Creek
Dutchman Flat
Dutchman Flat
Dutchman Flat
Dutchman Spring
Dutchy Creek
Dutchy Lake
Dutton Cliff
Dutton Ridge
Dutton Spring
Duval Creek
Dwarf Lakes Area
Dwight Creek
Dwyer Creek
Dyer Well
Dyke Creek
Dyke Creek
ERA Spring
Ead Creek
Eagle Butte
Eagle Butte
Eagle Butte
Eagle Butte Creek
Eagle Canyon
Eagle Cap
Eagle Cove
Eagle Crags
Eagle Creek
Eagle Creek
Eagle Creek
Eagle Creek
Eagle Creek
Eagle Creek
Eagle Creek
Eagle Creek
Eagle Creek Recreation Site
Eagle Creek Trail
Eagle Creek Trail
Eagle Gap
Eagle Island Creek
Eagle Lake
Eagle Mountain
Eagle Mountain
Eagle Peak
Eagle Point
Eagle Point
Eagle Point
Eagle Point Irrigation Canal
Eagle Reservoir
Eagle Ridge
Eagle Ridge
Eagle Rock
Eagle Rock
Eagle Rock
Eagle Rock
Eagle Rock
Eagle Rock
Eagle Rock
Eagle Valley
Eagles Rest
Eagles Rest Trail
Earl Spring
Earley Creek
Earmuff Spring
East Bear Creek
East Beaver Creek
East Birch Creek
East Bologna Canyon
East Branch Thomas Creek
East Branch Willow Creek
East Brookling Creek
East Burnt Log Spring
East Butte
East Camp Creek
East Canal
East Canyon
East Channel Willamette River
East Clover Creek
East Cow Creek
East Creek
Eva Creek
East Creek
East Creek
East Duncan Creek
East Eagle Mine
East Fisher Lake
East Fork Alder Creek
East Fork Annie Creek
East Fork Applegate Creek
East Fork Ash Creek
East Fork Ashland Creek
East Fork Beech Creek
East Fork Big Creek
East Fork Big Windy Creek
East Fork Blue Creek
East Fork Bolan Creek
East Fork Boneyard Canyon
East Fork Broady Creek
East Fork Brush Creek
East Fork Buck Creek
East Fork Butter Creek
East Fork Canal Creek
East Fork Canyon Creek
East Fork Canyon Trail
East Fork Chapman Creek
East Fork Clear Creek
East Fork Clear Creek
East Fork Collawash River
East Fork Cottonwood Creek
East Fork Cottonwood Creek
East Fork Cottonwood Creek
East Fork Cow Creek
East Fork Coyote Creek
East Fork Coyote Creek
East Fork Crazy Creek
East Fork Deadman Creek
East Fork Deer Creek
East Fork Dismal Creek
East Fork Dry Creek
East Fork Eagle Creek
East Fork Eagle Creek
East Fork Elk Creek
East Fork Elliot Creek
East Fork Eslick Creek
East Fork Fence Creek
East Fork Foley Creek
East Fork Gimlet Creek
East Fork Green River
East Fork Herman Creek
East Fork Hood River
East Fork Horse Creek
East Fork Howard Creek
East Fork Indian Creek
East Fork Indian Creek
East Fork Indigo Creek
East Fork Jones Creek
East Fork Kelsey Creek
East Fork Layng Creek
East Fork Lobster Creek
East Fork Luce Creek
East Fork Main Canal
East Fork McCoin Creek
East Fork Meadow Brook
East Fork Mill Creek
East Fork Minnow Creek
East Fork Mosby Creek
East Fork Muir Creek
East Fork Park Creek
East Fork Peavine Creek
East Fork Pine Creek
East Fork Pistol River
East Fork Poole Creek
East Fork Prather Creek
East Fork Quarry Creek
East Fork Rattlesnake Creek
East Fork Reservoir
East Fork Rock Creek
East Fork Salmon River
East Fork Scott Creek
East Fork Shively Creek
East Fork South Fork Trask River
East Fork Sru Creek
East waqímatáw Creek
East Fork Steamboat Creek
East Fork Stouts Creek
East Fork Sucker Creek Trail
East Fork Sumac Creek
East Fork Sunshine Creek
East Fork Tamarack Creek
East Fork Thirtymile Creek
East Fork Trout Creek
East Fork Wallowa River
East Fork Warrens Creek
East Fork Way
East Fork Williams Creek
East Fork Winchuck River
East Fork Wolf Creek
East Gardiner
East Grossman Creek
East Gulch
East Hanks Lake
East Lake
East Lateral
East Long Hollow
East Lostine River
East McFarland Lake
East Meacham Creek
East Mountain
East Muley Creek
East Pass Creek
East Peak
East Phillips Creek
East Pine Creek
East Point
East Porter Creek
East Rock Creek
East Elementary School
East Scotty Creek
East Sheep Creek
East Shotgun Spring
East Springer Spring
East Stack Creek
East Tanner Creek
East Tanner Lake
East Ten Cent Creek
East West Trail
East Willow Creek
East Windfall Creek
East Witham Creek
East Wolf Creek
East Zigzag Mountain Trail
Eastern Brook Lake
Easy Creek
Eaton Butte
Eb Lake
Echo Canyon
Echo Creek
Echo Creek
Echo Creek Trail
Echo Falls
Echo Island
Echo Lake
Echo Lake
Echo Mountain
Echo Point
Echo Spring
Echo Valley
Eckman Creek
Eden Park
Eden Ridge
Eden Valley
Edgewood Mountain
Edgewood Spring
Edison Butte
Edison Ice Cave Trail
Edmonds Creek
Edmonds Mine
Edmonson Spring
Edna Mine
Lake Edna
Ednas Point
Eds Meadow
Edson Butte
Edson Creek
Edson Creek
Eel Creek
Eel Creek Recreation Site
Eel Lake
Egan Memorial Lodge (historical)
Egan Springs
Egg Creek
Egg Spring
Egglestron Creek
Egypt Canyon
Egypt Creek
Egypt Well
Eight Dollar Mountain
Eight Lakes Basin
Eight Lakes Creek
Eighth Creek
Eightmile Creek
Eightmile Creek
Eightmile Meadow
Eightmile Point
Eightmile Prairie Mountain
Eighty Acre Creek
Eileen Lake
Elbow Butte
Elbow Canyon
Elbow Creek
Elbow Gulch
Elbow Lake
Elbow Lake
Elder Cabin
Elder Creek
Elder Creek
Elder Flat
Elder Mountain
Elderberry Flat
Eldorado Ditch
Eldorado Pass
Elephant Butte
Elephant Head
Elephant Mountain
Elephant Mountain
Elephant Rock
Elephant Rock
Elephant Rock Creek
Elephants Back
Elgin
Elgin Cemetery
Mount Elijah
Eliot Branch
Eliot Glacier
Lake Elizabeth
Elk Camp Shelter
Elk Camp Spring
Elk Camp Spring
Elk City
Elk Cove
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Big Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek
Elk Creek Falls Recreation Site
Elk Creek Recreation Site
Elk Creek Trail
Elk Flat
Elk Flat
Elk Flat
Elk Flat Creek
Elk Flat Spring
Elk Glade
Elk Grove
Elk Grove Trail
Elk Horn Creek
Elk Lake
Elk Lake
Elk Lake
Elk Lake Creek
Elk Lake Trail
Elk Lick
Elk Meadows
Elk Meadows
Elk Meadows Trail
Elk Mountain
Elk Mountain
Elk Mountain
Elk Mountain
Elk Mountain
Elk Mountain
Elk Mountain Trail
Elk Ridge
Elk River
Elk Spring
Elk Spring
Elk Spring
Elk Spring
Elk Trail Elementary School
Elk Wallow
Elk Wallow Creek
Elk Wallow Spring
Elk Wallow Spring
Elk Wallow Spring
Elk Wallows
Elkhorn
Elkhorn Camp
Elkhorn Cow Camp
Elkhorn Creek
Elkhorn Creek
Elkhorn Creek
Elkhorn Creek
Elkhorn Creek
Elkhorn Creek
Elkhorn Creek
Elkhorn Lake
Elkhorn Mine
Elkhorn Mountain
Elkhorn Peak
Elkhorn Peak
Elkhorn Prairie
Elkhorn Spring
Elkhorn Spring
Elkhorn Valley
Ellen Creek
Ellick Creek
Elliot Creek
Elliot Creek
Elliott Creek Ridge
Elliot Spring
Elliot Spring
Elliott Creek
Elliott State Forest
Ellis Canyon
Ellis Creek
Ellis Creek
Ellis Forest Service Station
Elma Creek
Elmer Creek
Elms Ditch
Elms Reservoir
Eloise Lake
Elos Prairie
Elowah Falls
Elwood
Emerald Lake
Emerson Creek
Emerson Ranch
Emery Canyon
Emery Well
Emigrant Butte
Emigrant Butte
Emigrant Creek
Emigrant Creek
Emigrant Creek
Emigrant Crossing (historical)
Emigrant Forest Camp
Emigrant Lake
Emigrant Pass
Emigrant Reservoir
Emigrant Springs State Heritage Area
Emil Creek
Emil Creek Reservoir
Emile Creek
Emile Creek
Emile Falls
Emile Shelter Recreation Site
Emile Trail
Emily Cabin
Emily Creek
Emily Creek Way
Mount Emily
Empire Gulch
Empire Lakes
End Creek
End Spring
End Spring
Engineers Creek
English Spring
Enid Lake
Ennis Butte
Ennis Creek
Enola Hill
Enterprise
Erhart Lake
Erickson Creek
Erickson Ranch
Erlebach Ranch
Ernest Creek
Ernie Spring
Erskine Beal Spring
Escondia Gulch
Eslick Creek
Esmond Creek
Esmond Mountain
Estep Creek
Esterly Lakes
Esterly Mine
Estes Creek
Esther Creek
Etelka School (historical)
Ethel Creek
Ethel Mountain
Ethel Creek
Etta Prairie
Euchre Creek
Euchre Creek
Euchre Mountain
Eugene Creek
Eugene Glacier
Eureka Bar
Eureka Creek
Eureka Gulch
Eureka Mine
Eureka Mine
Eureka Mine
Eureka Peak
Eureka Peak Trail
Eureka Spring
Eustis Meadow
Evangeline Creek
Evans
Evans Creek
Evans Creek
Evans Creek
Evans Creek
Evans Mountain
Evans Trail
Evans Well
Evarts Creek
Evening Creek
Evergreen Creek
Evergreen Creek
Everton Riffle
Evick Spring
Ewe Creek
Ewing Spring
Excelsior Gulch
Experiment Creek
Starkey Experimental Forest Headquarters
F L Spring
Failor Creek
Fairchild Point
Fairchild Spring
Fairview
Fairview Creek
Fairview Creek
Fairview Meadow
Fairview Mountain
Fairview Mountain
Fairview Mountain
Fairview Peak
Fairview Spring
Fairy Creek
Fairy Shelter
Faith Spring
Falcon Butte
Falcon Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek
Fall Creek Cabin
Fall Creek Falls
Fall Creek Guard Station
Fall Creek Trail (historical)
Fall Gulch
Fall Mountain
Fall Mountain
Fall Mountain Spring
Fall River
Fall River Recreation Site
Fall River Falls
Fall River Guard Station
Fall River Lodge
Fall Valley
Falls Creek
Falls Creek
Falls Creek
Falls Creek
Falls Creek Forest Camp
Fan Creek
Fan Creek
Fan Creek
Fantail Creek
Fantail Spring
Fanton Plaza Trail
Fantz Ranch
Farewell Bend Recreation Site
Farewell Spring
Farley Spring
Farley Spring
Farley Spring Trail
Farlow Hill
Farm Creek
Farm Trail
Farmer Creek
Farmer Creek
Farmers Ditch
Farmers Ditch
Farrell Lake
Farva Creek
Fashion Reef
Fate Creek
Father Mountain
Faubion
Faught Creek
Fawcett Creek
Fawn Butte
Fawn Camp
Fawn Camp Trail
Fawn Creek
Fawn Creek
Fawn Creek
Fawn Creek
Fawn Creek
Fawn Creek
Fawn Lake
Fawn Lake
Fawn Lake Trail
Fawn Lake Way
Fawn Meadow
Fawn Reservoir
Fawn Spring
Fawn Spring
Fawn Spring Trail
Fayes Gulch
Feagin Ranch
Feagles Creek
Federal Spring
Fehley Gulch
Felix Gulch
Feller Pond
Fence Creek
Fence Gulch
Fendall Creek
Ferguson Creek
Ferguson Creek
Ferguson Creek
Ferguson Mountain
Ferguson Ridge
Ferguson Spring
Fern Creek
Fern Creek
Fern Ridge Cemetery
Fern Top
Fernview Recreation Site
Ferriers Gulch
Ferris Creek
Ferris Gulch
Ferry Creek
Ferry County Park
Ferry Road Park
Fiddle Creek
Fiddler Gulch
Fiddlers Hell
Fields
Fields Basin
Fields Creek
Fields Peak
Fifteen Mile Recreation Site
Fifteenmile Creek
Fifteenmile Creek
Fifteenmile Creek Trail
Fifth Creek
File Butte
Fin Roberts Creek
Finch Lake
Findley Spring
Fine Spring
Fingerboard Gulch
Fingerboard Saddle
Finke Ranch
Finke Spring
Finley Bend
Finley Butte
Findley Buttes
Finley Creek
Finley Creek Cow Camp
Finley Lake
Finley Ridge
Fintcher Creek
Fir Creek
Fir Creek
Fir Creek
Fir Creek
Fir Grove Cemetery
Fir Mountain
Fir Timber Butte
Fir Tree Canyon
Fir Tree Creek
Fir Tree Creek
Fir Tree Campground (historical)
Fir Tree Spring
Fir Tree Spring
Fir Tree Spring
Fire Butte
Fire Creek
Fire Creek
Fire Spring
Fire Spring
Fire Spring
Firecamp Lakes
Fireline Creek
Firemans Leap
Firestone Butte
Firo
First Creek
First Creek
First Creek
First Creek
First Creek
First Creek Camp
First Gulch
First Lake
First Peak
First Prairie Mountain
Firwood
Fischer Creek
Fischer Island
Fish Creek
Fish Creek
Fish Creek
Fish Creek
Fish Creek Desert
Fish Creek Divide
Fish Creek Recreation Site
Fish Creek Mountain
Fish Creek Shelter
Fish Creek Valley
Fish Hook Camp (historical)
Fish Hook Peak
Fish Lake
Fish Lake
Fish Lake
Fish Lake
Fish Lake
Fish Lake
Fish Lake Creek
Fish Lake Creek
Fish Lake Recreation Site
Fish Lake Remount Depot
Fish Lake Resort
Fish Lake Trail
Fish Lake Trail
Fish Mountain
Fisher
Fisher Creek
Fisher Creek
Fisher Creek
Fisher Creek
Fisher Creek
Fisher Creek
Fisher Point
Fisher Slough
Fishers Bar
Fishhole Creek
Fisk Creek
Fisk Gulch
Fitt Creek
Fitzgerald Ranch
Fitzpatrick Ridge
Fitzwater Pass
Fitzwater Pass Spring
Fitzwater Point
Five Finger Gulch
Five Hundred Flat
Five Minute Draw
Five Points Creek
Five Points Creek
Five Points Trail
Five Rivers
Five Sticks Camp
Fivemile Butte
Fivemile Butte
Fivemile Cow Camp
Fivemile Creek
Fivemile Creek
Fivemile Creek
Fivemile Creek
Fivemile Shelter
Fivemile Well
Fivepoint Hill
Five Corners
Fizz Spring
Flag Creek
Flag Mountain
Flag Mountain Trail
Flag Point
Flag Point Trail
Flag Prairie
Flagstaff Point
Flagstone Creek
Flagstone Peak
Flagtail Cow Camp
Flagtail Creek
Flagtail Mountain
Flannigan Creek
Flannigan Prairie
Flapper Springs Guard Station
Flat Creek
Flat Creek
Flat Creek
Flat Creek
Flat Creek
Flat Creek
Flat Creek
Flat Creek
Flat Creek Work Station
Flat Creek Spring
Flat Creek Trail
Flat Mountain
Flat Reservoir
Flat Rock
Flat Rock Branch
Flat Rock Spring
Flat Spring
Flat Top
Flat Top
Flatiron Point
Flatiron Spring
Flats Ranch
Flea Creek
Fleece Ridge
Fleming Canyon
Flesher Slough
Fletcher Cemetery
Flexer Spring
Flood Meadow
Flora
Flora Dell Creek
Floras Creek
Florence
Florence Cabin
Florence Creek
Florida Creek
Flounce Rock
Flower Pot (historical)
Flowers Gulch
Flume Canyon
Fly Creek
Fly Creek
Fly Creek
Fly Creek
Fly Creek Canyon
Fly Creek Ranch
Fly Creek Trail
Fly Lake
Fly Lake
Fly Lake Lookout
Flycatcher Spring
Flying W Spring
Flynn
Flynn Creek
Flynn Reservoir
Flynn Spring
Foggy Creek
Foland Creek
Foley Butte
Foley Creek
Foley Ridge Trail
Foley Spring
Folk Creek
Folsoms Spring
Fools Canyon
Foot Creek
Footbridge Mine
Fopian Campground
Fopian Creek
Foreman Point
Target Meadows Campground
Cedar Creek
Forest Creek
Forest Creek Trail
Forestvale Cemetery
Fork Lake
Forked Butte
Forked Horn Butte
Forked Horn Springs
Forks Guard Station
Forks Reservoir
Forks Ridge
Forks Tank
Formader Ridge
Forshey Creek
Forshey Meadow
Fort Butte
Fort Creek
Fort Creek
Fort Creek
Fort Harney (historical)
Fort Hill Census Designated Place
Fort Hill
Fort Klamath
Fort Klamath Elementary School (historical)
Fort Klamath Junction (historical)
Fort Rock
Fort Rock Valley
Fort Spring
Fort Vannoy Elementary School
Forty-five Spring
Fortynine Spring
Foss Spring
Foss Spring
Fosback Marsh
Foster Butte
Foster Butte
Foster Creek
Foster Creek
Foster Creek
Foster Creek Forest Camp
Foster Field
Foster Flat Meadow
Foster Glades
Foster Gulch
Foster Lake
Foster Ranch
Fosters Temple
Found Creek
Found Lake
Foundation Creek
Foundation Spring
Foundation Spring
Four in One Cone
Four Bar Spring
Four Cabin Corner
Four Corners
Four Corners
Four Corners
Four Corners Recreation Site
Four Horse Smith Spring
Four O'Clock Lake
Four One Half Mile Bridge
Four-bit Flat
Fourbit Creek
Fourbit Ford
Fourmile Butte
Fourmile Canyon
Fourmile Creek
Fourmile Creek
Fourmile Creek
Fourmile Creek
Fourmile Gap
Fourmile Spring
Fourmile Spring
Fourmile Springs
Fourth of July Creek
Fourth of July Spring
Fourth Creek
Fourth Creek
Fourth Creek Trail Spring
Fowler Creek
Fowler Spring
Fox
Fox Butte
Fox Canyon Creek
Fox Corral
Fox Creek
Fox Creek
Fox Creek
Fox Creek
Little Fall Creek
Fox Creek
Fox Creek
Fox Creek
Fox Creek Trail
Fox Hill
Fox Mill
Fox Point
North Fox Reservoir
Fox Spring
Fox Spring
Frailey Point
Frailey Point Trail
Frakes Cabin
Francis Creek
Francis Creek
Francis Lake
Francis Way
Lake Francis
Frankie and Johnny Spring
Franklin Creek
Franklin Mountain
Franklin School
Franks Creek
Frantz Creek
Frantz Meadow
Franz
Frazier
Frazier Recreation Site
Frazier Creek
Frazier Creek
Frazier Creek
Frazier Creek
Frazier Guard Station
Frazier Lake
Frazier Meadow
Frazier Mountain
Frazier Pass
Frazier Point
Frazier Spring
Fred Creek
Fred Creek Lake
McNeil Recreation Site
Freddy Camp
Fredenburg Spring
Frederick Lateral
Free and Easy Creek
Free and Easy Pass
Freeland Mountain
Freeman Creek
Freeman Ranch
Freeman Spring
Freezeout Cabin
Freezeout Camp
Freezeout Creek
Freezeout Creek
Freezeout Creek
Freezeout Ridge
Freezeout Saddle
Freezeout School (historical)
Freezeout Trail
Freezeout Trail
Fremont Canyon
Fremont Meadow
Fremont Point
Fremont Powerhouse
Fremont - Hay Elementary School
French Corral Meadow
French Corral Spring
French Creek
French Creek
French Creek
French Creek
French Creek Ridge
French Creek Trail
French Diggings
French Flat
French Camp Recreation Site
French Gulch
French Gulch
French Gulch Divide
French Pass
French Peak
French Pete Creek
French Spring
Frenchman Camp Trail
Frenchy Butte
Frenchy Spring
Fresno Creek
Fret Creek
Frey Creek
Freye Lake
Friday Creek
Friend (historical)
Friendship Cemetery
Frier Spring
Friese Creek
Fritsche Cabin
Fritts Spring
Fritz Creek
Frizzel Mountain
Frizzell Creek
Frog Camp (historical)
Frog Camp Creek
Frog Creek
Frog Creek Trail
Frog Heaven Meadow
Frog Lake
Frog Lake
Frog Lake
Frog Lake
Frog Lake Buttes
Frog Pond
Frog Pond
Frog Pond Butte
Frog Pond Mine
Frog Ponds
Frog Reservoir
Frog Spring
Frost Mill
Frosty Gulch
Fruitdale Creek
Fruitdale Elementary School
Fry Creek
Fry Gulch
Fry Meadow
Fry Meadow Creek
Fry Meadow Guard Station
Fry Place
Fry Spring
Frying Pan Lake
Frying Pan Spring
Fryingpan Creek
Fryrear Butte
Frys Camp Spring
Fuego
Fuego Mountain
Fuqua Creek
Fuji Creek
Fuji Meadow
Fuji Mountain
Fuji Mountain Trail
Fulk Cabin
Fuller Creek
Fuller Creek
Fuller Lake
Fuller Mine
Fulton Creek
Funny Bug Basin Spring
Funny Butte
Furnish Creek
Fuzztail Butte
Fuzzy Gulch
Kelley Creek
Gabe Creek
Gabe Spring
Gabe Spring
Gable Creek
Gable Creek School (historical)
Gabriel City Park
Gabriel Spring
Gacey Spring
Gaerky Creek
Gailord Gulch
Gaily Creek
Galena
Galena Creek
Galena Mountain
Gales Creek
Gales Landing
Galice
Galice Creek
Galloway Cemetery
Galloway Spring
Game Lake
Game Lake Lookout (historical)
Gand Saddle
Gander Lake
Garden Creek
Garden Creek
Garden Gulch
Garden Spring
Gardiner
Gardiner Reservoir
Gardener Butte
Gardner Peak
Gardner Ranch
Gardner Ridge
Garfield Peak
Garfield Peak Trail
Garfield Elementary School
Garrett Basin Spring
Garrett Place
Garrett Ridge
Garrison Butte
Garrison Lake
Garvin Gulch
Garwood Butte
Garwood Creek
Gate Creek
Gate Creek
Gate Creek
Gauldy Ridge
Mount Gauldy
Gay Spring
Gaylord
Gaywas Peak
Gearhart Mountain
Gearhart Trail
Geary Creek
Geary Meadow
Geisel Monument State Park
Geiser
Geiser Creek
Gellatly Creek
Gellatly Creek
Gem Quartz Mine
General Patch Bridge (historical)
Geneva Bar
Gentry Creek
George W Joseph State Park
George
George Creek
George Creek
George Creek
George Lake
George T Gerlinger State Experimental Forest
Georgia Creek
Geppert Butte
Gerking Spring
German Cemetery
Gerow Butte
Gertrude Lake
Getchel Ridge
Geyser Spring
Ghost Creek
Ghost Ridge
Gib Spring
Gibbon
Gibbon Ridge
Gibbs Creek
Gibraltar Creek
Gibson Creek
Gibson Creek
Gibson Gulch
Gibson Hill
Gibson Lake
Gibson Prairie
Gideon Creek
Gifford Lakes
Gilbert Creek
Gilbert Creek
Gilbert Ridge
Gilbert Ridge Spring
Gilchrist
Gilchrist Butte
Gilchrist Butte
Gilchrist Junction
Gilchrist Reservoir
Gilchrist Spring
Gill Ranch
Gilligan Butte
Gilligan Creek
Gilman Canyon
Gilman Canyon
Gilman Flat
Gilman Ranch
Gilmore Creek
Gilmore Cutoff Trail
Gilson Creek
Gilson Gulch
Gimlet Creek
Ginger Creek
Ginkgo Creek
Ginkgo Trail
Git'em Creek
Glacier Creek
Glacier Lake
Glacier Mountain
Glacier Mountain
Glacier Pass
Glacier Way
Glade Creek
Glade Creek
Glade Creek
Glade Creek
Glade Creek Trail
Glade Fork
Glade Ski Trail
Glades Well
Lake Gladys
Glasgow
Glasgow Point
Glass Mountain
Glass Mountain Spring
Glaze Meadow
Gleason Spring
Glenada
Gleneden Lake
Glenn Canyon
Glenn Ridge
Glines Creek
Glisan Glacier
Glutton Falls Canyon
Gnarl Ridge Trail
Gnat Lake
Goat Cabin Ridge
Goat Creek
Goat Creek
Goat Creek
Goat Island
Goat Mountain
Goat Mountain
Goat Peak
Gobblers Knob
Gobblers Knob
Gobel Creek
Gobel Creek Trail
Gober Spring
God Butte
God Creek
Godfrey Glen and Colonnades
Godias Creek
Godowa Spring
Goebel Canyon
Goen Creek
Goff Canyon
Golars Goat Trail
Gold Basin
Gold Basin Butte
Gold Beach
Gold Bug Mine
Gold Butte
Gold Center
Gold Creek
Gold Creek
Gold Creek
Gold Creek
Gold Creek
Gold Creek
Gold Creek
Gold Creek
Gold Creek
Gold Creek
Gold Dollar Creek
Gold Hill
Gold King Creek
Gold Lake
Gold Lake Trail
Gold Mountain
Gold Mountain Creek
Gold Pan Placer Mine
Gold Peak
Gold Plate Mine
Gold Point
Gold Point Trail
Golden Basin
Golden Boy Mine
Golden Creek
Golden Curry Creek
Golden Eagle Mine
Golden Gate Mine
Golden Gulch
Golden Lake
Golden Stairs Trail
Golden Wedge Mine
Golden West Mine
Goldeneye Lake
Goldie Spring
Gone Creek Recreation Site
Goodfellow Lakes
Goodman Creek
Goodman Ridge
Goodwater Spring
Goodwin Creek
Goofy Spring
Goolaway Gap
Goose Creek
Goose Creek
Goose Egg
Goose Lake
Goose Lake
Goose Lake Trail
Goose Nest
Gooseberry Creek
Gopher Creek
Gopher Ridge
Gopher Spring
Gordan Peak
Gordan Peak Trail
Gordey Creek
Gordon Butte
Gordon Butte
Gordon Butte Trail
Gordon Creek
Gordon Creek
Gordon Lakes
Gorge Camp
Gorge Creek
Gorr Island
Gorton Creek
Goslin Corral
Gosling Lakes
Goss Ranch
Goss Trail
Gotcher Cemetery
Gould Creek
Gould Gulch
Gover Reservoir
Government Harvey Pass
Government Cove
Government Spring
Government Spring
Governor Patterson Memorial State Recreation Site
Governors Bay
Gowdy Ranch
Gowing Creek
Gabenheim Creek
Grade Creek
Gradon Canyon
Graham Butte
Graham Corral Horse Camp
Graham Creek
Graham Creek
Graham Creek
Graham Creek
Graham Mountain
Graham Pass
Graham Spring
Grand Ronde
Grand Ronde Agency
Granddad Butte
Grandview
Grandview Campground
Grandview Spring
Granger Ditch
Granite
Granite Boulder Creek
Granite Butte
Granite Butte
Granite Cliff
Granite Creek
Granite Creek
Granite Creek
Granite Creek
Granite Creek
Granite Creek
Granite Creek
Granite Creek
Granite Creek
Granite Creek
Granite Gulch
Granite Hill Mine
Granite Meadows
Granite Peak
Granite Peaks
Granite Spring
Granite Spring
Granny Creek
Granny Spring
Granny View Point
Grannys Run
Grant Butte
Grant Creek
Grant Creek
Grant Creek
Grant Creek
Grant Creek
Grant Creek
Grant Meadows
Grant Union High School
Grantham Gulch
Grants Pass
Grants Pass Peak
Grapefruit Creek
Grass Creek
Grass Creek
Grass Creek
Grass Creek
Grass Lake
Grass Mountain
Grass Mountain
Grass Mountain Trail
Grass Spring
Grasshopper Creek
Grasshopper Creek
Grasshopper Flat
Grasshopper Mountain
Grasshopper Mountain
Grasshopper Point
Grasshopper Point
Grasshopper Trail
Grassy Butte
Grassy Butte Creek
Grassy Creek
Grassy Glade
Grassy Knob
Grassy Knob Trail
Grassy Knoll
Grassy Lake
Grassy Pond
Grassy Ranch Camp
Grassy Ranch Trail
Grassy Spring
Grave Creek
Grave Creek
Grave Creek
Grave Creek Trail
Gravel Butte
Gravel Creek
Gravel Creek
Gravel Ridges
Gravel Spring
Graves Butte
Graves Creek
Graveyard Point
Graveyard Butte
Graveyard Gulch
Graveyard Gulch
Gravy Creek
Gravy Gulch
Gray Butte
Gray Butte Cemetery
Gray Creek
Gray Creek
Gray Creek
Gray Creek
Gray Creek
Gray Eagle Mine
Gray Gulch
Gray Prairie
Gray Rock
Grayback Clapboard Trail
Grayback Creek
Grayback Recreation Site
Grayback Glades
Grayback Mountain
Grayback Ridge
Grayback Shelter
Graylock Butte
Grays Creek
Grays Creek
Greasy Creek
Great Northern Mine
Greely Creek
Green Acres
Green Butte
Green Butte
Green Butte
Green Butte
Green Craggie
Green Creek
Green Creek
Green Creek
Green Creek
Green Creek
Green Creek Meadow
Green Knob
Green Lake
Green Lake
Green Lake
Green Lake Creek
Green Lakes
Green Lakes Trail
Green Mountain
Green Mountain
Green Mountain
Green Mountain
Green Mountain
Green Mountain
Green Mountain
Green Mountain
Green Mountain
Green Mountain
Green Point
Green Point Creek
Green Point Lower Reservoir
Green Point Mountain
Green Point Upper Reservoir
Green Ridge
Green River
Green Spring
Green Valley
Green Valley
Green Valley Spring
Green Valley Trail
Greenhorn
Greenhorn Creek
Greenleaf
Greenleaf Creek
Greenley Gulch
Greenman Creek
Greens Creek
Greenspring Draw
Greentop
Greenwood Cemetery
Gregg Creek
Greggs Creek
Gregory (historical)
Grenada Butte
Grey Rock
Greylock Mountain
Greylock Mountain Trail
Griffin Camp Spring
Griffin Creek
Griffin Creek
Griffin Creek Reservoir
Griffin Meadow
Griffin Pass
Griffin Ranch
Griffis Creek Trail
Griffith Creek
Griffith Creek
Griggs
Grimes Creek
Grimmet Spring
Grindstone Camp
Grindstone Creek
Grindstone Recreation Site
Grindstone Mountain
Griswell Creek
Grizzly
Grizzly Creek
Grizzly Creek
Grizzly Creek
Grizzly Creek
Grizzly Creek
Grizzly Flat
Grizzly Flats
Grizzly Gulch
Grizzly Mine
Grizzly Mountain
Grizzly Mountain
Grizzly Peak
Grizzly Peak
Grizzly Ridge
Groshen Cabin
Groshen Trail
Grossman Creek
Grotto Cove
Groundhog Mountain
Groundhog Knoll
Grouse Butte
Grouse Canyon
Grouse Creek
Grouse Creek
Grouse Creek
Grouse Creek
Grouse Creek
Grouse Creek
Grouse Creek
Grouse Hill
Grouse Knob
Grouse Mountain
Grouse Mountain
Grouse Mountain
Grouse Mountain Falls
Grouse Point
Grouse Ridge
Grouse Spring
Grouse Spring
Grouse Spring
Grouse Spring Trail (historical)
Grouslous Mountain
Grub Box Gap
Grub Creek
Grub Gulch
Grub Spring Reservoir
Grubstake Mine
Gulliford Crossing
Gulliford Spring
Gulling
Gully Spring
Gumboot Butte
Gumboot Creek
Gumjuwac Creek
Gumjuwac Saddle
Gunbarrel Creek
Gunderson Creek
Gunsight Butte
Gunther Cabin Springs
Gunther Creek
Gunther Spring
Gurdane Creek
Gus Well
Gutherie Prairie
Gutridge Creek
Gutridge Mine
Guy W Talbot State Park
Guyer Creek
Guyon Basin
Guyon Spring
Gwyn Creek
Gwynn Creek
Gwynn Knoll
Gyp Creek
Gyp Point
Gyppo Creek
Gypsy Fork
Gypsy Spring
H and Y Cabin
H J Baker Ranch
H J Spring
H K Spring
Haas Hollow
Haas Ridge
Hack Hollow
Hackleman Creek
Hackman Creek
Haden Creek
Hadley Butte
Hadley Creek
Hadsall Creek
Hagar Creek
Hagar Ridge
Hagen Creek
Hagen Ridge
Hager Mountain
Hager Spring
Hakki Creek
Hald Butte
Culver IOOF Cemetery
Hale Meadow
Hale Ranch
Hale Spring
Hale Spring Trail
Half Moon Bar
Half Moon Spring
Half-pint Creek
Halfway
Halfway Creek
Halfway Hill
Halfway House
Halfway Lake
Halfway Reservoir
Halfway Spring
Halfway Spring
Halfway Spring
Halfway Spring
Halifax Creek
Halifax Trail
Hall Cabin
Hall Creek
Hall Creek
Hall Creek
Hall Ranch
Hall Ridge
Hall Slough
Hallet Spring
Hallock Spring
Halls Cabin
Halls Lake
Halo Creek
Hamaker Bluff
Hamaker Butte
Hamaker Creek
Hamaker Meadows
Hamaker Mountain
Hambone Butte
Hambone Trail
Hamelton Butte
Hamilton
Hamilton Butte
Hamilton Canyon
Hamilton Creek
Hamilton Creek
Hamilton Mountain
Hamilton Ranch
Hamilton Spring
Hamlin Prairie
Hammer Creek
Hammer Creek Spring
Hammersley Canyon
Hamms Spring
Hamner Butte
Hamner Creek
Hamner Creek Way
Hampton
Hanan Spring
Hanan Trail
Hanchet Creek
Hand Creek
Hand Lake
Hand Lake
Handy Spring
Haner Butte
Hanks Lake
Hanley Gulch
Hanscombe Creek
Hanscombe Mountain
Hansen Creek
Hansen Mine
Hansen Saddle
Hanson Canyon
Hanson Creek
Happy Camp
Happy Camp Creek
Happy Camp Spring
Happy Canyon
Happy Creek
Happy Creek
Happy Creek
Happy Hollow
Happy Home Spring
Happy Jack Camp
Happy Jack Creek
Happy Jack Spring
Happy Lake
Happy Prairie
Happy Prairie
Happy Prairie Way
Happy Reservoir
Happy Ridge
Happy Spring
Happy Valley
Happy Valley
Happy Valley Ditch
Harbor
Hardesty Mountain
Harding Butte
College Hill High School
Hardscrabble Mountain
Hardscrabble Ridge
Hardy Creek
Hardy Ridge
Hardy Spring
Hare Gulch
Harer Canyon
Haring Creek
Harl Butte
Harlan Creek
Harlequin Lake
Harmon Spring
Harney
Harney Road Spring
Harp Mountain
Harp Spring
Harper Bridge
Harper Creek
Harper Creek
Harper Gulch
Harper Meadow
Harpham Spring
Harphan Creek
Lake Harriette
Harriman Lodge
Mount Harriman
Harrington Creek
Harrington Spring
Harris
Harris Beach State Park
Harris Canyon
Harris Creek
Harris Creek
Mount Harris
Harrison Mountain
Harrison Spring
Harry Creek
Harter Creek
Harter Mountain
Hartley Cemetery
Hartley Creek
Harve Creek
Harvey Creek
Harvey Creek
Harvey Creek
Harvey Creek
Harvey Flat
Harvey Gap
Harvey Lake
Harvey Lake
Harvey Spring
Hascall Spring
Hash Rock
Hash Rock Creek
Haskins Creek
Hass Creek
Hasting Spring
Hat Creek
Hat Point
Hat Spring
Hatchery Creek
Hatchet Creek
Hatfield Spring
Hathaway Mead
Hattie Creek
Hattie Spring
Hauser
Hauser Substation
Haw Cabin
Hawk Creek
Hawk Creek
Hawk Creek
Hawk Creek
Hawk Creek
Hawk Creek Station
Hawk Mountain
Hawk Mountain
Hawk Spring
Hawkins Butte
Hawkins Creek
Hawkins Creek
Hawkins Pass
Hawks Mountain
Hawks Rest
Hawley Butte
Hawley Creek
Hawley Ditch
Hawley Gulch
Hawthorne Spring
Hay Barn Creek
Hay Creek
Hay Creek
Hay Creek
Hay Creek
Hay Creek Cemetery
Hay Creek Ranch
Hay Creek Ranch
Hay Flat
Hay Pen Camp
Hay School (historical)
Hayden Creek
Hayden Creek
Hayden Glacier
Hayden Prairie
Hayes Creek
Hayes Hill
Haynes Inlet
Haypress Creek
Hayrick Butte
Hays Canyon
Hays Creek
Hays Gulch
Haystack Butte
Haystack Cemetery
Haystack Creek
Haystack Dam
Haystack Draw
Haystack Meadow
Haystack Reservoir
Haystack Rock
Haystack Rock
Haystack Spring
Hayward Peak
Hazel Camp
Hazel Camp Trail
Hazel Creek
Hazel Creek
Hazel Hollow
Hazel Lake
Hazel Mountain
Lake Hazel
Head Lake
Head O'Boulder Camp
Headquarters Camp
Heart Lake
Heater Creek
Heather
Heather Creek
Heather Lake
Heather Mountain
Heavenly Twin Lakes
Hebo
Hebo Lake
Hebo Work Camp
Mount Hebo
Heceta Junction
Heckletooth Mountain
Heckman Reservoir
Hedgepath Creek
Heflin Creek
Heflin Spring
Hegel Spring
Hehe Creek
Heisler Creek
Helen Creek
Helen Creek Way
Helena Mine
Helens Spring
Hell for Slim Draw
Hellbore Spring
Hellgate Canyon
Hellhole Creek
Hellion Canyon
Hellion Rapids
Hello Boy Spring
Hellroaring Creek
Hells Canyon Creek
Hells Half Acre
Hells Island
Hells Peak
Helms Creek
Helphenstein Creek
Hemlock
Hemlock Butte
Hemlock Butte
Hemlock Butte
Hemlock Creek
Hemlock Creek
Hemlock Creek
Hemlock Lake
Hemlock Lake
Hemlock Lake
Hemlock Lake Trail
Hemlock Spring
Hemp Spring
Henderson Cove
Henderson Creek
Henderson Creek
Henderson Marsh
Henderson Peak
Hendricks Creek
Henkle Butte
Henline Creek
Henline Mountain
Henline Mountain Lookout
Henry Canyon
Henry Creek
Henry Creek
Henry Creek
Henry Creek
Hensley Butte
Hensley Creek
Hepburn Creek
Heppsie Mountain
Herb Lake
Herberger Spring
Herbst Place
Herburger Cabin
Herder Spring
Herman Creek
Herman Creek
Herman Creek
Herman Creek Trail
Herman Peak
Herman Spring
Herren Creek
Herren Meadow
Herron Ridge
Hershberger Creek
Hershberger Mountain
Hesslan Canyon
Hewed Log Creek
Hewed Log Spring
Hewitt Creek
Hi Yu Guard Station
Hiack Creek
Hickey Basin Reservoir
Hickey Creek
Hickey Creek
Hickey Meadow
Hickey Ranch
Hickey Reservoir
Hickey Reservoir
Hickman Butte
Hickman Creek
Hickman Lake
Hicks Creek
Hicks Lake
Hicks Spring
Hidaway Creek
Hideaway Lake
Hidaway Meadows
Hidaway Springs
Hidden Lake
Hidden Lake
Hidden Lake
Hidden Lake Trail
Hidden Meadow
Hidden Spring
Hidden Spring
Hidden Spring
Hidden Valley
Hyde Creek
Hideaway Spring
Hideaway Spring
Higgins Creek
Higgins Spring
High Bridge
High Camp
High Camp Creek
High Camp Lookout
High Camp Trail
High Creek
High Creek
High Deck
High Divide Trail
High Hat Butte
High Horn Creek
High Horn Reservoir
High Knob
High Lake
High Lake
High Peak
High Prairie
High Prairie
High Prairie
High Prairie
High Ridge
High Ridge
High Rock
High Rock Spring Recreation Site
High Spring Ridge
High Tableland
High Trail
High Trail
Highland Cabin
Highland Ditch
Highland Flat
Linus Pauling Middle School
Highline Canal
Highrock Creek
Highrock Mountain
Lake Hilda
Hildebrand
Hill Creek
Hill Creek
Hill Creek
Hill Ranch
Hillcrest Elementary School
Hilliker Gulch
Hillman Peak
Hillockburn Guard Station (historical)
Hillockburn Spring
Hills Creek
Hills Creek Trail
Hills Peak
Hillside Spring
Hilton Gulch
Hilton Ridge
Himmelwright Spring
Hinkle Gulch
Hinkle Lake
Hinton Creek
Hinton Creek
Idaho Point
Hinton Ranch
Hinton Spring
Hipower Bluffs
Hipower Creek
Hiyu Mountain
Hiyu Ridge
Hiyu Trail
Hobo Creek
Hobo Lake
Hobson Horn
Hoffman Creek
Hoffman Creek
Hoffman Ranch
Hoffman Spring
Hoffman Spring
Hog Creek
Hog Creek
Hog Creek
Hog Creek
Hog Creek
Hog Creek
Hog Creek
Hog Creek Reservoir Number Two
Hog Creek Ridge
Hog Flat
Hog Flat Spring
Hog Island
Hog Mountain
Hogan Spring
Hogback Creek
Hogback Mountain
Holbrook Creek
Holbrook Creek
Holbrook Spring
Holcomb Creek
Holcomb Peak
Holcomb Spring
Holderman Mountain
Holdout Spring
Hole in the Ground
Hole in the Ground
Hole in the Ground
Hole in the Ground Spring
Hole-in-the-Ground
Hole-in-the Ground
Hole-in-the-Ground Spring
Hole-in-the-Wall Park
Holiday Beach
Holland
Holland Meadows
Holland Meadows Trail
Holland Point
Hollenbeck Creek
Hollenbeck Spring
Hollow Log Cow Camp
Hollywood Creek
Hollywood Spring
Holman Creek
Holman Creek
Holmes Canyon
Holmes Cemetery
Holmes Creek
Holmes Ranch
Holst Lake
Holt Creek
Holton Creek
Homestead Camp
Homestead Creek
Homestead Recreation Site
Homestead Ridge
Hominy Creek
Hominy Saddle
Hondu Spring
Honey Creek
Honey Creek
Honey Grove Creek
Honey Lake
Honey Lakes
Jessie M Honeyman Memorial State Park
Honeymoon Basin
Honeymoon Creek
Honeymoon Creek
Honeymoon Creek
Honeysuckle Creek
Honeysuckle Creek
Hon Spring
Hood Creek
Hood Mountain
Hood River
Hood River Meadows
Hood River Valley
Hood River Ranger Station
Hood View Recreation Site
Mount Hood
Mount Hood
Hoodoo Creek
Hoodoo Creek
Hoodoo Spring
Hook Reservoir
Hooks Gulch
Hooligan Hill
Hootnanny Point
Hoover Creek
Hoover Gulch
Hoover Ridge
Hoover Elementary School
Hop Creek
Hope Creek
Hope Gulch
Mount Hope
Hopkins Gulch
Hoppy Spring
Horkelia Meadow
Horn Butte
Horn Creek
Horn Creek
Horn Gap
Horn Gulch
Horner Creek
Horner Ranch
Hornet Reservoir
Horse Basin Creek
Horse Butte
Horse Butte
Horse Canyon
Horse Creek
Horse Creek
Horse Creek
Horse Creek
Horse Creek
Horse Creek
Horse Creek
Horse Creek
Horse Creek
Horse Creek
Horse Creek
Horse Creek
Horse Creek
Horse Creek
Horse Creek
Horse Creek
Horse Creek Cabin
Horse Creek Trail
Horse Creek Trail
Horse Flat
Horse Gulch
Horse Heaven Creek
Horse Heaven Creek
Horse Heaven Creek
Horse Heaven Creek
Horse Heaven Ridge
Horse Lake
Horse Lake Guard Station
Horse Lake Trail
Horse Mountain
Horse Mountain
Horse Mountain
Horse Mountain
Horse Mountain Trail
Horse Pasture Creek
Horse Pasture Ridge
Horse Pasture Ridge Saddle
Horse Prairie
Horse Prairie
Horse Prairie
Horse Prairie
Horse Prairie Creek
Horse Ridge
Horse Ridge
Horse Ridge
Horse Ridge Summit
Horse Sign Butte
Horse Sign Creek
Horse Spring
Horse Spring
Horse Spring
Horse Spring Camp
Horsefly Lake
Horseglade Spring
Horsehead Creek
Horsehead Spring
Horseheaven Creek
Horseshoe Bend
Horseshoe Bend
Horseshoe Butte
Horseshoe Butte
Horseshoe Creek
Horseshoe Creek
Horseshoe Creek
Horseshoe Creek
Horseshoe Lake
Horseshoe Lake
Horseshoe Lake
Horseshoe Lake
Horseshoe Meadow
Horseshoe Prairie
Horseshoe Reservoir
Horseshoe Ridge
Horseshoe Ridge
Horseshoe Ridge Trail
Horseshoe Spring
Horseshoe Spring
Horsetail Creek
Horsetail Falls
Horsethief Meadows
Horsfall Lake
Hortense Lake
Norton Creek
Horton Pass
Horton Reservoir
Hoskins Creek
Hoskins Spring
Hospital Creek
Hot Rocks
Hot Spring
Hot Spring
Hot Springs
Hotel de Bum Camp
Hothole Ridge
Hough Creek
House Creek
House Creek Spring
House Rock
House Rock Recreation Site
Houston Butte
Howard Butte
Howard Butte
Howard Canyon
Howard Creek
Howard Creek
Howard Creek
Howard Creek
Howard Cutoff Trail
Howard Meadow
Howard Meadow
Howard Meadows
Howard Ranch
Howard School (historical)
Howard Valley
Howell Ridge
Howkum Lake
Howland Mine
Howlock Creek
Howlock Mountain
Hoxie Creek
Hoyt Ranch
Hubbard Creek
Hubbard Hill
Hubbard Mound
Hubbel Lake
Huckleberry Butte
Huckleberry Butte
Huckleberry Camp
Huckleberry Creek
Huckleberry Creek
Huckleberry Creek
Huckleberry Creek
Huckleberry Guard Station
Huckleberry Lake
Huckleberry Lake
Huckleberry Lake
Huckleberry Mountain
Huckleberry Mountain
Huckleberry Mountain
Huckleberry Mountain
Huckleberry Mountain
Huckleberry Mountain
Huckleberry Mountain
Huckleberry Mountain Trail
Huckleberry Spring
Huckleberry Spring
Huckleberry Spring
Huckleberry Spring
Huckleberry Spring
Hudson Creek
Hudson Slough
Huff Spring
Huffman Camp Spring
Hugh Spring
Hughet Creek
Hughet Valley
Hughey Creek
Hukill Creek
Hukill Hollow
Hollo Creek
Humboldt Mine
Humbolt Elementary School
Humbug Creek
Humbug Recreation Site
Humbug Mountain
Humbug Mountain State Park
Humbug Ridge Trail
Humdinger Mine
Hummingbird Creek
Hummingbird Mountain
Humpback Mine
Humphreys Camp
Humpy Mountain
Hunchback Mountain
Hunchback Mountain Trail
Hungry Creek
Hungry Hill
Hunsaker Creek
Hunt Canyon
Hunt Cove
Hunt Creek
Hunt Gulch
Hunt Spring
Hunter Butte
Hunter Camp
Hunter Camp Way
Hunter Creek
Hunter Creek
Hunter Creek
Hunter Creek
Hunter Creek
Hunter Creek
Hunter Creek Trail
Hunter Hill
Hunter Hill Pass
Hunter Spring
Hunter Spring
Hunter Spring
Hunter Spring
Hunter Spring
Hunter Spring
Hunters Cabin Spring
Hunters Camp
Hunters Cove
Hunters Hot Springs
Hunters Island
Hunters Spring
Hunters Spring
Hunting Camp Cow Camp
Hunting Camp Ridge
Huntley Spring
Hunts Cove
Hunts Creek
Hunts Lake
Hurbers Canyon
Huron
Hurricane Creek
Hurricane Creek Recreation Site
Hurricane Ditch
Hurricane Divide
Hurricane Grange
Hurryon Creek
Hurt Cabin
Hurwal Divide
Husband Lake
Husky Creek
Husky Spring
Huss Creek
Hutchinson Slough
Hutson Gulch
Huxley Lake
Hyall Gulch
Hyde Reservoir
IXL Mine
Ice Creek
Ice Lake
Ichabod Spring
Ida Mine
Idaho Creek
Idanha
Ideal Spring
Idlewild Recreation Site
Idol City Mines
Ike Butte
Ike Spring
Ikenick Creek
Ikt Butte
Illahe
Illahee Guard Station
Illahee Rock
Illahee Spring
Illinois River
Illinois River Trail
Illumination Rock
Image Creek
Imagination Peak
Imbler
Imbler Gulch
Immigrant Gulch
Immigrant Spring
Imnaha
Imnaha Creek
Imnaha Divide
Imnaha Recreation Site
Imnaha Grange
Imnaha Guard Station
Imnaha Rapids
Imnaha River
Improved Order of Redmen Cemetery
Inch Creek
Inch Creek
Independence Mine
Independent Mine
Indian Butte
Indian Butte
Indian Camp
Indian Charlie Creek
Indian Creek Flat
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek
Indian Creek Butte
Indian Creek Cemetery
Indian Creek Reservoir
Indian Creek Spring
Indian Creek Trail
Indian Creek Trail
Indian Flat
Indian Ford
Indian Fort Creek
Indian Glade
Indian Grave Creek
Indian Head Rock
Indian Hill
Indian Holes
Indian Lakes
Indian Mountain
Indian Mountain
Indian Point
Indian Prairie
Indian Ridge
Indian Ridge
Indian Ridge
Indian Rock
Indian Rock
Princess Trail
Indian Springs
Indian Spring
Indian Spring
Indian Spring
Indian Spring
Indian Spring Reservoir
Indian Springs
Indian Trail
Indian Trail Canyon
Indian Trail Creek
Indian Trail Spring
Indian Valley
Indiana Creek
Indigo Creek
Indigo Creek
Indigo Lake
Indigo Prairie
Ingle Cemetery
Ingle Creek
Ingle Mountain
Ingle Rock
Ingram Butte
Ingram Creek
Ingram Point
Ingram Spring
Inlet Creek
Inman Mine
Inspiration Point
Intake Trail
Ipsoot Butte
Iris Pond
Irish Gulch
Irish Hill
Irish Lake
Irish Mountain
Irish Spring
Irishmans Campground
Iron Creek
Iron Creek
Iron Creek
Iron Creek
Iron Hand
Iron Knob
Iron Mountain
Iron Mountain
Iron Mountain
Iron Mountain
Iron Spring Creek
Iron Spring Gulch
Irondyke Recreation Site
Irondyke Creek
Ironside C and H Corrals
Ironside Mountain
Ironside School (historical)
Irvin Canyon
Irving Creek
Irving Glacier
Isham Creek
Isherwood Lake
Island Ditch
Island Recreation Site
Island Lake
Island Lake
Island Lake
Island Lake
Island Lake Trail
Island Meadow
Island Meadow Trail
Island Rock
Mount Italy
Ithema Spring
Lake Ivern
Ivory Pine Mill
Ivy Creek
Izee
Izee Spring
J F Spring
J L Spring
J T Spring
JB Reservoir
Jack and Jenny Buttes
Jack of Clubs
Jack Cabin Meadow
Jack Creek
Jack Creek
Jack Creek
Jack Creek
Jack Creek
Jack Creek
Jack Creek
Jack Creek
Jack Creek Corral
Jack Flat
Jack Lake
Jack Lowery Creek
Jack Pine Spring
Jack Point
Jack Shelter
Jack Spring
Jack Spring
Jack Springs
Jackalope Spring
Jackass Butte
Jackass Creek
Jackass Creek
Jackass Creek
Jackass Mountain
Jackass Mountain
Jackass Spring
Jacket Springs
Jakey Ridge
Jackies Thicket
Jackknife Creek
Jackknife Flat
Jackpot Meadow
Jacks Creek
Jacks Lakes
Jacks Spring
Jackson Buttes
Jackson Cemetery
Jackson Creek
Jackson Creek
Jackson Creek
Jackson Creek
Jackson Creek
Jackson Creek
Jackson Creek
Jackson Creek
Jackson Creek
Jackson Creek Guard Station (historical)
Jackson Creek Trail
Jackson F Kimball State Park
Jackson Gap
Jackson Peak
Jackson Spring
Jackson Spring
Jade Camp
Jade Reservoir
Jake Creek
Jake Green Spring
Jalland Creek
James Creek
James Creek Shelter
James Meadow
Jamison Meadow
Jamison Ranch
Janus Butte
Janus Butte Trail
Japanese Creek
Japanese Hollow
Japanese Meadow
Jarboe Creek
Jarboe Meadow
Jaussaud Corral
Jaussaud Creek
Jay Bird Mine
Jay Lake
Jaybird Creek
Jaynes Ridge
Jazz Creek
Jean Lake
Jeeter Prairie
Jeff Creek
Jeff Davis Creek
Jefferson Creek
Jefferson Creek Trail
Jefferson Lake
Jefferson Lake Trail
Jefferson Park Glacier
Jefferson Park Trail
Jefferson Elementary School
Mount Jefferson
Jenkins Creek
Jenny Corral Gulch
Jenny Creek
Jenny Creek
Jenny Creek Spring
Jenny Lake
Coyote Spring
Jerden Cove
Jericho Creek
Jernigan Island
Jerome Prairie
Jerome Prairie Elementary School
Jerry Creek
Jerry Mountain
Jerry Spring
Jerry Spring
Jesse Spring
Jessie Spring
Jewel Creek
Jewett Lake
Jezebel Lake
Jim Creek
Jim Creek
Jim Creek
Jim Creek
Jim Creek
Jim Creek
Jim Creek Butte
Jim Elliott Creek
Jim Hayes Creek
Jim Meadow
Jim Spring
Jim White Ridge
Jimmy Creek
Jimmy McCuen Spring
Jims Creek
Jinks Creek
Joaquin Miller Trail
Job Creek
Jobs Garden
Jody Creek
Joe Creek
Joe Creek
Joe Creek
Joe Day Creek
Joe Hall Creek
Joe Hall Creek
Joe Spring
Joes Peak
Joes Point
Joes Prairie
John B Yeon State Park
John Creek
John Creek
John Day
John Day River
John Henry Lake
John Long Placer Mine
John S Spring
John Smith Island
John Swallow Grave
John Young Meadows
John Z Canyon
Johnnie Creek
Johnny Cake Mountain
Johnny Lake
Johnny Lake
Johns Camp
Johns Mill Trail
Johnson Barn
Johnson Butte
Johnson Butte
Johnson Camp
Johnson Canyon
Johnson Canyon
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnston Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek
Johnson Creek Reservoir
Johnson Ditch Spring
Johnson Gulch
Johnson Gulch
Johnson Gulch
Johnson Gulch Spring
Johnson Meadow
Johnson Meadow
Johnson Meadow Guard Station
Johnson Meadows
Johnson Meadows Trail
Johnson Mountain
Johnson Point
Johnson Prairie
Johnson Ridge
Johnson Ridge
Johnson Spring
Johnson Springs
Johnson Trail
Joice Spring
Jolly Creek
Jonas Creek
Jonas Mountain
Jones Butte
Jones Canal
Jones Canyon
Jones Canyon
Jones Canyon
Jones Creek
Jones Creek
Jones Creek
Jones Creek
Jones Creek
Jones Gulch
Jones Lava
Jones Ranch
Jones Spring
Jones Spring
Jones Troughs
Jones Well
Jones Well Guard Station
Jordan Butte
Jordan Cove
Jordan Creek
Jordan Creek
Jordan Creek
Jordan Cutoff Trail
Jordan Lake
Jordan Point
Jordan Spring
Jordan Spring
Jordan Creek
Jorn Lake
Joseph
Joseph Canyon
Joseph Canyon Viewpoint
Joseph Cemetery
Joseph Creek
Joseph Mountain Mines
Josephine Creek
Josephine Lake
Josephine Mountain
Joyce Creek
Jubilee Lake
Judd Mountain
Jude Creek
Jude Lake
Judy Creek
Judy Spring
Jug Creek
Jug Spring
Jugow Creek
Jumbo Creek
Jump Creek
Jump Creek
Jumpoff Joe Camp
Jumpoff Joe Lake
Jumpoff Joe Trail
Junco Lake
Junction Burn
Junction Creek
Junction Creek
Junction Lake
Junction Lake
Junction Spring
Junction Spring
June Lake
Mount June
Junetta Creek
Jungle Creek
Jungle Creek
Jungle Creek
Jungle Spring
Jungle Spring
Jungle Spring
Juniper Butte
Juniper Butte
Juniper Camp
Juniper Canyon
Juniper Canyon
Juniper Canyon
Juniper Creek
Juniper Creek
Juniper Creek
Juniper Creek
Juniper Flat
Juniper Flat
Juniper Flat Spring
Juniper Lake
Juniper Mountain
Juniper Park
Juniper Ridge
Juniper Ridge
Juniper Spring
Juniper Spring
Juniper Spring
Juniper Trail
Junkens Creek
Juno
Jupiter
Justus Spring
K B Spring
K Creek
K Davis Hill
Ko Butte
Kaenta Spring
Kahler Basin
Kahler Butte
Kahler Creek
Kaleetan Butte
Kaleib Spring
Kamela
Kamkaun Spring
Kanaka Gulch
Kane Springs
Kansas Creek
Kapka Butte
Karnowsky Creek
Katalo Butte
Kate Creek
Kate Spring
Kates Dairy
Katsuk Butte
Katy Mountain
Katydid Ranch
Kautz Creek
Kawak Butte
Keating Creek
Keddy Field
Keeler Creek
Keeler Creek
Keen Canyon
Keene Creek Ridge
Keener Gulch
Keeney Camp (historical)
Keeney Creek
Keeney Creek
Keeney Creek
Keeney Mine
Keeps Mill Recreation Site
Kees Canyon
Keeton Creek
Keith Creek
Kellar Creek
Keller Cabin Spring
Keller Creek
Keller Creek
Keller Spring
Kellers Cabin
Kelley Creek
Kellow Creek
Kelly Butte
Kelly Creek
Kelly Creek
Kelly Creek
Kelly Creek
Kelly Creek
Kelly Gap
Kelly Gulch
Kelly Mountain
Kelly Prairie
Kelly Spring
Kelsay Butte
Kelsay Butte
Kelsay Butte Trail
Kelsay Creek
Kelsay Meadows
Kelsay Mountain
Kelsay Point
Kelsay Spring
Kelsay Valley
Kelsay VAlley Recreation Site
Kelsay Way
Kelsey Butte
Kelsey Creek
Kelsey Creek
Kelsey Peak
Kelsey Reservoir
Kelsey Spring
Kemp Bridge
Kemp Spring
Kendall Spring
Kenny Gulch
Kenny Prairie
Kenny Spring
Keno Gulch
Kent Peak
Kent Spring
Kentuck Creek
Kentuck Inlet
Kentuck Slough
Kentucky Creek
Highland School at Kenwood Elementary School
Kerby
Kerby Creek
Kerby Ditch
Kerby Flat
Kerby Hill
Kerby Mountain
Kerby Peak
Kerman Spring
Kernan Spring
Kerr Notch
Kerr Valley
Kershaw Lake
Kester Mine
Ketchin Butte
Ketchketch Butte
Ketchum Reservoir
Kettle Belly Glade
Kettle Creek
Kettle Creek
Kettle Creek
Buck Creek
Kettle Creek Trail
Kettle Lake
Kettle Rock
Kettleson Meadow
Keyes Creek
Keys Creek
Keys Troughs
Keystone Gulch
Keystone Mine
Keystone Ranch
Khoeery Creek
Kicking Horse Spring
Kid Flat Spring
Kidnap Spring
Kiechle Arm
Kiger Island
Kilchis River
Kilgore Gulch
Kilgore Spring
Killam Creek
Kimberling Cabin (historical)
Kimberly
Kimmell (historical)
Kimport Ridge
King Cole
King Creek
King Creek
King Forest Camp
King Mountain
King Mountain
King Slough
King Spring
King Spring
King Spring
King Spruce Camp
King Spruce Trail
Kingbolt Spring
Kingbolt Spring
Kings Cabin
Kings Gap Spring
Kings Saddle
Kingsley Reservoir County Park
Kingston Creek
Westside Village Magnet School at Kingston Elementary School
Kink Creek
Kinney Creek
Kinney Creek
Kinney Lake
Kinney Mountain
Kinney Ridge
Kinnikinnic Lake
Kinzel Creek
Kinzel Lake
Kirby Creek
Kirk
Kirk Creek
Kirkland Campground
Kirkwood Spring
Kiser Creek
Kiter Creek
Kitson Hot Springs
Kitson Ridge
Kitson Ridge Trail
Kitten Creek
Kitten Rock
Kittredge Ranch
Kitty Creek
Kitty Spring
Kiwa Butte
Kiwa Springs
Lake Kiwa
Kizer Ranch
Klak Butte
Klamath Agency
Klamath Marsh
Klamath Point
Klamath Ridge
Klawhop Butte
Klees Creek
Klickitat Creek
Klickitat Lake
Klickitat Mountain
Klickitat Ridge
Klickitat Shelter
Deep Creek
Klondike Creek
Klondike Creek
Klondike Spring
Klone Butte
Klootchman Creek
Klopp Placer Mine
Klovdahl Bay
Knapke Gulch
Knapper Gulch
Knebal Spring
Kneeland Place
Knight Creek
Knight Creek
Knight Creek
Knight Creek
Knights of Pythias Camp
Knights Pond
Knob Creek
Knob Hill
Knob Peak
Knob Rock
Knob Rock Creek
Knot Tableland
Knowles Creek
Knox Meadow
Knox Mountain
Knutson Saddle
Koch Butte
Koch Mountain
Koch Mountain Trail
Conger Mountain
Kooney Spring
Koosah Mountain
Koski Basin
Kotzman Basin
Krag Lake
Krag Peak
Krause Cabin
Kreuger Rock
Kroll
Kuamaksi Butte
Kuckup Park
Kuhn Canyon
Kuhn Ridge
Kuiman Creek
Kutcher Well
Kweo Butte
Kwinnum Butte
Kwolh Butte
Kyle Creek
Kyle Spring
L and H Spring
L N Spring
La Brie Lake
La Pine
La Pine Station
La Bare Creek
La Sere Creek
La Sere Point
Labellevue Mine
Labrador Creek
Lackey Creek
Lackeys Hole
Lackeys Lake
Ladd Creek
Ladd Creek Campground (historical)
Ladd Glacier
Ladore Creek
Lady Creek
Lady Lake
Ladybug Gulch
Lafollett Creek
Lake of the Woods Mountain
Lake Basin
Lake Basin
Lake Basin Creek
Lake Branch
Lake Butte
Lake Camp Gulch
Lake Camp Spring
Lake Camp Springs
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek
Lake Creek Forest Camp
Lake Creek Forest Camp
Lake Creek Guard Station
Lake Creek Trail
Lake Fork
Lake Fork Creek
Lake Gulch
Lake Mountain
Lake Mountain Trail
Arnold Mountain
Lake Penland
Lake Point
Lake Spring
Lake Valley
Lake Way
Lake Creek
Lakeside
Lakeside Trail
Lakeview
Lakeview Mountain
Lakeview Ranger Station
Lakin Place
Lally Creek
Lamb Creek
Lamb Creek
Lamb Ranch
Lamberson Butte
Lamberson Butte Spur Trail
Lambert Point
Lame Dog Creek
Lamm Camp
Lamms Camp
Lancaster Falls
Lancelot Lake
Lake Land
Landes Creek
Landing Creek
Lane Creek
Lane Creek
Lane Creek
Lane Creek Recreation Site
Lane Mountain
Lane Plateau
Lane Ranch
Lane Well
Langille Crags
Langille Glacier
Jimtown
Lansing Spring
Lantern Spring
Lapover Ranch
Larch Creek
Larch Creek
Larch Creek
Larch Mountain
Larch Summit
Larison Creek
Larison Creek Trail
Larison Rock
Larkspur Creek
Larkspur Spring
Larraneta Reservoir
Larsen Spring
Larson Creek
Larson Creek
Larson Place
Larson Slough
Larson Spring
Larson Way Trail
Lasky Creek
Last Camp
Last Chance Creek
Last Chance Creek
Last Chance Creek
Last Chance Mountain
Last Creek
Last Chance Creek
Last Creek
Last Creek
Lately Prairie
Lateral B
Lateral H
Lather Mountain
Lathrop Creek
Latigo Creek
Latourell Creek
Latourell Falls
Latourell Prairie
Laughlin Hills
Laura Creek
Laurel Cemetery
Laurel Creek
Laurel Hill
Vinzenz Lausmann Memorial State Natural Area
Lava Butte
Lava Camp Lake
Lava Cast Forest Recreation Site
Lava Creek
Lava Flat
Lava Island
Lava Island Recreation Site
Lava Island Falls
Lava Lake
Lava Spring
Lava Spring
Lava Spring
Lava Spring
Lava Springs
Lava Top Butte
Lavadoure Community Hall
Lavadoure Creek
Lava Lake
Laverty Lakes
Lawhead Creek
Lawrence Creek
Lawson Butte
Lawson Creek
Lawson Creek
Lawson Creek
Lawson Mountain
Laycock Creek
Layman Gulch
Layng Creek
Layng Creek Ranger Station
Lazy Bend Recreation Site
Lazy Creek
Le Conte Crater
Leach Camp Trail
Leacy Spring
Leaning Rock
Leapfrog Creek
Ledge Creek
Ledge Lake
Ledge Spring
Lee Creek
Lee Creek
Lee Gulch
Lee Lake
Lee Peak
Lee Prairie
Lee Spring
Leech Lake
Leeds Island
Leehmann Ranch
Lefevre Prairie
Left Branch Powder Creek
Left Fork Lick Gulch
Left Fork Sucker Creek
Left Hand Fork Brush Creek
Little Redwood Creek
Leggins Spring
Legore Lake
Legore Mine
Lehman Springs
Leitel Creek
Lemcke Spring
Lemish Butte
Lemish Lake
Lemiti Butte
Lemiti Campground (historical)
Lemiti Creek
Lemiti Meadow
Lemolo Falls
Lemolo Lake
Lemon Butte
Lemon Cabin
Lemon Creek
Lemon Creek
Lemon Creek
Lems Spring
Lenhart Butte
Leno Hill
Lake Lenore
Lent Butte
Lent Canyon
Lenz
Lenz Ranch
Leone Creek
Leone Lake
Leopold Creek
Lethas Spring
Letitia Creek
Letz Creek
Leuizenger Creek
Levage Creek
Lew Spring
Lewis
Lewis Branch
Lewis Butte
Lewis Creek
Lewis Creek
Lewis Creek
Lewis Creek
Lewis Creek
Lewis Creek
Lewis Glacier
Lewis School (historical)
Lewis Spring
Lewis Spring
Leyva Lakes
Libby Creek
Liberty Grange
Lick Creek
Lick Creek
Lick Creek
Lick Creek
Lick Creek
Lick Creek
Lick Creek
Lick Creek
Lick Creek
Lick Creek Ranger Station
Lick Creek Trail (historical)
Lick Creek Trail
Lick Gulch
Lick Rock
Lick Spring
Leaver Creek
Lieutenant Creek
Light Ridge
Lighthouse Rock
Lightning Creek
Lightning Creek
Lightning Creek
Lightning Creek
Lightning Creek
Lightning Creek Placers
Lightning Gulch
Lightning Gulch
Lightning Spring
Lightning Spring
Lillard Ditch
Lilly Creek
Lilly Pond
Lillyville Forest Camp
Lily Camp
Lily Lake
Lily Lake
Lily Lake
Lilly Lake
Lily Pad Lake
Lily Pond
Lily White Guard Station
Limber Creek
Limburger Cabin
Lime Creek
Lime Creek
Lime Gulch
Lime Gulch
Lime Rock
Limestone Creek
Limestone Creek
Limestone Trail
Limpy Creek
Limpy Creek
Limpy Mountain
Limpy Rock
Lincoln Canyon
Lincoln Grange
Lincoln Elementary School
Lincton Mountain
Lindick Lake
Lindros Arm
Lindsey Creek State Park (historical)
Lindsey Pond
Lindsley Creek
Line Butte
Line Creek
Line Creek
Line Creek
Line Creek
Line Creek
Linger Longer Prairie
Link Bar Spring
Link Creek
Link Spring
Linn Glacier
Linney Butte
Linney Creek
Linslaw
Lint Creek
Lint Slough
Linton Creek
Linton Spring
Lionshead
Lionshead Creek
Liston Lake Mine
Litch Ranch
Lillian Falls
Lithgow Spring
Lithia Park
Lithia Spring
Little Agency Plains
Little Antelope Flat
Little Applegate Butte
Little Applegate River
Little Aspen Butte
Little Badger Recreation Site
Little Badger Creek
Little Badger Creek Trail
Little Bald Mountain
Little Bald Mountain Prairie
Little Baldy
Little Baldy
Little Baldy Creek
Little Baldy Mountain
Little Baldy Trail (historical)
Little Basin Creek
Little Battle Mountain
Little Bear Camp
Little Bear Creek
Little Bear Creek
Little Bear Creek
Little Bear Creek
Little Bear Creek
Little Bear Creek
Little Bear Creek Meadow
Little Bear Spring
Little Bear Spring
Little Beaver Creek
Beaver Creek
Little Beech Creek
Little Belknap
Little Bend Creek
Little Black Butte
Little Black Rock
Little Black Rock
Little Black Stump Gulch
Little Blanket Shelter
Little Blue Mine
Little Boulder Creek
Little Boulder Creek
Little Boulder Lake
Little Boulder Way Trail
Little Briches Spring
Little Bristo Creek
Little Brother
Little Buck Creek
Little Buck Creek
Little Bunchgrass Lookout
Little Butte
Little Butte Creek
Little Butte Creek
Little Butte Creek
Little Cache Mountain
Little Canyon
Little Canyon Mountain
Little Castle Creek
Little Cedar Creek
Little Cedar Creek
Little Chetco River
Little Chinquapin Mountain
Little Clear Creek
Little Clear Creek
Little Courtney Canyon
Little Cow Creek
Little Craggy Creek
Little Craggy Peak
Little Crane Recreation Site
Little Crane Creek
Little Crater Meadow
Little Creek
Little Creek
Little Creek
Little Creek
Little Creek
Little Cultus Lake
Little Cummins Creek
Little Dark Canyon
Little Dark Canyon Trail
Little Deception Rock
Little Deep Creek
Little Deschutes Campground (historical)
Little Deschutes River
Little Devils Canyon
Little Digger Mountain
Little Dog Creek
Little Dog Spring
Little Dome Rock
Little Dry Creek
Little Dutch Canyon
Little Eagle Creek
Little Eagle Creek
Little Elder Creek
Little Elk Creek
Little Elk Prairie
Little Emigrant Creek
Little Emigrant Spring
Little Emily Creek
Little Euchre Mountain
Little Fall Creek
Little Falls
Little Finger Lake
Little Fish Lake
Little Fly Creek
Little Frazier Lake
Little Gold Creek
Little Goodman Ridge
Little Granite Creek
Little Grayback Creek
Little Grayback Mountain
Little Grayback Peak
Little Groundhog Mountain
Little Gulch
Little Hebo
Little Horse Heaven Creek
Little Horse Spring
Little Horseshoe Spring
Little Howard Spring
Little Humpy Peak
Little Hurricane Creek
Little Indian Creek
Little Indian Creek
Little Jim Mine
Little John Day Creek
Little Johnson Creek
Little Kelsay Creek
Little Kettle Creek
Little Lake
Little Lake
Little Lake Creek
Little Lake Trail
Little Lakes
Little Lava Lake
Little Lick Creek
Little Lobster Creek
Little Logan Creek
Little Lookingglass Creek
Little Lost Creek
Little Malheur River
Little McKay Creek
Little Meadow Canyon
Little Meadows Creek
Little Meadows
Little Meadows
Little Mill Creek
Little Minam River
Little Mowich Mountain
Little Mud Lake
Little Muddy Creek
Little Muddy Creek
Little North Santiam River
Little Oak Flat
Little Odell Butte
Little Odell Creek
Little Odell Spring
Little Parsnip Creek
Little Pearson Creek
Little Phillips Creek
Little Pickett Creek
Dry Pine Creek
Little Pine Creek
Little Pine Openings
Little Pot Creek
Little Potamus Creek
Little Potamus Well
Little Red Mountain
Little Red Mountain Creek
Little Riner Basin
Little River
Little River
Little Rock Creek
Little Rock Creek
Little Rock Creek
Little Rock Flat
Little Round Butte
Little Round Meadow
Little Round Prairie
Little Round Prairie Spring
Little Roundtop Mountain
Little Rowell Creek
Little Sage Hen Creek
Little Sage Hen Flat
Little Salmon River
Little Sandy Guard Station
Little Sandy River
Little Sandy Trail
Little Scotty Creek
Little Sheep Creek
Little Sheep Ridge
Little Silver Creek
Little Silver Creek
Little Sixmile Creek
Little Slide Lake
Little Snowshoe Creek
Little South Fork Hunter Creek
Little Spring
Little Spring
Little Akawa Butte
Little Škáypiya Creek
Little Isqúulktpe Creek
Frosty Meadow
Myrtle Spring
Little Isqúulktpe Spring
Little Storm Lake
Little Strawberry Lake
Little Sugarloaf Peak
Little Summit Campground
Little Summit Creek
Little Summit Prairie
Little Sunshine Creek
Little Table Mountain
Little Taft Creek
Little Tamarack Mountain
Little Three Creek Lake
Little Todd Creek
Little Walker Mountain
Little Wall Creek
Little Washout Creek
Little Weasel Spring
Little Willow Creek
Little Willow Creek
Little Wilson Creek
Little Windy Creek
Little Windy Creek
Little Wocus Bay
Little Wocus Butte
Little Wolf Creek
Little Yamsay Mountain
Little Zigzag Canyon
Little Zigzag Creek
Littlemile Creek
Liveoak Creek
Lake Liza
Lizard Lake
Lizard Lake
Lizard Point
Lizard Ridge
Lizard Spring
Llao Bay
Llao Rock
Lloyd Spring
Loa Mae Mine
Loafer Creek
Lobelia Meadow
Lobert Draw
Lobster Creek
Lobster Creek
Lobster Hill
Location Butte
Lockhart Creek
Lockhart Creek
Lockit Butte
Loco Canyon
Loco Spring
Lodgepole Creek
Lodgepole Creek
Lodgepole Guard Station
Lodgepole Lake
Lofton Creek
Log Cabin Spring
Log Creek
Log Creek
Log Creek
Log Creek
Log Creek
Log Pile Trail
Log Spring
Log Spring
Log Spring
Log Spring
Log Table Camp
Logan Creek
Logan Cut
Logan Valley
Logdell
Loggan Springs
Logger Butte
Logging Camp Spring
Lois Lake
Lolah Butte
Loletta Lakes
Lolo Butte
Lolo Pass
Lone Creek
Lone Fir Cemetery
Lone Mountain
Lone Pine
Lone Pine Basin
Lone Pine Butte
Lone Pine Creek
Lone Pine Ditch
Lone Pine Flat
Lone Pine Saddle
Lone Pine School (historical)
Lone Pine Spring
Lone Pine Spring
Lone Ranch Creek
Lone Rock
Lone Rock Creek
Lone Spring
Lone Spring Mountain
Lone Star
Lone Tree Creek
Lone Tree Creek
Lone Tree Ridge
Lone Wolf
Lonepine Creek
Lonerock
Lonerock Cemetery
Longs Creek
Lonesome Creek
Lonesome Creek
Lonesome Creek
Lonesome Meadow
Lonesome Spring
Lonewoman Creek
Long Branch
Long Branch
Long Branch
Long Branch Creek
Long Butte
Long Cabin
Long Canyon
Long Canyon
Long Creek
Long Creek
Long Creek
Long Creek
Long Creek
Long Creek
Long Creek
Long Creek
Long Creek
Long Creek Mountain
Long Creek Reservoir
Long Glade
Long Gulch
Long Gulch
Long Gulch
Long Gulch
Long Gulch Springs
Long Hollow
Long Hollow
Long Hollow
Long Hollow
Long Hollow
Long Hollow
Long Hollow
Long Hollow Creek
Long Hollow Creek
Long John Creek
Long Lake
Long Lake
Long Lake
Long Lake
Long Lake
Long Lake
Long Lake Camp
Long Meadow
Long Meadow Creek
Long Meadows
Long Mountain
Long Pond
Long Prairie
Long Prairie
Long Prairie
Long Prairie
Long Prairie
Long Prairie
Long Prairie
Long Prairie
Long Prairie
Long Prairie Forest Camp
Long Prairie Reservoir
Long Prairie Spring
Long Prong
Long Ridge
Long Ridge
Long Ridge
Long Ridge
Long Ridge
Long Ridge
Long Ridge Spring
Long Spring
Long Tom Creek
Long Valley
Long Wiley Creek
Looking-Glass Prairie
Lookingglass Creek
Lookingglass Falls
Lookingglass Lake
Lookout
Lookout Butte
Lookout Creek
Lookout Creek
Lookout Creek
Lookout Creek
Lookout Gap
Lookout Gulch
Lookout Lake
Lookout Mountain
Lookout Mountain
Lookout Mountain
Lookout Mountain
Lookout Mountain
Lookout Mountain
Lookout Mountain
Lookout Mountain
Lookout Mountain Trail
Lookout Pasture
Lookout Point
Lookout Point
Lookout Point Lake
Lookout Rock
Lookout Spring
Lookout Spring
Lookout Spring
Lookout Springs Guard Station (historical)
Loon Creek
Loon Lake
Looney Creek
Looney Reservoir
Looney Spring Campground
Loowit Falls
Lord Flat
Lorin Lake
Lost Basin Creek
Lost Boulder Ditch
Lost Boy Butte
Lost Boy Gulch
Lost Buck Mine
Lost Bucket Creek
Lost Cabin
Lost Cabin Creek
Lost Camp
Lost Camp Prairie
Lost Camp Spring
Lost Camp Trail
Lost Camp Trail
Lost Canyon
Lost Cow Spring
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek
Lost Creek Camp
Riley Horse Camp
Lost Creek Glacier
Lost Creek State Recreation Site
Lost Creek Spring
Lost Dog Gulch
Lost Dog Reservoir
Lost Flat
Lost Fork
Lost Guard Creek
Lost Guard Spring
Lost Gulch
Lost Horse Creek
Lost Horse Meadow
Lost Indian Reservoir
Lost Indian Trail
Lost Lake
Lost Lake
Lost Lake
Lost Lake
Lost Lake Butte
Lost Lake Butte Trail
Lost Lake Creek
Lost Lake Spring
Lost Lake Trail
Lost Meadow
Lost Peak
Lost Peak Trail
Lost Prairie
Lost Prairie
Lost Prairie
Lost Prairie Cemetery
Lost Spring
Lost Spring
Lost Spring
Lost Spring
Lost Spring
Lost Spring
Lost Spring
Lost Valley
Lost Valley Creek
Lost Valley Creek
Lostine Cemetery
Lostine Guard Station
Lostine River
Loughs Mine
Louie Creek
Louis Creek
Louise Creek Trail
Louse Creek
Louse Lake
Louse Rock
Louse Spring
Lava Pass
Love Creek
Love Station
Lovlett Corral
Lovlett Creek
Low Divide
Low Echo Camp
Low Gap
Low Gap
Low Gap Creek
Low Pass Spring
Low Ridge
Low Ridge
Low Ridge Creek
Lowe Creek
Lowe Mill
Mount Lowe
Lowell Creek
Lowell Mountain
Lowell Spring
Lower Bench
Lower Bennett Spring
Lower Berley Lake
Lower Bluff Springs
Lower Bridge Recreation Site
Lower Bridge School (historical)
Lower Buttes Reservoir
Lower Cache Creek Rapids
Lower Chewaucan Marsh
Lower Cougar Camp
Lower Cyrus Spring
Lower Davis Flat
Lower Desert
Lower Dugout Creek Reservoir
Lower East Lateral
Lower Eddeeleo Lake
Lower Eightmile Crossing Recreation Site
Lower End Camp (historical)
Lower Erma Bell Lake
Lower First Creek Spring
Lower Gorge
Lower Howard Camp
Lower Island Lake
Lower Jones Canyon Reservoir
Lower Kirby Rapids
Lower Lake
Lower Land Creek
Lower Marilyn Lake
Lower Mosquito Creek Spring
Lower Mud Spring
Lower Pine Ridge Spring
Lower Quinn Lake
Lower Reservoir (historical)
Lower Rigdon Lake
Lower River Trail
Lower Rosary Lake
Lower Salmon Lake
Lower Sheepy Reservoir
Lower Soda Falls
Lower Swiss Spring
Lower Valley
Lower Valley Ditch
Lowry Gulch
Lowullo Butte
Loyd Creek
Lucas Gulch
Lucas Ranch
Luce Creek
Luce Place (historical)
Lucifer
Lake Lucile
Luck Creek
Lucky Butte
Lucky Butte
Lucky Butte
Lucky Camp Trail
Lucky Canyon
Lucky Creek
Lucky Creek
Lucky Lake
Lucky Lake Trail
Lucky Lass Mine
Lucky Reservoir
Lucky Reservoir
Lucky Spring
Lucky Strike Mine
Lucky Strike Mine
Luder Creek
Ludwick Cabin
Luelling Spring
Luethye Mine
Luger Spring
Lukens Creek
Lumrum Butte
Luna Butte
Lunch Creek
Lunch Creek
Lunch Spring
Lund Creek
Lund Park Recreation Site
Lundy Spring
Lupine Creek
Lusby Cabin
Luther Butte
Luther Divide
Luther Mountain
Lutsey Point
Lyle Reservoir
Lyman Creek
Lyman Meadow
Lyman Meadow Spring
Lynch Creek
Lyndon Creek
Lynholm Gulch
Lynx Creek
Lyons Canyon
Lytle Creek
Lytle Creek
Lytle Prairie
M and M Creek
Mabel L Mine
Mac Creek
Mac Lake
Mace Mountain
Macey Cove
Mack Arch
Mack Arch Cove
Mack Hall Creek
Mack Landing
Mack Point
Mack Reef
Mackatie Spring
Mackey Butte
Mackey Creek
Macklyn Cove
Mad Creek
Madams Creek
Madden Butte
Madison Butte
Madison Butte Trail
Madison Creek
Madison Gulch
Madras
Buff Elementary School
Madras Station
Madstone Cabin
Madstone Creek
Mafler Creek
Maggie Spring
Maggot Spring
Magill Creek
Magnolia Mine
Magone Lake
Magpie Butte
Magpie Creek
Magpie Creek
Magpie Creek
Magpie Peak
Magpie Spring
Mahogany Butte
Mahogany Butte
Mahogany Butte
Mahogany Creek
Mahogany Flat
Mahogany Mountain
Mahogany Mountain
Mahogany Reservoir
Mahogany Spring
Mahogany Spring
Mahogany Spring
Maid of the Mist Mine
Maiden Lake
Maiden Peak
Maiden Peak Trail
Maiden Spring
Maidu Lake
Maidu Lake Way
Main Creek Trail
Main Spring
Maitland Spring
Major Creek
Major Prairie
Makin Creek
Maklaks Creek
Maklaks Mountain
Maklaks Pass
Maley Creek
Malheur River
Malheur Spring
Lake Malice
Mallard Arm
Mallard Creek
Mallard Marsh Recreation Site
Mallory Creek
Mallory Spring
Malone Spring
Maltby Creek
Mammoth Lode Mine
Mammoth Spring
Mammoth Spring
Mangriff Lake
Mann Ridge
Mansfield Creek
Mansfield Mountain
Mansfield Trail
Manzanita Creek
Mapes Creek
Maple Creek
Maple Creek
Maple Creek
Maple Creek
Maple Creek
Maple Dell Gap
Maple Spring
Maples Forest Camp (historical)
Mapleton
Marble Mountain
Marble Point
Marble Reservoir
Marco Creek
Mares Egg Spring
Margurette Lake
Maria Creek
Marial
Lake Marie
Lake Marie
Mariel Creek
Marine Creek
Marion Creek
Marion Creek
Marion Lake
Marion Lake Guard Station
Marion Lake Trail
Marion Point
Marks Cabin
Marks Creek
Marks Creek
Marks-Thompson Mine
Marksbury Spring
Marmot
Marmot Butte
Marmot Pass
Marr Creek
Marr Flat
Lake Marr
Marsh Creek
Marshall Creek
Marshall Place (historical)
Marshall High School
Marshall Spring
Marshfield Channel
Marsters Spring
Marten Creek
Marten Lake
Marten Spring
Martie Creek
Martie Creek Guard Station
Martin Bridge Trail
Martin Creek
Martin Creek
Martin Creek
Martin Creek
Martin Creek
Martin Creek Trail
Martin Lake
Martin Lake
Martin Lake
Martin Prairie
Martin Prairie Spring
Martin Spring
Martin Way
Martins Mill
Marval (historical)
Mary Oard Homestead
Lake Mary
Maryanne Spring
Marys Creek
Marys Peak
Marys River
Marysville Placer
Mascall Corralls
Masekesket Cemetery
Mason Spring
Masten Butte
Masterson Spring
Mate Cabin
Matlock Creek
Matlock Flat
Matlock Hill
Matlock Prairie
Matlock Waterhole
Matson County Park
Matterhorn
Matthews Guard Station
Matts Well
Maude Creek
Maude Mountain
Maude- S Mine
Maury Creek
Maury Guard Station (historical)
Maury Mountain Mines
Maury Mountains
Maverick Creek
Max Spring
Maxville
Maxwell Creek
Maxwell Lake
Maxwell Point
Maxwell Reservoir
Maxwell Spring
May Creek
May Queen Mine
Mayfield Creek
Mayflower Mine
Mayflower Trail
Mazama Creek
Mazama Creek Campground (historical)
McAllister Creek
McAllister Spring
McAllister Spring
McAlister Spring
McArthur Spring
McArthur Spring
McAttee Spring
McBee Creek
McBee Lake
McBee Trail
McBride Creek
McBride Guard Station
McBroom Ranch
McBroom Spring
McCaffery Slough
McCaleb Ranch
McCall Creek
McCall Creek
McCall Dipping Vat Spring
McCall Spring
McCallister Soda Spring Forest Camp (historical)
McCarty Butte
McCarthy Spring
McCartie Ranch
McCarty Butte
McCarty Creek
McCarty Creek
McCarty Field
McCarty Flat
McCarty Gulch
McCarty Meadow
McCarty Reservoir
McCarty Spring
McClellan Creek
McClellan Creek
McClellan Meadow
McClellan Mountain
McClellan Spring
McCoin Creek
McComas Creek
McComb Butte
McCool Butte
McCord Cabin Spring
McCord Creek
McCormick Gulch
McCoy Creek
McCoy Creek
McCoy Creek
McCoy Creek
McCoy Flats
McCoys Cove
McCready Ranch
McCredie Creek
McCredie Springs
McCubbin Basin
McCubbin Creek
McCubbin Creek
McCubbins Gulch
McCue Spring
McCully Basin
McCully Creek
McCully Fork
McCurdy Campground
McCurdy Creek
McDaniel Creek
McDonald Creek
McDonald Creek
McDonald Ditch
McDonald Meadow
McDonald Peak
McDonald Ridge
McDonald School (historical)
McDonald State Forest
McDougall Camp
McDowell Creek
McEwen Spring
McEwen Valley Ditch
McFarland Lake
McFarland Point
McGarr Meadows
McGee Creek
McGinnis Creek
McGlynn Creek
McGowan Mountain
McGowan Mountain Way
McGribble Guard Station
McGuire Gulch
McIntire Basin
McKay Butte
McKay Creek
McKay Creek
McKay Creek
McKay Saddle
McKee Basin
McKee Bridge Recreation Site
McKee Cabin
McKee Lake
McKenzie Canyon
McKenzie Canyon Reservoir
McKenzie Pass
McKenzie Spring
McKie Camp
McKinley Creek
McKinley Creek
McKinley Creek Trail
McKinley Ranch
McKinley Rock
McKinney Butte
McKinney Creek
McKinney Creek
McKinney Creek
McKinney Creek
McKinney Slough
McKnight Creek
McKnabe Creek
McLain Gulch
McLean Mountain
McLeod
McLeod Creek
McLeod Wayside
Mount McLoughlin
McMeen Creek
McMeen Spring
McMullen Spring
McMullen Spring
McMullen Spring
McMullin Creek
McMurdo Cabin
McNamee Gulch
McNaughton Spring
McNeese Flat
McNeil Creek
McNulty Basin
McNutt Flat
McQuade Creek
McVey Creek
McVey Spring
McWillis Gulch
Meacham
Meacham Creek
Meacham Lake
Meadow Branch
Meadow Brook Summit
Meadow Recreation Site
Meadow Cow Camp
Meadow Creek
Meadow Creek
Meadow Creek
Meadow Creek
Meadow Creek
Meadow Creek
Meadow Creek
Meadow Creek
Meadow Creek
Meadow Creek
Meadow Creek
Meadow Creek Driveway Trail
Meadow Creek Trail
Meadow Fork
Meadow Fork Big Creek
Meadow Lake
Meadow Lake
Meadow Mountain
Meadow Reservoir
Meadow Spring
Meadow Spring
Meadow Waterhole
Meadows Creek
Meads Flat
Meda
Medford Aqueduct
Medford Irrigation District Canal
Medicine Creek
Medicine Creek
Medicine Creek
Medicine Mountain
Medicine Rock
Mee Cove
Meek Lake
Meengs Spring
Mehlhorn Butte
Mehlhorn Mill
Melco Landing
Melis Lake
Mellow Moon Spring
Melvin Butte
Melvin Creek
Melvin Spring
Memaloose Creek
Memaloose Guard Station
Memaloose Lake
Memaloose Lake
Memaloose Point
Memaloose Trail
Memorial Home Cemetery
Mendenhall Creek
Menefee
Mercer Creek
Mercer Lake
Merit Meadows
Merle Burn
Merle Gulch
Merle Lake
Merlie Butte
Merlie Table
Merrill Lake
Merrill Spring
Merritt Creek
Merritt Spring
Meryl Creek
Meryl Springs
Mesa Creek
Mesman Creek
Metal Creek
Metlako Falls
Metolius
Metolius Bench
Metolius River
Metolius Spring
Metsker Spring
Mettman Creek
Metzler Creek
Myer Creek
Meyers Canyon
Meyers Hill
Michigan Mine
Mid Slough
Middle Bear Camp
Middle Butte
Middle Channel Willamette River
Middle Creek
Middle Creek
Middle Erma Bell Lake
Middle Fork Crooked Creek
Middle Fork Annie Creek
Middle Fork Big Sheep Creek
Middle Fork Burnt River
Middle Fork Canyon Creek
Middle Fork Coquille River
Middle Fork Dahl Creek
Middle Fork Deadman Creek
Middle Fork Deep Creek
Middle Fork Dry Creek
Middle Fork Fivemile Creek
Middle Fork Hood River
Middle Fork Imhaha River
Middle Fork John Day River
Middle Fork Junetta Creek
Middle Fork Lake Creek
Middle Fork Mosby Creek
Middle Fork Mount Emily Creek
Middle Fork National Creek
Middle Fork North Fork Smith River
Middle Fork Parsnip Creek
Middle Fork Pass Creek
Middle Fork Rock Creek
Middle Fork Rock Creek
Middle Fork Rogue River
Middle Fork Sixes River
Middle Fork Street Creek
Middle Fork Sunshine Creek
Middle Fork Trout Creek
Middle Fork Tumalo Creek
Black Snag Creek
Middle Fork Whisky Creek
Middle Fork Wilkins Creek
Middle Fork Willamette River
Middle Fork Wolf Creek
Middle Hanks Lake
Middle Kirby Rapids
Middle Lake
Middle Lake
Middle Long Hollow
Middle Mountain
Middle Point
Middle Point Divide
Middle Ridge
Middle Ridge
Middle Ridge
Middle Rosary Lake
Middle Santiam River
Middle Sister
Middle Sister Creek
Middle Trail Creek
Middle Valley
Middle Willow Creek
Midget Lake
Midnight Lake
Midnight Spring
Midway
Midway Pond
Midway Spring
Mike Acton Spring
Mike Bauer Recreation Site
Mike Creek
Mikes Gulch
Mill Creek
Milbury Mountain
Mildred Lake
Mile Camp Recreation Site
Mile Lake
Miller Spring
Miles Creek
Miles Creek
Miles Mountain
Miles Reservoir
Milk Creek
Milk Creek
Milk Creek
Milk Creek
Milk Creek
Milk Shakes
Milk Spring
Milk Spring
Milk Spring
Mill Canyon Spring
Mill Creek
Macklyn Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek
Mill Creek Buttes
Mill Creek Divide
Mill Creek Ridge
Mill Creek Ridge
Mill Creek School (historical)
Mill Creek Trail
Mill Flat
Mill Gulch
Mill Pond
Mill Ridge
Mill Spring
Mill-Mar Ranch
Miller and Jackson Spring
Miller Arm
Miller Butte
Miller Creek
Miller Creek
Miller Creek
Miller Creek
Miller Creek
Miller Creek
Miller Creek
Miller Flat
Miller Flat Creek
Miller Flat Spring
Miller Gulch
Miller Gulch
Miller Lake
Miller Lake
Miller Lake
Miller Lake Creek
Miller Meadow
Miller Mine
Miller Mountain
Miller Mountain
Miller Mountain
Miller Mountain Mine
Miller Prairie
Miller Reservoir
Miller Spring
Miller Spring
Millhayes Meadow
Millican Crater
Millican Crater Trail
Millican Valley
Millrace
Mills Creek
Mills Creek
Mill Reservoir
Milner Crest Elementary School (historical)
Milo
Milo Gard Cemetery
Mina Creek
Minam
Minam Lake
Minam Peak
Minam River
Mine Creek
Mine Ridge
Mine Ridge Spring
Mine Spring
Miner Basin
Miner Basin Creek
Miner Creek
Miner Gulch
Mineral Canyon
Mineral Creek
Mineral Creek
Mineral Hill
Mineral Hill Fork
Mineral Wonder Mine
Miners Basin
Miners Butte
Miners Cabin
Miners Cabin Spring
Miners Creek
Minerva
Minetop Trail
Mingus Park
Minikahda Creek
Mining Iron Creek
Mink Creek
Mink Creek
Mink Lake
Mink Lake Basin
Mink Lake Loop Trail
Mink Lake Shelter
Minnehaha Creek
Minnehaha Creek
Minnehaha-Hurryon Trail
Minnie Creek
Minnie Scott Spring
Minniece Point
Minniece Point Trail
Minnow
Minnow Creek
Minnow Creek
Minotti Creek
Minski Place
Minto Creek
Minto Pass
Minto Pass Trail
Minute Creek
Mirror Lake
Mirror Lake
Mirror Lake Trail
Mirror Lake Trail
Mirror Pond
Mirror Pond
Misery Creek
Misery Creek
Misfit Creek
Misfit Spring
Mislatnah Creek
Mislatnah Lookout (historical)
Mississippi Head
Missouri Bar
Missouri Bend School
Missouri Creek
Missouri Hollow
Mist Creek
Mist Falls
Mistletoe (historical)
Mitchell
Muncey Creek
Mitchell Creek
Mitchell Creek
Mitchell Ridge
Mitchell Spring
Mitchell Spring
Moccasin Lake
Moccasin Prairie
Moco Spring
Modoc Creek
Modoc Creek
Modoc Point
Modoc Point Main Canal
Moffett Creek
Moffit Table
Moffitt Spring
Mokst Butte
Molalla River
Monkey Creek
Monkey Run Creek
Monner Spring
Monogram Lakes
Monon Lake
Monroe Spring
Monte Rico Ridge
Monteith Rock
Monterica Creek
Montgomery Ranch
Monty Recreation Site
Monument
Monument Mountain
Monument Peak
Monument Reservoir
Monument Ridge
Monument Rock
Monument Rock
Monument Spring
Moody Lake
Moolack Butte
Moolack Creek
Moolack Lake
Moolack Mountain
Moon Canyon
Moon Creek
Moon Creek
Moon Creek
Moon Creek Cemetery
Moon Lake
Moon Lake
Moon Lake Trail
Moon Meadow
Moon Mountain
Moon Mountain
Moon Point
Moon Prairie Guard Station
Mooney Mountain
Moonshine Alley
Moonshine Canyon
Moonshine Creek
Moonshine Ditch
Moonshine Spring
Moore Creek
Moore Creek
Moore Creek
Moore Creek Trail
Moores Crossing
Moose Creek
Moose Lake
Moose Mountain
Moose Ridge
Moraine Lake
Moraine Lake Trail
Morden Spring
Moreland Canyon
Morfitt Reservoir
Morg Spring
Morgan Butte
Morgan Butte
Morgan Butte Spring
Morgan Creek
Morgan Creek
Morgan Landing
Morgan Mountain
Morgan Reservoir
Morgan Ridge
Morgan Spring
Morgans Buckhorn
Morin Spring
Morine Creek
Morley Canyon
Mormon Flat
Mormon Prong
Morning Glory Mine
Morning Mine
Morphine Canyon
Morphine Ranch
Morphine Ridge
Morphine Spring
Morris Creek
Morris Creek
Morris Mine
Morris Rodgers Creek
Morris Spring
Morrison Creek
Morrison Gulch
Morrow Well
Morsay Creek
Morse Creek
Mortimer Canyon
Morton Butte
Mosby Creek
Moser Creek
Moses Creek
Mosier Camp
Mosier Creek
Mosier Spring
Mosquito Camp
Mosquito Creek
Mosquito Creek
Mosquito Creek
Mosquito Creek
Mosquito Creek
Mosquito Fish Lake Trail
Mosquito Flat
Mosquito Flat
Mosquito Flat
Mosquito Gulch
Mosquito Lake
Mosquito Lake
Mosquito Spring
Moss Creek
Moss Creek
Moss Creek
Moss Creek
Moss Creek Trail
Moss Mountain
Moss Pass Butte
Moss Ranch
Moss Spring
Moss Springs
Mossback Creek
Mossy Creek
Mossy Gulch
Mote Spring
Mottet Creek
Mottet Spring
Mother Lode Creek
Mother Lode Trail
Mothers Creek
Mott Trail
Moude Mountain Trail
Mount Ashland Trail
Mount Bailey Trail
Mount Emily Creek
Mount McLoughlin Trail
Mount Mitchell
Mount Pitt School
Mount Pleasant Cemetery
Mount Ray Trail
Mount Scott Trail
Mount Union Cemetery
Mount Vernon
Mount Vernon Hot Springs
Mount Wilson Trail
Mount Emily
Mountain Air Park
Mountain Chief Mine
Mountain Creek
Mountain Creek
Mountain Home
Mountain Lakes Trail
Mountain Meadows
Mountain Meadows Trail
Mountain Ranch
Mountain Sheep Creek
Mountain Sheep Rapids
Mountain Spring
Mountain Well
Mountain Wells Trail
Mouse Creek
Mouse Creek
Mouse Spring
Mousehawk Butte
Mowich
Mowich Creek
Mowich Park
Mowich Spring
Mowich Spring Butte
Mowrey Landing
Muckney Lake
Mud Creek
Mud Creek
Mud Creek
Mud Creek
Mud Creek
Mud Creek
Mud Flat Reservoir
Mud Hole Spring
Mud Lake
Mud Lake
Mud Lake
Mud Lake
Mud Lake
Mud Lake
Mud Lake
Mud Lake
Mud Lake Cutoff Trail
Mud Lake Mountain
Mud Lake
Mud Lake Spring
Mud Lake Trail
Mud Lake Trail
Mud Reservoir
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Springs
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Springs
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring
Mud Spring Butte
Mud Spring Creek
Mud Spring Pond
Mud Springs Creek
Mud Springs Creek
Muddy Creek
Muddy Creek
Muddy Creek
Muddy Fork
Muddy Gulch
Muddy Reservoir
Muddy Spring
Muddy Spring
Mudjekeewis Mountain
Mudjekeewis Trail
Muir Creek
Muldoon Mountain
Mule Creek
Mule Creek
Mule Creek
Mule Creek
Mule Creek
Mule Creek
Mule Creek
Mule Deer Ridge
Mule Deer Spring
Mule Gulch
Mule Gulch
Mule Gulch
Mule Hill
Mule Hill
Mule Mountain
Mule Mountain
Mule Mountain
Mule Mountain Lookout (historical)
Mule Peak
Mule Peak
Mule Prairie
Mule Tail Creek
Mule Tail Ridge
Muletail Creek
Muley Creek
Scheele Creek
Mulkey Spring (historical)
Mullen Spring
Muller Basin Spring
Mulligan Creek
Mulligan Gulch
Mulligan Stew Canyon
Mullinix Creek
Multiple Springs
Multnomah Creek
Multnomah Falls Recreation Site
Multorpor Mountain
Munger Creek
Mungers Butte
Munra Point
Munsel Creek
Munsel Lake
Munson Creek
Munson Point
Munson Valley
Munson Valley Trail
Murderers Creek
Murderers Creek Forest Service Station
Murdock Creek
Murdock Creek
Murphy
Murphy Creek
Murphy Creek
Murphy Creek
Murphy Creek
Murphy Creek
Murphy Gulch
Murphy Mountain
Murphy Mountain
Murray Creek
Murray Hill
Murray Hill Spring
Murry Mine
Murray Pasture
Murray Peak
Murray Reservoir
Murray Saddle
Music Creek
Llaos Hallway
Musick Guard Station
Musick Mine
Muskrat Lake
Mussel Creek
Musty Creek
Musty Creek
Mutton Camp
Mutton Camp
Mutton Creek
Muttonchop Butte
Myers Butte
Myers Canyon
Myers Creek
Myers Creek
Myers Meadow
Myers Meadow Spring
Myrtle Butte
Myrtle Creek
Myrtle Creek
Myrtle Creek
Myrtle Creek
Myrtle Grove Recreation Site
Myrtle Park Meadows
Myrtle Spring
Myrtle Spring
Myrtlewood Campground
Mystic Lake
Northwest Rock
Nail Keg Creek
Nancy Creek
Nancy Creek
Nancy Creek
Nanitch Campground (historical)
Nannie Creek
Nannie Creek Trail
Nanny Creek
Nans Rock
Nash Lake
Nash Lake Trail
Nash Reservoir
Nasty Rock
National Creek
Natural Bridge Recreation Site
Nature Creek
Navaho Lake
Navy Spring
Neal Butte
Neal Camp Burn
Neal Creek
Neal Creek Lateral
Nebo Lookout
Mount Nebo
Neds Gulch
Needham Butte
Needham Creek
Needle Creek
Needle Creek
Needle Fork
Needle Point
Needle Rock
Needle Rock
Needle Rock
Needle Rocks
Neely Mountain
Neeves Creek
Negro Creek
Negro Creek
Nehi Creek
Neiglick Creek
Neil Canyon
Neil Creek
Nekbobets Lake
Nekoma (historical)
Nell Creek
Nelson Creek
Nelson Creek
Nelson Creek
Nelson Creek
Nelson Creek
Nelson Guard Station
Nelson Monument
Nelson Reservoir
Nelson Spring
Nelson Well
Nena Creek
Nena Spring
Neotsu
Nep-Te-Pa Lake
Nesbit Butte
Nesika Beach
Neskowin
Neskowin Creek
George R Vogel Group Camp
Neskowin Crest
Neskowin Natural Area
Neskowin Ridge
Nesmith Point
Nesmith Point Trail
Nestucca High School
Netarts
Netarts Bay
Nettie Creek
Nettle Creek
Neuman Gap
Nevada Gulch
Nevergo Creek
New Bridge
New Deal Spring
New England Flat
New Idanha
New Pine Creek Cemetery
New York Mine
Newberry Crater
Newbill Creek
Newby Creek
Newell Creek
Newell Creek
Newell Spring
New Hope
Newman Meadows
Newsome Creek
Newt Gulch
Newt Gulch
Newt Young Ditch
Newton Creek
Newton Creek
Niagara Creek
Niagara Point
Nichol Spring
Nichols Camp (historical)
Nichols Creek
Nichols Creek
Nichols Ranch
Nichols Spring
Nichols Spring
Nick Barry Spring
Nick Eaton Ridge
Nicoll Creek
Nicoson Cemetery
Ben Johnson Mountain
Negro Knob
Negro Knob Trail (historical)
Nightshade Lakes
Nine Dollar Gulch
Nine Top Spring
Ninemile Creek
Ninemile Ridge
Ninemile Saddle
Ninemile Creek
Nineteenhundred Eighteen Gulch
Nineteenhundred Seventeen Gulch
Nineteenhundred Sixteen Gulch
Ninth Creek
Nip and Tuck Lakes
Nipple Butte
Nipple Creek
Nixon Creek
Number Six Canal
No Man Creek
No Man Shelter
No Name Creek
No Name Creek
No Name Creek
No Name Flat
No Name Reservoir
No Name Spring
Noah Butte
Noah Creek
Noble Creek
Noble Garden Spring
Noel Creek
Nogle Creek
Nohorn Butte
Noisy Creek
Nolan Slough
Nome Creek
Nome Peak
Nook Creek
Noon
Noon Creek
Noonday Mine
Noonday Ridge
Nork Creek
Norma Creek
Norman Canyon
Norna Spring
Norris Pond
North and South Trail
North Beach
North Beaver Creek
North Bend
North Blue Lake Group
North Boulder Creek
North Calimus Spring
North Canal
North Cape Creek
North Cinder Peak
North Combs Spring
North Corner Reservoir
North Corral Lake
North Creek
North Creek
North Creek
North Davis Creek
North Fairview Mountain
North Flat Spring
North Fork
North Fork East Fork Rock Creek
North Fork Alsea River
North Fork Anderson Creek
North Fork Bean Creek
North Fork Bear Creek
North Fork Beaver Creek
North Fork Beaver Creek
North Fork Bieberstedt Creek
North Fork Big Butte Creek
North Fork Big Sheep Creek
North Fork Breitenbush River
North Fork Bridge Creek
North Fork Bridge Creek
North Fork Buck Creek
North Fork Buck Creek
North Fork Bull Run River
North Fork Burnt River
North Fork Cabin Creek
North Fork Cable Creek
North Fork Cape Creek
North Fork Carrol Creek
North Fork Cascade Creek
North Fork Catherine Creek
North Fork Cedar Creek
North Fork Cedar Creek
North Fork Chetco River
North Fork Chilcoot Creek
North Fork Chocktoot Creek
North Fork Clackamas River
North Fork Clark Creek
North Fork Clarks Fork Creek
North Fork Cliff Creek
North Fork Cogswell Creek
North Fork Cold Spring Creek
North Fork Collier Creek
North Fork Cow Camp
North Fork Crane Creek
North Fork Crooked River
North Fork Dahl Creek
North Fork Deadwood Creek
North Fork Deardorff Creek
North Fork Deep Creek
North Fork Deer Creek
North Fork Deer Creek
North Fork Desolation Creek
North Fork Dry Creek
North Fork Durham Creek
North Fork Elk Creek
North Fork Elk Creek
North Fork Elk River
North Fork Fall Creek
North Fork Falls
North Fork Fivemile Creek
North Fork Fourbit Creek
North Fork Galice Creek
North Fork Gravel Creek
North Fork Green Point Creek
North Fork Groundhog Creek
North Fork Guard Station (historical)
North Fork Gumboot Creek
North Fork Hubbard Creek
North Fork Imnaha River
North Fork Indian Creek
North Fork Indigo Creek
North Fork Iron Creek
North Fork Jim Creek
North Fork John Day Recreation Site
North Fork John Day River
North Fork King Creek
North Fork Lake Creek
North Fork Little Butte Creek
North Fork Lobster Creek
North Fork Louse Creek
North Fork Malheur Recreation Site
North Fork Malheur River
North Fork McDowell Creek
North Fork McKay Creek
North Fork Meacham Creek
North Fork Meadow
North Fork Middle Fork Willamette River
North Fork Mill Creek
North Fork Mill Creek
North Fork Mineral Creek
North Fork Molalla River
North Fork Munger Creek
North Fork Owens Creek
North Fork Park Creek
North Fork Pass Creek
North Fork Reservoir
North Fork Ridge
North Fork Rock Creek
North Fork Rock Creek
North Fork Rough and Ready Creek
North Fork Ruby Creek
North Fork Siletz River
North Fork Silver Creek
North Fork Simpson Creek
North Fork Sixes River
North Fork Smith River
North Fork Sprague River
North Fork Spring Creek
North Fork Whychus Creek
North Fork Staley Creek
North Fork Steelhead Creek
North Fork Street Creek
North Fork Salmonberry Creek
North Fork Summit Creek
North Fork Trail
North Fork Trout Creek
North Fork Trout Creek
North Fork Tumalo Creek
North Fork Twelvemile Creek
North Fork Umatilla River
North Fork Wall Creek
North Fork Walla Walla River
North Fork Wallowa Creek
North Fork Wenaha River
North Fork West Camp Creek
North Fork Whisky Creek
North Fork Willow Creek
North Fork Winberry Creek
North Fork Wind Creek
North Fork Wolf Creek
North Fork Yachats River
North Fox Canyon Creek
North Jetty
North Jetty
North Jones Prairie
North Lake
North Lake
North Lake
North Marble Gulch
North Matthieu Lake
North Minam Guard Station
North Minam Meadows
North Minam River
North Minam Trail
North Mountain
North Myrtle Creek
North Paulina Peak
North Peak
North Pine Creek
North Pinhead Butte
North Pisgah Spring
North Point
North Point
North Pole Creek
North Powder River
North Powder Valley
North Prairie
North Prong Maple Creek
North Reynolds Creek
North Rock
North Rosary Lake
North Roy Creek
North Santiam River
North Scotty Creek
North Sister
North Sister Creek
North Slough
North Spit
North Squaw Tip
North Tenmile Lake
North Trail Creek
North Twin Lake
North Umpqua River
North Unit Main Canal
North Wickiup Campground
North Willow Creek
North Willow Spring
North Wilson
North Wolf Creek
Northeast Fork Rock Creek
Northern Glades
Northern Prairie
Norton Creek
Norton Fork
Norwegian Creek
Lake Notasha
Notch Lake
Nowhere Meadow
Number Eight Gulch
Number Eight Peak
Number Seven Gulch
Nunamaker Pond
Nunamaker Spring
Nurse Creek
Nute Slough
Nye Creek
Nye Creek
Nye Ranch
O'Neil Butte
O'Neil Creek
O'Neil Spring
OK Butte
O'Brien
O'Brien Creek
O'Brien Creek
O'Connell Creek
O'Conner Meadow
O'Kelly Creek
O'Neill Butte
O'Rouick Spring
Oak Creek
Oak Flat
Oak Flat
Oak Flat Lookout
Oak Flats
Oak Flats
Oak Grove Butte
Oak Grove Ditch
Oak Grove Fork Clackamas River
Oak Grove Work Center (historical)
Oak Grove School (historical)
Oak Lawn Memorial Park
Oak Mountain
Oak Ridge
Oar Creek
Oard Flat
Oard Spring
Oasis Spring
Oasis Spring
Oat Butte
Oatman Flat
Obenchain Ranch
Obenchain Reservoir
Obernolte Spring
Observation Gap
Observation Peak
Obsidian Creek
Obsidian Trail
Ocean Beach Recreation Site
Oceanside
Ochillee Spring
Ochoco Agate Beds
Ochoco Butte
Ochoco Creek
Ochoco Creek Park
Ochoco Divide Recreation Site
Ochoco Main Canal
Ochoco Mountains
Ochoco Pass
Lookout Mountain Ranger Station
Ochoco Reservoir
Ochoco Elementary School
Ochoco Spring
Ochoco State Park
Ochre Creek
Odell
Odell Butte
Odell Creek
Odell Creek
Odell Creek
Odell Creek Recreation Site
Odell Lake
Odell Pasture
Oden Ranch
Offenbacher Gulch
Offenbacher Point
Officer Creek
Officer Spring
Officer Springs
Ogle Creek
Ogle Mountain Mine
Ogre Creek
Oh Boy Forest Camp (historical)
Ohm Spring
Ojalla Bridge
Ojalla Creek
Ok Truck Barn
Okanogan Creek
Olallie Butte
Olallie Creek
Olallie Lake
Olallie Meadow
Peninsula Recreation Site
Olallie Trail
Old Baldy
Old Blue Mountain
Old Burn Way
Old Cabin Spring
Old Camp Pond
Old Channel Mine
Old Cold Spring
Old Desolation Driveway Trail
Old Dole Smith Homestead
Old Dry Creek
Old Fairview
Old Forest Camp
Old German Brethren Church
Old Glory Mine
Old Humbolt Diggings
Old Johnson Mill (historical)
Old Kennedy Cabin (historical)
Old Maid Flat
Old Man Camp
Old Man Creek
Old Man Creek
Old Man Rock
Old Mill Canyon
Old Peterson Ranch
Old Red Mine
Old Schoolhouse Spring
Old Stephenson Ranch
Oldenburg Lake
Olive Butte
Olive Creek
Olive Lake
Olive Lake Camp
Oliver Creek
Oliver Creek
Oliver Spring
Olmstead Creek
Olmstead Meadow
Olson Meadows
Olson Mountain
Ona
One Trough Canyon
One Trough Spring
Oneatta Point
Oneonta (historical)
Oneonta Creek
Oneonta Falls
Onion Camp
Onion Creek
Onion Creek
Onion Creek
Onion Creek
Onion Creek
Onion Creek Trail
Onion Flats
Onion Gulch
Onion Knoll
Onion Mountain
Onion Spring
Onion Spring
Onion Spring
Opal Butte
Opal City
Opal Creek
Opal Creek
Opal Creek
Opal Lake
Opal Lake
Opal Mountain
Opal Spring
Opal Springs
Ophir
Ophir Mine
Ophir Mountain
Opie Dilldock Pass
Orange Creek
Ordell Ditch
Oregon Bonanza Mine
Oregon Recreation Site
Oregon Caves National Monument and Preserve
Oregon Caves Trail
Oregon Desert
Oregon Gulch
Oregon Gulch Camp
Oregon Mine Creek
Oregon Mountain
Oregon State University
Oretown
Oriental Basin
Oriental Creek
Oriole Mine
Orion Mine
Ork Reef
Orofino Gulch
Orphan Butte
Orphan Creek
Orris Pond
Osborne Canyon
Osborne Spring
Oscar Creek
Osier Creek
Otis
Mule Creek Basin
Otis Creek
Otis Junction
Otis Mountain
Ott Cow Camp
Otter Creek
Otter Creek
Otter Creek
Otter Creek
Otter Lake
Otter Point
Otter Rock
Otter Spring
Ottertail Lake
Outside Canal
Ouxy Spring
Oval Lake
Overholt Creek
Overholt Creek
Overholt Spring
Overtime Spring
Overturf Butte
Owen Spring
Owens Butte
Owens Creek
Owings Creek
Owl Cabin Way
Owl Creek
Owl Creek
Owl Creek Meadow
Owl Creek Trail
Owl Hollow
Owl Mine
Owsley Creek
Owsley Hogback
Owyhee Canyon
Owyhee River
Owyhee Spring
Owyhee Spring Reservoir
Oxbow Ranch
Oxbow Spring
Oxhead Ridge
Oxstable Creek
Oysterville
P and P Spring
PK Creek
Pacific Creek
Pack Rat Spring
Packard Creek
Packard Creek Trail
Packers Gulch
Packers Gulch
Packsaddle Canyon
Packsaddle Creek
Packsaddle Creek
Packsaddle Gap
Packsaddle Mountain
Packsaddle Reservoir
Packsaddle Spring
Packsaddle Spring
Packsaddle Spring
Packsaddle Trail
Paddy Creek
Paddy Spring
Paddys Meadow
Paddys Valley
Page Creek
Page Creek Guard Station
Page Mountain
Page Springs
Paine Creek
Painted Rock Creek
Paisley
Paisley Flat Well Number One
Paisley Flat Well Number Two
Paisley Flat Well Number Three
Paiute Cemetery
Palanush Butte
Palatine Hill
Palisade Point
Palisades
Palmateer Creek
Palmateer Meadows
Palmer Butte
Palmer Creek
Palmer Creek
Palmer Glacier
Palmer Junction School (historical)
Palmer Lake
Palmer Peak
Palmer Peak
Palmer Reservoir
Palmer Spring
Palomino Creek Reservoir
Palouse Creek
Pamelia Creek
Pamelia Lake
Pamelia Lake Trail
Pan Creek
Pansy Basin
Pansy Mountain
Panther Bar
Panther Creek
Panther Creek
Panther Creek
Panther Creek
Panther Creek
Panther Creek
Panther Creek
Panther Creek
Panther Creek
Panther Creek
Panther Gulch
Panther Gulch
Panther Gulch
Panther Lake
Panther Mountain
Panther Peak
Panther Ridge
Panther Ridge
Panther Trail
Papoose Creek
Papoose Creek
Papoose Lake
Papoose Lake
Papoose Lakes
Paquet Gulch
Paradise
Paradise Bar
Paradise Cemetery
Paradise Creek
Paradise Creek
Paradise Creek
Paradise Creek
Paradise Lake
Paradise Mine
Paradise Park Shelter
Paradise Park Trail
Paradise Ridge
Paradise Trail
Paragon Lake
Parallel Creek
Parasol Butte
Pardee Spring
Paris Spring
Parish Lake
Park Butte
Park Creek
Park Creek
Park Creek
Park Creek
Park Creek
Park Lake
Park Lake
Park Meadow
Park Meadows
Park Trail
Parkdale
Parker Butte
Parker Canyon
Parker Creek
Parker Creek
Parker Creek
Parker Creek
Parker Creek
Parker Creek
Parker Creek
Parker Hills
Parker Meadow
Parker Meadow
Parker Meadows
Parker Meadows Recreation Site
Parker Reservoir
Parker Slough
Parker Spring
Parker Spring
Parkey Springs
Parkers Flat
Parkers Mill
Parkerville Mine
Parkett Creek
Parliament (historical)
Parrett Mountain
Parrish Creek
Parsnip Creek
Parsnip Creek
Parsnip Creek
Parsnip Springs
Part Creek
Partin Butte
Partin Spring
Paxton Creek
Partridge Creek
Pasola Mountain
Pass Creek
Pass Creek
Pass Creek
Pass Creek Shelter
Pass Creek Trail
Paste Creek
Pasture Creek
Pasture Spring
Pat Creek
Patjens Lakes Trail
Patricia Creek
Patrick Creek
Patrick Meadow
Patsy Lake
Patterson Creek
Patterson Mountain
Patterson Spring
Patton Meadow
Paul Creek
Paulina
Paulina Butte
Paulina Creek
Paulina Creek
Paulina Creek Falls
Paulina Lake
Paulina Lake Recreation Site
Paulina Mountains
Paulina Peak
Paulina Peak Trail
Paulina Prairie
Paulina Reservoir
Paulina Valley
Pawn
Pawnee Lake
Paxton
Payraise Spring
Payten Creek
Payten Trail
Payton Gulch
Payton Spring
Pea Ridge
Peabody Homestead
Peabody Spring
Peach Creek
Peak Creek
Pear Lake
Pearce Gulch
Pearce Point
Pearl Creek Guard Station
Pearse Peak
Pearsoll Peak
Pearson Butte
Pearson Cabin
Pearson Creek
Pearson Creek
Pearson Guard Station
Pearson Ridge
Pearson Trail
Peaslee Creek
Peat Creek
Peavine Camp
Peavine Creek
Peavine Creek
Peavine Creek
Peavine Lookout
Peavine Mountain
Peavine Ridge
Peavine Ridge
Peavine Spring
Mount Peavine
Peavy Cabin
Pebble Bay
Pebble Ford Recreation Site
Pebble Hill
Pechuck Lookout
Peck Cabin
Peck Gulch
Peck Spring
Peddlers Creek
Peddlers Ridge
Pedro Canyon
Pedro Creek
Pedro Ridge
Peep Creek
Peep Creek Camp (historical)
Peep Creek Trail (historical)
Peerless Spring
Peet Creek
Peggler Butte
Pelican Bay
Pelican Butte
Pelican Butte Trail
Pelican Creek
Pelican Forest Service Station
Pelt Creek
Pelton Dam
Pelton Park
Pen Creek
Pen Point
Pen Way Trail
Pendleton Spring
Pengra Pass
Penland Prairie
Penn Creek
Penn Lake
Penn Prairie
Pennington Creek
Pennington Mountain
Pepper Camp
Pepper Creek
Pepper Creek
Pepper Mountain
Percival Creek
Perdin Creek
Perdue Creek
Perham Creek
Perham Creek Spring
Perkins Creek
Perkins Creek
Perkins Spring
Perrin Spring
Perry Butte
Perry Butte Way
Perry Lake
Perry Meadows
Perry Point
Perry School
Perry Spring
Peter Paul Prairie
Peter Skene Ogden State Park
Peters Pasture
Peters Spring
Peterson Cabin
Peterson Creek
Peterson Creek
Peterson Creek
Peterson Creek Reservoir
Peterson Lava
Peterson Point
Petersen Spring
Peterson Spring
Petes Camp
Petes Camp Creek
Petes Lake
Petes Point
Petticoat Creek
Pewee Creek
Pfefferkorn Canyon
Pfefferkorn Ridge
Phantom Lake
Phantom Natural Bridge
Phantom Ship
Pheasant Creek
Pheasant Creek
Phelps Creek
Phelps Spring
Phillips Creek
Phillips Creek
Phillips Creek
Phillips Creek
Phillips Ditch
Philomath
Phipps Creek
Phipps Meadow
Phlox Point Recreation Site (historical)
Phoenix Mine
Pick Creek
Pick Spring
Picketpin Flat
Picketpin Spring
Pickett Butte Lookout Tower
Pickett Creek
Pickett Mountain
Pickett Prairie
Picnic Creek
Picnic Spring
Picture Rock
Picture Tree Springs
Pie Creek
Pie Meadow
Pierce Creek
Pierce Point
Pierpont Spring
Pig Iron Lookout
Pig Iron Mountain
Pig Iron Trail
Pikes Camp
Pilcher Creek
Pileup Canyon
Pileup Creek
Pileup Saddle
Pillar Peak
Pillar Rock
Pilot Rock
Pilot Butte
Pilot Butte Canal
Pilot Butte Cemetery
Pilot Butte North Canal
Pilot Butte South Canal
Pilot Butte State Scenic Viewpoint
Pilot Rock
Pilpil Butte
Pinard Butte
Pine Butte
Pine Cone Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek
Pine Creek Cow Camp
Pine Creek Mountain
Pine Creek Shelter (historical)
Pine Creek Trail
Pine Creek Trail
Pine Crest Trail
Pine Flat
Pine Flat
Pine Flat
Pine Flat Creek
Pine Grove
Pine Grove
Pine Gulch
Pine Gulch
Pine Hollow
Pine Hollow
Pine Knoll Basin
Pine Lakes
Pine Mountain
Pine Mountain Observatory
Pine Rest Recreation Site
Pine Ridge
Pine Ridge
Pine Ridge
Pine Ridge
Pine Ridge Spring
Pine Ridge Trail
Pine Spring
Pine Spring
Pine Spring Basin
Pine Stub Creek
Pine Tree Campground
Pine Tree Gulch
Pine Tree Spring
Pine Tree Spring
Pine Tree Spring
Pine Tree Spring
Pine Valley
Pinewan Lake
Pinhead Buttes
Pinhead Creek
Pink Creek
Pinkie Spring
Pinnacle Creek
Pinnacle Creek
Pinnacle Peak
Pinnacle Point
Pinnacle Ridge Trail
Pinnacle Valley
Pint Creek
Pinto Creek
Pinto Mountain
Pinto Mountain Way
Pinus Creek
Pioneer Bridle Trail
Pioneer Butte
Pioneer Ford Recreation Site
Pioneer Gulch
Pioneer Memorial Hospital Prineville
Pioneer Monument
Pioneer Park
Pioneer City Park
Tollgate Campground
Pioneer Way
Pipe Clamp Spring
Pipe Fork
Pipe Rock
Pipe Spring
Pipe Spring
Piper Lake
Pipestone Creek
Pipp Spring
Pisgah Spring
Mount Pisgah
Pismire Camp
Pistol Butte
Pistol River
Pistol River
Pitch Creek
Pitcher Creek
Pitcher Ranch
Pitchfork Ridge
Pitsua Butte
Pittsburg Creek
Piute Rock
Pizer Creek
Placedor Gulch
Placer Ditch
Placer Gulch
Placer Mine
Plainview
Plainview Ditch
Plant Canyon
Plass Canyon
Plateau Creek
Platt Creek
Platt Lake
Plaza Lake
Pleasant Center (historical)
Pleasant Hill
Pleasant Ridge
Pleasant Valley
Pleasant Valley Cemetery
Pleasant Valley Creek
Plenty Bear Ridge
Plot Butte
Plum Trees
Plumb Lake
Plumber Spring
Plummer Gulch
Plusfour Creek
Pluto Spring
Pocket Creek
Pocket Lake
Poer Reservoir
Pogue Point
Pogue Spring
Point Recreation Site
Point Comfort
Point Mountain
Point Terrace
Poison Creek
Poison Creek
Poison Creek
Poison Creek
Poison Hollow
Poison Point
Poison Spring
Poison Spring
Poker Bill Spring
Polallie Campground (historical)
Polallie Creek
Polallie Creek
Polander Creek
Polar Spring
Pole Bridge Creek
Pole Bridge Creek
Pole Bridge Creek
Pole Bridge Recreation Site
Pole Butte
Pole Camp Spring
Pole Canyon
Pole Creek
Pole Creek
Pole Creek
Pole Creek
Pole Creek
Pole Creek
Pole Creek
Pole Creek Ditch
Pole Creek Spring
Pole Creek Swamp
Pole Creek Trail
Pole Gulch
Pole Gulch
Pole Patch Canyon
Pole Spring
Pole Spring
Pole Spring
Pole Spring
Poley-Allen Ditch
Polie Creek
Pollard Butte
Pollard Creek
Polly Creek
Pollywog Butte
Pollywog Spring
Poly Top Butte
Pomeroy Dam
Pompadour Bluff
Ponderosa Spring
Ponina Butte
Ponina Creek
Muriel O Ponsler Memorial State Scenic Viewpoint
Pony Creek
Pony Creek
Pony Point
Ponyshoe Mine
Pool Prairie
Poole Creek
Poole Creek
Poole Hill
Poole Lake
Poole Slough
Poop Creek
Poopanelly Creek
Poor Boy Mine
Poore Creek
Poorman Mine
Pop Creek
Pope Spring
Mount Popocatepetl
Poppy Creek
Porcupine Camp
Porcupine Creek
Porcupine Peak
Porcupine Reservoir
Porcupine Ridge
Porcupine Spring
Porcupine Spring
Porky Creek
Porky Lake
Port Orford
Port Orford Cedar Experimental Forest
Port Orford Cedar Forest State Wayside
Port Spring
Portage Trail
Porter Creek
Porter Creek
Porter Creek
Porter Ranch
Porter School (historical)
Porter Spring
Porter Spring
Porterville (historical)
Fir Ridge Campus
Portland Creek
Portuguese Canyon
Portuguese Flat
Portuguese Spring
Post Camp Recreation Site
Post Gulch
Post Gulch
Post Point
Post School (historical)
Post Spring
Posy Valley Ditch
Pot Creek
Pot Creek
Pot Creek
Pot Creek Cabin
Pot Creek Trail
Potamus Creek
Potamus Point
Potamus Ridge
Potato Butte
Potato Hill
Potato Illahe Mountain
Potato Patch Mine
Pothole Butte
Pothole Camp
Pothole Creek
Pothole Meadow
Pothole Spring
Pothole Spring
Potlid Creek
Potter Creek
Potter Meadows
Potter Mountain
Potter Mountain Trail
Potts Lake
Poujade Field
Poujade Ranch
Poverty Flat
Poverty Gulch
Poverty Meadows
Powder Creek
Powder Creek
Powder Creek Trail
Powder House Hill
Powder Spring Reservoir
Powder Springs
Powell Creek
Powell Creek
Powell Creek
Powell Gulch
Powell Mountain
Powell Spring
Powerline Spring
Powerline Spring
Powers
Powers Ranch
Powwatka Ridge
Prairie Camp Shelter
Prairie Recreation Site
Prairie City
Prairie Creek
Prairie Creek
Prairie Creek
Prairie Creek
Prairie Creek Cemetery
Prairie Diggings
Prairie Farm Creek
Prairie Farm Spring
Prairie Hill
Prairie Hill
Prairie Hill
Prairie Mountain
Prairie Peak
Prater Creek
Prather Creek
Preacher Creek
Preacher Flat
Preachers Peak
Pretty Lake
Pretty Lake Trail
Priday Agate Beds
Prill Lake
Prince Gulch
Princess Creek
Princess Creek Recreation Site
Princess Ridge
Prineville Valley
Pringle Butte
Pringle Creek
Pringle Falls
Pringle Falls Recreation Site
Proctor Creek
Profane Gulch
Professor Spring
Promise
Prong Creek
Proposal Rock
Prospect
Prospect Creek
Prospect Creek
Prospect Lake
Prospect Spring
Prospect Spring
Prouty Glacier
Providence Creek
Pryor
Public Waterhole
Puck Lakes
Packer Spring
Puddin Rock
Puddin Rock Creek
Puddle Spring
Puddle Spring Work Center
Pullen Canyon
Pulpit Rock
Puma Creek
Puma Creek Recreation Site
Puma Spring
Pumice Butte
Pumice Butte
Pumice Desert
Pumice Flat
Pumice Flat
Pumice Point
Pumice Well
Pumphouse Creek
Pumpkin Creek
Pumpkin Ridge
Pumpkinseed Mountain
Punch Bowl Falls
Punchbowl Falls
Punky Lake
Pansy Lake
Pup Creek
Pup Creek
Pup Prairie
Puppy Creek
Puppy Lake
Purdy Creek
Purple Mountain
Putnam Spring
Putney Meadows
Putney Mountain
Puzzle Creek
Puzzle Creek
Pyburn Creek
Pygmy Lake
Pyle Creek
Pyramid Creek
Pyramid Lake
Pyramid Lake
Pyramid Rock
Pyramid Rock
Pyramid Rock
Pyramid Rock
Pyramid Trail
Pyramid Trail
Quail Creek
Quail Prairie Creek
Quail Prairie Mountain
Quaking Aspen Spring
Quaking Aspen Spring
Quarry Creek
Quartz Butte
Quartz Canyon
Quartz Creek
Quartz Creek
Quartz Creek
Quartz Creek
Quartz Creek
Quartz Gulch
Quartz Gulch
Quartz Gulch
Quartz Gulch
Quartz Gulch
Quartz Mountain
Quartz Mountain
Quartz Mountain
Quartz Mountain Guard Station
Quartzville
Quartzville Creek
Quartzville Guard Station
Quebec Mine
Quebec Hill
Queen Creek
Questionmark Lake
Quicksand Creek
Quicksand Spring
Quinn Creek
Quinn Creek Trail
Quinn Meadows
Quinn River Recreation Site
Quirk Spring
Quita Creek
Quosatana Butte
Quosatana Creek
R D Spring
R F Smith Ranch
R T Spring
R K Spring
Booth State Scenic Corridor
Rabbit and Porcupine Creek Forest Camp
Rabbit Butte
Rabbit Creek
Rabbit Creek
Rabbit Ears
Rabbit Ears
Rabbit Mine
Rabbit Ridge
Rabbit Ears Creek
Raber Canyon
Racing Creek
Racks Creek
Radar Hill
Raft Lake
Rafter Ranch
Rager Creek
Ragged Creek
Ragged Ridge
Ragged Rock Spring
Ragged Rocks
Ragged Rocks Trail (historical)
Ragsdale Butte
Ragsdale Lookout
Ragsdale Spring
Rail Hollow
Rail Canyon
Rail Canyon
Rail Canyon
Rail Creek
Rail Creek
Rail Creek
Rail Creek
Rail Creek
Rail Creek
Rail Creek
Rail Creek Butte
Rail Creek Trail
Rail Glade
Rail Gulch
Rail Gulch Spring
Rail Hollow
Rail Hollow
Rail Spring
Railroad Canyon
Railroad Creek
Railroad Gap
Railroad Pond
Rainbow Bay
Rainbow Creek
Rainbow Creek
Rainbow Creek
Rainbow Creek
Rainbow Creek
Rainbow Falls
Rainbow Lake
Rainbow Mine
Rainbow Point
Rainbow Quarry
Rainbow Spring
Rainbow Springs
Rainbow Trough Spring
Rainier Spring
Rainrock
Rains Canyon
Rainy Creek
Rainy Lake
Raker Point
Rakes Meadow
Raleigh Creek
Ralph Creek
Ralphs Spring
Ram Creek
Ram Creek
Ramona Falls
Ramsey Creek
Ramsey Creek
Ramsey Mine
Ramsey Mine
Ramsey Ranch
Ramsey Spring
Ran Creek
Rancheree Canyon
Rancheria Creek
Rancheria Creek
Rancheria Ranch
Rand
Randall Canyon
Ranes & Borger Mine
Range School (historical)
Ranger Butte
Ranger Creek
Ranger Creek
Ranger Prairie
Ranger Spring
Ranger Spring
Ranger Station Camp (historical)
Ranger Station Camp (historical)
Rankins Horse Pasture
Ransom Creek
Ransom Creek
Rapidan Creek
Rapidan Trail
Rapp Gulch
Rarey Spring
Rasler Creek
Rasmuss Meadow
Rasmussen House
Raspberry Creek
Raspberry Mountain
Rastus Camp Spring
Rastus Creek
Rastus Mountain
Rat Butte
Rath Creek
Rattlesnake Canyon
Rattlesnake Creek
Rattlesnake Creek
Rattlesnake Creek
Rattlesnake Creek
Rattlesnake Creek
Rattlesnake Creek
Rattlesnake Mountain
Rattlesnake Ridge
Rattlesnake Ridge
Rattlesnake Ridge
Rattlesnake Spring
Rattlesnake Spring
Rattlesnake Spring
Rattlesnake Spring
Rattlesnake Trail
Rattlesnake Trail
Rattlesnake Way
Raw Dog Creek
Rawhide Spring
Ray Cole Campground
Ray Creek
Ray Flat
Ray Mine
Ray Ranch
Mount Ray
Razz Lake
Red Gulch
Read Creek
Reade Canyon
Reagan Gulch
Reavis Creek
Rebel Creek
Rebel Rock
Rebel Rock Lookout
Rebel Rock Trail
Record Creek
Record Mine
Recreation Creek
Red Bird Mine
Red Blanket Creek
Red Blanket Mountain
Red Blanket Trail
Red Boy Mine
Red Butte
Red Butte
Red Butte
Red Butte Lake
Red Rock Canyon
Red Cedar Creek
Red Cinder Butte
Red Cloud Mine
Red Cone
Red Cone
Red Cone Spring
Red Cone Spring
Red Crater
Red Creek
Red Creek
Red Creek
Red Dog Creek
Red Fir Creek
Red Fir Spring
Red Flat
Red Flat
Red Gulch
Red Gulch
Red Gulch
Red Hill
Red Hill
Red Hill
Red Hill
Red Hill
Red Hill
Red Hill
Red Hill Creek
Red Hill Guard Station (historical)
Red Hill Spring
Red House Ditch
Red Lake
Red Lake
Red Lake
Red Lake Trail
Red Lick Spring
Red Meadow
Red Mound
Big Red Mountain
Red Mountain
Red Mountain
Red Mountain Creek
Red Mountain Mine
Red Mountain Prairie
Red Mountain Trail
Red Mountain Trail
Red Peak
Red Ridge
Red Ridge
Red Rock
Red Rock Canyon
Red Rock Pass
Red Saddle
Red Shed Canyon
Red Slide Lake
Red Spring
Red Spring Canyon
Red Top Meadow
Red Top Spring
Red Top Spring
Red Trough Spring
Red Wolf Pass
Redcloud Cliff
Redfish Rocks
Redjacket Mine
Redmans Tooth
Redmont Creek
Redrock Creek
Redtop Mountain
Redwood Elementary School
Reed and Hawley Mountain
Reed Creek Grange
Reed Island
Reed Ranch
Reed Ranch
Reed Reservoir
Reed Reservoir
Reeder Gulch
Reeder Reservoir
Reeds Mill
Reedsport
Reedy Creek
Reese Creek
Reeves Creek
Reflection Lake
Refrigerator Creek
Reichen Well
Reid Glacier
Reilly Creek
Reilly Flat
Reinecke Burn
Reneke Creek
Renfrew Glacier
Renner Ranch
Reno Spring
Reser Cabin
Reser Creek
Reservation Mountain
Reservation Trail
Reserve Meadow
Reservoir Creek
Reservoir Trail
Resort Creek
Rest Lake
Rest Lawn Cemetery
Retz Creek
Reuter Well
Reynolds Butte
Reynolds Creek
Reynolds Creek
Reynolds Creek
Reynolds Creek Trail
Reynolds Ridge
Reynolds Ridge Lookout (historical)
Rhea Creek
Rheumatiz Gulch
Rhinehart
Rhododendron Ridge Shelter
Rhododendron Ridge Trail
Rhoda Creek
Rhodabush Creek
Rhodes Creek
Rhodes Creek
Rhodod Creek
Rhododendron
Rhododendron Creek
Rhododendron Meadow
Rhododendron Ridge
Rhododendron Ridge
Rice Corral Reservoir
Rice Corral Spring
Rice Creek
Rice Creek
Rich Creek
Rich Gulch
Rich Gulch
Richard Butte
Richard G Baker Park
Richardson
Richland
Richter Cabin
Richter Mountain
Rickard Creek
Rickman Ranch
Rickreall Ridge
Ricks Creek
Riddle Field
Rice Spring
Ridenor Canyon
Riders Camp
Ridgetop Pond
Riffle Lake
Rifle Creek
Rifle Spring
Rigdon Butte
Rigdon Guard Station
Riggs Creek
Riggs Meadow
Right Fork Pleasant Creek
Right Fork Salt Creek
Right Fork Squaw Creek
Right Hand Fork Rock Creek
Right Hand Fork Steve Fork
Right Hand Fork West Fork Williams Creek
Rilea Creek
Riley
Riley Creek
Riley Creek
Riley Creek Butte
Riley Creek Meadow
Riley Mountain
Rim Creek
Rim Lake
Rim of the Crater
Rim Rock
Rim Rock
Rim Rock Ranch
Rim Rock Spring
Rim Rock Trail
Rimrock Creek
Rimrock Lake
Rimrock Point
Rimrock Ridge
Rimrock Spring
Rimrock Spring
Rimrock Spring
Rimrock Spring
Rimrock Spring
Rimrock Trail
Rinfroe Springs
Ring Butte
Ring Lake
Ring Tail Creek
Ringo Butte
Ringsmeyer Reservoir
Ripley Gulch
Ripplebrook Recreation Site
Rippleton Creek
Riser Butte
Riser Creek
Risley Creek
Ritter
Ritter Butte
Ritter Cemetery
Ritter Grange (historical)
Ritter School (historical)
Wyeth Recreation Site
River Head Camp (historical)
Riverside Cemetery
Riverside Recreation Site
Riverside Recreation Site
Riverside Gulch
Riverside Ranch
Roach Creek
Roache Creek
Road Camp Spring
Road Canyon
Road Canyon
Road Creek
Road Creek
Road Creek Spring
Roads End Spring
Road Gulch
Road Gulch
Road Gulch
Road Spring
Road Spring
Road Springs
Roads End
Roadside Reservoir
Roadside Spring
Roadside Spring
Roaring Creek
Roaring Creek
Roaring Creek Trail
Roaring River
Roaring River
Roaring River Recreation Site
Roaring River Ridge
Roaring River Trail
Roaring Spring
Roaring Spring
Roaring Spring
Roaring Spring
Roaring Springs Canyon
Roba Brothers Mine
Roba Butte
Roba Creek
Roba Spring
Roba Westfall Mine
Robbins Ditch
Roberts (historical)
Roberts Creek
Roberts Creek
Roberts Creek Trail (historical)
Robertson Bridge
Robertson Mine
Robertson Ridge
Robertson Spring
Robideau Landing
Robin Reservoir
Robinette Creek
Robinhood Creek
Robinhood Guard Station
Robins Island
Robinson Butte
Robinson Canyon
Robinson Canyon
Robinson Gulch
Robinson Prairie
Robinson Ranch
Robinson Spring
Robinson Spring
Robinson Spring Creek
Robinsonville
Rock Butte
Rock Butte
Rock Canyon
Rock Cone
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Upper Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek
Rock Creek Recreation Site
Rock Creek Recreation Site
Rock Creek Guard Station
Rock Creek Hideout
Rock Creek Lake
Rock Creek Ranch
Rock Creek Reservoir
Rock Creek Springs
Rock Gulch
Rock Gulch
Rock Lake
Rock Lake
Rock Lakes
Rock Mesa
Rock Pit Reservoir
Rock Point
Rock Pond
Rock Reservoir
Rock Rim Lake
Rock Slide
Rock Spring
Rock Spring
Rock Spring
Rock Spring
Rock Spring
Rock Spring
Rock Spring
Rock Spring
Rock Spring
Rock Spring
Rock Spring
Rock Spring
Rock Spring
Rock Spring
Rock Spring Camp
Rock Springs
Rock Spring
Rock Springs Trail
Rockhouse Creek
Rocking Bar Spring
Rockingchair Creek
Rockpile Lake
Rockpile Mountain
Rockpile Ranch
Rocktop Butte
Rockwall
Rockwood Creek
Rocky Bar Gulch
Rocky Basin
Rocky Bedground
Rocky Bend Recreation Site
Rocky Butte
Rocky Butte
Rocky Butte Way Trail
Rocky Creek
Rocky Flat
Rocky Flat
Rocky Flat
Rocky Flat Spring
Rocky Ford
Rocky Gulch
Rocky Knoll
Rocky Point
Rocky Point
Rocky Point
Rocky Point
Rocky Point
Rocky Point
Rocky Point Trail
Rocky Point Way
Rocky Prairie
Rocky Ridge
Rocky Ridge
Rocky Top
Rocky Top Shelter
Rocky Top Trail
Rod Creek
Rodeo Butte
Rodeo Spring
Rodgers Gulch
Rodgers Ridge
Rodley Butte
Rodley Butte Trail
Rodman Rock
Rodman Spring
Roger Creek
Rogers (historical)
Rogers Butte
Rogers Creek
Rogers Creek
Rogers Creek
Rogers Spring
Rogger Meadow
Rogger Peak
Rogue River
Rogue River
Rogue River Reef
Rogue-Umpqua Divide Trail
Roland Creek
Rolling Grounds
Rolling Riffle Campground (historical)
Rolling Riffle Creek
Roman Nose Mountain
Romine Creek
Rondowa
Roop Spring
Roosevelt Beach
Roosevelt Creek
Roosevelt Point
Roosevelt Elementary School (historical)
Roosevelt School (historical)
Roosevelt Way
Rooster Rock
Rooster Rock
Rooster Rock
Rooster Rock
Rooster Rock Spring
Roots Creek
Root Spring
Root Spring
Roper Spring
Rosa Creek
Rosary Creek
Rosary Lakes
Rose Hill
Rose Lodge
Rosebud Creek
Rosewood Gulch
Roslyn Lake (historical)
Ross Creek
Ross Flat
Ross Gulch
Ross Mountain
Ross Ranch (historical)
Ross Reservoir
Ross Spring
Ross Spring
Rough and Ready Creek
Rough and Ready State Park
Rough Canyon
Rough Canyon
Rough Canyon Reservoir
Rough Canyon Reservoir
Rough Creek
Rough Creek
Rough Creek
Rough Creek Trail
Rough Ridge
Round Basin School (historical)
Round Butte
Round Butte
Round Butte
Round Butte
Round Butte
Round Butte
Round Butte Dam
Round Creek
Round Creek
Round Lake
Round Lake
Round Lake
Round Lake
Round Lake
Round Lake Trail
Round Lake Trail
Round Meadow
Round Meadow
Round Meadow
Round Meadow
Round Meadow Spring
Round Meadow Trail
Round Meadows
Round Mountain
Round Mountain
Round Mountain
Round Mountain
Round Mountain
Round Mountain
Round Mountain
Round Mountain
Round Mountain
Round Mountain
Round Mountain
Round Mountain Creek
Round Mountain Mine
Round Mountain Pass
Round Mountain Spring
Round Mountain Well
Round Pass
Round Prairie
Round Prairie
Round Prairie
Round Prairie Creek
Round Prairie Reservoir
Round Reservoir
Round Top
Round Top
Round Top
Round Top
Roundtop
Roundtop Mountain
Roundup Grounds
Rover Creek
Row River
Rowdy Creek
Rowland Creek
Rowley Gulch
Rowley Mine
Roy Canyon
Roy Creek
Royal Purple Creek
Royal White Mine
Royce Mountain
Royce Ranch
Roys Spring
Rubble Creek
Ruby Creek
Ruby Creek
Ruby Creek
Ruby Creek Mines
Ruby Peak
Ruby Reservoir
Ruch
Ruckel Creek
Ruckel Junction
Ruckel Ridge
Ruckel Spring
Ruddy Hill
Rudio Creek
Rudio Meadows
Rudio Mountain
Rudolph Creek
Rugg Cemetery
Rugg Spring
Rugged Crest Palisades
Rum Creek
Rumbaugh Creek
Run Gulch
Rush Creek
Rush Creek
Rush Creek
Rush Creek
Rush Creek
Rush Creek
Rush Spring
Rushing Water Creek
Russ Creek
Russ Lake
Russell Creek
Russell Creek
Russell Glacier
Russell Lake
Russell Point
Russell Spring
Rustler Mine
Rustler Peak
Rusty Butte
Rusty Creek
Rutabaga Creek
Ruth Gulch
Ruth Lake
Ruth Mountain
Ruth Spring
Ryan Creek
Ryan Creek
Ryan Creek
Ryan Ranch Meadow
Ryder Creek
Rye Branch
Rye Flat
Rye Mountain
Rye Ridge
Rye Spring
Rye Spur
Ryegrass Ditch
Rysdam Canyon
S Lake
S S Spring
S-2 Spring
SOB Spring
S S Spring
S'Ocholis Canyon
Sabre Creek
Sacajawea Peak
Sacajawea Spring
Sacajawea Spring
Sad Lake
Saddle Basin
Saddle Basin Creek
Saddle Butte
Saddle Camp
Saddle Camp
Saddle Camp
Saddle Camp Butte
Saddle Camp Spring
Saddle Creek
Saddle Gulch
Saddle Gulch
Saddle Hollow
Saddle Lake
Saddle Mountain
Saddle Mountain
Saddle Mountain
Saddle Peaks
Saddle Rock
Saddle Spring
Saddle Spring
Saddle Spring
Saddle Springs
Saddle Bag Mountain
Saddleblanket Mountain
Sadie Spring
Sage Creek
Sage Creek
Sage Flat
Sage Hen Butte
Sage Hen Canyon
Sage Hen Creek
Sage Hen Creek
Sage Hen Creek
Sage Hen Creek
Sage Hen Creek
Sage Hen Flat
Sage Hen Flats
Sage Hen Spring
Sage Hen Spring
Sage Hen Spring
Sage Hen Valley
Sage Spring
Sage Spring
Sagebrush Creek
Sagebrush Draw
Sagebrush Flat
Sagebrush Flat
Sagebrush Flat
Sagebrush Spring
Sagehen Creek
Sagehen Gulch
Sahale Falls
Sailor Gulch
Sailors Gulch
Saint Andrews Cemetery
Saint John Creek
Saint Peter Creek
Saint Peters Dome
Salado
Salal Creek
Salal Point
Salal Spring
Salamander Lake
Mount Salem
Saling Creek
Sally Creek
Sally Glade
Sallys Flat
Sallys Flat Spring
Salmon Back Ridge
Salmon Butte
Salmon Butte Trail
Salmon Creek
Salmon Creek
Salmon Creek
Salmon Creek
Salmon Creek
Salmon Creek
Salmon Creek
Salmon Creek
Salmon Creek
Salmon Creek
Salmon Creek
Salmon Creek Trail
Salmon Falls
Salmon Falls
Salmon Mountain
Salmon Mountain
Salmon Mountain Trail
Salmon River Campground (historical)
Salmon River Guard Station
Salmon River Guard Station
Salmon River Meadows
Salsbury Creek
Salt Butte
Salt Canyon
Salt Canyon Spring
Salt Creek
Salt Creek
Salt Creek
Salt Creek
Salt Creek
Salt Creek
Salt Creek
Salt Creek
Salt Creek
Salt Creek Falls
Salt Creek Guard Station
Salt Lick Prairie
Salt Rock Prairie
Salt Spring
Salt Trail
Saltpeter Creek
Sam Creek
Sam Creek
Sam Creek
Sam Creek
Samison Mountain
Sampson Butte
Sampson Creek
Sams Cabin
Sams Creek
Samuel H Boardman State Park
San Antone Creek
Sam Davis Spring
San Lou Flat
San Marine
Sand Bar Gulch
Sand Butte
Sand Canyon
Sand Creek
Sand Creek
Sand Creek
Sand Creek
Sand Creek
Sand Creek
Sand Creek
Sand Flat
Sand Gulch
Sand Hill
Sand Hollow
Sand Island
Sand Mountain
Sand Mountain
Sand Pass
Sand Pass Creek
Sand Prairie
Sand Ridge
Sand Rock Creek
Sand Rock Mountain
Sand Spring
Sand Spring
Sand Spring
Sanderson Spring
Sandlake
Sandoz Gap
Sandpoint Lake
Sandstone Creek
Sandstone Trail
Sandy
Sandy Butte
Sandy Glacier
Sandy Hollow
Sandy Lake
Sandy River Trail
Sandy Saddle
Sanford Canyon
Sanford Creek
Sanford Spring
Sanger Gulch
Sanger Mine
Sankey Creek
Santiam Pass
Santiam Peak
Sarah Lake
Lake Sarah
Sardine Butte
Sardine Creek
Sardine Creek
Sardine Spring
Sargent Butte
Satan Creek Forest Camp
Sauers Creek
Sauers Flat
Saulsberry Saddle
Saunders Creek
Saunders Creek
Savage Bluffs
Savage Creek
Savage Creek
Savage Creek
Savage Creek
Savage Creek
Sawmill Canyon
Sawmill Creek
Sawmill Creek
Sawmill Creek
Sawmill Creek Camp
Sawmill Flat
Sawmill Gulch
Sawmill Number One Reservoir
Sawmill Number Two Reservoir
Sawtell Canyon
Sawtooth Creek
Sawtooth Meadows
Sawtooth Mountain
Sawtooth Mountain
Sawtooth Peak
Sawtooth Ridge
Sawtooth Rock
Sawtooth Rock
Sawtooth Spring
Sawtooth Way
Scab Reservoir
Scaffold Creek
Scandia Tunnel
Scar Creek
Scar Mountain
Scar Mountain Trail
Scare Creek
Scaredman Camp
Scaredman Creek
Schadler Cow Camp
Scharff Cabin Creek
Swartz Creek
Schleur Creek
Schleur Gulch
Schlupe Spring
Schmadeke Reservoir
Schmoker Spring
Schmoker Well
Scholfield Creek
School Creek
School Creek
School Flat
School Fork
School Land Bay
Schoolcraft Creek
Schoolhouse Canyon
Schoolhouse Creek
Schoolhouse Creek
Schoolhouse Creek
Schoolhouse Creek
Schoolhouse Creek
Schoolhouse Creek
Schoolhouse Gulch
Schoolma'am Creek
Schoolmam Spring
Schoolmarn Spring
Schooner Creek
Schreiner Peak
Schrum Creek
Schulz Creek
Schumacher Creek
Schurtz Creek
Schurtz Spring
Schwayder Mine
Schweitzer Creek
Scissors Creek
Scissors Spring
Scoria Cone
Scorpion Butte
Scorpion Creek
Scorpion Creek
Scorpion Mountain
Scorpion Mountain Trail
Scorpion Ridge Trail
Scot Prairie
Scotch Creek
Scotch Gulch
Scott Bluffs
Scott Creek
Scott Creek
Scott Creek
Scott Creek
Scott Mountain
Scott Pass
Scott Reservoir
Scott Spring
Scott Trail
Mount Scott
Scotts Cabin Creek
Scotts Cabin Spring
Scotts Recreation Site
Scottsburg
Scotty Creek
Scotty Creek
Scotty Spring
Scout Creek
Scout Hill
Scout Lake
Scout Lake
Scout Lake
Scout Lake Group Camp
Sea Lion Point
Seal Rock
Seal Rock State Recreation Site
Seal Rocks
Sealy Creek
Searose Beach
Sears Creek
Sears Lake
Seats Dam
Sebastopol Creek
Second Creek
Second Creek
Second Creek
Second Creek
Second Creek
Second Creek
Second Creek Spring
Second Peak
Second Prairie Mountain
Second Water Gulch
Secret Creek
Secret Recreation Site
Section 9 Spring
Section Corner Spring
Section Creek
Section Line Gap
Section Line Spring
Section Line Trail
Section One Spring
Section Eleven Spring
Seekseequa Junction
Seeley Creek
Seep Spring
Seldom Creek
Sellers Creek
Sellers Marsh
Selma
Seneca
Seneca Substation
Senoj Lake
Senoj Trail
Sentinel Creek
Sentinel Hills
Sentinel Peak
Sentinel Peak
Sentinel Rock
Separation Creek
Separation Creek Meadow
Separation Creek Trail
Sera Spring
Serene Lake
Serenity Bay
Serpentine Flat
Serpentine Point
Serpentine Spring
Serviceberry Camp
Seven C Ranch
Seven D Bar Spring
Seven Lakes Basin
Seven Lakes Trail
Seven Sixty Reservoir
Seven Sixty Spring
Seven Up Spring
Seven-Nine Trail
Seven-Thirty Mine
Sevenmile Canal Levee
Sevenmile Creek
Sevenmile Creek
Sevenmile Creek
Sevenmile Guard Station
Sevenmile Marsh
Sevenmile Peak
Sevenmile Ridge
Seventh Creek
Seventy Creek
Sevier
Sewer Trail
Shade Creek
Shadow Canyon
Shadow Lake
Shady Creek
Shady Creek
Shady Creek
Shady Dell Recreation Site
Shady Recreation Site
Shady Gap
Shale Butte
Shale Creek
Shale Lake
Shamrock Creek
Shamrock Creek
Shamrock Spring
Shan Creek
Shanahan Place
Shane Saddle
Shaner Spring
Shanghai Creek
Shangri-La Mill (historical)
Sharp Peak
Sharp Ranch
Sharp Ridge
Sharps Creek
Shasta Costa Creek
Shasta Costa Riffle
Shaw Brant Ditch
Shaw Creek
Shaw Creek
Shaw Ditch
Shaw Gulch
Shaw Mountain
Shaw Spring
Shaws Camp
Shea Canyon
Shea Creek
Shed Camp
Shed Creek
Sheep Bridge Recreation Site
Sheep Camp
Sheep Camp Spring
Sheep Corral Spring
Sheep Corral Springs
Sheep Corrals
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek
Sheep Creek Butte
Sheep Creek Butte
Sheep Creek Divide
Sheep Ridge Ditch
Sheep Flat
Sheep Gulch
Sheep Gulch
Sheep Herder Creek
Sheep Mountain
Sheep Mountain
Sheep Prairie
Sheep Ranch Creek
Sheep Ridge
Sheep Ridge
Sheep Rock
Sheep Rock
Sheep Rock
Sheep Rock
Sheep Rock
Sheep Rock
Sheep Rock
Twin Buttes
Sheep Rock Creek
Sheep Rock Spring
Sheep Smother Spring
Sheep Spring
Sheep Spring
Sheep Spring
Sheep Spring
Sheephead Mountain
Sheephead Mountain Spring
Sheepy Creek
Sheepy Reservoir
Sheepy Spring
Sheldon Creek
Sheldon Ridge
Shell Creek
Shell Rock
Shell Rock Butte
Shell Rock Spring
Shelley Family Cemetery
Shelley Springs
Shellrock Creek
Shellrock Creek Recreation Site
Shellrock Lake
Shellrock Mountain
Shellrock Mountain
Shellrock Spring
Shelter Cove
Shepperds Dell State Park
Sherar Burn
Sheridan Mountain
Sherlock Dipping Vat Spring
Sherman Ranch
Sherman Spring
Sherwood Butte
Sherwood Recreation Site
Sherwood Canyon
Sherwood Creek
Sherwood Creek
Sherwood Meadow
Sherwood Spring
Shevlin Park
Shevlin Well
Sheythe Creek
Shimmiehorn Creek
Shin Creek
Shingle Creek
Shingle Gulch
Shingle Mill Butte
Shingle Mill Creek
Shining Lake
Shirley Lake
Shirts Creek
Shirttail Creek
Shitepoke Creek
Shitepoke Trail
Shitike Butte
Shitike Creek
Shivigny Mountain
Shoemaker Creek
Shoestring Butte
Shoestring Creek
Shoestring Creek
Shoestring Glade
Shoestring Spring
Shoestring Spring
Shoofly Creek
Shoofly Spring
Shop Gulch
Shorewood
Short Beach
Short Butte
Short Canyon
Short Creek
Short Creek
Short Creek
Short Creek
Short Creek
Short Creek
Short Creek
Short Creek
Short Creek
Short Creek Forest Service Station
Short Creek Prairie
Short Lake
Short Lake Mountain
Short Ridge
Short Ridge
Short Wiley Creek
Shorty Davis Ranch
Shorty Reservoir
Shot Pouch Creek
Shotgun Creek
Shotpouch Creek
Shott Spring
Shovel Creek
Shown Troughs
Shroy Meadows
Shueble Creek
Shukash Butte
Shultz Creek
Shuman Canyon
Shump Gulch
Shutter Arm
Shutter Creek
Shutter Landing
Shy Creek
Si Lake
Siah Butte
Siamese Spring
Sibley Draw
Siboco (historical)
Sicklebar Spring
Sidehill Spring
Sidehill Spring
Sidewalk Creek
Signal Buttes
Silcox Hut
Silent Creek
Silent Creek
Siletz River
Silica Camp (historical)
Silica Mountain
Silica Trail
Siltcoos Recreation Site (historical)
Siltcoos Lookout
Siltcoos River
Silver Butte
Silver Butte
Silver Butte Trail
Silver Creek
Silver Creek
Silver Creek
Silver Creek
Silver Creek
Silver Creek
Silver Creek
Silver Creek
Silver Creek
Silver Creek Marsh
Silver Dollar Flat
Silver Falls
Silver Fork Gap
Silver Grange Ditch
Silver Gulch
Silver Hill Trail
Silver King Mountain
Silver Lake
Silver Lake Ditch
Silver Lake Ranger Station
Silver Peak
Silver Prairie
Sliver Rock
Silver Spring
Silver Spring Camp
Silver Star Mine
Silver Tip Camp
Silver Tip Mine
Silvers Mine
Silverstairs Creek
Silvies
Silvies Landing
Silvies River
Silvies Valley
Silvies Valley Ranch
Simax Bay
Simerson Spring
Simmons Creek
Simmons Draw
Simmons Gulch
Simmons Ranch (historical)
Simnasho Butte
Simon Lake
Simonetti Spring
Simpson Creek
Simpson Creek
Simpson Creek
Simpson Park
Sims Butte
Lake Simtustus
Singe Creek
Single Creek
Sink Creek
Sink Creek
Sink Creek
Sinker Mountain
Sinnott Memorial
Sisi Butte
Sisi Creek
Siskiyou Peak
Siskiyou Springs
Sister Spring
Sisters Cemetery
Sisters Horse Camp (historical)
Sisters Mirror Lake
Sisters Rocks
Sisters State Park (historical)
Sitkum Butte
Sitkum Creek
Seits Ridge
Siuslaw (historical)
Siuslaw River
Siuslaw School (historical)
Siwash Creek
Six Corners
Six Creek
Six Dollar Gulch
Six Lakes
Six Lakes Trail
Sixbit Point
Sixes
Sixes River
Sixmile Butte
Sixmile Creek
Sixmile Creek
Sixmile Ridge
Sixteen Butte
Sixteen Gulch
Sixth Creek
Sixtynine Reservoir
Skag Creek
Skagway Creek
Skagway Reservoir
Skate Gulch
Skeen Ranch
Skeeter Camp
Skeeter Camp Trail
Skeeters Creek
Skeeters Camp
Skeleton Mountain
Skell Channel
Skell Head
Skellock Draw
Skid Creek
Skillet Creek
Skimmerhorn Creek
Skin Shin Creek
Skinner Creek
Skinner Creek
Skinner Glacier
Skinner Mine
Skinner Spring
Skinners Fork
Skiphorton Creek
Skipper Creek
Skipper Creek
Skipper Lakes
Skookum Butte
Skookum Canyon
Skookum Creek
Skookum Creek
Skookum Creek
Skookum Creek
Skookum Creek
Skookum Creek Camp
Skookum Creek Recreation Site
Skookum Game Exclosure
Skookum Lake
Skookum Lake
Skookum Prairie
Skookum Prairie Lookout
Skookum Rock
Skookum Spring
Skookum Spring
Skookum Spring
Skookum Spring
Skookum Spring
Skookumhouse Butte
Skookumhouse Prairie
Skull Creek
Skull Creek
Skull Creek
Skull Creek
Skull Creek Camp
Skull Gulch
Skull Gulch Spring
Skull Hollow
Skull Spring
Skull Spring
Skull Spring
Skunk Butte
Skunk Cabbage Spring
Gilbert Creek
Skunk Creek
Skunk Creek
Skunk Creek
Skunk Creek
Skunk Creek
Skunk Creek
Skunk Gulch
Skunk Hollow
Sky Lakes Area
Skyline Trail
Skyline Alternate Trail
Skyline Creek
Skyline Mine
Slab Creek
Slabhouse Springs
Slack Canyon
Slapjack Butte
Slash Spring
Slate Creek
Slate Creek
Slate Creek
Slate Creek
Slate Creek
Slate Gulch
Slate Reservoir
Slate Rock
Slater Creek
Slaughter Gulch
Slaughterhouse
Slaughterhouse Gulch
Slayton Corral
Sled Creek
Sled Springs
Sled Springs Work Center
Sleepy Bill Fork
Sleepy Creek
Sleepy Ridge
Sleppy Mine
Slick Creek
Slick Creek
Easter Creek
Slick Ear Creek
Slick Rock Creek
Slick Rock Creek
Slick Rock Creek
Slick Rock Creek
Slick Taw Gulch
Slickear Canyon
Slickear Creek
Slickear Mountain
Slickrock Creek
Slide Creek
Slide Creek
Slide Creek
Slide Creek
Slide Creek
Slide Creek
Slide Creek
Slide Creek
Slide Creek
Slide Creek
Slide Creek
Slide Creek
Slide Creek
Slide Creek
Slide Creek
Slide Creek
Slide Creek
Slide Creek
Slide Creek
Slide Creek
Slide Gulch
Slide Lake
Slide Lake
Slide Mountain
Slide Mountain
Slide Mountain
Slide Mountain
Slide Spring
Slideout Lake
Slim Creek
Slim Prairie
Slipper Creek
Slipper Lake
Sloan Cemetery
Sloan Creek
Sloan Gulch
Sloan Mountain
Sloans Ridge
Slop Spring
Slough Recreation Site
Slow Creek
Sluice Creek
Sluice Creek
Sluice Creek
Sluice Creek Saddle
Slusher Creek
Slusher Spring
Small Creek
Small Creek
Small Creek
Small Creek
Smith Birch Spring
Smith Canyon
Smith Canyon
Smith Creek
Smith Creek
Smith Creek
Smith Creek
Smith Creek
Smith Creek
Smith Ditch
Smith Gate
Smith Lake
Smith Meadows
Smith Mountain
Smith Prairie
Smith Prairie Trail
Smith Reservoir
Smith Ridge
Smith Ridge
Smith Ridge
Smith River
Smith River
Smith River Falls
Smith River Grange
Smith River Light
Smith River Ranger Station (historical)
Smith Rock
Smith Spring
Smith Springs Campground
Smith Well
Smiths Ford (historical)
Smock Prairie
Smock School (historical)
Smokey Bear Spring
Smoky Creek
Smoky Creek
Smoky Spring
Snoot Creek
Smooth Gulch
Smooth Gulch
Smooth Hollow
Snag Lake
Snail Creek
Snailback Creek
Snake Creek
Snake Creek
Snake Creek
Snake Den
Snakehead Creek
Snaketooth Butte
Snaketooth Way
Snapp Spring
Snell Creek
Snell Lake
Snipe Creek
Snipe Creek
Snow Basin
Snow Cabin
Snow Camp Meadow
Snow Camp Mountain
Snow Camp Trail
Snow Creek
Snow Creek
Snow Creek
Snow Creek
Snow Creek
Snow Creek
Snow Creek
Snow Creek
Snow Creek
Snow Creek
Snow Creek Ditch
Snow Creek Project Camp
Snow Fork Creek
Snow Gulch
Snow Mountain
Snow Mountain Spring
Snow Peak
Snowshoe Spring
Snow Spring
Snow Spring
Snowbird Mountain
Snowbird Shelter
Snowbrush Gulch
Snowshoe Butte
Snowshoe Creek
Snowshoe Creek
Snowshoe Creek Trail
Snowshoe Flat
Snowshoe Forest Camp (historical)
Snowshoe Lake
Snowshoe Lake Trail
Snowshoe Point
Snowshoe Spring
Snowshoe Spring
Snyder Canyon
Snyder Spring
Soap Creek
Soap Spring
Socialist Valley
Sock Hollow
Soda Creek
Soda Creek
Soda Creek
Soda Creek
Soda Creek Recreation Site
Soda Fork
Soda Gulch
Soda Gulch
Soda Smith Spring
Soda Spring
Soda Spring
Soda Spring
Soda Spring
Soda Springs
Soda Springs Dam
Soda Valley
Softwater Spring
Solace Camp
Soldier Camp
Soldier Camp Mountain
Soldier Creek
Soldier Creek
Soldier Creek
Soldier Creek
Soldier Gulch
Soldier Spring
Solitude Bar
Soloman Butte
Solomon Creek
Soloman Flat
Somers Creek
Somers Point
Sometime Reservoir
Lake Sonya
Soosap Peak
Sopher Ridge
Sorenson Creek
Sorghum Flat
Soup Spring
Soup Spring
Sour Apple Flat
Sourdough Camp
Sourdough Camp (historical)
Sourdough Flat
Sourdough Gulch
Sourdough Ridge
Sourdough Spring
Sourgrass Camp
Sourgrass Creek
Sourgrass Creek
Sourgrass Mountain
Sourgrass Summit
Sourgrass Trail
South Amity Creek
South Arm Reservoir
South Arm Spring
South Arm Yokum Valley
South Beaver Creek
South Bend Mountain
South Blue Lake Group
South Boundary Spring
South Branch Mill Creek
South Breitenbush Trail
South Recreation Site
South Canal
South Canyon
South Canyon
South Canyon
South Cinder Peak
South Corral Lake
South Cottonwood Reservoir
South Creek
South Creek
South Flat
South Flat
South Fork Middle Fork Imhaha River
South Fork Alsea River
South Fork Anderson Creek
South Fork Antelope Creek
South Fork Argo Creek
South Fork Bald Mountain Creek
South Fork Basin
South Fork Bean Creek
South Fork Bear Creek
South Fork Bear Creek
South Fork Beaver Creek
South Fork Beaver Creek
South Fork Bieberstedt Creek
South Fork Big Butte Creek
South Fork Big Creek
South Fork Big Sheep Creek
South Fork Big Wall Creek
South Fork Boulder Creek
South Fork Breitenbush River
South Fork Buck Creek
South Fork Buck Creek
South Fork Bull Run River
South Fork Burnt River
South Fork Cabin Creek
South Fork Cable Creek
South Fork Recreation Site
South Fork Campground (historical)
South Fork Canyon Creek
South Fork Cedar Creek
South Fork Chesnimnus Creek
South Fork Chetco River
South Fork Chilcoot Creek
South Fork Clackamas River
South Fork Clark Creek
South Fork Clarks Fork Creek
South Fork Cliff Creek
South Fork Cogswell Creek
South Fork Cold Spring Creek
South Fork Collier Creek
South Fork Coquille River
South Fork Cottonwood Creek
South Fork Cripple Creek
South Fork Dam
South Fork Deardorff Creek
South Fork Deep Creek
South Fork Deer Creek
South Fork Deer Creek
South Fork Deer Creek
South Fork Desolation Creek
South Fork Durham Creek
South Fork Elk Creek
South Fork Elk River
South Fork Fivemile Creek
South Fork Floras Creek
South Fork Fourbit Creek
South Fork Gimlet Creek
South Fork Groundhog Creek
South Fork Hill
South Fork Howard Creek
South Fork Imnaha River
South Fork Iron Creek
South Fork Jim Creek
South Fork John Day River
South Fork King Creek
South Fork Lake Creek
South Fork Lemiti Creek
South Fork Little Butte Creek
South Fork Little Nestucca River
South Fork Lobster Creek
South Fork Long Creek
South Fork McDowell Creek
South Fork McKenzie River
South Fork Meadow Creek
South Fork Mill Creek
South Fork Mill Creek
South Fork Mineral Creek
South Fork Mosquito Creek
South Fork National Creek
South Fork North Fork Breitenbush River
South Fork Park Creek
South Fork Parsnip Creek
South Fork Pistol River
South Fork Ridge Trail
South Fork Roaring River
South Fork Rock Creek
South Fork Rogue River
South Fork Rough and Ready Creek
South Fork Round Prairie Creek
South Fork Ruby Creek
South Fork Salmon River
South Fork Salt Creek
South Fork Schooner Creek
South Fork Seekseequa Creek
South Fork Shelter
South Fork Silver Creek
South Fork Simpson Creek
South Fork Sixes River
South Fork Sprague River
South Fork Spring Creek
South Fork Spring Creek
South Fork Spring Creek
South Fork Whychus Creek
South waqímatáw Creek
South Fork Staley Creek
South Fork Steelhead Creek
South Fork Street Creek
South Fork Salmonberry Creek
South Fork Summit Creek
South Fork Sycan River
South Fork Taylor Creek
South Fork Tenmile Creek
South Fork Trail
South Fork Trask River
South Fork Trout Creek
South Fork Trout Creek
South Fork Tumalo Creek
South Fork Umatilla River
South Fork Vance Creek
South Fork Vine Maple Creek
South Fork Walla Walla River
South Fork Wallowa Creek
South Fork Warm Springs River
South Fork Way
South Fork Wenaha River
South Fork West Camp Creek
South Fork Whisky Creek
South Fork Wilkins Creek
South Fork Winberry Creek
South Fox Reservoir
South Inlet
South Jetty
South Jones Prairie
South La Pine Roadside Rest (historical)
South Lake
South Lake
South Marble Gulch
South Mountain
South Mountain
South Mountain Reservoir
South Myrtle Creek
South Pass Lake
South Pass Lake Trail
South Peak
South Peak
South Pine Creek
South Pinhead Butte
South Point
South Point
South Prairie
South Prairie Elementary School
South Prong Black Canyon Creek
South Prong Reservoir
South Prong Trail
South Prong Troughs
South Pyramid
South Pyramid Creek
South Roy Creek
South Santiam River
South Scotty Creek
South Shore Recreation Site
South Side Canal
South Sister Creek
South Sister
South Slough
South Spring
South Squaw Tip
South Trail Creek
South Twin Lake
South Umpqua Falls
South Umpqua Guard Station
South Umpqua River
South Waldo Shelter
South Walker Spring
South Willow Creek
South Wind Creek Reservoir
South Beach
Southern Oregon State University
Southwestern Oregon Community College
Souva Creek
Spain Saddle
Spangler Spring
Spanish Gulch
Spanish Peak
Sparks
Sparks Lake
Sparta Butte
Spaulding Mill
Spear F Spring
Spears Meadow
Spencer Cemetery
Spencer Creek
Spencer Creek
Spencer Creek
Spencer Creek
Spencer Gulch
Spencer Well
Sperry Creek
Sperry Creek
Sperry Spring
Sperry Spring
Specht Rim
Sphagnum Bog
Sphinx Butte
Sphinx Creek
Spider Creek
Spinning Lake
Spinning Lake
Spirit Lake
Spirit Lake
Spirit Mountain
Split Rock
Split Rock Creek
Spokane Creek
Sponge Creek
Sponge Creek Camp
Spoon Creek
Spoon Lake
Spoon Spring
Sportsman Lakes
Spot Creek
Spot Creek
Spout Spring
Sprague Gulch
Sprague River
Sprague River
Sprague River Valley
Spignet Butte
Spignet Creek
Spring Butte
Spring Butte
Spring Butte
Spring Butte Creek
Spring Butte Well
Spring Canyon
Spring Canyon Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Spring Creek
Perry South Campground
Spring Forest Camp
Spring Gulch
Spring Gulch
Spring Gulch
Spring Hollow
Spring Hollow
Spring Lake
Spring Meadow
Spring Mountain
Spring Prairie
Spring River
Spring River
Spring Valley Creek
Spring Valley Meadow
Springer Creek
Springer Mountain
Springwater
Sproats Meadow
Sproul Spring
Spruce Creek
Johns Creek
Spruce Creek
Spruce Creek
Spruce Gulch
Spruce Lake
Spruce Log Trail
Spruce Point
Spruce Spring
Spruce Spring
Spud Mountain
Spur Butte
Spy Lake
Square Lake
Square Mountain
Square Top
Akawa Butte
Squaw Butte
Waqíima Butte
Cúuy’em Butte
Squaw Butte
Kwiskwis Butte
Squaw Butte Creek
Squaw Butte Trail (historical)
taxsāwkt Canyon
Squaw Creek
Sru Creek
Squaw Creek
Tokatee Creek
Podo Creek
Latiwi Creek
Squaw Creek
Squaw Creek
Dunawi Creek
Kúckuc Creek
Škáypiya Creek
Aspen Creek
Mitáat Hiwéelece Creek
Tumala Creek
waqímatáw Creek
Sharp Creek
Squaw Creek
Squaw Creek
Squaw Creek
Squaw Creek
Tipi-Tehaga Creek
Se-ng abi Huudi Creek
Mona Creek
Congleton Creek
Whychus Creek
Wíwaanaytt Creek
Wewa Creek
Squaw Creek
Nestucca Bobb Creek
Pe’ískit Creek
ípsus tíḿe Creek
weelikéecet Creek
Isqúulktpe Creek
Three Sisters Canal
Upper Chush Falls
Isqúulktpe Creek Overlook
Se-ng abi Huudi Reservoir
Congleton Creek Reservoir
Se-ng abi Huudi Creek Spring
Squaw Flat
WogonagaT potso-na Flat
Tai Flat
Squaw Flat
Singing Horse Ranch
WogonagaT potso-na Flat Spring
Switchback Flat
Squaw Gulch
Akawa Gulch
Imnáha Gulch
Squaw Lake
Sru Lake
Squaw Lakes
Tumala Lakes
Shootingstar Meadow
Wíwaanaytt Meadow
Tumala Meadow
Podo Meadows
Squaw Mountain
Squaw Mountain
Squaw Mountain
Moohoo'oo Mountain
Tumala Mountain
Squaw Peak
Squaw Prairie
Hoona Ridge
Donaldson Rock
Squaw Spring
Squaw Spring
Tuhu-u Spring
Waqíima Spring
Aspen Spring
Patúšway Spring
Wináha’ay Spring
Squaw Tip Trail (historical)
Squaw Valley
Squeedunk Slough
Squeegee Creek
Squires Peak
Squirrel Camp (historical)
Squirrel Camp Creek
Squirrel Creek
Squirrel Peak
Squirrel Prairie
Squirrel Ridge
Squirrel Spring
Stack Creek
Stack Yards
Stag Lake
Stag Shelter
Stahl Canyon
Stahlbusch Island
Stahlman Point
Stair Creek
Stair Creek Falls
Stalder Creek
Staley Creek
Staley Ridge
Staley Ridge Trail
Stallard Reservoir
Stalling Butte
Stalter Mine
Stampede Creek
Stams Mountain
Standard Creek
Standard Mine
Standard Mine
Standfield Meadow
Standley Guard Station
Standley Spring
Stanley Cabin
Stanley Creek
Stanley Creek
Stanley Creek
Star Flat
Star Glade
Star Gulch
Star Gulch
Star Gulch Sulphur Camp
Applegate Ranger Station
Starkey Creek
Starkey Experimental Forest
Starr Creek
Starr Creek
Starr Creek
Starr Ridge
Starvation Creek
Starvation Creek State Park
Starvation Ridge
Starvation Trail
Starve-to-Death Ridge
Starveout Creek
Starveout Spring
Starwano Way
State Creek
State Ditch
State Line Creek
State Line Guard Station (historical)
Station Butte
Station Creek
Station Creek
Station Spring
Station Spring
Steamboat
Steamboat
Steamboat Creek
Steamboat Creek
Steamboat Falls
Steamboat Island
Steamboat Lake
Steamboat Mine
Steamboat Mountain
Steamboat Spring
Steamboat Trail
Steampot Creek
Stearn Cemetery
Stearns (historical)
Steeds Crossing
Steel Bay
Steel Cliff
Steele Mill Canyon
Steelhead Creek
Steelhead Falls
Steen Ranch
Steep Creek
Steep Creek
Steeple Rock
Steer Creek
Steer Creek
Steffin Meadow
Steiger Butte
Stein Butte
Steinhauer Creek
Steinmetz Creek
Steins Pillar
Mount Stella
Stephenson Creek
Stephenson Lake
Stephenson Mountain
Sterling Cemetery
Sterling Creek
Sterling Ditch
Sterling Gulch
Steve Fork
Steve Peak
Stevens Canyon
Stevens Creek
Stevens Spring
Stewart Cabin
Stewart Creek
Stewart Creek
Stewart Spring
Stewart Spring
Stewart Spring
Stewart Spring
Slick Rock Creek
Stickler Spring
Stickney Gulch
Still Creek
Still Creek Recreation Site
Still Creek Trail
Still Spring
Still Spring
Still Spring Creek
Stillwell Creek
Stilson Creek
Stimson Meadow
Stinger Creek
Stink Creek
Stinking Spring
Stinking Water Pond
Stithum Mine
Stockton Spring
Stone Butte
Stone Corral Creek
Stone Creek
Stone Gulch
Stone Mountain
Stone Spring
Stonewall Creek
Stoney Mountain
Stoney Point
Stony Creek
Stony Creek
Stony Creek
Stookey Flat
Store Gulch
Store Gulch Guard Station
Storm Creek
Storm Lake
Stormy Lake
Stott Mountain
Stouts Creek
Stove Spring
Stover Canyon
Straight Creek
Straight Creek
Straight Creek Cat Trail
Straight Creek Trail
Straight Whisky Creek
Stranahan Ridge
Strapping Creek
Strasburg Mine
Stratton Creek
Stratton Meadow
Stratton Place
Strawberry Butte
Strawberry Recreation Site
Strawberry Creek
Strawberry Creek
Strawberry Creek
Strawberry Creek
Strawberry Falls
Strawberry Flat
Strawberry Mountain Wilderness
Strawberry Range
Strawberry Reservoir
Strawberry Spring
Strawberry Spring
Street Creek
Strickland Flat
Strickland Spring (historical)
Strider Lake
String Butte
String Creek
Stringer Gap
Stringtown Gulch
Stroubs Mine
Stroud Springs
Stubblefield Fork
Stud Creek
Studhorse Creek
Stumbough Ridge
Stump Creek
Stump Creek
Stump Creek
Stump Creek Trail
Stump Lake
Stump Prairie
Stump Spring
Stupid Creek
Sturdevant Spring
Sturgill (historical)
Sturgill Creek
Sturgill Peak
Sturgill Rapids (historical)
Sturgis Fork
Sturgis Guard Station
Sucker Creek
Sucker Creek
Sucker Creek
Sucker Creek Gap
Sucker Creek Shelter
Sucker Creek Trail
Sucker Spring
Sudan Creek
Sugar Creek
Sugar Creek
Sugar Creek
Sugar Creek
Sugar Creek
Sugar Creek
Sugar Creek Reservoir
Sugar Gulch
Sugar Hill
Sugar Loaf Mountain
Sugar Peak
Sugar Pine Butte
Sugar Pine Camp (historical)
Sugar Pine Flat
Sugar Pine Mine
Sugar Pine Ridge
Sugar Pine Ridge
Sugar Pine Ridge Trail
Sugar Spring
Sugarbowl Creek
Sugarbowl Creek
Sugarbowl Ridge
Sugarloaf
Sugarloaf
Sugarloaf Butte
Sugarloaf Gulch
Sugarloaf Mountain
Sugarloaf Mountain
Sugarloaf Mountain
Sugarloaf Mountain
Sugarloaf Mountain
Sugarloaf Mountain
Sugarloaf Mountain
Sugarloaf Mountain
Sugarloaf Mountain
Sugarloaf Spring
Sugarloaf Spring
Sugarpine Burn
Sugarpine Creek
Sugarpine Mountain
Sugarpine Shelter
Suicide Well
Snipe Creek
Sullens Cow Camp
Sullivan Creek
Sullivan Creek
Sullivan Creek
Sullivan Gulch
Sullivan Spring
Sulphur Creek
Chapman Creek
Sulphur Creek
Sulphur Creek
Sulphur Creek
Sulphur Creek
Sulphur Creek
Sulphur Creek Trail
Sulphur Gulch
Sulphur Gulch
Sulphur Gulch
Sulphur Spring
Sulphur Spring
Sulphur Spring
Sulphur Spring
Sulphur Spring Butte
Sulphur Springs
Sumac Creek
Sumac Spring
Summer Creek
Summer Lake
Summer Lake
Summer Lake Hot Spring
Summerfield Canyon
Summerfield Ridge
Summers Creek
Summers Ranch
Summerville
Summerville - Imbler Cemetery
Summit (historical)
Summit Butte
Summit Cabin
Summit Camp
Summit Cascade Divide
Summit Creek
Summit Creek
Summit Creek
Summit Creek
Summit Creek
Summit Creek
Summit Creek
Summit Creek
Summit Creek Trail
Summit Guard Station
Summit Guard Station
Summit Lake
Summit Lake
Summit Lake
Summit Lake
Summit Lake
Summit Lake Trail
Summit Meadow
Summit Meadows
Summit Mount Emily Trail
Summit Mountain
Summit Point
Summit Prairie
Summit Prairie
Summit Prairie
Summit Prairie Truck Barns (historical)
Summit Ranger Station
Summit Ridge
Summit Ridge Spring
Summit Rock
Summit Rock
Summit Rock Point
Summit Spring
Summit Spring
Summit Spring
Summit Spring
Summit Spring Ridge
Summit Trail
Sumpter
Sumpter Creek
Sumpter Valley
Sun Creek
Sun Meadows
Sun Mountain
Sun Notch Trail
Sun Pass
Suncrest Point Lookout
Sunderland Canyon
Sundew Lake
Sundown Gap
Sundown Mountain
Sundstrom Place (historical)
Sunflower Creek
Sunflower Flat
Sunflower Flat
Sunflower Flats
Sunflower Spring
Sunny Camp
Sunny Hill Elementary School (historical)
Sunnyridge Grange
Sunrise Butte
Sunrise Creek
Sunrise Springs
Sunset
Sunset Cemetery
Sunset Cove Recreation Site
Sunset Heights Memorial Gardens
Sunset Lake
Sunset Lake Trail
Sunset Landing
Sunset Mountain
Sunset Shelter
Sunset Spring
Sunset Spring
Sunset Trail
Sunset View Recreation Site
Sunshine Creek
Sunshine Creek
Sunshine Creek
Sunshine Creek
Sunshine Creek
Sunshine Flat
Sunshine Flat Trail
Sunshine Guard Station
Sunshine Lake
Sunshine Spring
Suplee
Surprise Lake
Surprise Lake
Surprise Lake
Surprise Spring
Surprise Spring
Surprise Spring
Survey Spring
Surveyor Creek
Surveyor Mountain
Surveyor Peak
Surveyor Spring
Surveyors Benches
Surveyors Ridge
Susan Creek
Susanville
Suttle Lake
Sutton Creek
Sutton Creek
Sutton Gulch
Sutton Lake
Sutton Recreation Site
Svinth Creek
Swab Creek
Swagger Creek
Swain Prairie Spring
Swale Creek
Swale Creek
Swale Pond
Swale Spring
Swale Springs
Swalley Canal
Swallow Lake Trail
Swamp Basin
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek
Swamp Creek Hidden Meadows Trail
Swamp Gulch
Swamp Lake
Swamp Peak
Swamp Peak Trail
Swamp Spring
Swamp Spring
Swamp Way
Swamp Wells
Swamp Wells Butte
Swampy Lakes
Swampy Lakes Shelter
Swampy Lakes Trail
Swan Lake
Swan Lake Mountain
Swan Lake Point
Swan Mountain
Swan Valley
Swanson Creek
Swastika Mountain
Swastika Mountain Trail
Sweat Point
Swede Basin
Swede Cabin
Swede Cabin
Swede Cabin Flat
Swede Canyon
Swede Creek
Swede Heaven
Swede Lake
Swede Ridge Shelter
Sweet Creek
Sweet Grass Spring
Swick Creek
Swickey Canyon
Swift Creek
Swift Creek Trail
Swikert Meadow
Swindle Lake
Swing Field
Swinger Ditch
Swiss Flat
Swiss Spring
Swisshome
Switch Creek
Switchback Creek
Switchback Falls
Switchback Hill
Sycan Butte
Sycan Flat
Sycan Marsh
Sycan River
Sycan Siding
Symons Wood Camp
Syrup Creek
T Spring
T-6 Spring
TJW Reservoir
TNT Creek
TNT Gulch
Table Creek
Table Creek
Table Glade
Table Lake
Table Mountain
Table Mountain
Table Mountain
Table Mountain
Table Mountain
Table Mountain Cutoff Trail
Table Mountain Gulch
Table Mountain Spring
Table Mountain Trail
Table Mountain Trail
Table Rock
Table Rock
Table Rock
Table Rock
Table Rock
Table Rock
Table Rock Creek
Table Rock Fork
Table Spring
Tabor Diggings
Taft Creek
Taft Mountain
Tag Creek
Taggarts Bar
Taggarts Creek
Taghum Butte
Tahkenitch Creek
Tahkenitch Lake
Tahkenitch Recreation Site
Takilma
Talapus Butte
Mount Talapus
Talent
Tallow Butte
Tallow Creek
Tallowbox Mountain
Tally Creek
Tam Lake
Tam McArthur Rim
Tamanawas Falls
Tamarack Basin
Tamarack Butte
Tamarack Butte Reservoir
Tamarack Camp (historical)
Tamarack Camp
Tamarack Canyon
Tamarack Canyon
Tamarack Creek
Tamarack Creek
Tamarack Creek
Tamarack Creek
Tamarack Creek
Tamarack Creek
Tamarack Creek
Tamarack Creek
Tamarack Creek
Tamarack Creek
Tamarack Creek Spring
Tamarack Gulch
Tamarack Gulch
Tamarack Mountain
Tamarack Reservoir
Tamarack Spring
Tamarack Spring
Tamarack Spring
Tamarack Spring
Tamarack Spring
Tamarack Spring
Tamarack Spring
Tamarack Spring
Tamarack Spring
Tamarack Swamp
Tamba Ranch
Tammy Pond
Tandy Creek
Tank Spring
Tanner Creek
Tanner Lake
Tanner Mountain
Tanner Butte
Tanner Butte Trail
Tanner Creek
Tanner Cutoff Trail
Tanner Gulch
Tanner Spring
Tanners Pass
Tansy Reservoir
Tar Creek
Target Meadows
Tarzan Springs
Tate Creek
Tate Spring
Tater Hill
Tatouche Peak
Tats Spring
Taylor Burn Guard Station
Taylor Butte
Taylor Butte
Taylor Butte
Taylor Buttes
Taylor Creek
Taylor Creek
Taylor Creek
Taylor Creek
Taylor Creek
Taylor Creek
Taylor Creek
Taylor Flat
Taylor Gulch
Taylor Lake
Taylor Mountain
Taylor Ranch
Taylor Spring
Tea Creek
Tea Table Mountain
Teacup Lake
Teal Creek
Teal Lake
Teal Lake
Teal Lake
Teaser Creek
Tecumseh Spring
Teddy Lakes
Teddy Powers Meadow
Teepee Butte
Teepee Ridge
Teepee Spring
Teepee Spring
Teeter Creek
Teeter Creek Loop
Telephone Butte
Telephone Creek
Telephone Draw
Telephone Flat
Telephone Gulch
Telephone Gulch
Telephone Ridge
Telephone Ridge
Telephone Spring
Telephone Spring
Telephone Spring
Telephone Spring
Telephone Spring
Telfer Butte
Teller Butte
Teller Creek
Teller Flat
Temperance Creek
Tempest Mine
Temple Reservoir
Temple Spring
Templeton
Templeton Arm
Ten Cent Butte
Ten Cent Creek
Tenas Camp
Tenas Peak
Tenino Bench
Tenino Creek
Tenmile Butte
Tenmile Creek
Coleman Creek
Tenmile Creek
Ten Mile Creek Recreation Site (historical)
Tenmile Lake
Tenmile Ridge
Tenmile Shelter
Tennessee Creek
Tennessee Mountain
Tennessee Pass
Tent Prairie
Tepee Creek
Tepee Draw
Tepee Spring
Tepee Spring
Testament Creek
Teto Lake
Tetons
Tex Creek
Texas Bar Creek
Texas Butte
Texas Gulch
Texter Gulch
Tharp (historical)
Thayer Glacier
The Basin
The Big Pot
The Box
The Bridge School
The Bull Pasture
The Canyon
The Chimney
The Cockscomb
The Cove Palisades State Park
The Cutoff
The Dead Slough
The Dome
The Drew
The Dungeon
The Elbow
The Frog
The Gap
The Holdout Cow Camp
The Hole
The Horseshoe
The House Rock
The Husband
The Island
The Island
The Island
The Jumpoff
The Knob
The Loop
The Meadows
The Mill Ditch
The Narrows
The Narrows
The Narrows Bridge
The Notch
The Oaks
The Park
The Peaks
The Pinnacle
The Point
The Portage
The Potholes
The Potholes
The Potholes
The Punchbowl
The Rhubarb Patch
The Rock
The Shimmiehorn
The Slide
The Swamp
The Table
The Watchman
The Wife
Theimer Canyon
Thicket Reservoir
Thiel Creek
Thielsen Creek
Thielsen Creek Trail
Thielsen Forest Camp
Mount Thielsen
Thimble Mountain
Thimble Mountain Trail
Thimbleberry Mountain
Third Creek
Third Creek
Third Creek
Third Creek
Third Creek Spring
Thirsty Creek
Thirsty Gulch
Thirsty Gulch Spring
Thirsty Point
Thirteenmile Creek
Thirteenmile Spring
Thirty-Thirty Spring
Thirty-Thirty Spring
Thirtymile Creek
Thirtytwo Point Creek
Thomas Creek
Thomas Creek
Thomas Creek
Thomas Creek Campground (historical)
Thomas Creek Work Center
Thomas Hill
Thomas Spring
Thomas Trail
Thomason Creek
Thomason Meadow
Thomason Meadow Reservoir
Thomason Mine
Thompson Cabin
Thompson Corral
Thompson Corral
Thompson Creek
Thompson Creek
Thompson Creek
Thompson Creek
Thompson Creek
Thompson Creek
Thompson Creek
Thompson Creek
Thompson Creek
Thompson Creek
Thompson Creek Forest Camp
Thompson Creek Guard Station
Thompson Falls
Thompson Falls Spring
Thompson Flat
Thompson Flat Well
Thompson Gulch
Thompson Gulch
Thompson Gulch
Thompson Lake
Thompson Mountain
Thompson Point
Thompson Reservoir
Amity Creek Elementary School
Thompson Spring
Thompson Spring
Thompson Spring
Thompson Spring
Thompson Valley
Thomson Ranch
Thorn Creek
Thorn Creek
Thorn Creek
Thorn Creek
Thorn Creek
Thorn Creek
Thorn Creek
Thorn Creek Butte
Thorn Hollow
Thorn Mountain
Thorn Patch Spring
Thorn Prairie
Thorn Spring
Thorn Spring Butte
Thorn Spring Creek
Thornburg Placer Mine
Thornburg Spring
Thorn Creek Guard Station
Thornton Creek
Thorny Creek
Thorp Creek
Thorpe Creek
Thousand Springs
Thousand Springs Trail
Three Arch Rocks
Three Bear Spring
Three Buttes
Three Cabin Creek
Three Cabin Ridge
Three Cabin Spring
Three Cent Gulch
Three Cent Gulch
Three Cent Spring
Three Creek
Three Creek
Three Creek
Three Creek Butte
Three Creek Guard Station
Three Creek Lake Trail
Three Creek Ridge
Three Creek Trail
Three E Spring
Three Fingered Jack
Three Forks
Three J Spring
Three Lakes
Three Lakes Trail
Three Lynx
Three Lynx Creek
Three Pyramids
Three Rivers
Three Rock Creek
Three Rocks
Three Rocks
Three Rocks
Three Sisters
Three Springs
Three Trappers
Three Tree Lookout (historical)
Three Trough Creek
Three Trough Spring
Three-Seven Spring
Threebuck Creek
Threehorn Mountain
Threemile Creek
Threemile Creek
Threemile Creek
Threemile Creek
Threemile Creek
Threemile Creek
Threemile Ditch
Threemile Lake
Threemile School (historical)
Threemile Shelter
Threemile Spring
Threemile Trail
Thronson Creek
Thrush Pond
Thunder Creek
Thunder Creek
Thunder Egg Lake
Thunder Mountain
Thunder Mountain Trail
Thunder Mountain Trail
Thunder Rock
Thune Mountain
Tick Hill
Tickle Creek
Tide
Tidewater
Tie Creek
Tie Creek
Tie Spring
Tiger Creek
Tiger Creek
Tiger Mine
Tiger Springs
Tilden Creek
Tillamook
Tillamook Bay
Tillamook River
Tiller
Tiller Creek
Tillicum Creek
Tillicum Creek
Tillicum Mine
Tillotson Creek
Tilly Jane Creek
Tilly Jane Guard Station
Tilly Jane Trail
Tim Creek
Tim Long Creek
Timber Basin
Timber Cabin
Timber Canyon
Timber Crater
Timber Creek
Timber Creek
Timber Creek
Timber Creek
Timber Fall Butte
Timber Gulch
Timber Lake
Timbered Knoll
Timbered Rock
Timberline Creek
Timberline Trail
Timmy Lake
Timothy Butte
Timothy Creek
Timothy Guard Station
Timothy Lake
Timothy Meadow
Timothy Patch
Timothy Spring
Timothy Well
Timpanogas Lake
Timpanogas Way
Tin Canyon Gulch
Tin Can Spring
Tin Flag Ridge
Tin Troughs Spring
Tin Wagon Canyon
Tincup Creek
Tincup Creek
Tincup Creek
Tincup Pass
Tincup Peak
Tinker Creek
Tinroof Canyon
Tiny Creek
Tiny Creek
Tiny Lake
Tip Top Mine
Tip Top Spring
Tipsoo Creek
Tipsoo Trail
Tipton (historical)
Tire Creek
Tire Mountain
Tire Mountain Trail
Tish Creek
Tison Gulch
Tison School (historical)
Titanic Creek
Toad Creek
Toast Camp
Tobe Creek
Tobin Cabin
Tobin Ditch
Tobin Spring
Tod Creek
Todd Creek
Todd Lake
Toggle Meadows
Toketa Creek
Toketee Falls
Toketee Falls
Toketee Lake
Toledo
Toll Bridge County Park
Toll Rock
Tolman Creek
Tolman Ranch
Tolo Creek
Tolo Creek
Tolo Mountain
Tom and Jerry Trail
Tom Creek
Tom Creek
Tom Creek
Tom Dick and Harry Mountain
Tom Dick Trail
Tom East Creek
Mount Tom
Tom Spring
Tom Vawn Creek
Tom Young Creek
Mount Tom
Toms Meadow
Tombstone Gap
Tombstone Lake
Tombstone Prairie
Tomlike Mountain
Tomlinson Slough
Tommy Cork Spring
Tommy Creek
Tommys Spring
Tone Spring
Tones Creek
Tongue Gulch
Tonto Spring
Tony Creek
Tony Creek
Tony Creek
Tony Spring
Too Much Bear Lake
Toolbox Meadows
Toomey Gulch
Toothrock Tunnel 4555
Toothacher Creek
Top
Top Creek
Top Lake
Top Lake
Top Lake
Top School
Tope Creek
Topso Butte
Torchlight Gulch
Torchlight Spring
Torrent Spring
Tot Mountain
Tower Mountain
Tower Point
Town Gulch
Town Lake
Tracy Creek
Tracy Gulch
Tracy Mountain
Trail
Trail Butte
Trail Canyon
Trail Canyon
Trail Creek
Trail Creek
Trail Creek
Trail Creek
Trail Creek
Trail Creek
Trail Creek
Trail Creek
Trail Creek
Trail Creek
Trail Flat
Trail Gulch
Trail Meadow
Trail Ridge
Trail Spring
Trail Spring
Trail Spring
Tranquil Lake
Transvaal Mines
Trap Canyon
Trap Canyon Spring
Trap Creek
Trap Creek
Trap Creek
Trap Mountain
Trapper Creek
Trapper Creek
Trapper Creek
Trapper Creek
Trapper Gulch
Trapper Lake
Trapper Ridge
Trapper Shelter
Trapper Spring
Trapper Spring Meadow
Trappers Butte
Trask River
Trask Summit
Travail Creek
Traverse Creek
Traverse Ridge
Traxtel Creek
Treat River
Tree Root Canyon
Tree Root Spring
Trenholm Saddle
Trestle Creek
Triangle Hill
Triangle Lake
Tribble Creek
Trillium Lake
Trinity Creek
Triple Creek
Triple Spring
Triplet Spring
Tripod Camp
Troff Canyon
Trouble Creek
Trough Creek
Trough Creek Trail (historical)
Trough Gulch
Trough Spring
Trough Spring
Trough Spring
Trout Creek
Trout Creek
Trout Creek
Trout Creek
Trout Creek
Trout Creek
Trout Creek
Trout Creek
Trout Creek
Trout Creek
Trout Creek
Trout Creek
Trout Creek
Trout Creek
Trout Creek
Trout Creek
Trout Creek
Trout Creek Butte
Trout Creek Cow Camp
Trout Creek Recreation Site
Trout Creek Ranch (historical)
Trout Creek Reservoir
Trout Creek Ridge
Trout Creek Swamp
Trout Farm Recreation Site
Trout Meadow
Trout Meadows
Trout Meadows Butte
Trout Meadows Trail
Troutman Gulch
Truax Mountain
Tryon Creek
Tryon Creek Ranch
Tryon Saddle
Tsuga Lake
Tub Lake
Tub Spring
Tub Spring
Tub Spring
Tub Springs Reservoir
Tucca Creek
Tuck Reservoir
Tucker Creek
Tucker Creek
Tucker Flat
Tucker Gap
Tucker Hill
Tucker Spring
Tucker Spring
Tuckta Trail
Tudor Canyon
Tufti Creek
Tufti Mountain
Tule Lake
Tulley Creek
Tulley Creek Ranch
Tum Lake
Tumalo Butte
Tumalo Feed Canal
Tumalo Creek
Tumalo Dam
Tumalo Falls
South Fork Shelter
Tumalo Feed Canal
Tumalo Lake
Tumalo Mountain
Tumalo State Park
Tumalt Creek
Tumble Creek
Tumble Creek
Tumble Creek
Tumble Creek
Tumble Creek
Tumble Lake
Tumblebug Creek
Tumblebug Way
Tumbledown Creek
Tumbledown Creek
Tumbling Creek
Tumtum River
Tunnel Canyon
Tunnel Creek
Tunnel Creek
Tunnel Creek
Tunnel Creek
Tunnel Falls
Tunnel Number 1
Tunnel Spur
Tupper Butte
Tupper Creek
Tupper Guard Station
Tupper Meadow
Tupper Spring
Tureman Creek
Tureman Spring
Tureman Spring
Turner Basin
Turner Cabin
Turner Creek
Turner Creek
Turner Creek
Turner Creek
Turner Gulch
Turner Mountain
Turner Ranch
Turner Spring
Turpentine Creek
Turpin Ridge
Turpin Spring
Tussing Park
Tuttle Creek
Tututni Pass
Twelve Creek
Twelvemile Creek
Twelvemile Creek
Twelvemile Creek
Twelvemile Creek
Twelvemile Creek
Twentymile Creek
Twentynine Creek
Twin Basin
Twin Basin Creek
Twin Bridge Creek
Twin Bridges Campground (historical)
Twin Buttes
Twin Cabins Spring
Twin Canyon
Twin Coves
Twin Creek
Twin Creek
Twin Knobs
Twin Lake Creek
Twin Lakes
Twin Lakes
Twin Lakes
Twin Lakes
Twin Lakes Mountain
Twin Lakes Trail
Twin Lakes Trail
Twin Lick
Twin Meadows
Twin Meadows
Twin Meadows Trail
Twin Peaks
Twin Peaks
Twin Peaks Trail
Twin Pillars
Twin Ponds
Twin Ponds Camp
Twin Ponds Trail
Twin Rocks
Twin Rocks
Twin Sisters
Twin Spring
Twin Spring
Twin Spring
Twin Spring
Twin Spring Reservoir
Twin Springs
Twin Springs
Twin Springs
Twin Springs
Twin Springs Creek
Twin Springs Forest Camp
Twin Stoves Creek
Twin Tank Spring
Twin Trough Spring
Twin Buck Creek
Twinbuck Camp
Twincheria Creek
Twons
Twins Crane Prairie Trail
Two Bear Creek
Two Bit Fork
Two Cabin Creek
Two Color Creek
Two Color Lake
Two Corral Creek
Two Dot Spring
Two Spring
Two Spring Creek
Two Springs
Two-Bit Spring
Twobuck Creek
Twomile Canyon
Twomile Creek
Twomile Creek
Twomile Creek
Twomile Gap
Twomile Rapids
Tycer Creek
Tye Canyon
Tyee Butte
Tyee Creek
Tyee Creek
Tygh Creek
Tygh Creek Trail
Tyler Draw
Ukiah
Ukiah-Dale Forest State Park
Ulmer Mountain
Ulrich Ranch
Umapine Creek
Umatilla Brakes Viewpoint
Umatilla Creek
Umatilla Forks Recreation Site
Umbrella Falls
Umbrella Falls Trail
Umli
Umpqua Hot Springs
Umpqua Mine
Umpqua River
Umpqua Rogue Trail
Umpqua State Scenic Corridor
Uncle Creek
Uncle Sam Mine
Union Creek
Union Creek
Union High School (historical)
Knappa High School
Union Mine (historical)
Union Peak
Union Peak Trail
Union Spring
Unit Lake
Unity
Unity Cemetery
Unity Forest State Park
Unity Lake State Recreation Site
Unity Reservoir
Upper Bench
Upper Bennett Spring
Upper Bluff Spring
Upper Cache Creek Rapids
Upper Campground (historical)
Upper Chetco Charter School
Upper Chetco Trail
Upper Chewaucan Marsh
Upper Cougar Camp
Upper Crowsfoot Spring
Upper Cyrus Spring
Upper Eddeeleo Lake
Upper Erma Bell Lake
Upper Falls
Upper Farm
Upper First Creek Spring
Upper Hollenbeck Spring
Upper Hood River Valley
Upper Howard Camp
Upper Island Lake
Upper Jones Canyon Reservoir
Upper Keeney Spring
Upper Kirby Rapids
Upper Klamath Lake
Upper Klamath National Wildlife Refuge
Upper Lake
Upper Land Creek
Upper Long Meadow
Upper Marilyn Lake
Upper McKay School (historical)
Upper Mountain Meadows
Upper Mud Spring
Upper Olalla School (historical)
Upper Pine Ridge Spring
Upper Quinn Lake
Upper Ray Spring
Upper Reservoir
Upper Rigdon Lake
Upper Road Spring
Upper Salmon Lake
Upper Sandy Guard Station (historical)
Upper Snake River Trail
Upper Snowshoe Lake
Upper Soda
Upper Soda Falls
Upper Tumalo Reservoir
Upper Valley Cemetery
Upper West Fork Reservoir
Upper West Lateral
Upper Yachats School
Upset Creek
Utley Butte
Utley Creek
Utley Creek Trail
Valen Lake
Valley View Cabin
Valley View Mine
Valpey Butte
Van
Van Anda Mine
Van Aspen Creek
Van Cleve Creek
H B Van Duzer Forest State Scenic Corridor
Van Gulch
Van Gulch Spring
Van Zandt Meadows
Vanata Basin
Vanata Creek
Vance Creek
Vance Draw
Vance Draw
Vandevert Ranch
Vannoy Creek
Vanora (historical)
Vansycle Canyon
Varmint Creek
Varmint Creek
Vaughn Creek
Vawter Canyon
Vawter Spring
Veazie Creek
Veda Butte
Veda Lake
Vehrs Spring
Velvet Creek
Venator Creek
Venator Creek
Venus
Vera Lake
Verdun Rock
Verdun Way
Vernon School (historical)
Vernon Spring
Mount Vernon
Vester Creek
Vester Creek Meadows
Victor Gulch
Victor Mine
Victor Rock
Vidae Cliff
Vidae Ridge
Viento Creek
Viento Ridge
Viento State Park
View Lake
View Point
Villard Glacier
Vincent (historical)
Vincent Creek
Vincent Creek
Vincent Creek Guard Station (historical)
Vine Creek
Vine Maple Creek
Vinegar Creek
Vinegar Hill
Vingie Creek
Vinyard Cabin
Viola Canyon
Violet Hill
Vista Ridge
Vista Ridge Trail
Vogel Lake
Vol Spring
Volcano Trail
Volstead Reservoir
Vulcan Lake
Vulcan Peak
W B J Spring
WPA Reservoir
Lake Waban
Wakonda Beach
Wade Creek
Wade Ditch
Wade Gulch
Wade Pond
Wade Spring
Wagner Creek
Wagner Gap
Wagner Glade Gap
Wagner Gulch
Wagner Gulch Trail
Wagon Road Gulch
Wagon Trail Ranch
Wahanna Lake
Wahe Falls
Wahkeena Creek
Wahkeena Falls
Wahtum Lake
Waight Spring
Waite Creek
Wake Butte
Wakefield Cabin
Waldo
Waldo Glacier
Waldo Hill
Waldo Lake
Waldo Lake Trail
Waldo Meadows Guard Station
Waldo Mountain
Waldport
Central Coast Ranger Station
Walker Creek
Walker Creek
Walker Creek
Walker Creek
Walker Creek
Walker Creek
Walker Creek
Walker Creek
Walker Gulch
Walker Gulch
Walker Mountain
Walker Peak
Walker Peak Lookout (historical)
Walker Prairie
Walker Ranch
Walker Ridge
Walker Rim
Walker Rim Spring
Walker Spring
Walker Spring
Wall Creek
Wall Creek
Wall Creek
Wall Creek
Wall Creek
Wall Creek Ridge
Wall Creek Trail (historical)
Wall Lake
Walla Walla Recreation Site
Wallace Creek
Wallalute Falls
Wallow Creek
Wallow Spring
Wallowa
Wallowa Cemetery
Wallowa Creek
Wallowa Creek
Wallowa Lake
Wallowa Mountains
Wallowa River
Wallowa Valley Improvement Canal
Blue Gulch
Wallupa Creek
Walpole Creek
Walt Brown Gulch
Wamic
Wampus Butte
Wampus Springs
Wanderers Peak
Wanderers Peak Trail
Wanoga Butte
Wapinitia
Wapinitia Creek
Wapinitia Pass
Wapiti Camp
Wapiti Creek
War Canyon
Warble Creek
Ward Canyon
Ward Creek
Ward Lake
Ward Mine
Warden Creek
Wards Meadow
Warfield Creek
Warm Spring
Warm Spring Butte
Warm Spring Creek
Warm Springs Creek
Warm Spring Creek
Warm Springs
Warm Springs
Warm Springs Cabin
Warm Springs Creek
Warm Springs Meadow
Warm Springs Meadow Trail
Warm Springs Meadows
Warm Springs River
Warnock Corral
Warner Canyon
Warner Creek
Warner Creek
Warner Mountain
Warner Work Center
Warnock Gulch
Warren Creek
Warren Lake
Warren Tison Ranch
Warrendale
Warrens Creek
Warrior Creek
Wart Peak
Wasco Lake
Wash Creek
Wash Creek Butte
Washboard Ridge
Washboard Ridge
Washboard Trail
Washington Ponds
Washington School (historical)
Mount Washington
Washout Creek
Wassen Meadows
Wasson Canyon
Wastina Butte
Watchdog Butte
Water Canyon
Water Gap
Water Gap Creek
Water Gulch
Water Gulch
Water Holes Trail
Water Tank Spring
Water Tower Mountain
Water Trough Canyon
Waterbury Ditch
Waterbury Gulch
Waterbury Mill
Waterdog Creek
Waterdog Lake
Waterfall Creek
Waterhole
Waterhole Canyon
Waterhole Spring
Waterlog Gulch
Waterman Mine
Waters Creek
Waters Creek
Waters Creek Campground (historical)
Waters Gulch
Waterspout Creek
Waterspout Draw
Waterspout Gulch
Watkins Butte
Watkins Creek
Watkins Hollow
Watson Butte
Watson Cabin
Watson Creek
Watson Creek
Watson Creek
Watson Falls
Watson Gulch
Watson Mountain
Watts
Watts Mine
Waucoma Ridge
Waucup Creek
Wauna Point
Wauneka Point
Way Creek
Wayne Butte
Weasel Butte
Weasel Spring
Weaver Canyon
Weaver Creek
Weaver Creek
Weaver Creek
Weaver Mountain
Weaver Ranch (historical)
Webb Creek
Webb Gulch
Webb Slough
Weburg Spring
Wedderburn
Weddle Creek
Wee Lambie Spring
Weed Creek
Weed Spring
Weiss Ranch
Welch Butte
Welch Creek
Welch Creek Recreation Site
Welch Creek Mine
Welch Creek Trail
Welches
Welches Middle School
Welcome Creek
Welcome Lakes
Welcome Lakes Ridge Trail
Welcome Lakes Trail
Welker Creek
Welker Spring
Wells Creek
Wells Creek
Wells Spring
Welter Creek
Wemme
Wenaha Forks (historical)
Wenaha River
Wendson
Wesler Canyon
West Basin Canyon
West Basin Well
West Bay
West Bay Creek
West Bear Creek
West Beaver Creek
West Birch Creek
West Bologna Canyon
West Branch Bridge Creek
West Branch Cemetery
West Branch Elk Creek
West Branch Long John Creek
West Branch North Fork Smith River
West Branch Rock Creek
West Branch Willow Creek
West Buker Spring
West Burnt Log Spring
West Camp Creek
West Chicken Creek
West Coon Creek
West Creek
West Creek
West Creek
West Davis Lake Recreation Site
West Dry Creek
West Fisher Lake
West Fork Agency Creek
West Fork Applegate Creek
West Fork Ash Creek
West Fork Ashland Creek
West Fork Austin Creek
West Fork Basin Creek
West Fork Booneville Channel
West Fork Bridge Creek
West Fork Broady Creek
West Fork Buck Creek
West Fork Burnt River
West Fork Camp Creek
West Fork Carrol Creek
West Fork Clear Creek
West Fork Clear Creek
West Fork Cow Creek
West Fork Coyote Creek
West Fork Crazy Creek
West Fork Deadwood Creek
West Fork Deadwood Creek
West Fork Deep Creek
West Fork Deer Creek
West Fork Dismal Creek
West Fork Dismal Creek
West Fork Dry Creek
West Fork Dry Creek
West Fork Duck Creek
West Fork East Gulch
West Fork Evans Creek
West Fork Floras Creek
West Fork Fox Creek
West Fork Goose Creek
West Fork Grub Creek
West Fork Hay Creek
West Fork Hood River
Tamarack Creek
West Fork Howard Creek
West Fork Illinois River
West Fork Indian Creek
West Fork Indian Creek
West Fork Indigo Creek
West Fork Johnson Creek
West Fork Jones Creek
West Fork Junetta Creek
West Fork Lick Creek
West Fork Little Indian Creek
West Fork Meadow Brook
West Fork Mill Creek
West Fork Millicoma River
West Fork Mosby Creek
West Fork Mosier Creek
West Fork Muir Creek
West Fork Mule Creek
West Fork Neal Creek
West Fork Park Creek
West Fork Peavine Creek
West Fork Pine Creek
West Fork Pine Creek
West Fork Pine Creek
West Fork Prather Creek
West Fork Rancherie Creek
West Fork Reservoir
West Fork Ruby Creek
West Fork Salmon River
West Fork Salmon River
West Fork Scott Creek
West Fork Shoestring Creek
West Fork Silver Creek
West Fork Skimmerhorn Creek
West Fork Smith River
West Fork Snipe Creek
West Fork Sru Creek
West Fork Taylor Creek
West Fork Thomason Creek
West Fork Trail Creek
West Fork Trout Creek
West Fork Wallowa River
West Fork Warrens Creek
West Fork Wickiup Creek
West Fork Williams Creek
West Fork Wolf Creek
West Fork Wolf Creek
West Gopher Pond
West Gulch
West Hanks Lake
West Lake
West Lateral
West Lava Forest Camp (historical)
West Mountain
West Myrtle Butte
West Myrtle Creek
West Myrtle Spring
West Pass Creek Way
West Pinhead Butte
West Ranch
West Ridge
West Shotgun Spring
West Side Cemetery
West Ten Cent Creek
West Thornton Creek
West Willow Creek
West Willow Creek Reservoir
West Zigzag Lookout (historical)
West Zigzag Mountain Trail
Westland Middle School (historical)
Westfall Spring
Westfir
Westridge Middle School
Weston Lake
Weston Mountain
Weston Mountain
Weston Ridge
Wests Butte
Wests Mine
Westside Ditch
Westwood Creek
Wet Creek
Wet Creek
Wetmore (historical)
Wetmore Recreation Site
Weygandt Canyon
Whale Creek
Whale Head
Wharf Creek
What Creek
Wheeler Creek
Wheeler Creek
Wheeler Creek
Wheeler Creek
Wheeler Point
Wheeler Spring
Wheelock Creek
Whetstone Butte
Whetstone Mountain
Whig Lake
Whiskers Peak
Whiskey Creek
Whiskey Creek
Whiskey Creek
Whiskey Creek
Whiskey Creek
Whiskey Creek
Whiskey Flat
Whiskey Flat
Whiskey Gulch
Whiskey Jack Spring
Whiskey John Flat
Whiskey Lake
Whiskey Mountain
Whiskey Spring
Whiskey Spring
Whiskey Spring
Whisky Camp
Whisky Creek
Whisky Creek
Whisky Creek
Whisky Creek
Whisky Creek
Whisky Creek
Whisky Creek
Whisky Flat
Whisky Peak
Whisky Ridge
Whisky Spring
Whisky Spring
Whisky Spring
Whisky Spring
Whiskey Spring Recreation Site
Whisky Spring Trail
Whispering Pine Horse Camp
Whistle Spring
Whistler Point
Whitaker Holes
White Branch
White Bull Mountain
White Butte
White Butte
White Butte Creek
White Creek
White Creek
White Creek
White Creek
White Creek
White Creek
White Creek
White Fir Forest Camp
White Hill Creek
White Horse Ridge
White Horse Spring
White House Spring
White King Mine
White Mule Creek
White Pine Knob
White River
White River Glacier
White River Park Campground (historical)
White Rock
White Rock
White Rock
White Rock Creek
White Rock Creek
White Rock Mountain
White Rock Spring
White Rock Spring
White Rock Trail
White Spring
Whited Reservoir
Whiteface Peak
Whitefish Creek
Whitehead Creek
Whitehorse Bluff
Whitehorse Creek
Whitehorse Spring
Whitehouse Flat
Whitehorse Meadows
Whitehouse Place
Whiterock Creek
Whiterock Creek
Whitetail Butte
Whitetail Spring
Whitetail Spring
Whitewater (historical)
Whitewater Creek
Whitewater Glacier
Whitewater Lake
Whitewater River
Whiting Ranch
Whiting Spring
Whitman Creek
Whitman Creek
Whitman Rock
Whitman Spring
Whitmore Reservoir
Whitney (historical)
Whitney Creek
Whitney Meadow
Whitney Spring
Whittaker Creek
Whitten Prairie
Whoopee Creek
Wick Creek
Wickheiser Spring
Wickiser Slough
Wickiup Butte
Wickiup Butte
Wickiup Campground (historical)
Wickiup Creek
Wickiup Creek
Wickiup Creek
Wickiup Creek
Wickiup Creek
Wickiup Creek
Wickiup Dam
Wickiup Forest Camp (historical)
Wickiup Meadow
Wickiup Plain
Wickiup Plain Trail
Wickiup Shelter
Wickiup Spring
Wickiup Spring
Wickiup Spring
Wickiup Spring
Wickiup Spring
Wickiup Spring
Wickiup Trail
Wickiup Creek
Wicopee
Widow B Spring
Widow Creek
Widow Spring
Widows Creek
Wiggler Spring
Wigtop Butte
Wigwam Reservoir
Wigwam Spring
Wilbur Mountain
Wild Billy Lake
Wild Calf Canyon
Wild Canyon
Wild Horse Butte
Wild Horse Creek
Wild Sheep Creek
Wild Sheep Creek
Wild Woman Spring
Wildcat Basin
Wildcat Camp
Wildcat Creek
Wildcat Creek
Wildcat Creek
Wildcat Creek
Wildcat Creek
Wildcat Creek
Wildcat Creek
Wildcat Creek
Wildcat Creek
Wildcat Creek
Wildcat Creek
Wildcat Creek
Wildcat Gulch
Wildcat Gulch
Wildcat Ridge
Wildcat Spring
Wildcat Spring
Wildcat Swamp
Wildcat Trail
Wilder Spring
Wilderville
Wilderville School (historical)
Wildhorse Creek
Wildhorse Lookout
Wildhorse Meadow
Wildhorse Mountain
Wildhorse Prairie
Wildhorse Ridge
Wildhorse Ridge
Wildhorse Spring
Wildhorse Spring
Wildhorse Spring
Wildwood
Wiley Creek
Wiley Creek
Wyllie Creek
Wiley Flat Recreation Site
Wilhelm Creek
Wilkins Creek
Wilkins Creek
Wilkinson Creek
Will Rogers Spring
Willagillespie Elementary School
Willamette City
Willamette Divide Trail
Willamette City Park
Willamette Pass
Willanch Creek
Willanch Slough
Williams
Williams Creek
Williams Creek
Williams Creek Trail
Williams Ditch
Williams Field
Williams Lake
Williams Prairie
Williams Reservoir
Williams Spring
Williamson Creek
Williamson Recreation Site
Williamson Mountain
Williamson River
Williamson River Mission
Willis Creek
Willits Ridge
Willoughby Spring
Willow Butte
Willow Camp Spring
Willow Campground
Willow Creek
Willow Creek
Willow Creek
Willow Creek
Willow Creek
Willow Creek
Willow Creek
Willow Creek
Willow Creek
Willow Creek
Willow Creek
Willow Creek
Willow Creek Cabin
Willow Creek Recreation Site
Willow Creek Corral
Willow Creek Flats
Willow Creek Hills
Willow Creek Resort
Willow Flat
Willow Flat
Willow Flats
Willow Point
Willow Point
Willow Prairie
Willow Prairie Recreation Site
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring
Willow Spring Brook
Willow Spring Canyon
Willow Springs
Wilson Basin
Wilson Beach
Wilson Cabin
Wilson Cemetery
Wilson Cove Trail
Wilson Creek
Wilson Creek
Wilson Creek
Wilson Creek
Wilson Creek
Wilson Creek
Wilson Creek
Wilson Creek
Wilson Creek Driveway
Wilson Flats
Wilson Prairie
Wilson Prairie
Wilson Elementary School
Wilson Spring
Mount Wilson
Wilts Creek
Winant
Winberry
Winberry Creek
Winberry Mountain
Winburn Camp
Winchester Bay
Winchester Bay
Winchester Creek
Winchester Forest Camp (historical)
Winchester Lake
Winchester Point
Winchester Trail
Winchuck Recreation Site
Winchuck River
Wind Creek
Wind Creek
Wind Creek
Wind Creek
Wind Creek
Wind Creek Basin
Wind Creek Trail
Wind Lake
Wind Lake
Wind River
Wind Rock
Windfall Creek
Windfall Creek
Windfall Spring
Windigo Butte
Windigo Lakes
Windigo Pass
Windigo Way
Windlass Creek
Windy Camp Lookout
Windy Canyon
Windy Creek
Windy Creek
Windy Creek
Windy Creek
Windy Gap
Windy Gap
Windy Gap
Windy Hell Canyon
Windy Lakes
Windy Lakes Trail
Windy Mountain
Windy Pass Way
Windy Peak
Windy Point
Windy Point
Windy Ridge
Windy Ridge
Windy Spring
Wineburger Camp
Winegar Gulch
Winegar Spring
Wineglass
Wineland Canyon
Wineland Lake
Wing Butte
Wing Butte Cabin (historical)
Wing Creek
Wing Ridge
Wing Ridge
Wingdam Gulch
Winkle Bar
Winlock
Winom Butte
Winom Creek
Winom Meadows
Winopee Lake
Winopee Lake Trail
Winslow Cabin Spring
Winslow Creek
Winston Creek
Winter Butte
Winter Canyon
Winter Creek
Winter Ridge
Winters Creek
Wenner Creek
Winters Gulch
Winters Spring
Winterville Creek
Wire Corral Spring
Wire Meadow
Wise Creek
Wise Meadow
Wisehart Creek
Witham Creek
Witham Hill
Withers Creek
Withers Lake
Withrow Creek
Wits End
Wizard Creek
Wizard Falls
Wizard Island
Wizzard Lake
Woahink Creek
Woahink Lake
Wocus Bay
Wocus Butte
Wolf Butte
Wolf Camp Butte
Wolf Creek
Wolf Creek
Wolf Creek
Wolf Creek
Wolf Creek
Wolf Creek
Wolf Creek
Wolf Creek
Wolf Creek
Wolf Creek
Wolf Creek Recreation Site
Wolf Creek Job Corps Center
Wolf Creek Meadow
Wolf Gap
Wolf Gulch
Wolf Lake
Wolf Lake
Wolf Mountain
Wolf Mountain
Wolf Mountain
Wolf Mountain Trail
Wolf Peak
Wolf Peak
Wolf Prairie
Wolf Ridge
Wolf Ridge
Wolf Run Community Hall
Wolf Run Ditch
Wolf Shelter
Wolf Spring
Wolf Spring
Wolf Spring
Wolf Spring Trail
Wolfe Creek
Wolfer Creek
Wolff Ranch
Wolfinger Butte
Wolsey Creek
Wolverine Creek
Wonder
Wonder Creek
Wonder Spring
Wood Butte
Wood Camp Spring
Wood Creek
Wood Lake
Woodby Mountain
Woodchuck Spring
Woodcock Creek
Woodcock Mountain
Wooden Rock Creek
Shields Creek
Wooden Rock Guard Station
Wooden Trough Spring
Woodin Spring
Woodland Recreation Site
Woodmere Elementary School
Woodpecker Lake
Woodpecker Spring
Woodpecker Trail
Woodrat Mountain
Woodruff Bridge
Woodruff Creek
Woodruff Meadow
Woods
Woods Backbone
Woods Creek
Woods Creek
Lake in the Woods
Lake of the Woods
Woodward Creek
Woodward Creek
Wooley Creek
Woolly Horn Ridge
Worley Creek
Worley Spring
Worlow Creek
Wrangle Recreation Site
Wrangle Creek
Wrangle Gap
Wray Creek
Wray Mine
Wren Guard Station
Wrenn Dobbin Ditch
Wright Butte
Wright Creek
Wright Creek
Wright Spring
Wrightman Canyon
Wrights Meadows
Wrights Spring
Wuksi Butte
Wy'east Basin
Wyatt Creek
Wyeth
Wyeth Trail
Wygant State Natural Area
Wygant Trail
Wymer Creek
Wymer Flat
Wymer Glade
Wymer Meadow
XI Spring
Y Ridge
Ya Whee Plateau
Ya Whee Plateau Rim
Yachats
Yachats Grange
Yachats River
Yaden Creek
Yaden Flat
Yager Creek
Yainax Agency
Yainax Ridge
Yale Creek
Yamsay Guard Station
Yamsay Ranch
Yandall Spring
Yank Gulch
Yank Prairie
Yapoah Crater
Yapoah Lake
Yaquina
Yaquina Bay
Yaquina Bay State Recreation Site
Yaquina River
Yarn Spring
Yeager Creek
Yeager Mine
Yearling Spring
Yellow Creek
Yellow Jacket Glade
Yellow Jacket Point
Yellow Jacket Ridge
Yellow Jacket Spring
Yellow Jacket Spring
Yellow Jacket Spring
Yellow Pine Recreation Site
Yellow Rock
Yellow Rock
Yellowbottom Creek
Yellowjacket Creek
Yellowjacket Creek
Yellowjacket Creek
Yellowjacket Reservoir
Yellowjacket Ridge
Yellowjacket Spring
Yellowjacket Spring
Yellowjacket Spring
Yellowjacket Spring
Yellowjacket Trail
Yellowjacket Trail
Yellowstone Mine
Yeon Mountain
Yew Creek
Yew Creek
Yew Lane School (historical)
Yew Spring
Yew Wood Creek
Yew Wood Spring
Yocum Falls
Yocum Ridge
Yocum Valley
Yokum Corrals Camp
Yokum Reservoir
Yoncalla Creek
Yonna Ditch
Yonna Valley
Yoran Lake
Yoran Lake Trail
Mount Yoran
York and Rannels Mine
York Butte
York Creek
Yoss Creek
Yoss Creek Meadow
Young Creek
Young Creek
Young Gap
Young Ridge
Young Valley
Younger Spring
Youngs Butte
Youngs Creek
Youngs Creek
Younkers Ranch
Youtlkut Butte
Yoyo Spring
Yreka Creek
Yu-ma Spring
Yukon Creek
ZX Ranch
Zahn Creek
Zane Spring
Zeb Lake
Ziba Dimmick State Park (historical)
Zigzag
Zigzag Canyon
Zigzag Creek
Zigzag East Lookout (historical)
Zigzag Glacier
Zigzag Mountain
Zigzag River
Zigzag River Campground (historical)
Zigzag Spring
Zigzag Trail
Zimmerman Burn
Zims Point
Zinc Creek
Zion Scope
Zowie Lake
Zumwalt
Zumwalt School
Zwagg Island
ZX Brattain Ditch
ZX Ranch
ZX Ranch Red House
Blue Mountain Ditch
Morse Gulch
Laycock Long Ditch
Enterprise Ditch
Panama Ditch
Hodson Creek
Big Gulch
Kottmeier Reservoir
Painters Gulch
Spring Gulch
Corrigal Spring
West Fork Pine Creek
Tackle Gulch
Baldy Gulch
Stoddard Reservoir
Eagle Creek Canyon
Rattlesnake Creek
East Fork Goose Creek
Wood Creek
Copper (historical)
Shell Creek
Timothy Spring
Hale Creek
Hidden Recreation Site
Evergreen Recreation Site
Ollokot Recreation Site
Eureka (historical)
Willow Spring
Dark Canyon Creek
Glover (historical)
Robbs Creek
Eustis (historical)
Indian Valley (historical)
Merritt Reservoir
Cabin Creek (historical)
Howardville (historical)
Hendersons Pond
Grossman (historical)
Red Fir Spring
Hollow Log Spring
Dougherty Spring
Coyote Spring
Hinton Spring
Mayville Spring
Hunter Canyon
Waite Creek
Wrights Reservoirs
York Reservoir
Fleets Loop Reservoir
Outhouse Creek
Shaw Creek
Maxwell Basin
Hacker Creek
Lanman Creek
Hidden Branch
Hidaway Spring
West Fork Pine Creek
Spring Creek
Arnoldus Loop Reservoir
Waller Reservoir 5
Hartshorn Butte
Imnaha Cemetery
Magpie Creek
Hutton Gulch Rapids
Slaughter Gulch Rapids
West Fork Somer Creek
Hangover Creek
Wallowa Ponds
Enterprise Cemetery
Alder Slope Cemetery
Mill Creek
Point Joseph
Hurricane Rapids
Hurricane Point
Spring Creek
Spring Creek
Wades Point
Still Creek
French Creek
Granite Meadow
Lapover Lake
Twobuck Creek
Swamp Creek
Standley Creek
West Fork Prairie Creek
Bug Creek
Rock Bar
Granite Rapids
Two Bars
Sacajawea Recreation Site
Pony Bar
Neil Creek
Double Hitch Spring
Boneyard Creek
Armin (historical)
Thorn Creek
Monument Cemetery
Pole Creek
Gander Creek
Bingville Creek
Spring Creek
Everett Creek
Stussi Creek
Smokers Canyon
Slip Up Creek
Number One Spring
Stewart Creek
Fish Creek
East Creek
Scott Creek
Merrill Creek
West Fork Cochran Creek
Sweek Canyon
Merrill Canyon
Beck Creek
McHaley Creek
Kingsley Creek
Dipping Vat Creek
Burton Creek
Winlock Cemetery
Cochran Creek
Long Point
Happy Jack Ridge
Bull Prairie Lake
Balm Creek
Stalling Butte Spring
Bull Prairie Spring
Ives Creek
East Fork of North Fork Desolation Creek
West Fork of North Fork Desolation Creek
Dry Gulch
Cabin Creek
Pole Creek
Lick Creek
Charlie Creek
Steep Creek
Cold Spring
Galena Cemetery
Chattanooga Mountain
Gem Meadow
Gem Mine
Windy Point
Eagle Creek
Coxie Creek
Little Trail Creek
Cold Spring
Fir Spring
Huckleberry Spring
Cline Draw
Izee Cemetery
Cottonwood Draw
Chappel Gulch
Slide Falls
Strawberry Spring
Wildcat Spring
Warm Springs Branch
Dickerson Ranch Cemetery
Little Basin Creek
Litch Meadow
Comer (historical)
Morris Basin
Morris Creek
Southworth Ditch
Owens Ditch
Dry Soda Lookout
Macy Meadow
Rock Creek
Onion Gulch Meadow
Portland Mine
Ella Gulch
Buck Gulch
Cougar Ridge
Wickiup Creek
Long Tom Gulch
Honeymoon Canyon
Bennett Creek
Squatter Flat
Corner Creek
Psyche Butte
Poker Creek
East Fork Granite Boulder Creek
West Fork Granite Boulder Creek
Hunter Meadow
Shumway Meadow
Reynolds Meadow
Pizer Meadow
Snake Creek
Shaw Creek
Fox Valley Cemetery
High Bar
Little Bar
Little Bar Rapids
Hominy Creek Rapids
Salt Creek Rapids
China Bar Rapids
East Branch Gordon Creek
Rocky Point
No-Name Rapids
Wild Sheep Rapids
Sluice Creek Rapids
Rush Creek Rapids
Eagle Nest Rapids
Needham Pond
The Saddle
Gowing Spring
Gates Pond
Miner Spring
Huckleberry Spring
Mud Spring
Starr Reservoir
Mint Spring
Goat Mountain Spring
Minam Falls
Sunny Slope Springs
Minnie Boohoo Creek
Olallie Butte Guard Station
Gatch Falls
Baker Lake
Upper Falls Deschutes River
Harper Cemetery
Harper (historical)
Breese Cemetery
Lindh Lake
Masten Cemetery
W R Lateral
W A Lateral
Walker Basin Canal
Log Cabin (historical)
Mayfield Ditch
Basin Cove
Hoey Point
South Dagus Reservoir
Drift Creek
Juniper Reservoir
Wizzard Falls Spring
Hubbards Draw
Seekseequa Spring
Big Sheep Basin
Lostine Dam
Sheep Ridge Dam
Lostine Reservoir
Benham Creek
Pine Haven Cemetery
Eagle Valley Cemetery
Swedes Landing (historical)
Magone Lake Recreation Site
Howell (historical)
Twin Buttes
Sky Lake
Lost Lake
Wolf Creek Reservoir
Bearwallow Gulch
Dry Barnard Creek
Foothill Ditch
Motley Reservoir
McKinnon Creek
Fall Creek
Coin Creek
Skookum Chuck Creek
Turnbull Creek
Mormon Spring
Englishman Hill
Somers Creek Rapids
Lookout Creek Rapids
Maxwell Pond
Skylight Canyon
Arnoldus Pond
Jarvis Ponds
Feik Reservoirs
Eagle Spring
Galloway Meadows
Lady Spring
Joso Meadow
Warnock Spring
Lodgepole Spring
Tin Can Spring
Sheepherder Spring
Deer Spring
Lookout Mountain Spring
Grove Meadow
Indian Point
Driveway Spring
Baker Spring
Yankee Bar
Yankee Bar Rapids
Muir Rapids
Coverdale Spring
Spruce Spring
Smith Ditch
Reed Ditch
Sisters Reservoir
Beaver Creek Cemetery
Maxwell Ditch
Little Crater Creek
Bend Feed Canal
Gist
Whychus Creek Rim
Potter Canyon
Carcass Canyon
Whychus Creek Canyon
Trahan Canyon
Crow Foot Springs
Joe Fisher Reservoir
Grizzly Cemetery
Grizzly Mountain Canyon
Ochoco Distribution Canal
Putnam Gulch
Juniper Creek
Burn Creek
Yancey Reservoir
Smith Ditch
Barney
Riley Creek
Pine Hollow
Dry Creek
Kelly Lateral
Rice Creek
Wapinitia Cemetery
Red Lake Cemetery
Wapinitia Canal
Gray Butte Creek
Cyrus Hill
Adams Spring
Lillie Flat
Flag Flat
Wiley Flat
Knox Cemetery
Reams Reservoir
Telephone Flat
Peterson Reservoir
Frank Reservoir
Spring Creek
Horse Heaven Reservoir
Fisher Spring
Cougar Rock
Gerow Spring
Howard Cemetery
Scissorsville
Chuckwagon Spring
Hickeyville
Elk Creek
Cold Spring Creek
Crane Prairie Dam
Billy Quinn Grave
Cottonwood Springs
Elk Lake Springs
John Brown Canyon
Willow Creek Canyon
Jefferson Plywood Company Mill Pond
Washburn Spring
Graveyard Butte Cemetery
Miller Reservoir
Rock Creek Ditch
Wamic Elementary School (historical)
Wamic Cemetery
Pine Hollow Reservoir
Cody Ponds
Hill Bench
Box Canyon
Sunset Cove
Johnston Creek
Haystack Draw
Big Canyon Rim
Mud Springs Valley
Howard
Mill Creek Cemetery
Juniper Haven Cemetery
Barnes Butte Reservoir
Smarts Reservoir
North Fork Gate Creek
Taylorville (historical)
Shell Rock (historical)
Lindsey (historical)
Alder Creek
Aubert Reservoir
English Spring
Lone Pine Spring
Parkdale Cold Spring
Poplar Spring
Trout Creek
Flume Creek
Hannum Spring
Glacier Ditch
Gibson Spring
Fall Creek
Elk Bed Springs
Ditch Creek
Clinger Campground (historical)
Brooks Meadow Guard Station (historical)
Wahtum Lake Recreation Site
Simmons Creek
Shingle Creek
Searra Casa Reservoir
Savage Springs
Japanese Springs
Ice Fountain Spring
Dee Flat Guard Station
Dago Spring
Crystal Springs
Summit Spring
Bruner Spring
Cold Springs
Cemetery Creek
Wasp Reservoir
Paulina Spring
Mainline Reservoir Number 3
Mainline Reservoir Number 2
Mainline Reservoir Number 1
Mount Hood Canal
Cedar Branch
Capron Spring
Warren Creek Falls
Parker Springs
Davis Gulch
South Fork Campground
Buck Creek Group Camp
Tie Creek
Sloan (historical)
Porter (historical)
Lost Lake Ranger Station
Sparks Spring
Shinners English Spring
Routson County Park
Roaring Camp Spring
Green Apple Creek
Tanks (historical)
Stone Hill Reservoir
South Fork Camp
Conway (historical)
Meacham Cemetery
Rowley Cabin Spring
Lazinka School (historical)
Nelson Meadows
West Butte Reservoir
Upper Rock Quarry Canyon Reservoir
Virginia Creek
Stark Spring
Horton Canyon
Black Stump Gulch
Lost Valley Cemetery
Wildhorse Falls Reservoir
Sherar Springs Creek
Friend Cemetery
East Spring
Cascade Spring
Moody Spring
Moody Creek
Government Spring
Cascade Locks Cemetery
Summit Meadows Cemetery
Minott Spring
Little Herman Creek
Sky Ranch Reservoir Number Three
Balm Fork School (historical)
Blakes Pond
Cutsforth Pond
Burns Reservoir
Wastina (historical)
Rock Point
Beaver Marsh Guard Station
Mazama Junction
Sulphur Spring
Wright (historical)
China Gulch
Kinworthy Reservoir
Bingham (historical)
Camp Meeting Creek
Hunter-Best Reservoirs
Wertz Spring
Alder Brook
Kirkland Spring
Hells Canyon Dam
Horse Gulch
Midget Creek
Dead Point Spring
Sand Canyon
Dry Mountain Reservoir
Little Cheney Creek
Welches Creek
Tawney (historical)
Katy Creek
Lymp Creek
Robinhood Recreation Site
Nottingham Campground
Mine Creek
Lunch Creek
Wolf Run
Tamarack Creek
Spring Gulch
Marvel Reservoir
Liechti Pond Number One
Kelly Cistern
Knebal Spring Recreation Site
Glade Spring
Birdseye Spring
Bascom Spring
Springer Ridge
Denest Spring
Bird Spring
Royce Creek
West Fork Yoncalla Creek
Hidout Reservoir
Garrison Reservoir
Nenamusa Falls
Wilson Creek
Springer Creek
Kennedy Creek
Lodgepole Spring
Crystal Lake Masonic Cemetery
Buttermilk Creek
Antelope Creek
Colorado Mine
Fugowee Creek
Hotel Spring
Puddin Creek
Judson Rock Creek
Bohemia Creek
Bohemia (historical)
Glenwood (historical)
Bohemia Saddle
Champion (historical)
Helena Saddle
Crystal Basin
Utopian Saddle
Mattox Creek
Sharps Prairie
Staples Creek
Sharps Creek Recreation Area
Wee Creek
Spring Brook
Red Bridge (historical)
Wildwood
Star (historical)
Shockley Reservoir
Minette Creek
Arrowhead Saddle
Steampot Saddle
Deetee Creek
Doodle Creek
Murray Reservoir
Cabin Creek
Coon Creek
Disgust Creek
Timber Creek
Murphy Creek
Hyde Creek
Station Creek
Indian Creek
Timber Butte
Horsehead Creek
Kalitan Creek
Salt Springs
Mill Creek
Elephant Rock
Williams Lake
Billy Lake
Edna Lake
North Torrey Lake
Cervus Lake
Mickey Lake
Brittany Lake
Conim Lake
Ernie Lake
Alice Creek
Moolack Flat
Wapiti Creek
Chucksney Creek
Bull Creek
East Quinn Lake
Small Creek
Cloverpatch Creek
Channel Creek
Rooster Creek
Strait Creek
Moose Creek Falls
Mount Canary Company Log Pond
Pier Point Spring
Acme
Elbow Lake Creek
Crown Z Lake
Lost Lake
Perkins Lake
Miller Creek
Little North Woahink Lake
Dismal Swamp
Buck Creek
Bombard Bay
Bedolf Arm
Cherry Arm
Cleves Cove
Bear Lake
Five Mile Arm
Deer Arm
Big Arm
North Arm
Booth Arm
Glenada Ponds
Flint Creek
Skunk Creek
Saubert Creek
Deer Creek
Cox Creek
Prosser Slough
Shulte Creek
Independent Order of Odd Fellows Cemeteries
Booth Ridge
Middle Point
Isthmus Point
Spring Point
Fall Creek
Martin Eddy
Martin Eddy Creek
Townsend Creek
Skalada Creek
Strome County Park
Foster Creek
Grave Creek
Misac Creek
Dry Creek
Stewart Creek
Jack Morgan County Park
Fingerboard Slough Creek
Black Creek
Cape Kiwanda State Natural Area
Tucker Spring
Ray Creek
Queens Creek
Bob Straub State Park
Upton Slough
Woods County Park
Bower Creek
Jensen Springs
Morgan Spring
Little Nestucca County Park
Sutton Creek
Kiwanda Creek
Neskowin Beach
Little Nestucca Camp (historical)
Fox Creek
Muscott Creek
Woods IOOF Cemetery
Oretown Cemetery
Union Cemetery
Chitwood Falls
Curl Creek
McMillin Creek
North Fork Panther Creek
Morton Creek
Panther Creek
Baxter Creek
Logan Creek
Roads End State Recreation Site
Deer Creek Lake
Rock Creek
Hebo Lake Recreation Site
Castle Rock Recreation Site
Castle Rock
Spring Creek
Sand Creek
Knight Reservoir
North Fork Reservoir
Miller Creek
Wren Cemetery
Larson Log Pond
Pheasant (historical)
Clemens Log Pond
Peak Log Pond
South Lake Recreation Site
Mount Hebo Recreation Site (historical)
Koch Creek
Duck Bay
Harmony Bay
Lagoon Recreation Site
Joaquin Miller State Park
Cherry Point
Home Point
Snare Point
Clay Point
Lone Tree Point
Weed Island
Burnt Point
Halfway Point
Crabtree Point
Georgia Lake
Rocky Point
Ada County Park
McAllister Creek
Swampy Creek
Little Creek
Telephone Creek
Mink Creek
Knight County Park
Ervin Creek
Spencer Creek
Powell Cemetery
Mercer Creek
Moss Creek
Moore Creek
Esmond Creek Recreation Area
Whittaker Creek Recreation Site
Sutherland Creek
Pucker Creek
Linslaw County Park
Jasper Creek
Box (historical)
Lobster Valley
Missouri Bend Recreation Site
Missouri Bend
Buck Creek Ridge
Elk Creek
Preston Creek
Wilcut Creek
Little Beech Creek
Dry Creek
Camp Lane County Park
North Fork Panther Creek
Bear Creek
Five Rivers Lookout (historical)
Indian Creek Cemetery
Independent Order of Odd Fellows - Mapleton Lodge 3139 Cemetery
Farnham Landing
Euclid (historical)
Crooked Creek
Paris
Klickitat Spring
Table Mountain Creek
Phillips Creek
Tidewater Cemetery
Barclay Meadows
Little Switzerland
Little Albany
Alsea Rivera
Line Creek
Hellion Ridge
Slide Campground (historical)
Smallwood Creek
Rock Creek
Meander Along Creek
Blackberry Recreation Site
Denzer (historical)
Five Rivers County Park
Cascade Falls
Canal Creek Recreation Site
Upper Yachats
Keller Creek Recreation Site
Hinton Slough
Mill Creek Reservoir
Babcock Creek
Chetco Slough
Needle Branch
Blair Creek
Elk City County Park
Glen (historical)
Errol Ridge
Palmer Mountain
Glenwood Cemetery
Sunnyridge
Park Creek
Plowman Creek
Snell Creek
Lichtenthaler Spring
Count Creek
Woosley Creek
Slide Creek
Wilson Creek
Camp Creek
Tide Wayside
Central Coast Ranger District-Florence Office
Whiskey Creek
Horseshoe Creek
Olsen Creek
Betzen (historical)
Boyle Creek
Saddle Mountain Springs
Deadwood Cemetery
Erskine Log Pond
Martin Creek
Brickerville
North Fork Siuslaw Recreation Site
Jim Dick Creek
Misery Ridge
Scoville Spring
Narrow Creek
Fall Creek Falls
Stiltner Creek
Mason Creek
Slate Creek
Alsea Mountain Roadside Rest Area
Little Alder Creek
Yew Wood Camp (historical)
Roberts Creek
Cathcart Creek
Cathcart Springs
Kiger Creek
Ryder Creek
Hayden Creek
Headrick Creek
Cedar Creek
Gygi and Engle Reservoir
Banton Creek
Brown Creek
Blackberry Creek
Minto Dam
Darling Creek
Big Twelve Creek
Niagara Creek
Lodore Creek
McCulloch Cemetery
Side Camp (historical)
McMullen Creek
Euchre Falls
Moonshine County Park
Baker Creek
Werner Camp (historical)
Southman Creek
Tarry Creek
Callow Creek
Martha Creek
Horse Creek
Alsea Cemetery
Doe Mountain
Conger (historical)
Clark Creek
Blodgett Cemetery
Thompson Lake
Peak (historical)
Marys Peak Recreation Site
Smittie Ridge
Horseshoe Bend
Fisher Creek
Robinson Ridge
Wasson Ridge
Lower Smith River Cemetery
Buzzards Butte
Sulphur Ridge
Smith River Recreation Site (historical)
Buckwheat Creek
Earl (historical)
Earl Creek
Sunrise Ranger Station
Blackwell Creek
The Horn
Schooner Creek Campground (historical)
Oceanlake Dam
North Creek Campground (historical)
Abrams Creek
Reed Reservoir
Bones Creek
Bear Creek
Wildcat Creek
Summit Spring
Henrys Reservoir
Huddleston Reservoir
Bowman Spring
Goff Spring
Baker Creek
Spring Creek
Sparta Spring (historical)
Roudoth Spring
Sheep Creek Hill Summit
Thomason Meadow Guard Station
Veats Draw
Bens Creek
Mining Channel
Hooker Flat
Rainbow Rock
Baldwin Ditch
Walden
Powell Hot Springs
Dixie (historical)
Box Spring
Lawton (historical)
Herburger Pond
Lemons Ditch
Eddington Ditch
O'Keefe Reservoir Number Four
O'Keefe Reservoir Number Six
O'Keefe Reservoir
Lane Waterhole Number Eleven
Lane Waterhole Number Twelve
Lane Reservoir Number Four
O'Keefe Meadow
Willow Creek Guard Station
Lane Reservoir Number One
Wakefield Reservoir
Tule Swamp
Duke Creek
Church Creek
Thomas (historical)
Wendell (historical)
Hot Springs (historical)
Roaring Spring
Big Spring
Warner Canyon Ski Area
Ski Lodge Spring
Hammersley Creek Reservoir
Gussie Creek
Coral Creek Reef
Upper Pittsburg Rapids
Alum Bed Rapids
Kings Hole Reservoir
Dutch Point
Big Minam Guard Station
Baldwin Ditch
Goose Swale
Gray Lateral
Farleighs Reservoir
New Idaho
Heckman Reservoir Number Two
Moss Ditch
Lower Marsh Canal
Game Reservoir
Deboy Reservoir
Dog Lake Spring
Renner Reservoir
Stover Reservoir
Clyde Fenimore Reservoir
Stevenson Creek
Drews Valley (historical)
Lucky Six Spring
Snake Spring
South Fork Bridge Creek
Connor Creek Reservoir
Throop Ditch
Ringsmeyer Ditch
Cummings Ditch
Murray Ditch
Waller Reservoir Number Four
Neal Dam
Big Bend
Newtons (historical)
Little Phipps Creek
Haystack Valley
Notch Prairie
Ledgerwood (historical)
Hell Fire Flat
Emergency Point
Porcupine Spring
Morrow Meadow
Jonas Flat
Beymer Flat
Caverhill (historical)
Farrow Creek
Woodward Reservoir Number Two
Woodward Reservoir Number One
Summer Lake Hot Springs
Gibson Hot Spring
Blue Lake
Conn Ditch
Chewaucan (historical)
Paisley Flat
Admans Mill Pond
Indian Spring
Hammersley Creek
Pine Ridge
Hines Log Pond
Greenhorn Mountains
Sunshine Springs
Malcolm Ridge
Linville (historical)
Chitwood Creek
Patterson Creek
Blue Jay Creek
Alder Swamp
Granite Mountain (historical)
Cold Creek
Bryant City (historical)
Edison Gulch
Red Heifer Mountain
Silver Creek
West Fork McQuade Creek
Sturdivant Cemetery
Leverenz Reservoir
Dry Lake
Community Reseeding Waterhole
Juniper Basin Spring
Powell Valley
Wildhorse Reservoir
Holding Pasture
Basin Creek
Clover Creek
Lewis Ditch
Hudspeth Mill (historical)
Parkersville (historical)
White Pine (historical)
Ukiah School
Badger Creek
Wildcat Creek
Long Prairie Reservoir
Flowers Dam
Pine Creek
Chapin Guard Station
Cold Spring
Hogwallow Spring
Foster Reservoir
Little Ross Reservoir
Dead Indian Spring
Foster Spring
Summer Lake I D Canal
Foster Reservoirs
Bullgate Dike
Windy Waterhole
Dudley Waterhole
O'Keefe Waterhole
Winkle Flat Reservoir
Two Sheep Waterhole
Dry Creek Waterhole
Rocky Waterhole
Weaver Waterhole
Egli Rim Reservoir Number One
Egli Rim Reservoir Number Two
Silver L Canal
Hagerhorst Mountains
Lost Lake
Grohs Reservoir
Beaver Marsh
Murphy Spring
Wakefield (historical)
Wakonda Beach State Airport
Inshallah International Airport
Winkle Bar Airport
Wonder Airport
Wulff Airstrip (historical)
KTMT-FM
KURY-FM
KXIQ-FM
KCRF-FM
KFMJ-FM
KICR-FM
KMTB-FM
KOOS-FM
Logger Waterhole
Williams Mill (historical)
Burn Waterhole
Staked Waterhole
Basalt Reservoir
South Spring Reservoir
Ted Reservoir
Bridge Creek Waterhole
Hagadorn Waterhole
Blow Waterhole
Rocky Waterhole
Airstrip Reservoir
KQIK-AM
KURY-AM
KJDY-AM
KTVL-TV
KTVZ-TV
KAJO-AM
KBBR-AM
KBCH-AM
KDOV-AM
Camp Creek Dam
Bennett Dam
H S Johnson Reservoir
H S Johnson Dam
Whited Dam
Morfitt Dam
Lyle Dam
Saw Mill Gulch Dam
Bolan Lake Dam
Long Creek Dam
Fish Lake Dam
Fourmile Lake Dam
Drews Dam
Scheckels Dam
Scheckels Reservoir (historical)
Murray Dam
Poer Dam
Ochoco Dam
Swamp Creek Dam
Nootnagle Reservoir
Nootnagle Dam
Reeder Gulch Dam
Dailey Dam
Munn Dam
Dick Dam
Dick Reservoir
Pine Creek Dam
Pringle Flat Reservoir
Mud Spring
Swede Spring
Minam Lake Dam
Eagle Lake Dam
Lookingglass Lake Dam
KIVR-AM
South Arm Dam
Devaul Dam
Thompson Valley Diversion Dam
Gardener Dam
Pierce Dam
Badger Lake Dam
Rock Creek Dam
Circle W Ranch-Condon Airstrip (historical)
Madras Municipal Airport
Compressor Station Number 11 Airstrip (historical)
Crescent Lake State Airport
D M Stevenson Ranch Airport
Hickey Dam
Cottonwood Spring Reservoir
Stewart Ditch
Anderson Airfield (historical)
Ashland Municipal Airport-Sumner Parker Field
Backachers Ranch Airport
Barkers Field (historical)
Beach Ranch Airport
Brookings Airport
Cascade Locks State Airport
Blue Lick Creek
Chitlam Creek
Mud Puppy Lake
Fawn Creek
Tamarack Spring Campground (historical)
Alder Spring
Sheep Spring
Cavin Swamp
Cavin Ditch
Cook Ditch
Colt Ware Ditch
Sagebrush Gulch
Warm Spring
Tiger Ditch
Wham Whited Ditch
Haskins Gulch
Curop Ditch
Audrey (historical)
High Line Ditch
Thompson Ditch
Hanby Reservoir
Bay Area Hospital Heliport
Idanha Log Pond
Cold Spring Reservoir
Madill Creek
Osburn Reservoir
Osburn Dam
Wahkeena Rearing Lake
Bull Run Dam Number 1
Bull Run Dam Number 2
Timber Lake
Acme Timber Company Mill Dam
Skookum Lake Dam
Lake Roslyn Dam (historical)
Frog Lake Dam
Mercer Dam
Mill Creek Dam
Ollala Lake
Good Samaritan Hospital Heliport
Gopher Gulch Airport (historical)
Kuhn Landing Strip (historical)
Lake Billy Chinook State Airport
Lake County Airport
Lakeside Municipal Airport
Lord Flat Airport
Mc Kinnon Airpark
Memaloose Airport
Menasha Pad
Meuret Airstrip (historical)
Monument Municipal Airport
Newport Municipal Airport
Southwest Oregon Regional Airport
Samaritan North Lincoln Hospital Heliport
Hanel Field
Hendershots Airstrip (historical)
Inland Helicopters Heliport
Round Butte Heliport
Grant County Regional Airport/Ogilvie Field
Joseph State Airport
Josephine Memorial Hospital Emergency Heliport
Oakridge State Airport
Lehman Field
Oxbow Ranch Airport
Pacific City State Airport
Paisley Airport
Pineridge Ranch Airport
Powers Airport
Powwatka Ridge Airport
Prospect State Airport
Sandy River Airport
Riverview Ranch Airport
Roseburg Lumber Chip Facility Airstrip (historical)
Roseburg Lumber Company Airstrip (historical)
Sawalish Airstrip (historical)
Silver Lake Forest Service Strip
Sisters Eagle Air
Skirvin Air Park (historical)
Saint Charles Medical Center Heliport
Sunnyhill Airport
Sunriver Airport
Tillamook Airport
Tillamook General Hospital Heliport
Toketee State Airport
Toledo State Airport
Miranda's Skyranch Airport
Ellingson Lumber Company Airstrip (historical)
Enterprise Municipal Airport
Florence Municipal Airport
Flying T Ranch Airport
Garvins Airfield (historical)
Gold Beach Municipal Airport
Black Pasture
Coyote Spring
Rimrock Spring
Rim Spring
Bohna (historical)
Sperry (historical)
Boney Spring Number 2
Boney Spring Number 1
Perry Spring
Howard Creek
Stanbro Reservoir
Dalton Springs
Trout Farm Spring
Little Meadows
French Lane (historical)
Horse Spring
Camp Logan (historical)
Prairie City Bench
Snow Creek
Faiman Spring
Walden Springs
Prairie City Reservoir
Bradley Creek
Parkers (historical)
Carroll (historical)
Gimlet (historical)
Whitney Valley
Larch (historical)
South Fork Camp Creek Campground
Shadow Lake
Lemolo Lake Resort
Opal Lake Recreation Site
Bunker Hill Recreation Site
Linda Lake
Inlet Recreation Site
East Lemolo Recreation Site
Poole Creek Recreation Site
Crystal Creek
Rockpile Lake
Spruce Lake
Sunrise Lake
Sunset Lake
Neet Lake
Fir Lake
Tranquil Cove
Tandy Bay
Greenwood Point
Dreadnought Island
Darlene Lake
Suzanne Lake
Eagle Creek Forest Camp
Mount Howard Gondola Lift
Mud Spring Camp (historical)
Paddock Camp
Sapphire Lake
Cupit Mary Meadow
Emerald Lake
King Lake
Kinglet Lake
Spirit Lake
Zircon Lake
Ray Creek
Birthday Lake
Full Creek
Gold Lake Bog
Verde Lake
Rhododendron Island
Photo Lake
Lower Betty Lake
Bongo Lake
Cardiac Lake
Fig Lake
Last Lake
Sump Lake
Trio Lake Number 3
Trio Lake Number 2
Trio Lake Number 1
McLeod Creek
Construction Creek
Bills Creek
Bechel Creek
Doe Creek
Last Creek
Lopez Lake
Vivian Lake
Cascade Creek
Bect Creek
West Lava Creek
Indian Hole Falls
Mesa Springs
Camp Lake
Yocum (historical)
Alkali Spring
Potts Field
Dry Gulch
Crane Flat
East Willow Creek
Brush Canyon
Sandy Flat
Loperfido Spring
Beaver Reservoir
Burnt Basin
Harney Cemetery
Armstrong Canyon
Robertson Draw
Middle Fork Rattlesnake Creek
Mystery Spring
Merit Meadows Spring
Frazier Spring
Grindstone Reservoir
Engineers Springs (historical)
Hawk Spring (historical)
Tamarack Spring
J M Ranch
Whistle Creek
Button Flat
Mill Spring
Pigeon Spring
Spring Creek
H V I Company Ditch
Danforth Ditch
Cow Creek Valley
Davis Gulch
Mortimer Canyon Reservoir
Armstrong Canyon Reservoir
Silvies Canyon
Heifer Canyon
Chappel Gulch Reservoir
Wickiser Spring
Phillips Spring
Pewee Creek Reservoir
Blue Creek Spring
Mud Spring
Rickman Reservoir
Officers Reservoir
Yellowjacket Lake
Doorbell Spring
Alder Creek
Spring Creek Spring
Lost Dog Flat
Sunshine Spring
Altnow Ditch
Landing Creek Spring
Red Lick Spring
Baker Spring
Pheasant Spring
Slickear Creek
Varien Canyon
Finke Draw
Little Sage Hen Spring
Gravel Ridge
Spring Draw
Hunter Camp Seep
Mahogany Ridge
Hixon Brandon Spring
Old Road Camp Spring
Ice Creek
Fern Spring
Tipton Spring
Hopper Spring
Short Spring
Willow Spring
Seneca Well
Rex Reservoir
Bull Run Reservoir
Bull Run Spring
Shields Spring
Big Glade Spring
Hagney Spring
Roach Creek Spring
Rock Spring
RIL Spring
Log Pipe Spring
Crow Flat
Buffalo Lake
West Side Ditch
Ennis Riffle
Flanagan Mine
Grotto Falls
Indianhead Rock
Judson Creek
Lake Spring
Lathrop Glacier
Little Crater Lake
Little Niagara Falls
Elliott Well
Gibbons Mill Canyon
Hells Canyon Rapids
Hodge Crest
Mount Howard
Jefferson Park
Landax (historical)
Leuthold Couloir
Gnarl Ridge
Annie Falls
Antelope Flat Reservoir
Benson Glacier
Bedrock Riffle
Blossom Bar Rapids
Broken Hand
Bullpup Lake
Campbell Creek
Castle Rock
Clay Hill Rapids
Committee Creek
Latgawa Mountain
Dead Horse Creek
Duwee Falls
Blue Mountains
Butter Creek
Bull Run Lake
Coalman Glacier
Port of Brookings Harbor
Brushy Chutes
China Bar Rapids
Chair Riffle
Craigie Point
Crescent Lake
Dodge Island
Devils Stairs
Drake Dune
Double Corral Creek
Dorothy Creek
Dunn Riffle
Merriam Point
Middle Fork Copeland Creek
Mule Creek Canyon
Munson Springs
Reinhart Creek
Rocky Riffle
Sevenmile Canal
McNeil Point
Maklaks Spring
Maklaks Crater
Mazama Rock
Middle Fork Catherine Creek
Munson Ridge
Munson Creek
Oakerman Butte
North Fork Copeland Creek
Palisades
Packsaddle Creek
The Potholes
Post
Poison Creek
Prineville
Rand Ranger Station (historical)
Schuster Place
Skookum Gorge
South Fork Copeland Creek
Starr Spring
Stevens Canyon
South Fork Wind Creek
Sprague Lake
Trapper Creek
Umpqua National Forest
Wallowa-Whitman National Forest
Volmer Ditch
Whitcomb Island
Whitehorse Riffle
Whitehorse Pond
Sun Notch
Teardrop Pool
Taylor Creek Gorge
Tanner Creek Falls
Romaine Gulch
Woodworth (historical)
Wheeler City (historical)
Baldwin Gulch
Pocket Knoll
West Fork Squaw Creek
East Fork Squaw Creek
Midnight Gulch
China Creek
Valley Creek
Maple Creek
Whiskey Gulch
Windy Creek
Ryan Creek
Selma Cemetery
Hegan Creek
Schmitts Bayou
Salt Gulch
Hansen Creek
Booker Creek
Potter Gulch
Bonham Spring
Wonder Mountain
Azalea Spring
Brockhurst Creek
Sulphur Spring
Slide Creek
Marks Creek
Rocky Bar Creek
Price Creek
Dostler Creek
East Fork Hewitt Creek
Venner Creek
Paradise Creek
Kelsy Creek Campground
Fish Hook Creek
West Fork Clay Hill Creek
Fives Creek
Oak Flats Cemetery
Snout Creek
Muleshoe Creek
Boiler Riffle
Rattlesnake Creek
Old House Creek
Tom Fry Creek
Sundown Creek
Stonehouse Creek
Anderson Creek
Walker Creek
Cochran Creek
Chrome Creek
North Fork Foster Creek
Foster Pond
Southard Lake
Doerr Creek
Billys Creek
Hosposki Creek
Milbury Creek
Laird Lake
JoAnn Creek
Bacon Flat
Fall Creek
Blaine Cemetery
Wake Creek
Thorn Creek
Elk Bend Campground
Bear Creek
Fagan Creek
Larson Creek
Flower Pot Creek
Seal Rock
Dick Creek
Memaloose Creek
Tomlinson Creek
North Branch Fall Creek
Netarts Spit
Austin Creek
Tillamook Reservoir
Killam Fawcett Reservoir
Marys Creek
Nestocton (historical)
Tillamook River Safety Rest Area
Slide Creek
Neilson Slough
Stasek Slough
Walter Creek
Woods Creek
Gilbert Creek
Bummer Creek
Wildcat Creek
Hester Creek
Jackson Creek
Little Foland Creek
Fuqua Creek
Munson Creek Falls State Natural Area
Sams Ponds
North Fork Reservoir
Helen Lake
Mount Home Cemetery
Sand Creek
Hidden Creek
Gray Flat
Patrick Creek
Seal Cove
Ward Memorial Cemetery
Seal Point
Tanbark Point
Table Rock
Sand Hill
Black Point
Eiler Creek
House Rock Creek
Green Hill
Alder Spring
Big Alder Spring
South Fork Whalehead Creek
Thomas Hill
Wridge Creek
Whiskey Creek
Carpenterville Brookings Wayside (historical)
Ridge Knob
Arch Rock
Rainbow Island
Thomas Creek Rest Area
Thomas Point
Windy Point
Fountain Rock
Salmon Creek
Ragsdale Creek
Whitewash Creek
Hayes Cemetery
Powers Cemetery
Mystic Creek
China Creek
Morris Creek
Powers Pond
Alder Creek
Rowland Prairie
Coquille Myrtle Grove State Park
Grants Creek
Etelka (historical)
Florence Creek
Eckley (historical)
McFarlin (historical)
Sucker Creek
Josh Creek
Laird Creek
Boundary Picnic Ground
Miller Creek
Bales Creek
Stretch Creek
South Creek
Yankee Branch
Triangle Lake
Fawn Creek
Minnehaha Ridge
Rock Meadow
Razor Ridge
Cathedral Creek
Rondeau Cemetery
Heart Lake
Deadhorse Creek
Cole Creek
Cook Creek
East Fork Drew Creek
Growey Creek
North Fork Dismal Creek
Elk Creek
Steamboat Creek
Maple Creek
Granite Creek
Copper Creek
Gilbeaugh Creek
Ash Creek
Lavadoure Cemetery
Hill County Wayside
Lick Creek
Cedar Creek
Canyon Creek
Eight Dollar Mountain Creek
Rail Gulch
Oxbow Butte
Eddington Creek
Lost Creek
Grant (historical)
Sawyer Slough
Brown Slough
Mitchell Cemetery
Buck Gulch
Keyte Creek
Cooksie Gulch
Delta Creek
Paint Creek
Waterspout Creek
Spangler Gulch
Cold Springs Creek
Toss Gulch
Friday Spring
Maple Gulch
Sanders Gulch
Belknap Gulch
North Star Gulch
South Fork Rocky Gulch
Fraser Spring
Sailor Gulch
Bartley Gulch
Baldy Creek
Birch Creek
East Fork Howard Creek
Julie Creek
Patrick Gulch
Smith Creek
Almeda (historical)
Rand Recreation Area
Carpenters Island Park
Blue Canyon
Little Bear Creek
Green Gulch
Althouse (historical)
All Hours (historical)
Hydraulic Gulch
Browntown Gulch
Hansford Gulch
Allentown (historical)
Brown City (historical)
Scofield Gulch
Lime Gulch
Toinen Gulch
Pigeon Gulch
Quail Gulch
Frog Gulch
Studhorse Creek
Sailor Gulch
George Drain
Butcher Gulch
Hope Spring
O'Brien Creek
Althouse Slough
Frost Gulch
Choke Cherry Creek
Rosenberg Reservoir
Bacus Creek
Mill Creek
Jimmy Creek
Tennessee Gulch
Canyon Gulch
Montgomery Creek
Sauers Creek
Chandler Creek
Peterson Creek
Kerby Slough
Jacobson Springs
Horse Spring
Camp Creek
Payne Slough
Donaldson Creek
Lipp Creek
Kleiner Creek
Smith Creek
Johnston Creek
Black Creek
Bear Creek
East Fork of West Fork Cow Creek
Porphyry Spring
Bolivar Spring
Anaktuvuk Saddle
August Knob
Arrastra Fork Mule Creek
North Creek
Bear Creek Recreation Site
Cabin Creek
Gold Spring
Hidden Creek
Cawrses Log Pond
Bone Mountain Pond
Gobblers Knob
Clear Creek Camp
Foggy Creek Camp
Rock Creek
Little Vulcan Lake
Limber Camp (historical)
Parker Creek
Shuttpelz Lake
Hall Lake
William M Tugman State Park
Tenmile Lake County Park
South Eel Campground (historical)
Clear Lake
Saunders Lake
Saunders Lake Boat Ramp
Charlotte Creek
Tenmile
McKeown Reservoir
Templeton Cemetery
Halfmoon Bay
Copple Creek
Wades Flat
Hinsdale Slough
Koepke Slough
Battle Rock Wayside Park
Coon Creek
Stan Creek
Butler Bar Recreation Site
Panther Creek Campground
Platinum Creek
McGribble Campground
Rocky Point Creek
Rocky Creek
Bear Creek
East Fork Panther Creek
West Fork Panther Creek
Mid Fork Panther Creek
Fort Point
Mountain Well Camp
Corbin (historical)
O'Brien Creek
Gillman Creek
Euchre Creek Pond
Parker Creek
Ophir Safety Rest Area
Ophir Beach
Frankport
Sunshine Mine
Richman Reservoir
Silver Butte Creek
Bagley Creek
Marsh Log Pond
Summers Creek
Bull Creek
Price Creek
Madden Creek
North Fork Crystal Creek
Middle Fork Crystal Creek
Boulder Creek
Edson Creek Campground
Pipeline Creek
Duvall Creek
Grassy Creek
Small Creek
Bea Creek
Lily B Creek
Sixes River Recreation Site
Little Redwood Recreation Site
Gardner Bar
Miller Bar
Ram Creek
Ostenbery Bar
McVay Creek
Johnson Creek
Cooley Creek
Moore Creek
Chetco (historical)
Winchuck State Park
Wildcat Creek
Dry Creek
Louise Creek
Grass Lake
Kink Creek
Wheeler Ridge
Long Ridge Campground (historical)
Nook Creek
Malheur Ford
Crump (historical)
Blacksmith Creek
Bray Gulch
Birch Creek
Deep Gulch
Thunder Gulch
Trickle Creek
Post Gulch
North Fork Greely Creek
Pollard Spring
Oak Flat
Bear Gulch
Hope Spring
Rail Gulch
Holton Creek
Packard Gulch
Phipps Gulch
Randle Creek
Lake Creek Flats
Mud Creek
Long Canyon
Yew Creek
Maple Creek
Gardener Reservoir
Millport Slough
Tide Slough
Kerby Ridge
Agate Point
Fourmile Camp
Beachside State Recreation Site
Little Creek Spring
Copper Mountain Mine
Metolius Canyon
Barkley Creek
Nancy Creek
Mitchell Creek
Reynoldsville
Tillicum Beach
San Marine State Park
Strawberry Hill
Smelt Sands State Recreation Site
Big Creek Log Pond
Worth Creek
Bay Hills Reservoir
South Beach State Park
Forfar
Ona Beach
Ona Beach State Park
Bowers Creek
Keno Cemetery
Horsehead Island
Bear Creek Rapids
Dowell Arm
Three Mile Prairie
Ackerley Creek
Clear Creek
Collard Creek
Mitchell Creek
Kilmer Spring
Baker Beach Recreation Site
Baker Beach
Quarry Creek
Mussel Lake
Nott Lake
Dahlin Arm
Mercer (historical)
Heceta Junction Lake
Haring Cemetery
Panther Creek
Red River
South Fork Weist Creek
William P. Keady State Wayside
Constantine Creek
Annice Creek
Darling Creek
Freeman Creek
Weist Creek
Patterson Creek
Alsea Bay - North Bridgehead Wayside (historical)
Lotus Lake
Walker Creek
Twombly Creek
Little Creek
Elephant Rock
Holly Beach
Driftwood Beach State Recreation Site
Judd
Spring Creek
Long Creek
Cedar Creek
Gender Creek
Gregory Creek
Fourmile Slough
Crystal (historical)
Fat Klamath Meadows
Tiger Lily Spring
South Mound Spring
Blue Spring
Short Creek
Sevenmile Marsh Campground
Lake Ruden
Lake Florence
Crippled Horse Spring
Corbell Ditch
Calor (historical)
Ivan (historical)
Abernathy Station (historical)
Humboldt Spring Camp (historical)
Submarine Hole
South Fork Lawson Creek
Tolman Creek
Koontz and Davis Creek
Lyons Reservoir
Grange Creek
Ingersoll Gulch
Lone Rock
Willanch Inlet
Johnston Creek
Ocean View Memorial Gardens
Bluebill Recreation Site
Upper Empire Lake
Masonic Cemetery
Beaver Pond
Oak Flat Creek
Moon Creek
Green Wall
Cox Mine (historical)
Albright Mine (historical)
Little Siberia Mine
Hustis Mine (historical)
Golden Eagle Mine (historical)
Pearsoll Creek
Chetco Pass Creek
Bills Gulch
Myrtle Creek
Mill Creek
O'Conner Creek
Golden Dreams Mine (historical)
Krambeal Creek
Flood Creek
Lynch Creek
Tomcat Hill
Pistol River State Park
McKinley Creek
North Fork Myers Creek
Egans Creek
Daniels Creek
Pine Point
Smith Creek
Yorke Creek
Taylor Creek
Hunter Creek
Turner Creek
Antone Creek
West Fork Cunniff Creek
East Fork Cunniff Creek
Cunniff Creek
Pioneer Cemetery
Pistol River Cemetery
Miller Creek
Ferry Hole Bar
South Fork Riley Creek
Middle Fork Riley Creek
North Fork Riley Creek
Doyle Point
Knoxville (historical)
Needles
Barley Beach
Otter Point State Park
Scott Creek
Agate Beach
Wakeman Beach
Cummins Creek
Drip Creek
Mag Creek
Austin Creek
Jack Davis Creek
Station Creek
Murphy Creek
Monty Creek
Small Fry Lake
Deer Creek
Plaza Creek
South Fork Gordon Creek
North Fork Gordon Creek
Palmer (historical)
Dalton Creek
Henderson Creek
Donahue (historical)
Brower (historical)
Butler Creek
George Cemetery
Kotzman Creek
Little Sandy Diversion Dam (historical)
Bowman Creek
Laughing Water Creek
Firwood Creek
Marmot Dam (historical)
Arrow Creek
Spring Creek
Wall Creek
Kasch Creek
Hope Lake
Eagle Creek Upper Falls
Porter (historical)
Lower Rock Lake
Middle Rock Lake
Upper Rock Lake
Steep Spring
Spring Creek
Aquarius Spring
Swift Creek
Deschutes Canyon
Hood River Hatchery
Lint Slough Fish Hatchery (historical)
Spout Springs Ski Area
Calico Gulch
Edgewood Creek
Odessa Spring
Tomahawk Ski Bowl (historical)
Harriman Spring
Sunset Campground
Sesti Tgawaals Marsh
Shoalwater Bay Marsh
Barkley (historical)
Jumping Rock
Hagelstein County Park
Wampler Marsh
Doaks Marsh
Grampian Hills
South Pass
South Creek
Bridge Creek
Swan Creek
Camp Creek
Wampler Spring
McCollum (historical)
Klamath River Recreation Site
Forest (historical)
Camp Day (historical)
Clover Station (historical)
Maggard (historical)
Parker (historical)
Canby Mountains
Chiloquin Rapids
Chiloquin Narrows
Larkin Spring
Larkin Creek
Williamson River Access Park
Fort Creek Ditch
Idlerest (historical)
Hatchery Spring
B Canal
C Canal
Squaw Creek
Wood River Marsh
Agency Spring
Lobert Cemetery
Agency Landing (historical)
Lobert (historical)
Hobbs Ditch
Gerwick Ditch
Yamsay Land and Cattle Company Ditch
Scott Creek Recreation Site
Sand Creek Canal
Sand Creek Junction
Middle Fork Trout Creek
Wocus Bay Guard Station
Skellock Guard Station
Y J Canal
Kittredge Canal
Bluejay Creek
Johnson Cemetery
Cusick Creek
Cricket Creek
Flat Creek
Hill Creek
Kendale Creek
Myers Canyon
Needle Rock Spring Camp
West Fork Abbott Creek
North Fork Abbott Creek
Serviceberry Creek
Heck Rock
Bitter Lick
Persist Ranch Reservoirs
Soup Creek
Huckleberry Gap
Whaleback
Green Prairie
Cold Spring Creek
Big Bend
Pipeline Creek
North Fork Mill Creek
North Fork Little Copeland Creek
Cow Creek
Dead Soldier Creek
Coffee Creek
Salt Fork Fourbit Creek
Ash Creek
Parker (historical)
Paradise (historical)
Cold Springs
Doe Point
Walch Creek
Shake Camp Spring
Swamp Creek
Elder Spring
Grizzly Canyon
Service Glades
Owens Spring
Railroad Prairie
Hafer Flat
Jerry Gotts Spring
Dudley (historical)
Fall Creek
Tie Creek
Cold Spring Creek
Yellow Rock Canyon
Berrian Spring
Cornstock Ditch
Swayne Ditch
Dry Gulch
Darnielle Gulch
Right Fork Tallowbox Creek
Left Fork Tallowbox Creek
Tallowbox Creek
Straight Gulch
Saw Pit Gulch
Mocks Gulch
Quartz Gulch
Seattle Bar (historical)
Salt Creek Recreation Site (historical)
Osborne Creek
Perdue Creek
Dunlap Creek
Matz Draw
Pode Creek
Rich Creek
Richard Creek
Wildcat Gulch
Cod Creek
Quedo Creek
Haven Creek
Garradella Gulch
Mulvaney Gulch
Peterson Gulch
South Fork Fiddler Gulch
Jack Creek
Jeffery Creek
Pool Creek
Green Creek
Trout Creek
Turpy Creek
Bogue Creek
The Cascades (historical)
Little Jim Gulch
Oregon Bar
Sugarloaf Gulch
Horsetail Creek
Yew Wood Gulch
Davidson Gulch
Elder Gulch
Wildcat Creek
Hartley Reservoir
Blue Jay Creek
Dugout Spring
Little Miller Lake
Brushy Gulch
Carr Gulch
Cave Creek Recreation Site
Onion Gulch
Julian Gulch
Goldsby Gulch
State of Oregon
Malheur National Forest
Ochoco National Forest
Rogue River National Forest
Bear Valley National Wildlife Refuge
Diamond Peak Wilderness
Grassy Range
Hells Canyon National Recreation Area
Hells Canyon Wilderness
Klamath Marsh National Wildlife Refuge
Minam State Park
Mount Jefferson Wilderness
Rogue River Range
Siletz Reservation
Sun Pass State Forest
Benton County
Clackamas County
Crook County
Curry County
Deschutes County
Hood River County
Jefferson County
Josephine County
Klamath County
Wallowa County
Wasco County
Washington County
Barron Creek
North Fork Barron Creek
Trail Camp
Grouse Creek Gap
Bear Gulch
Cole Spring
White Point (historical)
Tuff (historical)
Coggins Saddle
Lamb Mine
Jemmison Gulch
Wrights Creek
Mountain View Cemetery
West Fork Wrights Creek
Mountain View Cemetery
Ashland Cemetery
Sulphur Springs
Sulphur Springs
Danns Spring
Hamby Spring
Scenic Hills Cemetery
Hargadine Cemetery
Meyers Cemetery
Rock Creek
Jewett Creek
Carl Creek
Hamlin Gulch
KirKirs Canyon
West Gold Brook
East Gold Brook
South Fork Louse Creek
East Fork Gilbert Creek
West Fork Gilbert Creek
Frosty Canyon
Simmons (historical)
Ferrydale Cemetery
Wilderville Cemetery
Carter Creek
Robertson Creek
Knights Gulch
Rail Canyon
Haven Creek
Britton Creek
Cedar Creek
Fowlie Creek
Harmon Creek
Drier Creek
Dry Creek
Small Gulch
Little Cheney Creek
Stringer Creek
Skunk Creek
Johnson Creek
Black Canyon Creek
Dales Bluff Creek
Maple Gulch
Blodgett Ditch
Blodgett Creek
Webb Reservoir
Bricker Creek
Dry Creek
Wood Reservoir
Pennington Butte
Cold Springs Campground
Lost Creek Spring
Crater Lake Ski Bowl
Goodbye Creek
Walker Creek
Granite Hill (historical)
Granite Hill Cemetery
Owl Creek
Gaughan Spring
Fisher Gulch
Wrights Creek
Heath Creek
McCaffery Pond
Hutchinson Creek
Dry Creek
Radford Creek
Hob Knob
Dumont Creek Recreation Site
Boulder Creek Recreation Site
Eureka Pond
White Creek Recreation Site
Coolwater Recreation Site
Negro Ridge
Emile Creek Recreation Site
Little River Christian Camp
Shivigny Creek
Wolf Creek Recreation Site
Wolf Creek Falls Recreation Site
Wolf Creek Falls
Red Butte Burn Camp
Cultus Lake
Gobblers Knob
Bogus Creek Recreation Site
Williams Creek Recreation Site
Union Creek Spring
Rabbit Creek
Broken Arrow Recreation Site
South Shore Recreation Site
Dry Creek
Pumice Beach (historical)
Thielsen View Recreation Site
Nugget (historical)
Briggs Reservoir
Letitia Cemetery
White Rock Springs
Stacey Gulch Creek
Collins Creek
Sampson Lake
Cavitt Falls
High Prairie Creek
Cole Creek
Cedar Creek
Susan Creek Park (historical)
Fish Creek Forebay
Bridge Prairie
Winter Knight Camp
Charlie Creek
Alvin Creek
Barkenberger Creek
Karen Creek
Lemolo Number 2 Canal
Toketee Recreation Site
Picture Rock Prairie
Jack Falls
Station Creek
Eagle Rock Recreation Site
Boulder Flat Recreation Site
Slim Chance Campground
President Ridge
Horseshoe Bend Recreation Site
Canton Creek Recreation Site
Mosquito Camp
Buckeye Lake Campground
Cliff Lake Campground
Castor Lake
Silver Creek
Buster Spring
Alligator Lake
Birdseye Camp
Buckhead Mountain Campground
Raven Rock
Big Twin Lakes Campground
Lake in the Woods Recreation Site
Harpham Lake
Hemlock Lake Recreation Site
Last Camp
Camp Vena
Flood Creek
Andraieff Meadows
Times Square Rock
South Umpqua Falls Recreation Site
Coffeepot Creek
Little Franklin Creek
Burchard Lake
Rock Island
Scottsburg Cemetery
Golden Ridge
Skagit Ridge
Lunch Ridge
Lenz Creek
A Canal
Gayheart Slough
Leonard Slough
North Fork Ditch
Elder Ditch
Spring Creek
East Branch Whisky Creek
Lola K West Spring
Williams Drain
Modoc Billy Creek
Smokey Lake
Rock Creek Cemetery
Bechdoldt Gulch
Yamsay (historical)
Yamsay Spring
Williamson River Spring
Annie Creek Slough
Melhase Ditch
Crescent Airport (historical)
West Fork Evans Creek
Hawk Rim
McKinney Creek
Maude Oakerman Spring
Jaca Creek
Bellworm Reservoir
Dick Miller Canyon
Bridge Waterhole
Elliott Ridge
Elliott Spring
Pine Lake
Clay Myers State Natural Area at Whalen Island
Pothole Spring
Smoke Creek Spring
Magic Lantern Creek
Herman Creek Horse Camp
Frazier Upland
Cow Camp Meadows
Skookum Creek
Spring Creek
Central Pumice Cone
East Fork Brisbois Creek
Jackass Creek
Reub Long Butte
Sugarloaf
West Fork Brisbois Creek
Ryegrass Creek
Rock Quarry Canyon
Williams Crater
Wilson Creek
Brisbois Creek
Crossen Creek
Watkins Flat
Waespe Point
South Fork Cow Creek
Sam Creek
Lime Gulch
Spring Gulch
South Creek
Big Red Mountain Creek
Two Springs
Smith Falls
Saddle Camp Creek
Lake Murphy
Jackass Ridge
Jacks Saddle
Judson Rock
Day Creek
Dinah-mo Peak
Downing Point
Elephant Lake
Glenwood Creek
Grizzly Creek
Frog Rock
Hobart Creek
Knott Spring
Moonfalls
Spirit Falls
Gleason Creek
Gale Creek
Black Pine Spring
Canyon Creek Meadows
Dollar Nine Lake
Sand Camp Lake
Bone Lake
Torso Lake
Peewee Lake
Three Creek Meadow
Mill Creek Falls
Mud Spring
Rancheria Prairie
Big Elk Meadow
Whiskey Spring
Twin Ponds
Butte Falls
Fredenburg Spring
Rumley Creek
Evergreen Spring
Green Creek
Cougar Spring
Sugar Pine Spring
Sand Creek
South Fork Spring
Williamson River Ditch
Forest Spring
Cabin Spring
Recovery Spring
Wocus Butte Spring
Spring Hill
Hilltop Reservoir
Miranda Spring
Beaverdam Springs
Sand Point
Rocky Hole Reservoir
Corbell Spring
Lobert Draw Reservoir
Grouse Spring
Hawks Lake
Lone Pine Reservoir
Borrow Reservoir
Nut Reservoir
Prairie Reservoir
Wigwam Reservoir
Long Reservoir
Grade Reservoir
South Grade Reservoir
John Smith Reservoir
Pelland Spring
Electric Pond
Ace Pond
Powerline Pond
Ponina Spring
Mill Creek Spring
Lonesome Pond
Wild Pond
Camp Six Guard Station
Goose Spring
Ray Ranch
Indian Springs Campground
Slide Creek Recreation Site
McNaughton Spring Recreation Site
Strawberry Basin Trail
Buckhorn Meadows Trail
Slide Basin Trail
Meadow Fork Trail
Twin Springs Trail
Deerhorn Campground
Dixie Trail Mine
Davis Creek Trail
Cougar Ridge Mine
Smuggler Mine
Shatt Mine
Bull Run Creek
Boulder Group Mine
Bimetallic Mine
Little Doe Mine
Middle Fork Recreation Site
Plute Spring
Coyote Bluff
Head O'Boulder Spring
Faulkner Gulch
Rattlesnake Spring
Upper Manhattan Spring
Fawn Spring
Eagle Spring
Gwinn Spring
Rock Camp Spring
Cedar Spring
Red Knob
Giebeler Lake
STEP Creek
Beachie Creek
Crown Creek
East Basin
West Basin
Ritter Hot Springs
Amos Lake
Claypool Butte
Brandenburg Butte
Maiden Peak Saddle
Skunk Creek
Gordon Creek
No Name Creek
West Fork Rattlesnake Creek
Lehman Meadow
North Fork Rock Creek
West Branch Sam Creek
Easter Ridge
Dune Lake
Cape Meares National Wildlife Refuge
Deschutes National Forest
Mount Hood National Forest
Three Arch Rocks National Wildlife Refuge
Winema National Forest
Siltcoos Lake Dam
Thompson Dam
Tahkenitch Lake Dam
Albertson Dam
Allen Creek Dam
Andy Hill Dam
Andy Hill Reservoir
Antelope Flat Dam
Applegate Dam
Applegate Lake
Balm Creek Dam
Barnes Butte Dam
Bates Dam
Bend Power Dam
Big Sandy Dam
Big Sandy Reservoir
Three Creek Lake
Big Three Creek Lake Dam
Bonnieview Dam
Bradshaw Dam
Bradshaw Number 2 Dam
Bradshaw Reservoir Number Two
Brewer Dam
Buffalo Dam
Bull Prairie Dam
Bull Run Lake Dam
Campbell Dam
Catching Reservoir
Clark Lake Dam
Clear Lake Dam
Clearwater Number One Diversion Dam
Clearwater Number Two Forebay Dam
Clemens Log Pond Dam
Clemens Dam
Coos Bay Timber Company Dam
Cottonwood Dam
Cottonwood Dam
Crater Lake Dam
Crow Creek Dam
Crow Creek Reservoir
Cyrus Dam
Cyrus Reservoir
Dam Number One
Delintment Lake Dam
Dickson Dam
Duncan Dam
Elgin Mill Wastewater Lagoon
Elgin Mill Wastewater Lagoon Dam
Elms Dam
Erenos Dam
Erenos Reservoir
Fenmore Dam
Ferry Creek Dam
Firwood Veneer Corporation Dam
Firwood Veneer Corporation Reservoir
Fish Creek Diversion Dam
Fisher Dam
Fleet Dam Number Two
Fleet Reservoir Number Two
Flynn Dam
Fritz Creek Dam
Gale-Merwin Dam
Grays Slough Reservoir
Grindstone Dam
Grohs Dam
Hells Canyon Reservoir
Hemlock Meadows Dam
Hobin Dam
Hobin Log Pond
Hoover Dam Number 3
Howard Prairie Dam
Jefferson Plywood Company Dam
Jones Dam
Johnson Creek Dam
Jubilee Meadows Dam
Ketchum Dam
King Dam
Klootchman Creek Dam
Klootchman Creek Reservoir
Lake Edna Dam
Lake Harriet Dam
Lake Penland Dam
Lake Pons Dam
Langdon Lake
Langdon Lake Dam
Lint Slough Dam (historical)
Lippert Dam Number Two
Lippert Reservoir Number Two
Little Three Creek Lake Dam
Lost Creek Dam
Lower Empire Lake Dam
Lower Green Point Dam
Lower Pine Lake
Lower Pine Lake Dam
Lower Pony Creek Dam
Mainline Dam Number 1
Mainline Dam Number 2
Mainline Dam Number 3
Marks Lake
Marks Lake Dam
McKenzie Canyon Dam
Medford Forest Nursery Dam (historical)
Medford Forest Nursery Reservoir (historical)
Merwin Reservoir Number 1
Merwin Reservoir Number 2
Middle Empire Lake
Middle Empire Lake Dam
Miller Lake Dam
Miller Dam
Miller Dam
Morrow Brothers Dam
Mortimer Canyon Dam
Muddy Creek Dam
Newsome Creek Dam Number 1
Newsome Creek Reservoir Number 1
North Fork Dam
North Fork Diversion Dam
North Fork Diversion Reservoir
North Unit Diversion Dam
Obenchain Dam
O'Connors Puddle Dam
O'Connors Puddle Reservoir
Officers Dam
Olive Lake Dam
Oxbow Ranch Dam
Palmer Dam
Paris Dam
Pelton Regulating Dam
Pelton Regulating Reservoir
Peterson Creek Dam
Pine Hollow Dam
Pyles Canyon Dam Number Two
Pyles Canyon Reservoir Number Two
R K Moseley Dam
Renner Dam
Rickmans Camp Creek Number 2 Dam
Rickmans Camp Creek Reservoir Number Two
Rock Creek Lake Dam
Rock Quarry Canyon Dam
Rough and Ready Mill Pond Dam
Rough and Ready Log Pond
Slide Creek Dam
Slide Creek Reservoir
Smith Dam
Three Sisters Irrigation District Dam
Watson Reservoir
Squaw Lakes Dam
Stallard Dam
Tall Timber Dam
Tall Timber Reservoir
Thompson Dam
Timothy Lake Dam
Trillium Lake Dam
Twelvemile Dam
Ukiah Sewage Lagoon
Ukiah Sewage Lagoon Dam
Unity Dam
Upper Green Point Dam
Upper Pine Lake
Upper Pine Lake Dam
Wallowa Lake Dam
Wasco Dam
Watson Dam
Watson Reservoir
Willow Creek Dam
Withers Dam
Wolf Creek Dam
Zoglmann Dam
Zoglmann Reservoir
Coonskin
Marys Creek
Slide Creek
Bungalow Creek
McCurdy Creek
Little Silver Creek Lake
Rawhide Creek
Dasher Meadow
Nobles House
Briggs Creek Recreation Site
Little Illinois River Falls
Montana Spring
Miami Bar
Pearsoll Mine
Eagles Nest Mine
Peck Mine
Fall Creek Copper Mine
Deep Gorge Mine
Brushy Bar Recreation Site
Illinois Wild and Scenic River
Rogue Wild and Scenic River
Elko Creek
Winkle Bar Riffle
Antler Creek
South Fork Galice Creek
Sailor Jack Creek
Taylor Creek Bar
Old Man Riffle
Bear Gulch
North Fork Rocky Gulch
Almeda Bar
Marks Island
Upper Galice Riffle
Lower Galice Riffle
Schoolmarm Creek
Armedio Riffle
Jacoby Butte
Mineral Spring
Windy Valley
Humboldt Spring
Black Rock Creek
Bluff Creek
West Ridge Camp
Bald Mountain Prairie
Bald Mountain Camp
Forest Creek
Horse Sign Creek Rapids
Brandon Camp
Burt Camp
Sizeable Stream
Fresno Camp
Lish Lake
Moores Creek
Gardner Mine
Freeland Saddle
Lone Tree Pass
Payton Riffle
Burnt Rapids
Billings Rapids
Foster Rapids
Foster Bar
Burnt Rock
Illahe Recreation Site
Coquille River Falls
Two-Bit Creek
Gurkin Creek
Agness Pass
Sru Lake Campground
Brewery Hole
Allen Pool
Smith Riffle
Mermaid Riffle
Smith Hole
Big Eddy
Little Wildcat Rapids
Tom Fry Eddy
Milkmaid Riffle
Wee Riffle
Twin Sisters
Walker Riffle
Lower Shasta Costa Riffle
Hotel Riffle
Upper Crooked Riffle
Old Diggins Riffle
Walker Bar
Agness Bar
Big Creek Arm
Copeland Spring
Haines Creek
Mussel Rock
Yachats Ridge
Abe Creek
Reese Lake
Devils Den
Wear Creek
High Cascades Ranger District - Prospect Office
Gawa Church Camp
Owens Ranch
Pennington Ranch
Stanley Ranch (historical)
Elder Ranch
Harvey Ranch
J V Withers Ranch
Mill Creek Recreation Site
T Emery Ranch
Silver Dollar Cinder Pit
Sycan Ford
R Emery Ranch
Sunday Camp
Wagon Camp
Trail Forest Service Facility
Clearwater Falls Recreation Site
Star Gulch Recreation Site
Huckleberry Mountain Recreation Site
Sevenmile Marsh Trailhead
Sevenmile Trail
Watkins Recreation Site
Manzanita Trailhead
Seattle Bar Trailhead
Seattle Bar Recreation Site
Elk Creek Reservoir
Takelma Park Picnic Area
Neal Springs Campground
Abbott Creek Recreation Site
Copper Recreation Site
Joseph H Stewart State Park
Huckleberry Lake Campground
Lakeview Water Users Headquarters
Ashcraft Ranch
Bly Ranger Station
Fishhole Substation
Dice Spring
Lee Adkins Place
Obenchain Ranch
BK Ranch
Campbell Ranch
North Fork Ranch
Cougar Springs
D Emery Ranch
Silver Creek Marsh Recreation Site
Wickiup Spring Forest Service Station (historical)
Gaylord Ranch
Fred Ross
Dog Lake Recreation Site
Vernon Ranch
Snider Ranch
Fisher Ranch
Gunsight Well
Warm Springs Campground (historical)
JC Collins Ranch
Pacific Telephone and Telegraph Substation
Horse Ridge Natural Area
East Lake Resort
Boundary Springs Recreation Site
Crescent Ranger Station
Lava Flow Recreation Site
Timpanogas Recreation Site
Indigo Lake Recreation Site
Elk Lake Pack Station
Elk Lake Guard Station
Lava Lake Boat Rental
Cabin Lake Recreation Site
Ground Hog Butte
Bates Ranch
Pine Mountain Recreation Site
Sparks Lake Recreation Site
China Hat Recreation Site
Upper Three Creek Sno-Park
Lower Three Creek
Besson Boating Site
Sand Spring Recreation Site
Lavacicle Cave Geological Area
Royce Mountain Snow Park (historical)
Crescent Lake Guard Station
Crescent Lake Resort
Sisters Guard Station (historical)
Charlton Lake Shelter
Little Belknap Trail
Summit Lake Recreation Site
Memaloose
Amalgamated Mine
Elk Lake Recreation Site
Metzler Park Recreation Site
Latourell Recreation Site
Bonney Crossing Recreation Site
Lost Creek Recreation Site
Plot Butte Waterhole
Spring Butte Well Camp
Cascade Hyland Resort
Kinzel Lake Campground (historical)
Hoodland Park (historical)
AJ Dwyer Roadside Reservation Memorial Area
Wildwood Recreation Site
Bull Run Watershed
Joe Graham Horse Camp
Tenino Boat Launch
Wickiup Butte Recreation Site
Rho Ridge Shelter
Devils Lake Recreation Site
Sheep Spring Horse Camp
Sport Haven Trailer Park Recreation Site
Brookings Recreation Site
Chetco Ranger Station
South Jetty Recreation Site
Siuslaw Vista
Cascade Head Scenic Research Area
Alder Dune Recreation Site
Holman Vista Recreation Site
Griffin Picnic Area
Maddsens Knob
Marys Wayside Recreation Site
Spalding Pond Recreation Site
Sam Brown Recreation Site
Secret Creek Recreation Site
Myers Creek Recreation Site
Indian Creek Campground
Gold Beach Ranger Station
Gold Beach Boat Launch
Anderson Mine
Agness Recreation Site
Villair Ranch
Cold Spring Camp
Ferris Ford Work Center
Eden Valley Recreation Site
Bowman Ranch
York Creek Botanical Area
Three Trees
Cold Springs Camp
The Wild
Little Beaver Creek
Wolf Creek
Angell Job Corps Center
Riveredge Recreation Site
Blodgett Work Center
Trail Creek
Chittam Creek
Grant Ridge
Cummins Creek Wilderness
Munson Creek Falls
Alsea Valley
Wren Forest Service Station
Waxmyrtle Trail
Lobster Bar
Pack Saddle Gulch
Hardtack Creek
Carter Lake Recreation Site
Carter Dunes Trail
Oregon Dunes Recreation Site
Carter Lake Boat Ramp
Lodgepole Recreation Site
Driftwood II Recreation Site
Middle Eel Campground (historical)
Spinreel Recreation Site
Tahkenitch Boat Ramp
Overlook Loop Trail
Crown Zellerback Campground
Tahkenitch Trail
Tahkenitch Landing Recreation Site
Threemile Lake Trail
Swede Fork
Norris Creek
Drift Creek Wilderness
Parking Lot Marsh
North Spit
Stagecoach Trailhead
Shedd Camp Shelter
Crockett Knob Lookout
Matlock Spring (historical)
Penland Lake Recreation Site
Monument Mountain Lookout
Lunch Creek
Shady Cove Recreation Site
Weigand Well
Lone Pine Artesian Well
Sumner Spring
Lehman Hot Springs Recreation Site
Research Corrals
Only Entry Point
Elgin Forest Service Station
Oregon Mine Recreation Site
Black Ranch
Bear Wallow Camp Recreation Site (historical)
Yokum Cabin
Walker
Westview Shelter
Salmon Creek Falls Recreation Site
Big Creek Meadows Recreation Site
Tamarack Lookout Tower
Gold Dredge Recreation Site
Toll Bridge Recreation Site
Whitcomb Creek County Park
North Shore Recreation Site
Indian Rock Trail
Desolation Butte Lookout
Indian Rock Lookout Tower
Santiam Sno-Park
North Loop Trail
Hoodoo Ski Bowl Snow-Park
South Loop Trail
South Loop Cut Off
Corbett Sno-Park
Thompson Canyon
Mill Creek Watershed
North Fork Umatilla Wilderness
Grande Ronde Scenic Area
Knob Trail
Corral Spring Forest Service Station
Fourmile Flat Quarry
Great Meadows Recreation Site
Four Mile Lake Trail
Rye Spur Trail
Lake of the Woods Resort
Bear Camp
Devils Flat Recreation Site
Greek Creek
Crawfish Shelter
Trail Cabin
Cabin Lake Wildlife Area
Rogue-Umpqua Divide Wilderness
Indian Creek School (historical)
Oliver Ranch
Jenkins Cabin
Dunlap Cabin
Rock Creek Spring
Rudio Mountain Lookout
Holiday Ranch
Smith Spring
Call Meadow Forest Service Facility
Cross Ranch
Boy Scout Cabin
Craddock Ranch
West Myrtle Butte Forest Service Facility
Deer Spring
Spring Valley meadow
Mountain View School (historical)
Glascock Ranch
Hankins Ranch
FLCR Translator Tower
Smith Ranch
Brisbois Ranch
Lower Camp Creek Recreation Site
Murray Recreation Site
Malheur National Forest Headquarters
Blue Mountain Ranger Station
LC Mountain Translator Site
Snowshoe Camp
Sky Line Camp
John Day Sanitary Landfill
Long Creek Municipal Watershed
Benson Ranch
Oliver Ranch
Luce-Belshaw School (historical)
Pine Creek Recreation Site
Buckhorn Meadow Recreation Site
Fletcher Ranch
A Coombs Ranch
Miller Ranch (historical)
Howard Ranch
Carter Ranch
I Standbro Ranch
H Coombs Ranch
Winegar Ranch
B Standbro Ranch
Velvin Ranch
Depot Park Recreation Site
Prairie City Ranger Station
Prairie City Depot
Johnson Ranch
Drinkwater Ranch
Kimberly Ranch
Strawberry Lake Camp
Ricco Ranch
Joaquin Miller Recreation Site
Canyon Mountain Recreation Site (historical)
Stevens Creek Recreation Site
Badger Creek Wilderness
Salmon-Huckleberry Wilderness
Black Wolf Meadow Creek
Bull Run Water Shed
Varney Creek Trail
Harriman Rural Fire Department
Pelican Fire Guard Station
Kodiac
Cold Springs Recreation Site
Crystal Springs Recreation Site
Crystal Spring Trailhead
Malone Springs Recreation Site
Little Crater Lake Recreation Site
Aspen Lake Cinder Pit
Barlow Creek Recreation Site
Paul Dennis Recreation Site
Camp Ten Recreation Site
Rock Creek Reservoir Work Center
Oneonta Gorge Botanical Area
Larch Mountain Recreation Site
Methodist Youth Camp
Triangle Lake Recreation Site
Lower Lake Recreation Site
Camp Sherman Recreation Site
Lake Creek Lodge
Jack Creek Recreation Site
House on the Metolius Resort
Head of Jack Creek
Diamond Crater
Digit Point Trailhead
Annie Creek Sno-Park
Sugarpine Mountain Lookout
Mazama Sheep Corral
Camas Reservoir
Cow Camp
Sherman Ranch
Lost Spring
Buck Spring Campground
Mills Upper Ranch
McCormack Ranch
Rickman Ranch
Puett Ranch (historical)
Miller Ranch
Sugar Creek Recreation Site
Cow Camp
Sugar Creek Spring
Powell Ranch
Paulina Ranger District
Cow Camp
Cow Camp
H Bernard Ranch (historical)
Mud Springs Recreation Site
Scab Spring
Frog Spring
North Entrance Station
North Crater Trailhead
Annie Creek Pit
Long Prairie Corral
McKinney Ranch
Thielsen Creek Recreation Site
Severance Ranch
Glenn Ranch
Abbott Creek Research Natural Area
Hyde Airstrip (historical)
Casey State Park
Silver Fork Gap Point of Interest
Dexter Ranch
Joe Fisher Ranch
Robertson Ranch
Bernard Ranch
Big Springs Recreation Site
Beaver Forest Service Station
Ihrig Ranch
Howard Ranch
Payne Ranch (historical)
Gage Range
Bandit Spring Safety Rest Area
Bootan Ranch
Walton Lake Recreation Site
Crystal Springs Organization Camp
Teaters Ranch
Mossy Rock Camp
Negus Ranch
Pine Creek Campground
Arrow Wood Camp (historical)
R Knox Ranch
Bull Run Research Natural Area
Union Creek Resort
National Creek Camp
Buckhead Trail Recreation Site
Big Bend Camp
Mount Stella Lookout Tower
Lookout Mountain Management Area
Ochoco Divide Research Area
Union Creek Recreation Site
Caritt Falls Recreation Site
Ashland Watershed
Oregon Cascades Recreation Area
Beaver Swamp Trailhead
Skookum Chuck Camp (historical)
Windy Camp
Middle Fork Ranger Station
Elliot Ranch
Isadore Ranch
Cow Camp Cabin
Ochoco National Forest Headquarters
Rainbow Campground
Emigrant Recreation Site
Gill Reservoir
Bluejay Spring Research Natural Area
Jenny Creek
Surveyor Mountain Recreation Site
Fish Lake Trailhead
Skimmerhorn Trailhead
Head of the River Recreation Site
Mount Scott Lookout
Lost Creek Recreation Site
Jackson Creek Recreation Site
Sweikert Ranch
Harris Park Recreation Site
Tollgate Chateau
Indian Spring
Trapper Spring
Blue Mountain Lutheran Bible Camp
Tollgate Work Center
South Umpqua Experimental Forest
Vermillion Bar Campground
Rayenoof Field (historical)
Moon Lake Shelter
Twin Lakes Recreation Site
Boulder Spring Trail
Pringle Falls Research Natural Area
Boyce Pond Well
Madras Control Tower
U P Water Tank (historical)
Diamond Lake Ranger Station
Morrow Ranch
Gates Ranch
Blue Lake Resort
West Fork Keeney Creek
East Fork Keeney Creek
Keeney Creek
Wet Horse Creek
Jones Trail
Hells Canyon Creek Recreation Site
Dug Bar Recreation Site
Ketchum Ranch
Winburn Ridge
West Fork Grouse Creek
Rogue Watershed
Rigdon District Ranger Office (historical)
Logger Butte Recreation Site
Greenwaters Park
Houston Ranch
Ashland Research Natural Area
Summer Lake Safety Rest Area
S D Harris Ranch
Lower Walker Quarry
Braymill Cinder Pit
Packsaddle Lookout
Devils Knob Camp
Threehorn Recreation Site
Paisley Ranger Station
Brattain Ranch
Marsters Spring Recreation Site
Rock Springs Campground
Great Basin Historical Marker
Buchanan Ranch
Big Rock Creek
Big Craggies Botanical Area
Ludlum House Recreation Site
McBride Recreation Site
Peavy Cabin Recreation Site
North Pine Rest Area
Balm Creek Reservoir Recreation Site
Summit Point Trailhead
HB Murray
Murray Reservoir Recreation Site
Unity Ranger Station
Duck Creek Reservoir
Milk Creek Glacier
Bend City Water Intake
Morris Ranch
Dixon Ranch
Van Guard Station
B S Well
Kelsay Valley Trailhead
Rosland Campground
Dehne Ranch
Chase Spring Administrative Study Plot
Hager Trail
Snow Bunny Lodge
Pioneer Woman's Grave
Trillium Lake Recreation Site
Devils Half Acre Meadow Recreation Site
Hurricane Creek Trailhead
Summit Lake Recreation Site
Old Wagon Road Historical Area
Buck Creek Trailhead
Wagon Road Trailhead
Tenderfoot Trailhead
Lick Creek Trailhead
Mahogany Corral
Marr Flat Cow Camp
North Fork Catherine Creek Recreation Site
North Fork Picnic Area
Mount Howard Gondola Recreation Site
McColly Trailhead
Harl Butte Lookout
North Fork of Middle Fork Imnaha River
Bearwallow Trailhead
Pilcher Creek Reservoir Recreation Site
Wolf Creek Reservoir Recreation Site
Joseph Grain Elevator
Chief Joseph Cemetery Recreation Site
Wallowa Lake Forest Service Station
Boy Scout Camp
Wallowa Lake Trailhead
Enterprise Magnetic Station
Black Lake Recreation Site
Hells Canyon National Recreation Area Ranger Station
Eagle Cap Ranger Station
Enterprise Forest Service Station
Little Creek Fish Weir Recreation Site
Cold Canyon
Warnock Corral Trailhead
Big Canyon Fish Weir Recreation Site
North Fork Gravel Pit
Corral Creek Ranch
Horse Creek Viewpoint
Hat Point Lookout Tower
Granny View Recreation Site
Freezeout Trailhead
Wallowa Forest Service Station
Jim Creek Ranch
Lillyville Trailhead
Cloud Cap-Tilly Jane Historic Area
Tilly Jane Recreation Site
Triangle Moraine
Kinnikinnick Recreation Site
Dog Fight Corral
Miller Ridge
Indian Rock Recreation Site (historical)
Pole Creek Ridge Trailhead
Mount Emily Sno-Park
Eureka Creek Cabin
Buckhorn Recreation Site
Kirkland Cabin
Two Pan Trailhead
Coal Docks
Bush Ranch
Officer Ranch
Bradley Ranch
P W Hyde Ranch
Hyde Ranch
H H Trowbridge Ranch
Tamarack Spring Camp
Horse Ranch
Geo Peyerl Ranch
Klamath County Dump
Special Trust Land
Corbell Cinder Pit
Minniece Creek
Johnny Creek
Whistler Recreation Site
Knob Creek
No Man Creek
Bunchgrass Meadows Shelter
Coffin Butte
Williams Forest Service Facility
Stuart Falls Camp
Lucky Camp
Chocolate Falls
Grouse Gap Shelter
Mount Ashland Recreation Site
East Eagle Trailhead
Copperfield Campground
Ferguson Recreation Site
Imnaha River Woods Development
Union Creek Trail
Tipsu Tyee Recreation Site
Harr Point Recreation Site
Bybee Meadow Trail
Latgawa Cove Recreation Site
Dutton Creek Trail
Rim Village Picnic Area
Lightening Spring Trail
Vigne Recreation Site
Flag Prairie Cow Camp
Blue Bucket Cow Camp
Little Malheur River Recreation Site
Breitenbush Lake Recreation Site
Olallie Meadow Recreation Site
Olallie Lake Recreation Site
Durbin Meadows
Iron Mountain
Ivy Station
Jefferson Ditch
Kernan Point
Long Creek
Long Creek
Lostine
Maple Knoll
Mill Race
Pierce Creek
Pierce Creek
Montague (historical)
Kirbros (historical)
KCBY-TV
Mehlhorn-Bassett Dam
Hampton Creek
Hemlock Lake
Grand Canyon of the Snake River
Bitterlick Creek
Huylers Spring
Adams Prairie
Sycan Capacitor Station
Spencer Creek
Umatilla County
South Fork Trout Creek
Separation Corrals Camp
Main Eagle Bridge Campground
Eagle Forks Recreation Site
Cold Springs
Lake Fork Recreation Site
Hat Point Recreation Site
Breitenbush
Koko Lake
Little Bowerman Lake
Flapper Springs
Lava Butte Geological Area
West Cultus Lake Recreation Site
North Twin Recreation Site
South Twin Recreation Site
North Davis Creek Recreation Site
Reservoir Recreation Site
Pop Lake
Little Pop Lake
North Pine Recreation Site
Keeney Camp Guard Station
Butler Mine
Reed Mine
Lynch Creek Forest Camp (historical)
Vermilion Forest Camp
Lower Twin Campground (historical)
Three Creek Lake Recreation Site
Trapper Meadow Camp (historical)
Antelope Reservoir Recreation Site
Double Cabin Recreation Site
Biggs Spring Recreation Site
Ochoco Recreation Site
Cougar Forest Camp
Crane Prairie
Little Cultus Lake Recreation Site
Rock Creek Campground
Rock Creek Recreation Site
McKay Creek Forest Camp
Cayuse Forest Camp
Elk Campground
County Creek
Trough Creek Campground
Tupper Corral
Twin Springs Reservoir
Divide Cabin
Bingham Prairie Campground
Schiedler Reservoir
Sand Prairie Recreation Site
Doris Ridge
Kelly Ridge
Hobo Creek Recreation Site
Green Rock Mine
Fairview Camp
Alder Spring Recreation Site
North Fork Silver Creek
Squaw Spring Corral
East Bay Recreation Site
Thompson Reservoir Recreation Site
Cline Clark Recreation Site
Gate Creek Forest Camp
T V Butte
Noisy Creek Forest Camp
Rock Knob
Camp 5
Marine Ridge
Pocher Creek
Wilson Ridge
Butler Ridge
Kingfisher Recreation Site
Chandler Airstrip (historical)
Piety Island Recreation Site
Upper Arm Recreation Site
Hoover Recreation Site
Big Huckleberry Butte
Round Lake Christian Camp
Round Lake Recreation Site
Link Creek Recreation Site
Tandy Bay Recreation Site
Allen Creek Horse Camp
Salt Creek Falls Recreation Site
Pebble Bay Recreation Site
Willamette Pass Ski Area
Shadow Bay Recreation Site
Gold Lake Recreation Site
Gold Lake Bog Research Natural Area
Trapper Creek Recreation Site
Malheur Ford Camp (historical)
Allingham Recreation Site
River Island Forest Camp (historical)
Smiling River Recreation Site
Ferndale Upper Range
Marshfield Range Channel
Entrance Range
Inside Range
Willamette Falls
Christie (historical)
Messinger Lower Range
Messinger Middle Range
Messinger Upper Range
Long Walk Island
Irrigon Lower Range
Irrigon Middle Range Channel
McNary Range Channel
Threemile Rapids (historical)
Cook Point Range Channel
Shaver Mooring
Hells Gate Channel Range B
Bingen Range Channel
Willow Lower Range
Morgan Channel
Bybee Ledge Channel
Duck Club Turn
Lady Island Channel and Upper Range
Washougal Lower Range
Washougal Upper Range
Gary Island Range
Reed Island Range
Tunnel Point Channel
North Fork Shoal
Warrendale Upper Range
Hamilton Island Reach
Warrendale Lower Range
Cape Horn Channel
Candiana Channel
Fashion Reef Lower Range
Multnomah Falls Bar
Multnomah Falls Upper Range
McGowans Channel
Upper Desdemona Shoal
Lower Desdemona Shoal
Tansy Point Turn and Range
Two Arches
Lower Jarvis Range
Jarvis Turn
Empire Range
North Bend Lower Range Channel
North Bend Range
North Bend Upper Range
Ferndale Lower Range
Salmon Harbor
Double Cove Point
Barretts Range Channel
Big Tree Campground
Lewis Camp
Alkali Camp
Wiley Camp
Rolling Grounds Camp
Fish Creek Campground
Camas Creek Campground
Whitehorse Falls Recreation Site
Camp Creek
Dog Prairie Shelter
Three Lakes Camp
Clear Creek Camp
Buck Camp
Prineville Camp (historical)
Muir Creek Falls
Haymaker Campground
Hurryon Camp
Log Camp
Mule Creek
East Fork Elk Creek
South Fork Eddington Creek
Cinnabar Gap
Corral Creek
Wayside Springs Forest Camp
Blue Jay Ridge
Stagnant Lake
Hidden Lake
Barren Lake
Grouse Lake
Fairview Camp
Rainbow Recreation Site
Armstrong Recreation Site
Carter Bridge Recreation Site
Cripple Creek Forest Camp (historical)
Linney Creek Recreation Site (historical)
Hideaway Lake Recreation Site
Oak Fork Recreation Site
Pine Point Recreation Site
Frazier Fork Campground
Lake Harriet Recreation Site
Woodruff Bridge Recreation Site
Dead Soldier Camp
Dead Soldier Meadow
Big Ben Campground (historical)
South Fork Recreation Site
Sumpter Creek Camp (historical)
Sheep Camp Glades
Shadow Falls Campground
Mazama Campground
Susan Creek Falls
Ranger Stone
Coverdale Recreation Site
Winterbottom Riffle
Blue Bay Recreation Site
Gorge Recreation Site
Cold Spring Recreation Site
Harris Reservoir
Lost Creek Cinder Pit
Pack Rat Reservoir
Champaigne Family Cemetery
Archambeaux Family Cemetery
Eddy Cemetery
Haines Cemetery
Lampa Creek Cemetery
Brack Cemetery
Garrett Cemetery
Doolittle Cemetery
Myrtle Creek Cemetery
Warner Grave
Wise Cemetery
Neal Cemetery
Waterman Cemetery
McClure Cemetery
Bryant Cemetery
Norris Family Cemetery
Lower Wolf Creek Cemetery
Placer Cemetery
Bear Creek
Stillwell Ditch
Ox Bow Bend
Louise Creek
Dead Cow Lake
Mill Creek
Oral Hull Picnic Area
Gibson Prairie Horse Camp
Sheridan Wayside State Park
Clay Hill Cemetery
Howell Spring
Reservoir Number Three (historical)
Dove Creek Campground
Aspen Reservoir
Hill Spring
Laycock Spring
Koehler Ranch
Gibb Spring
Randall Spring
Ferris Spring
Willow Springs
Lost Creek Reservoir
Station Spring
Mutiny Spring
Sproul Ranch
Dago Spring
Lake Creek Organization Camp
Road Gulch
Keeney Camp Spring
Beech Creek Summit
Shrier Spring
Raddue Spring
Cottonwood Spring
Phillips Ranch
Keerins Ranch
McHaley Cemetery
Prairie City Cemetery
Daniels Spring
Hamlin Boat Landing
Blue River Community Park
Terwilliger Hot Spring
Dry Gulch Reservoir
Horse Spring
Four Deer Reservoir
Boulder Spring
Lumsden Spring
West Bassout Reservoir
Neal Spring
Abbott Butte Lookout
Cedar Creek
Needle Rock Spring
Halls Point Lookout
White Point Lookout
Morgan Spring
Persist Ranch
Bassett Reservoir
Trail Creek
Stinkingwater Reservoir Number Three
Silvies Cemetery
Van Aspen Spring
Southworth Ranch
Biggs Ranch
Mule Spring
Sand Spring
Delta Recreation Site
Deer Camp Reservoir
Dead End Reservoir
Rocky Road Reservoir
Old Horton Mill
Silver Reservoir
Horse Spring Reservoir
East Horton Basin Reservoir
Sagadore Spring
Panel Spring Reservoir
Hillary Grade
Obrist Grade
Suicide Grade
Kershaw Creek
Smith Ridge
Horton Mill Reservoir
Winslow Canyon
Patrick Spring
Lyle Spring
Whiskey Spring
Big Flat Cemetery
Brook Creek
Nena
Deadman Spring
Deep Spring
Buck Spring
Hi Yu Spring
Allen Spring
Long Creek Reservoir
Willow Spring
Long Creek Cemetery
Burnt Mountain
Morgan Ranch
Spring Creek
Upper Bernard Creek Rapids
Lower Bernard Creek Rapids
Willow Creek Rapids
Rocky Point Rapids
Brush Creek Rapids
Cliff Mountain Rapids
Butler Bridge
Antelope Lookout Tower
Royal Purple Mine
Natural Bridge
Wolf Prairie
Devils Knob
Cow Horn Arch
Worlds Tallest Sugarpine
Eden Creek
Paradise Creek
Cougar Creek
Saddle Camp
Paradise Camp
Aiken Family Plot
River Bridge Recreation Site
Mammoth Pines Picnic Area (historical)
Takelma Gorge
Bull Bend Recreation Site
Wampus Campground
Round Swamp Campground
Stan H Spring
Haynesville Cemetery
Lorella Drain
Lorella Lateral
Williams Reservoir
Big Flat Airstrip (historical)
Frankton School (historical)
Mountain View Memorial Cemetery
Van Horn Butte
Panorama Point County Park
Hood River Valley High School
Wah Gwin Gwin Falls
Pine Grove Butte Cemetery
Powerdale Dam
Cedar Creek
Mid Columbia Agricultural Experiment Station
Windmaster Corner
Eliot Park
Jackson Park
Orchard Ridge Ditch
North Fork Hazel Hollow
Seven-and-a-Half Mile Campsite (historical)
Cedar Swamp Campsite (historical)
Buck Point Creek
Sunshine Rock
Blue Grouse Campsite
Wy'East Camp
Smokey Spring
Seven-and-a-Half Mile Camp (historical)
Lymp Reservoir
Kloshe Chuck Reservoir
Henry Creek Reservoir
Fern Creek
Pucci Glade
Swim (historical)
Swim Creek
Mud Springs
Lost Meadow
Prospect State Park
Barr Creek Falls
Scott Lake Recreation Site
Butte Spring
Hand Lake Shelter
Red Top Spring Helipond
Allan Creek
Collins Ridge
McReady Spring
Harris Reservoir
Coble Creek
Perdue (historical)
Diamond Rock
Rainville Cemetery
Callahan Meadows
Tiller Ranger Station
Tinhat Pond
Callahan Ridge
Three C Rock Recreation Site
Lake Creek
Joseph Reed Reservoir
Joseph Reed Dam
Dompier Creek Slide Area
Coffee Creek Cemetery
Corral Gulch
Dads Lake
Ruthton Point
Buehler Pond
Kent IOOF Cemetery
False Waterhole
One Crock Waterhole
Parachute Pond
Musser Waterhole
Dry Lake Waterhole
Webster Waterhole
Hollow Waterhole
Hidden Lake
Pearson Log Pond
Keystone Log Pond (historical)
Hillman Reservoir
Herbert Log Pond
Hiles Reservoir
Scott Pond
William D Bradley Cemetery
Pine Spring
Charles V Stanton Park
Pioneer Cemetery
Chicago Valley
Browns Valley
Stauffer Rim
Canyonville Cemetery
Herberts Pond Park
Canyonville County Park
Lawson Bar
Colvin Cemetery
Pistol River Log Pond
Evans Log Ponds
Henry Rock
Reels Springs
Jessie Applegate Historical Marker
Houston Reservoir Number One
Houston Reservoir Number Two
Houston Reservoir Number Three
Sherman Rim
Criterion Cemetery
Multnomah County Farm and Home (historical)
Oxbow (historical)
Coyote Butte
Spike Butte
Dog Lake
Cream Lake
Woodrow (historical)
Connley
Sprague Well
Gubser Well
Morehouse Lake Reservoir
Morehouse Lake
Three-Mile Corner
Thomas Well
Gauldin Well
South Beeler Well
Fort Rock Cemetery
Community Seeding Well
Windmill Lake
McCall Lake
Chalk Canyon Reservoir
L C Spring
Chalk Canyon
Adrian Place
Mickey Basin
Mickey Butte
Mickey Cabin (historical)
Ancient Lake
Calderwood Desert Well
Red Lookout Butte
Buckskin Reservoir Number 3
Buckskin Reservoir Number 2
Buckskin Spring
Big Sand Gap Spring
Big Sand Gap
Little Sand Gap
Sailor Jack Spring
Tule Springs
Brummit Creek
Burnt Ridge
Burnt Mountain
Cherry Creek Ridge
Sheeps Head
Luse Spring
Rogers Spring
Myrtle Tree Hole
Wee House Hole
Hewett Falls
McGee Ranch
Upper Canal Reservoir
Two Fork Reservoir
Long Canyon Reservoir
Rocky Hole Reservoir
On Top Waterhole
Griffen Waterhole
Tooney Waterhole
Mammoth Waterhole
Horseshoe Reservoir
Middle Walker Reservoir
Lower Walker Reservoir
Larrys Reservoir
Second Lake Reservoir
Twin Buttes
Rattlesnake Reservoir
Little Rattlesnake Reservoir
Lower Butler Reservoir
Middle Butler Reservoir
Dunn Reservoir
Wheatgrass Reservoir
Wheatgrass Lake
Spring Canyon Reservoir
Rocky Draw Reservoir
Rocky Draw
Sheep Mountain Reservoir
Harry Arnold Ranch
Poteet Spring
Old Egli Place
Hole in Ground
Spring Canyon
Wagontire Mountain Reservoir
Juniper Lake Reservoir
Pilot Butte
East Immigrant Waterhole
Lost Creek Well
Titus Creek
Sinks of Lost Creek
Pasture Lake
Lost Creek Reservoir
West Sheep Mountain Reservoir
Bradley Spring
Anderl Place
Anderl Lake
Manoeuver Road Reservoir
North Sheep Mountain Reservoir
Davis Spring
Chukar Park
Murphy Ditch
Schoolhouse Gulch
Madronna Creek
Reinhardt Reservoir
Lincoln Savage Reservoir
Meehan Slough
Small Reservoir
Willson Reservoir
Fifer Reservoir
Miller Spring
Old Pony Express Station (historical)
Swisher Ranch
Pedro Trails
Soldier Creek Trails
Owyhee Canyon Overlook
Lambing Camp Reservoir
Soldier Creek Vee
Rimrock Reservoir
Mud Flat Reservoir
Mud Flat Waterhole
Mud Flat
Scotts Ditch
Skull Cap Reservoir
Dead Horse Butte Reservoir
Halfway Reservoir
Iron Pit Reservoir
Upper Duncan Reservoir
Grassy Mountain Lake
Paus Reservoir
Eiguren Reservoir
Lower Deary Pasture
Deary Pasture Reservoir
Hogback
Skull Creek
Skull Creek Reservoir
East Hoodoo Butte Reservoir
Defeat Butte Reservoir
Defeat Lake Reservoir
Hoodoo Butte Reservoir
North Hoodoo Butte Reservoir
Defeat Ridge
Black Snake Reservoir
East Toppin Creek Reservoir
Little Lake
Mustang Lake Reservoir
Mustang Lake
South Fork Toppin Creek
Old Stoney Corral
Stoney Corral Ridge
Lower Wildhorse Reservoir
Wildhorse Reservoir
Stoney Corral
Deep Draw Reservoir
Little Louse Canyon Reservoir
Banana Lake
East Black Butte Reservoir
North Lookout Butte Reservoir
Lookout Butte Reservoir
Napoleon Reservoir
Subsoiler Reservoir
Whitehorse Creek
Whitehorse Reservoir
Whitehorse Creek Reservoir
Long Canyon
Long Canyon Reservoir Number Two
Long Canyon Reservoir Number One
Three Forks Rim Reservoir
Three Forks Reservoir
Porcupine Canyon
Warm Springs Canyon
Porcupine Reservoir
Lone Tree Reservoir
Military Grade
Three Forks Dome
Squaw Flat Reservoir Number Two
Chicago Pond
Chicago Valley Well
Bull Lake Waterhole
Browns Valley Well
Little Sagehen Waterhole
Sagehen Waterhole
Moonlight Butte
McCarthy Ridge Reservoir
Tub Mountain Reservoir
Redsull Well
Pueblo Mountains Wilderness Study Area
Catlow Creek
Antelope Creek
Spring Creek
Snake Den Butte
Trout Creek Ranch
Little Butte Well
Leonard (historical)
Bedsprings Flat Reservoir
Hayward Spring
Mohawk Community Church Cemetery
Antelope Well
Tobiason Reservoir
Spalding Reservoir
Blow Mud Reservoir
Jack Reservoir
Mud Reservoir
Gibson Lake
Slice Reservoir
Case Reservoirs
Goffrier Pond
Pole Creek Spring
Buck Spring
Fort Stevens Cemetery
Camp Rilea
Farley Hills
Short Low Ditch
Daugherty Family Cemetery
Bailey Reservoir
Lasells D Stewart County Park
Nyssa Bench
Perkins Slough
Blue Lake Slough
Independent Order of Odd Fellows Cemetery
Masonic Cemetery
Greenwood Landing County Park
Leaburg Landing County Park
Lee (historical)
Sky Ranch
Clem Cemetery
Grove Elementary School
Rothrock Landing Strip (historical)
Woodpecker Landing Strip (historical)
Matheny Bar
Union Bar
Henry Hill Elementary School
Henry Hill Park
Pioneer Park
Central High School
Sherman Junior - Senior High School
Long
Goering Ranches / Crocheta Airport Estates
Threemile Ridge
Burnt Ridge
Sesti Tgawaals Wildlife Area
Burnett Cemetery
Engles and Worth Log Pond
Myrtle Creek Pioneer Cemetery
Myrtle Creek IOOF Cemetery
Goose Creek
Oliver Spring
Hawkins Park
Anderson Park
D Reservoir
Mills Butte
Hudson Cemetery
Walls Lake Reservoir
Dry Creek
The Flats
Twelvemile Hill Grade
Twelvemile Ridge
Twelvemile Ranch
Crooked Creek Range
Duck Creek
Lower Willow Creek Waterhole
Twin Buttes
Coyote Meadows
Coyote Meadows Well
Twin Springs
Warm Spring
Hot Spring
Three Man Butte
Buckskin Reservoir Number Four
Spring Creek
Lower Roux Place
Hall Ditch
Lower Mitchell Cemetery
Cougar Rock
North Fork Trout Creek
Trout Creek
Miners Flat
Soda Spring
Henshaw Spring
O'Henry Reservoir
Pitt Butte
Colpitts Butte
Soda Table
Smith Basin
Delore Spring
Long Spring
Weberg Butte
Weberg Ranch
Suplee Hot Spring
Davin Spring
Gollum Reservoir
Angell Butte
Forbes Butte
Axtell Gap
Halfway Waterhole
Stump Waterhole
Scareoff Point
Oberg Ridge
Yreka Rim
Wade Spring
Upper Coyote Reservoir
Lower Coyote Reservoir
Coyote Spring
Brennan Ranch
Trail Basin
Brennan Reservoir
Logan Reservoir
Freezeout Reservoir
Saddle Butte
Bradford Ridge
Freezeout Ridge
Doe Spring
Gravelly Flat Reservoir
Three Pines Reservoir
O'Keefe Reservoir
Rough Creek Reservoir
Roadside Reservoir
Morris Meadows
Trails End Reservoir
McIntosh Ranch
Turnpike Reservoir
Palmer Reservoir
Middle Bronco Reservoir
Upper Bronco Reservoir
Bronco Reservoir
Humphrey Ranch
Duck Puddle Reservoir
Stump Creek Reservoir
Cold Spring
Palmer Ranch
Pine Tree Reservoir
Monroe Draw
Cold Spring Guard Station Landing Field (historical)
Basin Spring
Brummer Springs
Cherry Spring
Swamp Creek
Telephone Springs
Mud Spring
Mud Spring Canyon
Partnership Reservoir
Hole-in-the-Ground Reservoir
Little Juniper Reservoir
Lower Falls
Rough Canyon Creek
Mud Spring
Whitney Reservoir
Section Eight Reservoir
Cox Reservoir
Mercury Creek
Gerow Butte Lookout Tower
Gill Ditch
Lucky Reservoir
Hope Reservoir
Shovel Reservoir
Hellebore Spring
Coyote Spring
Gibson Spring
Sunny Slope Springs
Knox Spring
Ritch-Fayne Reservoir
X X Ridge
Sartain Ranch
Salem Ridge
Waucoma Park
Graham Gulch
Bundy Bridge
Division Reservoir
Dahlgren Rim
Laughlin Table
Stockade Point
Palmer Ditch
Little Bear Creek
Bob Spring
Bellworm Canyon
Rager Spring
Boundary Reservoir
Heisler Reservoir Number Two
Heisler Reservoir Number One
Ashley Ridge
Telephone Spring
Thompson Reservoir
Treichel Ridge
Christiansen Lake
Rock Creek
Claypool Ridge
Coggins Flat
Moccasin Ridge
Minifie Ranch
Minifie Ridge
Sheepshooter Ridge
Rager Airstrip (historical)
Rattlesnake Butte
Durgan Ranch
Logan Ridge
Widow Spring
Marshy Reservoir
Mud Spring
Elkins Butte
Allyn Draw
Laughlin Ranch
Lister Ranch
Myers Ranch
Cordella Rim
Noble Well
Palmer Reservoir
Dorschied Butte
Bear Butte Reservoir
Hawk Reservoir
Rock Spring Reservoir
Black Stump Creek
Birdsong Butte
Congleton Ranch
Remington Ridge
Roundtree Lake
Ferian Ranch
Faulkner Butte
Big Rattlesnake Butte
Upper Pocket
Geodetic Reservoir
Ruby Butte
Antelope Spring
Henry Rim
Lower Pocket
Mills Reservoir
Shoun Reservoir
Lava Point Spring
Sheep Rock Reservoir
Federal Spring
Old Faithful Reservoir
Gate One Reservoir
Lone Pine Spring
Oscar Canyon
Windmill Pond
Tyler Lake
Double O Flat
Derrick Lake
Double O Station
Jewel Waterhole
Smokey Waterhole
Bourbon Waterhole
Geyser Waterhole
Viv Waterhole
Best Waterhole
Dragon Rock
Elk Butte Camp
Wallace Creek
Williams Lake
Shortridge Park
Pine Meadows Campground
Lakeside Park
Primitive Campground
Jake Lakes
Thumbtack Reservoir
Windmill Flat
Porkchop Lake
Sandy Lake
Magpie Butte
Westlake Waterhole
Boston Sink
Ryegrass Reservoir
Coffee Creek
Eowyn Reservoir
Little Lake Waterhole
Speck Lake
Coffee Lake
Hardin Ranch
Long Hollow Dam
Long Hollow Reservoir
Pacific Power & Light Substation
Lonely Reservoir
Little Tank Canyon
Horsehead Reservoir
North Desert Waterhole Number Eleven
Three Forks Waterhole
Cogans Waterhole
Hunters Reservoir
Smokeout Creek
Sandy Bed Reservoir
Hutton Waterhole
Little Links Lake
Links Lake
Little Juniper Well
Bend Reservoir
Bunchgrass Reservoir
McDaniels Cabin
Cabin Waterhole
Five Corners Reservoir
Jerrys Homestead Reservoir
Southside Spring
Smoke Out Canyon
Deadhorse Pass Reservoir
Stovepipe Reservoir
Little Windy Pass
Hamilton Ranch
Blue Mountain Basin Reservoir Number Two
Blue Mountain Basin Reservoir
Achabal Spring
West Blue Reservoir
Twin Reservoirs
Backside Reservoir
Diversion Ditch Reservoir
Oregon Canyon Reservoir Number Two
Oregon Canyon Reservoir
Dinky Reservoir
Big Brush Reservoir
Blue Mountain Basin
Twelvemile Summit
Ditch Spring
Bog Hole Reservoir
Steens View Reservoir
Trout Creek School (historical)
Boney Spring
Camp C F Smith (historical)
Little Antelope Creek
Dry Creek Bench
Wagon Draw
Brandts Waterhole
Little Tank
Wolter Lake
Stormy Reservoir
Linahan Lake
North Gap Waterhole
Papoose Lake
Lone Tree Reservoir
Yellowstone Lake
Evening Lake
China Lake
Blowhole Lake
Piersol Well
Barnyard Spring
Basque Spring
Hibbard Spring
Ross Spring
Antelope Springs
Holloway Ditch
Red Mountain
Red Mountain Spring
Oriana Reservoir
Table Mountain
Grassy Basin
Als Canyon
Earnest Bridge
Cherry Spring
Windy Pass
Double O Elementary School
Rock Island
Trail Canyon
Schoolhouse Hill
Cherry Spring
Dry Creek Reservoir
Miracle Reservoir
Green Pond
Bench Spring
Buck Spring
Tin Trough Spring
Fish Reservoir
Twelvemile Reservoir
Frenchys Reservoir
Side Spring
Sweeney Ranch
Reed Landing Strip (historical)
South Mud Spring
Death Trap
Mahogany Spring
Sheep Corral Spring
Doolittle Spring
Doolittle Camp
Horse Spring
Cottonwood Spring
Twin Peaks
Rodeo Spring
Ralph Camp Spring
Cottonwood Creek
Juniper Spring
Jug Spring
Whitehorse Spring
Snowberry Reservoir
Antelope Valley
Cold Spring
Spreader Reservoir
Logger Waterhole
Cottonwood Creek Reservoir
Mendi Suri
Bretz Mine
Oregon Canyon Mountains
Schoolhouse Hill Spring
Hawkins Spring
Meadow Spring
Parks Dam
Deer Park
Gin Basin Reservoir
Wilson Creek Park
London
Black Butte
Guidottie Reservoir
Shale City Reservoirs
Mitchell Reservoir
Price Creek Reservoir
Bunker Hill Mine (historical)
Bunker Hill
Chezik Spring
Sigsby Spring
Bowron Gulch
Archie Gulch
Brainard Creek
Colliver Springs
Kruse Ponds
Brodie Gulch
Independent Order of Odd Fellows Cemetery
Belfast Mine
Englewood Mine
Rock Fort
Barnes Cabin (historical)
Ted Glover Spring
Philling-McFadden Ditch
Buck Pasture
Junction Springs
Waller Reservoir Number Two
Waller Reservoir Number One
Crowcamp Hills
Rebel Hill
Canyon City Reservoir
Town Gulch
San Juan Log Ponds
Luce Ditch
Alice Creek
Azalea City Park
Bagby Hot Springs Guard Station
Bagby Trail
Baty Butte
Baty Silver King Trail
Betty Creek
Blister Creek
Calapooya Mountains
Campers Flat Recreation Site
Doris Creek
East Davis Lake Recreation Site
East Gold Creek
East Mountain Trail
Fish Creek
Hot Springs Fork
Hugh Creek
Lost Creek
Lost Creek Meadow
Molalla Trail
Nohorn Creek
Nohorn Trail
Ora Creek
Pal Creek
Pansy Creek
Perry Creek
Pin Creek
Rock Creek
Shower Creek
Skin Creek
Skookum Lake
South Fork Mountain Trail
Spray Creek
Stroupe Creek
Thunder Creek
Thunder Mountain
Umatilla River
Whetstone Creek
Whetstone Trail
Whobrey Mountain
Joyce Lake
Pegleg Falls Recreation Site
Pegleg Falls
Worsted Creek
Skookum Lake Campground
Roads End Camp
Ballston County Park
Brigittine Monastery
Huddleston Pond Park
Stuart Grenfell County Park
Buell County Park
Oaken Hills Memorial Park
Garden Spot Park
Fort Yamhill State Park
Terry Park
Wascher Elementary School
Alderman Park
Dayton Grade School
Dayton Landing County Park
Patton Middle School
Chemeketa Community College
Newby Elementary School
Crabtree Park
Billick/Dundee School Park
Independent Order of Odd Fellows Cemetery
Tarrybrooke Park
Harleman Park
Talbot Park (historical)
Alpine Park
Joseph Gale Park
Bard Park
Water Park
Lincoln Park
Hazel Sills Park
Sunset Park
Forest Glen Park
Northridge Park
Gales Creek Elementary School
Forest Grove High School
Scoggins Creek Picnic Area (historical)
Carlton Elementary School
Wennerberg Park
Upper City Park
Airport Park
Angella Park (historical)
Carlson Park (historical)
Crestwood Park (historical)
Heather Glen Park
James Park
Jandina Park
Joe Dancer Park
Kiwanis Marine Park
McMinnville City Park
McMinnville High School
Quarry Park (historical)
Tall Oaks Park (historical)
Tice Park
Westvale Park
Wortman Park
Bethel Community Church
Faulconer - Chapman School
Faulconer School (historical)
Sunset Grove Golf Course
Lake Labish Ditch
Mountaindale School (historical)
Amity Hills
Athey Canyon
Ayers Creek
Baker Creek
Balm Grove
Banks
Beaver Creek
Berry Creek
Brunswick Canyon
Bryan Creek
Buck Mountain Ranch (historical)
Buxton
Camp Mountaindale
Cape Horn
Carpenter Creek
Cedar Canyon
Chehalem Valley
Claggett Creek
Coffee Island Bar
Coffee Chute
Crowley Creek
Cummings Creek
Davies Junction
Deer Creek
Denny Creek
Lousignont Canal
Duke Landing
Durettes Landing
Eagle Peak
Eagle Point
East Creek
East Fork Dairy Creek
Erratic Rock State Park
Fairfield
Feasters Rocks
Fern Hill
Forest Dale School (historical)
Forest View Cemetery
Fort Lane (historical)
Gales Peak
Garrigus Creek
Gaston
Gopher Valley
Gulf Canyon
Gumm Creek
Hares Canyon
Hawn Creek
Hayward
Hill Creek
Hillside
Jerusalem Hill
Kansas City
Lafayette
Lafayette Cemetery
Lake View School (historical)
Laurel Quarry (historical)
Little Beaver Creek
Little Bend Park (historical)
Lone Tree Bar
Lower Martine Bar
Lower Simon Bar
Manning
McCall Bar
McCloskie Bar
McKay Creek
Meacham Corner
Mercer Creek
Mill Creek
Mountain Top School (historical)
Mountaindale Church
Murtaugh Creek
O'Neil Creek
Orchard View
Palmer Creek
Pleasantdale
Puddy Gulch
Pumpkin Ridge
Red Hills of Dundee
Ribbon Ridge School (historical)
Mount Richmond
Roberts School (historical)
Robinson Creek
Rock Creek
Roundy Creek
Sadd Creek
Delphian School
Scoggins Creek
Slide Mountain
Snaggy Bend Bar
Snooseville Corner
Spring Hill
Spring Hill School (historical)
Spring Valley Creek
Staleys Junction
Strassel
Tolke Canyon
Tualatin Mountains
Tualatin River
Upper Martine Bar
Upper Simon Bar
Valley View School (historical)
Walker Creek
Wall Creek
Wapato (historical)
Wapato Lake Bed
Watts
West Fork Dairy Creek
Weston Landing
Wheatland Bar
Wheatland Dam (historical)
Wheatland Ferry
Whites Landing
Wildcat Mountain
Willamette River
Williams Creek
Windsor Island
Windsor Island Reach
Woods Landing
Centerville (historical)
Harris Creek
Guthrie Reservoir
South Yamhill (historical)
Schuetze Reservoir
Brookside Cemetery
O'Dell Cemetery
Grand Island Junction
Feldman Reservoir
Hussey Cemetery
Buck Hollow Cemetery
Gopher (historical)
Darrow Chute
Lafayette Pioneer Cemetery
West Chehalem (historical)
Kunz Reservoir
Hillside Cemetery
KWAY-AM
Kauer Reservoir
Chadwick Airport
Little White Salmon Range Channel
Shaw Creek
Fort Smith (historical)
Fort Lamerick (historical)
Helitack Base
Low Line Ditch
Barnhardy
Henry Hagg Lake
Meengs Canyon
Mohawk
Sheeplick Draw
Still (historical)
Aaron Mercer Reservoir
Acton Gulch
Alder Lake
Swan Hill
Anderson Creek
Andy Creek
Annie Creek
Arcadia School (historical)
Mount Ashland
Aspen Butte
Clatsop Community College
Astoria Reservoir
Alton Baker City Park
Bald Mountain
Barklow Mountain Campground
Barry Reservoir
Bartrums Rock
Beal Creek
Bear Creek
Bear Flat
Bear Wallow Springs
Belknap Spring
Biddle (historical)
Big Eddy
Big Rackheap Creek
Bird Rocks
Black Butte Swamp
Blann Meadow
Bloucher (historical)
Bluebird Mine
Bluebird Mine
Boardman Oasis Roadside Rest (historical)
Boner Spring
Booneville Channel
Booneville Slough
Boulder Creek
Boulder Creek
Bradbury Slough
Bridlemile
Brophy Hill
Brogan Hill Summit
Brown Creek
Browntown (historical)
Browntown
Brushy Bar
Bull Creek
Bull Mountain
Bull Prairie Guard Station (historical)
Bus Point
Butcher Point
Butteville
Cache Creek
Cache Creek
Cache Creek Toll Station
Calapooia Middle School
Jim Creek
Camp Pioneer
Cape Perpetua Special Interest Area
Caviatta Ridge
Cedar Grove Church
Saint Charles Medical Center Redmond
Cerro Gordo
Almasie Creek
Clarkes
Cliffs Camp
Clifton
Cline Falls
Cloudcap
Cold Spring Trail
Cold Springs
Coleman Rim
Coleman Rim
Columbia Slough
Conundrum Creek
Conundrum Creek
Cooks Chasm
Corless Reservoir
Cottage Grove Lake
Cottonwood Camp
Cougar Dam
Council Crest
Cow Hollow
Coyote Creek
Cranston Ditch
Crescent Lake
Creston
Crooks
Crowfoot
Currier Guard Station
Cyclone Reservoir
Dairy Creek Campground (historical)
Dairy Creek Campground (historical)
Damewood Creek
De Moss Canyon
De Moss Springs
Hatchery Creek
Deep Lake
Deep Lake
Deer Creek
Deer Creek
Devils Garden
Devils Lake
Dexter Siding
Diamond Hill
Diamond Lake Guard Station
Lord Island
Dickey Creek
Dimple Hill
Dolph
Don Lake
Dork Canal
Dorrance Meadow
Drews Creek Slough
Drews Gap
Drews Gap Summit
Drip Spring
Drip Spring
Dry Run
Eagle Camp
East Lateral
Eels Ridge
Elliott Creek
Erwin Ditch
Evergreen Cemetery
Fall Creek
Fectley Reservoir
Freeman Dry Camp
Fiddler Mountain
Fire Springs Trail
First Water Gulch
First Water Gulch
Fish Creek
Fitzwater Gulch
Ritter Butte Summit
Foley Ridge
Foley Spring
Foley Springs
Svensen Pioneer Cemetery
Fort Stevens State Park
Fox Valley
Fox Valley
Free Bridge
Fremont National Forest
French Gulch
French Gulch
Fredenburg Ranch
Frissell Point
Frog Lake
Fulton City Park
Furnish Ditch
Gage Creek
Grand Army of the Republic Cemetery
Gerdine Butte
Garret Creek
Gerry Mountain
Gladtidings
Gordon Creek
Gordon Hollow
Grabenhorst Corner
Grand Island
Granger
Grant Canyon
Grant Hill
Grassy Island
Grassy Island
Green Mountain Ridge
Greenwood Butte
Guano Lake
Haflinger Creek
Haggard Mine
Hall Ridge
Hall Ridge
Hardesty Trail
Hardman IOOF Cemetery
Harpold Dam
Harpold Reservoir
Lake Harriet
Haskin Butte
Heceta Head
Heisler Station
Helen Lake
Helm Canyon
Hi Desert Ski Area (historical)
Hill Military Academy (historical)
Hillcrest Creek
Hills Creek Dam
Hillis Peak
Hoquarten Slough
Horning Gap
Horseshoe Island
Hosmer Lake
Hull Creek
Ironside Mine
Jacques Creek
Jefferson City Park
Johnnie Springs
Jonesboro (historical)
Judson Rocks
Jump-off Joe Mountain
Jumpoff Joe Peak
Juniper Gap
Juniper
Keene Creek
Kinzua (historical)
Kirby Creek
Kokostick Butte
Kramer Point
Ladd Circle
Lang Forest State Park Wayside (historical)
Lava
Lava Cast Forest
Lava River Cave Recreation Site
Layton Mine
Le Page Park
Lebanon Dam
Lee Woods Spring
Lilleas
Limpy Prairie
Lincoln City
Little Creek
Little Creek
Little Humbug Creek
Logan Creek
Looking Glass (historical)
Lookout Point
Lost Cabin Creek
Lost Canyon
Lost Creek
Lost Prairie Rock
Lousignont Creek
Love Ditch
Low Line Ditch
Iowa Hill
Iowa Hill School (historical)
Iowa Slough
Lowe Creek Trail
Lower Burnt Spring
Luce Creek
Mahon Reservoir
Marion Mountain
Marion Peak
Marks Slough
Marsh Island Creek
Mascall Trail
McAlister Slough
McBee Slough
McCarty Canyon
McCarty Gulch
McCullough Memorial Bridge
McFadden Marsh
McIntyre Creek
McIntyre Lookout
McIntyre Reservoir
McIntyre Reservoir Number Two
McKenzie River Park
McLeod Guard Station
Meadow Camp
Meadow Camp
Medco Pond
Meditation Point Recreation Site
Magerly Gulch
Melix Spring
Meyer Creek
Miami Cove
Four Corners
Miles Lake
Mill Hill
Miller Spring
Minaker Island
Minam Summit
Mission Bar
Mohawk Post (historical)
Mosquito Lake
Morning Creek
Morning Star Mine
Motanic
Mount Hood Flat
Mount Bailey
Mud Creek Ridge
Mud Springs
Mulkey Creek
Necanicum Guard Station
Neptune State Park
Neverstill
No-See-Em Creek
North Dickey Peak
North Fork Recreation Site
North Fork Siuslaw River
North Jones Trail
North Table Mountain
North Temperance Creek
O'Hara Creek
O'Keefe Creek
Obsidian Cliffs
Ochoco Mine
Odell Lake
Old Maids Canyon
Olalla Slough
Ontario Heights
Oregon Dunes National Recreation Area
Orofino Mine
Overlook City Park
PYX Mine
Paradise Creek
Parallel Spring
Parish Cabin Recreation Site
Perkins Ditch
Mount Peter
Phoca Rock
Piety Knob
Pigeon Butte
Pillar Rock Lower Range
Pine Creek
Pole Creek
Pony Creek
Pony Slough
Portland Meadows
P O Creek
P O Saddle
Powell Butte
Pringle Falls Experimental Forest
Prospect Guard Station
Quarter Butte
Rambo Creek
Rainbow End Lake
Raleigh Hills
Rail Gulch
Rancherie Creek
Randolph
Rattlesnake Creek
Rector
Red Butte Trail
Red Hill
Red Mountain
Reed Creek
Reed Creek
Reilly Meadows
Rice Hill
Rice Hill
Sawyer Park
Rock Creek
Rock Creek
Rock Creek Recreation Site
Rock Gulch
Rock Gulch
Rockville
Rocky Peak
Rodman Rim
Rooster Rock State Park
Round Lake
Round Meadow
Round Meadow
Round Valley Reservoir
Rujada Point
Ryegrass Reservoir
Sagebrush Point
Saint Louis
Saint Mary's Cemetery
Archbishop Howard School
Smith Creek
Scholls
Little Searcy Creek
Searcy Creek
Shady Cove
Sheaville
Sheep Hill
Sheep Hill
Sheep Lake
Sheep Lake
Sheepshead Mountains
Sherrard Point
Siltcoos Lake
Silver Falls State Park
Simax Group Campground
Siskiyou Gap
Skeeters Swamp
Skipanon Slough
Snow Lakes
Snow Lakes
Wallowa Lake State Park
Solomon Creek
Sonny (historical)
South Ditch
South Fork Gate Creek
South Fork Trail
South Limpy Prairie
South Matthieu Lake
Spores Creek
Spores Point
Springer Ditch
tíkem Creek
Téemux Creek
Starvation Rock
Steamboat Point
Strawberry Spring
Substitute Point
Summit Springs
Summit Springs
Sundial Beach
Sunflower Flat
Sunflower Flat
Swan Island
Swan Lake Rim
Taft
Tartar Gulch
The Pinnacles
Tillamook Rock
Timber Gulch
Timberline Lodge
Tison Trail
Tongue Point Naval Base (historical)
Trailover Creek
Camp Kuratli
Oregon Health Sciences University
Upper Table Rock
David Ridge
Valsetz (historical)
Valsetz Lake (historical)
Vanderhoof Canyon
Vey Ranch
Wagner Butte
Wagonblast Canyon
Wagontire Mountain
Wahtum Lake Guard Station (historical)
Wakefield (historical)
Walcott Tunnel
Walker Creek
Walker Creek
Walker Point
Walker Point
Walrus Rocks
Wauna Range
West Birch Creek
West Lake
West Point
West Point Cemetery
Whalehead Creek
Whalehead Island
Whisky Creek
Wilcox Ditch
Williamson Creek
Willow Creek
Willow Creek
Willow Spring Basin
Wire Corral Canyon
Jobe Canyon
Yachats Memorial Park Cemetery
Yachats Mountain
Yachats Ocean Road State Natural Site
Yachats State Recreation Area
Yaquina John Point
Quinton
McDow Creek
Brushy Creek
Needham Gulch
Twin Buttes
Wallowa Falls
Lapover Meadows
Blue Mountain Spring
Pursel Spring
The Black Pines
Eleven Spring
Shevlin (historical)
Jackson Lake
I N Young Ditch
Cundiff Slough
Howell Ditch
Packsaddle Spring
Purvis Ponds
Gant Spring
Huckleberry Spring
Pinical Spring
Soap Flat
Joseph Warm Spring
Upper Cochran Rapids
Lower Cochran Rapids
Dry Creek Rapids
Powell Valley Butte
Todd Lake Recreation Site
Little Houston Lake
Grimes Flat
Shotgun Canyon
Seekseequa Cemetery - 2
Seekseequa Cemetery - 1
Clear Creek
Fort Dalles (historical)
Powerdale (historical)
Holstein (historical)
Juniper Creek
Meadow Creek
Winan Spring
Viento (historical)
Celilo Indian Cemetery
Celilo Indian Cemetery
Bald Mountain Ridge
Weston Pond
Spanish Gulch Cemetery
Erickson Ditch
Cottonwood Spring
Wasco Methodist Cemetery
De Moss Cemetery
Kerr Creek
Cold Springs Diversion Dam
North Island
Cooper Mountain Cemetery
Marylhurst
China Hill
Shevlin (historical)
Cameron (historical)
Spray Cemetery
Crawford Creek
Goodwin Gulch
Home Hollow Creek
Domby Ditch
Cooper Mountain Evangelical Cemetery
Rivergate
Clackamette Cove
Timothy Lake
Molalla River State Park
Horning Reservoir
Seufert County Park
Owyhee Bench
Tamarack Springs
Suver Junction
Sigfredson County Park
North Glass Butte Reservoir Number Two
North Glass Butte Reservoir
Rhea (historical)
Goltra (historical)
Lowson (historical)
Short Creek
Moore Reservoir
Lower Dead Ox Flat
Sherar Grade (historical)
North Branch Swanson Creek
Mystery Creek
Elliott Slough
Cabell Marsh
Wroten Reservoir 1
Wroten Reservoir 2
Crescent Lake Reservoir
Lake Henry
Packard Creek Recreation Site
Dotyville (historical)
Mabel Cemetery
Dorena Dam
Carmen Reservoir
Carmen Diversion Dam
Foster Creek
Lake Neskowin
Camp Baldwin Lake
Annie Creek
Bonner Mountain
National Forest Land Park
Corn Creek
Foster Dam
Wigglesworth Spring
Elmer Ditch
Walker Union Church Cemetery
Bates Pond
Cutsforth Dam
Forest Spring
Zinter Pond
Hall Hill
Hacheney Spring
Lun (historical)
Hotchkiss Ditch
State Game Reservoir Number Two
Vistillas (historical)
Horseheaven
Ironside Butte
Taylor Bridge
Kennedy Gulch
Fort Basin Springs
Bilyeu Cemetery
Flett Cemetery
Ukiah Cemetery
Weissenfluh Reservoir
Peavy Creek
Go Spring
Lick Spring
Trent Creek
Shoemaker Ditch
Carroll Rim
Hoover Creek Reservoir
Ballew Reservoir
Fish Creek Waterhole Number Forty-four
Luce Ditch
Fish Creek Waterhole Number Forty
Fish Creek Waterhole Number Forty-seven
KBOO-FM
KBVR-FM
Monument Flat
KRRC-FM
KSKD-FM
KSKD-FM
KTEC - FM
KTIL-FM
KTIL-FM
KWAX-FM
KWAX-FM
KXBQ-FM
KXBQ-FM
KYNG-FM
KEZI-TV
KOAP-TV
KOTI-TV
KOTI-TV
KCMX-FM
KCMX-FM
KEPO-FM
KICE-FM
KLLB-FM
KLOO-FM
KMHD-FM
KPNW-FM
Wakefield Waterhole
KPDQ-AM
KQDQ-AM
KQDQ-AM
KRNS-AM
KSRV - AM
KSWB - AM
KTIL - AM
KUIK-AM
KUIK-AM
KUMA - AM
KWIL- AM
KWIP-AM
KWJJ-AM
KWVR-AM
KXL-AM
KGAY-AM
KGAY-AM
KGRL-AM
KGRV-AM
KGW - AM
KLAD-AM
KLAD - AM
KLIQ-AM
KLOO-AM
KMED-AM
KNPT-AM
KNPT-AM
KOAC - AM
KODL - AM
KOHU - AM
KAGI-AM
KAGO - AM
KASH-AM
KAST - AM
KBND-AM
KBND-AM
KBPS-AM
KCMX-AM
KCYX-AM
KDUN-AM
KYJC-AM
KYNG - AM
KYTE-AM
KYXI-AM
Keene Creek Dam
Mountain Sheep Dam
Corless Dam
Scott Dam
Dexter Dam
Blue River Dam
Green Peter Dam
Ruby Dam
Benson Reservoir
Salt Lick Reservoir
Scott Dam
Becker Reservoir
Veterans Reservoir
Sun Studs Log Pond
Munn Reservoir
Pine Creek Reservoir
Pringle Flat Dam
Pierce Reservoir
Chenoweth Airpark Terminal
Collins Landing Strip (historical)
Collins Landing Strip
Cottage Grove State Airport
Woolfolk Reservoir
Indian Lake Reservoir
Yankee Creek Dam
Grizzly Creek Dam Number 2
Bryson Spring
Briggs Airport (historical)
Cape Blanco State Airport
Central Oregon District Hospital Helipad
City of Portland Number 1 Dam
City of Portland Number 3 Dam
City of Portland Number 4 Dam
City of Portland Number 5 Dam
City of Portland Number 6 Dam
Mountain Springs Ranch Reservoir
Mountain Springs Ranch Dam
Rohde Reservoir
Graham Reservoir
Pierson Reservoir
Kay Reservoir
Hawn Creek Reservoir
Keene Dam
Walker Reservoir
Dober Reservoir
Hickory Hill Farm Reservoir
Kuehne Reservoir
Unger Reservoir
North Fork Dam
River Mill Dam
Trail Bridge Reservoir
Helms Reservoir
Grants Pass Airport
Starvout Creek Airport (historical)
Teufels Farm Strip (historical)
Pole Creek
Arrastra Gulch
Bully Creek Reservoir
Antelope Cemetery
Cracker City (historical)
Tranquil Cove Recreation Site
Axehandle (historical)
Antelope Cemetery
Jim Creek
Hines Mill Pond (historical)
Honeymoon Creek
Jimmy Creek
Fall Creek Lake
Final Falls
Frustration Falls
Friday Creek
Gardner Creek
Galice Riffle
Grave Creek Riffle
Green Peter Lake
Hideaway Falls
Hemlock Falls
Hills Creek Lake
Howard Creek Chute
Hymes Creek
Inspiration Point
Johns Riffle
Kelsey Falls (historical)
Little Windy Riffle
Long Gulch Riffle
Lower Black Bar Falls
Lost Creek Lake
Frank Fulton Canyon
Foster Lake
Green Acres
Howard Prairie Lake
Jensen Spring
Klamath Mountains
Kilts
Lonoley
Sid Luce Reservoir
Big Eddy (historical)
Corbin Creek
Coopey Creek
Depoe Bay
Argo Riffle
Bagby Hot Springs
Blue River Lake
Buck Canyon
Cougar Reservoir
Cornett Lake
Crooked Creek
Dulog Riffle
Dulog Creek
Maggies Riffle
Placer Lake
Riggs Lake
Russian Rapids
Sand Creek
Schuster Spring
Matthieu Lakes
Memaloose Island (historical)
Mount Hood Wilderness
Mount Washington Wilderness
Nellies Cove
Nehalem Beach
Perron Creek
Reservation Spring
Slim Pickins Rapid
Skull Spring
Solitude Riffle
Split Falls
Starr Creek
Stein Falls
Shadow Falls
Shroyer Ridge
Shevlin (historical)
Skookum Creek
South Warm Springs Creek
Stonehouse Canyon
Tonquin Scablands
Tub Springs
Tree Branch Creek
Upper Black Bar Falls
Vanishing Falls
Washboard Rapids
Warm Springs Creek
Watson Riffle
Yakso Falls
Thursday Creek
Terminal City
Pine Creek
South Fork Willow Creek (historical)
Pollard Creek
Auberry Creek
Lehman Creek
Guano Rock
Ruthton (historical)
South Channel Range B
South Channel
South Channel Range C
Willow Upper Range
Cox Rock
John Day Channel
Astoria Range
Upper Jarvis Range
Sand Island Range
Utter Rock
Long Rock
Red Point
White Rock
Sow and Pigs
Delta Island
Cedar Reservoir
Pamplins Pond
Shore Acres (historical)
Whalehead
Forks Creek
Eck Creek
School Creek
Prouty Creek
Sharp Creek
Washout Creek
Bill Creek
Blowout Creek
Ruth Creek
Stanley Peak
Ripple Creek
Lester Creek
Tom Fool Creek
Footlog Creek
Valsetz Guard Station
Found Creek
Cow Creek Safety Rest Area
Black Chunk Canyon
Paynes Pond
West Nelson Creek
Grave Creek Falls
Camp Nehalem
Jody Creek
Mills Creek
Briar Gulch
Conical Rock
Lake Hunice
Lake No-Se-Um
Homestead Lake
Fort Klamath Cemetery
Beetles Rest Reservoir
John C Boyle Dam
Rogue Elk
Etna (historical)
Finger Rock
Varmint Camp
Geppert Creek
McGregor Park
Geppert Creek
Quick Gulch
Quartz Gulch
Hacker Gulch
Eagle Gulch
Zigzag Creek
Andy Creek
Davis Creek
Miller Creek
Timothy Meadows (historical)
The Dalles (historical)
Lake Creek Cemetery
Whittier Reservoir
Succor Creek State Park
Kendall Slough
McCormick Reservoir
Mount Creek
Kubli (historical)
Dardanelles
Azalea Spring
Diamond Lake Recreation Site
Sawyers Rapids
Oakland Cemetery
Boswell Mineral Springs
Alca (historical)
Meadow Lake Valley
Tule Lake (historical)
Cavieta Reservoir
Larribeau Reservoir
Rodman Rim
Bayshore
Cedar Mountain
Columbia Plateau
Johnson Creek
Deadwood Junction
Elliott Canyon
Wessel Creek
Reed
Mohawk Valley
Keys Reservoir
Small Creek
Whiskey Creek
Seeley Creek
Nye Spring
Hurd Creek
Middle Creek
Hole in the Ground Creek
Knighten Creek
Rosebud Helipond
Swinning Creek
Old Town
Cooper Creek Reservoir
Babe Creek
Yankee Creek Reservoir
Panther Gulch
Shell Rock Spring
Quitters Point
Six Creek Spring
Buckeroo Spring
Pankey Springs
House Spring
Nail Spring
Haynesville
Creed Field
Utley Ranch
Dutton Creek
Moores Spring
Defeat Butte
Umatilla Reservation
Ruckman Reservoir
Valsetz Lake Dam (historical)
Blann Meadow Reservoir
Blann Meadow Reservoir Dam
Brookings Log Pond Dam
Chickahominy Creek Dam
Clearwater Number One Forebay
Clearwater Number Two Forebay
Toketee Dam
Cold Springs Dam
Crescent Lake Dam
Denley Reservoir
Dixonville Log Pond
Fish Creek Reservoir
Gold Ray Reservoir
Hoover Pond Number One
Hoover Pond Number Two
Hoover Pond Number Three
Hult Log Storage Reservoir
Keene Creek Diversion Dam
Kinzua Dam (historical)
Kinzua Reservoir (historical)
Lake Bonneville
Laurance Lake
Clear Branch Dam
Lake Selmac Dam
Lemolo Number 1 Dam
Lemolo Forebay Number Two
Lemolo Number 2 Forebay Dam
Lester James Dam
Lester James Dam Number 3
Lester James Reservoir
Lester James Reservoir Number 3
Lower Empire Lake
Mahon Dam
Mount Baldy Log Pond
Soda Springs Reservoir
Teasel Creek Reservoir
Tygh Valley Storage Dam
Tygh Valley Storage Pond
Widman Reservoir
Willow Creek Reservoir
Winchester Dam
Woodrat Knob Reservoir
Brushy Bar Riffle
Quosatana Creek Riffle
Quosatana Recreation Site
Lowery Riffle
Skookumhouse Canyon
Fry Landing
Coal Riffle
Wildhorse Recreation Site
North Fork Pistol River
Battle Bar Riffle
Island Rapids
Big Boulder Rapids
Skull Creek
Pix Mine
Lake Selmac
Hayes Hill Summit
Draper Valley
Indian Creek
Reservoir Creek
Little Stratton Creek
Indian Mary County Park
Limber Camp Spring
Moores Ridge
Secret Valley
Yellow Jacket Creek
North Fork Shale Creek
South Fork Shale Creek
Manganese Creek
Annie Spring
Taylor Creek Falls
Flanagan Slough
Shan Creek Recreation Site
Smithers Riffle
Dunbar Riffle
Bear Riffle
Bean Riffle
Mixer Riffle
Painted Riffle
Ethels Creek
Lynch Bar
New Riffle
Nail Keg Riffle
Tom East Riffle
Combs Riffle
Sherman Riffle
Shindler Riffle
Slide Creek Riffle
Upper Coal Riffle
Silver Creek Riffle
Dog Creek
Rachels Delight Riffle
Slide Creek
Bear Canyon
Little Canyon
Hardscrabble Ridge
Simpson Creek
East Gulch
Natural Bridges
Kettle Creek
Township Meadow
Rineman Ditch
French Pete Recreation Site
Coley Creek
Loon Creek
Sigerist Spring
Dixon Basin
Collins Butte Spring
Rush Pond
Gilson Pond
Range
Keeney Meadows
Gibbs Meadow
Four Corners
High Bar Rapids
McGraw Lookout
McGraw Spring
Duck Lake Recreation Site
McGraw Creek Cabin
Irondyke Mine
Ninety Six Spring
Howard Point
Dickenson Ranch
Purdy Ranch
Crow Flat Guard Station
King Spring
Jordan Reservoir
Harper Basin
South Cat Waterhole
South Cat Waterhole
Lake Janice
Dandelion Creek
Fort Klamath (historical)
Cavieta Creek
Keenig Campground (historical)
Nelson Creek
West Fork Mill Creek
North Fork Mill Creek
Kimble Ridge
Thissell Pond
Mill Creek County Park
Stonefield Beach State Recreation Site
North Fork Quarry
Alsea Summit
Sweethome Creek
James Reservoir
Bolan Lake Recreation Site
Andrew Wiley Park
Frog Lake
Upper South Fork Campground (historical)
Davis Creek
Gurtis Creek
Beltz Creek
Sand Beach Recreation Site
Orchard Bar
Gibson Reservoir
Cantrall Buckley County Park
Briar Gulch
Brushy Gulch
Wooldridge Gulch
Schoolhouse Gulch
Bear Pen Gap
Iron Gulch
Bald Hill
Left Fork Humbug Creek
Packers Gulch
Rowden Mine
Burnham Creek
Graves Creek
Howe Canyon
South Fork Collins Creek
W B Nelson State Recreation Site
Devils Bend
Mount Eckman
Eckman Quarry
Starr Creek
Big Stump Beach
Rogue Elk County Park
South Beamer Creek
Dawson Creek
Clear Creek
Bush Creek
Aqua Fria Reservoir
Cornpatch Prairie
Spikenard (historical)
Beagle
Cavitt Creek Falls Recreation Site
Portuguese Spring
Siltcoos Lagoon
Dog Creek
Gibson Reservoir
Cook Reservoir
Hanson Ridge
Shumard Creek
Mason Creek
Cathedral Hills County Park
Diamond Lake Information Center
Cook Ranch
Ashland Ranger Station
Ashland Forest Service Facility (historical)
Hart-Tish Recreation Site
Butte Falls Ranger Station
McLeod Forest Service Station
Entrance Range
Gull Point Recreation Site
Harralson Horse Camp
Cultus Lake Recreation Site
Cultus Lake Resort
McKay Crossing Recreation Site
Whitefish Horse Camp
Elk Lake Lodge
Elk Lake Recreation Site
Maidu Lake Recreation Site
Seventh Mountain Resort
Green Ridge Lookout Tower
Lava Camp Lake Recreation Site
Bagby Natural Research Area
Wyeth Recreation Site
McCubbins Gulch Recreation Site
Roslyn Lake Picnic Area (historical)
Lost Lake Recreation Site
Green Canyon Recreation Site
Mount Hood Skibowl
Little Crater Lake Geological Area
Wizard Falls State Fish Hatchery
Coast Creek Shelter
Coneridge School
Big Elk Campground
Hebo Ranger Station
Whitehorse County Park
Schroeder County Park
Alsea River Hatchery
Alsea Ranger Station (historical)
Tin Can Recreation Site
Elk River State Fish Hatchery
Foster Bar Recreation Site
Pioneer Recreation Site
Babyfoot Lake Area
Slack Creek
Cougar Creek
Tillicum Beach Recreation Site
Scare Creek
Taylor Creek
Neilson Creek
Stout Canyon
South Russell Creek
Peterson Creek
Hayes Eddy
Big Fish Riffle
Clay Hill Stillwater
Independent Order of Odd Fellows Cemetery
Anderson Creek
Aspen Flat
John Day River Dam
Glen Cabin
Courtrock
P P & L Canal
Poplars Ranch
Umatilla Bridge
Indian Spring
Little Stonehouse Creek
Stergen Meadows
Van Horn Basin
Ten Cent Meadows
O'Conner Homestead
Denio Basin
Monument Basin
Mapes Springs
Poor Farm
Tiller Cabin
Propeller Meadows
French Creek
Rough Canyon
McDade Ranch
Starr Homestead (historical)
Rabbit Hole Mine
Roux Place (historical)
Oleachea Place (historical)
Oleachea Pass
Stergen Cabin
Machine Meadows
Cold Spring
McLean Cabin
Willow Creek Pockets
Box Canyon Reservoir
Domingo Pass
Desert Bog Spring
Deer Spring
Bear Dog Spring
Rincon Flat
Dip Creek
Bronco Spring
Dugout Creek
Dip Spring
Dip Spring Reservoir
Hawks Valley Airstrip (historical)
Pueblo Reservoir
Box Canyon
Holmes Spring Reservoir Number One
Coyote Hole Reservoir
Middle Box Canyon Reservoir
Funnel Canyon Reservoir
Basque Hills Well
Roux Spring
Robbers Roost
Oreana Reservoir
Dry Well
Jordan Valley Cemetery
Jack Creek Hill
Palmer Dam
Middle Willow Creek Well
Alvord Well Number Four
Alvord Well Number Three
Alvord Well Number Two
Alvord Well Number One
Alvord Ranch
Pipeline Well
Mann Lake Ranch
Mann Lake Well
Miranda Flat
Big Basin
Big Basin Well
Boundary Lake
Sitz Lake
Browns Well
Hat Butte
Hat Lake
Lone Duck Reservoir
Wise Flat
Carlon Corral
Mercury Reservoir
Midnight Point
Black Rock Reservoir
Little Glass Butte
Bald Waterhole
Chesebro Spring
Musser Reservoir
Dribble Spring
Highway Waterhole
Pausch Lake
The Tank
Glass Butte
Robins Spring
Musser Draw
Musser Well
Cabin Spring
Perry flat
Canary Flat
Parmele Ridge
Jones Lake
Parmele Well
Browns Well
Browns Lake
Stauffer Well
Ant Flat
Hassler Lake
Yreka Butte
Mahogany Flat
Mahogany Waterhole
Wells Draw
Elvies Canyon
Rock Lake
Midway Lake
Brooks Lake
Benjamin Point
Harder Butte
Great Basin Waterhole
Hill Top Waterhole
Trail Flat
East Butte
Cracker Lake
No Name Butte
Concentration Reservoir Number Three
Indian Butte
Indian Lake
Hayes Spring
Little Benjamin Lake
Peters Butte
Duck Lake
Jim Lake
Line Lake
Chewaucan Slough
Paiute Lake
Dog Butte
Last Chance Well
Last Chance Lake
Trail Butte
Saddle Butte
Sage Hen Butte
East Walker Reservoir
Basalt Lake
Jaynes Well
North Butte Waterhole
North Butte
South Butte
East Reservoir
Division Reservoir
Rogers Well
Walker Cabin
Walker Creek
Stevens Butte
Coyote Hole Reservoir
Squaw Flat
Walker Butte
Twin Buttes
Ice Cave Pothole
Jacks Place
Ward Reservoir
Seventeen Well
East Green Mountain
Green Mountain Lookout
Green Mountain
Boundary Well
Sixteen Well
Rinaldi Reservoir
Gould Creek
Bunch Bar Wayside
Hurd Creek
Shale Creek
Hound Creek
Whitehorse Creek
Maupin Bar
Jones Bar
Smith Ferry Rapids
Heddin Bluff
Cedar Creek
West Fork Halfway Creek
Saddle Butte
Hancock Hill
Hancock Mountain
Sand Hollow Well
Burrows Lake Reservoir
Eades Well
Jew Valley
Curve Waterhole
Rams Butte Reservoir
Mecca Grade
Rattlesnake Grade
Quinook (historical)
Whiskey Canyon Spring Reservoir
Ryegrass Reservoir
Holmes Spring
Lone Mountain Spring
Williams Springs
Independent Order of Odd Fellows Cemetery
Mishawaka
Sitz Ditch
Drewsey Rodeo Ground
Drewsey Cemetery
Sheep Spring
Stallard Ditch
Otis Valley
Schlitz Waterhole
Folder Waterhole
Spook Waterhole
Oblong Waterhole
Immigrant Waterhole
Jinx Well
Black Rim
Bear Hollow County Park
Gordy Flat
Mabe Hill
Juniper Creek
Homestead Spring
Little Happy Spring
Peter Spring
Slow Spring
Three C Spring
Round Butte Cemetery
Coburn Well
Cougar Gulch
Hail Creek
Watson Creek
Boundary Reservoir
Bracket Canyon
Long Ridge
Committee Spring
Teater Spring
Booton Spring
Fly Reservoir
Hells Half Acre
Walton Canyon
Clymer Canyon
Fossil IOOF Cemetery
Walton Spring
Trail Fork (historical)
Lost Valley (historical)
S A Canyon
Stanton Canyon
Sullivan Spring
Hermiston Cemetery
Taylor Grade
Hazardous Chemical Waste Site
Schuebel Cemetery
Leland (historical)
McNary Dam Fish Viewing Station
McNary Dam Fish Ladder
Umatilla Toll Bridge Toll Plaza (historical)
Spanish Hollow (historical)
John Day Dam Fish Ladder
Preachers Eddy
Jake Spring Reservoir
Rock Hill
Buffalo Creek
Skip Creek
Cabin Creek
Gods Thumb Creek
Hattin Creek
Thimble Creek
Mud Creek
Vaughn Peach Ranch
D Jones Ranch
Fenton Spring
P Coyne Ranch
Short Creek
Spring Reservoir
School Section Reservoir
Opal Reservoir
Cow Camp
Lasa Place
Dry Gulch
South Fork Fish Creek
Fish Creek Breaks
Dry Creek
Buckaroo Corral Spring
Buck Spring
Locust Spring
East Wall Rock Spring
Mud Spring
Clay Reservoir
The Cove
Sera Well
Ibex Waterhole
Willow Springs
Willow Ridge
Willow Butte
Ann Butte
Rickman Spring
Juniper Spring
Santry Waterhole
Twelvemile Reservoir Number One
Twelvemile Reservoir Number Two
Ibex Butte
Twelvemile Reservoir Number Three
Twelvemile Reservoir Number Four
Mills Waterhole
Sartain Reservoir Number Two
Kid Peak
Enchanted Prairie Cemetery
Fetter Cemetery
Fetter Creek
Fox Pond
Little Rock Creek
Skull Ridge
Narrows
Tumwater Falls
Pistol Canyon
Woolhawk Canyon
Rattlesnake Canyon
Bull Creek Reservoir
Lower Chimney Creek Reservoir
Upper Chimney Creek Reservoir
Little Grassy Mountain
Coyote Spring
Holding Corral Reservoir
Potomac Ranch
Truck Trail Pit
Dry Creek
Parks Reservoir
Arrow Gap
Fort Rock Substation
Hayes Place
Bridge Well
Arrow
Tuff Butte
Tuff Cabin
Echave Reservoir
Lonely Reservoir
South Fork Elk Creek
Brownson Creek
Slide Creek
Split Mountain
Scott Mountain
Jenkins Prairie
Pheasant Creek
Tyee Bar
Little Windy Creek Campground
North Jenny Creek Campground
Black Bar Lodge
Doe Creek Campground
Big Slide Campground
Whiskey Creek Campground
Big Windy Creek Campground
Wildcat Campground
Big Slide Riffle
McKinley Cemetery
Fort Briggs (historical)
Lenz Creek
Masonic Cemetery (historical)
High Bridge
Independent Order of Odd Fellows Cemetery
Bonanza Springs
Malin Irrigation District Pumps
Dearborn Reservoir
Sand Hollow
Dry Spring
Threemile Flat
Rocky Canyon
Malheur Cemetery
Ponderosa Substation
Price Spring
Ensley Cemetery
Flagg Reservoir
Horseshoe Bar
Big Basin
Green Flat
Tiller Well
Sweek Dam
Clemens Well
Hotchkiss Well
Luig Spring
Paiute Cemetery 2
Oberg Canyon
Williams Creek
Buzzard Butte Canyon
White Rock
Horner Creek
Doe Camp
Camp Fir Croft
White Elephant Bridge
Bills Prairie
Powers County Park
Dagus Lake
Sand Hollow Well
Sand Hollow
Sheep Head Canyon
Cold Spring Ranch
Lower Sherman Ranch
Thurman Weaver Reservoir
Yoncalla Valley
Furnace Waterhole
Juniper Waterhole
Soda Spring
Bedell Canyon
Orr Point
Steens Ridge
Fadeley Reservoir
Burnt Mountain Reservoir
Becker Reservoir
Rattlesnake Reservoir
Squaw Bluff
Cape Blanco Lighthouse
Needle Rock
Barrel Rock
Split Rock
Paradise Point State Park
Hughes Family Cemetery
Rivers Edge Park
Cole M Rivers Fish Hatchery
Jackson Spring
Dipping Vat Spring
Wild Hog Creek
Tubb Springs State Wayside
Sloan Creek
Hamaker Spring
Wallis Spring
Rosebud Reservoir
Oregon Gulch Reservoir Number One
Box O Ranch
Fall Creek Reservoir
Ling Reservoir
Taylor Ranch
Leonard Ranch
Fall Creek Ranch
Willow Point County Campground
Howard Prairie Canal
Sugar Pine County Group Campground
Howard Prairie County Recreation Area
Asperkaha County Campground
Elk Creek Dam
Elk Creek Lake
North Point
Charity Reservoir
Cinch Reservoir
Connell Reservoir
Market Spring
Pine Reservoir
Shale Reservoir
Faith Reservoir
Watson Spring
Owl Reservoir
Pine Mountain
Pine Spring
Lightning Spring
Reservoir Twenty-eight
Bone Reservoir
Jumbuck Reservoir
Deadline Flat
Lakeside Ridge
Clover Creek
Llewelyn Spring
Clover Creek Reservoir
West Keno Springs
Robinson Reservoir
Larson Spring
Zimmerman Spring
Kraitz Reservoir
Four H Reservoir
Brydon Reservoir
Athey Creek
Neighbors Reservoir
Fast Reservoir (historical)
Phoenix Reservoir
Stapleton Reservoir
Bruinsma Reservoir
Walker Reservoir
Canemah Cemetery
Saint Patrick Cemetery
Clackamas County Fairgrounds
MC Well
Dribble Creek
Staircase Creek
Calf Creek
Hutch Creek
Hare Creek
Henry Spring
Dutchman Creek
Sweat Creek
No Sweat Creek
North Fork Darby Creek
West Fork Darby Creek
Manzanita Creek
Live Oak Creek
Michigan Spring
Whiskey Camp Creek
Bull Canyon Creek
Brush Creek
Juliano Creek
Bateman Ridge
Bateman Lookout Tower
Rattlesnake Ridge
Red Point
Pueblo Well
South Sand Hills Well
Sand Hills Well
Sand Hills
Mapes Flat
Cherry Creek
Colony Creek
Oliver Creek
Stonehouse Creek
East Creek
Pass Creek
Deep Creek
Oregon End Ranch
Oregon End Well
Hickey Waterhole
Buck Flat
Buck Flat Waterhole
Buck Spring
Als Spring
Blue Mountain Reservoir Number Two
Blue Mountain Reservoir Number One
Burnout Spring
Gild Reservoir
Wash Rock Spring
The Cap
Basque Flat Reservoir
Lone Star Reservoir
Summit Spring
The Table
Blue Mountain Pit Reservoir
Horse Corral Creek
Lava Ridge Reservoir
Blue Mountain Reservoir Number Five
Long Draw Reservoir
Crossroad Reservoir
American Fossil Mine
Government Well
Morehouse Well
Lane Lake
Gerkin Well
Fleetwood
Loma Vista
Stingley Reservoir
Linn Memorial Cemetery
Cookes Camp
Corral Creek Recreation Site
Indian Camp
Hoodoo Ridge
Chalk Bank Reservoir
William Spring
Wisner (historical)
Canyon Spring
Lower Crossing
Warm Hill
Windmill Point
Whiteman Pond
Feathered Friend Pond
Bamford Spring
Cedar Canyon Creek
Scoggins Valley
Jesse Reservoir
Nelson Pond
Hortons Reservoir
Larsen Reservoir
Ken Larsen Dam
Big Spring
Lafayette Spring
Nelson Spring
Saint Josephs Dam
Saint Josephs Reservoir
Fairfield Cemetery
Sager Creek
Buster Creek Quarry
Barnhart Reservoir
Thrush Reservoir
Combs Reservoir
Turquoise Pond
Lost Lake
Denn Reservoir
Watson Spring
Slide Mountain Lookout Tower
Elkhorn Spring
Carmen Creek
Trail Gulch
Cleveland Ditch
Rattlesnake Gulch
Nickols Spring
Cabin Spring
Gilman Spring
Del Spring
Rocky Flat
Bull Prairie
Jefferson School Park
Rheinhardt Gulch
Brockway Reservoir
Wertz Reservoirs
Woolfolk Reservoir Number Two
Trammel Reservoir
Owens Reservoir
Stanley Reservoir
Willow Lake County Park
Buck Point Lookout
Goose Lake State Park
Juniper Lake Ranch
Negro Springs
Steens Mountain School
Alberson (historical)
Fifteen Cent Lake
Neal Spring
South Lake
Pollock Reservoir
Riddle Mountain Lookout
Tom Jenkins Cabin
Puhi-Pane Na-De Lake
Mclean Cabin
Puhi-Pane Na-De Flat
Ross Dollarhide Springs
Bill Gordon Spring
Clark Place
Ward Place
Dollar Lake
Leppy Springs
Smyth Cabin
Slim Dupree Place
Charles Kuhl Springs
Courtwrights Spring
Comegys Cabin
Sullivan Creek
Sullivan Meadows
Paddle Meadows
Barrel Springs
Mann Lake Cabin
Alberson Station (historical)
Big Springs
Strode Springs
Hamilton Place (historical)
Little Stonehouse Creek
White Sage Flat
Sulphur Springs
Pollock Well
Summit Creek
Whiskey Hills
Sherman Reservoir Number Two
Nash Canyon
Chris Fur Canyon
Lingo Slough
Territorial Elementary School
Glazers Grade
Svensen Slough
Westport Beach
Hidden Valley
Eagle Fern Youth Camp
Middle Falls
Shirk Ranch
Mercer (historical)
Watters Reservoir
Green Mountain Lookout Tower
Hunter Grade
Foley Butte Lookout Tower
Woods Cemetery
Dog Lake Guard Station (historical)
North Canal Flume
Friday Ranch
Becraft Ranch
Drews Reservoir County Park
Wilson Bend
Kimsey - Walker Cemetery
Wright Sump
Shaw
Herren Cemetery
Hunsaker Cemetery
Browns Spring
Flying M Reservoir
Vincent Pond
Bailey Spring
Baker Creek Falls
Bolton Creek
Heater Reservoir
Alder Creek Reservoir
Kinsey Reservoir
Trask Mountain Lookout
Tillamook Gate
Meadow Lake
Walker Creek Reservoir
Bedortha Reservoir
Elliott Prairie
Kern Reservoir
Gribble (historical)
Rose Reservoir
Aurora IOOF Cemetery
Jacks Bridge
Noble (historical)
Hartman Dam
Harding (historical)
Beyer Reservoir
Abiqua (historical)
Walker Ditch
Central Howell
Eoff Cemetery
Nygren Reservoir
Polvi Reservoir
Salem Hospital Regional Health Services
Oregon School for the Deaf
Eola
McNary (historical)
Finzer (historical)
Ross Reservoir
Polk County Fairgrounds
Boeder Pond
Bass Reservoir
Pond A
Oberg Reservoir
Everz Creek
Maddux Reservoir (historical)
Christianson Reservoir
Ratzlaff Reservoir
McGuire Reservoir
Crescent Valley
Oakshire Reservoir
Palestine Memorial Church Cemetery
Rutherford Ditch
Rutherford Spring
Canterbury Creek
Wigle Cemetery
Moonshine Ridge
Whiskey Spring
Black Ridge
Pumice Waterhole
Dickerson Flat
Dickerson Well
Spicer Flat
Two Post Lake
Whiskey Rock
Berger Ridge
Rimrock Creek
Espeland Draw
Johnson Flat
Dominick Well
Imperial (historical)
Braken Flat
Peters Well
Burns Well
Cody Well
Coyote Rock
Bronco Butte
Meeks Waterhole
Nershal Well
Sunflower Flat
Sunflower Lake
Rim Waterhole
Ram Lake
Skull Lake
Mud Lake
Corral Butte
Grassy Lake
Grassy Ridge
Ancient Lake Well
Grassy Ridge Well
Echart Grade
Antelope Spring
Antelope Pond
Little Hole Spring
Bone Spring
Red Line Reservoir
Corner Reservoir
Groan Canyon
Bone Canyon
Whitby Spring
Mud Spring
Early Spring
Stoddart Reservoir
Mickey Spring
Hub Reservoir
Inbetween Reservoir
Euglena Reservoir
Capp Reservoir
Upper Hole Reservoir
Small Butte
North Heath Creek
North Heath Creek Reservoir
Gabriel Reservoir
Lake Edge Reservoir
Wildhorse Spring Number Two
Wildhorse Spring Number Three
Wildhorse Spring Number One
Ryegrass Butte
Mickey Canyon
Pouge Holes Spring
Heath Creek Spring
Sagehen Spring
Short Draw Spring
Wildcat Reservoir Number Two
Jimmy Spring
Canyon Well
Wildcat Reservoir
Bobcat Reservoir
Steel Post Reservoir
Three Forks Reservoir
Wildcat Well Number Two
West Table Mountain Reservoir
Table Mountain Reservoir
Table Mountain Well
North Table Mountain Reservoir
East Table Mountain Reservoir
Antelope Spring Number Three
Wire Corral Flat
Wagner Waterhole
Wildlife Lake
Squib Waterhole
O'Keefe Reservoir
Tohatin Reservoir
Tunnel Point
Bastendorff Beach County Park
Handle Reservoir
Marine Park
Roland Lake
Duck Ridge
Grindstone Rim
Mudhole Reservoir
Boundary Reservoir
Drummond Basin Reservoir
Twin Springs
Twin Springs Reservoir
Wade Butte
Coffee Butte
Martin Spring
Rose Mine
Deadman Butte
Five Points
Cabin Spring
Veason Spring
Cabin Butte
Division Reservoir
Optimism Reservoir
Speckle Butte
Three Buttes
Juniper Spring
Juniper Canyon Reservoir
Emmets Hole
Antelope Corral
Desperation Reservoir
Russell Reservoirs
No Crossing Crossing
Seldom Reservoir
Emil Reservoir
Funeral Ridge
Fir Tree Spring
Lame Dog Reservoir
Mayme Spring
Berger Ranch
Grass Butte
Doubtful Reservoir
Hawkins Basin Reservoir
Hawkins Basin
Sheep Reservoir
Merwin Reservoir Number Three
Shaw Spring
Muhly Lake
Soda Lake
Sheepcamp Reservoir
Little Basin Reservoir
Sevenmile Slough
Richardson Gulch
Shaw Spring
Harper Dam
Adrian Elementary School
York Butte
Lower Watson Spring
Biddle Reservoir
Cannery Spring
Baker Ranch
Flat Lake
Poley Reservoir
Isadore Butte
Dracatos Reservoir
McKee Gulch
Anderson (historical)
Davies Ranch
Foster Reservoir
Rabbit Valley
Skinner Well
Fitchett Well
Winters Reservoir
Spring Creek Reservoir
McKee Spring
Sabre Ridge
Derr Creek
Jones Well
Cabbage Creek
Toggle Creek
Angell Ranch
Bitter Brush Basin
Sweeney Waterhole
Rodgers Reservoir
Lamb Lake
Abbot Creek Recreation Site
Ady Canal
Agency Lake
Aldrich Creek
Aldrich Grave
Aldrich Mountain
Allen Springs Recreation Site
Anderson Creek
Antelope Creek
Artman Basin
Aspen Lake
Badger Hole
Bailey Waterhole
Ball Bay
Ball Point
Face Rock State Park
Bark Cabin Creek
Barnett (historical)
Barview
Bastendorff Beach
Bay City
Bay City Channel
Bays Creek
Bear Creek Park
Bench Top Waterhole
Big Dry Lake
Big Pine Springs
Big Ridge
Big Spring
Cape Meares Lake
Bingham Point
Black Rock
Black Rocks
Blossom Bar Creek
Bluejoint Lake
Bly Mountain Pass
Boardman Junction
Bottomless Lake
Boulder Creek
Boundary Spring
Bridge Creek
Bridgeport
Browns Cove
Buck Lake
Buck Point
Buck Point
Buckaroo Pass
Buena Vista Lake
Bullards Bridge
Butcher Flat Reservoir
Cabbage Patch Camp
Cabbage Patch Spring
Cabin Creek
Cabin Creek Trail
Caledonia Canal
Caledonia Dike
Caledonia Marsh
Calohan Spring
Camp Two
Camp Walker (historical)
Cape Arago
Cassnor Peak
Cedar Point
Center Canal
Chicken Springs
Chickses Creek
Chilkoot Pass
China Diggings
China Town
Clarke
Clarksville
Cleo (historical)
Coal Creek Camp
Cold Creek
Cold Spring
Cold Spring
Coleman Creek
Company Trough
Coon Point
Coos Head
Coquille Point
Coquille River
Corral Gulch
Cow Canyon
Cox Butte Waterhole
Coyote Bucket
Coyote Lake
Coyote Lake
Crab Harbor
Crazy Creek
Crows Nest
Crystal Creek
Cunningham Creek
Cut Creek
Day Creek
Dead Pine
Deadmans Point
Deer Creek
Deer Gulch
Dixie (historical)
Dollar (historical)
Doty Creek
Dry Cabin Creek
Dry Cabin Creek Trail
Dry Creek Swamp
Dry Duncan Creek
Dry Duncan Creek Trail
Duncan Creek
Eagle Point
East Fork Brummit Creek
East Fork Corral Gulch
Eldorado
Eldriedge Landing
Eldriedge School (historical)
Emigrant Crossing
Empire
Ennis Butte Spring
Famine Lake
Farley Creek
Fern Valley
First Creek
Fisher Creek
Fivemile Creek
Fivemile Point
Flat Creek
Fourmile Creek
Fourmile Lake
Fox Creek
Geneva
Gibson Lake
Glen Brown Place
Goff (historical)
Goodview Point
Goose Point
Gore Creek
Grant Place
Gravel Point
Gregory Point
Grizzly Prairie (historical)
Halls Point
Hanging Rock
Hankins Spring
Hibbard Point
Hogg Rock
Honeycombs
Howard Bay
Howard Prairie (historical)
Huckleberry Draw
Hungryman Cove
Huntington Junction
Indian Spring
Indian Village
Jefferson Elementary School
Joe Lake
Joe Ney Slough
Jackson Creek
Johnson Creek
Judge Hamilton County Park (historical)
Juniper Butte
Keno Spring
Kenutchen Creek
Kilchis Flat
Klamath Strait
Kronenberg County Park
Lajeunesse Creek
Lake Ewauna
Lake of the Woods
Lake Waterhole
Lamm Crossing
Larson Creek
Left Fork Scotty Creek
Liberty Bottom
Lighthouse Beach
Link River
Little Aldrich Mountain
Little Bridge Creek
Little Steamboat Point
Lockhart Crossing
Log Lake
Lone Pine Elementary School
Long Island
Long Island Point
Long Water Holes
Lost Lake
Lower Bridge (historical)
Magpie Table
Malheur City (historical)
Marks Creek
Mayfield Pond
Maynard Flat
Meadow Lake
Merchants Beach
Miami River
Middle Cove
Military Crossing
Mill Creek
Miller (historical)
Miller Island
Mission Lake
Missouri Bottom
Moody
Moss Creek
Mud Lake
Mud Pot Waterhole
Mud Spring
Murderers Creek Ranch
Murray Creek
Mussel Reef
Mustang Jail
Namorf (historical)
New Pass
New River
Nichols Branch
North Beach
North Cove
North Jetty
Odessa Creek
Old Kelly Mill (historical)
Olson (historical)
Oregon Islands National Wildlife Refuge
Otwin Spring
Page Place
Palomino Grade
Patterson Creek
Payne Canyon
Payne Creek
Persist (historical)
Peterson Point
Phoenix
Pigeon Point
Pikes Crossing Recreation Site
Pilot Rock
Pinchot Lake
Pistol Lake
Pitcher Point
Plainview School (historical)
Ponderosa Junior High School
Puckett Glade
Rainbow Lake
Rigdon Point
Riley Huff Place
Ringtail Pine
Ritter Reservoir
Roaring Spring
Roberts Butte
Rock Island
Rocky Point
Rocky Point
Roosevelt Lake
Round Lake
Ruggles Grade
Sage Hen Crossing
Sand Lake
Sawmill Spring
Schoolhouse Gulch
Scotty Creek
Second Creek
Seth School (historical)
Seven Devils
Shake Table
Lake Shell Rock
Shoalwater Bay
Shoestring Grade
Short Creek
Shrock
Simon Landing
Simpson Place
Siskiyou Memorial Park
Sisters
Sitka Dock
Skookum Lake
Skull Island
Skyview Memorial Park
Slide Lakes
Smith Rock State Park
Socket Waterhole
South Cove
South Fork Murderers Creek
South Jetty
Brandon South Jetty County Park
South Slough
Spongs Landing
Spoos Mill
Spring Lake Valley
Starr Recreation Site
Stewart Lake
Stewarts Crossing
Stockdale Creek
Sunset Bay
Swan Creek
Table Rock
Table Rock
Table Top
Talbot Creek
Talent Lateral
Tarheel Reservoir
Taylor Butte
Taylor Lake
Telegraph Hill
The Big Horse Trails
The Devils Garden
The Indian Trails
The Peninsula
The Peninsula
The Tongue
Thorn Creek
Thorn Lake
Three Lakes Waterhole
Timber Mountain
Tioga (historical)
Todd Creek
Todd Creek Camp
Tompkins Landing
Trail Ridge
Tucker Flat Camp
Tunnel Creek
Tupper Creek
Twin Rocks
Twomile Creek
Twomile Creek
Union Creek (historical)
Upper Crossing
Upper Pony Creek Reservoir
Valino Island
Varney Creek
Vaughn Point
Voorhies
Wagonslide
Walker Flat (historical)
Water Gulch
Waterman (historical)
Waterpipe Creek
Watseco Creek
Klamath Falls-Lakeview Forest State Park
Weaver Cabin
Weaver Place
West Fork Brummit Creek
Westside Waterhole
Whetstone Point
Whisky Run
Whisky Run Beach
White Point
Whiteline Reservoir
Wildhorse Canyon
Wildhorse Spring
Wyllie Creek
Willow Lake
Winchester Creek
Windy Point
Windy Point
Wizard Falls Campground (historical)
Wocus Drainage Canal
Wocus Marsh
Wood River
Lake of the Woods
Worlow Reservoir
Wylie Gulch
Yoakam Point
Yonna
Zuckerman Island
Willow Spring
Klondike School (historical)
Juniper Point
Thistle Creek
Tumalo Falls Recreation Site
Walton Lake
Oreana Waterhole
Robbins (historical)
Bull Frog Lake
Shipley Pool
Mayes Reservoir
Bruce
Rickard
Hughes (historical)
Buchanan
Lorence Reservoir
Lake of the Winds
Johnson Creek
Creswell Association Cemetery
Slide Mountain Geological Area
KBOY-FM
KHUG-AM
KISD-AM
KMED-AM
Gulch Dam
Grohs Reservoir
Simms Dam
Willow Creek Dam
Link River Dam
Keno Dam
McLoughlin Airfield (historical)
Kime (historical)
Seventh Day Adventist Organization Camp
Islet Recreation Site
Huggins Canyon
Bandon Beach
Celilo Falls (historical)
Coyote Island (historical)
Tacoma Rapids
Independence Mine
Powers City Park
Sproul Reservoir
Horse Prairie (historical)
Dunkard Cemetery
Hillcrest Memorial Cemetery
Falcon Heights
Enchanted Prairie
Coquille Valley Intermediate School
Oberman Reservoir
Aspen Point Recreation Site
White Pine Campground (historical)
Rainbow Bay Recreation Site
Fourmile Lake Recreation Site
Brookside Creek
Cattail Creek
Edsalla (historical)
Sandoz (historical)
Grubbe Creek
Little Stony Brook Creek
Mahoney Reservoir
Beatty Gap
Cox Reservoir
Ritter Reservoir
Peters Lake
Goose Paint
Juniper Glade Pond
Clarno Rapids
Bob Plank Spring
Rum Pond
Coke Pond
Witch Drain Pond
Aspirin Pond
Flu Pond
Pill Pond
Round Pond
Near Pond
Pulpit Rock
Tyee
Princeton (historical)
Meadow Lake Dam
Sproul Dam
Star Lake Dam
Star Lake Reservoir
Tarheel Creek Dam
Upper Pony Creek Dam
Wade Dam
Wade Reservoir
Last Chance Gulch
Fourmile Rock Pit
Schonchin Cinder Pit
North Fork Elk Creek
South Fork Elk Creek
Fall Creek
Cline Falls (historical)
Cabin Reservoir
Homesite Reservoir
Wickiup Reservoir
Wagner Springs
Grandview Cemetery
Bingham Springs
Hendricks Reservoirs
Sky Ranch Reservoir Number Four
Cold Springs
Sandy Reservoirs
Hot Rock Reservoir
Hart Reservoir
Rock Reservoir
Courter Reservoir
Siletz Reservoir
Olalla Barrier Reservoir
Peck Reservoir
Cory Reservoir
Lower Basin Draw Reservoir
Little Reservoir Number Three
Cork Reservoir Number Seven
Shumacher Reservoir Number Five
Silver Creek Reservoir
Maher Reservoir
Chiloquin State Airport
Southshore Campground
Jackson Creek Reservoir
Hole-in-the-Ground Reservoir
Molalla Prairie
De Vos Pond
Macduff Mountain
McLennan Mountain
Ajax (historical)
West Fork Shutler Creek
East Fork Shutler Creek
Coles Bridge
Vance Creek Safety Rest Area (historical)
Cottonwood Bridge
Odessa Spring
Ford Spring
Christmas Creek Camp
Cat Creek Ranch
Peasley Lake
Warm Springs Elementary School
Buckingham Elementary School
Camp Abbot Bridge
Montgomery Bridge
La Pine State Park
Irish and Taylor Recreation Site
La Pine Elementary School
Fremont (historical)
Gilchrist Log Pond
Rosedale (historical)
Squirrel Camp
Milliorn Hill
Brothers Oasis Safety Rest Area
Harney Holes
Bottero Park
Spring Creek Ditch
Fawn Gulch
Pleasant Ridge
Harry M Hewitt Memorial Park
Richland Elementary School (historical)
Soda Lake
Olive Lake Recreation Site
Fairview Recreation Site
Cry Creek
Spring Creek
Fossil Creek
Faith Spring Forest Camp (historical)
Forest Creek Recreation Site
Crane Creek Forest Camp (historical)
Keen Camp (historical)
Persia M Robinson Natural Area
Christ Our Redeemer Lutheran School (historical)
R E Jewell Elementary School
Ponderosa Park
Bear Creek Elementary School
Woodland Pond Park
Juniper Elementary School
Pilot Butte Middle School
Saint Charles Medical Center
Mountain View Senior High School
Saint Francis School (historical)
Drake Park
Skyliners Park Sports Complex
Cascade Junior High School (historical)
Central Oregon Community College
Terrebonne Community School
Redmond High School
M A Lynch Elementary School
Ray Johnson Park (historical)
Obsidian Middle School
Tygh Valley School (historical)
Maupin Grade School
South Wasco County High School
Crooked River National Grassland
Lamonta (historical)
Bear Springs Recreation Site
Cedar Burn Camp
Warm Springs Junction
White River Crossing Camp (historical)
Potters Camp
Little Fawn Recreation Site (historical)
South Sherman Elementary School
Beavertail Recreation Site
Rufus Elementary School (historical)
Westside Elementary School (historical)
Madras High School
Madras Elementary School
Mountain View Hospital
Ochoco Lake State Park
Crawford Reservoir
Crooked River Elementary School
Crooked River Park
McCornack Elementary School
New Hope Christian College
Acorn City Park
Hawkins Heights City Park
Burma
Golden Gardens City Park
Candlelight City Park
Cantrell Hill
Hileman Landing County Park
Cartwright Slough
West Point Airport
Oak Grove Safety Rest Area
Howard Buford Recreation Area
Douglas Gardens Park
Vickery County Park
Ridgeview Elementary School
Mosier Community School
Mosier Pioneer Cemetery
Hood River Middle School
Lane Community College Main Campus
Christensen Landing Park
Washburne Park
Bergstrom Park
Laurel Park
Bailey Park
Wells Island
Prineville Reservoir Resort
Freewater Elementary School
McNary Heights Elementary School
Horne Airfield (historical)
Elliott Memorial Park
Weston Middle School
Athena Elementary School
Dorothy Bridge
Joe West Bridge
Reservoir Campground
North Side Spring
Emigrant Hill Viewpoint
United States Forest Service Guard Station
Matlock Water Hole Camp
Snake River Slides Safety Rest Area (historical)
Becker Ponds
May Roberts Elementary School
Aiken Elementary School
Eastside Park
Riverside Junior and Senior High School
Sam Boardman Elementary School
Boardman Safety Rest Area
Tollbridge Park
Thunder Island
Cascade Locks School
Mount Hood Flat School (historical)
Mill Creek School (historical)
Chenowith Elementary School
Whitford Middle School
Greenway Elementary School
Hiteon Elementary School
Crystal Lake
James Templeton Elementary School
Spring Creek
Rocky Heights Elementary School
Steelhead Park
Highland Hills Elementary School
Armand Larive Middle School
Seventh Day Adventist School (historical)
McGee Ranch
Upper Silver Creek Ranch
Dunn Ranch
Morgan Ranch
Kellogg Ranch
Raleigh Hills Elementary School
Garden Home School (historical)
Valley Catholic School
Aloha High School
Mountain View Middle School
Thomas R Fowler Middle School
Errol Hassell Elementary School
Chehalem Elementary School
Highland Park Middle School
Astoria Middle School
Astoria Senior High School
Gray Elementary School
Seaside High School
Gearhart Elementary School
Jennings Lodge Elementary School
Arleta Elementary School
Woodstock Elementary School
Essex City Park
Earl Boyles City Park
Gilbert Park Elementary School
Bloomington City Park
Brentwood Park
Berkeley City Park
Flavel City Park
Battin School (historical)
Ardenwald Elementary School
Lewelling Elementary School
Wichita Elementary School
Christ the King Parish School
La Salle Catholic College Preparatory
Linwood Elementary School
Rex Putnam High School
View Acres Elementary School
Lovawalla Spring
Clackamas School (historical)
Candy Lane Elementary School
Walter L Kraxberger Middle School
John Wetten Elementary School
Sunnyside Elementary School
Pendleton City Park
Lakeridge Junior High School
Bryant Elementary School
River Grove Elementary School
Jackson Middle School
Legacy Meridian Park Hospital
Montclair Elementary School
Capitol Hill Elementary School
Lewis and Clark Law School
Portland Community College Sylvania Campus
Stephenson Elementary School
Uplands Elementary School
Alice Ott Middle School
Our Lady of the Lake School
Lakeridge High School
Stafford Primary School
Frazee Ranch
Houston Ranch
Poison Creek
Watkins
Ruch Elementary School
Rogue River Junior/Senior High School
Palmerton Park
Rogue River Elementary School - West Campus
Coyote Evans Wayside
Mid Valley Elementary School
Indian Springs Campground (historical)
Eugene Blue Star Safety Rest Area (historical)
Feyer County Park
Molalla River School District 35
Assumption School (historical)
Holladay City Park
Holladay Park Hospital (historical)
Bess Kaiser Hospital (historical)
Wallace City Park
Convent of the Good Shepherd
Claredon Elementary School (historical)
Portsmouth City Park
Physicians and Surgeons Hospital (historical)
Irvington Elementary School
Dawson City Park
Lillis Albina City Park
Jones Cemetery
Periander Park
Legacy Good Samaritan Medical Center
International Learning Program
Col Summers City Park
Legacy Emanuel Medical Center
East Sylvan School
Saint Helens High School
Columbia District Hospital
Pisgah Home Cemetery
Hauton B Lee Middle School
Harold Oliver Intermediate Center
Oliver Elementary School
Alder Elementary School
Highland Elementary School
Mount Hood College Reservoir
Fairview Elementary School
Troutdale Elementary School
Reynolds High School
Sweetbriar Elementary School
Mount Hood Community College Gresham Campus
Hillsboro High School
Scholls Bridge
Cedar Park Middle School
Providence Saint Vincent Medical Center Hospital
Portland Community College
Rock Creek Elementary School
Bethany Elementary School
Five Oaks Middle School
Pioneer Catholic Cemetery of Saint Anthony of Padua
Cemetery Reservoir
Elmonica Elementary School
Meadow Park Middle School
Holy Trinity School
Cedar Hills Kindergarten and Preschool
Bethany Presbyterian Cemetery
Glencoe High School
Rivercrest Park
Gaffney Lane Elementary School
Oregon City Senior High School
Carus School
Beavercreek Memorial Cemetery
Carus Cemetery
Saint Peters Cemetery
Edward Byron Elementary School
Sherwood High School
Baldock Safety Rest Area
Callahan Rehabilitation Center
Wilsonville School (historical)
Jim Tapman Creek
Sandy Intermediate School (historical)
Sandy Grade School
West Orient Middle School
East Orient Elementary School
Pleasant Home Cemetery
Sam Barlow High School
Fields Bridge
John McLoughlin Elementary School
Knights Bridge
Red Bridge
Barlow Pioneer Cemetery
William Knight Elementary School
Baker Prairie Cemetery
Ackerman Middle School
Colton Elementary School
Colton High School
Colton Middle School
Clarkes Elementary School
Cedar Creek Reservoir
Thompson Park
Saint Mary's Academy
Joseph G Wilson Elementary School (historical)
Howe Park
Dry Hollow Elementary School
The Dalles Middle School
Dufur School
Bonney Meadows Recreation Site
Badger Lake Recreation Site
Lower Fivemile School (historical)
Lower Eightmile School (historical)
Fairfield School (historical)
Wasco Lookout
Lincoln Park Elementary School
Margaret Scott Elementary School
Frazer Park
Shaver Elementary School
Columbia City School
Graveyard Rim
Davis Ranch
The Dalles - Wahtonka High School
Mid - Columbia Medical Center
Colonel Wright Elementary School
Pleasant Ridge School (historical)
Upper Eightmile School (historical)
Endersby School (historical)
Grass Mountain
South Shore Elementary School
Lippin Cotts Gulch
San Salvador Access
Peoria County Park
McCartney County Park
Murphy Hill
Adair County Park
Nenamusa (historical)
Broadway Middle School
Seaside Heights Elementary School
Sunset Beach
Mantel Lake
Cannon Beach Elementary
Mayo
Pittsburg Guard Station
Piedmont Creek
Rainier Elementary School (historical)
Verges Ranch
Barney Ranch
Cowan Ranch
Hughet Dam
Wildhorse Lake Reservoir
Cox Butte Reservoir
Empty Lake Well
End of the Trail Reservoir
China Cap Mine
Boyce Waterhole
Little Juniper Reservoir
Smoke Out Canyon Reservoir
Locust Butte Reservoir
Hanby Middle School
Patrick Elementary School
Western Baptist College
Turner Elementary School
South Albany High School
Linn - Benton Community College
Central Linn Elementary School
Plainview School (historical)
Memorial Park
Oakville School (historical)
Good Samaritan Regional Medical Center
Crescent Valley High School
Timberhill City Park
Hayesville School (historical)
Middle Grove Elementary School
Four Corners Elementary School
Eyre Elementary School
Asbestos (historical)
Springdale School (historical)
Corbett School (historical)
Little Butte Elementary School
Glen D Hale Elementary School (historical)
Sublimity Elementary School
Stayton Intermediate School
Stayton Elementary School
Stayton Bridge County Boat Ramp
Rogers Wayside County Park
Blue Star Safety Rest Area (historical)
Gervais Middle School
Brooks Elementary School
John B Humpert Park
Saint Mary's Public School
Fisher Memorial Park
Robert Frost Elementary School
Mulino Elementary School
Molalla High School
Molalla River Middle School
Dickey Bridge
Yoder Seventh Day Adventist School (historical)
Ross Bridge
Scotts Mills Elementary School
Dunagan Bridge
Kimmel Park
Minto County Park
North Fork Johnson Creek
Boring Middle School
Oakridge School (historical)
Barnard Bridge
Errin Campground
Bohemia Saddle County Park
Staples Covered Bridge (historical)
Sharps Creek Wayside
Wildwood Falls County Park
Elkhorn Woods Park
Camp Cascade
Hollydale Elementary School
Russell Middle School (historical)
Portland Adventist Elementary School
Carver School
Redland Elementary School
Eagle Creek Elementary School
River Mill Elementary School
Salmon Creek Park
Crabtree School (historical)
Centennial Elementary School
Old Barnard Bridge
Hampton Park (historical)
Ivan Oakes Park
Signal Point Recreation Area
Landax Landing Park
Roaring River Group Camp
Wendling Picnic Area
Mabel Park
Shotgun Recreational Site
Teeter Creek Recreational Area
Baker Bay County Park
Harms Park
Schwartz Park
Jasper State Park
Fall Creek County Park
Hyland Cemetery
Elijah Bristow State Park
Lowell State Park
Crawfordsville Bridge
McKercher Bridge
Independent Order of Odd Fellows Cemetery
McKercher County Park
Matlock Bridge
Waterloo County Park
Waterville School (historical)
Sodaville Mineral Springs
Garland Bridge
Long Bow Group Camp
Cascadia School (historical)
Lakes End Recreation Site
Trail Bridge Recreation Site
Olallie Recreation Site
Wildcat Mountain Research Area
Quentin Knob
Blachly Mountain Forest State Park
Elmira High School
Elmira Elementary School
Zumwalt County Park
Gardiner Landing
Elbow Lake Campground
Shag Arm
Lost Lake Campground (historical)
Siuslaw High School
Lane Community College
Rhododendron Elementary School (historical)
Spruce Point Cemetery
Siuslaw School (historical)
Munsel Creek County Park
Pacific Sunset Memorial Park Cemetery
Westlake County Park
Tyee Recreation Site
Catfish Hole
Booth Landing
Meda Bridge
Town Creek
Yach Bridge
Muscott Bridge
Weed Bridge
Otis School (historical)
Rose Lodge School (historical)
Moar Cemetery
Parkrose Middle School
McKenzie Bridge Recreation Site
Harvard Creek
Condor Bridge
Castle Creek
Lee Elementary School
Big Canyon Creek
Meredith (historical)
Ice Cap Creek Recreation Site
Gate Creek Park
Waterboard Park
Deerhorn County Park
Helfrich Landing County Park
Marten Rapids Park
Quartz Creek Picnic Area
Finn Rock Safety Rest Area (historical)
McKenzie River Elementary School (historical)
Silver Creek Landing
Forest Glen Landing County Park
Mona Recreation Site
Deadwood Landing County Park
Drift Creek
Mary Harrison School (historical)
Mid - Coast Christian School
Community Services Consortium
Toledo High School
Fuller Bridge
Oak Heights Elementary School
McDowell Creek County Park
McDowell Creek Camp
Camp Tadmor
Lewis Creek County Park
Lost Prairie Recreation Site
Tombstone Prairie Campground
Dry Creek
Dudlee Hill
Regatta Park
Eddyville Charter School
Eddyville School (historical)
Willamette Leadership Academy
Creswell High School
Creslane Elementary School
Creswell Middle School
Lincoln Middle School
Bohemia Elementary School
Latham Elementary School
Mary White Bridge
Lorane Elementary School
Heck and Gone
Blue Mountain Forest State Scenic Corridor
Nibley (historical)
Clem School (historical)
Camp Morrison
North Wilson Reservoir
DeArmond Park
Dogwood Recreation Site
Cougar Camp
Yellowbottom Recreation Site
Larwaood Wayside County Park
Mayville School (historical)
Beaver Marsh State Airport
Beaver Marsh Safety Rest Area
Hatfield Marine Science Center - Oregon State University
Silver Lake Elementary School (historical)
Camas Creek Corral
Stahlman Creek
Middle North Falls
Skookum Tum Tum Park
Abiqua Creek Park
Camp Peterson
North Silver Creek Youth Camp
North Fork County Park
Butler Ranch
Munkers Ranch
Murphy Brothers Ranch
Perry Ranch
Hinkle Ranch
Hanna Reservoir
Hilgard Junction State Park
Contorta Point Recreation Site
Cow Canyon Safety Rest Area
Salt Creek Safety Rest Area (historical)
Jungle Creek
Windfall Creek
Junco Creek
Engineer Creek
Gobblers Knob
Temple Ranch
Nelson Ranch
Hardesty Ranch
Robertson Ridge
Crane Union High School
Old Graham Homestead
Jameson Ranch
Reed Ranch
Upper Sherman Ranch (historical)
Harris Ranch
Robertson Ranch
Crane Elementary School
Pine Creek Ranch
George Clark Ranch
Joel Sword Ranch
Jack Miller Ranch
Shelly Ranch
George Riley Ranch
Cleveland Ranch
Azley Acton Cow Camp
Jack Bear Cabin
Illahe Riffle
Whiskey Creek
Zimmerman Butte
Sweet Myrtle State Natural Site (historical)
Harris Butte
Stanchion Creek
Corral Creek
Ripple (historical)
Preston (historical)
Buick (historical)
Snark (historical)
Maples (historical)
Nehalem Falls (historical)
Knudson (historical)
South Fork Wind Creek
Ziolkouski Beach Park
Masonic Cemetery
Kennedy Slough
Southside County Park
Champion Park
Willard (historical)
Bufo (historical)
North Lake (historical)
Windy Cove County Park
Oak Rock County Park
Salmon Harbor County Park
Umpqua City (historical)
McIntosh Slough
Barneburg Hill
Suncrest Safety Rest Area
Tunnel Ridge Recreation Site
Little Applegate Recreation Site
Talent Middle School
Frazier Gulch
Gleneden Beach State Park
Kirtsis Park
Oceanlake Elementary School
Devils Lake State Park
Delake School Elementary (historical)
Taft High School
Canyon Drive Park
Cape Perpetua Recreation Site
Black Mountain Creek
White River Falls State Park
Sam Case Elementary School
Yaquina View Elementary School
Eureka Cemetery
Hurbert Creek
Taft Elementary School
Taft Park
Josephine Young Memorial Park
Fremont Bridge
Plevna (historical)
Keno Bridge
Susie Creek
Crandall Creek
Carl G Washburne Memorial State Park
Tokatee Kloochman State Natural Site
Alder Lake Camp
Mercer Lake County Park
Dune Lake Park
Houghton Landing County Park
Funke Bridge
Bender Landing County Park
Munsel Landing County Park
Shepards Point
Crystal Creek County Park
South Island Campground (historical)
Red Lake Campground (historical)
Island Lake Campground (historical)
South Lake Campground (historical)
Cliff Lake Campground (historical)
Grass Lake Campground (historical)
Grass Lake Campground Number 2 (historical)
Alta Campground (historical)
Mahogany Ridge Reservoir
S'Ocholis Campground (historical)
Flat Lake
Quarry Reservoir
Saddle Mountain Spring
Junction Reservoir
Pothole Reservoir
West Canal
Klamath Wildlife Area
Merganser (historical)
Plevna Ditch
Madison Elementary School
Sunset Middle School
Huntley Park
RAAB Recreation Site
Two Rivers Recreation Site
Sunstrip Recreation Site
Whitewater Forest Camp (historical)
Three Lynx School (historical)
Dry Creek
River Ford Recreation Site
Doaks Mountain
Oux-Kanee Recreation Site
Chiloquin Elementary School
Chiloquin High School
Bray Mill (historical)
Wood River Recreation Site
Middley Bridge
Fort Klamath Park and Museum
Spring Creek Recreation Site
Petric County Park
Henzel County Park
Pothole Well Guard Station
Topsy Recreation Site
John C Boyle Reservoir
Spencer Bridge
Yainax Guard Station
John Cole Spring
Whitney Bridge
Lost River High School
Stevenson Park
Blue Lake Camp
Pear Lake Camp
Carney Lake Camp (historical)
Meadow Lake Camp
Rogue Head Camp
Beaver Dam Recreation Site
Daley Creek Recreation Site
Pole Bridge Campgound (historical)
Lilyglen (historical)
Quartz Creek
Penny Ante Mine
Miller Cemetery
Brownsboro Cemetery
Burbank Creek
Grizzly Camp
Jacksonville Hill
Cattle Creek
Hooper Springs County Wayside
Spout Spring
Mount Ashland Ski Area
Bull Gap Campground (historical)
Murphy Elementary School (historical)
Lincoln Savage Middle School
New Hope Christian Schools
Hidden Valley High School
Riverside Elementary School
South Middle School
Fall Creek Recreation Site
Cougar Creek
Mace Creek
Scaredman Creek Recreation Site
Wapiti Creek
Fracture Creek
Diamond Lake Trailer Camp Area
Jackson Creek
Surprise Creek
Ravel Creek
Zag Creek
Zig Zag Creek
Mellow Moon Creek
Call Creek
Black Jack Creek
Bluff Creek
Twin Cedar Creek
Middle Mountain Creek
Cleft Creek
Hurry Up Creek
Cobble Creek
Stony Creek
Pebble Creek
Brouse Creek
Illahee Spring
Buzzard Bay County Park
Scott Creek County Park
Brown Cemetery
South Umpqua Safety Rest Area
Burkhart Rapids
East Shore Recreation Site
Loon Lake Recreation Area
Umpqua River Safety Rest Area (historical)
Murphys Camp (historical)
Scottsburg Park
Merritt Reservoir
Bedfield (historical)
Nimrod River County Park
Gem Pond
Melvins Pond
Kodiak Pond (historical)
Jackson Ridge
Skeeter Butte
Gordon Lake
Blue Buck Camp
Coyote Bucket Pond
Pelican Reservoir
Pelican Bay Camp (historical)
Yamsi Reservoir
Wildhorse Reservoir
Willow Pond
Airstrip Pond
Guard Pond
Little Hole Reservoir
Bootleg Pond
Miller Pond
Tree House Pond
Buck Spring Pond
Raymonds Pond
Raymonds Camp (historical)
Some Chance Pond
Knife Pond
High Table Pond
Dibbon Cook Spring
Heceta Beach County Park
Riverside Psychiatric Hospital
Linn-Benton Community College (historical)
Legal Waterhole
Kilchis River Jetty
Long Hollow
Schindler Landing County Park
Archie Knowles Recreation Site
Harbor Vista County Park
Wendson Substation
Tahkenitch substation
Fall Creek Work Center
Fall Creek National Recreation Trail
Cedar Creek Administration Site Fish Hatchery
Elk Flats Recreation Site (historical)
Monon Lake Recreation Site (historical)
Horseshoe Lake Recreation Site
Barlow Crossing Recreation Site
Camp Comfort Recreation Site
Clover Creek
Corral Spring
Eightmile Crossing Recreation Site
Elk Creek Recreation Site
Frissell Crossing Recreation Site
Government Camp
Indian Ford Creek
North Fork Crossing Forest Camp
Salmonberry Creek
Taylor Place (historical)
Toad Lake
Wildwood Recreation Site
C 2 Lumber Camp
Illinois Valley Airport
Fort Miner (historical)
Camp Six
Oxbow Hatchery
Hartley Park
Rochester Covered Bridge
Lake Diane
Lawrence Reservoir (historical)
Indian Burial Ground
Reeher CCC Camp (historical)
Consolidated Timber Company Camp (historical)
Johnson Lake
Barr Bridge
Witzig Reservoir
Stark Reservoir
LRM Pond
Pleasant Valley
Wellspring Reservoir
Holly Reservoir
Groner Elementary School
Vierra Springs
Tilikum Lake
Slide Creek
Mulkey (historical)
Somerset Meadows Park
Bonny Slope Park
Pioneer Park
Foothills Park
Peppertree Park
Commonwealth Lake Park
Willow Creek Park
Whispering Woods
Salix Park
Pheasant Park
Saint Johns Bridge
Saint Marys Regional Park (historical)
Krueger Pond
Cedar Hills Park
Meadowhurst
Johnson Spring
Cedar Mill Pond
Saint Marys (historical)
Parcourse Park (historical)
Saltzman Creek
Tanasbrook Reservoirs
Washington County Home
Hembree Reservoir
Jackson Reservoir
Jackson Quarry Reservoir
Teufel Reservoir
Bastion Reservoir
Falkenberg Reservoir
Luscher Reservoir
Leichtman Sump
Rufener Reservoir
Haynes (historical)
Varley (historical)
Baker Creek
Verboort Reservoir
Van Loo Reservoir
Hillsboro Pioneer Cemetery
Mount Olive Lutheran Cemetery
Havens Reservoir
Seventh Day Adventist School (historical)
Masonic Cemetery
Wil-Lyn Reservoir
Folsom Pond
Lakeview Slough
Ballins Mill (historical)
Leffler Grade
Elkhorn Woods
Perkins Mill (historical)
Ferguson Cemetery
Montgomery Creek
Johnson Slough
Nisly Reservoir
Drazdoff Reservoir
Adair Air Force Station (historical)
Verley Pond
Brugato Reservoir
Yeagers Landing (historical)
Elwart Reservoir
Shady Dell Reservoir
Howell Spring
Krause Springs
Brookforest Pond
Freitag Reservoir
Coffee Lake Creek
Corral Creek (historical)
Nuffer Reservoir
Faloma
North Umpqua Village
Susan Creek Falls Recreation Area
Swiftwater Park
Wimberly Family Cemetery
Glide Junction
North Umpqua Ranger Station
Williams Creek
The Narrows
Faults Creek
Doerner Reservoir
La Brie Family Cemeteries
Lehman Reservoir
Cougar Spring
Strong Reservoir
Black Canyon
Dollar Log Ponds
Twin Harbor Log Pond
Mill Creek Reservoir
Superior Log Pond
Wolf Creek Pools
Ehlig Reservoir
Fort Leland (historical)
Poe Spring
Big Spring
V T Jackson County Wayside
Anderson Reservoir
Kenney Reservoir
Henline Falls
Clay Creek
Rogers Creek
Red Rock Hill
Slide Point
Brix Creek
Triangulation Point
Camp Cooper Reservoir
Anglersvale (historical)
North Fork Falls
West Fork Plympton Creek
Cow Creek
Gnat Creek Falls
Boxler Creek
Horseshoe Camp
Tandy Creek
Fishhawk Creek
Warner Creek
Nelson Creek
Grub Creek
Cougar Creek
Vesper
Neverstill
Kauppi Lake
Falls Creek
Buck Creek
Douty (historical)
Blue Lake Lookout
Eureka Bar
Quincy Reservoir
Dibblees Beach
Cottonwood Beach
Red Mill Beach
Winters Spring
Pruitt Reservoir
Martin Creek
Big Spring
Mist Cemetery
Pisgah Lookout
Jim George Creek
Clatsop County Home
Weather Bureau Tower
Tongue Point Lighthouse
United States Navy Radio Tower Number One
United States Navy Radio Tower Number Three
Upper Sands
Quarantine Anchorage
Green Spring
Arlington Masonic Cemetery
Oatman Junction
Chase (historical)
Bud Spring
Lost Park
Howard M Terpenning Recreation Complex
Seely Ditch
Calvin Creek
United States Navy Radio Station
Independent Order of Odd Fellows Cemetery
Willow Creek
Earthquake Spring
Prescott Bar
North Douglas Log Ponds
Abiqua Basin
Abiqua Falls
Academy Junior High School (historical)
Media Arts Communication Academy
Agency Creek
Airlie
Airlie Creek
Aldrich City Park
Alecs Butte
Amity
Apostolic Cemetery
Arbor Creek
Ash Creek
Ash Creek
Ash Swale
Aurora Cemetery
Peter Boscow Elementary School (historical)
Bagley Park
Baker Elementary School (historical)
Mount Baldy
Ball Cemetery
Ballston
Barneys Butte
Barneys Butte Waterhole
Barrick Field City Park
Baskett Slough
Baskett Slough National Wildlife Refuge
Bausch Creek
Mount Beachie
Beardsley Bar
Beaver Creek
Beaver Creek
Belcrest Memorial Park
Belle Passi Cemetery
Bellevue
Ben Smith Creek
Bend in the Creek Spring Reservoir
Berger Lake
Berry Creek
Bingham Park
Bledsoe Creek
Blitzen Creek
Bowers Slough
Box Canyon Creek
Boyle Lakes
Gracemont City Park
Bridgeport
Brier Pond
Broadacres (historical)
Brookwood Elementary School
Brunks Corner
Brush College City Park
Brush College Elementary School
Buchanan Reservoir
Buckskin Lake
Buell
Buena Vista
Bull of the Woods
Bump Creek
Burgett Creek
Burns Corner
Bush's Pasture City Park
Bush Elementary School
Butler Davidson Cemetery
Butte Creek School
CCC Reservoir
Cachebox Meadow
Cadle Hill
Calloway Creek
Camp Winema
Cape Kiwanda
Carlton
Carlton Lake (historical)
Carlton Lake Wildlife Refuge
Carnation
Cascade Junior High School
Cascade Senior High School
Case Creek
Cemetery Hill
Central Cemetery
Central School (historical)
Central School (historical)
Champoeg
Champoeg Creek
Champoeg Monument
Champoeg State Park
Chandler Lake
Chapman Corner
Chapman Hill
Chehalem Center School (historical)
Chehalem Creek
Chehalem Mountains
Cherry Grove
City View Cemetery
Clackamas River
Claggett Creek Park
Clark Creek
Clarmount Park
Clayton Creek
Clear Creek
Cliff Creek
Cloverdale Elementary School
Clow Corner
Cockerham Creek
Coffin Butte
Cold Creek
Columbus Elementary School
Comer Creek
Cook Creek
Cook Elementary School (historical)
Cooper Hollow
Copp Reservoir
Cornelius
Cosper Creek
Cove Orchard
Coyote Reservoir
Cozine Creek
Crabtree Creek
Crider Pond
Cronin Creek
Cummings Elementary School
Cupids Knoll
D and Winter Park
Winema Lake
Dallas
Dallas Cemetery
Davidson Bridge
Davies Spring
Dawson Creek
Dayton Prairie
Deer Creek Cemetery
Dellwood (historical)
Derry
Detour (historical)
Devils Lake Fork
Dickens Cemetery
Dickey Creek
Dilley Creek
Doane Creek
Dog Ridge
Donald
Doves Bar
Downs Lake
Drift Creek
Drift Creek Falls
Dry Creek
Dunning Creek
Dupee Creek
Durbin Waterhole
Dutch Creek
Dutch Creek
East Champoeg Creek
East Fork Drift Creek
East Fork Marys River
East Humbug Creek
Ediger Reservoir
E E Wilson Game Management Area
Elk Creek
Elk Creek Campground
Ellendale Creek
Elliott Creek
Elliott Prairie
Elliott Prairie Christian School
Embree Cemetery
Englewood Elementary School
Eola Crest
Eola Village
Evans Creek
Evergreen Memorial Park
Fairmont City Park
Falls City
Fargo
Fast Cemetery
Fellers
Fern Corner
Fern Creek
Fern Hill Cemetery
Fern Ridge
Fern Rock Creek
Fernwood School (historical)
Fidler Creek
Fir Lawn Cemetery
Fir Villa
Fish Creek
Forest Grove
Forest Grove Junction
Foster Flat
George Fox University
French Prairie
Yamhill County Friends Cemetery
Friesen Reservoir
Fuller Creek
Gale Hill
Gales Creek
Garfield School (historical)
Garrish Valley
Garry Lake Waterhole
Gearins Ferry (historical)
Gentle Woods Park
Gibson Gulch
Giesy Mineral Spring
Gilmore Field City Park
Gingles Cemetery
Glenbrook Creek
Glencoe
Glenn Creek
Gold Creek
Gold Creek
Goodin Creek
Goodwin Branch Mud Slough
Gooseneck Creek
Gooseneck School
Graham Bridge
Grant Creek
Grant Community School
Green Crest Memorial Park
Greens Bridge
Greenwood School (historical)
Grice Hill
Grindstone Ridge
Grouse Butte
Haines Cabin
Hamilton Reservoir
Happy Acres Memorial Hospital (historical)
Harland Slough
Hart Riggs Cemetery
Harvey Clarke Elementary School
Harvey Creek
Hawn Creek
Hay Creek
Hayden Lake
Hayden Slough
Helmick Hill
Sarah Helmick State Park
Hembre Ridge
Hering Creek
Hess Creek
High Water Slough
Highland Elementary School
Hill School (historical)
Hillcrest Cemetery
Hillsboro
Hito
Hoekstre Reservoir
Hoekstre Slough
Hoover Park
Hopewell Cemetery
Mount Horeb
Hospital Hill
Hubbard
Hubbard Mineral Spring
Humbug Lake
Hutchcroft Creek
Idaville
Idiot Creek
Illahe Hill
Independence
Indian Creek
J W Poynter Middle School
Jack Creek Reservoir
Jackass Creek
Jackson Creek
Jefferson
Jefferson Cemetery
Jefferson High School
Jerrys Lake
Jont Creek
Jordan Creek
Joseph Gale Elementary School
Judson Middle School
Juniper Spring Creek Reservoir
Kay Hill
Keg Springs
Keg Springs Reservoir
Keg Springs Rimrock Reservoir
Keg Springs Valley
Keizer
Keizer Bottom
Kennedy Elementary School
Kiel Creek
Kiwanda Beach
Lacreole Middle School
Lady Creek
Lakeview School (historical)
Laurel Creek
Laurelwood
Laurelwood Adventist Elementary School
Lee Mission Cemetery
Lee City Park
Leisy School (historical)
Howard Street Charter School
Letteken Ponds
Lewisburg
Lewisville
Liberty
Libolt Reservoir
Lincoln School (historical)
Linfield College
Little Luckiamute River
Little Nestucca River
Little Sardine Creek
Locke Cemetery
Logsden Ridge
Lost Lake
Lower Herlihy Reservoir
Lower South Falls
Luckiamute River
Lunnville
Lyle Elementary School
Lytle Creek
Mabel Rush Elementary School
William P Lord High School
Maple Creek
Maple Grove (historical)
Maple Park
Marion
Marion Friends Cemetery
Marion Creek
Marion Square City Park
Marten Buttes
May Creek
Mayflower Creek
McAlpin School (historical)
McBride Cemetery
McCarthy Slough
McCrae Reservoir
McKinley Elementary School
McMahan Branch
McMinnville
McNary Creek
McTimmonds Valley
Memorial Elementary School
Merle
Middle Fork Ash Creek
Middle Herlihy Reservoir
Mill Creek
Mill Creek
Mill Creek
Mill Creek County Park
Mill Creek Recreation Site
Mill Creek School (historical)
Miller Butte
Minto (historical)
Minto
Mission Creek
Mission Ditch
Mitchell (historical)
Monitor
Monmouth
Montgomery Cemetery
Moore Creek
Morgan Creek
Morningside City Park
Morningside Elementary School
Morris Bridge
Mount Hope Cemetery
Mountain View Creek
Mountain View Elementary School
Mountain View School (historical)
Mountaindale
Mud Slough
Munsey Lake
Murphy Creek
Nestucca Bay
Nestucca River
New Hole Reservoir
North Fork Ash Creek
North Fork Kilchis River
North Fork North Fork Trask River
North Fork Norton Creek
North Fork Silver Creek
North Marion High School
North Plains
North Salem High School
North Spit
North Yamhill River
Oak Point Creek
Oleman Creek
Olinger Pool Park
Western Oregon University
Oregon State Capitol
Oregon State Fairgrounds
Oregon State University Test Field Laborator
Orenco
Pacific University
Panther Creek
Panther Creek
Parrish Middle School
Patton
Patton Valley
Pedee
Pedee School (historical)
Peters Pond
Pettijohn Creek
Pettit Reservoir
Pike
Pinckney (historical)
Pioneer Cemetery
Mount Pisgah
Pleasant Hill Pioneer Cemetery
Riverview City Park
Popcorn School (historical)
Porter Point
Powers Creek
Pratum Cemetery
Pringle Creek
Pringle City Park
Quartz Creek
Quatama
Red Prairie
Restlawn Memory Gardens Cemetery
Rice Rocks
Richards Creek
Richmond Elementary School
Rickreall
Rickreall Creek
Ridders Pioneer Cemetery
Ritner
Ritner Creek
River Road City Park
Fran Wilson Riverside Park
Roberts
Rock Creek
Rock Creek School
Rocky Butte
Rocky Butte Waterhole
Rowell Creek
Rowell Creek
Roy (historical)
McRae City Park
South Saddle Mountain
Sain Creek
Saint Barbara Cemetery
Saint Francis Cemetery
Saint Francis of Assisi School
Saint James Cemetery
Saint James Catholic Schools
Saint Joseph
Saint Louis School (historical)
Saint Lukes Cemetery
Saint Paul
Saint Vincent de Paul Catholic School
Salem Heights Elementary School
Salmon River
Salt Creek (historical)
Salt Creek
Salt Creek
Salt Creek Cemetery
Santiam River
Sardine Mountain
Schefflin
Schefflin School (historical)
Schrag Cemetery
Scoggins Slough
Scotts Mills
Senecal Creek
Sewell
Shaw Creek
Shelton Ditch
Sheridan
Shipley
Short Mountain
Shute Park
Sidney Ditch
Simpson (historical)
Sinker Creek
Skookum Lakes
Smithfield
Smuggler Cove
Soap Creek
South Fork Ash Creek
South Fork Camp
South Fork Jackass Creek
South Fork Kilchis River
South Fork Norton Creek
South Fork Wilson River
South Salem High School
South Slough Pond
South Yamhill River
Spring Branch
Spring Creek
Staats Hollow
Stag Hollow Creek
Starkey Corner
Stimson Mill
Sucker Slough
Sunday Creek
Talmadge Middle School
Tanner Creek
Taylor Cemetery
Taylor Lake
Teal Creek
Thielsen
Thomas Creek
Tietz Hill
Tillamook State Forest
Timbuktu (historical)
Tindle Creek
Tuality Community Hospital
Old Scotch Cemetery
Tucke Lake
Tumble Rock
Tustin Lake
Twin Road Waterhole
Tyson Island
Tom McCall Upper Elementary
Union Hill Cemetery
Union Hill Grange
University Falls
Upper Hawkins Reservoir
Upper Herlihy Reservoir
V Canyon
Valley Junction
Vaughn Creek
Verboort
Visitation Cemetery
Voss Hill
Votaw (historical)
Waldo Hills
Walker Middle School
Walker Park
Walkers Corner
Wall Reservoir
Wallace Bridge
Wallace Hill
Wallace Marine City Park
Wallinch (historical)
Waymire Creek
Wells Island
Wells Landing
West Branch Ash Swale
West Champoeg Creek
West Fork Drift Creek
West Fork Elk Creek
West Keg Springs Waterhole
West Salem
West Union
West Union Cemetery
West Union Elementary School
West Woodburn
Whiteson Bridge
Whitworth Elementary School
Widow Creek
Wigrich
Wildwood Creek
Willamette Slough
Willamette University
Willamina
Willamina Creek
Williams Canyon
Wilson River
Winch
Windless Reservoir
Wirtz Branch
Womer Cemetery
Woodburn
Woods Point
Yamhill Creek
Yamhill River
Yamhill - Carlton Cemetery
Bellevue - Yocum Cemetery
Zena
Zena Cemetery
Rainbow Cove
Juniper Creek
Camel Lake
Butler (historical)
Indian Cemetery
Hussey Cemetery
Suttner Reservoir
Lind Reservoir
Jackson Cemetery
North Plains School
Harrison Cemetery
Cornelius Elementary School
Rogers Park
Tuality Forest Grove Hospital
Echo Shaw Elementary School
Neil Armstrong Middle School
Cornelius Lutheran Cemetery
Council Reservoir
S I C Reservoir
Walters Reservoir
South Fork Hill Creek
North Reservoir
Evergreen Junior High School
W Verne McKinney Elementary School
Eastwood Elementary School
Indian Hills Elementary School
Ladd Acres Elementary School
Mooberry School (historical)
Lenox Elementary School
Storey Creek
Scoggins Dam
Stimson Millpond
Muskrat Pond
Cherry Grove Cemetery
Black Jack Creek
Mennonite Cemetery
Elk Horn (historical)
Red Prairie Creek
Berkey Creek
Harrison (historical)
Hidden Lake Reservoir
Harrison Lake
Wabash (historical)
Tucker (historical)
Staats Reservoir
Chatnicka Creek
Minto-Browns Island City Park
Santiam City (historical)
Pacific Plywood Log Pond
Willamina Reservoir
Willamina Cemetery
Harmony Cemetery
Bourland Reservoir
Aebi Reservoir
Masonic Cemetery
North Branch Cozine Creek
Peavey Reservoir
Holmes (historical)
Johnson Creek
Mathew Spring
Neuschwanger Reservoir
Emerson Reservoir
Ingebrand Reservoir
Scharf Reservoir
Green Acres Reservoir
Byerley Corner
Buhler Reservoir
Larson Reservoir
Tellin Reservoir
Stewart Reservoir
Crescent Hill
Masonic Cemetery
Wilson Reservoir
Maple Mound Reservoir
Mineral Creek
Myers Reservoir
Beyers Pond
Greenwood (historical)
Stapleton
Halls Ferry Cemetery
Independence Bend
Monmouth Reservoir
Cemetery Hill Cemetery
Lundeen Reservoir
Helmick (historical)
Buena Vista Cemetery
G P Reservoir
Bryant Lake Bed
Peavey (historical)
Randall Pond
Camp Adair (historical)
Calloway (historical)
Bush
Keizer Rapids
Salemtowne
Brush College
Haines Reservoir
Gibson Reservoir
Croft Reservoir
Kinsey Reservoir
Gilliam Swale
Ferns (historical)
Luckiamute (historical)
Winegar Reservoir
Putnam (historical)
Crisp (historical)
Fidel Brothers Irrigation Reservoir
Yamhill Station (historical)
Beulah City Park
Batan (historical)
Pioneer Community Hall (historical)
Oberg Reservoir
White Cloud Community Hall (historical)
Sitton Reservoir
Gidding Reservoir
Stevens Reservoir
Riverside (historical)
Idiotville (historical)
Fern Rock Rest Area
Boys Cemetery
Aumsville Elementary School
Bell Road Creek
Lockhart Reservoir
Web (historical)
Springbrook Middle School (historical)
Newberg Senior High School
Jaquith Park
Edwards Elementary School
Renne Middle School (historical)
G A R Cemetery
Brandy Creek
Fry Creek
Fry Reservoir
Hoch Reservoir
Lauterman Creek
Superior (historical)
Stiles Reservoir
Bowersville (historical)
Trom Reservoir
Willamette Log Pond
Steen Reservoir
Falls City Cemetery
Frink Reservoir
Carey (historical)
Morgan Reservoir
S M S Reservoir Number One
Clymer (historical)
South Fork Pudding River
Millford (historical)
Stadeli Reservoir
Beaver Creek Reservoir
Spady Reservoir
Lewis Reservoirs
Worden (historical)
Kinsey Reservoir
Dyer Reservoir
McBee Reservoir
Aebi Reservoir
Classen Reservoir
Domaschofsky Reservoir
Blanchard Reservoir
Stamy Reservoir
Nesmith Mills (historical)
Crosby Reservoir
O'Neal Reservoir
Woodburn Academy of Art Science and Technology
Saint Luke School
Legion Park
Washington Elementary School
Nellie Muir Elementary School
Settlemier Park
Mclaren Cemetery
Serres Reservoir
Newellsville (historical)
Tribbett Reservoir
Zorn Pond
Murphy Creek
Wilmes Reservoir
Monitor Elementary School
Marquam Reservoir
Butte Creek (historical)
Nowlen Bridge
Lone Pine Corner
Mill Creek
Orr Creek
Pierce Creek
Wonder Creek
Marion School (historical)
Edgar Slough
Independence Prairie
Novak Slough
Gaines (historical)
Harvstack Reservoir
Wilson Reservoir
Arstell Creek
Commons Creek
Fletcher Spring
Bye Reservoir
Olge Reservoir
Miles Creek
Williams Cemetery
Meadow Creek
Ewing Young Park
Teats (historical)
Little Sweden
Buckhorn Creek
Packsaddle Creek
Pleasant Grove - Condit Cemetery
Gist Cemetery
Wigrich Airfield (historical)
Vineyard Airport
Western Division Service Center Airport (historical)
Pacific Plywood Corporation Dam
Davidson Ranch Airstrip (historical)
Capital Mall Heliport
Cascade Airstrip (historical)
Mount Pleasant Cemetery
Siegmund Reservoir
Lewis Cemetery
Echo Creek
Moss Lake
Goober Creek
Upper North Falls
Phil Olson Reservoir
Phil Olson Dam
Blue Heron Reservoir
Ingebrand Dam
Lind Dam
Graham Dam
Vanderzanden Reservoir
Ornoname 24 Dam
Dejong Dam
Hawn Creek Dam
Fidel Brothers Irrigation Reservoir Dike
McKay Reservoir
Art McKay Dam
Martin Brothers Flashboard Dam
Wendell Kreder Dam
Helms Dam
Kohlmeyer Private Airstrip (historical)
Lafayette Airstrip
Marr Field
McMinnville Municipal Airport
McLagan Airstrip (historical)
Mountaindale Airstrip (historical)
Mount Jefferson Lumber Company Airstrip (historical)
Joe Cards Airpark (historical)
Gates Airport
Kingston Airpark
Portland-Hillsboro Airport
Salem General Unit Hospital Heliport
Abba's Airport
Skyport Airport
Sportsman Airpark
Steel Systems Airstrip (historical)
Sunset Air Strip
North Plains Gliderport
Flying E Airport
Boundary Creek
Summit Creek
Sibley Creek
Phipps Creek
South Santiam (historical)
Renner (historical)
Bussard (historical)
Randall Hill
Zigzag Canyon
Sam Downs Creek
North Fork Valentine Creek
South Fork Valentine Creek
Aders Sump
Trask Creek
Rowland Creek
Independent Order of Odd Fellows Cemetery
Boulder Ridge
Marten Creek
Barnes Brothers Reservoir Dam
Croft Dam
Glenn Walters Dam
Oak Crest Farm Dam
Oak Crest Farm Reservoir
Oberg Brothers Dam
Oscar Dam Number 4429
Oscar Reservoir Number 4429
S M S Dam Number 1
Cabin Creek
Crater Lake
Crater Lake National Park
Mount Mazama (historical)
Albany Golf Club
Astoria Country Club
University of Oregon Autzen Stadium
Bachelor Ski Lift (historical)
Balboa Park Drag Strip (historical)
Bandon Gun Club
Battle Creek Country Club
Bend Seed Extractory
Bone Spring Lookout (historical)
Bonneville Power Station
Broadmoor Golf Course
Bronaugh Memorial Plaque
Buxton Lookout Tower
Cascade Salmon Hatchery
Cazadero Powerhouse
Circle Bar Golf Club
Clatsop Fire Tower
Clear Lake Golf Course
Columbia Edgewater Golf Club
Colwood National Golf Club
Compressor Station Number 9
Cooper Spur Ski Area
Coos Golf Club
Copco Powerhouse
Corvallis Country Club
Country Plaza Golf Course
Denny Creek Historic Monument
Dorion Historical Marker
Dunaway Pumping Station
Earl Snell Birthplace Historical Monument
Eastmoreland Golf Course
Eugene Country Club
Eugene Speedway (historical)
Eugene Yacht Club
Evergreen Golf Course
Ewing Young Historical Marker
Fall River Fish Hatchery
Flat Lake Lookout Tower
Forest Hills Golf Course
Gearhart Golf Course
Glendoveer Golf Course
Goodman Lookout Tower
Grants Pass Country Club
Greenacres Golf Range (historical)
H H Wheeler Historical Marker
High Heaven Lookout Tower
Joseph L Meek Land Claim Historical Marker
Hoodoo Lookout Tower
Hoodoo Ski Bowl
Illahe Hills Country Club
Jason Lee Mission Historical Marker
Jones Number 2 Pump
Juniper Golf Course
Kent Compressor Station
Kentuck Country Club
Kinzua Golf Course (historical)
Kirkland Lookout Tower
Klaskanine Fish Hatchery
Oswego Lake Country Club
Laurelwood Municipal Golf Course
Leaburg Power Plant
Lewis and Clark Salt Cairn Historic Monument
Lookout Tower
Lytle Pump
Mark Clark Golf Course
Marysville Golf Course
McBroom Administrative Study Plot
McCullock Stadium
McNary Golf Course
Meriwether Golf Course
Montague Memorial Plaque
The Courses
Nehalem Fish Hatchery
Oak Knoll Golf Course
Oak Knoll Golf Course
Oakway Golf Course
Ochoco Relift Pumping Plant
Oregon City Golf Club
Oregon City Water Patrol Station
Oregon State Correctional Institution
Oregon State Penitentiary
Oregon State Correctional Institution
Oregon State University Experimental Farm
Oregon Yacht Club
Orenco Woods Golf Course (historical)
Pendleton Country Club
Poma Ski Tow (historical)
Portland Golf Club
Portland Gun Club
Portland Hunt Club
Prineville Golf and Country Club
Pringle Falls Experimental Station
Prouty Memorial Plaque
Redmond Pumping Plant (historical)
River Mill Powerhouse
Riverside Country Club
Riverwood Golf Course
Rogue Valley Country Club
Rose City Golf Course
Salem Golf Club
Salem Gun Club
Shadow Hills Country Club
Sherman Experiment Station
Spout Springs Lookout Tower
Spring Hill Country Club
Stringer Shearing Plant
The Dalles City Waterworks
Tillusqua Fish Hatchery
Top O' Scott Golf Course
Tualatin Country Club
United State Fish and Wildlife River Testing Site
United States Weather Bureau Station
United States Bureau of Reclamation Pumping Plant E
United States Bureau of Reclamation Pumping Plant F
Walterville Powerplant
Waverly Country Club
Weatherford Historical Monument
Wildwood Golf Course
Williamson River Pumping Plant
Ocean Dunes Golf Links
Ornoname 4 Dam
Ornoname 3 Dam
Ornoname 2 Dam
Ornoname 9 Dam
Ornoname 11 Dam
Ornoname 8 Dam
Ornoname 12 Dam
Ornoname 5 Dam
Ornoname 13 Dam
Ornoname 22 Dam
Lake Merritt
Lake Merritt
Agate Beach Golf Course
Salishan Golf Course
Olalla Valley Golf Course
Chinook Winds Golf Resort
Neskowin Marsh Golf Course
John C Boyle Power Plant
McKenzie River Golf Course
Mount Rose
Lake Creek Trail
Ornoname 7 Dam
Ornoname 10 Dam
Ornoname 14 Dam
Ornoname 15 Dam
Ornoname 16 Dam
Ornoname 17 Dam
Ornoname 18 Dam
Ornoname 21 Dam
Lake Selmac County Park
Lake Creek
Lake Ridge Creek
Black Hills Lookout
Hatinger Creek
Doerner Creek Reservoir
Wylie Reservoir
Smith Reservoir
Cleveland Log Ponds
Dickerson Canyon
Upper Olalla Valley
Porter Hill
Sibold Canyon
Porter Creek
Tenmile Valley
Reston Ridge
Morgan Hill
Tamura Reservoir
McGill Reservoir
Clear Creek Park (historical)
Cotton (historical)
Preston (historical)
Kunitake (historical)
Riverside (historical)
Siefer (historical)
McMurray Ferry
Norris (historical)
Fir Hill Cemetery
Peterson Crossroads
Gavins Pond
Sandy Ridge (historical)
Scenic (historical)
Cottrell Station (historical)
Mayberry (historical)
Gillis (historical)
River Mill (historical)
Cazadero (historical)
Alspaugh (historical)
Highland Store (historical)
Union (historical)
McIntyre Reservoir
Deep Creek (historical)
Van Zyl Reservoir
Rays Spring
Connors Ponds
North Highland
Rock Creek
South Fork Bee Creek
Independent Order of Odd Fellows Cemetery
Rattlesnake Grade
Borstel Pond
Boeing Test Site
Papersack Cemetery
Irby Reservoir
Thorn Hollow Grade
Agency Indian Cemetery
Tutuilla Presbyterian Indian Mission Cemetery
Valley View Drain
Hahilly Reservoir Number Four
Crane Wells
Robberson Reservoir
Derr Pond
Jasper - Wallace Cemetery
Smith - Weyerhauser Cemetery
Coburg IOOF Cemetery
East Springfield (historical)
Maple Island (historical)
Merriams Slough (historical)
Royal Delle Park
Springfield IOOF Cemetery
Stumptown (historical)
Westmoreland City Park
Zinker Reservoir
Cord (historical)
Dogs Reservoir
Rockville Seeding Reservoir Number One
Rockville Seeding Reservoir Number Two
Pisa Paa Ta Tsi Tsa-da Reservoir
Owyhee Reseeding Reservoir
Antelope Reservoir
Campbell Reservoir
Varment Creek Reservoir
Red Tank
Five Points Reservoir
Pole Creek Reservoir
Baltzar Spring
Fenwick Spring
Cow Creek Slough
Baxter Creek
Baxter Spring
Cline Hill Summit
Riddle Rim
Shifting Sands Reservoir
Agate Field
Red Butte Lookout Tower
Cavitt Lake
Hansen Valley
Carmen Lake
Grasshopper Spring
Grasshopper Meadow
Skookum Pond
Doyle Ranch
Upper Twomile School (historical)
Bear Creek Cemetery
Buck Spring
Fort Jones Creek
Barn Canyon
Bad News Reservoir
Big Bend Reservoir
Corral Reservoir
Bellmare Reservoir
Little Flat Reservoir
Black Sage Reservoir
Overshoe Well
Mendi Gori Posue
Basque Well
Crater Creek
Dry Lake Waterhole
Muddy Water Spring
Shanks Landing (historical)
Ottawa Landing (historical)
Century Park
Independent Order of Odd Fellows Cemetery
Masonic Cemetery
West Switchback (historical)
Fitzgerald Reservoir Number Two
Draw Fork Waterhole
Pine Spring
Harper Cemetery
Westfall Cemetery
Munkers Spring
Reason - Reed Cemetery
Breitenbush Cascades View Point
Johnson Ditch
Quaking Aspen Spring
Indian Rapids (historical)
Squally Hook Rapids
Schofield Rapids (historical)
Upper John Day Rapids (historical)
Lower John Day Rapids (historical)
Jackass Canyon
Warrior Rock Light
Columbia Heights
Frogmore Slough
Honeyman (historical)
Bachelor Flat (historical)
Duck Club Light
Henrici Range
Henrici Bar (historical)
Henrici Landing (historical)
Gay Lake
Henderson Creek
Odell Hollow
Payne Ridge
Milk Butte
Homestead Butte
Ryegrass Ranch
Summit Reservoir
Maupin Spring
Post Office Bar (historical)
Riverview (historical)
Ban (historical)
Armona (historical)
Sauvies (historical)
Wilhoit Mineral Springs
Vale Hot Springs
Water Tower Number Two
Water Tower Number Four
Jamieson Gulch Reservoir
Three Forks Reservoir
Channel Reservoir
Henry Gulch Reservoir
Vale Valley
Upper Pump Canal
Larson Island
Fairview Cemetery
Star Creek Ditch
Cox Cemetery
Kink Spring
Maryhill Ferry (historical)
Woods Bar Light
Nitchman Reservoir
John Place Reservoir
Shadybrook (historical)
Barnes Cemetery
Gorge Canyon
Panther Creek
Onion Spring
A K Prairie
Waggoner Gap
Mildred Mine
Miser Mine
Quartzmill Mine
South Fork Quines Creek
Lammys Reservoir
Rieke Reservoir
Marsh Reservoir
Hubbard Pond
Lookingglass Cemetery
Jones Family Cemetery
Melrose Cemetery
Harris Reservoir
Yoder Reservoir
Powderhouse Canyon
Indian Nose
Park Lake
Melton Reservoir
Nordic Log Pond
Laurelwood Park
Gaddis Park
Riverside Park
Beulah Park
Shady Point
Stewart Park
River Front Park
Roseburg City Hall
Baker College
Baker Municipal Aqueduct
Baker Valley
Baldock Ditch
Baldock Slough
Brooklyn Elementary School
Calvary Cemetery
Baker Middle School
Central Elementary School
Churchill School (historical)
Candy Cane Park
Corral Ditch
Correll Ditch
Coyote Peak
Crooked Creek
Deal Creek
Devils Slide
Dismal Creek
Dobbin Ditch
Eastern Oregon University
Estes Ditch
Estes Slough
Gangloff Park
Gekeler Ditch
Gekeler Slough
Grande Ronde Ditch
Grande Ronde Hospital
Grande Ronde Valley
Grandview Cemetery
Greenwood Elementary School
Griffin Gulch
Haywire Canyon
Highway 203 Pond
Hillcrest Cemetery
Island City
La Grande
La Grande Country Club
Ladd Marsh
Ladd Marsh Game Management Area
Lone Pine Waterhole
May Park Ditch
McAlister Ditch
McCord Ditch
Mill Creek
Missouri Flat
Mount Hope Cemetery
Mulholland Slough
Nesley Ditch
New Home Ditch
New Pine Creek
North Baker Elementary School
Old Settlers Slough
Oregon Trail Monument
Owsley Canyon
Pierce Slough
Pioneer Park
Powder River
Riveria School (historical)
Rooster Peak
Saint Francis High School (historical)
Sam O Spring
Baker Valley Seventh - Day Adventist School
Sheep Creek
Smith Ditch
Smith Lake
South Baker Intermediate School
Spring Grove Gulch
Spring Slough
Stack Junior High School
Sutton Creek
Table Mountain
Taylor Creek
Willow Elementary School (historical)
Wright Slough
Byron Slough
Ackles Cemetery
Spence Reservoir
West Fork Ladd Creek
Byron Reservoir
Paddy Lots Springs
Orodell (historical)
KBKR-FM
KEOL-FM
KLBM-FM
KLBM-AM
KBKR-AM
Baker City Municipal Airport
La Grande/Union County Airport
Rambling Rotors Heliport
Saint Elizabeth Community Hospital Helipad
Estes (historical)
Missouri Flat (historical)
Kolb Reservoir
Union County
Smith Lake Dam
Abberdeen Post Office (historical)
Adamsville Post Office (historical)
Air Base Post Office (historical)
Air Base Post Office (historical)
Portland Airport Post Office
Albany Post Office
Alberson Post Office (historical)
Albert Post Office (historical)
Albion Post Office (historical)
Alderbrook Post Office (historical)
Alene Post Office (historical)
Aloha Post Office
Altamont Post Office (historical)
Alville Post Office (historical)
Alvord Post Office (historical)
Anderson Post Office (historical)
Anglersvale Post Office (historical)
Angora Post Office (historical)
Anthony Post Office (historical)
Argenti Post Office (historical)
Arrow Post Office (historical)
Arroyo Post Office (historical)
Ashland Post Office
Astoria Post Office
Atwood Post Office (historical)
Azalea Post Office (historical)
Bacona Post Office (historical)
Badger Post Office (historical)
Bagnell Post Office (historical)
Baker City Post Office
Bakersfield Post Office (historical)
Baldwin Post Office (historical)
Baldy Post Office (historical)
Bangor Post Office (historical)
Bar Post Office (historical)
Bar View Post Office (historical)
Barnes Post Office (historical)
Basin Post Office (historical)
Basin Post Office (historical)
Bay Post Office (historical)
Beaver Landing Post Office (historical)
Beaver Post Office (historical)
Beaverton Post Office
Belle Post Office (historical)
Bellwood Post Office (historical)
Ben Holladay Post Office (historical)
Bend Post Office
Bennett Post Office (historical)
Bentzen Post Office (historical)
Berdugo Post Office (historical)
Big Prairie Post Office (historical)
Bissell Post Office (historical)
Blackbutte Post Office (historical)
Blaine Post Office (historical)
Blanchet Post Office (historical)
Blanton Post Office (historical)
Blind Slough Post Office (historical)
Blitzen Post Office (historical)
Bloomington Post Office (historical)
Bluff Post Office (historical)
Bonita Post Office (historical)
Boon Post Office (historical)
Booth Post Office (historical)
Boswell Post Office (historical)
Bowdens Post Office (historical)
Boyer Post Office (historical)
Bradbury Post Office (historical)
Braden Post Office (historical)
Braunsport Post Office (historical)
Bridgeport Post Office (historical)
Brockville Post Office (historical)
Broughton Post Office (historical)
Brown Post Office (historical)
Buckfork Post Office (historical)
Budd Post Office (historical)
Buffalo Post Office (historical)
Burleson Post Office (historical)
Burnt Woods Post Office (historical)
Camp Clatsop Post Office (historical)
Camp Creek Post Office (historical)
Camp Ground Post Office (historical)
Campus Post Office (historical)
Cannon Beach Post Office (historical)
Canterbury Square Post Office (historical)
Cardwell Post Office (historical)
Carico Post Office (historical)
Carlisle Post Office (historical)
Carter Post Office (historical)
Cartwrights Post Office (historical)
Casey Post Office (historical)
Castle Rock Post Office (historical)
Cazadero Post Office (historical)
Cedar Camp Post Office (historical)
Celilo Post Office (historical)
Centennial Post Office (historical)
Center Bend Post Office (historical)
Center Post Office (historical)
Central City Post Office (historical)
Central Post Office (historical)
Chapman Post Office (historical)
Chehalem Post Office (historical)
Cherry Creek Post Office (historical)
Chester Post Office (historical)
Chloride Post Office (historical)
Christman Post Office (historical)
Clackemas Post Office (historical)
Clarion Post Office (historical)
Clatsop Post Office (historical)
Cliff Post Office (historical)
Cline Falls Post Office (historical)
Clover Flat Post Office (historical)
Cold Springs Post Office (historical)
Coldspring Post Office (historical)
Colia Post Office (historical)
College Crest Post Office (historical)
Collins Post Office (historical)
Columbia Post Office (historical)
Connley Post Office (historical)
Coos Bay Post Office
Cord Post Office (historical)
Corrie Post Office (historical)
Corvallis Post Office
Cottonwood Post Office (historical)
Crater Post Office (historical)
Creede Post Office (historical)
Crescent Post Office (historical)
Creston Post Office
Crook Post Office (historical)
Croston Post Office (historical)
Croy Post Office (historical)
Crutcher Post Office (historical)
Cullom Post Office (historical)
Cumtux Post Office (historical)
Cushing Post Office (historical)
Custer Post Office (historical)
Davidson Post Office (historical)
Davidson Post Office (historical)
De Moss Springs Post Office (historical)
Dechutes Post Office (historical)
Deer Park Post Office (historical)
Deering Post Office (historical)
Del Norte Post Office (historical)
Delaine Post Office (historical)
Delphia Post Office (historical)
Denio Post Office (historical)
Dent Post Office (historical)
Deschutes Bridge Post Office (historical)
Deter Post Office (historical)
Devils Lake Post Office (historical)
Diamond Post Office (historical)
Diffin Post Office (historical)
Divide Post Office (historical)
Douty Post Office (historical)
Downtown Bend Post Office
Downtown Post Office (historical)
Drylake Post Office (historical)
Duncanville Post Office (historical)
Eagan Station Post Office (historical)
Eckles Post Office (historical)
Eden Post Office (historical)
Edgewood Post Office (historical)
Egli Post Office (historical)
Egypt Post Office (historical)
Ekoms Post Office (historical)
El Dorado Post Office (historical)
Elkhorn Post Office (historical)
Elkridge Post Office (historical)
Elliott Post Office (historical)
Elliston Post Office (historical)
Elstow Post Office (historical)
Ely Post Office (historical)
Enchanted Prairie Post Office (historical)
Enterprise Post Office (historical)
Eola Post Office (historical)
Erskineville Post Office (historical)
Etna Post Office (historical)
Eugene Post Office
Eula Post Office (historical)
Eureka Post Office (historical)
Evergreen Post Office (historical)
Exposition Post Office (historical)
Fair Ground Post Office (historical)
Fairgrounds Post Office (historical)
Fairmount Post Office (historical)
Faloma Post Office (historical)
Farmington Mall Post Office (historical)
Farrens Post Office (historical)
Federal Post Office (historical)
Fern Post Office (historical)
Ferry Post Office (historical)
Fife Post Office (historical)
Finley Post Office (historical)
Fir Post Office (historical)
Firholm Post Office (historical)
Fleetwood Post Office (historical)
Flickbar Post Office (historical)
Flinn Post Office (historical)
Flournoy Post Office (historical)
Follyfarm Post Office (historical)
Forest Grove Post Office
Forest Park Post Office
Forks of Marys River Post Office (historical)
Forrest Post Office (historical)
Fort Clatsop Post Office (historical)
Freedom Post Office (historical)
French Settlement Post Office (historical)
Gage Post Office (historical)
Garrison Post Office (historical)
Gate Creek Post Office (historical)
Gate Creek Post Office (historical)
Gateway Post Office (historical)
Gazley Post Office (historical)
Glentena Post Office (historical)
Gold River Post Office (historical)
Goose Lake Post Office (historical)
Gordon Post Office (historical)
Graeme Post Office (historical)
Graham Post Office (historical)
Grand Prairie Post Office (historical)
Grants Pass Post Office
Grass Ridge Post Office (historical)
Green Basin Post Office (historical)
Gresham Post Office
Grover Post Office (historical)
Gumbo Post Office (historical)
Gypsum Post Office (historical)
Hammersley Post Office (historical)
Happy Post Office (historical)
Harriman Post Office (historical)
Harris Ferry Post Office (historical)
Harrison Post Office (historical)
Hawthorne Post Office (historical)
Hay Creek Post Office (historical)
Hayland Post Office (historical)
Haystack Post Office (historical)
Heceta Post Office (historical)
Held Post Office (historical)
Rock Creek Post Office (historical)
Henney Post Office (historical)
Herman Post Office (historical)
Hermansville Post Office (historical)
Hershal Post Office (historical)
Hiddensprings Post Office (historical)
High School Post Office (historical)
Highway Post Office (historical)
Hill Post Office (historical)
Hillsboro Post Office
Hillside Post Office (historical)
Hilton Post Office (historical)
Hoevet Post Office (historical)
Hoffman Post Office (historical)
Holladay Park Post Office
Salem Hollywood DCU Post Office
Homer Post Office (historical)
Horton Post Office (historical)
Hospital Post Office (historical)
Howell Post Office (historical)
Hudson Post Office (historical)
Hunters Post Office (historical)
Huntley Post Office (historical)
Hunts Post Office (historical)
Ibex Post Office (historical)
Idol Post Office (historical)
Ila Post Office (historical)
Illingworth Post Office (historical)
Imperial Post Office (historical)
Inlow Post Office (historical)
Iowa Slough Post Office (historical)
Isolate Post Office (historical)
Ivison Post Office (historical)
James Post Office (historical)
Jantzen Beach Post Office (historical)
Joppa Post Office (historical)
Kennedy Post Office (historical)
Kentuck Slough Post Office (historical)
Kilbride Post Office (historical)
Kilchis Post Office (historical)
Killgaver Post Office (historical)
Kindred Post Office (historical)
Kingsley Field Post Office (historical)
Kingwood Post Office (historical)
Klamath Falls Post Office
Kronenberg Post Office (historical)
La Mu Post Office (historical)
Lackemute Post Office (historical)
Lake Grove Post Office
Lake Lytle Post Office (historical)
Lake Oswego Post Office
Lake Post Office (historical)
Landing Post Office (historical)
Laraut Post Office (historical)
Larch Post Office (historical)
Larch Post Office (historical)
Lat Shaws Mill Post Office (historical)
Latourell Falls Post Office (historical)
Laurance Post Office (historical)
Lawn Arbor Post Office (historical)
Leader Post Office (historical)
Lebanon Post Office (historical)
Lee Post Office (historical)
Leeds Post Office (historical)
Legality Post Office (historical)
Lehman Hot Springs Post Office (historical)
Lemont Post Office (historical)
Lexington Post Office (historical)
Liberty Post Office (historical)
Lightner Post Office (historical)
Liverpool Post Office (historical)
Llano Post Office (historical)
Lobster Post Office (historical)
Loma Vista Post Office (historical)
Lonely Post Office (historical)
Lonesomehurst Post Office (historical)
Loraton Post Office (historical)
Lost Valley Post Office (historical)
Louis Post Office (historical)
Lower Astoria Post Office (historical)
Lower Bridge Post Office (historical)
Lowersoda Post Office (historical)
Luckyboy Post Office (historical)
Luda Post Office (historical)
Lutgens Post Office (historical)
Lynch Post Office (historical)
Mackdale Post Office (historical)
Malheur Post Office (historical)
Mango Post Office (historical)
Manila Post Office (historical)
Manse Post Office (historical)
Manseneta Post Office (historical)
Market Post Office (historical)
Matney Post Office (historical)
Matoles Post Office (historical)
Maud Post Office (historical)
May Post Office (historical)
Maywood Park Post Office (historical)
McAllister Post Office (historical)
McGlynn Post Office (historical)
McKay Dam Post Office (historical)
McMinnville Post Office
Mead Post Office (historical)
Meadows Post Office (historical)
Meadowville Post Office (historical)
Mealey Post Office (historical)
Medford Post Office
Menlo Park Post Office (historical)
Menominee Post Office (historical)
Meridian Post Office (historical)
Midway Post Office
Millers Post Office (historical)
Mink Post Office (historical)
Minnie Post Office (historical)
Mishawaka Post Office (historical)
Montezuma Post Office (historical)
Moore Post Office (historical)
Morton Post Office (historical)
Mosaba Post Office (historical)
Mount Hood Post Office (historical)
Mount Hood Parkdale Post Office
Mount Pleasant Post Office (historical)
Mount Sylvania Post Office (historical)
Mount Tabor Post Office (historical)
Mouth of Willamette Post Office (historical)
Mowry Post Office (historical)
Muddy Station Post Office (historical)
Munkers Post Office (historical)
Myrtle City Post Office (historical)
Naval Air Station Post Office (historical)
Navy 10102 Post Office (historical)
Navy 10146 Post Office (historical)
Navy 10151 Post Office (historical)
Navy 10269 Post Office (historical)
Navy 10371 Post Office (historical)
Navy 11088 Post Office (historical)
Navy 12028 Post Office (historical)
Navy 13003 Post Office (historical)
Navy 13023 Post Office (historical)
Navy 13027 Post Office (historical)
Neer Post Office (historical)
Neet Post Office (historical)
Nesmiths Post Office (historical)
Neverstil Post Office (historical)
Newbern Post Office (historical)
Nice Post Office (historical)
Noble Post Office (historical)
North Bend Post Office
North Post Office (historical)
Nye Beach Post Office (historical)
Oak Grove Post Office (historical)
Oak Post Office (historical)
Oakdale Post Office (historical)
Oakley Post Office (historical)
Oceola Post Office (historical)
Ochoco Post Office (historical)
Olden Post Office (historical)
Omro Post Office (historical)
Oneatta Post Office (historical)
Onion Peak Post Office (historical)
Ontario Post Office
Ord Post Office (historical)
Oregon Caves Post Office (historical)
Oregon City Post Office
Oretech Post Office
Oroville Post Office (historical)
Orville Post Office (historical)
Owens Post Office (historical)
Owyhee Ferry Post Office (historical)
Owyhee Post Office (historical)
Page Post Office (historical)
Palestine Post Office (historical)
Palmer Post Office (historical)
Palos Post Office (historical)
Paramount Post Office (historical)
Parkers Mills Post Office (historical)
Parkersburgh Post Office (historical)
Parkersville Post Office (historical)
Parkwood Post Office (historical)
Pass Creek Post Office (historical)
Payn Post Office (historical)
Peak Post Office (historical)
Pendleton Field Post Office (historical)
Pendleton Post Office
Pengra Post Office (historical)
Peninsular Post Office (historical)
Penola Post Office (historical)
Perdue Post Office (historical)
Perham Post Office (historical)
Peris Post Office (historical)
Peyton Post Office (historical)
Phillips Post Office (historical)
Pine Grove Post Office (historical)
Pine Post Office (historical)
Pioneer Post Office
Pioneer Post Office (historical)
Pitner Post Office (historical)
Pivot Post Office (historical)
Pix Post Office (historical)
Plano Post Office (historical)
Plum Valley Post Office (historical)
Polk Post Office (historical)
Pompeii Post Office (historical)
Pony Village Post Office (historical)
Port Clatsop Post Office (historical)
Portland Air Base Post Office (historical)
Portland Post Office
Portland Zoo Railway Post Office (historical)
Preston Post Office (historical)
Preuss Post Office (historical)
Price Post Office (historical)
Prichard Post Office (historical)
Pringle Park Plaza Post Office
Pringlefalls Post Office (historical)
Purdy Post Office (historical)
Pyrite Post Office (historical)
Quinn Post Office (historical)
Quinook Post Office (historical)
Quosation Post Office (historical)
Rachel Post Office (historical)
Rainbow Mine Post Office (historical)
Range Post Office (historical)
Rann Post Office (historical)
Redboy Post Office (historical)
Resort Post Office (historical)
Resort Post Office (historical)
Rest Post Office (historical)
Ringo Point Post Office (historical)
River Road Post Office (historical)
Riverdale Post Office (historical)
Rivers Post Office (historical)
Riverside Post Office (historical)
Robinson Post Office (historical)
Rockcreek Post Office (historical)
Rockland Post Office (historical)
Roland Post Office (historical)
Rolyat Post Office (historical)
Rome Post Office (historical)
Rosa Post Office (historical)
Rose City Post Office (historical)
Rose City Park Post Office (historical)
Rose Post Office (historical)
Roseburg Post Office
Rowes Post Office (historical)
Ruddock Post Office (historical)
Rujada Post Office (historical)
Saddlebutte Post Office (historical)
Saint Clair Post Office (historical)
Saint Helens Post Office
Saint Helens Station A Post Office (historical)
Saint Marys Post Office (historical)
Salem Post Office
Salineville Post Office (historical)
Salisbury Post Office (historical)
Salvater Post Office (historical)
San Rafael Post Office (historical)
Sandstone Post Office (historical)
Sandy Post Office (historical)
Santiam Post Office (historical)
Santyam Forks Post Office (historical)
Sauvies Island Post Office (historical)
Sauvies Post Office (historical)
Scoubes Post Office (historical)
Seaforth Post Office (historical)
Seaside House Post Office (historical)
Seaton Post Office (historical)
Section Base Post Office (historical)
Sellwood-Moreland Post Office
Sepanek Post Office (historical)
Shattuck Post Office (historical)
Shaw Post Office (historical)
Shelby Post Office (historical)
Sherrill Post Office (historical)
Shirk Post Office (historical)
Shirk Post Office (historical)
Sidney Post Office (historical)
Silver Creek Post Office (historical)
Silver Wells Post Office (historical)
Silverton Post Office
Sink Post Office (historical)
Skipanon Post Office (historical)
Slough Post Office (historical)
Sly Post Office (historical)
Smith Post Office (historical)
Smiths Post Office (historical)
Snow Post Office (historical)
Soda Springs Post Office (historical)
Soda Springs Post Office (historical)
Soda Stone Post Office (historical)
South 99E Post Office (historical)
South Inlet Post Office (historical)
South Post Office (historical)
Southgate Post Office (historical)
Southside Post Office
Springfield Post Office
Statesman Post Office (historical)
Stewart Post Office (historical)
Stokes Post Office (historical)
Stone Post Office (historical)
Straightsburg Post Office (historical)
Sugarloaf Post Office (historical)
Sunnyview Post Office (historical)
Swan Island Post Office (historical)
Sweetbrier Post Office (historical)
Swim Post Office (historical)
Taho Post Office (historical)
Tamarack Post Office (historical)
Taylor Post Office (historical)
Taylor Post Office (historical)
Taylors Ferry Post Office (historical)
Teepy Springs Post Office (historical)
Terry Post Office (historical)
Thelake Post Office (historical)
Theora Post Office (historical)
Thomas Mill Post Office (historical)
Thomas Post Office (historical)
Thompson Post Office (historical)
Thomson Post Office (historical)
Thornhollow Post Office (historical)
Threepines Post Office (historical)
Thurston Post Office (historical)
Tiara Post Office (historical)
Tidecreek Post Office (historical)
Tigardville Post Office (historical)
Time Post Office (historical)
Timon Post Office (historical)
Tiptop Post Office (historical)
Town Center Post Office (historical)
Tracy Post Office (historical)
Trailfork Post Office (historical)
Tremont Post Office (historical)
Trester Post Office (historical)
Trout Creek Post Office (historical)
Tryon Post Office (historical)
Tuality Plains Post Office (historical)
Tule Lake Post Office (historical)
Twelve Mile Post Office (historical)
Umatilla Post Office (historical)
Umpqua City Post Office (historical)
Unavilla Post Office (historical)
Undine Post Office (historical)
Uniontown Post Office (historical)
University Post Office
University Post Office (historical)
Upper Astoria Post Office (historical)
Utter City Post Office (historical)
Valfontis Post Office (historical)
Valley Post Office (historical)
Vannoy Post Office (historical)
Vernie Post Office (historical)
Vernon Post Office (historical)
Vesper Post Office (historical)
Viewpoint Post Office (historical)
Village Post Office (historical)
Villard Post Office (historical)
Vincent Post Office (historical)
Vinton Post Office (historical)
Vista Post Office
Vosburg Post Office (historical)
Wallamette Post Office (historical)
Wanaville Post Office (historical)
Wapato Post Office (historical)
Wapatoo Post Office (historical)
Wardway Post Office (historical)
Wasco Post Office (historical)
Washington Post Office (historical)
Washington Park Zoo Railway Post Office
Waverly Post Office (historical)
Weekly Post Office (historical)
Medford Carrier Annex
West Oak Post Office (historical)
West Side Post Office
Wheeler Post Office (historical)
Whelpley Post Office (historical)
Whitaker Post Office (historical)
Whitcomb Post Office (historical)
White Horse Post Office (historical)
Whitelake Post Office (historical)
Wilark Post Office (historical)
Willamette Post Office (historical)
Willamette Slough Post Office (historical)
Willoughby Post Office (historical)
Willsburgh Post Office (historical)
Winchuck Post Office (historical)
Windy Post Office (historical)
Wise Post Office (historical)
Woodburn Post Office
Woodlawn Post Office (historical)
Woodley Post Office (historical)
Woodrow Post Office (historical)
Wroe Post Office (historical)
Yainax Post Office (historical)
Yam Hill Post Office (historical)
Yeoville Post Office (historical)
Ziegler Post Office (historical)
Acme Post Office (historical)
Acton Post Office (historical)
Ada Post Office (historical)
Adair Village Post Office (historical)
Adams Post Office
Adel Post Office
Adrian Post Office
Agate Beach Post Office (historical)
Agate Post Office (historical)
Agness Post Office
Aims Post Office (historical)
Airlie Post Office (historical)
Ajax Post Office (historical)
Alamo Post Office (historical)
Albee Post Office (historical)
Albina Post Office (historical)
Alcoe Post Office (historical)
Alder Post Office (historical)
Ale Post Office (historical)
Alfalfa Post Office (historical)
Algoma Post Office (historical)
Alicel Post Office (historical)
Allegany Post Office
Alma Post Office (historical)
Almeda Post Office (historical)
Aloysius Post Office (historical)
Alpha Post Office (historical)
Alpine Post Office (historical)
Alpine Post Office (historical)
Alsea Post Office
Altamont Post Office (historical)
Althouse Post Office (historical)
Alvadore Post Office
Amity Post Office
Amos Post Office (historical)
Anchor Post Office (historical)
Anderson Post Office (historical)
Andrews Post Office (historical)
Angora Post Office (historical)
Anidem Post Office (historical)
Anlauf Post Office (historical)
Anoka Post Office (historical)
Antelope Post Office
Antler Post Office (historical)
Antone Post Office (historical)
Apiary Post Office (historical)
Applegate Post Office
Appleton Post Office (historical)
Arago Post Office (historical)
Arcadia Post Office (historical)
Arcadia Post Office (historical)
Arch Cape Post Office
Ardenwald Post Office (historical)
Arko Post Office (historical)
Arleta Post Office (historical)
Arlington Post Office
Armin Post Office (historical)
Arock Post Office
Arthur Post Office (historical)
Arthur Post Office (historical)
Asbestos Post Office (historical)
Ash Post Office (historical)
Ashwood Post Office (historical)
Athena Post Office
Auburn Post Office (historical)
Audrey Post Office (historical)
Augusta Post Office (historical)
Aumsville Post Office
Aurora Post Office
Austin Post Office (historical)
Axtell Post Office (historical)
Azalea Post Office
Baird Post Office (historical)
Bakeoven Post Office (historical)
Ballston Post Office (historical)
Balm Post Office (historical)
Bancroft Post Office (historical)
Bandon Post Office
Banks Post Office
Barber Post Office (historical)
Barbra Post Office (historical)
Barite Post Office (historical)
Barlow Post Office (historical)
Barnegat Post Office (historical)
Barnesdale Post Office (historical)
Barney Post Office (historical)
Barnhart Post Office (historical)
Barron Post Office (historical)
Bartlett Post Office (historical)
Barton Post Office (historical)
Bates Post Office
Bay City Post Office
Bayocean Post Office (historical)
Bayview Post Office (historical)
Beagle Post Office (historical)
Beatty Post Office
Beaver Marsh Post Office (historical)
Beaver Post Office
Beavercreek Post Office
Beckley Post Office (historical)
Bedfield Post Office (historical)
Beech Creek Post Office (historical)
Belknap Springs Post Office (historical)
Bellamy Post Office (historical)
Bellevue Post Office (historical)
Bellfountain Post Office (historical)
Belmont Post Office (historical)
Berkley Post Office (historical)
Berkley Post Office (historical)
Berlin Post Office (historical)
Berry Post Office (historical)
Bethany Post Office (historical)
Bethel Post Office (historical)
Beulah Post Office (historical)
Big Butte Post Office (historical)
Big Eddy Post Office (historical)
Biggs Post Office (historical)
Biglow Post Office (historical)
Binger Post Office (historical)
Birkenfeld Post Office
Bissell Post Office (historical)
Blachly Post Office
Black Butte Ranch Post Office
Black Rock Post Office (historical)
Blaine Post Office (historical)
Blalock Post Office (historical)
Blitzen Post Office (historical)
Blodgett Post Office
Blooming Post Office (historical)
Blue River Post Office
Bly Post Office
Blybach Post Office (historical)
Boardman Post Office
Bohemia Post Office (historical)
Boiling Point Post Office (historical)
Bolt Post Office (historical)
Bonanza Post Office
Bonita Post Office (historical)
Booth Post Office (historical)
Booth Post Office (historical)
Boring Post Office
Boston Mills Post Office (historical)
Bour Post Office (historical)
Bourne Post Office (historical)
Box Post Office (historical)
Boyd Post Office (historical)
Bradwood Post Office (historical)
Braymill Post Office (historical)
Breitenbush Post Office (historical)
Bridal Veil Post Office
Bridge Creek Post Office (historical)
Bridge Creek Post Office (historical)
Bridge Post Office (historical)
Bridgeport Post Office
Briedwell Post Office (historical)
Briggson Post Office (historical)
Brighton Post Office (historical)
Brightwood Post Office
Britten Post Office (historical)
Broadacres Post Office (historical)
Broadbent Post Office
Broadmead Post Office (historical)
Brockway Post Office (historical)
Brogan Post Office
Brookings Post Office
Brooklyn Post Office
Brooks Post Office
Brothers Post Office
Brower Post Office (historical)
Brownlee Post Office (historical)
Brownsboro Post Office (historical)
Brownsmead Post Office (historical)
Brownsville Post Office
Browntown Post Office (historical)
Bruce Post Office (historical)
Buchanan Post Office (historical)
Buell Post Office (historical)
Buena Vista Post Office (historical)
Bullards Post Office (historical)
Bully Post Office (historical)
Buncom Post Office (historical)
Bunker Hill Post Office (historical)
Burkemont Post Office (historical)
Burlington Post Office (historical)
Burns Post Office
Burnt Ranch Post Office (historical)
Burnt Woods Post Office (historical)
Burroughs Post Office (historical)
Butler Post Office (historical)
Butte Creek Post Office (historical)
Butte Falls Post Office
Butte Post Office (historical)
Butteville Post Office (historical)
Buxton Post Office
Cableville Post Office (historical)
Cake Post Office (historical)
Caleb Post Office (historical)
Calvert Post Office (historical)
Camas Valley Post Office
Camp Adair Post Office (historical)
Camp Lyon Post Office (historical)
Camp Polk Post Office (historical)
Camp Sherman Post Office
Camp Watson Post Office (historical)
Canary Post Office (historical)
Canby Post Office
Cannon Beach Post Office
Canyon City Post Office
Canyonville Post Office
Cape Meares Post Office (historical)
Carlton Post Office
Carnation Post Office (historical)
Carpenterville Post Office (historical)
Carson Post Office (historical)
Carus Post Office (historical)
Carver Post Office (historical)
Cascade Locks Post Office
Cascade Summit Post Office (historical)
Cascadia Post Office
Catlow Post Office (historical)
Cave Junction Post Office
Caverhill Post Office (historical)
Caviness Post Office (historical)
Cayuse Post Office (historical)
Cecil Post Office (historical)
Cedar Hills Post Office
Cedar Mill Post Office
Centerville Post Office (historical)
Central Post Office (historical)
Central Point Post Office
Chadwell Post Office (historical)
Champion Post Office (historical)
Champoeg Post Office (historical)
Chandler Post Office (historical)
Chapman Post Office (historical)
Charleston Post Office
Charlotte Post Office (historical)
Chase Post Office (historical)
Chemawa Post Office (historical)
Chemult Post Office
Cherry Grove Post Office (historical)
Cherryville Post Office (historical)
Cheshire Post Office
Chetco Post Office (historical)
Chewaucan Post Office (historical)
Chico Post Office (historical)
Chiloquin Post Office
Chitwood Post Office (historical)
Christmas Valley Post Office
Civil Bend Post Office (historical)
Clackamas Post Office
Clarkes Post Office (historical)
Clarksville Post Office (historical)
Clarnie Post Office (historical)
Clarno Post Office (historical)
Clatskanie Post Office
Clear Creek Post Office (historical)
Cleek Post Office (historical)
Clem Post Office (historical)
Cleveland Post Office (historical)
Clifford Post Office (historical)
Clifton Post Office (historical)
Climax Post Office (historical)
Clover Post Office (historical)
Cloverdale Post Office
Clymer Post Office (historical)
Coaledo Post Office (historical)
Coast Fork Post Office (historical)
Coburg Post Office
Cochran Post Office (historical)
Coles Valley Post Office (historical)
Colestin Post Office (historical)
Colson Post Office (historical)
Colton Post Office
Columbia City Post Office
Columbine Post Office (historical)
Comer Post Office (historical)
Comstock Post Office (historical)
Condon Post Office
Connor Creek Post Office (historical)
Coos City Post Office (historical)
Coos River Post Office (historical)
Cooston Post Office (historical)
Copper Post Office (historical)
Copper Post Office (historical)
Coquille Post Office
Corbett Post Office
Corbin Post Office (historical)
Cornelius Post Office
Cornucopia Post Office (historical)
Cottage Grove Post Office
Cottonwood Post Office (historical)
Cottrell Post Office (historical)
Cove Orchard Post Office (historical)
Cove Post Office
Coyote Post Office (historical)
Crabtree Post Office
Cracker Post Office (historical)
Crane Post Office
Crater Lake Post Office
Crawford Post Office (historical)
Crawfordsville Post Office
Crescent Lake Post Office
Crescent Post Office
Creston Post Office (historical)
Creswell Post Office
Criterion Post Office (historical)
Cromwell Post Office (historical)
Crooked River Ranch Post Office (historical)
Cross Hollows Post Office (historical)
Cross Keys Post Office (historical)
Crow Post Office (historical)
Crowley Post Office (historical)
Crowley Post Office (historical)
Crown Rock Post Office (historical)
Cruzatte Post Office (historical)
Crystal Post Office (historical)
Culp Creek Post Office
Culver Post Office
Currinsville Post Office (historical)
Curtin Post Office (historical)
Cushman Post Office (historical)
Dairy Post Office
Dale Post Office
Dallas Post Office
Damascus Post Office (historical)
Danner Post Office (historical)
Dant Post Office (historical)
Dardanelles Post Office (historical)
Days Creek Post Office
Dayton Post Office
Dayville Post Office
Deadwood Post Office
Dee Post Office (historical)
Deer Island Post Office
Deerhorn Post Office (historical)
Delake Post Office (historical)
Delena Post Office (historical)
Dell Post Office (historical)
Dellwood Post Office (historical)
Delmar Post Office (historical)
Dencer Post Office (historical)
Denmark Post Office (historical)
Denver Post Office (historical)
Denzer Post Office (historical)
Depoe Bay Post Office
Derby Post Office (historical)
Deschutes Post Office (historical)
Deschutes Post Office (historical)
Desert Post Office (historical)
Detroit Post Office
Devitt Post Office (historical)
Dewey Post Office (historical)
Dexter Post Office
Diamond Hill Post Office (historical)
Diamond Lake Post Office
Diamond Post Office
Dillard Post Office
Dilley Post Office (historical)
Dillon Post Office (historical)
Disston Post Office (historical)
Divide Post Office (historical)
Dixie Post Office (historical)
Dixie Post Office (historical)
Dixonville Post Office (historical)
Dodge Post Office (historical)
Dolph Post Office (historical)
Donald Post Office
Dora Post Office (historical)
Dorena Post Office
Dothan Post Office (historical)
Dotyville Post Office (historical)
Dover Post Office (historical)
Drain Post Office
Draper Post Office (historical)
Drew Post Office (historical)
Drews Valley Post Office (historical)
Drewsey Post Office
Drift Creek Post Office (historical)
Dryden Post Office (historical)
Dudley Post Office (historical)
Dufur Post Office
Duncan Post Office (historical)
Dundee Post Office
Durkee Post Office
Eagle Creek Post Office
Eagle Point Post Office
Eagleton Post Office (historical)
Earl Post Office (historical)
Early Post Office (historical)
East Portland Post Office
Eastside Post Office
Echo Post Office
Eckley Post Office (historical)
Eddyville Post Office
Eden Post Office (historical)
Edenbower Post Office (historical)
Eightmile Post Office (historical)
Elgarose Post Office (historical)
Elgin Post Office
Elk City Post Office (historical)
Elk Flat Post Office (historical)
Elk Horn Post Office (historical)
Elk Lake Post Office (historical)
Elkhead Post Office (historical)
Elkhorn Post Office (historical)
Elkton Post Office
Ella Post Office (historical)
Elmira Post Office
Elsie Post Office (historical)
Elwood Post Office (historical)
Embody Post Office (historical)
Emery Post Office (historical)
Emigrant Springs Post Office (historical)
Emma Post Office (historical)
Empire Post Office
Endersly Post Office (historical)
English Post Office (historical)
Enright Post Office (historical)
Enterprise Post Office
Errol Post Office (historical)
Erwin Post Office (historical)
Estacada Post Office
Estrup Post Office (historical)
Etelka Post Office (historical)
Etna Post Office (historical)
Euclid Post Office (historical)
Eureka Post Office (historical)
Eustis Post Office (historical)
Evans Post Office (historical)
Evarts Post Office (historical)
Fair Oaks Post Office (historical)
Fairbanks Post Office (historical)
Fairdale Post Office (historical)
Fairfield Post Office (historical)
Fairview Post Office
Fairview Post Office (historical)
Fall Creek Post Office
Falls City Post Office
Farewell Bend Post Office (historical)
Farmington Post Office (historical)
Faubion Post Office (historical)
Fern Hill Post Office (historical)
Fern Post Office (historical)
Fernvale Post Office (historical)
Fields Post Office
Finn Rock Post Office (historical)
Fir Post Office (historical)
Firwood Post Office (historical)
Firwood Post Office (historical)
Fisher Post Office (historical)
Fishhawk Post Office (historical)
Flanagan Post Office (historical)
Flavel Post Office (historical)
Fletts Post Office (historical)
Flora Post Office (historical)
Florence Post Office
Foley Post Office (historical)
Foley Springs Post Office (historical)
Foots Creek Post Office (historical)
Forest Post Office (historical)
Fort Klamath Post Office
Fort Rock Post Office
Fort Stevens Post Office (historical)
Foss Post Office (historical)
Fossil Post Office
Foster Post Office
Four Corners Post Office (historical)
Fourmile Post Office (historical)
Fox Hollow Post Office (historical)
Fox Post Office
Fox Valley Post Office (historical)
Francisville Post Office (historical)
Franklin Post Office (historical)
Freebridge Post Office (historical)
Fremont Post Office (historical)
Frenchglen Post Office
Friend Post Office (historical)
Fruita Post Office (historical)
Fruitland Post Office (historical)
Fulton Post Office (historical)
Galena Post Office (historical)
Gales Creek Post Office
Galesville Post Office (historical)
Galice Post Office (historical)
Galloway Post Office (historical)
Garden Home Post Office (historical)
Gardner Post Office
Garfield Post Office (historical)
Garibaldi Post Office
Garner Post Office (historical)
Gaston Post Office
Gates Post Office
Gateway Post Office (historical)
Gaylord Post Office (historical)
Gearhart Post Office
Geiser Post Office (historical)
Gem Post Office (historical)
Geneva Post Office (historical)
George Post Office (historical)
Gervais Post Office
Gibbon Post Office (historical)
Gilchrist Post Office
Gist Post Office (historical)
Gladstone Post Office
Glen Post Office (historical)
Glenada Post Office (historical)
Glenbrook Post Office (historical)
Glencoe Post Office (historical)
Glencullen Post Office (historical)
Glendale Post Office
Gleneden Beach Post Office
Glenn Post Office (historical)
Glenwood Post Office
Glide Post Office
Goble Post Office (historical)
Gold Beach Post Office
Gold Hill Post Office
Golden Post Office (historical)
Goldson Post Office (historical)
Gooch Post Office (historical)
Gooseberry Post Office (historical)
Gopher Post Office (historical)
Gorman Post Office (historical)
Goshen Post Office (historical)
Government Camp Post Office
Grade Post Office (historical)
Grand Rapids Post Office (historical)
Grand Ronde Post Office
Grandview Post Office (historical)
Granger Post Office (historical)
Granite Hill Post Office (historical)
Granite Post Office (historical)
Grant Post Office (historical)
Grant Post Office (historical)
Grass Valley Post Office
Gravelford Post Office (historical)
Gray Post Office (historical)
Greenback Post Office (historical)
Greenhorn Post Office (historical)
Greenleaf Post Office (historical)
Greenville Post Office (historical)
Grizzly Post Office (historical)
Grossman Post Office (historical)
Grouse Post Office (historical)
Gunter Post Office (historical)
Gurdane Post Office (historical)
Gwendolen Post Office (historical)
Hadleyville Post Office (historical)
Haines Post Office
Hale Post Office (historical)
Halfway Post Office
Halsey Post Office
Hamilton Post Office (historical)
Hamlet Post Office (historical)
Hammond Post Office
Hampton Post Office (historical)
Handy Post Office (historical)
Hanover Post Office (historical)
Harbor Post Office
Hardin Post Office (historical)
Hardman Post Office (historical)
Hare Post Office (historical)
Harlan Post Office (historical)
Harney Post Office (historical)
Harper Post Office
Harris Post Office (historical)
Harrisburg Post Office
Hat Rock Post Office (historical)
Hauser Post Office (historical)
Hawthorne Post Office (historical)
Hayward Post Office (historical)
Hebo Post Office
Helix Post Office
Helloff Post Office (historical)
Hemlock Post Office (historical)
Henryville Post Office (historical)
Heppner Post Office
Hereford Post Office
Herling Post Office (historical)
Hermann Post Office (historical)
Hermiston Post Office
Highland Post Office (historical)
Hildebrand Post Office (historical)
Hilgard Post Office (historical)
Hillsdale Post Office (historical)
Hines Post Office
Hoaglin Post Office (historical)
Hobsonville Post Office (historical)
Holbrook Post Office (historical)
Holdman Post Office (historical)
Holland Post Office (historical)
Holley Post Office (historical)
Home Post Office (historical)
Home Post Office (historical)
Homestead Post Office (historical)
Hood River Post Office
Hoover Post Office (historical)
Hopewell Post Office (historical)
Hopkins Post Office (historical)
Horton Post Office (historical)
Hoskins Post Office (historical)
Hot Lake Post Office (historical)
Hot Springs Post Office (historical)
Howard Post Office (historical)
Hubbard Post Office
Huber Post Office (historical)
Hudson Post Office (historical)
Hugo Post Office (historical)
Hullt Post Office (historical)
Humboldt Basin Post Office (historical)
Huntington Post Office
Hurlburt Post Office (historical)
Huron Post Office (historical)
Hutchinson Post Office (historical)
Idanha Post Office
Idaville Post Office (historical)
Idea Post Office (historical)
Idleyld Park Post Office
Igo Post Office (historical)
Illahe Post Office (historical)
Imbler Post Office
Imnaha Post Office
Inavale Post Office (historical)
Independence Post Office
Indian Valley Post Office (historical)
Inglis Post Office (historical)
Ione Post Office
Irma Post Office (historical)
Ironside Post Office
Irrigon Post Office
Irving Post Office (historical)
Island City Post Office (historical)
Ivan Post Office (historical)
Izee Post Office (historical)
Jacksonville Post Office
Jamestown Post Office (historical)
Jamieson Post Office
Jasper Post Office
Jefferson Post Office
Jennings Lodge Post Office (historical)
Jennyopolis Post Office (historical)
Jett Post Office (historical)
Jewell Post Office (historical)
John Day Post Office
Johnson Post Office (historical)
Jordan Post Office (historical)
Jordan Valley Post Office
Joseph Post Office
Joy Post Office (historical)
Junction City Post Office
June Post Office (historical)
Juniper Post Office (historical)
Juniper Post Office (historical)
Juntura Post Office
Kamela Post Office (historical)
Kaskela Post Office (historical)
Keasey Post Office (historical)
Keating Post Office (historical)
Keen Post Office (historical)
Keizer Post Office
Kellogg Post Office (historical)
Kelso Post Office (historical)
Keno Post Office
Kent Post Office
Kenton Post Office
Kerby Post Office
Kernville Post Office (historical)
Kerry Post Office (historical)
Kilts Post Office (historical)
Kimberly Post Office
King City Post Office
King Post Office (historical)
Kings Valley Post Office (historical)
Kingsley Post Office (historical)
Kingston Post Office (historical)
Kinton Post Office (historical)
Kinzua Post Office (historical)
Kirk Post Office (historical)
Kist Post Office (historical)
Klamath Agency Post Office (historical)
Klondike Post Office (historical)
Klumb Post Office (historical)
Knappa Post Office (historical)
Knight Post Office (historical)
Kroll Post Office (historical)
Kubli Post Office (historical)
Kyser Post Office (historical)
La Grande Post Office
La Pine Post Office
Lacomb Post Office (historical)
Lacy Post Office (historical)
Lafayette Post Office
Lake Post Office (historical)
Lake of the Woods Post Office (historical)
Lakecreek Post Office (historical)
Lakeport Post Office (historical)
Lakeside Post Office
Lakeview Post Office
Lamonta Post Office (historical)
Lampa Post Office (historical)
Lancaster Post Office (historical)
Landax Post Office (historical)
Langell Valley Post Office (historical)
Langlois Post Office
Larwood Post Office (historical)
Latham Post Office (historical)
Laurel Post Office (historical)
Lava Post Office (historical)
Lawen Post Office
Lawton Post Office (historical)
Leaburg Post Office (historical)
Leap Post Office (historical)
Lebanon Post Office
Lee's Camp Post Office (historical)
Leland Post Office (historical)
Lena Post Office (historical)
Leneve Post Office (historical)
Lenox Post Office (historical)
Lents Post Office
Leona Post Office (historical)
Lewis Post Office (historical)
Lewisville Post Office (historical)
Lexington Post Office
Libby Post Office (historical)
Liberal Post Office (historical)
Liberty Post Office (historical)
Liberty Post Office (historical)
Lightning Post Office (historical)
Lilyglen Post Office (historical)
Lime Post Office (historical)
Lincoln Beach Post Office (historical)
Lincoln City Post Office
Lincoln Post Office (historical)
Linfield College Post Office (historical)
Linneus Post Office (historical)
Linnton Post Office (historical)
Linslaw Post Office (historical)
Linville Post Office (historical)
Llewellyn Post Office (historical)
Locust Grove Post Office (historical)
Log Cabin Post Office (historical)
Logan Post Office (historical)
Logdell Post Office (historical)
Logsden Post Office
Loma Post Office (historical)
London Post Office (historical)
Long Creek Post Office
Long Tom Post Office (historical)
Lookingglass Post Office (historical)
Lorane Post Office
Lorella Post Office (historical)
Lost Prairie Post Office (historical)
Lost River Post Office (historical)
Lostine Post Office
Lovely Post Office (historical)
Lowell Post Office
Lucky Queen Post Office (historical)
Lurley Post Office (historical)
Lyman Post Office (historical)
Lyons Post Office
Mabel Post Office (historical)
Macksburg Post Office (historical)
Macleay Post Office (historical)
Madras Post Office
Malin Post Office
Manhattan Beach Post Office (historical)
Manning Post Office
Manzanita Post Office
Maple Grove Post Office (historical)
Mapleton Post Office
Maplewood Post Office (historical)
Marcola Post Office
Margaret Post Office (historical)
Marial Post Office (historical)
Marion Post Office
Marmot Post Office (historical)
Marquam Post Office (historical)
Marshland Post Office (historical)
Marx Post Office (historical)
Marylhurst Post Office
Mason Post Office (historical)
Matney Post Office (historical)
Maupin Post Office
Maxville Post Office (historical)
Maxwell Post Office (historical)
Mayger Post Office (historical)
Mayville Post Office
McCoy Post Office (historical)
McCredie Springs Post Office (historical)
McCurdy Post Office (historical)
McDermitt Post Office (historical)
McDonald Post Office (historical)
McEwen Post Office (historical)
McKay Post Office (historical)
McKee Post Office (historical)
McKenzie Bridge Post Office
McKenzie Post Office (historical)
McKinley Post Office (historical)
McNary Post Office
Meacham Post Office
Meadow Post Office (historical)
Meadow Post Office (historical)
Meadowbrook Post Office (historical)
Mecca Post Office (historical)
Meda Post Office (historical)
Medical Springs Post Office
Medley Post Office (historical)
Mehama Post Office (historical)
Melrose Post Office (historical)
Melville Post Office (historical)
Mercer Post Office (historical)
Merganser Post Office (historical)
Merlin Post Office
Merrill Post Office
Metolius Post Office (historical)
Metzger Post Office (historical)
Middleton Post Office (historical)
Midland Post Office
Midway Post Office (historical)
Mikkalo Post Office
Miles Post Office (historical)
Mill City Post Office
Miller Post Office (historical)
Miller Post Office (historical)
Millican Post Office (historical)
Millwood Post Office (historical)
Milo Post Office (historical)
Milton - Freewater Post Office
Milwaukie Post Office
Minam Post Office (historical)
Mineral Post Office (historical)
Minerva Post Office (historical)
Minto Post Office (historical)
Mirth Post Office (historical)
Mist Post Office (historical)
Mitchell Post Office
Modoc Point Post Office (historical)
Mohawk Post Office (historical)
Mohler Post Office (historical)
Molalla Post Office
Monitor Post Office (historical)
Monkland Post Office (historical)
Monmouth Post Office
Monroe Post Office
Montague Post Office (historical)
Montavilla Post Office (historical)
Monument Post Office
Moody Post Office (historical)
Mooreville Post Office (historical)
Moorhouse Post Office (historical)
Morgan Post Office (historical)
Moro Post Office
Morton Post Office (historical)
Mosier Post Office
Mosquite Post Office (historical)
Mound Post Office (historical)
Mount Angel Post Office
Mount Hood Post Office (historical)
Mount Hood Post Office (historical)
Mount Scott Post Office (historical)
Mount Vernon Post Office
Mountain House Post Office (historical)
Mountain Post Office (historical)
Mountaindale Post Office (historical)
Mowich Post Office (historical)
Mule Post Office (historical)
Mulino Post Office
Multnomah Post Office
Murphy Post Office
Myrick Post Office (historical)
Myrtle Creek Post Office
Myrtle Point Post Office
Nansene Post Office (historical)
Narrows Post Office (historical)
Nashville Post Office (historical)
Natal Post Office (historical)
Natron Post Office (historical)
Naylox Post Office (historical)
Necanicum Post Office (historical)
Needy Post Office (historical)
Nehalem Post Office
Nenamusa Post Office (historical)
Neotsu Post Office
Neskowin Post Office
Nestocton Post Office (historical)
Netarts Post Office
New Bridge Post Office (historical)
New Era Post Office (historical)
New Pine Creek Post Office
Newberg Post Office
Newellsville Post Office (historical)
Newport Post Office
Niagara Post Office (historical)
Nibley Post Office (historical)
Nichols Post Office (historical)
Nofog Post Office (historical)
Nolin Post Office (historical)
Nonpareil Post Office (historical)
Norfolk Post Office (historical)
North Junction Post Office (historical)
North Plains Post Office
North Portland Post Office (historical)
North Powder Post Office
Norton Post Office (historical)
Nortons Post Office (historical)
Norway Post Office
Noti Post Office
Nugget Post Office (historical)
Nye Post Office (historical)
Nyssa Post Office
O'Brien Post Office
O'Neil Post Office (historical)
Oak Creek Post Office (historical)
Oak Grove Post Office
Oakland Post Office
Oakridge Post Office
Oakville Post Office (historical)
Oasis Post Office (historical)
Oceanside Post Office
Odell Post Office
Odessa Post Office (historical)
Olalla Post Office (historical)
Olene Post Office (historical)
Olete Post Office (historical)
Olex Post Office (historical)
Olney Post Office (historical)
Ona Post Office (historical)
Oneonta Post Office (historical)
Opal City Post Office (historical)
Ophir Post Office
Ordnance Post Office (historical)
Orenco Post Office (historical)
Oretown Post Office (historical)
Orient Post Office (historical)
Orodell Post Office (historical)
Ortley Post Office (historical)
Othello Post Office (historical)
Otis Post Office
Otter Rock Post Office
Owyhee Post Office (historical)
Oxbow Post Office
Pacific City Post Office
Paisley Post Office
Palmer Junction Post Office (historical)
Palmer Post Office (historical)
Panther Post Office (historical)
Paradise Post Office (historical)
Paris Post Office (historical)
Park Place Post Office (historical)
Parkdale Post Office (historical)
Parker Post Office (historical)
Parkersville Post Office (historical)
Parkrose Post Office
Pattersons Mills Post Office (historical)
Paulina Post Office
Pawn Post Office (historical)
Paynesville Post Office (historical)
Peak Post Office (historical)
Pebble Post Office (historical)
Peck Post Office (historical)
Pedee Post Office (historical)
Pedro Post Office (historical)
Peel Post Office (historical)
Pengra Post Office (historical)
Peoria Post Office (historical)
Perry Post Office (historical)
Perrydale Post Office (historical)
Persist Post Office (historical)
Philomath Post Office
Phoenix Post Office
Piedmont Post Office
Pilot Rock Post Office
Pine Grove Post Office (historical)
Pine Post Office (historical)
Pine Ridge Post Office (historical)
Pinehurst Post Office (historical)
Piney Post Office (historical)
Pioneer City Post Office (historical)
Pioneer Post Office (historical)
Pistol River Post Office
Pittsburg Post Office (historical)
Placer Post Office (historical)
Plainview Post Office (historical)
Pleasant Hill Post Office
Pleasant Home Post Office (historical)
Plevna Post Office (historical)
Plush Post Office
Pocahontas Post Office (historical)
Point Terrace Post Office (historical)
Pokegama Post Office (historical)
Polk Post Office (historical)
Pondosa Post Office (historical)
Poplar Post Office (historical)
Port Orford Post Office
Porterville Post Office (historical)
Post Post Office
Powell Butte Post Office
Powell Valley Post Office (historical)
Powellhurst Post Office (historical)
Powers Post Office
Powwatka Post Office (historical)
Prairie City Post Office
Prairie Creek Post Office (historical)
Pratum Post Office (historical)
Prescott Post Office (historical)
Princeton Post Office
Prineville Post Office
Progress Post Office (historical)
Promise Post Office (historical)
Prospect Post Office
Prosper Post Office (historical)
Provolt Post Office (historical)
Pursel Post Office (historical)
Quartz Mountain Post Office (historical)
Quincy Post Office (historical)
Quinton Post Office (historical)
Ragic Post Office (historical)
Rainbow Post Office (historical)
Rainier Post Office
Raleigh Hills Post Office (historical)
Randolph Post Office (historical)
Range Post Office (historical)
Recreation Post Office (historical)
Rector Post Office (historical)
Redland Post Office (historical)
Redmond Post Office
Redne Post Office (historical)
Reed Post Office (historical)
Reedsport Post Office
Reedville Post Office (historical)
Remote Post Office
Reston Post Office (historical)
Reuben Post Office (historical)
Reuben Post Office (historical)
Rex Post Office (historical)
Rhododendron Post Office
Rice Hill Post Office (historical)
Richland Post Office
Richmond Post Office (historical)
Rickard Post Office (historical)
Rickreall Post Office
Riddle Post Office
Ridge Post Office (historical)
Ridgeway Post Office (historical)
Rieth Post Office (historical)
Riley Post Office
Ritter Post Office
Riverside Post Office
Riverton Post Office (historical)
Roberts Post Office (historical)
Roberts Post Office (historical)
Robinette Post Office (historical)
Robinsonville Post Office (historical)
Rocca Post Office (historical)
Rock Point Post Office (historical)
Rockaway Beach Post Office
Rockcreek Post Office (historical)
Rockville Post Office (historical)
Rockville Post Office (historical)
Rockwood Post Office (historical)
Rocky Point Post Office (historical)
Rognes Post Office (historical)
Rogue River Post Office
Rome Post Office (historical)
Rondowa Post Office (historical)
Roosevelt Beach Post Office (historical)
Rooster Rock Post Office (historical)
Roots Post Office (historical)
Rose Lodge Post Office
Rosedale Post Office (historical)
Rosland Post Office (historical)
Round Prairie Post Office (historical)
Row River Post Office (historical)
Rowena Post Office (historical)
Rowland Post Office (historical)
Roy Post Office (historical)
Royal Post Office (historical)
Royston Post Office (historical)
Ruby Post Office (historical)
Ruch Post Office (historical)
Ruckles Post Office (historical)
Rufus Post Office
Rural Post Office (historical)
Russellville Post Office (historical)
Rutledge Post Office (historical)
Rye Valley Post Office (historical)
Sageview Post Office (historical)
Saginaw Post Office (historical)
Saint Benedict Post Office
Saint Johns Post Office
Saint Joseph Post Office (historical)
Saint Louis Post Office (historical)
Saint Paul Post Office
Salado Post Office (historical)
Salisbury Post Office (historical)
Salmonberry Post Office (historical)
Salt Creek Post Office (historical)
Sampson Post Office (historical)
Sams Valley Post Office (historical)
Sand Ridge Post Office (historical)
Sandlake Post Office (historical)
Sandy Post Office
Sanger Post Office (historical)
Scappoose Post Office
Scholls Post Office (historical)
Scio Post Office
Scofield Post Office (historical)
Scotts Mills Post Office
Scottsburg Post Office
Seal Rock Post Office
Seaside Post Office
Seghers Post Office (historical)
Sellwood Post Office (historical)
Selma Post Office
Seneca Post Office
Service Creek Post Office (historical)
Shady Cove Post Office
Shake Post Office (historical)
Shaniko Post Office
Sheaville Post Office (historical)
Shedd Post Office
Shelburn Post Office (historical)
Shell Rock Post Office (historical)
Sherars Bridge Post Office (historical)
Sheridan Post Office
Sherwood Post Office
Shevlin Post Office (historical)
Shubel Post Office (historical)
Shutler Post Office (historical)
Sidney Post Office (historical)
Siletz Post Office
Siltcoos Post Office (historical)
Silver Lake Post Office
Silvies Post Office (historical)
Simnasho Post Office (historical)
Sinamox Post Office (historical)
Sinnott Post Office (historical)
Siskiyou Post Office (historical)
Sisters Post Office
Sitkum Post Office (historical)
Siuslaw Post Office (historical)
Sixes Post Office
Skelley Post Office (historical)
Skullspring Post Office (historical)
Slater Post Office (historical)
Smithfield Post Office (historical)
Smock Post Office (historical)
Sodaville Post Office (historical)
South Beach Post Office
South Junction Post Office (historical)
South Yamhill Post Office (historical)
Sparta Post Office (historical)
Speaker Post Office (historical)
Spencer Creek Post Office (historical)
Spencers Butte Post Office (historical)
Spicer Post Office (historical)
Spikenard Post Office (historical)
Sprague River Post Office
Spray Post Office
Spring Valley Post Office (historical)
Spring Valley Post Office (historical)
Springbrook Post Office (historical)
Springville Post Office (historical)
Springwater Post Office (historical)
Spruce Post Office (historical)
Stacey Post Office (historical)
Stafford Post Office (historical)
Stanfield Post Office
Stanley Post Office (historical)
Star Post Office (historical)
Starkey Post Office (historical)
Starrs Point Post Office (historical)
Starvout Post Office (historical)
Stauffer Post Office (historical)
Steamboat Post Office (historical)
Steinman Post Office (historical)
Stephens Post Office (historical)
Sterlingville Post Office (historical)
Stipp Post Office (historical)
Stone Post Office (historical)
Strassel Post Office (historical)
Strawberry Post Office (historical)
Sublimity Post Office
Sucker Post Office (historical)
Sulphur Springs Post Office (historical)
Summer Lake Post Office
Summerville Post Office
Summit Post Office (historical)
Sumner Post Office (historical)
Sumpter Post Office
Sunny Valley Post Office
Sunnyside Post Office (historical)
Sunriver Post Office
Sunset Post Office (historical)
Sunset Post Office (historical)
Suntex Post Office (historical)
Suplee Post Office (historical)
Susanville Post Office (historical)
Sutherlin Post Office
Suver Post Office (historical)
Svensen Post Office (historical)
Swan Post Office (historical)
Swart Post Office (historical)
Swastika Post Office (historical)
Sweet Home Post Office
Swisshome Post Office
Switzerland Post Office (historical)
Sycamore Post Office (historical)
Sylvan Post Office (historical)
Syracuse Post Office (historical)
Table Rock Post Office (historical)
Takilma Post Office (historical)
Talbot Post Office (historical)
Talent Post Office
Tallman Post Office (historical)
Tangent Post Office
Tanks Post Office (historical)
Telocaset Post Office (historical)
Templeton Post Office (historical)
Tenmile Post Office
Tenysville Post Office (historical)
Terrebonne Post Office
Thatcher Post Office (historical)
The Dalles Post Office
Thornberry Post Office (historical)
Thurston Post Office (historical)
Tidewater Post Office
Tiernan Post Office (historical)
Tigard Post Office
Tillamook Post Office
Tiller Post Office
Timber Post Office
Timberline Lodge Post Office
Tioga Post Office (historical)
Tipton Post Office (historical)
Toketee Falls Post Office (historical)
Toledo Post Office
Tollgate Post Office (historical)
Tolo Post Office (historical)
Tolovana Park Post Office
Tongue Point Naval Station Post Office (historical)
Tonquin Post Office (historical)
Top Post Office (historical)
Topsy Post Office (historical)
Trail Post Office
Trask Post Office (historical)
Trenholm Post Office (historical)
Trent Post Office (historical)
Triangle Post Office (historical)
Troutdale Post Office
Troy Post Office (historical)
Tualatin Post Office
Tucker Post Office (historical)
Tule Lake Post Office (historical)
Tumalo Post Office (historical)
Turner Post Office
Twickenham Post Office (historical)
Twin Rocks Post Office (historical)
Tygh Valley Post Office
Ukiah Post Office
Ulvstad Post Office (historical)
Umapine Post Office (historical)
Umatilla Post Office
Umpqua Post Office
Union Creek Post Office (historical)
Union Mills Post Office (historical)
Union Post Office
Union Point Post Office (historical)
Unity Post Office
University Park Post Office (historical)
Upper Ochoco Post Office (historical)
Utopia Post Office (historical)
Vale Post Office
Valley Falls Post Office (historical)
Valsetz Post Office (historical)
Van Post Office (historical)
Vanora Post Office (historical)
Vanport City Post Office (historical)
Vansycle Post Office (historical)
Varien Post Office (historical)
Venator Post Office (historical)
Veneta Post Office
Verboort Post Office (historical)
Vernon Post Office (historical)
Vernonia Post Office
Victor Post Office (historical)
Vida Post Office
Viento Post Office (historical)
Vinemaple Post Office (historical)
Vinson Post Office (historical)
Viola Post Office (historical)
Vistillas Post Office (historical)
Voltage Post Office (historical)
Waconda Post Office (historical)
Wagner Post Office (historical)
Wagontire Post Office (historical)
Waldo Post Office (historical)
Waldport Post Office
Waldron Post Office (historical)
Walker Post Office (historical)
Wallace Post Office (historical)
Wallowa Post Office
Walterville Post Office
Walton Post Office
Wamic Post Office
Wampus Post Office (historical)
Wapinitia Post Office (historical)
Wardton Post Office (historical)
Warm Springs Post Office
Warner Lake Post Office (historical)
Warren Post Office
Warrendale Post Office (historical)
Warrenton Post Office
Wasco Post Office
Wastina Post Office (historical)
Waterloo Post Office (historical)
Waterman Post Office (historical)
Watkins Post Office (historical)
Watson Post Office (historical)
Wauna Post Office (historical)
Weatherby Post Office (historical)
Wecoma Beach Post Office (historical)
Wedderburn Post Office
Welches Post Office
Wellen Post Office (historical)
Wells Post Office (historical)
Wemme Post Office (historical)
Wenaka Post Office (historical)
Wendling Post Office (historical)
Wesley Post Office (historical)
West Chehalem Post Office (historical)
West Linn Post Office
West Portland Post Office (historical)
West Salem Post Office
West Side Post Office
West Slope Post Office
Stayton Post Office
West Union Post Office (historical)
West Woodburn Post Office (historical)
Westfall Post Office
Westfir Post Office
Westimber Post Office (historical)
Westlake Post Office
Westland Post Office (historical)
Weston Post Office
Westport Post Office
Wetmore Post Office (historical)
Wheatland Post Office (historical)
Wheeler Post Office
White City Post Office
White Pine Post Office (historical)
Whiteaker Post Office (historical)
Whitehill Post Office (historical)
Whiteson Post Office (historical)
Whitney Post Office (historical)
Wilbur Post Office
Wilderville Post Office
Wildwood Post Office (historical)
Wilhoit Post Office (historical)
Wilkesboro Post Office (historical)
Willamette Forks Post Office (historical)
Willamette Post Office (historical)
Willamina Post Office
Willard Post Office (historical)
Willard Post Office (historical)
Williams Creek Post Office (historical)
Williams Post Office
Williamsburg Post Office (historical)
Willow Forks Post Office (historical)
Willow Springs Post Office (historical)
Willowcreek Post Office (historical)
Willowdale Post Office (historical)
Willows Post Office (historical)
Wilson Post Office (historical)
Wilsonville Post Office
Wimer Post Office (historical)
Winant Post Office (historical)
Winberry Post Office (historical)
Winchester Bay Post Office
Winchester Post Office
Winema Post Office (historical)
Wingville Post Office (historical)
Winlock Post Office (historical)
Winniford Post Office (historical)
Winona Post Office (historical)
Winslow Post Office (historical)
Winston Post Office
Witch Hazel Post Office (historical)
Wolf Creek Post Office
Wonder Post Office (historical)
Woods Post Office (historical)
Woodson Post Office (historical)
Woodstock Post Office (historical)
Woolley Post Office (historical)
Worden Post Office (historical)
Wren Post Office (historical)
Wrentham Post Office (historical)
Wright Post Office (historical)
Wyeth Post Office (historical)
Yach Post Office (historical)
Yachats Post Office
Yamada Post Office (historical)
Yamhill Post Office
Yamsay Post Office (historical)
Yankton Post Office (historical)
Yaquina Post Office (historical)
Yocum Post Office (historical)
Yoncalla Post Office
Yonna Post Office (historical)
Youngs Post Office (historical)
Zena Post Office (historical)
Zigzag Post Office
Zion Post Office (historical)
Zumwalt Post Office (historical)
F C Branch Crossing (historical)
V and S Crossing (historical)
Sheridan Junction (historical)
Thurston (historical)
Brandt (historical)
Sully (historical)
Jacksons Mill (historical)
Munsey (historical)
Skinner (historical)
Klamath Falls Yard
Kotan (historical)
Lumberton (historical)
Martin (historical)
Ouxy (historical)
Pelican (historical)
Warco (historical)
Armet (historical)
Botsford (historical)
Burgess (historical)
Carter (historical)
Davis-Weber Lumber Company (historical)
Fall Creek Junction
Lawler (historical)
Magness (historical)
Reserve (historical)
Signal (historical)
Tunnel (historical)
A B Crossing (historical)
Amifer (historical)
Baisen (historical)
Beaver Hill Junction (historical)
Binks (historical)
Butterfield (historical)
C C Carter (historical)
Carman (historical)
Colby (historical)
Coos White Cedar Company (historical)
Davis Slough (historical)
Delfit (historical)
Emmons (historical)
Fairview Junction (historical)
G H Chaney Logging Railroad Crossing (historical)
Haydon (historical)
Helon (historical)
Inlet (historical)
Mill Spur (historical)
Mineola (historical)
Neal (historical)
Regal (historical)
Stave Mill (historical)
Sunshine (historical)
Yoakum (historical)
York (historical)
H P Dutton Lumber Company (historical)
Ivy (historical)
Minard (historical)
Stout Lumber Company (historical)
W D Hull Mill (historical)
A G Spence (historical)
B and B Spur (historical)
Blair (historical)
Blencoe (historical)
Capps (historical)
Cardiff (historical)
Cosmos (historical)
Enfield (historical)
H L Bergman (historical)
Hume (historical)
Ivison (historical)
Mayard (historical)
Orth (historical)
Rock Quarry (historical)
Rollo (historical)
Seneca (historical)
W D Hull Mill (historical)
Wye (historical)
Goodin (historical)
Lake Grove (historical)
Links (historical)
Rock Quarry (historical)
Rock Spur (historical)
Cemetery (historical)
Ewahwe (historical)
Jefferson Street Depot (historical)
Jones (historical)
Mulbox (historical)
Rivera (historical)
Southern Portland (historical)
Thorsen (historical)
Wrenn (historical)
Zimmerman (historical)
Ford (historical)
Frank (historical)
Galbreath (historical)
Glad (historical)
Gore (historical)
Rock Creek (historical)
Spauldings Spur (historical)
Stewart (historical)
Benbow (historical)
Meridian (historical)
Polk (historical)
Anderson (historical)
Chestnut (historical)
Balm (historical)
Gilkey (historical)
Scio Junction (historical)
Washburn (historical)
Broughton and Wiggins (historical)
Fir (historical)
Johnsons Mill (historical)
Scandia (historical)
Tinclestead (historical)
Brophy (historical)
Buman Quarry (historical)
Camp 2 (historical)
Derry Orchard (historical)
Dutch Creek (historical)
Guthrie (historical)
Hosford (historical)
Kingwood Park (historical)
Knowles (historical)
Lees Farm (historical)
Partridge (historical)
Wye (historical)
Cranor (historical)
Barbur (historical)
Flander (historical)
Haskell (historical)
Hawley Pulp and Paper (historical)
Laidlaw (historical)
Powder Switch (historical)
Rock Island (historical)
W V S Crossing (historical)
Wiggins (historical)
Willsburg Junction
Eugene Yard
American
Folk (historical)
Hallawell
River Spur (historical)
Bunting (historical)
Crandall (historical)
Fair Grounds (historical)
Hofer (historical)
Labish
Poplar (historical)
Renard
State School (historical)
Tile Works (historical)
East Morrison Street Station (historical)
Ladd (historical)
Reed (historical)
Virgil (historical)
Keech (historical)
Bally (historical)
Baxter (historical)
Drury (historical)
Albany Lumber Company (historical)
Bryant (historical)
Coxs Crossing (historical)
Forbes (historical)
Kiphart (historical)
Knox Butte (historical)
Maxwell (historical)
Munkers (historical)
Payne (historical)
Thomas (historical)
Trollinger (historical)
Weatbery (historical)
Wentworth (historical)
Williams (historical)
Birchwood (historical)
Cascade Operating Company (historical)
Cumley (historical)
Elk River (historical)
Gooch Lumber Company (historical)
Gravel Spur (historical)
Halls (historical)
Hammond Lumber Company Number 1 (historical)
Hammond Lumber Company Number 2 (historical)
Homer (historical)
Lakewood (historical)
Larson (historical)
Livesay (historical)
R G Balderee Logging Company (historical)
Schroeder (historical)
Kraft (historical)
Patrol (historical)
Platt (historical)
Rames (historical)
Scott (historical)
W V S Crossing (historical)
Browns Crossing (historical)
S C York Lumber Company Spur (historical)
Shell Oil Company Spur (historical)
Argil (historical)
Daugherty Piling Company Spur (historical)
Gretna (historical)
Isabell (historical)
Lystul (historical)
Palmer (historical)
Schuman Lumber Company Spur (historical)
Siuslaw (historical)
Stearns (historical)
Totten (historical)
Youngs (historical)
Buena (historical)
Cemetery (historical)
Colvig (historical)
Crater Lake Junction (historical)
Frederick (historical)
Orcal (historical)
Penniger (historical)
Rosenberg Brothers Spur (historical)
Van Der Hellen Gravel Pit (historical)
Viaduct (historical)
Zacher (historical)
Booth (historical)
Heffling (historical)
Josephine (historical)
Sanders (historical)
Savage Rapids Crossing (historical)
Tunnel 8
Tunnel 9
Mathews (historical)
Ironhill (historical)
Reynolds (historical)
Adair (historical)
Akron (historical)
Badger (historical)
Big Baldwin (historical)
Creekside (historical)
East Portland Lumber Company (historical)
Edwards (historical)
Elmore Park (historical)
Fishers (historical)
Foley (historical)
Haak Logging Company (historical)
Haddon (historical)
Hall Street (historical)
Hammond Tillamook Lumber Company (historical)
Hillburn (historical)
Jetty (historical)
Kelches River Ry Crossing (historical)
Killen (historical)
Lake Lytle (historical)
McAboy (historical)
Miami (historical)
Oceanlake (historical)
Paquet (historical)
Saltair (historical)
Seaview (historical)
South Fork Timber Company (historical)
Stonehill (historical)
Water Tank (historical)
Weist (historical)
Wheeler Lumber Company (historical)
B N Junction
Bagley (historical)
Blue Lake Logging Company (historical)
Castor Creek (historical)
Clayhill (historical)
Eccles Mill (historical)
Fashion (historical)
Fernwood (historical)
Hulbert (historical)
J Cole Logging Company (historical)
L H Timber Company (historical)
Lowick (historical)
Standard Box and Lumber Company (historical)
Thornburg (historical)
Treen (historical)
Walcott (historical)
Whittseley and Wisk (historical)
Wirfs (historical)
Butler (historical)
Cabbage Patch
Cain (historical)
Dunlap (historical)
Garrow (historical)
Larson (historical)
Altree (historical)
Bevens Quarry (historical)
Bittner Plug Lumber Company (historical)
Cobb (historical)
Little Elk (historical)
Miami Quarry Company (historical)
Morrison (historical)
Pioneer Lumber Company (historical)
Redfern (historical)
Sidings Number One (historical)
Storrs (historical)
Burnett (historical)
Buttes (historical)
Reckards (historical)
Winfield (historical)
Adkins (historical)
Ferguson (historical)
Malabon (historical)
Transfer (historical)
Bancroft (historical)
Dosch (historical)
Shattuck (historical)
South Portland (historical)
Woodrow (historical)
Calvert (historical)
Clay Pit (historical)
Cottle (historical)
Ledford (historical)
O'Brien Place (historical)
WVRR Junction (historical)
Tillamook Junction (historical)
Adams (historical)
Archer (historical)
Arrow (historical)
Catching (historical)
Dunzer (historical)
Eddy (historical)
Hays (historical)
Hefter (historical)
Jobe (historical)
Kilgore (historical)
Matson (historical)
Murray (historical)
Olsen (historical)
Range (historical)
Retlaw (historical)
Richfield Oil Company (historical)
Saint Marys (historical)
Teffer (historical)
Ware (historical)
Baxter (historical)
Seitters (historical)
Sight (historical)
Harriman Lodge (historical)
Ritter (historical)
Fonda (historical)
McCready (historical)
School (historical)
Sims (historical)
Spring Lake (historical)
Stanwood (historical)
Sycan (historical)
Braley Street (historical)
C and E Crossing (historical)
O E Crossing (historical)
O E Crossing
O E Ry Crossing
P R L and P Crossing (historical)
S P and S Crossing (historical)
Dolph (historical)
North Albany (historical)
Albany C and E Depot (historical)
Akin (historical)
Alkali Flats
Alkali Gulch
Austa (historical)
Avery (historical)
Barlow
Barview
Bear Creek (historical)
Beburg
Tiernan
Big Stick Creek
Black Canyon
Bonita
Boswell Mineral Springs
Briedwell (historical)
Brighton
Broadmead
Brooklyn
Bryant
Byers (historical)
Calimus
Chemult
Cheshire
Chinchalo
Cipole (historical)
Clackamas
Comstock
Coos Bay
Cordes
Corvallis Junction
Cottage Grove
Crowley
Dawson
Dayton
Delmar
Dennis
Desert Creek
Devitt
Diamond Lake
Dilley
Dimmick (historical)
Drain
Dry Gulch
Dundee
East Milwaukie
Estabrook
Fall Creek Station
Franklin
Gaylord Siding
Gellerman Canal
Gerlinger
Glencullen
Glendale
Globe
Green
Hampton Buttes
Hemlock
Hendricks
Huber
Isadore (historical)
Jasper
Johnson (historical)
Junction City
Lake Oswego
Lateral 197
Leland
Leona
Lizard Creek
Mahan
Main Canal
Maywood
Mazama
McCormac
McCoy
Merlin
Merrill Siding
Milwaukie
Modoc Point
Moody (historical)
Mount Angel
Newberg
Niagara
North Santiam
Oakridge
Overland
Owyhee Canal
Page
Park Place
Parker
Penn
Plainview
Polk Station
Pratum
Pringle (historical)
Redbell
Rex
Riddle
Riverwood
Robinson
Rockaway Beach
Rogue River
Ruckles (historical)
Scofield
Seghers
Seven Oaks
Shelburn
Siltcoos
South Fork Crooked River
Springbrook
Suver
Tallman (historical)
Walker
Warm Springs Pump Canal
Watseco (historical)
Wellsdale
Westimber (historical)
Whiteson
Wigrich Spur (historical)
Wilbur
Willow Creek
Wilson Creek
Winona (historical)
Wolf Creek
Wren
Yamhill
Yamsay
Paunina (historical)
Bowers (historical)
Luper (historical)
Fairman Coulee
Oaklawn (historical)
Alford
Nesmith (historical)
Cochrane (historical)
Howe (historical)
Crawford (historical)
Stanwood (historical)
Crocus (historical)
Hare (historical)
Buman
Switzerland (historical)
Baron (historical)
Russell (historical)
Starrs Point (historical)
Cebu (historical)
Cram (historical)
Spores (historical)
Aeroacres Airport
Potter (historical)
Hoover (historical)
Berry (historical)
Willow Creek Valley
Association Reservoir
Haymaker Gulch
Home (historical)
Willowcreek Elementary School
High Desert
Ray Gold
Calahan (historical)
Nichols (historical)
Lynbrook (historical)
Whitmore (historical)
Dickey Lake
South Dickey Peak
Terrace Spring
Algoma Siding
Granite (historical)
Little Fan Creek Campground
Port of Cascade Locks Marina
Poujade Ditch
Bull of the Woods Wilderness
Homes Gallup Bridge
Willamette Mission State Park
Sherwood Middle School
Port Barnum (historical)
South Harbor (historical)
Huckleberry Creek
Perrydale School
Saint Louis Cemetery
Oregon School for the Blind
Viewpoint Waterhole
Firestone Basin
Little Mud Lake
Frederick Butte Well
Boles Flat
Grouse Lake
Porcupine Lake
Cruiser Well
Soldiers Cap
Squaw Lake
Baldwin Waterhole
Battle Point
Old Lakebed Waterhole
Juniper Canyon
Township Reservoir
Fitchett Place
Kinnaman Elementary School
Rood Bridge
Metzger County Park
Garden Home Park
Redtail Golf Course
Camille Park
Greenway Park
Fanno Farmhouse Park
Hyland Forest Park
Oregon Episcopal School
Summerfield Golf Course
Cook Park
King City Golf Course
Roamers Rest Park (historical)
Avalon Park (historical)
Elsner Park (historical)
Kaiser Sunnyside Medical Center
Tumalo Elementary School
Mint Lake
Lyons View Park
Carver Boat Ramp
High Rocks City Park
Stocker City Park
Max Patterson Memorial City Park
Cross Memorial City Park
Gilbert Primary Park
Meldrum Bar City Park
Cub Airport (historical)
Happy Valley City Park
Water Tower Park
Tideman Johnson City Park
Errol Heights City Park
Glenwood City Park
Kern City Park
Depot City Park
North Gresham Park
Ruby Junction Maintenance Facility-Portland Light Rail System
Red Sunset Park
Jacobs Square
Barclay Park
Sportcraft Landing
McLoughlin Promenade Park
Butler Creek Park
Till Taylor Park
Roy Raley Park
Umatilla County Juvenile Center
May Park
Rice-Blakey Park
Prairie City School
Nyssa-Arcadia Drain
North Park
River Park
Ward Drain
South Park
Amazon Ball Fields
Amazon Pool
Eugene Civic Stadium
Treasure Valley Ball Park
Harry Holt Memorial Park
Mount Pisgah Arboretum
Clearwater Park and Landing
Bob Artz Memorial Park
William S Fort Memorial Park
Tyson Park
Jack B Lively Memorial Park
Thurston Park
Rodakowski Landing
Pride Park
Dorris Ranch Living History Farm
Moon Mountain
Hamlin Sports Complex
Greenway Bike Bridge
Knickerbocker Bike Bridge
Owosso Bike Bridge
East Bank City Park
Blanton Ridge City Park
Bloomberg City Park
Bond Lane City Park
Campbell Senior Center
Charnel Mulligan City Park
Condon Hall - University of Oregon
Crescent City Park
Crest Heights City Park
Day Island
Delta Ponds City Park
Eugene City Hall
Eugene Mall
Garfield City Park
Gilham City Park
Glen Oak City Park
Kelly Butte Park and Overlook
Lafferty City Park
Lane County Courthouse
Lane County Fairgrounds
Lane County Juvenile Court Detention Center
Marche Chase City Park
Wayne Morse Ranch City Park
Skinner Butte City Park
Sorrel Way City Park
South Ridge City Park
Springfield City Hall
Tandy Turn City Park
Valley River Center
West Bank City Park
West University City Park
Willis City Park
Mangan City Park
Irwin City Park
State Street City Park
Petersen City Park
Empire Park
Gilbert City Park
Willow Corner City Park
Balboa Park
Morrow County Fairgrounds
Heppner Junior - Senior High School
Heppner Elementary School
Willow Creek Reservoir
Willow Creek Dam
Rock Creek Cemetery
Deep Lake
Log Pond Lake
Lily Pond
Lewis and Clark Elementary School
Saint Helens Middle School
John Gumm Elementary School (historical)
Civic Pride Park
Heinie Heumann Park
Domeyer Lake
Millionaire Lake
Widgeon Lake
Knighton Square
Sand Island Marine Park
Lyons Beach
McCormick Park
Boise Cascade Park (historical)
Riverfront Park
Little League Park
Columbia County Fair and Rodeo Complex
Cathlacom Point
Gilmore Lake Landing
Lake Farm Landing
Stumps Landing
Oak Island Landing
Frakes Landing
Dry Lake
Sand Island (historical)
Griffith Island (historical)
Little Sturgeon Lake
Belle Vue Point Park
Howell Territorial Park
The Wash
Mud Lake
Holman Point
Johnson Lake
Kelley Point City Park
Multnomah Channel County Park
Coe Park
Mann Park
Wilson Park
Providence Hood River Memorial Hospital
Port of Hood River Marina Park
Morrison Park
Ruthton Cove
De Moss County Park
Serendipity Center
Floyd Light Middle School
Donald E Long School
Harrison City Park
West Powellhurst City Park
Cherry City Park
Mill City Park
North Powellhurst City Park
Midland City Park
Ventura City Park
Berrydale City Park
Parklane City Park
Lincoln City Park
Russell Academy
Glenfair City Park
Merrifield City Park
Rocky Butte Natural Area
Strathmore Park
Beech Park
Rocky Butte State Park
Columbia Masonic Cemetery
Sacajawea City Park
Whittaker Middle School (historical)
Pixie Park
Quintus Park
Brown Park
Riverside School (historical)
Umpqua National Forest Headquarters
Fir Grove Section of Stewart Park
Templin Beach Park
Deer Creek Park
Eagles Park
Parrott Creek Park
South Knoll Park (historical)
Eastwood Elementary School
Eastwood Park
Snelling (historical)
Lemrock (historical)
E and S Crossing (historical)
E and S Crossing (historical)
Donna (historical)
Bertha (historical)
P E and E Crossing (historical)
Raleigh (historical)
P E and E Crossing (historical)
Briggs Valley
Prineville Reservoir State Park
Two Color Recreation Site
Beech Creek Forest Camp
White Rock Recreation Site
Harvey Point
Lefty Creek
Little Smokey
Williams Ridge
Wet Gulch
Symbol Ridge
Coldwater Cove Recreation Site
Clear Lake Recreation Site
Clear Lake Resort
Hemlock Lake Campground (historical)
Mallory Spring
Cultus Corral Horse Camp
Osprey Point
Crane Prairie Resort
Lanham Bike Recreation Site (historical)
Yachats Purchase Unit
Cold Spring Cow Camp
Kelsay Valley Horse Camp
Lake Lucile Campground (historical)
Sunriver
Lava Island Shelter
Besson Camp Recreation Site
Rhododendron Island Recreation Site
Gilbertson Ranch
Springer Ranch
Quinn Meadows Horse Camp
Little Fawn Group Camp
Lava Lake Recreation Site
Lava Lake Resort
Little Lava Lake Recreation Site
Lava Lands Visitor Center
High Desert Museum
Blacks Ranch
Swampy Lakes Sno-Park
Swampy Lakes Trailhead (historical)
Wanoga Sno-Park
Edison Butte Sno-Park
Ten Mile Sno-Park
Paulina Lake Lodge
North Cove Campground (historical)
Chief Paulina Horse Camp
Newberry Group Camp
Ogden Group Camp
Six Mile Sno-Park
Taylor Burn
Lemolo Two Forebay Recreation Site
Bog Camp Cabin
Frog Lake Recreation Site
Clear Lake Recreation Site
Bagby Hot Springs Recreation Site
Hampton Recreation Site
Johnny Creek Nature Trail
Hemlock Meadows Recreation Site
China Flat Campground
New Mine
Canyon City Municipal Watershed
Canyon Creek Research Natural Area
Williams Ranch
J Bar L Ranch
Dixie Ski Bowl Recreation Site
Big Meadows Horse Camp
Hagan Block Research Natural Area
Hoover Group Camp
Mongold Recreation Site
Coffin Mountain Lookout
Middle Santiam Wilderness
Blair Lake Recreation Site
H J Andrews Experimental Forest
Falls Recreation Site
McCornick Campground
Wallowa-Whitman National Forest Headquarters
Tenderfoot Pass
Lamb Field
Red Buttes Wilderness
East Mule Recreation Site
West Mule Recreation Site
Gleason Bar Recreation Site
Blossom Bar Recreation Site
East Creek Recreation Site
Marial Lodge
Tale Creek Recreation Site
Hewitt Creek Recreation Site
Burnt Woods State Forest Service Station (historical)
Noble Fir Management Buffer Zone
Battle Bar Recreation Area
Long Gulch Recreation Area
Dulog Creek Recreation Area
Bear Camp Viewpoint Recreation Site
Lake Marie Campground
Fourmile Light
Threemile Light
Oregon Dunes National Recreation Area Visitors Center
Dutchman Peak Lookout
Kenney Meadows Picnic area
French Gulch Recreation Site
Stringtown Recreation Site
Squaw Lakes Recreation Site
Goose Pasture Recreation Site
Bible Ranch
Oakdale School (historical)
Wilson Ranch
Round Grove Weather Station
East Carter Campground (historical)
Rhea Spring
Pearson Recreation Site
Kamela Guard Station (historical)
Nine Top Camp
Circle Bar Ranch
Jubilee Lake Recreation Site
Mottet Recreation Site
Dairy Point Recreation Site
Counts Ranch
Fremont-Winema National Forest Headquarters
Vernon Ranch
Anderson Butte Lookout
Swayne Viewpoint
Cinnabar Lookout
Hammersly Ranch
Coquille River Falls Natural Area
Flora Dell Recreation Site
North Fork John Day Ranger Station
Tower Mountain Lookout Tower
Tollgate Work Camp
Tollgate Guard Station
Swamp Creek Corral (historical)
Riley Camp
Mount Emily Lookout Tower
Beaver Creek Seed Orchard
Flynn Creek Research Area
Salmon River State Forest Service Station
Drift Creek Camp
Marys Peak Botanical Special Interest Area
Enterprise Compound Forest Service Station
Wallowa Valley Ranger Station
Robinson Picnic Area
Dee Flat Seed Orchard
Forshey Corral
Lost Lake Resort
Hesperin Camp
Boundary Log Scaling Station
Big Canyon Fish Weir
Oliver Homestead
Imnaha Fish Weir
Pallette Ranch
Mahogany Cow Camp
Mahogany Canal
Timothy Spring Campground
Ashland Ranger Station (historical)
Butte Falls State Forest Station
Lon Krise Cabin
Bridge Creek Wildlife Area
Skyline Recreation Site
Fryes Mine
Jack Lake Recreation Site
Ray Benson Sno-Park
Big Lake Recreation Site
Lower Three Creek Sno-Park
Shitike Butte Lookout Station (historical)
Tetherow Recreation Site
Flagtail Mountain Fire Lookout
Koehler Ranch
Fall Mountain Fire Lookout
Starr Bowl Winter Sports Area
Malheur River Trailhead
Oliver Rock
Holliday Ranch
H Ricco Ranch
H Coombs Ranch
Johnson Ranch
Clark Ranch
Kuhl Ranch
Emigrant Creek Ranger Station
Table Rock Fire Lookout Tower
Sand Flats
Fourth Creek Camp
Anthony Lakes Shoreline Recreation Site
Anthony Lakes Forest Service Station
Mud Lake Recreation Site
Grande Ronde Lake Recreation Site
Billy Fields Recreation Site
Cedar Grove Botanical Area
Oregon Mine Camp
Canyon Meadows
Wickiup Recreation Site
Dixie Butte Fire Lookout Tower
Yellowjacket Recreation Site
Calamity Butte Lookout Tower
Time and a Half Campground (historical)
Southwest Shore Recreation Site
Mowich Recreation Site
Killamacue Trailhead
Dutch Flat Creek Trailhead
Pilcher Creek Recreation Area
Tamarack Recreation Site
Table Rock Trailhead
Amelia Trailhead
South Fork Rock Creek
Eldorado Recreation Site
PUI Airstrip (historical)
Mouse Spring
Strober Ranch
Fly Ridge
Elkhorn Wildlife Area
Powell Ranch
Metolius Research Natural Area
Indian Ford Recreation Site
Head of the Metolius
Black Butte Lookout Station
Suttle Lake Resort
Sahalie Falls Recreation Site
Underwater Forest
Koosah Falls Recreation Site
Cliff Spring
Chemult Ranger Station
Kalmiopsis Wilderness
Madras Southwest Base
Madras Water Tank
Pine Ridge Corral
Brewer Airstrip (historical)
Metolius Water Tank
Scales Corral
McCoin Orchard
Vinegar Hill-Indian Rock Scenic Area
Mud Spring
Granny View Forest Service Station (historical)
Rogue Gorge Recreation Site
Coyote Spring
Lamont Springs
Hells Canyon Creek Forest Service Station
Eagle Cap Wilderness
Detroit Ranger Station
Seneca Cow Camp
Snowshoe Trailhead
Skyline Trailhead
H Officer Ranch
Cottonwood Camp
Prairie City Forest Service Depot
Oliver Ranch
High Lake Rim Trailhead
Roads End Trailhead
Three Creek Meadow Recreation Site
Pine Creek Trailhead
Buckhorn Meadow Trailhead
Hart Ranch
Frazier Point Fire Lookout
Tenas Peak Lookout Station
Underhill Recreation Site
Munjar Place (historical)
Moon Creek School (historical)
Lemons Ranch
West Myrtle Butte Fire Lookout
Sugarloaf Mountain Fire Lookout
King Mountain Lookout
Long Creek Recreation Site
Mammoth Spring Recreation Site
North Butte
Round Lake Recreation Site
Passage Ranch
Dicks Ranch
Mill Lake
Campbell Mill
Schmidt Ranch
O'Leary Ranch
Natural Bridge Viewpoint
Union Rogue Church Camp
Mammoth Pines
Wanoga Butte Lookout Tower
Walker Mountain Lookout station
Goodlow Mountain Research Natural Area
Pankey Ranch
Indian Lake Recreational Area
Woodland Sno-Park
Columbia Gorge District Ranger Office (historical)
Rock Creek Guard Station
Mark O Hatfield Wilderness
Zigzag Ranger Station
Prospect Powerhouse
Melakwa Boy Scout Camp
Stauch Ranch
North Entrance Crater Lake National Park
Jones Ranch
Hopper Ranch
Woodward Ranch
Gage Ranch
Bridge Creek Wilderness
Kuhn Ranch
Gill Ranch
Breese Ranch
Oregon State Forestry District Headquarters
Prineville and Crooked River National Grassland Headquarters (historical)
Howard Ranch
Hewed Log Hollow
Buchanan Springs Safety Rest Area
Cottonwood Recreation Site (historical)
Shoesole Spring
Rimrock Springs Wildlife Management Area
Marysville School (historical)
Geneva Overlook
Black Mountain Lookout (historical)
Mossy Rock Camp
Lower Skull Hollow Spring
Baker City Sanitary Landfill
East Fork Canyon Creek Trailhead
Joaquin Miller Trailhead
Canyon Mountain Trailhead
Hyatt Lake Campground
East Wolf Lookout
West Wolf Lookout
Twin Springs Campground
Rocky Canyon
Coykendall Cabin
Lofton Reservoir Recreation Site
Butcher Flat (historical)
Walton Lake Campground
Mayflower Mining Settlement (historical)
Campbell Lake Recreation Site
City of Medford Watershed
Swamp Creek Reservoir
Cow Creek Gorge
Albertson Ranch
Dovre Peak Wayside
Dracatos Draw
Moore Park Marina 1
Barnhouse Recreation Site
Klamath County Dump
Aspen Butte Cinder Pit
Howard Bay Park
Skimmerhorn Recreation Site
Fish Lake Recreation Site
Beaver Swamp Recreation Site
Fourmile Canal
South Entrance Crater Lake National Park
Lavenik Cinder Pit
Mud Creek Recreation Site
Camp Namanu Post Office (historical)
Lonerock Post Office (historical)
Rogers Lake
Goat Island
Home
Arlington
Athena
Baker City
Biggs
Blue Mountain
Bodie (historical)
Cecil
Champ
Oxbow
Corbett Station
Dodson
Erskine
Farley (historical)
Freels
Hay Canyon
Heppner Junction
Hermiston
Hope (historical)
Irrigon
Klondike
Latourell
Lime
Lone Tree
McBee (historical)
Milton-Freewater
Morgan
Palmer Junction
Quinton (historical)
Ross
Rufus
Sago
The Dalles
Union Junction
Grant (historical)
Dillon (historical)
Blalock
Seufert (historical)
Hook (historical)
Meno
Ainsworth (historical)
Castle (historical)
Caton (historical)
Coyote (historical)
Grebe (historical)
Kelsey (historical)
Mays (historical)
Mikecha (historical)
Nish (historical)
Pyle (historical)
Sand (historical)
Sun (historical)
Albritton (historical)
Allens Spur (historical)
Bailey (historical)
Bates (historical)
Baum (historical)
Birch Siding (historical)
Blakes (historical)
Bluffs (historical)
Booth Lane (historical)
Boulder (historical)
Bruun (historical)
C L Lumber Company (historical)
Claude (historical)
Cold Springs (historical)
Cove Creek (historical)
Crusher (historical)
Day (historical)
De Moss (historical)
Des Chutes (historical)
Eagle Creek (historical)
Eagle Island (historical)
Eastland (historical)
Eri (historical)
Finley (historical)
Fort (historical)
Fosters (historical)
Gilmore (historical)
Gravel Pit Spur (historical)
Gwinn (historical)
Gwynne (historical)
Gypsum (historical)
Hack (historical)
Harriet (historical)
Harris (historical)
Harris (historical)
Hensley (historical)
John Days (historical)
Johns (historical)
Judson (historical)
Juniper (historical)
Ketchum (historical)
Laka (historical)
Langs (historical)
Lostine Station
Macfer (historical)
Magoffin (historical)
Marble (historical)
Maupin Station (historical)
Mayberg (historical)
McLennon (historical)
Mess House (historical)
Millroad (historical)
Mocks (historical)
Morsil (historical)
Musser (historical)
Nordeen (historical)
Oak Springs (historical)
Park (historical)
Pendleton Junction (historical)
Peters (historical)
Pheney (historical)
Pierce Spur (historical)
Pilot Rock Junction (historical)
Prevost (historical)
Quarry (historical)
Ramsey (historical)
Realore (historical)
Reardon Siding (historical)
Retrah (historical)
Reynolds (historical)
Riverview (historical)
Rodeo (historical)
Romeo (historical)
Sandy
Scotts Spur (historical)
Silica (historical)
Sink (historical)
Smythe (historical)
Stone (historical)
Summit (historical)
Sumpkin (historical)
Sutton (historical)
Taylor (historical)
Titus (historical)
Toma (historical)
Truman (historical)
Tumwater (historical)
Tunnel (historical)
Two Springs (historical)
Umatilla Junction (historical)
W. W. V. Ry. Crossing
Wade (historical)
Ward (historical)
Wilbur (historical)
Winslow (historical)
Woodlawn (historical)
Hackett Creek
Alder Creek
Badger Creek
Boulder Creek
Brightwood
Cascade Range
Cedar Creek
Cheeney Creek
Eagle Creek
Eagle Creek Cutoff
Eagle Creek Lookout (historical)
Huckleberry Mountain
North Fork Eagle Creek
Old Baldy
Old Baldy Trail
Plaza Trail
Salem
Salmon (historical)
Salmon River
Sandy River
South Fork Eagle Creek
Trout Creek
Whisky Creek
Wildcat Creek
Wildcat Mountain
Githens Mountain
McIntyre Ridge
Lake Creek
Salmon Post Office (historical)
Warehouse Beach Recreation Center
Sand Station Recreation Area
Belt Park
Victory Square Park
Hodge Park
McKenzie Park
Hermiston Christian Center and School
Newport Park
Hermiston Junior Academy
Hermiston High School
Good Shepherd Medical Center
Saddle Dam
Clara Brownell Middle School
Irrigon Marina Park
Umatilla High School
Pioneer Memorial Cemetery
McNary Beach Recreation Area
Umatilla Marina Park
Stanfield Secondary School
Stanfield Junior High School (historical)
Willbridge Siding (historical)
Portland Tug and Barge Spur (historical)
Claremont (historical)
Orwood Spur (historical)
Sunset Pacific Oil Company Spurs (historical)
General Petroleum Spurs (historical)
Richfield Oil Company Spur (historical)
Gunderson Spur (historical)
Signal Oil Spur (historical)
West Oregon Lumber Company Spur (historical)
Bans Spur (historical)
Harbor Track (historical)
Hubluco (historical)
Brix (historical)
Multnomah Plywood
Cormick (historical)
Texas Oil Company Spur (historical)
Assembly (historical)
Western Spar Company Spur (historical)
Crown Zellerbach Number 4 (historical)
"CZ Tracks 1, 2, and 3"
Murphy (historical)
Nehalem Junction (historical)
Shell Oil Company Spur (historical)
Oasis (historical)
Jacobson Reid Lumber Company (historical)
Reeds (historical)
Plues (historical)
Avon
Van Vleet Lumber Company Spur (historical)
Goodat Crushed Rock (historical)
Tryon (historical)
Downing Station (historical)
Pyramid (historical)
Fluhrers Spur (historical)
Inglis Station (historical)
Palm (historical)
Bugby (historical)
Parsons (historical)
Aldrich Point (historical)
Blind Slough (historical)
Burnside (historical)
Fernhill (historical)
Van Dusen (historical)
Mill Creek Naval Spur (historical)
Tongue Point
Alderbrook (historical)
Halco (historical)
Port Dock (historical)
Meriwether (historical)
Skipanon (historical)
McGuire (historical)
Bayview Transit Mix (historical)
Surf (historical)
Seaside Lumber Company (historical)
Holladay (historical)
Irvine (historical)
Pelton (historical)
Central Oregon Fir Supply (historical)
Cascan (historical)
Brooks Scanlon Crossing (historical)
Lava Junction (historical)
Shevlin Hixon Junction (historical)
Corral (historical)
Barstow (historical)
Bonita Station (historical)
Tri-County Industrial
Maplewood Station (historical)
Highland Station (historical)
Storwest
Jefferson Street (historical)
Shops (historical)
Terwil (historical)
Coman (historical)
Fulton Park (historical)
Ryan Place (historical)
Shahapta (historical)
Garden Home Station (historical)
Pine Knot (historical)
Greenburg Station (historical)
Niles (historical)
Golf (historical)
Tualatin Mill Spur (historical)
Cahalin (historical)
Downing (historical)
Clutters (historical)
Maine (historical)
Raven (historical)
Loganville
Chemawa BPA Spur (historical)
Chemawa Station (historical)
Gravel Pit Spur (historical)
Ant Flat
Bear Creek
Bingen Gap
Birch Creek
Broughton Reach
Cottonwood Creek
Crooked Creek
Deep Canyon
Dexter Ridge
Fairview Creek
Fort Vancouver National Historic Site
Gardena Creek
Grande Ronde River
Joseph Creek
Kalama Lower Range
Kalama Upper Range
McNary Lock and Dam
Mill Creek
Morgan Upper Range
One Reef
Paradise Creek
Rainbow Creek
Reser Creek
Russell Creek
Sawtooth Ridge
Shovel Creek
Stella Range
The Dalles Bridge
Vancouver Lower Range
Vancouver Range
Walsh Creek
Warrior Rock Range
Weller Creek
Willow Lower Range
Mount Wilson
Saint Helens Turn
Calhounville
Klicker Mountain
South Channel Columbia River
Lake Umatilla
Big Spring Branch
East Little Walla Walla River
Mud Creek
Pine Creek
Walla Walla River
Lake Wallula
Warm Springs Canyon
West Little Walla Walla River
Umatilla National Forest
McNary National Wildlife Refuge
Columbia Quarry
Fivemile Rapids Light
Ilwaco Channel
Baker Bay
Gifford Pinchot National Forest
Snake River
Number 18 Island (historical)
Salem Station (historical)
Medill (historical)
General Motors (historical)
Saint Marys (historical)
Portland General Electric (historical)
Santa Rosa (historical)
Wistaria (historical)
Milkapsi (historical)
Fearing (historical)
Moffat (historical)
Rhoades (historical)
Fern Avenue (historical)
Race Track (historical)
Thornburg (historical)
DuBois (historical)
Chiltern Spur (historical)
Outfit Spur (historical)
Haydite (historical)
Schmidlin Spur (historical)
Koster Spur (historical)
Koster Spur Number 2 (historical)
Connacher (historical)
McPherson (historical)
Poynter (historical)
Homewood (historical)
Zan (historical)
Early (historical)
Tara (historical)
Lausman (historical)
Logspur (historical)
Eastman (historical)
County Line (historical)
Watson (historical)
Webster (historical)
Glen Harbor (historical)
Waldmere (historical)
Western Ore Lumber Company (historical)
Lucerne (historical)
Albeto (historical)
Ban Spur (historical)
Tunnel Spur
McCoy (historical)
Rockton (historical)
Howe Spur (historical)
Culliton (historical)
Groveland (historical)
Connell (historical)
Twin Fir (historical)
Lincoln (historical)
Grove Lumber Company Spur (historical)
Dersham (historical)
Dixon (historical)
Pacific Plastic Pipe (historical)
Fanno Creek (historical)
Beaverton Siding (historical)
Buxton Station (historical)
Trehorn (historical)
United Junction (historical)
Plainview Station (historical)
Pengra (historical)
Dorn Spur (historical)
Menke Spur (historical)
Seavy Hop Spur (historical)
Montague (historical)
Grays Spur (historical)
South Fork Industry Track (historical)
Durham Station (historical)
Scollard (historical)
Hazelau (historical)
Croisan (historical)
Cauthorn (historical)
Fordmill (historical)
Relf (historical)
Linnore (historical)
Albany Yard
Pirtle Station (historical)
Gray (historical)
Ehlen-Van Waters and Rogers
Bellplain (historical)
Faybell (historical)
American
Timber Incorporated Spur (historical)
Western Farmers Spur (historical)
Junction City Remilling (historical)
Valley Plywood Company Spur (historical)
Crown Zellerbach (historical)
Team Track (historical)
Fox Valley Lumber Company (historical)
North End Lumber Company (historical)
Ross (historical)
Bethel
Coover (historical)
SP Connection Albany
Lebanon OE Connection (historical)
Lebanon OE Siding (historical)
Evansville (historical)
Lebanon Lumber Company (historical)
Pacific Northwest Moulding Company (historical)
Kelley Timber Products (historical)
Kenshaws-Bauman Sales Incorporated (historical)
Bauman Lumber Company
M B Christianson (historical)
Gas Heat (historical)
G and G Lumber Company (historical)
Timber Owners Incorporated (historical)
Kell Lumber Company (historical)
Benjo Milling Company (historical)
J H Baxter Company (historical)
Mid Plywood Incorporated (historical)
End of Track (historical)
End of Track (historical)
Stock Yard Spur (historical)
Warrenton Clay Spur (historical)
Bioproducts (historical)
Point Adams Station (historical)
Fort Stevens Station (historical)
Crest (historical)
Ingraham Spur (historical)
Ryan (historical)
Malin Station
North Portland Junction
Bellevue (historical)
Colorado Lake (historical)
Harbor Siding
Melas (historical)
Port Westward Spur
Boise Cascade Plywood
Oak Grove School (historical)
Hardy
Beaverton
Bendemeer
Bowers Junction
Brownsmead
Burlingame
Calapooia
Christie (historical)
Clatsop Station (historical)
Columbia City
Dant
Dellmoor Station
Deschutes
Dike
Duroc
Elmonica
Folkenberg
Glenwood
Glenwood (historical)
Hopmere
Johnson Crossing
Kerry
Locoda (historical)
Miller (historical)
Myrick (historical)
Nasoma (historical)
Neawanna Station (historical)
North Junction
Oregon Trunk Junction
Ring (historical)
Roberts
Saint Louis Station
Smeltz
Stone Bridge
Talbot
Terrebonne
United Junction
Vadis
Vansycle
Verdure
Waterview
Wayland
Willbridge
Woodraffe
Woodson
Jersey (historical)
South Klamath (historical)
Dead Point Creek
Lindsey Creek
Junipers Reservoir
Abernethy
Big Cliff Dam
Big Cliff Reservoir
Willowcreek
Toppin Creek
Mountain Lakes Wilderness
Toppin Creek V
Tampico Post Office (historical)
Tampico School (historical)
Baker City Canyon
Baker City Draw
Baker City Springs
Beaver Dam Creek
Beaver Dam Flat
Bendire Creek
Bendire Mountain
Bendire Ridge
Big Flat
Black Rock
Buckskin Spring
Chenoweth Middle School (historical)
Cold Spring
Whitaker Columbia Middle School (historical)
Courtrock Post Office (historical)
Dyar Rock
Earp Spring
Fisk Reservoir
Gasco
Godding Creek
Mount Grayback
Greton
Hunter Creek
Hunter Ditch
Hunter Mountain
Hunter Mountain Spring
Hunter Ranch
Juniper Spring
Kitten Canyon
Kitten Canyon Reservoir
Kitten Canyon Spring
Mailbox Canyon
Mailbox Canyon Reservoir
McArthur Creek
McArthur Spring
Millersburg
North Bully Creek
North Fork Bully Creek
Pinto Springs
Puckett Creek
Schoolmarm Spring
Shedd
Shubel School (historical)
Bunnel Creek
South Bully Creek
Steamboat Creek
Steamboat Rock
Steamboat Spring
Wecoma Beach
West Fork Bendire Creek
Wilkesboro
Willow Basin
Willow Basin Creek
Willow Basin Reservoir
Willow Basin Spring
Wilson Spring
Ballwood (historical)
Chicken Spring Canyon
Box Canyon
Red and White Airport (historical)
Peach (historical)
Gebhard Well
Windy Creek Chute
Stonewall Bank
Hardwick Well
Oregon Butte Spring
Damascus Heights
Tuffy Creek
Michael Creek
McLoughlin House National Historic Site
Old Elliott Well
Howard Ridge
Soda Lake Spring
Bobs Field
Knox Rock
Three Man Butte Well
Kings Valley Charter School
Ash Swale Shelter
Devils Spring Creek
Bishop Creek
Grant Creek
Foster Creek
Stack Creek
Orseco Post Office (historical)
Aeropuerto de los Banditos (historical)
Barker Reservoir
Buckshot Hill
Freres Log Ponds
Lyons Log Pond
Russell Bridge
Osage Park
Baker County Fairgrounds
Gunsight Pass
Bummer Ridge
Dodge Bridge County Park
Upper Rogue Regional County Park
Timothy Flats
Little Pilot Rock
Buck Rock Tunnel
Buckhorn Springs
Green Springs Powerplant
Schoolhouse Creek
Sage Hen Safety Rest Area
Poysky Slough
Beaver Power Plant
Port Westward
John Slough
Dobbins Slough
Michigan Slough
Kinnunen Cut
Steamboat Cemetery
Stillwell Slough
Prince Bridge
Sollie Smith Bridge
McKenzie Bridge
Neilson Bridge
Goodspeed Park
Marine Park
Tillamook County Rodeo and Fairgrounds
Tillamook High School
Liberty Elementary School
Wilson School (historical)
Makinster Bridge
Stillwell Park
Stillwell Bridge
Goodspeed Bridge
Tone Bridge
Johnson Bridge
Blaser Bridge
Paulina Falls Recreation Site
Ed Rogers Wayside
Schreiber Lodge Boy Scout Camp
East Fork Mill Creek
Klamath Union High School
Green Springs Junction
Chelsea
Bieber Line Junction
Falcon Heights School
Hard Hole Reservoir
Deer Creek
Fensler (historical)
Doughnut Mountain
Fumarole Bay
Crater Lake National Park Headquarters
Rim Village
Mapleton Landing County Park
Camp Quarry
Farnham Landing County Park
Neper (historical)
Hillcrest Memorial Park Cemetery
Bulb (historical)
Caveman Bridge
Swan (historical)
Brennan Palisades
Lost Lake Campground (historical)
Bear Creek School (historical)
Auberry Riffle
Bacon Flat Riffle
Hellgate Bridge
Ditch Creek Recreation Site
Fawn Creek Recreation Site
Snipe Spring
Dusty Spring Forest Camp
Coulter Tunnel
Sulphur Spring
Revenue Bridge
Wilde Ranch
Hunter Falls
Two Pan Recreation Site
Sturgil Saddle
Cloverland City Park
Chintimini City Park
Arnold City Park
Benton County Rodeo and Fairgrounds
Starker City Park
Sunset City Park
Walnut City Park
Tunison City Park
Benton Cemetery
Central City Park
Washington City Park
Franklin City Park
Porter City Park
Hulse Airstrip (historical)
Battle Mountain Forest State Park
Presbyterian Organization Site
Middle Fork John Day River Rest Area
Williams Ranch (historical)
Baker Corral
Spool Cart Recreation Site
Charles Reynolds Safety Rest Area
Pratt Ranch Airstrip (historical)
Street Creek Boating Site and Campground
Sisters Ranger Station
Peyton Bridge
Black Canyon Wilderness
Summit Spring Forest Camp
Medford Watershed
Fox Camp
Cottonwood Recreation Site
Siskiyou Aerial Project Complex
Dale Ranger Station (historical)
George Hinton Ranch
Case Place
Knapp Ranch
Wallowa Lake Lodge
Klink Reservoir
C H Jackson Ranch
Davis Ranch
Mount Vernon Hot Springs Resort
Prospect Sanitary Landfill
Blue River Ranger Station (historical)
Head Meadow
Saddle Camp
Telephone Spring Camp
Long Creek Mountain Summit
Deduct Forest Camp
Westside Elementary School
Waucoma Basin Marina
Winans Park
Red Box
Mono Creek
Paiute Reservoir
Mount Hood Meadows Ski Resort
Four Point Spring
Lions Park
Jack Franz Bridge
Smith River Ranger Station (historical)
Triangle Park
Bicentennial Park
Ruthton County Park
Bush Mound
Burnt Hill Summit
Yokum Bridge
Fords Bridge
Hardy Ranch
Whiskey Dick Ranch
Salmon Creek
McGee Sawmill
Andrews Ranch
Pitcher Ranch
Boley Ranch
Miles Ranch
Morehouse Ranch
R Morehouse Place
Eskelin Ranch
McGee Ranch
Mattis Ranch
Parks Ranch
Owen Pitcher Ranch
Horse Haven Reservoir
Harry Arnold Spring
Surprise Lake Reservoir
McKenzie - Willamette Medical Center
McKenzie - Willamette Hospital Heliport
White Place
House Reservoir
Applegate County Park
Murphy Bridge
Catlow Place
Grove Place
Calderwood Ranch
Silvey Ranch
Sherburn Ranch
Outerkirk Ranch
Outerkirk Ranch
Spongs Landing County Park
Finney Lake Airport (historical)
Wilark County Park
Northside County Park
Whiteaker Middle School
Narrows Well
Park Campground
Cullaby Lake County Park
Nelson Ranch Airport
Miles Bridge
Carter Creek
Krogel Bridge
The Heights
Caroline Raymond Bridge
Gazley
Canyon Creek Forest State Park
Irish Bend County Park
Commons Airport (historical)
Coos County Fair and Rodeo
Fir Point Christian Camp
Columbia Heights
Freewater Park
Umapine High and Elementary School (historical)
Meadowbrook Bridge
Wrights Bridge
Campus Elementary School (historical)
Sherman County Fairgrounds
Bully Creek Campground
Millsite Park
Flynn Ranch
Con Lynch Ranch
Taylor Ranch
Trojan Nuclear Plant (historical)
Whitehorse Valley
Maple School (historical)
HCB Spring
Mitchell Airstrip (historical)
Dry Rock Creek
Brennan Dam
Marks Creek Lodge
Summit Prairie School (historical)
Porfily Ranch
Marg Lake
Broadbent School (historical)
Crook County Fairgrounds
Blue Ridge Mine
Crow Spring
Lost Spring Reservoir
Dick Ranch
Obiaque Place
Goose Egg Reservoir
Quarry Reservoir
Settlement Reservoir
Walters Lake Waterhole
Northern Great Basin Experimental Range Station Headquarters
Jones Ranch
Old Tyler Place
Fort Harney Historical Monument
Angus Reservoir
Oliver Ranch
Morcom Ranch
Henry Ranch
George Ranch
McKee Ranch
Seekay (historical)
Hayden (historical)
Morcom Ranch
Mule Pasture Spring
Miller Brothers Ranch
Trowbridge Ditch
Trowbridge Ranch
Grant County Fairgrounds
Patterson Pond
Hillside School (historical)
Independent Order of Odd Fellows Cemetery
Fangollano Post Office (historical)
Fisks Post Office (historical)
Tyee Post Office (historical)
Glad Tidings Post Office (historical)
Grove City Post Office (historical)
Heisler Post Office (historical)
Hemstad Post Office (historical)
Horse Heaven Post Office (historical)
Timberline Post Office (historical)
Rough Canyon Creek
Five Draws Creek
Five Draws
Roschene Place (historical)
Scotts Cache (historical)
Catlow Spring
Early Pass Well
Chukar Guzzler
Small Guzzler
Roux Spring Reservoir
Antelope Guzzler
Buckskin Reservoir
Crawley-Rinehart Reservoir
Mud Flat Ranch
Jordan Valley Airstrip (historical)
Ancil Miller Ranch
White Ranch
Barrick and Shannon Ranch
Turnbull Peak Reservoir
BLM Field Camp
Horse Spring
Big Springs
Mann Lake Well Number Two
Tudor Ranch
Western Quartz Mine
South Rincon Reseeding Well
Campground Reservoir
Whipple Place
Walker Cabin Well
South Fork Matson Creek
Dwight Phipps State Forest Nursery
Elkton Pond
Center Ridge School (historical)
Bango Reservoir
Bingo Reservoir
Chet Curry Ranch
Blair Ranch
Charbonneau Golf Course
Willamette Valley Country Club
Sandelie Golf Course
Frontier Golf Course
Cronin Ranch
Howard Ranch
Stallard Ranch
Cutting Mine
Keys Creek Summit
Lonesome Spring Campground
Opal City School (historical)
Jefferson County Fairgrounds
Wasp Spring
Lutsey Reservoir
Wheeler High School
Wheeler County Fairgrounds
Murtha Ranch
Smith Ranch
Rattray Ranch
Igo School (historical)
Alville (historical)
H Johnson Ranch
Ajax School (historical)
Hodges Corner
Kaseburg Ranch
Fairview School (historical)
Gwendolen School (historical)
Butlers Corner
Cooks Corner
Coxs Corner
Rickmans Corner
Schillings Corner
Finnegans Corner
Clackamette Park
Burns Island Park
West Bridge Park
Hammerle Park
Wilderness Park
Sunset Park
Camassia Conservancy
Singer Creek Park
Masonic Cemetery
Independent Order of Odd Fellows Cemetery
Atkinson Park
Reiber Spring
Hush Spring
Kiely Ranch
Vinyard Lake
Laird Ranch
D Fitzgerald Ranch
Ogden Middle School
Clackamas Community College
Fopiano Ranch
Elbow Point
Chenoweth Substation
Oregon Agricultural Experiment Station
Lewis and Clark Memorial
Calderwood Place
The Dalles Substation
Gerber Reservoir North Recreation Site
Bear Creek Agate Beds
Nault Reservoir
Prowell Reservoir
Jumbo Spring
Juniper Reservoir
Thissel Ranch
Clemens Spring Reservoir
Lower Thissel Place
Thomas Spring Reservoir
Brown Flat
Triple Springs
Old Cushman Ranch
Y Y Ranch
Bell A Ranch
Carter Reservoir
Roadland Warm Springs
Lincoln Junior High School (historical)
Harney County Fairgrounds
Coffelt Ranch
Hackleman Ranch
Elliot Heights
Warm Springs Agency Office
West Hills
Miller Heights
Pinehurst Cemetery
Plum Valley
Canby Community Park
Willamette Primary School
Willamette Falls Viewpoint
Hebb County Park
Canby Grove Church Camp
Willamette Park
Deadman Pass Safety Rest Area
Smith Creek (historical)
Reynolds Ranch
Owens Ranch
Red Point School (historical)
Pete Miller Ranch
Hoffman Ranch
Albertson Ranch
Shafter Ranch
Mallets Ranch
Desert Ranch
Mrs B A Gordon Ranch
Gilbert Ranch
Mitchell Recreation Area
Copeland Trough Spring
Riley Place
Harper School
Thompson Ranch
Ruby Springs Well
Witzel Ranch
Krumbo Mountain Reservoir
Harold Otley Place
Section Nineteen Reservoir
Whiskey Creek Reservoir Number Two
Whiskey Creek Reservoir
Antler Seep
Bird Fence Reservoir Number Two
Bird Fence Reservoir Number One
Frazier Lake Waterhole
Moon Hill Lakebed
Moon Hill Reservoir
Basin Reservoir
Juntura Elementary School
Allen Airstrip (historical)
Gulch Place
Bridge Creek Reservoir Number One
Bridge Creek Reservoir Number Two
New Road Reservoir
Knox Spring Reservoir
End Reservoir
East Rim Reservoir
Little Mud Creek Reservoir
Butte Creek Reservoir
Page Springs Recreation Site
Frazier Field Reservoir
Company Trough
Pickett Corrals
Jack Fine Place
M Glenn Place
Boardgate Waterhole
Kundert Place
Fred Wicker Place
Colt Waterhole
Mustang Waterhole
Frenchglen Hotel State Park
Lower Antelope Reservoir
Lower Road Reservoir
Larkspur Reservoir
Hilbert Ranch
Bird Waterhole
Witzel Patrol Station
Del Witzel Reservoir
Frazier Lake
Hog Wallow Well
Tombstone Spring
Bradeen Crossing
Blitzen Crossing Campground (historical)
Clemens Place
Burnt Car Spring
Tombstone Reservoir
Ysassio Creek
Starbuck Homestead
Andrews School (historical)
Knob Spring Reservoir
Horseshoe Spring
Middle Reservoir
Rock Creek Reservoir
Gil Thompson Reservoir
Antelope Spring Road Reservoir
D Hammond Place
W H Jones Ranch
Jackman Park Campground
Indian Burial Ground
Gaston Elementary School
Gaston Junior and Senior High School
Oregon State Fish Hatchery
Mission Creek Dam
Mission Landing
Jewell School
Weaver Ranch
Palmer Ranch
Dorrance Ranch
B and H Ranch
M Birkmaier Ranch
Paulson Ranch
Chico Camp
Fine Ranch
Davis Ranch
Baker Ranch
Arthur Creek Camp
Poison Spring
Bacon Reservoir
Dunn Spring
Howard Spring
Camas Valley School
Camas Valley High School (historical)
Trout Lake Campground
Old Pelican Bay Camp (historical)
Echo Pit Tank
Evans Pit Tank
Black Hills Guard Station Spring
Horseshoe Bend Bridge
Gwynn Bridge
Three Spring
Brown Spring
Cave Hollow
Shasta Gap
Anderson Ranch
Anderson Valley Ranch
Bill Griffin Ranch
Sullivan Corral
Scappoose Middle School
Petersen Elementary School
Georgetown (historical)
Adobe (historical)
Wood (historical)
Oak (historical)
Bell (historical)
Bridge (historical)
Mill River Park
Seaview Lake
Bay City Reservoir
Sweet Home City park
Sweet Home Junior High School
Langmack Hospital
Sweet Home High School
Cotton Creek
Tadmor Lake
McDowell Creek Evangelical Church Camp
Jazel Reservoir
Piper Reservoir
Gedney Creek County Park
Foster Elementary School
Northside Park
Clarke Orchard
Savage Grade
Clayton Ranch
Schmidt Ranch
Deely Twomey Ranch
Builta Ranch
D A Tracy Ranch
Behm Ranch
Goose Lake Timber Camp
Redmond-Bend Juniper State Park
Oaklea Middle School
Santiam Golf Club
Wildwood Park
West Stayton School (historical)
Yamhill-Carlton High School
Porter Boone Park
North Santiam School (historical)
Horn Airport
Marcola Elementary School
Nettle (historical)
McMinnville Reservoirs
Michelbrook Country Club
McMinnville Hospital
Whiteson Dip Bridge
Grub College School (historical)
Yamhill County Fair and Rodeo Grounds
Bowlus Ditch
Dorothy Ditch
Spence Ditch
Zell Ditch
Burley Creek
Sheridan High School
Willamina High School (historical)
Willamina Elementary School
Buell School (historical)
Killin Bridge
Francis Davis Airport (historical)
Frog Pond
Tile Factory Bridge
Adams Airport (historical)
Monitor Bridge
Evans Valley
Ebner County Park
Mark Twain Middle School
Marion County Health Center
Hayesville Cemetery
Livingston City Park
McKay High School
Blue Gill Lake
Santana County Park
Four Corners
Labish Creek
Oregon State Hospital
Oregon Women's Correctional Center
Salem General Hospital
Grant City Park
Wilson Park
Orchard Heights City Park
Englewood City Park
Eola Bend County Park
Holman State Park
Stone Quarry Lake
Oakdale
Country Estate
Oregon State Game Commission Regional Headquarters
Horse Creek Reservoir
Monument Reservoir
Bed Ground Reservoir
Oak Elementary School
Sunrise Park
Draper Park
Periwinkle Elementary School
Brownsville State Wayside (historical)
Norma Pfeiffer Park
Coburg Elementary School
Wilkins (historical)
Kriska Mine
Deppy Ranch
Carlson Ranch
Alexander Mine
Mud Puddle Pit
West Pit
East Pit
South Turnbull Reservoir
West Turnbull Pit
Army Bridge
Howard Anderson Place
Arrowhead Reservoir Number Three
Arrowhead Reservoir Number Two
Arrowhead Reservoir Number One
Renwick Ranch
Porcupine Reservoir
Rough Spring
Chickamin Mine
Desert Lawn Memorial Cemetery
Dubious Reservoir
Seven Devils Mine
Harper Airstrip (historical)
Lower Black Canyon Reservoir
Quesna County Park
Adrian High School
Cranberry Corners
Carl Smith Ranch
One-Oh-One Ranch
Thompson Ranch
Beckley Ranch
North Bend City Hall
Keizer Memorial Hospital (historical)
East Branch Gervais Creek
Wheeler Siding
Vosburg Creek
Port of Bay City Boat Moorage
Griggs School (historical)
Masonville Community Hall
Happy Valley Community Hall
Cape Kiwanda County Park
Cathedral City Park
James John Elementary School
Saint Johns City Park
Chimney City Park
Gatton Cemetery
Sunset Gardens
Barnes Heights
University of Oregon Medical School Primate Center (historical)
Arleda Park
Shadywood Park
Rock Creek Golf Course
Waible Gulch
R A Brown Middle School
Valley Memorial Park Cemetery
W L Henry Elementary School
Washington County Fair Complex
Tillamook Junction
Banks High School
Banks Junior High School
James Cemetery
Samaritan Lebanon Community Hospital
Tolstoj Sokol Lodge
Monmouth Elementary School
Interstate Log Pond
V & S Junction
McLain Island
Glide Elementary School
Colliding Rivers Park
Glide Bridge
Glide Community Hall
Glide Upper Elementary School (historical)
Glide Middle School
Glide High School
Floyd Frear Bridge
Laurel Hill
Harmon Airport (historical)
Twin Rivers Campground
Pitchford Boys Ranch
Stage Coach Forest State Park
Glendale High School
Sunny Wolf Charter School
Wolf Creek Inn State Park
Johnson Lake
Gladstone Park Seventh Day Adventist Camp
Rivergare Adventist Elementary School
Rivergreens Golf Course
Riverside County Park
Youth Adventure Park
Keser Israel and Shaarie Torah Cemetery
Saint Joe Crossing
Farmers Union Hall
Morrison Campus Alternative Program
Dallas High School Morrison Campus (historical)
Gunaldo Falls
Wilson River Safety Rest Area (historical)
Skibbereen Bridge
Seaside Golf Course
Dog Thief Point
Wilark Guard Station (historical)
Birkenfeld Bridge
Lower Midland Bridge
Arcadia Bridge
Rainier High School (historical)
Clatskanie Middle - High School
Clatskanie Elementary School
Clatskanie Station
Clatskanie City Park
Oregon State Forestry District Headquarters
John Warren Field
Boonesborough
Tapiola Park
Astoria Bridge Toll Plaza
Columbia Memorial Hospital
Astoria Reservoir Number Two
Lewis and Clark River Bridge
Youngs Bay Bridge
Eiguren Ranch
Grafton Ranch
Greene Ranch
Stitzel Ranch
John Lequerica Ranch
Loren Miller Ranch
Uriquiaga Ranch
Larrusea Ranch
Fretwell Ranch
Elwood Ranch
Arlington Elementary School
Arlington High School
Shindler Bridge
Jefferson Elementary School
Looking Glass Park (historical)
Thurston Middle School
Springfield Country Club
Wait City Park
Rockland (historical)
Dierickx Field
Stud Horse Creek
Kleinschmidt Airport (historical)
Gresham High School
Aspen Highlands Park
Burlingame Creek
East Rockwood Park
North Rockwood Park
Centennial Middle School
Lynch Meadows Elementary School
Lynchview City Park
South Rockwood Park
Vance Park
Oregon City Hospital
Oregon City Service Learning Academy
Library Park
Tennis Court Park
Latourette Park
Scouters Mountain
Gresham Pioneer Cemetery
Mountain View Golf Course
Maple Park
Dexter McCarty Middle School
Pleasant Valley Golf Course
Wilsada Park
Sabin Airport (historical)
Warner's Airport
Locust Grove School (historical)
Summers Ranch
Arbogast Ranch
Hartford Ranch
H Smith Ranch
Weatherford Ranch
Baird Ranch
Oregon State University Agricultural Experiment Station
The Pendleton Round - Up Rodeo Grounds
Pendleton High School
Pendleton Ranger Station
Pendleton Community Park
Sunridge Middle School
Nyssa Middle School
Nyssa Elementary School
Malheur Memorial Hospital
Nyssa High School
Beck-Kiwanis Park
Saint Alphonsus Medical Center
Ontario Middle School
Ontario High School
Malheur County Fairgrounds
Ontario State Park
Lions Park
Ontario Safety Rest Area
Ontario Municipal Golf Course
Otley Ranch
Caldwell Ranch
Vickers Lake
Hills Ranch
Headquarters Malheur National Wildlife Refuge
Crows Nest Ranch
Sod House Ranch
Campbell Ranch
James Dyke Place
Bull Lake
Saunders Place
Davies Place (historical)
Tom Jenkins Ranch
Calderwood Ranch
Dixon Place
Tucker Spring
Tucker Ranch
Unit Nine Pond
Anderson Ranch
Grain Camp
McKenzie Ditch
Awbrey Park Elementary School
Santa Clara Elementary School (historical)
Hanna Ranch
P Hart Ranch
Dickinson Brothers Ranch
Tom Dowell Ranch
Obenchain Pit
Diamond Pit
Twin Buttes Reservoir
Doman Ranch
Strode Ranch
Greeley Ranch
Glover Ranch
Scott Ranch
Hole in the Ground
Happy Valley
Scotts Ranch
Huntington School
Kaser Ranch
Carter Ranch
Jim Spring
E Jones Ranch
Summit Reservoir
Creston Cabin
Badger Corral
Hehe Mill Rodeo Grounds
Benton Lane Park
Coon Town (historical)
Bishop Ranch
Ant Hill Reservoir
Darkey Mountain Spring
Huckleberry Spring
Lampa Mine
Timon (historical)
Iowa Mine
Hamdock Creek
Brogan Elementary School (historical)
Bowden Guzzler
Gearhart School
Bly Siding
Northfork
Jones Canyon
Berdugo
Corral Creek
Rock Creek Sinks
J Miller Place
BLM Field Camp
Pete French Round Barn State Heritage Site
O'Toole Ranch
Rieth Bridge
Oregon State University Agricultural Experiment Station
Picnic Area Number Two
Gilchrist Elementary School
Thunder Beast Park
Condon Elementary School
Condon Golf Course
Condon High School
Gilliam County Fairgrounds
Cooney Ranch
Greiner Ranch
Oux-Kanee Overlook
Lucky Reservoir
Switchback Spring
Sherlock Ranch
Deter Ranch
Abert Rim Historical Marker
Wright Ranch
Pike Ranch
Edmundsen Ranch
Jenkins Ranch
Becker Ranch
Corrigal Ranch
Swamp Creek Place
Jones Hill Summit
Arlington Rodeo Grounds
Sutherlin City Park
Sutherlin Knolls Golf Course
West Sutherlin Intermediate
Cornwall Historical Marker
Independent Order of Odd Fellows Cemetery
Oakland Elementary School
Lincoln Middle School
Sutherlin Middle School
Sutherlin High School
East Sutherlin Primary School
Acton Spring
Alvin Baker Ranch
Campbell Park
Godfrey Park
Nob Hill
Grant Watts Elementary School
Hood River Golf Course
Sauvie Island Game Management Area
Sauvie Island Bridge
Vale Elementary School
Wadleigh City Park
Vale Middle School
Vale High School
Wilbur Ranch
Rogers Place (historical)
Cold Springs Ranch
Rock Spring
Harry Littlefield Ranch
Camp Crestwood
Rosedale Elementary School
Art Brandt Airport (historical)
Williams Spring Number Four
Portland Adventist Academy
Woodland Park Hospital (historical)
Hancock City Park
Shriners Hospital (historical)
Van Raden Reservoir
Shadybrook Cemetery
Columbia Safety Rest Area (historical)
Charlton (historical)
Tide Creek (historical)
Saunders Place
Demaris Place
Hucrest Elementary School
Roseburg Junior Academy
City of Roseburg Sewage Disposal Plant
Roseburg Sanitary Landfill
Lookingglass Sanitary Transfer Station
Melrose Bridge
North Fork Roberts Creek
Winston Bridge
Sunnyslope Elementary School
Green District Sewage Disposal Ponds
Roseburg Municipal Golf Course
Douglas County Cemetery - Old Masonic Cemetery
Douglas County Home
Roseburg High School
Saint Joseph Parish School (historical)
North Umpqua Sewage Disposal Plant
Mercy Medical Center
Veterans Affairs Roseburg Healthcare System Roseburg Medical Center
Douglas Community Hospital
Fir Grove Elementary School
Rose Elementary School
Elk Island (historical)
Umpqua Park
Douglas County Fairigrounds Complex and Speedway
Chesterbrook Post Office (historical)
Reliance (historical)
Cooperative Park (historical)
Albany Lumber and Supply (historical)
City Limits (historical)
Bully Creek
North Fork Indian Creek
Lens (historical)
Deadhorse Mountain
Blitzen Valley
Honey Creek
Victor View
Siskiyou National Forest
Smith Reservoir
Marvin Fast Reservoir
South Johns Creek
Monument Rock Wilderness
Rimrock Reservoir
Walker Ridge
Cricket Flat Grange Hall
Igo Grange Hall
McMinnville Grange Hall
Nestucca Grange Hall
Webfoot Grange Hall
White Eagle Grange Hall
Eastern Star Grange Hall
Lena Grange
Lexington Grange Hall
Holcomb Grange Hall
Scholls Grange Hall
Tualatin Grange Hall
Ramsey Park Grange
Morning Star Grange Hall
Charity Grange Hall
Washington Grange Hall
Fernwood Grange Hall
Waldo Hills Grange Hall
Richardson Gap Grange Hall
Sumner Grange
Techumtas Island (historical)
Switzler Island (historical)
South Deer Creek Grange
Marys River Grange
Midland Grange
La Bar Creek
Barber Creek
Schoolhouse Creek
Sharon Creek
Davis Rapids
Rock Canyon
Rice Creek
South Bend McLeod Creek
Elk Creek
Stout Creek
Bellstrom Canyon
Coon Creek
Slover Creek
Ackerley Creek
Cannery Point
Wendson Canyon
Enchanted Valley
Culver Creek
Demming Creek
Skunk Hollow
Bull Island
Barrett Lake
Lilly Lake
Summerbell Arm Woahink Lake
Cougar Creek
Erhart Cove
North Beach Bay
Miles Canyon
Young Creek
King Creek
Silver Creek
John Sims Creek
The Isthmus
Snake Point
Holden Creek
Pretty Gulch
Spike Arm
Bear Trap Arm
Fiddle Creek Arm Siltcoos Lake
Frarey Creek
Camp Seven Gulch
Otter Slough
S P Gulch
Plainview Grange
Keating Grange Hall
Grange Hall
McKinley Grange Hall (historical)
Columbia Grange Hall
Poison Creek Grange (historical)
Rhea Creek Grange
Haystack Grange
Cold Springs Grange Hall
Myrick Grange Hall
Drewsey Grange
Island Number 17 (historical)
Island Number 18 (historical)
Bovine Creek
Beale Lake
Big Sheep Creek
Carlon Ranch
Camp Howard
Cassidy Creek
Cedar Creek
China Diggings
Colestin
Clemons Place
Detroit Lake
Do Little Flat
Douthit Springs
Dutchman Peak
Eckman Slough
Elko Camp Recreation Site
Flume Gulch
Fredenburg Butte
Glass Buttes
Duffy Creek
Gold Hill
Horse Lake
Hooskanaden Creek
Klingers Camp Historical Marker
Lake of the Woods
Bernhardt Creek
Leggett Gulch
Linton Meadows
Middle Bald Prairie
Moffitt Butte
Necanicum Junction
Panther Creek
Seekseequa Creek
Seeley Spring
South Fork Rock Creek
South Fork Sweet Creek
Norcross Creek
Splintercat Creek
Stancliffe Creek
Starvation Spring
Steer Creek
Thorn Spring
Three Canyon
Tierra Del Mar
Toolbox Spring
Twin Reservoirs
Vale Oregon Main Canal
Waconda (historical)
Wasson Creek
Wasson Lake
West Prong Little Walla Walla River
Westlake
Willy Rock
Turner Creek Camp
Carpenters Island
Dunes City
Recession Lakes
Memaloose Island
Wild Rogue Wilderness
Rainy Lake Recreation Site
Siuslaw National Forest
Almeda County Park
Sand Springs Compensation Station
High Lake Rim Recreation Site
White River Station Recreation Site
Johnson City
Maywood Park
Scotch Creek
Wild Horse Creek
Lilly Mountain
Mud Lake Ridge
Battle Rock Arch
Haystack Rock Arch
Sea Lion Rock Arch
Twin Rocks Arch
Claron Arch
Rock Bridge
Devils Punchbowl Arch
Fort Umpqua (historical)
Neabeck (historical)
Tiff (historical)
Summit Siding (historical)
Walling (historical)
Magones (historical)
Junction (historical)
Tualatin River (historical)
Buena Vista (historical)
Colis (historical)
Campine (historical)
McBain (historical)
Glen Oak (historical)
Swift (historical)
Eby (historical)
Cemetery Spur (historical)
Ingram (historical)
Spangler (historical)
Lewis (historical)
Buckner Creek (historical)
Howard (historical)
North Liberal (historical)
Huntley (historical)
Richard (historical)
Kayler (historical)
Hitchman (historical)
Busch (historical)
Beaver Creek Station (historical)
Bear Creek Junction (historical)
Davis (historical)
Agate Station (historical)
Table Rock Station (historical)
Mountain View (historical)
School House Gap (historical)
Duprays Mill (historical)
Switchback
Johnson (historical)
Woods (historical)
Cedar Creek (historical)
Fairchilds (historical)
Chesterbrook (historical)
Swan Lake (historical)
Hildebrand Station (historical)
East Switchback (historical)
Sycan (historical)
Kesterson Spur (historical)
North Fork (historical)
Sears (historical)
Mohr (historical)
Dukes Valley (historical)
Camp 1 (historical)
Allen Creek (historical)
Sand Creek (historical)
Prairie Creek (historical)
Boulder Gorge (historical)
Mason (historical)
Curry (historical)
South Wye (historical)
Alder Springs (historical)
Corrin (historical)
Dorena (historical)
Row River Lumber Company Number 2 (historical)
Cerro Gordo (historical)
Baker (historical)
Red Rock (historical)
Gravel Pit (historical)
Stewart (historical)
Rocky Point (historical)
Hunts (historical)
Johnson Spur (historical)
Montgomery Spur (historical)
Slayton Spur (historical)
Wilton (historical)
Davis Weber Lumber Company (historical)
North Santiam (historical)
North Santiam (historical)
Hardesty Lookout Tower
Lake of the Cedars
Banks Creek
Panda Ridge
Boccard Point
Elkhorn Mountains
Peggy Creek
Cutler City
Nelscott
Oceanlake
Tibbs Creek
Fernwood Pioneer Cemetery
Wiesendanger Falls
Fir Clearing Creek
Egli Rim
Egli Ridge
Chiefs Island
Joe Champion Creek
Schmeltzer Creek
Right Fork Rat Creek
Multnomah Falls
Huss Ridge
Roads End Point
Boo Boo Lake
Bug Lake
Deer Camp Lake
Wildcat Creek
Windfall Lake
Palm Cemetery
Charlton Landing
The Lagoon (historical)
Charlie Creek Reservoir
Ki-a-Kuts Falls
Sawtell Cemetery
Camp Alden (historical)
Camp Alvord (historical)
Camp Barlow (historical)
Camp Blossom
Camp Currey (historical)
Camp Currey Spring
Camp Dahlgren (historical)
Camp Gibbs (historical)
Camp Gordon (historical)
Camp Henderson (historical)
Camp Lincoln (historical)
Camp Maury (historical)
Camp McDowell (historical)
Camp McKinley (historical)
Camp Russell (historical)
Camp Spencer (historical)
Camp Stuart (historical)
Canoe Encampment Rapids (historical)
Cemetery Hill
Charbonneau
China Creek
Claypool Bridge
Combs (historical)
Curiosity Creek
Camp White (historical)
Ballard Landing (historical)
Audison Creek
Foise (historical)
Fulquartz Landing (historical)
French Prairie (historical)
Fort Lee (historical)
Fort Hayes (historical)
Fort Bailey (historical)
Fort Orford (historical)
Fort Rowland (historical)
Fort Umpqua (historical)
Fort Vannoy (historical)
Fort Yamhill (historical)
Fort Kitchen (historical)
Hillside Community Center
Davidson Hill
Dundon Bridge
Ehrck Hill
Gatton Creek (historical)
Getchel Meadows
Gilchrist Valley
Glenora (historical)
Gone Creek (historical)
Gray Eagle Bar
Guild Lake (historical)
Finn Rock
Harlow Crater
Hoods Bar Light (historical)
Howard Spring
Hudson Bay (historical)
Ince Camp (historical)
Johns Landing
Kittredge Lake (historical)
Chief Joseph Island
Keeps Mill (historical)
Kent Station (historical)
Fivemile Rapids (historical)
Fox Hill
Lenz Butte
Latta Crater
Little Santiam River (historical)
Lasater Reservoir
Mother Lode Mountain
Moss Lakes (historical)
Mouse Island Lake (historical)
Switzler Lake (historical)
Owyhee Rapids (historical)
Tanner Creek (historical)
McNamers Camp (historical)
Oak Point (historical)
Plaza Guard Station (historical)
Puget Bar
Shonquest Ranch (historical)
Rays Landing (historical)
Rigdon Meadows
Stotts Landing (historical)
South Canyonville (historical)
Camp Castaway (historical)
Shepperds Dell
Sheep Shooter Tree (historical)
Stringtown (historical)
Salene Lake (historical)
Saint Helens Station
Tanasbourne
Tokyo Slough
Tenmile Rapids (historical)
Tepee Springs (historical)
Ten O'Clock Church
Tupper Rock (historical)
Treasure Cove
Vansycle Canyon
Venator Canyon
Alkali Valley
Wells Cove
Wickiups (historical)
Witches Cauldron
Wright Creek (historical)
Widby Loops (historical)
Wahclella Falls
Sodhouse (historical)
Pulpit Rock
Rhoades Spring
Cascade Head Experimental Forest
Osprey Bay
Reids Mill (historical)
Robins Nest (historical)
Uniontown
Klamath National Forest
Whitman National Forest
Arcadia Beach State Park
Del Rey Beach State Park
Manhattan Beach State Park
Mary S Young Park
McVay Rock State Park
North Santiam State Park
Ocean Shore State Recreation Area
Warm Springs State Recreation Site (historical)
Fishing Rock State Park
Gearheart Ocean State Park
Neakahnie-Manzanita State Park
Wyeth State Park (historical)
Tryon Creek State Park
Elmer Feldenheimer Forest Reserve
John Yeon State Park
L Presley and Vera C Gill State Park
McLaughlin State Park
Yoakam Point State Park
Illinois River Forks State Park
Umpqua Lighthouse State Park
Bowers Rocks State Park
Bridal Veil Falls State Park
Wallowa Lake Highway Forest State Park
Bonneville State Scenic Corridor
Wilson River Highway Forest State Park
Banks-Vernonia State Trail
Historic Columbia River Highway State Trail
OC&E Woods Line State Trail
Boring-Estacada Rail Line
Armitage (historical)
Adobe Camp (historical)
Balch Creek
Beggars Tick Wildlife Refuge
Ben Jones Bridge
Besters Ford
Bishop Meadows
Boones Ferry
Briggs Landing
Bruces Bones Creek
Bunker Hill
Bybee Bridge (historical)
Cape Blanco State Park
Portland Womens Forum State Park
Kam Wah Chung State Park
Sumpter Valley Gold Dredge Museum
Camp Wright (historical)
Pine Hollow
Deschutes River Woods
Hazelwood
Mount Hood Village
North Springfield
Oak Hills
Redwood
River Road
Rockcreek
South Lebanon
Three Rivers
Tri-City
Agency Lake Resort
Haines Cemetery
Auburn Cemetery
Big Creek Cemetery
Boyer Family Cemetery
Baker City Chinese Cemetery (historical)
Durkee Cemetery
Hibbard Creek Cemetery
Koontz Family Cemetery
McEwen Cemetery
Pleasant Valley Cemetery
Rosenberg Hill Cemetery
Saint Francis de Sales Catholic Cemetery (historical)
Trimble Family Cemetery
Whitney Cemetery
Our Mountain
Deschutes National Forest Headquarters
Bend - Fort Rock Ranger District
Mount Hood National Forest Headquarters
Estacada Ranger Station
Prineville Ranger Station (historical)
Allison Ranger Station
Crooked River National Grasslands Headquarters
Rogue River National Forest Headquarters
J Herbert Stone Nursery
Siskiyou National Forest Headquarters
Galice Ranger Station
Illinois Valley Ranger Station
Powers Ranger Station
Siuslaw National Forest Supervisor's Office
Umatilla National Forest Headquarters
Heppner Ranger Station
Cottage Grove Ranger Station
Dorena Tree Improvement Center
Baker Ranger Station
La Grande Ranger District
Willamette National Forest Headquarters
McKenzie River Ranger Station
Sweet Home Ranger Station
Lowell Service Center
Klamath Ranger District
United States Fish and Wildlife
Grass Well
Tutuilla
Waldo Park
Baker High School
Battle Mountain Forest State Scenic Corridor
Baker City Golf Club
Crissey Field State Park
Soap Creek Post Office (historical)
Morgan Creek
Parrett Mountain Access
Gateway State Wayside (historical)
Row River (historical)
Mike Robinson Spring
Rainbow Hill
Red Hill
Equisetum Canyon
Red Scar Knoll
Whitecap Knoll
Black Spur
West Fork Battle Creek
Chicken Whistle Creek
Metasequoia Creek
Thorn Hollow
Benham Falls West Recreation Site
Big Eddy Recreation Site
Cinder Beach Recreation Site
Crescent Lake Sno-Park
Cultus Cove Recreation Site
Deschutes Bridge Recreation Site
Dutchman Sno-Park
Head of Metolius Recreation Site
Junction Sno-Park
Lavacicle Cave Recreation Site (historical)
Meissner Sno-Park
Osprey Point Recreation Site
Simax Beach Recreation Site
Skyliner Sno-Park
Suttle Lake Water Ski
Swamp Wells Horse Camp
Three Creek Meadow Horse Camp
Todd Horse Camp
Vista Sno-Park
West South Twin Recreation Site
Windy Group Camp
Canyon Meadows Recreation Site
Boulder Lake Recreation Site
Cove Recreation Site
North Arm Recreation Site
Tollgate Recreation Site
Cyrus Horse Camp
Delintment Lake Recreation Site
Elkhorn Recreation Site
Haystack West Shore Recreation Site
Doe Point Recreation Site
Hamaker Recreation Site
Big Pine Recreation Site
First Camp Recreation Site
Game Lake Recreation Site
Island Recreation Site
Laird Lake Recreation Site
Lobster Creek Recreation Site
Lockhart Recreation Site
Miller Bar Recreation Site
Nook Bar Recreation Site
Oak Flat Recreation Site
Packers Cabin Group Camp
Page Mountain Sno-Park
Peacock Recreation Site
Redwood Bar Recreation Site
Sam Brown Horse Camp
Shasta Costa Overlook
Sixmile Recreation Site
South Fork Camp Recreation Site
Store Gulch Recreation Site
Taylor Gorge Overlook
Alder Springs Recreation Site
Big Lake West Recreation Site
Cougar Creek Recreation Site
Cougar Crossing Recreation Site
Cove Creek Recreation Site
Detroit Flats Recreation Site
Ferrin Recreation Site
Hard Rock Recreation Site
Indigo Springs Recreation Site
Johnny Creek Recreation Site
Larison Cove Canoe-In Recreation Site
Lookout Recreation Site
Red Diamond Recreation Site
Santiam Flats Recreation Site
Sunnyside Recreation Site
Taylor Burn Recreation Site
Terwilliger Hot Springs Recreation Site
Three Pools Recreation Site
Wolf Mountain Recreation Site
Yukwah Recreation Site
Corral Springs Recreation Site
Rocky Point Recreation Site
Summit Sno-Park
Walt Haring Sno-Park
Mount Thielsen Wilderness
Coquille River Lighthouse
Bowden Crater
Straight Pioneer Cemetery
Ogden Hill
Adrian Division
Newport Division
Agness Division
Albany Division
Antelope Division
Arlington Division
Ashland Division
Ashwood Division
Astoria Division
Athena Division
Badger Mountain Division
Baker City Division
Bandon Division
Bay City Division
Beaver Division
Beavercreek Division
Beaverton-Hillsboro Division
Bend Division
Boardman Division
Brogan Division
Brookings Division
Brownsville Division
Burns Division
Butte Falls-Prospect Division
Sutherlin Division
Canby Division
Carlton Division
Cascade Locks Division
Cave Junction Division
Chehalem Mountains Division
Chiloquin Division
Clatskanie Division
Coast Range Division
Coburg Division
Colton Division
Condon Division
Coos Bay Division
Coquille Division
Corbett Division
Corvallis Division
Cottage Grove Division
Cove Division
Crescent Lake Division
Creswell Division
Crooked River Division
Culver Division
Dallas Division
Dayton-Amity Division
Dead Ox Flat Division
Dee Division
Lincoln City Division
Depoe Bay Division
Diamond Division
Drewsey Division
Dufur Division
Eagle Point Division
Eagle Valley Division
East Linn Division
Eastside Division
Eddyville Division
Elgin Division
Elkton-Drain Division
Enterprise Division
Estacada Division
Eugene-Springfield Division
Falls City Division
Flora Division
Forest Grove-Cornelius Division
Fossil Division
Goble Division
Gold Beach Division
Grandview Division
Grants Pass Division
Halfway Division
Harbor Division
Harrisburg Division
Heppner Division
Hereford Division
Hood River Division
Hubbard Division
Huntington Division
Imnaha Division
Ione-Lexington Division
Jefferson Division
Jewell Division
John Day Division
Jordan Valley Division
Joseph Division
Junction City Division
Juntura Division
Kellogg-Yoncalla Division
Keno Division
Klamath Falls Division
Knappa-Brownsmead Division
La Grande Division
Lakeview Division
Langell Valley Division
Lebanon Division
Long Creek Division
Lowell Division
McKenzie River Division
McMinnville Division
Madras Division
Malheur Junction Division
Malin Division
Marcola Division
Marshland Division
Medford Division
Melrose Division
Merrill Division
Middle Siuslaw River-Triangle Lake Division
Mill City Division
East Marion Division
Mitchell Division
Molalla Division
Monmouth-Independence Division
Moro Division
Mount Angel Division
Mount Hood Division
Mulino Division
Myrtle Creek-Riddle Division
Myrtle Point Division
Nehalem Division
Neskowin Division
Newberg Division
North Albany Division
North Bayside Division
North Benton Division
Milton-Freewater Division
North Plains Division
Florence Division
North Umpqua Division
Northwest Clackamas Division
Northwest Jackson Division
Northwest Josephine Division
Hermiston-Umatilla Division
Nyssa Division
Oakridge Division
Prineville Division
Odell Division
Ontario Division
Owyhee Division
Parkdale Division
Pendleton Division
Pilot Rock Division
Pleasant Hill Division
Yonna Valley-Poe Valley Division
Portland Division (historical)
Port Orford Division
Powell Butte Division
Powers Division
Prairie City Division
Rainier Division
Redland Division
Redmond Division
Reedsport Division
Umatilla Reservation Division
Roseburg Division
Saint Helens Division
Saint Paul Division
Salem Division
Salem Division
Sams Valley Division
Sandy Division
Scappoose Division
Scio-Lacomb Division
Seaside Division
Seneca Division
Shady Cove Division
Sheridan Division
Siletz Division
Silver Lake-Fort Rock Division
Silverton Division
Sisters-Millican Division
Skyline Division
Rockcreek Division
Southeast Benton Division
Southeast Jackson Division
Dunes City Division
South Umpqua Division
Southwest Benton Division
Southwest Jackson Division
Starkey Division
Stayton Division
Summer Lake Division
Sweet Home Division
Tenmile Division
The Dalles Division
Tillamook Division
Toledo Division
Tumalo Division
Umapine Division
Union Division
Upper Siuslaw River Division
Vale Division
Vernonia Division
Waldport Division
Wallowa Division
Warm Springs Division
Warm Springs Division
Warner Valley Division
Wasco Division
Weston Division
West Bench Division
Wilderville Division
Willamina Division
Williams Division
Wilsonville Division
Wingville-Haines Division
Woodburn Division
Yoder Division
Steens Mountain Cooperative Management and Protection Area
Government Island State Recreation Area
Symons State Park
Dalton Point State Recreation Site
Wind Mountain Lower Range Channel
Oregon Islands Wilderness
Harlow Creek
Tyee View Cemetery
Painter Falls
Willamette Stone
Baughman (historical)
Hawkins Ridge
Kahneeta Hot Spring
Merwin Dam Number 1
Merwin Dam Number 3
Sixmile Creek
Crooked Finger Prairie
Antler Trailhead
Aspen Cabin Recreation Site
Bunyard Crossing Recreation Site
Can Spring Recreation Site
Chewaucan Crossing Trailhead
Clear Spring Recreation Site
Dismal Creek Recreation Site
Farm Well Recreation Site
Fishhole Recreation Site
Hadley Butte Launch Area
Hanan/Coffeepot Spring Recreation Site
Heart Lake Recreation Site
Holbrook Reservoir Recreation Site
Jones Crossing Recreation Site
Lower Buck Creek Recreation Site
Overton Reservoir Recreation Site (historical)
Pole Butte Sno-Park
Ponderosa Paraglide Launch Area
Quartz Mountain Sno-Park
Rock Creek Recreation Site
Slide Lake Recreation Site
South Fork Crooked Creek Horse Camp
Trapper Spring Recreation Site
Twin Spring Recreation Site
Upper Buck Creek Recreation Site
Upper Jones Recreation Site
Upper Marsters Spring Recreation Site
Withers Lake Recreation Site
Restless Waters Trailhead
Dry Lake Horse Camp
East Dunes Recreation Site
Horse Creek Trailhead
Horsfall Beach Recreation Site
Horsfall Recreation Site
Indian Creek Recreation Site (historical)
Launching Forest Camp Boat Launch
Marys Peak Observation Point
Meadow Sno-Park (historical)
North Ridge Sno-Park (historical)
Sandtrack Recreation Site
West Winds Recreation Site
Westpoint Sno-Park (historical)
Wild Mare Horse Camp
Andies Prairie Sno-Park
Bull Prairie Recreation Site
Coalmine Hill Recreation Site
Morning Creek Sno-Park
Winom Creek Recreation Site
Drift Wood Recreation Site
Boulder Annex Recreation Site
Howlock Mountain Horse Camp
North Crater Recreation Site
North End Boat Ramp
Watson Falls Recreation Site
Willow Flats Recreation Site
Windigo Pass Recreation Site
Auburn Sno-Park
Bird Track Springs Recreation Site
Blue Mountain Crossing Sno-Park
Blue Springs Summit Sno-Park
Buck Creek Recreation Site
Bunny Hill Recreation Site
Cache Creek Ranch Recreation Site
Catherine Summit Sno-Park
Clear Creek Sno-Park
Frog Heaven Recreation Site
Grande Ronde Group Camp
Ladd Canyon Sno-Park
Miller Lane Recreation Site
Moss Springs Horse Camp
Mount Harris Recreation Site
P O Saddle Recreation Site
Park Saddle Recreation Site
Powder River Recreation Site
Red Hill Recreation Site
Salt Creek Summit Sno-Park
Southeast Shore Recreation Site
Spring Creek Recreation Site
Turkey Flat Recreation Site
Two Color Horse Camp
Umapine Recreation Site
Eagle Creek Overlook Group Camp
Horsetail Falls Recreation Site
Multnomah Falls (historical)
Wahkeena Falls Recreation Site
Tanner Lakes
Tannen Lakes Trail
Freddie Masterson Grave
Oak Grove Cemetery
Homesteader Grave
Cushman's Pasture Cemetery
Saint Mark the Evangelist Church Columbarium
Wyeth Cemetery
Mount Hood Community Cemetery
McIsaac Ranch Cemetery
George W Weart Grave
John G Fischer Grave
Viento Cemetery
Harry Wollam Grave
Buck Creek Recreation Site
Oregon Trail Interpretive Park
East Pine Lake Well
South Ice Cave Recreation Site
Lava Crossing Cinder Pit
South Ice Cave Cinder Pit
John T Parkinson Grave
Pocahontas Cemetery
Robinette Cemetery
Sisley Family Cemetery
Sparta Chinese Cemetery (historical)
Speak Ranch Cemetery (historical)
Utter Party Cemetery
Wagon Box Burial Cemetery
Weatherby Cemetery
Hattie Wheelock Grave
Bastian Family Cemetery
Aunt Polly Cemetery
Thomas Bobbington Grave
Boot Hill Cemetery
Bourne Cemetery
Burkemont Cemetery
Clark Cemetery
Clarksville Cemetery (historical)
Hoopinggardner Cemetery
Tom Heath Grave
Haskins Yard Cemetery
Hardman Cemetery
Nathaniel Hamlin Grave
Frank Gordon Grave
Gold Ridge Mine Cemetery
Jim Fleetwood Family Cemetery
Emigrant Graves Cemetery
Ebenger Family Cemetery
Clawson Cemetery
Isaac Colt Grave
Connor Creek Cemetery
J F J Cooper Grave
Cornucopia Cemetery
Grandma Devin Grave
Thomas Creek Bridge
Neal Lane Bridge
Jordan Bridge
Office Bridge
Remote Bridge
Drift Creek Bridge (historical)
Weddle Covered Bridge
Myrtle Creek
Clark's Mountain
Aiken Canyon
Clinton Creek
Pipe Creek
Purcell Creek
Roller Creek
Sappington Creek
Shadow Creek
Spruce Creek
Couch Lake (historical)
Fort William (historical)
Frankton
McBride
Murphys Camp
Radium (historical)
Murphys Camp Creek
McClure Hill
Gumboot Canyon
Oak Grove County Park
Tucker County Park
Anderson County Park
Beazell Memorial County Forest
Clemens County Park
Fitton Green County Natural Area
Fort Hoskins Historic County Park
Hyak County Park
Jackson Frazier Wetland
North Albany County Park
Collins Creek State Park
Clark Creek City Park
Highland Park
Hillview City Park
Hoover School City Park
McKay School City Park
McKinley School City Park
Nelson City Park
Northgate City Park
Rees City Park
Richmond School City Park
Riverfront City Park
Sumpter School City Park
Sunnyslope City Park
West Salem City Park
Bear Creek County Park
Denny County Park
Lake Labish County Park
Parkdale County Park
Scotts Mills County Park
Saint Louis Fish Ponds County Park
Brandis City Park
Bald Hill City Park
Chip Ross City Park
Garfield City Park
Lilly City Park
Village Green City Park
Woodland Meadows City Park
Clackamas River Scenic Waterway
Deschutes River Scenic Waterway
Rogue River Scenic Waterway
Arlington State Park
Royal Oaks City Park
Pritchard State Park
John Day Wild and Scenic River
Eddeeleo Lakes
Erma Bell Lakes
Quinn Lakes
Salmon Lakes
Twin Lakes
Marilyn Lakes
Sunnyside County Park
Roaring River County Park
John Neal Memorial County Park
Thistle Creek County Park
Buell-Miller County Park
Lyons Mehama County Park
McClun Wayside
Alan B Berg City Park
Martin Luther King Junior City Park
Riverfront Commemorative City Park
Pioneer Boat Basin City Park
Peanut City Park
Wildcat City Park
Kermit E Roth City Park
Sandy River Scenic Waterway
Sisters Rock State Park
Whychus Creek Wild and Scenic River
Les Shirley Park
Baker Valley Safety Rest Area
Gettings Creek Safety Rest Area
Government Camp Safety Rest Area
Jantzen Beach Safety Rest Area
Memaloose Safety Rest Area
Midland Safety Rest Area
Stanfield Safety Rest Area
Weatherby Safety Rest Area
52nd & Willamette Trailhead
Arrowhead City Park
Bramblewood City Park
Brewer City Park
Cal Young Sports Park
Churchill Sports Park
Dillard Skyline City Park
Gillespie Butte City Park
Lincoln School City Park
Mission City Park
Moon Mountain City Park
River House
Scobert Gardens City Park
Shadow Wood City Park
Sheldon Sports Park
Skyview City Park
Trainsong City Park
Walnut Grove City Park
Washington/Jefferson City Park
Grassy Knob Wilderness
Menagerie Wilderness
North Fork John Day Wilderness
Opal Creek Wilderness
Rock Creek Wilderness
Table Rock Wilderness
Waldo Lake Wilderness
Oak Creek City Park
Rock Creek City Park
Austa Landing County Park
Blue Mountain County Park
Emmrich Landing County Park
Old McKenzie Fish Hatchery County Park
South Jetty County Park
Triangle Lake County Park
Vaughn County Park
Pierce Riffle County Park
Wolf Creek County Park
Hog Creek County Park
Ennis Riffle County Park
Howard Prairie County Resort
Lilly Glen County Campground
Grizzly County Campground
Fishers Ferry County Park
Savage Rapids County Park
Happy Camp County Park
Bayocean Peninsula County Park
Aiken County Park
Baxter Creek
Columbia City Park
C P City Park
Glen Otto City Park
Harlow House City Park
Helen Althaus City Park
Kiku City Park
Lewellyn City Park
Mayor's Square City Park
Sandee Palisades City Park
Sunrise City Park
Sweetbriar City Park
Weedin City Park
Woodale City Park
Airbase Reserve County Park
Netarts Community County Park
Mugg County Park
Twin Rocks County Park
Buck Run City Park
Creekside City Park
Harold Barclay City Park
Three Sisters Overnight City Park
Village Green City Park
Brown Grotto
Hardy Riffle County Park
Klum Landing County Campground
Indiola
North Fork McNulty Creek
Killin Wetlands
Cabin Lake
Chatfield Hill
Fern Rock Falls
Marsh Hill
Molinari Creek
Sherwood Forest Tot Lot
Ridgegate City Park
Salty Acres Wetlands
PTC/Abernethy Lane Trail
Dahl Beach City Park
Glen Echo Wetlands
Olson Wetlands
Valley View City Park
Baker City Park
Bowlby City Park
Firemans Lake City Park
Hayden City Park
Kalama City Park
Kiwanis Field
Qince City Park
Redmond City Skate Park
Sam Johnson City Park
Umatilla Sports Complex
Cottonwood Reservoir County Park
Ana Reservoir County Park
Egan County Park
Swimming Pool City Park
McDonald City Park
Alton Baker/Eastgate Woodlands
Bluebelle Park
By-Gully Bike/Jog Path
Harvest Landing
Jesse Maine Memorial Park
Millrace Park
Page Park
Wallace M Ruff Junior Memorial Park
32nd Street Community Sports Park
Cannon Quarry Park
Logan Road County Wayside
Mike Miller County Park
Seal Rock County Wayside
Twin Bridges County Park
Drift Creek County Park
Lakeshore City Park
Handy/Nechocokee City Park
Fairview Woods Wetlands City Park
Park Cleone City Park
Crossroads City Park
Langley City Park
Icicle City Park
Salish Ponds City Park
Gum Drop City Park
Stone City Park
Greenridge City Park
Fezett City Park
Bella Vista Park
Columbia View Park
Davis Park
Hall Park
Hollybrook Park
Jenne Butte Park
Kane Road Park
Kirk Park
Main City Park
Pat Pfeifer Park
Rockwood Central Park
Southeast Community Park
Southwest Community Park
Gradin Community Sports Park
Thom Park
Zimmerman House Historic Park
Donald L Robertson City Park
Hockaday City Park
Windstorm City Park
Marilyn's City Park
Pioneer City Park
Fairview Community Park
Pettijohn City Park
Pelfry City Park
Cedar Park
East Gresham Park
Southeast Neighborhood Park
Yamhill Neighborhood Park
Boutwell Creek
Newberry Volcano
Newberry National Volcanic Monument
Sky Lakes Wilderness
Three Arch Rocks Wilderness
Carruthers Memorial Park
Bonita City Park
Happy Valley Nature Park
Orchard Park
Commercial City Park
Fanno Creek City Park
Jack City Park
Liberty City Park
Main Street City Park
Summerlake City Park
Windmill City Park
Woodard City Park
Northview City Park
Durham City Park
Heron Grove City Park
Community Campus Park
Murdock City Park
Pioneer City Park
Stella Olsen City Park
Atfalati City Park
Browns Ferry City Park
Ibach City Park
Jurgens City Park
Lafky City Park
Little Woodrose Natural Area
Nyberg Creek Greenway
Stoneridge City Park
Tualatin Commons Park
Tualatin Community Park
Victoria Woods Natural Area
Boones Ferry City Park
Courtside City Park
River Fox City Park
Memorial City Park
Park at Merryfield
Montebello City Park
Town Center City Park
Tranquil City Park
Glencoe Creek Park
Frances Street Park
Rosebay Park
Arboretum City Park
Dogwood City Park
Free Orchard City Park
Ryland City Park
Satus City Park
Steamboat City Park
Cornelius City Park
Hembre City Park
Knox Ridge City Park
Reuter City Park
Stites City Park
Talisman City Park
Thatcher/Loomis City Park
Tualatin Commons
Saarinen Wayside Park
Hathaway City Park
Willow Creek/Landover Park
Wiedeman City Park
Bicentennial Park
Harold Eastman Memorial Rose Garden
Evergreen Park
Griffin Oaks Park (historical)
U J Hamby Park
McKinney Park
Noble Woods Park
Reedville Creek Park
Rood Bridge Park
Turner Creek Park
Walnut Street Park
Cinnamon Hills City Park
Lady Fern City Park
Langer City Park
Oregon Trail City Park
Veterans Memorial City Park
Woodhaven City Park
Wendy Kroger City Park
Chandler Nature Park
Deepwood Estate
Eastgate Basin City Park
Harry and Grace Thorp City Park
Hammond School Park
Lee School Park
Sprague School/Skyline Park
Straub Nature Park
Henry Hagg County Park
Sherman County RV Park
Gordon Faber Recreation Complex
Harbor View City Park
Portland Center City Park
Senn's Dairy City Park
Vernon Ross Veterans Memorial
Ainsworth Blocks
Ankeny Plaza
April Hill City Park
Argay City Park
Brentwood City Park
Brooklyn School Park
Brookside Park
Burlingame City Park
Butterfly City Park
Chapman Square
Cherry Blossom City Park
Portland Childrens Museum
Clatsop Butte City Park
Coe Circle
Columbia Children's Aboretum
Community Music Center
Cottonwood Bay City Park
Couch City Park
Crystal Springs Rhododendron Garden
Delta Park West
Unthank Park
Dewitt City Park
Dickinson City Park
Dickinson Woods
Disabled Citizens Recreation
Dishman Community Center
East Portland Community Center
Eastbank Esplanade
Eastmoreland Playground
Eastridge City Park
Ed Benedict City Park
Elk Rock Island Natural Area
Erv Lind Stadium
Fanno Creek Natural Area
Firland Parkway
Floyd Light Property
Forest Heights City Park
Fulton Park Community Center
Gates Park Property
Gentemann Property
George City Park
Gilbert Heights City Park
Hamilton City Park
Harney City Park
Heritage Tree Park
Heron Lakes Golf Course
Hillsdale City Park
East Holladay Park
Holman City Park
Interstate Firehouse Cultural Center
Ira Keller Fountain
Jamison Square
Japanese American Historical Plaza
Japanese Gardens
Jefferson Street City Park
Jensen Natural Area
John Luby City Park
Johnson Lake Property
Johnswood Property
Kelly Butte Natural Area
Kerr Site
King School Park
Kingsley D Bundy City Park
Klickitat Mall
Knott City Park
Ladd's Rose Gardens Circle and Squares
Lair Hill City Park
Laurelhurst Studio
Laurelwood City Park
Leach Botanical Garden
Lesser City Park
Lotus Isle City Park
Lovejoy Fountain
Lower Powell Butte Floodplain
Lownsdale Square
Lynchwood City Park
MacLeay Park Lower
Mallory Meadows Park
Maricara Natural Area
Marquam Nature Park
Marshall City Park
Mill Ends City Park
Mocks Crest Property
Montavilla Community Center
Moore Island City Park
Mount Scott Community Center
Multnomah Arts Center
North Park Blocks
O'Bryant Square
Oaks Bottom Wildlife Refuge
Oaks-Pioneer Church Park
Omaha Parkway
Oregon Park
Peninsula Crossing Trail
Peninsula Community Center
Peter Kerr Natural Area
Pettygrove City Park
Piccolo City Park
Pioneer Courthouse Square
Pittock Mansion and Acres
Portland Heights City Park
Portland International Raceway Dragstrip and Road Course
Portland Police Memorial
Portland Tennis Center
Powell Butte Nature Park
Raymond City Park
Reed College Parkway
Richmond Natural Area
Riverside Property
Rob Strasser Memorial Field
Rose City Park
Roselawn City Park
Rosemont Bluff Natural Area
Roseway Parkway
Sckavone Stadium
Sellwood Community Center
Sellwood Riverfront City Park
Senior Recreation
South Park Blocks
South Waterfront City Park
Southwest Community Center
Spring Garden City Park
Springwater Corridor Trail
Springwater on the Willamette
Saint Johns Community Center
Saint Johns Racquet Center
Stark Street Island
Stephens Creek Natural Area
Sumner-Albina Park
Sunnyside School Park
Sylvania City Park
Tenino Property
Terrace Trails Park
Terwilliger Boulevard Parkway
Thomas City Park
Thompson City Park
Toe Island City Park
Trenton City Park
Two Plum City Park
University city Park
University Community Center
Vernon Tank Playground
Vietnam Veterans of Oregon Memorial
Walker Stadium
Washington Park International Rose Test Gardens
Waterfront City Park
West Portland Park Natural Area
Whitaker Ponds Natural Area
Wilkes City Park
William V Owens Sports Complex
Woodlawn City Park
Woodstock Community Center
Johnson City Park
Meinig Memorial Park
Maple Street City Park
Beth Ryan Nature Preserve
Bryant Woods Nature Park
Campbell Native Gardens
Canal Acres Nature Park
Cooks Butte City Park
Cornell Natural Area
Ellen R Burgess Nature Preserve
Firlane Property
Foothills City Park
Freepons City Park
George Rogers City Park
Glenmorrie City Park
Greentree City Park
Glenmorrie Greenway
Hide-A-Way City Park
Iron Mountain City Park
Kelly Creek Natural Area
Kerr Natural Area
Lamont Springs City Park
Luscher Farm City Park
McNary City Park
Millenium Plaza City Park
Aspen City Park
Pennington City Park
Pilkington City Park
Pine Cone City Park
River Run City Park
Roehr City Park
Rossman City Park
South Shore Natural Area
Southwood City Park
Springbrook City Park
Sunnyslope Open Space
Waluga Park West
Westlake City Park
Westridge City Park
Woodmont City Park
Boones Ferry County Boat Launch
Carver County Boat Ramp
Wilhoit Springs County Park
Atkinson City Park
Barclay Hills City Park
Canemah City Park
Library City Park
Chapin City Park
End of the Trail Interpretive Center
Ermatinger House
Hartke City Park
Hazelwood City Park
Hillendale City Park
Old Canemah City Park
Park Place City Park
Pioneer Community Center
Sportcraft City Park
Stafford City Park
Wesley Lynn City Park
Abernethy Creek City Park
D C Latourette City Park
Rivergrove City Park
Rivergrove City Boat Ramp
Alma Myra Park
Altamont Park
Ann-Toni Schreiber Park
Ardenwald Park
Ashley Meadows Park
Bunnell Park
Dogwood Park
Furnberg Park
Harmony Road Neighborhood Park
Heddie Notz Park
Jefferson Street Boat Launch
Lewelling Elementary School Tennis Courts
Mill Park
Minthorn North Natural Area
North Clackamas Aquatic Park
North Clackamas Park
Rivervilla Park
Rowe Middle School Tennis Courts
Sara Hite Rose Garden
Scott Park
Sieben Park
Southern Lites Park
Summerfield Park
The Milwaukie Center
Village Green Park
Benski Park
Bernert Landing Boat Ramp
Burnside Park
Camassia Natural Area
Cedar Island Park
Cedaroak Boat Ramp
Fields Bridge Park
Ibach Nature Park
Maddax Woods
Mark Lane Tot Lot
McLean House
North Willamette Neighborhood Park
Oppenlander Field
Palamino Park
Robinwood Park
Sahallie-Illahee Park
Skate Park
Skyline Ridge Park
Sunburst Park
Sunset Fire Hall (historical)
Tanner Creek Park
Beaver Boat Ramp
Gilbert River Boat Ramp
J J Collins Memorial Park
Laurel Beach County Park
Prescott Beach County Park
Scappoose R V Park
A M Kennedy Park
Adams Acres Park
Allenbach Acres Park
Aloha Swim Center
Alohawood Park
Apollo Ridge Park
Arnold Park
Aspen Crest Park
Autumn Ridge Park
Bales Wetlands Park
Barlow Square Path
Barsotti Park
Bauman Park
Beacon Hill Park
Beaverton Creek Wetlands Park
Beaverton Swim Center
Ben Graf Park
Bethany Crest Park
Bethany Lake Park
Bethany Meadows Park
Bethany Wetlands Park
Bluegrass Downs
Bronson Creek Park
Brookhaven Park
Brookview Park
Buckskin Mini-Park
Burnsridge Park
Burntwood Powerline Park
Burntwood West Park
Burntwood West Upper Park
Burton Park
Butternut Park
C E Mason Wetlands Park
Cain Park
Camp Rivendale
Carolwood Park
Cedar Hills Recreation Center
Cedar Mill Park
Cedar Mill Woods Park
Cedar Park Tennis Courts
Center Street Park
Channing Heights Mini-Park
Chantal Village Park
City Park
College Park
Conestoga Recreation and Aquatic Center
Conestoga Tennis Courts
Cooper Park
Crowell Court Park
Crystal Creek Park
Davids Windsor Park
Deerfield II Park
Deerfield Park
Deline Park
Downing Bike Path
Dwight Parr Park
Eichler Park
Elizabeth Meadows Park
Elsie Stuhr Center
Emerald Estates Park
Fanno Creek Park
Fifth Street Park
Fir Grove Park
Five Oaks Tennis Courts
Florence Pointe Park
Foege Park
Forest Hills Park
Garden Home Recreation Center
George W Otten Park
Granada Park
Griffith Park
Harman Swim Center
Hart Meadows Powerline Park
Hartwood Hylands Park
Hazeldale Park
Hideaway Park
Highland Park Tennis Courts
Hiteon Meadows Park
Hiteon Park
Inger Property
Intel Aloha Wetlands Park
Jackie Husen Park
Jenkins Estate
John Marty Park
Jordan Park
Kaiser Ridge Powerline Park
Kaiser Woods Park
Koll Center Wetlands Park
Lawndale Park
Lexington Park
Lilly K Johnson Park
Little People Park
Lowami Hart Woods Park
Madrona Heights Park
Matrix Hill Park
McMillian Park
Meadow Park Tennis Courts
Meadowbrook Park
Melilah Park
Tualatin Valley Water Dist Athletic Fields
Merrit Orchard Park
Mitchell Park
Moonshadow Park
Mora Park
Morgan's Run Park
Morrison Woods Park
Mountain View Tennis Courts
Murrayhill Powerline Park
Murrayhill Powerline Park
NE Neighborhood Park
NW Park
Northshore Estates Park
Oregon Electric Right of Way Path
Papageorge Park
Paula Jean Powerline Park
Quarry Pond Park
Raleigh Park and Swim Center
Raleigh Scholls Park
Raleighwood Park
Reservoir Park
Ridgecrest Park
Ridgewood View Park
Rock Creek Landing Park
Rock Creek North Soccer Fields
Rock Creek Park
Rock Creek Powerline Park
Rock Creek Powerline Trail
Rock Creek North Soccer Fields
Roger Tilbury Memorial Park
Rosa Park
Roxbury Park
Roxie's Place Park
Roy Dancer Park
Satterberg Heights Park
Westside Linear Park
Evelyn Schiffler Memorial Park
Scott's Place Park
Seminole Park
Stoller Creek Greenway
Sexton Mountain Meadows Park
Sexton Mountain Wetlands Park
Shadow Creek Park
Shaughnessey Woods Park
Skyview Park
Somerset West Swim Center/Park
Springville Meadows Park
Spruce Woods Park
Spyglass Park
Steele Park
Stonegate Park
Stonemist Park
Summercrest Park
Summercrest West Park
Sunset Swim Center/Park
Surry West Path
Sutherland Meadows Park
Taliesen Park
Tallac Terrace Park
Taylor's Creek Park
Terra Linda Park
The Bluffs Park
Thornbrook Park
Tokola Wetlands Park
Traschel Meadows Park
Trenton Woods Path
Tualatin Hills Nature Park
Twin Cedars Park
Vale Park
Valley Park
Valley West Park
Vendla Park
Vista Brook Park
Wake Robin Park
Wanda L. Peck Memorial Park
Schlottman Creek Greenway
Waterhouse Park
Waterhouse Linear Park
West Slope Park
West Sylvan Park
West Union Estates Park
White Fox Park
Wildhorse Mini-Park
Wildwood Mini-Park
Willard Park Path
Willow Creek Nature Park
Willow Park
Wonderland Park
Wooded Ravine Park
Mount Talbert Nature Park
Spring Park Natural Area
Columbia Botanical Gardens
Dalton City Park
Walnut Tree City Park
Locust Street Park
Arneson City Park
13th Avenue City Park
19th Avenue City Park
Eco City Park
Canby Regional Park
Jim Bundy Memorial Park
Datis City Park
Carolyn King Memorial Park
Harvard City Park
Ruth Rose Richardson Park
Aumsville Ponds County Park
Bonesteele County Park
Ora Bolmeier City Park
Spencer City Park
Vernonia Lake City Park
Shay 102 City Park
Airport City Park
Blue Lake Regional Park
Chinook Landing Marine Park
Flagg Island Park
Larch Mountain Corridor
M James Gleason Ramp
Mason Hill Park
Portland Traction Trail
Sauvie Island Boat Ramp
Smith and Bybee Lakes Wildlife Area
Willamette Cove
Central Park
Century Park
Coffee Lake Park
Englewood City Park
Forest Glen Park
Gary Island Park
Indian John Island Park
Killin Wetlands Nature Park
Memorial Park
Northgate City Park
Northridge Park
Rock Creek Trail Park
Sunset City Park
Pine Creek
Lewis and Clark National Historical Park
Gnat Creek Campground
Charles Sprague Memorial Wayside
Jordan Creek OHV Staging Area
Lyda Camp OHV Staging Area
Nehalem Falls Campground
Smith Homestead
Stagecoach Horsecamp
Stones Road Boat Launch
Alva Park
Crest Park
Etna Park
Keller Park
Klein Park
Flagg Island
Armory Park
Babe Nicklous Pool Park
Buckley Park
College Park
Darnell Wright Softball Complex
Dundee Scenic Overlook
Falcon Crest Park
Gladys Park
Memorial Park
Nine Hole Golf Course
Oak Knoll Tot Lot
Rotary Centennial Park
Scott Leavitt Park
Spring Meadow Park
Aldrich Point Boat Ramp
Big Creek County Park
Camp Cullaby
Carnahan County Park
DeLaura Beach
John Day County Park
Lewis and Clark River Boat Ramp
Nehalem County Park
North Fork Nehalem County Park
Smith Lake County Park
Sunset Beach State Park
Sunset Lake Public Park
Westport Boat Ramp
Arago County Park Boat Ramp
Bradley Lake Park Boat Ramp
Charleston Fishing Pier Boat Ramp
Coquille Boat Ramp
Doris Place Boat Ramp
Hauser Dune Tract
6th Street Tenmile Lake Boat Ramp
8th Street Tenmile Lake Boat Ramp
Lakeside Dune Tract
Myrtle Tree Boat Ramp
New River County Park
Riverton Boat Ramp
Rocky Point Boat Ramp
Sandy Creek Covered Bridge
Wallace Dement Park
West La Verne Park
Eagle Ridge County Park
Exchange Park
Wocus Bay Boat Launch
Morrow County OHV Park
Buena Vista County Park
Eola Heights County Park
Nesmith County Park
Ritner Creek Bridge
Ritner Creek County Park
Emil Marx-Lloyd Strange Fishing Hole
Charles Metsker County Park
Juliette County Park
Monroe Landing County Park
Power House County Park
Rogers Landing County Park
Grass Valley City Park
Moro City Park
Rufus Community Center
Wasco City Park
Wasco Depot Park
Al Griffin Memorial Park
Bay City Forest Park
11th Street Park
Courthouse Square Park
Dayton Boat Landing
Legion Field
Memorial Lumbermans Park
Commons Park
Joel Perkins Park
Nehalem City Park
Nehalem H Street Public Dock
Nehalem Harwood Square
Rockaway Beach City Park
Seaview City Park
Stanger Memorial VFW Park
9th Street Park
Carnahan Park
Peace Park
Waterfront Park
Wheeler Upper Park
Birch Street Park
Dallas City Park
East Dallas Community Park
Gala Park
Kingsborough Park
LaCreole Sports Complex
Lyle Sports Complex
Rotary Park
Whitworth Sports Complex
Mountain Fir Park
Pfaff Park
Wild Fawn Park
Cherry Lane Park
Le Mesa Park
Madrona Park
Main Street Park
Marr Court Park
Monmouth Recreational Park
Southgate Park
Whitesell Park
Winegar Park
Sheridan City Park
Lamson Park
Tina Miller Memorial Park
Triangle Park
City Park
Bankus Fountain
Bud Cross Park
Chetco Point Park
Easy Manor Park
Richards Street Park
Stout Park
5th Street Park
Lions Club Park
Sanford Heights Park
Collier H Buffington Memorial Park
Pocket Park
South Beach Park
Lehnherr Park
Lions Memorial Park
Rotary Park
Sunset Park
Charles S Gardiner Park
Commercial Street Park
Micelli Park
Roseburg Skate Park
Stewart Park Wildlife Pond
Sunshine Park
Thompson Park
Willis Park
Conger Heights Park
Conger School Park
Eldorado Park
Ella Redkey Municipal Pool
Fairview Park
Henderson Park
Kiger Stadium
Kit Carson Park
Krause Park
Mills Little League Park
Mills-Kiwanis Park
Pacific Terrace Park
Putnams Point
Richmond Park
Southside Park
Klamath Falls Sports Complex / Skatepark
Stukel Park
Veterans Memorial Park
Warford Park
Triangle City Park
Washington City Park
Hines City Park
Condon City Park
City Park
Hager Park
Heritage Park
Veterans Mini Park
Ione City Park
Spray Riverfront Park
Cottonwood City Park
Lewin City Park
North Marion Primary School
Oregon Historical Society Museum and Research Library
Portland Art Museum
Multnomah County Courthouse
Oregon Museum of Science and Industry
Salt Creek Cabin (historical)
Larkspur Trail
McKay Park
Pacific Park
Pageant Park
Pinewood Park
Pioneer Park
Providence Park
L L Stub Stewart State Park
Railroad Park
Thompson's Mills State Park
Tseriadum State Park
Gary A Ward Park
Harwood Park
Kilowatt Park
Library Park
Mini Park
Mountain View Park
Rimrock Park
Stryker Park
Archie Briggs Canyon Open Space
Awbrey Village Park
Bend Senior Center
Big Sky Park and Sports Complex
Blakely Park
Brandis Square
Brooks Park
Canal Park
Columbia Park
Deschutes River Trail
Dohema Canoe Access
First Street Rapids Park
Foxborough Park
Vince Genna Stadium
Harmon Park
Hillside Park
Hixon Park Block
Hollinshead Park
Juniper Swim and Fitness Center
Kiwanis Park
Riverview Park
Stover Park
Summit Park
Sunset View Park
Sylvan Park
Tillicum Park/Chase Ranch
Woodriver Park I & II
Volunteer Park
Juniper Hill Park
Wheeler County Courthouse Park
Wes Bennett City Park
Bridge Park
George Kitchen Upper Park
Michael Harding Park
Bicentennial Park
King Street Park
Culver City Park
7th Street Park
Bean Park
Community Park
Cowden Park
Friendship Park
Oak Street Park
South Park
Totem Park
Fairhaven City Park
Spudbowl City Park
Valleyview City Park
West Canyon Rim City Park
Centennial Park
Grecian Heights Park
Kiwanis Park
McKay School Park
Pendair Park
River Parkway
Sergeant City Park
Sherwood Park
Vincent Park
Alkali Park
Earl Snell Memorial Park
Athena City Park
Athena Memorial Ball Park
Duggor Park
Fort Henrietta Park Echo
George Park
Oregon Trail Arboretum
Skate Park
City Pocket Park
Tom McDowell Park
Heritage Square
State Lands Ballfields City Park
Restoration Creek
Kraus Creek
McKernan Creek
Scappoose High School
Chinese Massacre Cove
Century High School
Liberty High School
Governor Tom McCall Waterfront Park
Hamilton Creek
Chush Falls
Hudspeth Guard Station
Calsh Trail
Tualatin Valley
Opal Pool
Opal Creek Trail
Three Pools
Jawbone Flats (historical)
North Fork Schooner Creek
Baker Air Force Station (historical)
Burns Air Force Station (historical)
Condon Air Force Station (historical)
Great Basin
Scottie Creek
Paget Creek
Mount Hebo Air Force Station (historical)
Shutter Creek Correctional Institution
Tillamook Naval Air Station (historical)
Tongue Point Naval Air Station (historical)
La Grande Fire Department
10th Street Park
Adams City Park
Airport Heights Park
Ashbrook Park
Bard Park
Bend O River Mini Park
Benton Park
George Birnie Memorial Park
Boardwalk Park
Burlingham Park
Butte Park
California Boat Ramp
Centennial Park
Charles Ames Memorial City Park
Charlotte Rauch Park
Christopher Columbus Park
Anna Classick Bicentennial Park
Cliff Clemens Park
Coe Street Park
College Park
Cowan Park
Dairy Creek Park
Discovery Meadows Community Park
Eastside Boat Ramp
Eastside Park
Empire Boat Ramp
Evans Park
Fleming Memorial Park
Garden Club Park
Gills Landing
Gresham/Fairview Trail
Had Irvine Park
Halsey Memorial Park
Halsey Veterans Memorial Park
Heritage Park
Hermanson Park I
Hermanson Park II
Hermanson Park III
Highland Park
Kingwood Mini Park
La Grande Police Department
Library Park
Locomotive Park
Morgan Lake Park
Nelson Park
North Evans Mini Park
North Front Street Park
Northside Park
Oak Street Park
Ponderosa Park
Ralston Park
River Bend County Park
Riverfront Park
Riverside Park
Senecal Creek Greenway
Senior Estates Park
Springwater Trail
Stanfield Heights Park
State Street Park
Strawberry Hill Park
Sunnyhill Park
Sunset Park
Taylor Park
Taylor/Wasson Park
Theater Sports Park
Thompson Park
Union City Park
Volunteer Park
Wallowa Fire Department
Windy Hill Park
Winsor Park
Woodburn Downtown Plaza
Wyffle Park
Redmond Fire and Rescue Station 403 Airport
Ashland Community Hospital
Ashland Dog Park
Ashland Fire and Rescue Station 1
Ashland Fire and Rescue Station 2
Ashland Police Department
Bluebird Park
Calle Guanajuato
Chapman and Linn Park
Clay Street Park
Dement Park
Garden Way Park
Garfield Park
Glenwood Park
Hald/Strawberry Park
Jon Storm Park
Liberty Street Park
Madrona Open Space
North Mountain Park
Oak Tree Park
Oredson Todd Woods
Railroad Park
Redmond City Hall
Redmond Fire and Rescue Station 401 Headquarters
Redmond Police Department
Scenic Park
Senior Citizen Park
Shenandoah Park
Sherwood Park
Siskiyou Mountain Park
Community Skate Park
Southern Oregon University Nat
Triangle Park
Ashland Creek Park
West Bridge Park
YMCA Park
Corvallis Army Air Field (historical)
Medford Army Air Field (historical)
Portland Army Air Base (historical)
Redmond Army Air Field (historical)
Salem Army Air Field (historical)
Keizer Elementary School
Whale Watching Center
Shoberg Creek
Sweeney Creek
Tex Creek Arch
Salvation Spring
Teakettle Spring
Bridlemile Creek
Hathaway Creek
Ki-a-kuts Bicycle and Pedestrian Bridge
Siletz Reef
Geisel Cemetery
Weston Cemetery
Kitchen Creek
Haines Elementary School
Pine Eagle High School
Lighthouse Christian School
Halfway Elementary School (historical)
Keating Elementary School
Alsea Elementary School
Alsea High School
Ashbrook Independent School
Clemens Primary School
Corvallis High School
Corvallis Montessori School
Monroe Grade School
Monroe High School
Nazarene Christian School (historical)
Philomath Elementary School
Philomath High School
Philomath Middle School
McDaniel Creek
Lakewood Theatre Company
Athey Creek Middle School
Molalla Elementary School
Clackamas Elementary School
Cedar Ridge Middle School
Rural Dell Elementary School
Trost Elementary School
Canby High School
Clackamas River Elementary School
Estacada Junior High School
Boones Ferry Primary School
Inza R Wood Middle School
Wilsonville High School
Boeckman Creek Primary School
Welches Elementary School
New Urban High School
Clackamas High School East Campus
Sojourner School
Kelso Elementary School
Gladstone High School
Westridge Elementary School
Hallinan Elementary School
Deep Creek Elementary School
Milwaukie High School
Oregon Trail Elementary School
Oak Creek Elementary School
Bolton Primary School
Rosemont Ridge Middle School
Exploration Learning School
Rowe Middle School
Mount Scott Elementary School
Spring Mountain Elementary School
Naas Elementary School
Oak Grove Elementary
Firwood Elementary School
Holcomb Elementary School
Arts and Technology Charter High School
Pacific Northwest Academy
North Clackamas Christian School
Arbor School of Arts and Sciences
Baker Prairie Middle School
Cascade Heights Public Charter School
Columbia Academy
Country Christian School
Damascus Christian School
Good Shepherd School
Grace Christian School
Heron Creek Academy
McLoughlin Middle School (historical)
Portland Waldorf High School
Stafford Academy
Three Rivers Charter School
Touchstone Elementary School
Westside Christian High School
Mount Hood Academy
Clackamas High School West Camous
Hilda Lahti Elementary School
South Jetty High School
Saint Mary Star of the Sea School
Clackamas Census Designated Place
Cloverdale Census Designated Place
Aloha Census Designated Place
Altamont Census Designated Place
Barview Census Designated Place
Beaver Census Designated Place
Biggs Junction Census Designated Place
Brooks Census Designated Place
Bunker Hill Census Designated Place
Butteville Census Designated Place
Cape Meares Census Designated Place
Cayuse Census Designated Place
Cedar Hills Census Designated Place
Cedar Mill Census Designated Place
Chenoweth Census Designated Place
Eola Census Designated Place
Marion Census Designated Place
Four Corners Census Designated Place
Fruitdale Census Designated Place
Garden Home-Whitford Census Designated Place
Glide Census Designated Place
Gopher Flats Census Designated Place
Grand Ronde Census Designated Place
Green Census Designated Place
Harbeck-Fruitdale Census Designated Place (historical)
Harbor Census Designated Place
Hayesville Census Designated Place
Hebo Census Designated Place
Jennings Lodge Census Designated Place
Kirkpatrick Census Designated Place
Labish Village Census Designated Place
Lincoln Beach Census Designated Place
Deschutes River Woods Census Designated Place
South Lebanon Census Designated Place
Mehama Census Designated Place
Metzger Census Designated Place
Mission Census Designated Place
Mount Hood Villages Census Designated Place
Neskowin Census Designated Place
Netarts Census Designated Place
Oak Grove Census Designated Place
Oak Hills Census Designated Place
Oatfield Census Designated Place
Oceanside Census Designated Place
Odell Census Designated Place
Pacific City Census Designated Place
Parkdale Census Designated Place
Pine Grove Census Designated Place
Pine Hollow Census Designated Place
Raleigh Hills Census Designated Place
Redwood Census Designated Place
Rickreall Census Designated Place
Riverside Census Designated Place
Rockcreek Census Designated Place
Rose Lodge Census Designated Place
Roseburg North Census Designated Place
Rowena Census Designated Place
Three Rivers Census Designated Place
Tri-City Census Designated Place
Tutuilla Census Designated Place
Tygh Valley Census Designated Place
City of Cascade Locks
City of Cave Junction
City of Central Point
City of Chiloquin
City of Clatskanie
City of Coburg
Wamic Census Designated Place
Warm Springs Census Designated Place
West Haven-Sylvan Census Designated Place
West Slope Census Designated Place
White City Census Designated Place
Winchester Bay Census Designated Place
City of Adair Village
City of Adams
City of Adrian
City of Albany
City of Amity
City of Antelope
City of Arlington
City of Ashland
City of Astoria
City of Athena
City of Aumsville
City of Aurora
City of Baker City
City of Bandon
City of Banks
City of Barlow
City of Bay City
City of Beaverton
City of Bend
City of Boardman
City of Brookings
City of Brownsville
City of Burns
City of Canby
City of Cannon Beach
City of Canyonville
City of Carlton
Sunnyside Census Designated Place
Terrebonne Census Designated Place
City of Idanha
City of Imbler
City of Independence
City of Ione
City of Irrigon
City of Island City
City of Jacksonville
City of Jefferson
City of John Day
City of Johnson City
City of Jordan Valley
City of Joseph
City of Junction City
City of Keizer
City of Columbia City
City of Condon
City of Coos Bay
City of Coquille
City of Cornelius
City of Corvallis
City of Cottage Grove
City of Cove
City of Creswell
City of Culver
City of Dallas
City of Damascus
City of Dayton
City of Depoe Bay
City of Detroit
City of Donald
City of Drain
City of Dufur
City of Dundee
City of Dunes City
City of Durham
City of Eagle Point
City of Echo
City of Elgin
City of Elkton
City of Enterprise
City of Estacada
City of Eugene
City of Fairview
City of Falls City
City of Florence
City of Forest Grove
City of Fossil
City of Garibaldi
City of Gaston
City of Gates
City of Gearhart
City of Gervais
City of Gladstone
City of Glendale
City of Gold Beach
City of Gold Hill
City of Granite
City of Grants Pass
City of Grass Valley
City of Greenhorn
City of Gresham
City of Haines
City of Halfway
City of Halsey
City of Happy Valley
City of Harrisburg
City of Helix
City of Heppner
City of Hermiston
City of Hillsboro
City of Hines
City of Hood River
City of Hubbard
City of Huntington
City of Lebanon
City of Lincoln City
City of Lonerock
City of Long Creek
City of Lostine
City of Lowell
City of Lyons
City of Madras
City of Malin
City of Reedsport
City of Richland
City of Riddle
City of Rivergrove
City of Rockaway Beach
City of Rogue River
City of Roseburg
City of Rufus
City of Manzanita
City of Maupin
City of Maywood Park
City of McMinnville
City of Medford
City of Merrill
City of Metolius
City of Mill City
City of Millersburg
City of Milton-Freewater
City of Milwaukie
City of Mitchell
City of Molalla
City of Monmouth
City of Monroe
City of Monument
City of Moro
City of Mosier
City of Mount Angel
City of Mount Vernon
City of Myrtle Creek
City of Myrtle Point
City of Nehalem
City of Newberg
City of Newport
City of North Bend
City of North Plains
City of North Powder
City of Nyssa
City of Oakland
City of Oakridge
City of Ontario
City of Oregon City
City of Paisley
City of Pendleton
City of Philomath
City of Phoenix
City of Pilot Rock
City of Port Orford
City of Portland
City of Powers
City of Prairie City
City of Prescott
City of Prineville
City of Rainier
City of Redmond
City of King City
City of Klamath Falls
City of La Grande
City of La Pine
City of Lafayette
City of Lake Oswego
City of Lakeside
Town of Bonanza
Town of Butte Falls
City of Saint Helens
City of Saint Paul
City of Salem
City of Sandy
City of Scappoose
City of Scio
City of Scotts Mills
City of Seaside
City of Seneca
City of Shady Cove
City of Shaniko
City of Sheridan
City of Sherwood
City of Siletz
City of Silverton
City of Sisters
City of Sodaville
City of Springfield
City of Stanfield
City of Stayton
City of Sublimity
City of Sumpter
City of Sutherlin
City of Sweet Home
City of Talent
City of Tangent
City of The Dalles
City of Tigard
City of Tillamook
City of Toledo
City of Troutdale
City of Tualatin
City of Turner
City of Ukiah
City of Umatilla
City of Union
City of Unity
City of Vale
City of Veneta
City of Vernonia
City of Waldport
City of Wallowa
City of Warrenton
City of Wasco
City of West Linn
City of Westfir
City of Weston
City of Wheeler
City of Willamina
City of Wilsonville
City of Winston
City of Wood Village
City of Woodburn
City of Yachats
City of Yamhill
City of Yoncalla
Town of Dayville
Town of Lakeview
Town of Lexington
Town of Canyon City
Town of Spray
Town of Summerville
Town of Waterloo
Gopher Flats
Kirkpatrick
Oatfield
Riverside
Hudson Park Elementary School
Rainier Junior - Senior High School
McBride Elementary School
Vernonia Middle School
Vernonia High School
Mist Elementary School
North Columbia Academy
Saint Helens Arthur Academy
Bandon Senior High School
Harbor Lights Middle School
Christ Lutheran School
Coquille High School
Crusader High School
Gold Coast Seventh - Day Adventist Christian School
Highland Elementary School
Kingsview Christian School
North Bay Elementary School
Myrtle Point High School
North Bend Middle School
North Bend Senior High School
Oregon Coast Technology School
Powers Elementary School
Powers High School
Reedsport Community Charter School
United Valley Christian Academy
Cecil Sly Elementary School
Crook County High School
Mount Bachelor Academy
Paulina Elementary School
Powell Butte Community Charter School
Pioneer Secondary Alternative High School
Agness Elementary School
Azalea Middle School
Brookings - Harbor High School
Kalmiopsis Elementary School
Blanco School
Brookings Harbor Christian School
Driftwood Elementary School
Gold Beach High School
Riley Creek Elementary School
Bend Senior High School
Bridges Academy
Saint Francis of Assisi School
Redmond High School Hartman Campus
Evergreen Elementary School
La Pine Senior High School
La Pine Middle School
Lava Ridge Elementary School
Sky View Middle School
Sisters Elementary School
Sisters Middle School
Sisters High School
Summit High School
Pine Ridge Elementary
Elk Meadow Elementary School
High Lakes Elementary School
Cascade Middle School
Deschutes Edge Charter School
Vern Patrick Elementary School
Three Rivers Elementary School
Ensworth Elementary School
High Desert Middle School
Cascades Academy of Central Oregon
Central Christian School
Elton Gregory Middle School
Waldorf School of Bend
Seven Peaks School
Sisters Charter Academy of Fine Arts
Sisters Christian Academy
Saint Thomas Academy
Tom McCall Elementary School
Trinity Lutheran School
Blue Mountain Alternative High School
Dayville School
Long Creek School
Monument School
Mount Vernon Middle School
Seneca Elementary School
Valley View Seventh Day Adventist Christian School (historical)
Henry L Slater Elementary School
Drewsey Elementary School
Fields Elementary School
Frenchglen Elementary School
Hines Middle School
Suntex Elementary School
Oakland High School
Brockway Elementary School
Canyonville Christian Academy
Canyonville School
Coffenberry Middle School
Days Creek Charter School
Elkton Grade School
Elkton High School
Fullerton Elementary School
Glendale Elementary School
Lookingglass Elementary School
McGovern Elementary School
Winston Middle School
North Douglas Elementary School
Reedsport Junior/High School
Riddle Elementary School
Riddle High School
South Umpqua High School
South County Christian School
Tri City Elementary School
Tiller Elementary School
Toketee Falls Elementary School
Umpqua Valley Christian School
Winchester Elementary School
Yoncalla Elementary School
Yoncalla High School
Parkdale Elementary School
Mid - Columbia Adventist Christian School
Wyeast Middle School
"Coos, Lower Umpqua, and Siuslaw Reservation"
Coquille Reservation
Cow Creek Reservation
Grand Ronde Community
Klamath Reservation
Celilo Village
Winema Creek
Cascade Locks Treaty Fishing Access Site
Celilo Treaty Fishing Access Site
Faler Road Treaty Fishing Access Site
Le Page Treaty Fishing Access Site
Lone Pine Treaty Fishing Access Site
Preachers Eddy Treaty Fishing Access Site
Rufus Treaty Fishing Access Site
Stanley Rock Treaty Fishing Access Site
Threemile Canyon Treaty Fishing Access Site
Academy of Alternatives
Albina Youth Opportunity School
Alpha High School
American Heritage Schools Incorporated
Apostolic Christian Academy
Arthur Academy
Belmont Academy
Butler Creek Elementary School
Celebration Academy of Performing Arts (historical)
Class Academy
Clear Creek Middle School
Corbett Grade School
Eastside Christian School
Emerson School
Faithful Savior Community School
Forest Park Elementary School
Four Corners School
French American International School
Gordon Russell Middle School
Grace Lutheran School
Hall Elementary School
Hartley Elementary School
Hilltop Christian School
Hogan Cedars Elementary School
Hollyrood Elementary School
Islamic School of Portland
Kelly Creek Elementary School
Lents Education Center
Mount Scott Park Center for Learning High
Neveh Shalom Foundation School
New Day Ananda Marga School
New Life School
Open Meadow High School
Open Middle School
Pacific Crest Community School
Portland Friends School
Portland International Community School
Portland Jewish Academy
Portland Opportunities Industrial Center
Reynolds Arthur Academy
Reynolds Learning Academy
Ron Russell Middle School
Rosa Parks Elementary School
Rosemont School
Saint Marys Academy
Saint Pius X School
Salish Ponds Elementary School
Self Enhancement Incorporated Academy
Springwater Trail High School
Success Academy
Sunshine School
The International School
The Northwest Academy
Trillium Charter School
Walt Morey Middle School
Woodland Elementary School
Upper Kentucky Falls
Lower Kentucky Falls
Beavercreek Baptist Church
Sonshine Christian Center
Lower Highland Bible Church and Sunday School
Unbroken Fellowship Church
Grand View Baptist Church
Good Shepherd Community Church
Living Word Fellowship
Sandy Baptist Church
Orient Drive Baptist Church
Saint Patrick Catholic Church
Canby Hispanic Foursquare Church
Calvary Baptist Church
Spiritual Assembly of the Bahais of Clackamas County South
Canby Alliance Church
Canby Christian Church
Bethany Evangelical Free Church
Canby Evangelical Church
Southgate Chapel
Canby Foursquare Church
Canby United Methodist Church
Zoar Lutheran Church
Canby Seventh Day Adventist Church
Church of Jesus Christ of Latter Day Saints Canby
Smyrna United Church of Christ
Macksburg Lutheran Church
Spring Mountain Bible Church
Creator Lutheran Church
Sunnyside Foursquare Church
Valley View Evangelical Church
Clackamas Bible Church
Eastridge Covenant Church
Christian Life Church Incorporated
Christ the Vine Lutheran Church
Carver Community Church
Emmanuel Community Church
Hillside Christian Fellowship
Seventh Day Adventist Churches Oregon Headquarters
Destiny Christian Fellowship
Colton Evangelical Lutheran Church
Colton Community Church
Aspen Meadow Church
Hillsview Community Church
Sunnyside Community Church
Saint Paul of Damascus Lutheran Church
Damascus Assembly of God
The Voice of the Trumpet Ministries
Hollyview Baptist Church
Damascus Community Church
Eagle Creek Presbyterian Church
Eagle Creek Foursquare Church
Dover Community Church
Church of Jesus Christ of Latter Day Saints
Estacada First Baptist Church
Estacada Seventh - day Adventist Church
Saint Aloysius Catholic Church
Estacada Assembly of God Church
Estacada Christian Church
Dodge Community Church
Estacada Bible Fellowship
Garfield Community Church
Clackamas Valley Baptist Church
Estacada United Methodist Church
George Community Church
Gladstone Christian Church
Universal Faith Church
Tri City Baptist Temple of Milwaukie
Gladstone Assembly of God Church
First Baptist Church of Gladstone
Saint Stephen Lutheran Church
Gladstone Park Seventh Day Adventist Church
Sunnyside Church of the Nazarene
New Hope Community Church Incorporated
Pleasant Valley Seventh Day Adventist Church
Town Center Baptist Church
Abundant Life Christian Church
Happy Valley Evangelical Church
Living Streams Church of Christ
Unity World Healing Center
Our Lady of the Lake Church
Lake Oswego United Church of Christ
Church of Jesus Christ of Latter-Day Saints the Portland Oregon Temple
Lake Oswego Christian Center
Our Saviors Lutheran Church
Christian City Church
Lake Bible Church
Lake Baptist Church
Convent of the Holy Names
Christ Church Episcopal Parish
River West Church
Youngnak Presbyterian Church
Lake Oswego United Methodist Church
Lake Oswego First Church
Church of Jesus Christ of Latter Day Saints Family History Center
Lake Grove Presbyterian Church
Whole Life Church
Mountain Park Church
Triumphant King Lutheran Church
Church of Jesus Christ of Latter Day Saints
Hope Community Church
Christ the King Catholic Church
Saint John the Baptist Catholic Church
Harmony Evangelical Church
Wichita Avenue Evangelical Church
Milwaukie Covenant Church
Clackamas Christian Center
Eastern Orthodox Church of the Annunciation
Life Christian Center
North Clackamas Church of Christ
Eagles Wings Prophetic Training Center
Open Bible Community Church
Milwaukie Lutheran Church
Ryder Ministries
Bridge City Community Church
Milwaukie Presbyterian Church
Faith Evangelical Church Milwaukie
King of Kings Evangelical Lutheran Church in American
Westwood Community Fellowship
Amazing Grace Lutheran Church
Milwaukie Foursquare Church
Gladstone Church of the Nazarene
Calvary Chapel Southeast Portland
Oak Grove Church
Saint John the Evangelist Episcopal Church
Church of Jesus Christ of Latter Day Saints
Foothills Community Church
Molalla Christian Church
The Country Christian Church
Saint James Catholic Church
The Evangelical Community Chapel at Liberal
Molalla Church of the Nazarene
Molalla United Methodist Church
New Beginnings Foursquare Church
Assembly of God
Meadowbrook Community Church
Mulino Grace Community Church
Christ Light Community Church
Clarkes United Methodist Church
New Martyrs of Russia Orthodox Church
Church of Jesus Christ of Latter Day Saints
Church of Jesus Christ of Latter Day Saints
Saint John the Apostle Catholic Church
Oregon City Foursquare Church
Oregon City South Foursquare Church
River of Life Christian Center
Oregon City Baptist Church
Park Place Evangelical Church
Victorious Faith Family Church
First Baptist Church of Oregon City
Marantha Baptist Church
Atkinson Memorial Congregational Church
Christ Church Apostolic Incorporated
Oregon City Evangelical Church
Trinity Lutheran Church
Prince of Life Lutheran Church
Faith Fellowship Ministries
Evergreen Community Church
Viola Ridge Christian Center
Follower of Christ Church
Saint Pauls Episcopal Church
Oregon Trail Free Will Baptist Church
First Evangelical Presbyterian Church
Followers of Christ Church
Reformation Covenant Church
Church of the Nazarene
Zion Lutheran Church
Oregon City Church of Christ
Oregon City United Methodist Church
United Pentecostal Church
Stone Creek Christian Church
Light On The Hill Fellowship
Saint Philip Benizi Catholic Church
Calvary Chapel Oregon City
Oregon City Bible Chapel
Immanuel Lutheran Church
Community Worship Church
Gospel of Our Savior Community Chapel
Sandy Foursquare Church
Saint Michael the Archangel
Church of Jesus Christ of Latter Day Saints
Beit Haverim
Willamette United Methodist Church
Willamette United Methodist Church
Willamette Christian Church
SouthLake Foursquare Church
Tacklebuster Reef
Taowhywee Point
South Park Unitarian Universalist Fellowship
Saint Francis Episcopal Church
Hope Fellowship Church
Creekside Bible Church
Grace Chapel
Celebration Church
Saint Cyril Catholic Church
Meridian United Church of Christ
Valley Christian Church
Canyon Creek Church
Church of Jesus Christ of Latter Day Saints
Community of Hope Lutheran Church
Church of Jesus Christ of Latter Day Saints
Solid Rock Baptist Church
Beautiful Savior Lutheran Church
Romanian Baptist Church
Christ Church of Co-Creation
Milwaukee First Baptist Church
Kairos Milwaukie Church Christ
Saint Pauls United Methodist Church
Milwaukie Christian Church
Church of Jesus Christ of Latter Day Saints
Thompson Road Bible Fellowship
Lidgerwood Evangelical Church
Christs Church of Marylhurst Oregon
Marquam United Methodist Church
Madrone Trail Public Charter School
Sacred Heart Catholic School
Rogue River Elementary School - East Campus
Talent Elementary School
Abraham Lincoln Elementary
Ashland High School
Ashland Middle School
Bellview Elementary School
Central Point Elementary School
Butte Falls Secondary School
Butte Falls Elementary School
Crater High School
Cascade Christian High School
River's Edge Academy Charter School
Eagle Point High School
Eagle Point Middle School
Eagle Rock Elementary School
Grace Christian School
Hedrick Middle School
Helman Elementary School
Hoover Elementary School
Jacksonville Elementary School
Jewett Elementary School
Richardson Elementary School
Sams Valley Elementary School
Scenic Middle School
Saint John Lutheran School
Kennedy Elementary School
McLoughlin Middle School
Central Medford High School
North Medford High School
Orchard Hill Elementary School
Walker Elementary School
Saint Mary's School of Medford
Wilson Elementary School
Phoenix Elementary School
Phoenix High School
Prospect School
Shady Cove School
Mountain View Elementary
Table Rock Elementary
Culver High School
Culver Elementary School
Culver Middle School
Jefferson County Middle School
Metolius Elementary School
Allen Dale Elementary School
Applegate Elementary School
Brighton Academy
Evergreen Elementary School
Fleming Middle School
Manzanita Elementary School
Grants Pass High School
Highland Elementary School
North Middle School
Illinois Valley High School
Lincoln Elementary School
Lorna Byrne Middle School
Madrona Elementary School
Newbridge High School
North Valley High School
Parkside Elementary School
Vineyard Christian School
Sandy Glacier Headwall
Kissack/Reynolds Airport
Bonanza Elementary School
Bonanza Junior Senior High School
Brixner Junior High School
Henley Elementary School
Hilltop Christian Academy
Keno Elementary School
Malin Elementary School
Merrill Elementary School
The Triad School
Daly Middle School
Lakeview Senior High School
North Lake School
Paisley School
Academy for Character Education
Academy of Arts and Academics
Agnes Stewart Middle School
Springfield Middle School (historical)
Springfield High School
Charlemagne at Fox Hollow French Immersion Elementary School
Junction City High School
Cottage Grove High School
Countryside Seventh Day Adventist School
Creative Minds Alternative School
Crow Middle - High School
Emerald Christian Academy
Eugene Christian School
Gateways High School
Kalapuya High School
Lane Community College at Cottage Grove
Lane Community College Downtown Center
Siuslaw Middle School
Laurelwood Academy
Lifegate Christian Middle and High School
Lowell High School
Lundy Elementary School
Marist High School
Meadow View School
Mohawk Elementary School
Network Charter School
Oakridge Elementary School
Oakridge High School
Ocean Dunes High School
Pleasant Hill High School
Pleasant Hill Middle School
Prairie Mountain School
Riverbend Elementary School
Siuslaw Elementary School
Saint Thomas Becket Academy
Trent Elementary School
Veneta Elementary School
Wellspring Friends School
Mapleton Elementary School
Mapleton Middle and High School
Toledo Elementary School
Nature Discovery School (historical)
Carolyn Brown School
Crestview Heights School
Isaac Newton Magnet School
Lincoln City Career Technical High School
Lincoln City Seventh - Day Adventist School
Newport High School
Olalla Center for Children and Families
Siletz Valley School
Waldport High School
Albany Christian School
North Albany Elementary School
North Albany Middle School
Takena Elementary School
Liberty Elementary School
Albany Learning Center Community Service
Fairview Christian School
Good Shepherd Lutheran School
Mid Valley Learning Center
Riverside High School
Crawfordsville Elementary School
Gates Elementary School
Harrisburg Elementary School
Harrisburg Middle School
Harrisburg High School
Lacomb School
Pioneer School
Riverview Elementary School
Sand Ridge Charter School
East Linn Christian Academy
Mill City Elementary School
Sanitam Junior - Senior High School
Scio Middle School
Scio High School
Oregon Connections Academy
Holley Elementary School
Sweet Home Charter School
Alameda Elementary School
Huntington School
Jordan Valley Elementary School
Jordan Valley High School
Saint Peter Catholic School
Treasure Valley Christian School
Berean Baptist Church
Beth Israel Jewish Synagogue
Bethany Bible Church
Bethany Lutheran Church
Bethel African Methodist Episcopal Church
Bethel Baptist Church
Bethel Bible Fellowship Church
Bethel Congregational United Church of Christ
Bethel German Assembly of God Church
Bethel Lutheran Church
Bethesda Christian Church
Bethlehem Church
Bethlehem Lutheran Church
Bethlehem Lutheran Church
Bible Doctrine Church of Portland
Blessed Temple Community Church of God in Christ
Boones Ferry Community Church
Bridgeport United Church of Christ
Brookwood Baptist Church
Burlingame Baptist Church
Calvary Baptist Church
Calvary Bible Church
Calvary Chapel Metro
Calvary Chapel of Portland
Calvary Chapel Worship Center
Calvary Church of Tigard
Calvary Gresham Church
Calvary Korean Presbyterian Church
Calvary Lutheran Church
Calvary Presbyterian Church
Calvin Presbyterian Church
Cambodian Buddhist Society of Oregon
Canby Chapel Church of the Nazerene
Cantores in Ecclesia
Capitol Hill United Methodist Church
Cascade Community Church
Cedar Hills Baptist Church
Cedar Mill Bible Church
Celebration Christian Church
Celebration Tabernacle
Central Bible Church
Central Church of Christ
Central Church of the Nazarene
Central Lutheran Church
Champions Church
Cherry Park United Methodist Church
Child Evangelism Fellowship of Greater Portland
Chinese Baptist Church
Chinese Christian and Missionary Alliance Church
Chinese Faith Baptist Church
Chinese Free Methodist Church of Portland
Chinese Grace Baptist Church
Chinese Presbyterian Church
Christ Apostolic Church
Christ Community Church
Christ Community Church
Christ Community Church
Christ Episcopal Church
Christ Light Unity Church
Christ the Healer United Church of Christ
Christ the King Lutheran Church
Christ United Methodist Church of Cedar Mill
Christian Deaf Church
Christian Meeting Place
Christian Missionary Alliance
Church in Portland
Church of Christ
Church of Christ of Albina
Church of Christ of Eastside
Church of Christ of Gladstone
Church of Christ of Linwood Avenue
Church of Christ of Peninsula
Church of Christ of Piedmont
Church of God of Prophecy
Church of God of Rockwood
Church of God Seventh Day
Church of Korean Martyrs
Church of Saint Michael the Archangel
Church of Scientology of Portland
Church of the Good Shepherd
Church of the Living God
Church of the Nazarene
Church of the Nazarene of Hillsboro
Clackamas Christian Center
Clackamas United Congregational Church of Christ
Clear Creek Community Church
Colonial Heights Presbyterian Church
Columbia Community Bible Church
Columbia View Wesleyan Church
Community Church of God
Community Covenant Church
Congregation Beth Israel
Congregation Chabad
Cooper Mountain Presbyterian Church
Cornerstone Church
Cornerstone Community Church
Countryside Community Church
Covenant Presbyterian Church
Crossroads Christian Center
Crossroads Church of Christ
Daniels Memorial Church of God in Christ
Downtown Chapel of Saint Vincent de Paul Parish Church
Eagles Wings Ministries
East County Church of Christ
Eastgate Bible Chapel
Eastminster Presbyterian Church
Eastrose Fellowship Unitarian Universalist Church
Eastside Free Methodist Church
Eckankar Religion of the Light of God Portland Chapter
Eden Bible Church
Eden Presbyterian Church
Eighth Church of Christ Scientist
Eleventh Church of Christ Scientist
Emmanuel Church of God in Christ United
Emmanuel Presbyterian Church
Emmanuel Temple Full Gospel Pentecostal Church
Englewood Christian Church
Evangelical Baptist Church
Evergreen Presbyterian Church
Faith and Life Center Free Methodist Church
Faith Chapel Assembly of God Church
Faith Lutheran Church
Faith Pentecostal Tabernacle
Faith Tabernacle Church of Portland
Fellowship Missionary Baptist Church
Fifth Street Church of Christ
First Baptist Church of Aloha
First Baptist Church of Beaverton
First Baptist Church of Canby
First Baptist Church of Gresham
First Christian Church
First Church of Christ Scientist
First Church of Christ Scientist
First Church of Christ Scientist
First Church of God
First Church of the Nazarene
First Congregational Church
First Covenant Church
First Immanuel Lutheran Church
First Love Ministries
First Pentecostal Church of God
First Presbyterian Church
First Samoan Church Assembly of God
First United Methodist Church
First United Methodist Church of Beaverton
Flavel Street Baptist Church
Foursquare Gospel Church
Franciscan Spiritual Center of the West
Freedom Foursquare Church
Fremont United Methodist Church
Fresh Faith Church
Friendship Christian Fellowship Church
Full Circle Temple Church
Full Gospel Temple of Prayer Church
Gateway Baptist Church
Gethsemane Church of God in Christ
Gethsemane Evangelical Lutheran Church
Gladstone First Baptist Church
Gladstone Spanish Seventh Day Adventist Church
Glencullen Baptist Church
Glenfair Evangelical Church of North America
Glisan Street Baptist Church
Golden Road Baptist Church
Good Shepherd Lutheran Church
Gospel Outreach of Portland
Grace and Truth Pentecostal Church
Grace Baptist Church
Grace Bible Church
Grace Bible Fellowship Church
Grace Christian Fellowship Church
Grace Community Church
Grace Community Church
Grace Covenant Fellowship Church
Fremont Bridge
Albinia-Mississippi Max Station
Alder Street Child Development Center
American Advertising Museum
Apostolic Faith Church International Headquarters
Aquarian Foundation
Arlene Schnitzer Concert Hall
TriMet Barbur Boulevard Transit Center
Beaverton Central Max Station
Beaverton Creek Max Station
TriMet Beaverton Transit Center
Blitz-Weinhard Brewery (historical)
Cascades Max Station
Cedar Mill Community Library
Church and Synagogue Library Association
Clackamas County Library
Clackamas Town Center Transit Center
Cleveland Avenue Max Station
Community Health Research Library
Convention Center Max Station
Delta Park / Vanport Park and Ride
Elmonica Max Station
Expo Center Max Station
Fair Complex / Hillsboro Airport Park and Ride
United States Customs and Border Protection Portland Deferred Inspection Site
Federal Courthouse
Fountain Plaza
Friends of the Multnomah County Library
Galleria Max Station
Garden Home Community Library
Gateway / Northeast 99th Avenue Transit Center
Goose Hollow Max Station
Green Wyatt Federal Building
Gresham Max Station
Gresham Central Transit Center
Hatfield-Government Center Station
Hawthorn Farm Max Station
Hillsboro Central Transit Center
Unitus Plaza
Hollywood / Northeast 42nd Avenue Transit Center
Interstate-Rose Garden Max Station
Jackson Tower
Justice Center
Keller Auditorium
Kenton-North Denver Avenue Max Station
Kids of the Kingdom Christian Child Care Center
Kindercorner Indoor Play Park
Kings Hill Max Station
Koin Center
Lake Oswego Transit Center
Ledding Library of Milwaukie
Library and Ninth Avenue Max Station
Lloyd Center
Lloyd Center Max Station
Masonic Temple
Max Parkrose-Sumner Station
Merlo Road Max Station
Midland Regional Library
Millikan Way Max Station
Milwaukie Center
Milwaukie Transit Center
Mount Hood Avenue Max Station
National College of Naturopathic Medicine Library
North Killingsworth Station Max Station
North Lombard Transit Center
North Portland Boulevard Max Station
North Prescott Street Max Station
Old Town-Chinatown Max Station
Oregon City Transit Center
Oregon Convention Center
Oregon Department of Transportation
Oregon History Center
Oregon Maritime Center and Museum
Oregon Sports Hall of Fame
Oregon State Building
The Oregonian Building
Orenco Max Station
Overlook Park Max Station
PGE Park Max Station
Pioneer Courthouse
Pioneer Place
Pioneer Square Max Station North
Pioneer Square Max Station South
Polish Library Association Hall
Portland Building
Portland Central Library
Portland Chamber of Commerce
Portland City Hall
Portland Fire and Rescue Station 1 Old Town
Portland Fire and Rescue Station 10 Burlingame
Portland Fire and Rescue Station 11 Lents
Portland Fire and Rescue Station 12 Sandy Boulevard
Portland Fire and Rescue Station 14 Alberta Park
Portland Fire and Rescue Station 18 Multnomah Village
Portland Fire and Rescue Station 19 - Mount Tabor
Portland Fire and Rescue Station 23 Lower Eastside (historical)
Portland Fire and Rescue Station 25 Woodstock
Portland Fire and Rescue Station 26 Portsmouth - University Park
Portland Fire and Rescue Station 27 Forest Heights
Portland Fire and Rescue Station 28 Rose City - Hollywood
Portland Fire and Rescue Station 29 Powellhurst
Portland Fire and Rescue Station 3 Northwest Pearl District
Portland Fire and Rescue Station 4 Portland State University
Portland Fire and Rescue Station 5 Hillsdale
Portland Fire and Rescue Station 6 Northwest Industrial
Portland Fire and Rescue Station 7 Mill Park
Portland Fire and Rescue Station 8 Kenton
Portland Fire and Rescue Station 9 Hawthorne District
Portland International Max Station
Portland Center for the Performing Arts
Portland Plaza
Quatama Max Station
Rockwood / East 188th Avenue Transit Center
Rose Quarter Center and Max Station
Ruby Junction Max Station
Skidmore Fountain Max Station
TriMet Sunset Transit Center
The Genealogical Forum of Oregon Library
The Ray Atkeson Photo Library
The Rose Garden Arena
Theosophical Society in Portland
TriMet Tigard Transit Center
Tuality Hospital Max Station
West Slope Community Library
Washington Max Station
TriMet Washington Square Transit Center
Willow Creek Max Station
World Trade Center
Yamhill District Max Station
Yamhill Market Place Shopping Center
YMCA
YWCA
Abernethy Center
Abundant Life Church
Agape Bible Church
Agape Wide World Mission Center
Ahmadiyya Movement in Islam
Ainsworth United Church of Christ
Albina Church of God
All Saints Church
All Saints Episcopal Church
Allen Temple Christian Methodist Episcopal Church
Alliance Bible Church
Aloha Bible Church
Aloha Christian Church
Aloha Church of God
Aloha United Methodist Church
Ammanuel Evangelical Church
Apostolic Lutheran Church
Apostolic Worship Center
Arabic Christain Church
Ark of Safety Church of God in Christ
Ascension Catholic Church
Ascension Lutheran Church
Assembly of God Church
Assembly of God Church of Gladstone
Augustana Lutheran Church
Baps Hindu Temple
Beaverton Christian Church
Beaverton Church of the Nazarene
Beaverton Foursquare Church
Beaverton Grace Bible Church
Bennett Chapel United Methodist Church
Kingdom Hall of Jehovahs Witnesses
Kingdom Hall of Jehovahs Witnesses
Kingdom Hall of Jehovahs Witnesses
Kingdom Hall of Jehovahs Witnesses
Kingdom Hall of Jehovahs Witnesses
Kingdom Hall of Jehovahs Witnesses
Kingdom Hall of Jehovahs Witnesses
Korean Bethel Presbyterian Church
Korean Evangelical Church of Portland
Korean First Southern Baptist Church
Korean Mission Church of Oregon
Korean Oriental Mission Church of Oregon
Lake Family Fellowship Church
Lake Oswego Family History Center
Lake Oswego First Church of Christ Scientist Reading Room
Laurelwood United Methodist Church
Lents Baptist Church
Lents Gilbert Church of God
Liberty Baptist Church
Life Church
Life Fellowship Church
Lifegate Baptist Church
Lifeline Christian Church
Light of Life Lutheran Church
Lighthouse Community Church
Lighthouse Mission Church
Lincoln Street Baptist Church
Lincoln Street Methodist Church
Living Enrichment Center
Living Hope Fellowship Church
Living Savior Lutheran Church
Living Water Community Fellowship Church
Living Waters Worship Center
Livinghope Baptist Church
Love Temple Church of God in Christ
Luis Palau Association
Luther Memorial Church
Lynchwood Christian Church
Lynchwood Church of God
Lynwood Friends Church
Madeleine Church
Maranatha Baptist Church
Maranatha Church of God
Meadow Springs Church
Mennonite Church of Portland
Messiah Finnish Lutheran Church
Metro Church of Christ
Metro District United Methodist Church
Metropolitan Community Church of Portland
Metropolitan Vineyard Christian Fellowship
Metzger Park Hall
Midway Christian Church
Mill Park Baptist Church
Milwaukie First Baptist Church
Mission Hispana el Buen Pastor
Peace Lutheran Church
Peace Mennonite Church
Peninsula Baptist Church
Peninsula Church of the Nazarene
Peninsula Open Bible Church
Philadelphia Community Missionary Baptist Church
Piedmont Presbyterian Church
Pilgrim Lutheran Church
Pilgrim Lutheran Church
Pioneer United Methodist Church
Pleasant Valley Community Baptist Church
Portland Area Seventh Day Baptist Church
Portland Campus Christian Ministry
Portland Center for Spiritual Awareness
Portland Central Church Assembly of God
Portland Faith Church
Portland Foursquare Church
Portland Hispanic Seventh Day Adventist Church
Portland Hmong Alliance Church
Portland Korean United Methodist Church
Portland Metro Assembly of God Church
Portland Miracle Revival Church
Portland Onnuri Church
Portland Pentecostal Church
Portland Rescue Mission
Portland Vancouver Korean Seventh Day Adventist Church
Portland Victory Center
Portland Word and Spirit Church
Portsmouth Trinity Lutheran Church
Powellhurst Baptist Church
Power House Church
Praise Chapel
Praise Chapel of Gresham
Presbyterian Church of Laurelhurst
Red Sea Community Church
Redeemer Evangelical Lutheran Church
Reedville Presbyterian Church
Reedwood Friends Church
Reformation Lutheran Church
Reorganized Church of Jesus Christ of Latter Day Saints
Resurrection Lutheran Church
Richmond Community Church
River Hills Church
Rivergate Community Church
Rivers of Life Church
Riversgate Church
Rock Creek Community Church
Rock Creek Foursquare Church
Rockwood Christan Church
Rockwood Church of Christ
Rockwood United Methodist Church
Rolling Hills Community Church
Bethel Romanian Apostolic Church
Rosary Center
Rose City Church of the Nazarene
Rose City Park United Methodist Church
Greater Grace Church
Russian Evangelical Baptist Church
Russian Full Gospel Church
Sacred Heart Church
Saint Andrew Catholic Church
Saint Anne Catholic Church
Saint Anthonys Catholic Church of Portland
Saint Barnabas Episcopal Church
Saint Bartholomews Episcopal Church
Saint Cecilia Catholic Church
Saint Charles Church
Saint Clare Church
Portland Adventist Medical Center
Careunit Hospital of Portland
Hemophilia Foundation of Oregon
Legacy Emanuel Childrens Hospital
Oregon Health and Science University Hospital
Vibra Specialty Hospital
Saint Johns Health Center
Tuality Urgent Care
Providence Willamette Falls Medical Center
Berry Hill Center Shopping Center
Canby Market Center Shopping Center
Canby Square Shopping Center
Canterbury Square Shopping Center
Cedar Hills Center Shopping Center
Clackamas Promenade Shopping Center
Clackamas Town Center Shopping Center
Columbia Boulevard Wastewater Treatment Plant
Country Square Shopping Center
Division Crossing Shopping Center
Divsion Center Shopping Center
Durham Advanced Wastewater Treatment Facility
Eastport Plaza Shopping Center
Evangelical Center Conference Grounds
Forest Grove Center Shopping Center
Forest Grove Wastewater Treatment Facility
Fred Meyer Raleigh Hills Center Shopping Center
Galleria Center Shopping Center
Gateway Center Shopping Center
Saint Davids Episcopal Church
Saint Elizabeth Ann Seton Catholic Church
Saint Francis Catholic Church
Saint Francis of Assisi Catholic Church
Saint Gabriels Episcopal Church
Saint George Antiochian Orthodox Church
Saint Henry Catholic Church
Saint Ignatius Catholic Church
Saint James Episcopal Church
Saint John Fisher Church
Saint John the Apostle Catholic Church
Saint John the Baptist Greek Orthodox Church
Saint Johns Christian Church
Saint Johns Episcopal Church
Saint Joseph of Petersburg Orthodox Church
Saint Joseph the Worker Catholic Church
Saint Juan Diego Church
Saint Lukes Episcopal Church
Saint Mark Baptist Church
Saint Mark Presbyterian Church
Saint Marks Lutheran Church
Saint Marys Catholic Cathedral
Saint Marys Romanian Orthodox Church
Saint Matthew Lutheran Church
Saint Matthews Episcopal Church
Saint Michael and all Angels Church
Saint Nicholas Orthodox Church
Saint Patricks Church
Saint Paul Lutheran Church
Saint Paul Lutheran Church
Saint Peter and Paul Episcopal Church
Saint Peters Catholic Church
Saint Philip Neri Catholic Church
Saint Philip the Deacon Episcopal Church
Saint Pius X Church of Cedar Mill
Saint Rita Catholic Church
Saint Rose Catholic Church
Saint Sharbel Maronite Rite Catholic Church
Saint Stanislaus Polish Catholic Church
Saint Stephans Serbian Orthodox Church
Saint Stephens Catholic Church
Saint Stephens Episcopal Church
Saint Therese Catholic Church
Saint Timothy Lutheran Church
Samil Korean Presbyterian Church
Sauvie Island Community Church
Savage Memorial Presbyterian Church
Saved by Grace Lutheran Church
Scholls Community Church
Self Realization Fellowship Church
Sellwood Baptist Church
Sellwood United Methodist Church
Seventh Day Adventist Church
Seventh Day Adventist Church of Mount Tabor
Seventh Day Adventist Churches of Sunnyside
Sharon Seventh Day Adventist Church
Shepherd of the Valley Lutheran Church
Sisters of Saint Francis Church
Sisters of Saint Mary of Oregon Church
Sixth Church of Christ Scientist Reading Room
Brook Hill Historic Church
Slavic Baptist Church
Slavic Evangelical Church
Slavic Evangelical Church
Smith Memorial Presbyterian Church
Solid Rock Fellowship Church
Somerset Christian Church
Southminster Presbyterian Church
Southwest Bible Church
Southwest Church of Christ
Southwest Hills Baptist Church
Stafford Baptist Church
Stone Tower Seventh Day Adventist Church
Sunnyside Centenary United Methodist Church
Sunnyside Church the Nazarene
Sunnyside Seventh Day Adventist Church
Sunset Christian Fellowship Church
Sunset Covenant Church
Sunset Presbyterian Church
Sylvan Hill Church
Tabernacle of Hope Church
Temple Baptist Church
Tenrikyo Portland Church
Tenth Church of Christ Scientist Reading Room
The Antioch Missionary Baptist Church
The Church of Jesus Christ of Latter Day Saints
The Church of Jesus Christ of Latter Day Saints
The Church of Jesus Christ of Latter Day Saints
The Church of Jesus Christ of Latter Day Saints
The Morning Star Baptist Church
The Old Church
The Parish of Saint Mark
The Village Seventh Day Adventist Church
The Well Church
The Word of Life Community Church
Thompson Road Bible Fellowship Church
Throne Seeker Ministries
Tigard Christian Church
Tigard Community Friends Church
Tigard Covenant Church
Tigard First Baptist Church
Tigard First Church of Christ Scientist
Tigard Foursquare Church
Tongan Fellowship of the United Methodists
Trinity Episcopal Cathedral
Trinity Evangelical Church
Trinity Fellowship Church
Trinity Lutheran Church
Trinity Lutheran Church
Trinity United Methodist Church
True Life Fellowship Church
True Vine Baptist Church
Truth in Love Ministries
Tualatin Hills Christian Church
Tualatin Presbyterian Church
Tualatin United Methodist Church
Tualatin Valley Wesleyan Church
Union Gospel Mission Lifechange Center
United House of Prayer for all People
United Methodist Church of Tabor Heights
Unity Church of Beaverton
Unity Church of Portland
University Park Baptist Church
University Park Seventh Day Adventist Church
University Park United Methodist Church
Valley Hope Community Church of God
Vancouver Avenue First Baptist Church
Vermont Hills United Methodist Church
Victory Christian Center
Victory Outreach Church
Victory Temple Church of God in Christ
Vietnamese Assembly of God Church
Vietnamese Baptist Church of Aloha
Village Baptist Church
Vineyard Christian Fellowship Westside
Voice of the Trumpet Ministries
Walker Road Grace Brethren Church
Walker Temple Church of God in Christ
Waverly Heights Congregational Church
West Hills Baptist Church
West Hills Covenant Church
West Hills Friends Church
West Linn Lutheran Church
West Portland United Methodist Church
West Valley Community Church
Westgate Baptist Church
Westminster Presbyterian Church
Westside United Methodist Church
Wilshire United Methodist Church
Wilsonville United Methodist Church
Wings of Healing Portland Temple
Woodland Park Baptst Church
Woodland Park Chapel
Woodlawn Methodist Church
Word of Grace Christian Church
World Gospel Mission
World Heart Ministry
World Vision
Worldview Center
Yang E Mun Presbyterian Church
Youth for Christ
Zion Lutheran Church
Zion United Church of Christ
Zion Worship Center
Mission of the Atonement Catholic Lutheran Community
Mittleman Jewish Community Center
Montavilla Baptist Church
Montavilla United Methodist Church
Moreland Bible Church
Moreland Presbyterian Church
Mosaic Church
Mount Carmel Lutheran Church
Mount Gillard Missionary Baptist Church
Mount Hood Christian Center
Mount Olivet Baptist Church
Mount Scott Church of God
Mount Scott Church of the Nazarene
Mount Scott Park Presbyterian Church
Mount Tabor Presbyterian Church
Mountainview Christian Church
Multnomah Holiness Association
Multnomah Presbyterian Church
Murray Hills Christian Church
Nam - Quang Temple
Native American United Methodist Fellowship Church
Nazarene Ministry of Help
Neighborhood Church
New Era Christian Spiritualist Church
New Heights Community Church
New Hope Missionary Baptist Church
New Jerusalem Baptist Church
New Life Christian Center
New Life Church
New Life Community Church of God in Christ
New Life Missionary Church
New Testament Church of God in Christ
New Thought Ministries of Oregon
New Vision Fellowship Church
North Community Church
Northeast Baptist Church
Northeast Community Fellowship Foursquare Church
Northminster Presbyterian Church
Northwest Christian Evangelistic Associates
Northwest District of the Lutheran Church
Norwood Bible Church
Oak Grove United Methodist Church
Oak Hills Church
Oak Hills Presbyterian Church
Oasis Christian Center
Old Laurelhurst Church
Open Bible Church
Oregon City Assembly of God
Oregon City Christian Church
Oregon City First Church of Christ Scientist
Orthodox Church of the Annunciation
Our Lady of Fatima Roman Catholic Church
Our Lady of the Lake Catholic Church
Faithful Savior Ministries
Overstreet Powerhouse Temple Church of God in Christ
Palace of Praise United Pentecostal Church
Parklane Christian Reformed Church
Abundant Life Church - Parkrose Campus
Parkrose Community United Church of Christ
Parkrose Deliverance Tabernacle
Parkrose United Methodist Church
Grace Foursquare Church
Grace Korean Methodist Fellowship Church
Grace Lutheran Church
Grace Memorial Episcopal Church
Grace Presbyterian Church
Grant Park Church
Great Day Fellowship Church
Greater Faith Baptist Church
Greater Portland Baptist Church
Greater Portland Bible Church
Gresham Christian Fellowship
Hall Boulevard Baptist Church
Harvest Christian Center
Harvest Community Church
Helvetia Community Church
Heritage Baptist Church
Highland United Church of Christ
Highland United Church of Christ II
Hillcrest Missionary Baptist Church
Hillsboro Presbyterian Church
Hillsdale Community Church
Hillsview Evangelical Covenant Church
Hinson Memorial Baptist Church
Holbrook Bible Church
Holladay Park Church of God
Holy Apostles Orthodox Church
Holy Cross Church
Holy Family Church
Holy Nativity of the Theotokos Orthodox Church
Holy Rosary Church
Holy Spirit Association for the Unification of the World
Holy Trinity Catholic Church
Holy Trinity Greek Orthodox Church
Holy Trinity Lutheran Church
Hope Community Church of Lake Oswego
Hope Lutheran Church of the Deaf
Hope of Portland Church
Hosanna Christian Fellowship Church
House of Prayer for All Nations
Hughes Memorial United Methodist Church
I Am Sanctuary Church
Iglesia de Dios
Iglesia de Dios Pentecostal
Iglesia De Dios Pentecostal
Iglesia del Dios Vivo Columna y Apoyo de la Verdad
Iglesia el Alfa y Omega
Iglesia la luz del Mundo
Imago Dei Community
Immaculate Heart Catholic Church
Immanuel Christian Fellowship
India Full Gospel Church
International Bible Church
Intown Presbyterian Church
Irvington Covenant Church
Iu-Mien Fellowship Baptist Church
Jackson Baptist Church
Japanese Grace Bible Church
Japanese International Baptist Church
Japanese United Methodist Church of Epworth
Jennings Lodge Community Church
Johrei Fellowship Church
Kairos-Milwaukie United Church of Christ
Kenilworth Presbyterian Church
Kenton United Presbyterian Church
Kern Park Christian Church
King of Glory Ministries
King of Kings Lutheran Church
Kingdom Hall of Jehovahs Witnesses
Kingdom Hall of Jehovahs Witnesses
Kingdom Hall of Jehovahs Witnesses
Minter Bridge Elementary School
Nancy Ryles Elementary School
Oak Hills Elementary School
Orenco Elementary School
Portland Faith College
Portland Westview Seminary
Renaissance Arts Academy
Saint Rita Religious Education Center
Saint Stephens Academy
Scholls Heights Elementary School
School of Science and Technology
Southridge High School
Spanish-English International School
Stoller Middle School
Terra Linda Elementary School
Terra Nova High School
Tualatin High School
Victory Middle School (historical)
Walla Walla College School of Nursing
Wee Wisdom Preschool
Westgate Christian School
Westview High School
Young Womens Academy (historical)
Glisan Street Station Shopping Center
Greenway Town Center Shopping Center
Gresham Square Shopping Center
Gresham Station Shopping Center
Gresham Town Fair Shopping Center
Halsey Crossing Shopping Center
Highland Fair Shopping Center
Hillsboro Mart Shopping Center
Hillsboro Plaza Shopping Center
Hillsboro Wastewater Treatment Facility
Hillsdale Center Shopping Center
Holladay West Park Station
Hood Center Shopping Center
Hoodland Plaza Shopping Center
Jantzen Beach Center Shopping Center
King City Plaza Shopping Center
King Road Center Shopping Center
Lloyd Center Shopping Center
Mall 205 Shopping Center
Martinazzi Square Shopping Center
Menlo Park Plaza Shopping Center
Milwaukie Marketplace Shopping Center
Murray Scholls Town Center Shopping Center
Murrayhill Marketplace Shopping Center
New Market Village Shopping Center
Newberg Plaza Shopping Center
Oak Village Shopping Center
Oregon City Shopping Center
Oregon Trail Center Shopping Center
Oswego Town Square Shopping Center
Oswego Village Center Shopping Center
Pittock Block
Powell Villa Center Shopping Center
Raleigh West Center Shopping Center
River Falls Shopping Center
Robinwood Center Shopping Center
Rock Creek Advanced Wastewater Treatment Facility
Rockwood Plaza Shopping Center
Ross Center Shopping Center
San Rafael Center Shopping Center
Sandy Marketplace Shopping Center
Sherwood Market Center Shopping Center
Sherwood Plaza Shopping Center
Shute Park Plaza Shopping Center
South Fork Water Board Treatment Plant
Springbrook Plaza Shopping Center
Sunset Mall Shopping Center
Sunset Square Shopping Center
Tanasbourne Town Center North Shopping Center
Tanasbourne Town Center South Shopping Center
Tanasbourne Village Shopping Center
The Sunset Esplanade Shopping Center
The Village Shopping Center
The Water Tower Shopping Center
Tigard Marketplace Center Shopping Center
Tigard Towne Square Shopping Center
Town Center Shopping Center
Union Station
Valley Plaza Shopping Center
Washington Square Shopping Center
Wood Village Town Center Shopping Center
Woodstock Super Center Shopping Center
Campbell Fountain
Lan Su Chinese Garden
Central Post Office
Cherry Blossom Post Office
Evergreen Post Office
Lents at Eastport Post Office
Rose City Park Post Office
Sellwood Post Office
Solomon Courthouse Post Office
Academy for Scriptual Knowledge (historical)
Archer Glen Elementary School
Arts and Communication Middle Magnet School
Arts Communication and Technology School
Ascension Early Childhood Education Center
Beaverton High School
Biztech High School
Bridgeport Elementary School
Calvary Christian Academy and Day Care Center
Centennial Learning Center
Century Seminary
Christ Church Episcopal Preschool
Christ the King Lutheran Preschool
Community Christian Learning Center and Day Care Center
Community Christian School
Community School
Conestoga Middle School
Deer Creek Elementary School
Dilley Elementary School
Durham Education Center
El Puente
Findley Elementary School
Gateway Christian School
Gresham United Methodist Preschool
Hazelbrook Middle School
Highland Community Pre-Kindergarten
Jackson Elementary School
Jacob Wismer Elementary School
Kerr Youth Center at Wynne Watts School
Kerr Youth and Family Center
Leadership and Entrepreneurship Public Charter High School
Little Lambs Preschool
Mary Woodward Elementary School
Merlo Station Night School
Metzger Community Preschool
Miller Education Center 6 - 8
Miller Education Center High School
Milwaukie Academy of the Arts
Milwaukie Covenant Church Preschool and Kindergarten
Bilingual Gateway School
Blanchet Catholic School
Chapman Hill Elementary School
Chemawa Indian School
Claggett Creek Middle School
Weddle Elementary School
Clear Lake Elementary School
Concordia Lutheran School
Cornerstone Christian School
Crossler Middle School
Gervais High School
Early College High School
Eldriedge Elementary School
Forest Ridge Elementary School
French Prairie Middle School
Lincoln Elementary School
Fruitland Elementary School
Gubser Elementary School
Hallman Elementary School
Hammond Elementary School
Harritt Elementary School
Hayesville Elementary School
Heritage Elementary School
Valor Middle School
Houck Middle School
Immanuel Evangelical Lutheran School
Jefferson Middle School
Mount Angel Middle School
Lamb Elementary School
Lee Elementary School
Leslie Middle School
Liberty Elementary School
Marion Elementary School
McNary High School
Migrant Primary School
Miller Elementary School
Myers Elementary School
North Marion Intermediate School
North Marion Middle School
Pratum Elementary School
Pringle Elementary School
Roberts High School
Salem Academy Christian School
Schirle Elementary School
Sprague High School
Scott Elementary School
Silverton Christian School
Silverton High School
Saint John Lutheran School
Saint Joseph School
Saint Paul High School
Saint Paul Parochial School
Stephens Middle School
Sumpter Elementary School
West Salem High School
Willamette Christian School
Willamette Valley Christian School
Woodburn Arthur Academy
Yoshikai Elementary School
Ione Community Charter School
Irrigon Elementary School
Windy River Elementary School
Ash Creek Intermediate School
Eola Hills Charter School
Dallas High School
Faith Christian School
Falls City Elementary School
Falls City High School
Independence Elementary School
Luckiamute Valley Charter School
Mid Valley Christian Academy
Oakdale Heights Elementary School
Riviera Christian School
North Sherman Elementary School
Nestucca Valley Middle School
Garibaldi Elementary School
Nehalem Elementary School
Neskowin Valley School
Pacific Christian School
Tillamook Adventist School
Trask River High Schools - Camp Tillamook
Desert View Elementary School
Echo School
Nixyaawii Community School
Pendleton Academies
Pilot Rock Elementary School
Pilot Rock High School
Sandstone Middle School
Stanfield Elementary School
Cove School
Elgin High School
Grande Ronde Academy
Imbler High School
Island City Elementary School
La Grande Adventist School
La Grande High School
La Grande Middle School
Powder Valley School
Stella Mayfield Elementary School
Union Elementary School
Union High School
Enterprise Elementary School
Joseph Elementary School
Joseph High School
Wallowa Elementary School
Agia Sophia Academy
Alberta Rider Elementary School
Aloha-Huber Park Elementary School
Banks Elementary School
Banks Christian Academy
Butternut Creek Elementary School
City View Charter School
Durham Elementary School
Emmaus Christian School
Fern Hill Elementary School
Forest Hills Lutheran School
Free Orchards Elementary School
Gaarde Christian School
German American School of Portland
Health and Science School
Heritage Christian School
Horizon Christian Elementary School
Imlay Elementary School
Life Christian School
Lincoln Street Elementary School
Middleton Elementary School
Mooberry Elementary School
Oak Tree School
Paul L Patterson Elementary School
Pilgrim Lutheran School
Quatama Elementary School
Reedville Elementary School
Sexton Mountain Elementary School
Southwest Christian School
Saint Francis School
Swallowtail School
Tobias Elementary School
Tualatin Elementary School
Visitation Catholic School
Mitchell School
Spray School
Amity Elementary School
Amity High School
Amity Middle School
Antonia Crater Elementary School
Bethel Christian School
Chehalem Valley Middle School
CS Lewis Academy
Dayton High School
Dayton Junior High School
Dundee Elementary School
Duniway Middle School
Grandhaven Elementary School
International Community School
Joan Austin Elementary School
McMinnville Adventist Christian School
Mountain View Middle School
Sheridan Japanese School
Saint John Lutheran School and Little Lamb Preschool
Sue Buel Elementary School
Yamhill Grade School
Veritas School
Willamina Middle School at Grand Ronde
Hayworth Saddle
Turner Drop
Lakeview Interagency Fire Center
Klamath Falls Interagency Fire Center
Negro Creek
Squaw Ridge
Camp Watson Cemetery
Mary Waterman Grave
Calvary Mennonite Church
Butteville Community Church
Saint Andrew Lutheran Church
Church of Jesus Christ of Latter Day Saints
Westside Church of Christ
Tualatin Valley Community Church
Church of Jesus Christ of Latter Day Saints
Church of Jesus Christ of Latter Day Saints
Seventh Day Adventist Church
Immanuel Community Church
Beaverton Church Of The Nazarene
Cascade Chapel Assembly of God
Clatskanie United Methodist Church
Clatskanie Presbyterian Church
Gateway Worship Center
Corbett Community Church
Sacred Heart Catholic Church
Hood River Alliance Church
Immanuel Lutheran Church
Tucker Road Baptist Church
Hubbard United Church
Zion Mennonite Church
Maupin Community Evangelical Church
Parkdale Church of the Nazarene
Parkdale Baptist Church
First Baptist Church
Pine Grove-Odell United Methodist Church
Rainier United Methodist Church
Rainier Church of God
Church of Jesus Christ of Latter Day Saints
First Lutheran Church
Sunset Park Community Church
Warren Baptist Church
Canaan Community Church
Saint Wenceslaus Catholic Church
Grace Lutheran Church
Church of Jesus Christ of Latter Day Saints
Dalles Evangelical Church
Zion Lutheran Evangelical Church
Chinese Christian Church of Corvallis
Suburban Christian Church
First Christian Church
Peace Lutheran Church
Monroe Church of Christ
North Albany Community Church
Alsea United Methodist Church
Corvallis Foursquare Church
United Methodist Church
First Church of the Nazarene
First Church Of Christ Scientist
Our Saviours Lutheran Church
Faith Lutheran Church
Grace Episcopal Church
Saint Frances De Sales
Philadelphia Church
Church of Jesus Christ of Latter Day Saints
Warrenton United Methodist Church
Calvary Assembly of God
Vernonia Foursquare Church
Coos Bay Foursquare Church
Coquille Foursquare Church
Emmanuel Baptist Church of Coquille Oregon
Saint James Lutheran Church
Church of God of North Bend Oregon
Bay Area Church of the Nazarene
Church of Jesus Christ of Latter Day Saints
Bandon Christian Fellowship
Saint Monicas Catholic Church
Arago Community Church
Church of Jesus Christ of Latter Day Saints
Saint Timothys Episcopal Church
Saint Charles Catholic Church
Zion Lutheran Church
First Community Church of Port Orford
Beautiful Savior Lutheran Church
Highlands Baptist Church
Vine Street Baptist Church
New Beginnings Christian Assembly
Sutherlin Family Church
Seventh Day Adventist Church
Drain Church of the Nazarene
First Baptist Church of Drain
Elkton Christian Church
Olivet Presbyterian Church
Glendale Baptist Church
Seventh-Day Adventist Church
Church of the Nazarene
Seventh Day Adventist Church
Oakland Church of Christ
Riddle First Church of God (historical)
Open Bible Christian Center
Church of Jesus Christ of Latterday Saints
Seventh Day Adventist Church
Lighthouse International Church
Emerald Baptist Church
Allison Park Christian Church
Bethesda Lutheran Church
Harvest Community Church
Norkenzie Christian Church
Trinity Lutheran Church
Living Faith Christian Fellowship
Art House Friends Church
Trent Church of Christ
Bethany Church of Franklin Oregon
Florence Foursquare Church
Faith Lutheran Church
Tri County Worship Center
Pleasant Hill Church of Christ
Pleasant Hill Lutheran Church
Trinity Baptist Church
Community Faith Church
East Side Baptist Church
Saint Matthews Episcopal Church
Grace Baptist Church
Unitarian Church in Eugene
Episcopal Church Resurrection
Church of the Nazarene
Elmira Church of Christ
Saint Marys Catholic Church
Marcola Christian Church
Olivet Baptist Church
Toledo Foursquare Church
Bahais of Lincoln County
Native American Church of Siletz
Newport Foursquare Church
Lighthouse Vineyard Christian Fellowship
Lincoln City Evangelical Church
First Baptist Church
First Baptist Church of Siletz
Siletz Foursquare Church
Church of Jesus Christ of Latter Day Saints
Saint Anthonys Catholic Church
Sweet Home Evangelical Church
First Christian Church
Family Worship Center
Calvary Baptist Church
Brownsville Mennonite Church
Lebanon Foursquare Church
Lebanon Evangelical Church
Evergreen Church of God in Christ Mennonite Church
Oakview Community Church of God
Church of Jesus Christ of Latter Day Saints
Harrisburg Christian Church
Church of God Seventh Day
Church on the Hill
Evergreen Church
First Christian Church
Saint Pauls Episcopal Church
Salem Christian Center
Messiah Lutheran Church
Skyline Baptist Church
Gateway Foursquare Church
Fruitland Evangelical Church of North America
Willamette Valley Baptist Church
Church of God of Prophecy Bible Place
Jefferson Evangelical Church
Chapel of The Holy Family and Retreat House at Saint Nicholas Ranch
First Christian Church
Apostolic Christian Church of Silverton Oregon
Calvary Lutheran Church
New Hope Community Church
Church of Jesus Christ of Latter Day Saints
Immanuel Lutheran Church
Saint Paul Catholic Church
Trinity United Methodist Church
Scotts Mills Friends Church
Saint Boniface Catholic Church
Turner Christian Church
Springdale Community Bible Church
Oregon Methodist Foundation
Portland Korean Church
Buddhist Daihonzan Henjyoji Temple
Mahasiddha Buddhist Center
Jehovahs Witnesses
Oregon Buddhist Church
Portland Buddhist Priory Incorporated
Immanuel Lutheran Church
Portland Moreland Church of the Nazarene
Calvary Open Bible Church
Han-Mee Presbyterian Church
Victory Fellowship Incorporated
Church Of Grace
Christian Assemblies of the World
Apostolic Christian Church
Tremont Evangelical Church
Asian Buddhist Community Congregation of Oregon
Havurah Shalom
Saint James Full Gospel Pentacostal Church
Saint Michaels Lutheran Church
New Birth Full Gospel Pentecostal Church
Mount Sinai Church of God in Christ
Mount Zion Baptist Church
Portland Slavic Evangelical Baptist Church
Providence Seaside Hospital
Oregon City Blessing Church
Portland Christian Center
Congregation Neveh Shalom
Church of Jesus Christ of Latter Day Saints
Free Methodist Church
Powell Valley Covenant Church
Saint James Lutheran Church
Church of Jesus Christ of Latter Day Saints
First Unitarian Church
Apostolic Christian Church
West Hills Community Church
Kingwood Bible Church
Dallas Alliance Church
Faith Evangelical Free Church
Saint Patricks Church
Robert D. Maxwell Veterans Memorial Bridge
Buena Vista Community Church
Living Word Faith Fellowship
Monmouth Evangelical Church
Calvary Bible Church
First Baptist Church
Tillamook Christian Center
Saint Josephs Catholic Church
Winema Christian Church
Pacific Coast Bible Church
Nestucca Valley Presbyterian Church
Church of Jesus Christ of Latter Day Saints
Sacred Heart Catholic Church
Church of Jesus Christ of Latter Day Saints
Woodhaven Community Church
Cornelius Baptist Church
Saint Peter Lutheran Church
Saint Bedes Episcopal Church
Zion Lutheran Church
Chinese Evangelical Church
North Plains Christian Church
Saint Francis of Assisi Catholic Church
Church of Jesus Christ of Latter Day Saints
Saint Anthony's Catholic Church
Wapato Valley Church
Valley Baptist Church
Abundant Life Community Church
Sherwood United Methodist Church
First Free Methodist Church of Carlton
Pioneer Evangelical Church
Valley Baptist Church
Saint John Lutheran Church
McMinnville Foursquare Church
United Methodist Church of McMinnville
Newberg Foursquare Church
Zion Lutheran Church
Chehalem Valley Baptist Church
Newberg Christian Church
First Christian Church
Trinity Lutheran Church of Sheridan
Church of Jesus Christ of Latter Day Saints
Church of Christ
Church of Jesus Christ of Latter Day Saints
Lafayette Community Church
Bible Baptist Church
First United Presbyterian Church
Saint Michaels Catholic Church
Portland Air Guard Station
Camp Withycombe
United States Coast Guard Lifeboat Station Coos Bay
United States Coast Guard Station Umpqua River
United States Coast Guard Motor Lifeboat Station Yaquina Bay
Naval Bombing Range Boardman
Umatilla Chemical Depot
United States Coast Guard Motor Lilfeboat Station Chetco River
Camas Creek
Bald Butte Lookout
Bald Mountain Lookout
Barnes Valley Boat Ramp
Bear Butte Lookout
Bly Trailhead
Crane Mountain Viewpoint
Deming Creek Trailhead
Frog Camp Recreation Site
Hager Mountain Lookout
Horsefly Mountain Lookout
Lantern Flat Guard Station
Miller Creek Camp
Morgan Butte Lookout
Farmers Creek
Moody Island
Pitch Log Recreation Site
Potholes Recreation Site
Shake Butte Lookout
Stan H Spring Recreation Site
Sycan Butte Lookout (historical)
Sycan Siding Trailhead
Wildhorse Recreation Site
Klamath Hills Trailhead
Aspen Ridge Trailhead
Bear Creek Trailhead
Black Hills Guard Station (historical)
Cottonwood Creek Trailhead
Cox Pass Trailhead
Hanan Sycan Trailhead
Lakes Loop Trailhead
Mill Trailhead
North Fork Sprague River Trailhead
Rogger Meadow Trailhead
Fremont Point Lookout (historical)
Lookout Rock Trailhead
Lookout Rock Lookout
Swale Trailhead
Vee Lake Trailhead
Walker Trailhead
Winter Rim Trailhead
Cal - Ore Life Flight Ground
Morrow County Emergency Medical Services Irrigon Station
Morrow County Health District Boardman Station
Oregon Air Life Headquarters
Metro West Ambulance
Med Trans of Oregon
Western Lane Ambulance District
South Lincoln Ambulance Service
Yachats Rural Fire Protection District North Station
Condon Ambulance Service
Crest II Emergency Medical Services
Tillamook County General Hospital Pacific City Station
City of Glendale Ambulance Service
Metro West Ambulance Service
Spray Volunteer Ambulance Association
East Umatilla County Health District
Port Orford Community Ambulance
Pacific West Ambulance
Pacific West Ambulance
Sherman County Ambulance
Halfway Oxbow Ambulance Service
American Medical Response
Tillamook County General Hospital Garibaldi Station
Town of Lakeview Emergency Medical Services
Lifeguard Ambulence Corporation Medical Transport
Lake County Search and Rescue
Tillamook County General Hospital Manzanita Station
Air Life of Oregon
John Topits Park
Sandpines Golf Links
Hawk Creek Golf Course
Salmon River Hatchery
Bay Area Hospital
Dean Creek Elk Viewing Area
Forest Hills Country Club
Vincent Creek Recreation Site
Crestview Hills Golf Course
Alsea Bay Historic Interpretive Center
Cape Perpetua Visitor Center
Smithwick Haydite Quarry
Husted Creek
Al Kennedy Alternative High School
Sullivan Creek Falls
Pine Eagle Elementary
Albany Options School
Good Samaritan School
Eastmont Community School
International School of the Cascades
Ponderosa Elementary School
John Muir Elementary School
Crater Academy of Health and Public Services
Crater Academy of Natural Sciences
Crater Renaissance Academy
Gilchrist Junior - Senior High School
Buena Vista Elementary School
Academy of International Studies at Woodburn
Douglas Avenue Alternative School
Jane Goodall Environmental Middle Charter School
Optimum Learning Environment Charter School
Crack in the Ground
Reed Rock
Four Craters Lava Field
Bowman Wells
Sprague Well
Trask Mountain Middle
Fire Mountain School
Sisters Charter Academy of Fine Arts
William E Miller Elementary School
Cobb School
North Douglas High School
Phoenix School
Warner School
Horizon Christian School
Armadillo Technical Institute
Ashwood Elementary School
Madras Christian School
Mount Sexton Intermediate School
Oak Hill School
Baker Charter School
Arata Creek Alternative School
Azbuka Academy
Imbler Elementary School
Chehalem Valley Academy
Bonny Slope Elementary School
Edy Ridge Elementary School
Ellen Stevens Community Academy
South Meadows Middle School
The Goddard School
Thomas Edison High School
Crosswater Golf Course
Bend Golf and Country Club
Meadows Golf Course
Woodlands Golf Course
Rock Viewpoint
Glaze Meadow Golf Course
Big Meadow Golf Course
West Village Lodge
Sunrise Lodge
Nordic Center
Mount Bachelor Ski Area
Pine Marten Lodge
China Hat Guard Station
West Cultus Lake Recreation Site
Big Obsidian Flow Trailhead
Camp II Trailhead
Road 25 Recreation Site
Derrick Well
Swamp Wells Trailhead
Horse Butte Trailhead
Lost Tracks Golf Club
Crescent Lake Recreation Site
Chief Paulina Trailhead
Paulina Peak Trailhead
Paulina Lake Visitor Center
Wake Butte Trailhead
Fall River Trailhead
Ko Butte Well
Widgi Creek Golf Club
Sisters Cow Camp
South Lava Trailhead
Bear Creek Orchards
Carter Orchards
Davis Orchards
Eden Valley Orchards
Highlands Orchards
Hillcrest Orchard
Hull Orchard
Meyer Orchards
Cygnet Farm
Union High School (historical)
Nordeen Shelter
Meissner Shelter
Withrow Creek
Sam Brown Creek
South Fork Sam Brown Creek
Petes Mountain Creek
53rd Avenue Community Park
Magnolia Park
Trepha M. Baron Pavilion
Columbia Gorge
Lasts Island (historical)
Antelope Reservoir Day-Use Area
Rackheap Creek
Edwards Pioneer Cemetery
Lower Trestle Creek Falls
Upper Trestle Creek Falls
Lower Parker Falls
Upper Parker Falls
Pinard Falls
Clover Falls
Beef City Feedlot
Top Cut Feedlot
Wolfe Feedlot
Mid - Columbia Fire and Rescue
West Valley Fire District
Union Rural Fire Protection District
Lebanon Fire District Station 31
Clackamas Fire District Number 1 Station 15 John Adams
Ontario Fire and Rescue
Gates Rural Fire Protection District
Forest Grove Fire and Rescue Headquarters
Eugene Fire Station 1 Downtown Station
Saint Paul Fire District Headquarters
Philomath Fire and Rescue Station 201
Jackson County Fire District 5
Mount Angel Fire District
Turner Fire Department
Siuslaw Valley Fire and Rescue Station 1
Springfield Fire Department Station 4
Glendale Rural Fire Protection District
Corvallis Fire Department Station 4
City of Moro Fire Department
Cove Rural Fire Protection District
Prospect Fire Department
Parkdale Fire Department
Junction City Rural Fire Protection District Station 1
Scio Rural Fire Protection District
Junction City Rural Fire Protection District Station 2
Lafayette Fire Department
Azalea Rural Fire Protection District
Columbia River Fire and Rescue Rainier Station
North Douglas County Fire and Emergency Medical Services Station 1
Reedsport Volunteer Fire Department Station 1
Stayton Rural Fire Protection District Stayton Station
North Powder Rural Fire Protection District
Williams Rural Fire Protection District
Pine Valley Rural Fire Protection District
Falls City Fire Department
Yachats Rural Fire Protection District South Station
Amity Fire District
Canyonville - South Umpqua Fire Department
Astoria Fire Department Station 1
Newport Fire Department Station 1
Rockaway Beach Fire Department
Canby Fire District Station 62
North Sherman County Rural Fire Protection District
Sheridan Fire District
Crook County Fire and Rescue Main Station
Toledo Fire and Rescue Department Station 41
McMinnville Fire Department
Imbler Rural Fire Protection District Headquarters
Phoenix Fire Department
Coos Bay Fire Department Central Station 1
Tualatin Valley Fire and Rescue Station 20
Baker City Fire Department
Aurora Rural Fire Protection District Headquarters
Idanha - Detroit Rural Fire Protection District Substation
Nestucca Rural Fire Protection District Station 81 Headquarters
Dayton Fire District
Mosier Volunteer Fire Department
Mount Vernon Fire Department
Medford Fire and Rescue Station 2
North Bend Fire Station 1
Jackson County Fire District 3 White City Station Headquarters
Odell Rural Fire Protection District
Siletz Rural Fire Protection District Main Station
Gearhart Volunteer Fire Department
Hillsboro Fire and Rescue Station 1 Downtown Main Station
Sublimity Rural Fire Protection District
Applegate Valley Rural Fire Protection District 9 Station 4
Pendleton City Fire and Ambulance Station 1
North Lincoln Fire and Rescue District 1 Station 1400 Lincoln City North
Lakeview Fire Department
Carlton Fire Department
Cannon Beach Rural Fire Protection District
City of Condon Volunteer Fire Department
Jefferson County Fire District 2
Salem Fire Department Station 6
Brookings Fire and Rescue
Stanfield Fire Department
Yamhill Fire Protection District
Springfield Fire Department Station 5
Douglas County Fire District 2 Station 8
North Gilliam County Rural Fire Protection District
Wolf Creek Rural Fire Protection District
Hubbard Rural Fire Protection District
South Lane County Fire and Rescue Station 2 - 1
Clackamas Fire District Number 1 Station 1 Town Center
Nyssa Fire Department
Molalla Rural Fire Protection District Number 73 Station 85
Columbia River Fire and Rescue Saint Helens Station
Scappoose Rural Fire Protection District
Umatilla County Fire District 1 Station 21
Sandy Rural Fire Protection District Station 71
Dee Rural Fire Protection District
Unity Volunteer Fire Department
Dundee Fire Department Station 3
Port Orford Volunteer Fire Department
Salem Fire Department Station 1 Headquarters
Aumsville Rural Fire District
Nehalem Bay Fire Department Station 13
Brownsville Rural Fire District 61
Keizer Fire District
Hoodland Fire District 74 Main Station
John Day Fire Department
Oakland Rural Fire Protection District
Tualatin Valley Fire and Rescue Station 34 Tualatin
Clatskanie Rural Fire Main Station
Canyon City Volunteer Fire Department
South Lane County Fire and Rescue Station 2 - 3
Harrisburg Fire and Rescue Station 41
Tri - City Rural Fire Department
Hines Fire Department
Lyons Rural Fire Protection District Station 1
Butte Falls Volunteer Fire Department
Hood River Fire and Emergency Medical Services
Seaside Fire and Rescue
Bay City Fire Department
Colton Rural Fire Protection District 70 Main Station
City of Bend Fire Department Station 305 North Fire Station
Kingsley Field Fire Department
Fossil Volunteer Fire Department
Peoria Station 53
Lostine Volunteer Fire Department
Keno Rural Fire Protection District Station 3
Milton - Freewater Rural Fire District North Station
Jackson County Fire District 4 Trail Station
Hermiston Fire and Emergency Services Station 2
Aumsville Rural Fire Protection District Substation 670
La Pine Fire Department Station 102
Mist - Birkenfeld Rural Fire Protection District Fishhawk Lake Station
Harbor Rural Fire Protection District
Days Creek Fire Department
Cornelius Fire Department
Tualatin Valley Fire and Rescue Training Center
Monitor Rural Fire Protection District Station 58
Milo Rural Fire Protection District
Lakeside Rural Fire Protection District
Prairie City Fire Department
Roseburg Fire Department Station 1
Corvallis Fire Department Station 1
Aurora Rural Fire Protection District Donald
Sweet Home Fire and Ambulance District Station 21
Springfield Fire Department Station 3
Jackson County Fire District 3 Eagle Point Station
Saint Paul Fire District Substation
City of Bend Fire Department Station 301 West Fire Station
Tygh Valley Fire Department
Powers Volunteer Fire and Ambulance
Central Oregon Coast Fire and Rescue District 7 Station 7200
Albany Fire Department Station 1
Monroe Rural Fire Protection District Station 1
Warrenton Fire Department
Clackamas Fire District Number 1 Boring Community Fire Station Number 14
Umatilla Tribal Fire Department
Coquille Fire and Rescue
Jackson County Fire District 4 Shady Cove Station
Tualatin Valley Fire and Rescue Station 61 Butner Road
Burns Fire Department
Gladstone Fire Department
Dallas Fire Department
West Valley Fire District Substation
Lake Oswego Fire Department Station 214
Grants Pass Fire and Rescue Operations Division Station 1 Headquarters
Vale Fire and Ambulance
Rogue River Rural Fire Protection District
City of Heppner Fire Department
Vernonia Rural Fire Protection District
Riddle Volunteer Fire Department
Halsey - Shedd Rural Fire Protection District Station 51
Stayton Rural Fire Protection District Marion Station
Evans Valley Fire District 6
Banks Fire Protection District 13 Headquarters
Seal Rock Rural Fire Protection District Bayshore Station
Silverton Fire District Headquarters
Illinois Valley Fire District Station 1
Gold Beach Volunteer Fire Department
Coos Bay Fire Department Empire Station
Tillamook Fire District Station 71
Mill City Fire Department
Oakridge Fire Department
Boardman Rural Fire Protection District Station 1
Lane County Fire District 1 Station 101
Applegate Valley Rural Fire Protection District 9 Station 3 Headquarters
North Lincoln Fire and Rescue District 1 Station 1600 Taft
Dufur Volunteer Fire Department
Scio Rural Fire Protection District Station 91
Rufus Volunteer Fire Department and Ambulance Service
Newport Fire Department Station 10
Jackson County Fire District 3 Agate Lake Station
Fairview Rural Fire Protection District
Cascade Locks Fire and Emergency Medical Services
Manzanita Department of Public Safety
Portland Fire and Rescue Station 2 Parkrose
Gaston Rural Fire Protection District
Jacksonville Fire Department
North Douglas County Fire and Emergency Medical Services Station 3
Bonanza Rural Fire Protection District
Sutherlin Fire Department
Chemeketa - Brooks Regional Training Center
Medford Fire Department Station 6
Netarts - Oceanside Rural Fire Protection District Station 62
United States Forest Service Tiller Ranger District
Fremont Winema National Forest Fire Center
Umatilla Chemical Depot Fire Department
Oregon Air National Guard Base Fire and Rescue Portland
Corvallis Fire Department Station 5 (historical)
Pine Hollow Volunteer Fire Department Station 1
Upper Chetco Rural Fire Protection District
Siuslaw Valley Fire and Rescue Station 5 Canary Station
South Lane County Fire and Rescue Station 2 - 2
Siuslaw Valley Fire and Rescue Station 2 Old Town Station
Hauser Rural Fire Protection District
Adrian Fire Department
United States Forest Service Ashland Ranger District
South Lane County Fire and Rescue Station 2 - 4
United States Forest Service Hebo Ranger District
United States Forest Service Hood River Ranger District
McKenzie Fire and Rescue Station 2 - Camp Creek Station
Keno Rural Fire Protection District Station 2
Douglas Forest Protective Association North Unit
Medford Fire Department Station 5
Jackson County Fire District 3 Gold Hill Station
Jackson County Fire District 3 Dodge Bridge Station
Irrigon Rural Fire Protection District
Boardman Rural Fire Protection District Station 2
Illinois Valley Fire District Station 5
Illinois Valley Fire District Station 3
Illinois Valley Fire District Old Station 3
Illinois Valley Fire District Station 2
Keating Rural Fire Protection District
Gresham Fire and Emergency Services Station 75
Gresham Fire and Emergency Services Station 74
Philomath Fire and Rescue Station 202
Thomas Creek Rural Fire Department
Southwest Polk County Rural Fire Protection District Station 110
United States Forest Service Prospect Ranger District
United States Forest Service Redmond Hotshots
Portland Fire and Rescue Station 24 - Overlook / Swan Island
United States Forest Service Wild Rivers Ranger District
Eugene Fire Station 6 Sheldon Station
McKenzie Fire and Rescue Station 3 - Camp Creek Station
Sweet Home Fire and Ambulance District Station 22
Central Oregon Helitak Prineville Helibase
City of Bend Fire Department Station 302 Tumalo Fire Station
Tualatin Valley Fire and Rescue Station 23 Robinhood
Applegate Valley Rural Fire Protection District 9 Station 2
United States Forest Service Detroit Ranger District
Myrtle Point Fire Department Station 1
Eugene Fire Station 9 Valley River Station
Eugene Fire Station 11Santa Clara Station
Merrill Rural Fire Protection District
Keno Rural Fire Protection District Station 1Headquarters
Huntington Volunteer Fire Department
Eagle Valley Rural Fire Protection District
Powder River Rural Fire Department - Mosquito Flat Fire Station
Applegate Valley Rural Fire Protection District 9 Station 1
Eugene Fire Station 7 Bethel Station
Tangent Rural Fire Department
Elkton Rural Fire Protection District
Tiller Rural Fire Protection District Headquarters
Applegate Valley Rural Fire Protection District Station 5
Eugene Fire Station 8 Danebo Station
Scio Rural Fire Protection District Station 92
Sweet Home Fire and Ambulance District Station 24
Corvallis Fire Department Station 6
City of Bend Fire Department Station 304 East Fire Station
Sumner Rural Fire Protection District Station 1
North Bay Rural Fire Protection District
Albany Fire Department Station 4
Marion County Fire District 1 Station 6 Wheatland
Marion County Fire District 1 Station 3 Pratum
Marion County Fire District 1 Station 2 Middle Grove
Marion County Fire District 1 Station 7 Labish Center
Pilot Rock Rural Fire Protection District 7
Hoskins - Kings Valley Rural Fire Protection District
Bandon Rural Fire Protection District Kehl Station
Woodburn Rural Fire Protection District Station 24 Waconda
Sunriver Fire Department
Reedsport Volunteer Fire Department Station 2
Woodburn Rural Fire Protection District Station 25 Broadacres
Woodburn Rural Fire Protection District Station 21 Headquarters
Pendleton City Fire and Ambulance Station 2
Woodburn Rural Fire Protection District Station 22 James Street
Clackamas Fire District Number 1 Station 9 Holcomb
Douglas County Fire District 2 Melrose Station
Springfield Fire Department Station 14
Nestucca Rural Fire Protection District Station 83 Beaver
United States Forest Service Sisters Ranger District
Camas Valley Fire Department Station 2
Southwest Polk County Rural Fire Protection District Station 130
Polk County Fire District 1 Station 70 Pedee
Polk County Fire District 1 Station 40 Buena Vista
Gresham Fire and Emergency Services Station 72
Sheridan Fire District Substation Ballston
Polk County Fire District 1 Station 80
Mosier Rural Fire District Station 2
Sublimity Fire District Station 52 Substation
Columbia River Fire and Rescue Fairgrounds Station
Monitor Rural Fire Protection District Number 73 Yoder Station
Pendleton City Fire and Ambulance Station 3 Airport
Chiloquin Agency Lake Fire District Station 2
Jefferson Rural Fire Protection District Millersburg
Tualatin Valley Fire and Rescue Station 56 Elligsen Road
Lexington Volunteer Fire Department
Mist - Birkenfeld Rural Fire Protection District Peterson Station
Lane County Fire District 1 Station 18 - 2
Lane County Fire District 1 Station 104
Olney - Walluski Volunteer Fire and Rescue District
United States Forest Service - Diamond Lake Ranger District
Sutherlin Fire Department Calapooia Station
Mist - Birkenfeld Rural Fire Protection District
Depoe Bay Rural Fire Protection District Station 2400 - Otter Rock
Goshen Rural Fire Protection District
Douglas County Fire District 2 Headquarters
Gresham Fire and Emergency Services Station 71
Baker Rural Fire Protection District Pocahontas Road
Rural / Metro Fire Department Station 6
Rural / Metro Fire Department Station 4
Rural / Metro Fire Department Station 1
Haines Fire Protection District Muddy Creek Road
Marion County Fire District 1 Station 5 Brooklake
Salem Fire Department Station 8
Elgin Rural Fire Protection District
Union City Fire Department
Scappoose Rural Fire District Holbrook Station
Scappoose Rural Fire Protection District Chapman
Scappoose Rural Fire Protection District Marina
Bandon Rural Fire Protection District Randolph Station
Clatskanie Rural Fire Quincy Station
Columbia River Fire and Rescue Fernhill Station
Columbia River Fire and Rescue - Deer Island Station
Lowell Volunteer Fire Protection District Station 1
Tualatin Valley Fire and Rescue Station 358 Rosemont (historical)
Tualatin Valley Fire and Rescue Station 52 Wilsonville
Tualatin Valley Fire and Rescue Station 59 Willamette
Tualatin Valley Fire and Rescue Station 58 West Linn Bolton
Tualatin Valley Fire and Rescue Station 57 Mountain Road
Tualatin Valley Fire and Rescue Station 66
Crook County Fire and Rescue - Juniper Canyon
Tualatin Valley Fire and Rescue Station 33 Sherwood
Tualatin Valley Fire and Rescue Station 72
Tualatin Valley Fire and Rescue Station 60
Mitchell Volunteer Fire Department
Portland Fire and Rescue Station 16 Sylvan
Portland Fire and Rescue Station 13
Tualatin Valley Fire and Rescue Station 68 Oak Hills
Portland Fire and Rescue Station 31 Rockwood
North Lincoln Fire and Rescue District 1 Station 1300 Otis
Hillsboro Fire and Rescue Station 2 Brookwood
Portland Fire and Rescue Station 30 Gateway
Portland Fire and Rescue Station 15 Portland Heights
Portland Fire and Rescue Station 22 Saint Johns
Portland Fire and Rescue Station 17 Hayden Island
Portland Fire and Rescue Station 20 Sellwood - Moreland
Tualatin Valley Fire and Rescue Station 67 Farmington Road
Winston Dillard Rural Fire Protection District
Salem Fire Department Station 3
Albany Fire Department Station 2
Charleston Rural Fire Protection District Crown Point Station
Joseph Fire Department
Multnomah County Rural Fire Protection District 14 Station 61 Springdale
Hillsboro Fire and Rescue Station 5 Parkwood
Lane County Fire District 1 Station 109
Ione Rural Fire Protection District
Hillsboro Fire and Rescue Station 3 Ronler Acres
Multnomah County Rural Fire Protection District 14 Station 62 Corbett
Yachats Rural Fire Protection District North Station
Sauvie Island Fire Department
Gresham Fire and Emergency Services Station 76
Coquille Fire Department Station 2
Gresham Fire and Emergency Services Station 73
Bend Fire Department Station 303 South Fire Station
Eugene Fire Station 2 Whiteaker Station
Salem Fire Department Station 2
Juniper Flat Rural Fire Protection District
Parkdale Rural Fire Protection District Station 2
Albany Fire Department Station 3
Idanha - Detroit Rural Fire Protection District
Drakes Crossing Rural Fire Protection District
Wallowa Lake fire station
Banks Fire Protection District 13 Buxton Station
Tualatin Valley Fire and Rescue Station 21
Sixes Rural Fire Protection
Marion County Fire District 1 Station 4 Macleay
Echo Rural Fire Protection District Station 1 Headquarters
Jefferson County Fire District 1
Port of Portland Airport Fire Department
Monroe Rural Fire Protection District Station 3
Monroe Rural Fire Protection District Station 2
Alsea Rural Fire Protection District
Corvallis Fire Department Station 3
Corvallis Fire Department Station 2
Adair Rural Fire Protection District Station 1401
Clackamas Fire District Number 1 Station 13 Clarkes
Lake Oswego Fire Department - South Shore
Clackamas Fire District Number 1 Station 4 Lake Road
Clackamas Fire District Number 1 Station 8 Clackamas
Clackamas Fire District Number 1 Station 6 Happy Valley
Clackamas Fire District Number 1 Station 10 Beavercreek
Molalla Rural Fire Protection District 73 Mulino Station
Molalla Rural Fire Protection District 73 Main Station
Estacada Fire District Main Station
Salem Fire Department Station 9
Lake Oswego Fire Department - Westlake
Lake Oswego Fire Department - Jean Road
Clackamas Fire District Number 1 Station 12 Logan
Clackamas Fire District Number 1 Station 11 Redland
Clackamas Fire District Number 1 Milwaukie Station 2
Clackamas Fire District Number 1 Station 3 Oak Grove
Clackamas Fire District Number 1 Station 20 Highland
Hoodland Fire District 74 Government Loop Station
Hoodland Fire District 74 Brightwood Station
Salem Fire Department Station 4
Charleston Rural Fire Protection District Station 1
Banks Fire Protection District 13 Timber Station
Tualatin Valley Fire and Rescue Station 17
Silverton Fire District Station 3 Abiqua
Tualatin Valley Fire and Rescue Station 19
Myrtle Point Fire Department Station 2
Myrtle Point Fire Department Station 3
Coquille Fire Department Station 4
Millington Rural Fire Protection District 5 Station 1
Bridge Rural Fire Department
Charleston Rural Fire Protection District Charleston Station
Dora - Sitkum Rural Fire Protection District
North Bend Fire Department Station 2
North Bend Fire Station 3
Millington Rural Fire Protection District 5 Station 2
Scio Rural Fire Protection District Station 90
Cape Ferrelo Rural Fire Protection District
Ophir Rural Fire Department
Pistol River Rural Fire Protection District
Langlois Rural Fire Protection District
Winchuck Rural Fire Protection District
Cedar Valley Fire Department
Black Butte Ranch Rural Fire Protection District
Multnomah County Rural Fire Protection District 14 Station 63 Aims
Bandon Rural Fire Protection District Main Station
Myrtle Creek Fire Department
North Lincoln Fire and Rescue District 1 Station 1200 Rose Lodge
Lane Rural Fire and Rescue Station 51
North Lincoln Fire and Rescue District 1 Station 1500 Delake
Lane Rural Fire and Rescue Station 52
Lane Rural Fire and Rescue Station 53
North Lincoln Fire and Rescue District 1 Station 1700 Kernville
Siuslaw Valley Fire and Rescue Station 4 Sutton Station
Lake Creek Fire and Rescue
McKenzie Fire and Rescue Station 1 Walterville Station
North Douglas County Fire and Emergency Medical Services Station 6
North Douglas County Fire and Emergency Medical Services Station 5
North Douglas County Fire and Emergency Medical Services Station 4
North Douglas County Fire and Emergency Medical Services Station 2
Redmond Fire and Rescue Station 404
Crook County Fire and Rescue Powell Butte Station
Tualatin Valley Fire and Rescue Station 53 Progress
Tualatin Valley Fire and Rescue Station 65 West Slope
Tualatin Valley Fire and Rescue Station 35 King City
Tualatin Valley Fire and Rescue Cooper Mountain Station 69
Tualatin Valley Fire and Rescue Station 64 Somerset
Sweet Home Fire and Ambulance District Station 23
Tualatin Valley Fire and Rescue Station 62 Aloha
Tualatin Valley Fire and Rescue Station 51 Tigard
Forest Grove Fire and Rescue Gales Creek
Mid - Columbia Fire and Rescue Station 2
Columbia River Fire and Rescue Goble
Mosier Rural Fire District Station 1
La Pine Rural Fire Protection District
Cloverdale Rural Fire Protection District Station 1
La Pine Fire Department Station 103
Mud Flat