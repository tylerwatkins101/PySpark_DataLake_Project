states_dictionary = {'Alabama':'AL', 'Alaska':'AK', 'Arizona':'AZ', 'Arkansas':'AR', 'California':'CA', 'Colorado':'CO', 'Connecticut':'CT',
'Delaware':'DE', 'Florida':'FL', 'Georgia':'GA', 'Hawaii':'HI', 'Idaho':'ID', 'Illinois':'IL', 'Indiana':'IN', 'Iowa':'IA', 'Kansas':'KS',
'Kentucky':'KY', 'Louisiana':'LA', 'Maine':'ME', 'Maryland':'MD', 'Massachusetts':'MA', 'Michigan':'MI', 'Minnesota':'MN',
'Mississippi':'MS', 'Missouri':'MO', 'Montana':'MT', 'Nebraska':'NE', 'Nevada':'NV', 'New Hampshire':'NH', 'New Jersey':'NJ',
'New Mexico':'NM', 'New York':'NY', 'North Carolina':'NC', 'North Dakota':'ND', 'Ohio':'OH', 'Oklahoma':'OK', 'Oregon':'OR',
'Pennsylvania':'PA', 'Rhode Island':'RI', 'South Carolina':'SC', 'South Dakota':'SD', 'Tennessee':'TN', 'Texas':'TX', 'Utah':'UT',
'Vermont':'VT', 'Virginia':'VA', 'Washington':'WA', 'West Virginia':'WV', 'Wisconsin':'WI', 'Wyoming':'WY'}

ports_dictionary = {'ALC':'ALCAN, AK', 'ANC':'ANCHORAGE, AK', 'BAR':'BAKER ISLAND, AK', 'DAC':'DALTONS CACHE, AK',
 'PIZ':'DEW STATION PT LAY DEW, AK', 'DTH':'DUTCH HARBOR, AK', 'EGL':'EAGLE, AK', 'FRB':'FAIRBANKS, AK',
 'HOM':'HOMER, AK', 'HYD':'HYDER, AK', 'JUN':'JUNEAU, AK', '5KE':'KETCHIKAN, AK', 'KET':'KETCHIKAN, AK',
 'MOS':'MOSES POINT INTERMEDIATE, AK', 'NIK':'NIKISKI, AK', 'NOM':'NOM, AK',
 'PKC':'POKER CREEK, AK', 'ORI':'PORT LIONS SPB, AK', 'SKA':'SKAGWAY, AK',
 'SNP':'ST. PAUL ISLAND, AK', 'TKI':'TOKEEN, AK', 'WRA':'WRANGELL, AK',
 'HSV':'MADISON COUNTY - HUNTSVILLE, AL', 'MOB':'MOBILE, AL', 'LIA':'LITTLE ROCK, AR (BPS)',
 'ROG':'ROGERS ARPT, AR', 'DOU':'DOUGLAS, AZ', 'LUK':'LUKEVILLE, AZ',
 'MAP':'MARIPOSA AZ', 'NAC':'NACO, AZ', 'NOG':'NOGALES, AZ',
 'PHO':'PHOENIX, AZ', 'POR':'PORTAL, AZ', 'SLU':'SAN LUIS, AZ', 'SAS':'SASABE, AZ',
 'TUC':'TUCSON, AZ', 'YUI':'YUMA, AZ' , 'AND':'ANDRADE, CA',
 'BUR':'BURBANK, CA', 'CAL':'CALEXICO, CA', 'CAO':'CAMPO, CA' , 'FRE':'FRESNO, CA',
 'ICP':'IMPERIAL COUNTY, CA', 'LNB':'LONG BEACH, CA', 'LOS':'LOS ANGELES, CA', 'BFL':'MEADOWS FIELD - BAKERSFIELD, CA',
 'OAK':'OAKLAND, CA', 'ONT':'ONTARIO, CA', 'OTM':'OTAY MESA, CA', 'BLT':'PACIFIC, HWY. STATION, CA', 'PSP':'PALM SPRINGS, CA',
 'SAC':'SACRAMENTO, CA', 'SLS':'SALINAS, CA (BPS)', 'SDP':'SAN DIEGO, CA', 'SFR':'SAN FRANCISCO, CA', 'SNJ':'SAN JOSE, CA',
 'SLO':'SAN LUIS OBISPO, CA', 'SLI':'SAN LUIS OBISPO, CA (BPS)', 'SPC':'SAN PEDRO, CA', 'SYS':'SAN YSIDRO, CA', 'SAA':'SANTA ANA, CA',
 'STO':'STOCKTON, CA (BPS)', 'TEC':'TECATE, CA', 'TRV':'TRAVIS-AFB, CA', 'APA':'ARAPAHOE COUNTY, CO', 'ASE':'ASPEN, CO #ARPT',
 'COS':'COLORADO SPRINGS, CO', 'DEN':'DENVER, CO', 'DRO':'LA PLATA - DURANGO, CO', 'BDL':'BRADLEY INTERNATIONAL, CT',
 'BGC':'BRIDGEPORT, CT', 'GRT':'GROTON, CT', 'HAR':'HARTFORD, CT', 'NWH':'NEW HAVEN, CT', 'NWL':'NEW LONDON, CT',
 'TST':'NEWINGTON DATA CENTER TEST, CT', 'WAS':'WASHINGTON DC', 'DOV':'DOVER AFB, DE', 'DVD':'DOVER-AFB, DE',
 'WLL':'WILMINGTON, DE', 'BOC':'BOCAGRANDE, FL', 'SRQ':'BRADENTON - SARASOTA, FL', 'CAN':'CAPE CANAVERAL, FL',
 'DAB':'DAYTONA BEACH INTERNATIONAL, FL', 'FRN':'FERNANDINA, FL', 'FTL':'FORT LAUDERDALE, FL', 'FMY':'FORT MYERS, FL',
 'FPF':'FORT PIERCE, FL', 'HUR':'HURLBURT FIELD, FL', 'GNV':'J R ALISON MUNI - GAINESVILLE, FL', 'JAC':'JACKSONVILLE, FL',
 'KEY':'KEY WEST, FL', 'LEE':'LEESBURG MUNICIPAL AIRPORT, FL', 'MLB':'MELBOURNE, FL', 'MIA':'MIAMI, FL',
 'APF':'NAPLES, FL #ARPT', 'OPF':'OPA LOCKA, FL', 'ORL':'ORLANDO, FL', 'PAN':'PANAMA CITY, FL',
 'PEN':'PENSACOLA, FL', 'PCF':'PORT CANAVERAL, FL', 'PEV':'PORT EVERGLADES, FL', 'PSJ':'PORT ST JOE, FL',
 'SFB':'SANFORD, FL', 'SGJ':'ST AUGUSTINE ARPT, FL', 'SAU':'ST AUGUSTINE, FL', 'FPR':'ST LUCIE COUNTY, FL',
 'SPE':'ST PETERSBURG, FL', 'TAM':'TAMPA, FL', 'WPB':'WEST PALM BEACH, FL', 'ATL':'ATLANTA, GA',
 'BRU':'BRUNSWICK, GA', 'AGS':'BUSH FIELD - AUGUSTA, GA', 'SAV':'SAVANNAH, GA', 'AGA':'AGANA, GU',
 'HHW':'HONOLULU, HI', 'OGG':'KAHULUI - MAUI, HI', 'KOA':'KEAHOLE-KONA, HI', 'LIH':'LIHUE, HI',
 'CID':'CEDAR RAPIDS/IOWA CITY, IA', 'DSM':'DES MOINES, IA', 'BOI':'AIR TERM. (GOWEN FLD) BOISE, ID', 'EPI':'EASTPORT, ID',
 'IDA':'FANNING FIELD - IDAHO FALLS, ID', 'PTL':'PORTHILL, ID', 'SPI':'CAPITAL - SPRINGFIELD, IL', 'CHI':'CHICAGO, IL',
 'DPA':'DUPAGE COUNTY, IL', 'PIA':'GREATER PEORIA, IL', 'RFD':'GREATER ROCKFORD, IL', 'UGN':'MEMORIAL - WAUKEGAN, IL',
 'GAR':'GARY, IN', 'HMM':'HAMMOND, IN', 'INP':'INDIANAPOLIS, IN', 'MRL':'MERRILLVILLE, IN', 'SBN':'SOUTH BEND, IN',
 'ICT':'MID-CONTINENT - WITCHITA, KS', 'LEX':'BLUE GRASS - LEXINGTON, KY', 'LOU':'LOUISVILLE, KY', 'BTN':'BATON ROUGE, LA',
 'LKC':'LAKE CHARLES, LA', 'LAK':'LAKE CHARLES, LA (BPS)', 'MLU':'MONROE, LA', 'MGC':'MORGAN CITY, LA', 'NOL':'NEW ORLEANS, LA',
 'BOS':'BOSTON, MA', 'GLO':'GLOUCESTER, MA', 'BED':'HANSCOM FIELD - BEDFORD, MA', 'LYN':'LYNDEN, WA',
 'ADW':'ANDREWS AFB, MD', 'BAL':'BALTIMORE, MD', 'MKG':'MUSKEGON, MD', 'PAX':'PATUXENT RIVER, MD',
 'BGM':'BANGOR, ME', 'BOO':'BOOTHBAY HARBOR, ME', 'BWM':'BRIDGEWATER, ME', 'BCK':'BUCKPORT, ME',
 'CLS':'CALAIS, ME', 'CRB':'CARIBOU, ME', 'COB':'COBURN GORE, ME', 'EST':'EASTCOURT, ME         ',
 'EPT':'EASTPORT MUNICIPAL, ME', 'EPM':'EASTPORT, ME', 'FOR':'FOREST CITY, ME', 'FTF':'FORT FAIRFIELD, ME',
 'FTK':'FORT KENT, ME', 'HML':'HAMIIN, ME', 'HTM':'HOULTON, ME', 'JKM':'JACKMAN, ME',
 'KAL':'KALISPEL, MT', 'LIM':'LIMESTONE, ME', 'LUB':'LUBEC, ME', 'MAD':'MADAWASKA, ME',
 'POM':'PORTLAND, ME', 'RGM':'RANGELEY, ME (BPS)', 'SBR':'SOUTH BREWER, ME',
 'SRL':'ST AURELIE, ME', 'SPA':'ST PAMPILE, ME', 'VNB':'VAN BUREN, ME', 'VCB':'VANCEBORO, ME',
 'AGN':'ALGONAC, MI', 'ALP':'ALPENA, MI', 'BCY':'BAY CITY, MI', 'DET':'DETROIT, MI',
 'GRP':'GRAND RAPIDS, MI', 'GRO':'GROSSE ISLE, MI', 'ISL':'ISLE ROYALE, MI', 'MRC':'MARINE CITY, MI',
 'MRY':'MARYSVILLE, MI', 'PTK':'OAKLAND COUNTY - PONTIAC, MI', 'PHU':'PORT HURON, MI', 'RBT':'ROBERTS LANDING, MI',
 'SAG':'SAGINAW, MI', 'LAN':'LANCASTER, MN', 'MSP':'MINN./ST PAUL, MN', 'LIN':'NORTHERN SVC CENTER, MN',
 'NOY':'NOYES, MN', 'ROS':'ROSEAU, MN', 'SPM':'ST PAUL, MN', 'WSB':'WARROAD INTL, SPB, MN',
 'WAR':'WARROAD, MN', 'KAN':'KANSAS CITY, MO', 'SGF':'SPRINGFIELD-BRANSON, MO', 'STL':'ST LOUIS, MO',
 'WHI':'WHITETAIL, MT', 'CLT':'CHARLOTTE, NC', 'FAY':'FAYETTEVILLE, NC', 'MRH':'MOREHEAD CITY, NC','FOP':'MORRIS FIELDS AAF, NC',
 'GSO':'PIEDMONT TRIAD INTL AIRPORT, NC', 'RDU':'RALEIGH/DURHAM, NC', 'GRF':'GRAND FORKS, ND', 'WND':'WILLISTON, ND',
 'OMA':'OMAHA, NE ', 'LEB':'LEBANON, NH', 'MHT':'MANCHESTER, NH', 'PNH':'PITTSBURG, NH', 'PSM':'PORTSMOUTH, NH',
 'BYO':'BAYONNE, NJ', 'CNJ':'CAMDEN, NJ','HOB':'HOBOKEN, NJ', 'JER':'JERSEY CITY, NJ',
 'WRI':'MC GUIRE AFB - WRIGHTSOWN, NJ', 'MMU':'MORRISTOWN, NJ', 'NEW':'NEWARK/TETERBORO, NJ', 'PER':'PERTH AMBOY, NJ',
 'ACY':'POMONA FIELD - ATLANTIC CITY, NJ', 'ALA':'ALAMAGORDO, NM (BPS)', 'ABQ':'ALBUQUERQUE, NM', 'LVG':'LAS VEGAS, NV',
 'REN':'RENO, NV', 'ALB':'ALBANY, NY', 'AXB':'ALEXANDRIA BAY, NY', 'BUF':'BUFFALO, NY',
 'LAG':'LA GUARDIA, NY', 'LEW':'LEWISTON, NY', 'MAS':'MASSENA, NY', 'NYC':'NEW YORK, NY', 'ROC':'ROCHESTER, NY',
 'SYR':'SYRACUSE, NY', 'AKR':'AKRON, OH', 'ATB':'ASHTABULA, OH', 'CIN':'CINCINNATI, OH', 'CLE':'CLEVELAND, OH',
 'CLM':'COLUMBUS, OH','TOL':'TOLEDO, OH', 'OKC':'OKLAHOMA CITY, OK', 'TUL':'TULSA, OK', 'AST':'ASTORIA, OR',
 'POO':'PORTLAND, OR', 'MDT':'HARRISBURG, PA', 'HSB':'HARRISONBURG, PA', 'PHI':'PHILADELPHIA, PA',
 'PIT':'PITTSBURG, PA', 'PRO':'PROVIDENCE, RI', 'PVD':'THEODORE FRANCIS - WARWICK, RI', 'CHL':'CHARLESTON, SC',
 'CAE':'COLUMBIA, SC #ARPT', 'GEO':'GEORGETOWN, SC', 'MYR':'MYRTLE BEACH, SC', 'SPF':'BLACK HILLS, SPEARFISH, SD',
 'HON':'HOWES REGIONAL ARPT - HURON, SD', 'MEM':'MEMPHIS, TN', 'NSV':'NASHVILLE, TN', 'AUS':'AUSTIN, TX',
 'CRP':'CORPUS CHRISTI, TX', 'DAL':'DALLAS, TX', 'DLR':'DEL RIO, TX', 'DNA':'DONNA, TX', 'EGP':'EAGLE PASS, TX',
 'ELP':'EL PASO, TX', 'FAB':'FABENS, TX', 'FAL':'FALCON HEIGHTS, TX', 'FTH':'FORT HANCOCK, TX',
 'AFW':'FORT WORTH ALLIANCE, TX', 'FPT':'FREEPORT, TX', 'GAL':'GALVESTON, TX', 'HOU':'HOUSTON, TX',
 'SGR':'HULL FIELD, SUGAR LAND ARPT, TX',
 'LLB':'JUAREZ-LINCOLN BRIDGE, TX', 'LCB':'LAREDO COLUMBIA BRIDGE, TX', 'LRN':'LAREDO NORTH, TX', 'LAR':'LAREDO, TX',
 'RIO':'RIO GRANDE CITY, TX', 'ROM':'ROMA, TX', 'SNA':'SAN ANTONIO, TX', 'SNN':'SANDERSON, TX', 'VIB':'VETERAN INTL BRIDGE, TX',
 'YSL':'YSLETA, TX', 'SLC':'SALT LAKE CITY, UT', 'CHO':'ALBEMARLE CHARLOTTESVILLE, VA', 'DAA':'DAVISON AAF - FAIRFAX CNTY, VA',
 'HOP':'HOPEWELL, VA', 'HEF':'MANASSAS, VA #ARPT', 'NWN':'NEWPORT, VA', 'NOR':'NORFOLK, VA', 'RCM':'RICHMOND, VA',
 'ABS':'ALBURG SPRINGS, VT', 'ABG':'ALBURG, VT', 'BEB':'BEEBE PLAIN, VT', 'BEE':'BEECHER FALLS, VT', 'BRG':'BURLINGTON, VT',
 'CNA':'CANAAN, VT', 'DER':'DERBY LINE, VT (I-91) ', 'DLV':'DERBY LINE, VT (RT. 5)', 'ERC':'EAST RICHFORD, VT',
 'HIG':'HIGHGATE SPRINGS, VT', 'MOR':'MORSES LINE, VT', 'NPV':'NEWPORT, VT', 'NRT':'NORTH TROY, VT',
 'NRN':'NORTON, VT', 'PIV':'PINNACLE ROAD, VT', 'RIF':'RICHFORT, VT', 'STA':'ST ALBANS, VT',
 'SWB':'SWANTON, VT (BP - SECTOR HQ)', 'WBE':'WEST BERKSHIRE, VT', 'ABE':'ABERDEEN, WA', 'ANA':'ANACORTES, WA',
 'BEL':'BELLINGHAM, WA', 'BLI':'BELLINGHAM, WASHINGTON #INTL',
 'BLA':'BLAINE, WA', 'BWA':'BOUNDARY, WA', 'CUR':'CURLEW, WA (BPS)', 'DVL':'DANVILLE, WA',
 'EVE':'EVERETT, WA', 'FER':'FERRY, WA', 'FRI':'FRIDAY HARBOR, WA', 'FWA':'FRONTIER, WA', 'KLM':'KALAMA, WA',
 'LAU':'LAURIER, WA', 'LON':'LONGVIEW, WA', 'MET':'METALINE FALLS, WA', 'MWH':'MOSES LAKE GRANT COUNTY ARPT, WA',
 'NEA':'NEAH BAY, WA', 'NIG':'NIGHTHAWK, WA', 'OLY':'OLYMPIA, WA', 'ORO':'OROVILLE, WA',
 'PWB':'PASCO, WA', 'PIR':'POINT ROBERTS, WA', 'PNG':'PORT ANGELES, WA', 'PTO':'PORT TOWNSEND, WA', 'SEA':'SEATTLE, WA',
 'SPO':'SPOKANE, WA', 'SUM':'SUMAS, WA', 'TAC':'TACOMA, WA', 'PSC':'TRI-CITIES - PASCO, WA',
 'VAN':'VANCOUVER, WA', 'AGM':'ALGOMA, WI', 'BAY':'BAYFIELD, WI', 'GRB':'GREEN BAY, WI', 'MNW':'MANITOWOC, WI',
 'MIL':'MILWAUKEE, WI', 'MSN':'TRUAX FIELD - DANE COUNTY, WI', 'CHS':'CHARLESTON, WV', 'CLK':'CLARKSBURG, WV',
 'BLF':'MERCER COUNTY, WV', 'CSP':'CASPER, WY'}