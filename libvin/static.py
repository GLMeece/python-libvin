WORLD_MANUFACTURER_REGIONS = {
    'africa': 'ABCDEFGH',
    'asia': 'JKLMNPR',
    'north_america': '12345',
    'south_america': '89',
    'oceania': '67',
}

WORLD_MANUFACTURER_MAP = {
    
    # AFRICA 

    'A': {'region': 'africa', 'countries': {
          'ABCDEFGH': 'south_africa',
          'JKLMN': 'ivory_coast'}},

    'B': {'region': 'africa', 'countries': {
          'ABCDE': 'angola',
          'FGHIJK': 'kenya',
          'LMNOPQR': 'tanzania'}},

    'C': {'region': 'africa', 'countries': {
          'ABCDE': 'benin',
          'FGHIJK': 'madagascar',
          'LMNOPQR': 'tunisia'}},

    'D': {'region': 'africa', 'countries': {
            'ABCDE': 'egypt',
            'FGHIJK': 'morocco',
            'LMNOPQR': 'zambia'}},

    'E': {'region': 'africa', 'countries': {
            'ABCDE': 'ethiopia',
            'FGHIJK': 'mozambique'}},

    'F': {'region': 'africa', 'countries': {
            'ABCDE': 'ghana',
            'FGHIJK': 'nigeria'}},

    # ASIA

    'J': {'region': 'asia', 'countries': {
            'ABCDEFGHIJKLMNOPQRST': 'Japan'}},

    'K': {'region': 'asia', 'countries': {
            'ABCDE': 'Sri Lanka',
            'FGHIJK': 'Israel',
            'LMNOPQR': 'Korea (South)'}},

    'L': {'region': 'asia', 'countries': {
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890': 'China'}},

    'M': {'region': 'asia', 'countries': {
            'ABCDE': 'India',
            'FGHIJK': 'Indonesia',
            'LMNOPQR': 'Thailand'}},

    'N': {'region': 'asia', 'countries': {
            'ABCDE': 'Philippines',
            'FGHIJK': 'Singapore',
            'LMNOPQR': 'Malaysia'}},

    'P': {'region': 'asia', 'countries': {
            'ABCDE': 'United Arab Emirates',
            'FGHIJK': 'Taiwan',
            'LMNOPQR': 'Vietnam',
            'STUVWXYZ0': 'Saudi Arabia'}},

    # Europe

    'S': {'region': 'europe', 'countries': {
            'ABCDEFGHIJKLM': 'United Kingdom',
            'NOPQRST': 'Germany',
            'UVWXYZ': 'Poland',
            '1234': 'Latvia'}},

    'T': {'region': 'europe', 'countries': {
            'ABCDEFGH': 'Switzerland',
            'JKLMNOP': 'Czech Republic',
            'RSTUV': 'Hungary',
            'WXYZ1234567890': 'Portugal'}},

    'U': {'region': 'europe', 'countries': {
            'HIJKLM': 'Denmark',
            'NOPQRST': 'Ireland',
            'UVWXYZ': 'Romania',
            '567': 'Slovakia'}},

    'V': {'region': 'europe', 'countries': {
            'ABCDE': 'Austria',
            'FGHIJKLMNOPQR': 'France',
            'STUVW': 'Spain',
            'XYZ12': 'Serbia',
            '345': 'Croatia',
            '67890': 'Estonia'}},

    'W': {'region': 'europe', 'countries': {
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890': 'Germany'}},

    'X': {'region': 'europe', 'countries': {
            'ABCDE': 'Bulgaria',
            'FGHIJK': 'Greece',
            'LMNOPQR': 'Netherlands',
            'STUVW': 'USSR',
            'XYZ2': 'Luxembourg',
            '34567890': 'Russia'}},

    'Y': {'region': 'europe', 'countries': {
            'ABCDE': 'Belgium',
            'FGHIJK': 'Finland',
            'LMNOPQR': 'Malta',
            'STUVW': 'Sweden',
            'XYZ12': 'Norway',
            '345': 'Belarus',
            '67890': 'Ukraine'}},

    'Z': {'region': 'europe', 'countries': {
            'ABCDEFGHIJKLMNOPQR': 'Italy',
            'STUVW': 'Finland',
            'XYZ12': 'Slovenia',
            '345': 'Lithuania'}},

    # Nort America

    '1': {'region': 'north_america', 'countries': {
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890': 'United States'}},

    '2': {'region': 'north_america', 'countries': {
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890': 'Canada'}},

    '3': {'region': 'north_america', 'countries': {
            'ABCDEFGHIJKLMNOPQRSTUVW': 'Mexico'}},

    '3': {'region': 'north_america', 'countries': {
            'XYZ1234567': 'Costa Rica'}},

    '3': {'region': 'north_america', 'countries': {
            '890': 'Cayman Islands'}},

    '4': {'region': 'north_america', 'countries': {
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890': 'United States'}},

    '5': {'region': 'north_america', 'countries': {
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890': 'United States'}},

    # Oceania

    '6': {'region': 'oceania', 'countries': {
            'ABCDEFGHIJKLMNOPQRSTUVW': 'Australia'}},

    '7': {'region': 'oceania', 'countries': {
            'ABCDE': 'New Zealand'}},

    # South America

    '8': {'region': 'south_america', 'countries': {
            'ABCDE': 'Argentina',
            'FGHIJK': 'Chile',
            'LMNOPQR': 'Ecuador',
            'STUVW': 'Peru',
            'XYZ12': 'Venezuela'}},

    '9': {'region': 'south_america', 'countries': {
            'ABCDE': 'Brazil',
            'FGHIJK': 'Colombia',
            'LMNOPQR': 'Paraguay',
            'STUVW': 'Uruguay',
            'XYZ12': 'Trinidad & Tobago',
            '3456789': 'Brazil'}},

}

YEARS_CODES_PRE_2010 = {
    'A': 1980, 'L': 1990, 'Y': 2000,
    'B': 1981, 'M': 1991, '1': 2001,
    'C': 1982, 'N': 1992, '2': 2002,
    'D': 1983, 'P': 1993, '3': 2003,
    'E': 1984, 'R': 1994, '4': 2004,
    'F': 1985, 'S': 1995, '5': 2005,
    'G': 1986, 'T': 1996, '6': 2006,
    'H': 1987, 'V': 1997, '7': 2007,
    'J': 1988, 'W': 1998, '8': 2008,
    'K': 1989, 'X': 1999, '9': 2009,
}

YEARS_CODES_PRE_2040 = {
    'A': 2010,    'L': 2020, 'Y': 2030,
    'B': 2011,    'M': 2021, '1': 2031,
    'C': 2012,    'N': 2022, '2': 2032,
    'D': 2013,    'P': 2023, '3': 2033,
    'E': 2014,    'R': 2024, '4': 2034,
    'F': 2015,    'S': 2025, '5': 2035,
    'G': 2016,    'T': 2026, '6': 2036,
    'H': 2017,    'V': 2027, '7': 2037,
    'J': 2018,    'W': 2028, '8': 2038,
    'K': 2019,    'X': 2029, '9': 2039,
}

WMI_MAP = {
    'AFA': 'Ford South Africa',
    'AAV': 'Volkswagen South Africa',
    'JA3': 'Mitsubishi',
    'JA': 'Isuzu',
    'JF': 'Fuji Heavy Industries (Subaru)',
    'JHM': 'Honda',
    'JHG': 'Honda',
    'JHL': 'Honda',
    'JK': 'Kawasaki (motorcycles)',
    'JM': 'Mazda',
    'JN': 'Nissan',
    'JS': 'Suzuki',
    'JT': 'Toyota',
    'KL': 'Daewoo General Motors South Korea',
    'KM8': 'Hyundai',
    'KMH': 'Hyundai',
    'KNA': 'Kia',
    'KNB': 'Kia',
    'KNC': 'Kia',
    'KNM': 'Renault Samsung',
    'KPA': 'Ssangyong',
    'KPT': 'Ssangyong',
    'L56': 'Renault Samsung',
    'L5Y': 'Merato Motorcycle Taizhou Zhongneng',
    'LDY': 'Zhongtong Coach, China',
    'LGH': 'Dong Feng (DFM), China',
    'LKL': 'Suzhou King Long, China',
    'LSY': 'Brilliance Zhonghua',
    'LTV': 'Toyota Tian Jin',
    'LVS': 'Ford Chang An',
    'LVV': 'Chery, China',
    'LZM': 'MAN China',
    'LZE': 'Isuzu Guangzhou, China',
    'LZG': 'Shaanxi Automobile Group, China',
    'LZY': 'Yutong Zhengzhou, China',
    'MA1': 'Mahindra',
    'MA3': 'Suzuki India',
    'MA7': 'Honda Siel Cars India',
    'MAL': 'Hyundai',
    'MHR': 'Honda Indonesia',
    'MNB': 'Ford Thailand',
    'MNT': 'Nissan Thailand',
    'MMB': 'Mitsubishi Thailand',
    'MMM': 'Chevrolet Thailand',
    'MMT': 'Mitsubishi Thailand',
    'MM8': 'Mazda Thailand',
    'MPA': 'Isuzu Thailand',
    'MP1': 'Isuzu Thailand',
    'MRH': 'Honda Thailand',
    'MR0': 'Toyota Thailand',
    'NLE': 'Mercedes-Benz Turk Truck',
    'NM0': 'Ford Turkey',
    'NM4': 'Tofas Turk',
    'NMT': 'Toyota Turkiye',
    'PE1': 'Ford Phillipines',
    'PE3': 'Mazda Phillipines',
    'PL1': 'Proton, Malaysia',
    'SAL': 'Land Rover',
    'SAJ': 'Jaguar',
    'SAR': 'Rover',
    'SCA': 'Rolls Royce',
    'SCC': 'Lotus Cars',
    'SCE': 'DeLorean Motor Cars N. Ireland (UK)',
    'SCF': 'Aston',
    'SDB': 'Peugeot UK',
    'SFD': 'Alexander Dennis UK',
    'SHS': 'Honda UK',
    'SJN': 'Nissan UK',
    'SU9': 'Solaris Bus & Coach (Poland)',
    'TK9': 'SOR (Czech Republic)',
    'TDM': 'QUANTYA Swiss Electric Movement (Switzerland)',
    'TMB': 'Skoda (Czech Republic)',
    'TMK': 'Karosa (Czech Republic)',
    'TMP': 'Skoda trolleybuses (Czech Republic)',
    'TMT': 'Tatra (Czech Republic)',
    'TM9': 'Skoda trolleybuses (Czech Republic)',
    'TN9': 'Karosa (Czech Republic)',
    'TRA': 'Ikarus Bus',
    'TRU': 'Audi Hungary',
    'TSE': 'Ikarus Egyedi Autobuszgyar, (Hungary)',
    'TSM': 'Suzuki, (Hungary)',
    'UU1': 'Renault Dacia, (Romania)',
    'VF1': 'Renault',
    'VF3': 'Peugeot',
    'VF6': 'Renault (Trucks & Buses)',
    'VF7': 'Citroen',
    'VF8': 'Matra',
    'VLU': 'Scania France',
    'VNE': 'Irisbus (France)',
    'VSE': 'Suzuki Spain (Santana Motors)',
    'VSK': 'Nissan Spain',
    'VSS': 'SEAT',
    'VSX': 'Opel Spain',
    'VS6': 'Ford Spain',
    'VS9': 'Carrocerias Ayats (Spain)',
    'VWV': 'Volkswagen Spain',
    'VX1': 'Zastava / Yugo Serbia',
    'WAG': 'Neoplan',
    'WAU': 'Audi',
    'WBA': 'BMW',
    'WBS': 'BMW M',
    'WDB': 'Mercedes-Benz',
    'WDC': 'DaimlerChrysler',
    'WDD': 'McLaren',
    'WEB': 'Evobus GmbH (Mercedes-Bus)',
    'WF0': 'Ford Germany',
    'WMA': 'MAN Germany',
    'WMW': 'MINI',
    'WP0': 'Porsche',
    'W0L': 'Opel',
    'WVW': 'Volkswagen',
    'WV1': 'Volkswagen Commercial Vehicles',
    'WV2': 'Volkswagen Bus/Van',
    'XL9': 'Spyker',
    'XMC': 'Mitsubishi (NedCar)',
    'XTA': 'Lada/AutoVaz (Russia)',
    'YK1': 'Saab',
    'YS2': 'Scania AB',
    'YS3': 'Saab',
    'YS4': 'Scania Bus',
    'YV1': 'Volvo Cars',
    'YV4': 'Volvo Cars',
    'YV2': 'Volvo Trucks',
    'YV3': 'Volvo Buses',
    'ZAM': 'Maserati Biturbo',
    'ZAP': 'Piaggio/Vespa/Gilera',
    'ZAR': 'Alfa Romeo',
    'ZCG': 'Cagiva SpA',
    'ZDM': 'Ducati Motor Holdings SpA',
    'ZDF': 'Ferrari Dino',
    'ZD4': 'Aprilia',
    'ZFA': 'Fiat',
    'ZFC': 'Fiat V.I.',
    'ZFF': 'Ferrari',
    'ZHW': 'Lamborghini',
    'ZLA': 'Lancia',
    'ZOM': 'OM',
    '1C3': 'Chrysler',
    '1C6': 'Chrysler',
    '1D3': 'Dodge',
    '1FA': 'Ford Motor Company',
    '1FB': 'Ford Motor Company',
    '1FC': 'Ford Motor Company',
    '1FD': 'Ford Motor Company',
    '1FM': 'Ford Motor Company',
    '1FT': 'Ford Motor Company',
    '1FU': 'Freightliner',
    '1FV': 'Freightliner',
    '1F9': 'FWD Corp.',
    '1G': 'General Motors USA',
    '1GC': 'Chevrolet Truck USA',
    '1GT': 'GMC Truck USA',
    '1G1': 'Chevrolet USA',
    '1G2': 'Pontiac USA',
    '1G3': 'Oldsmobile USA',
    '1G4': 'Buick USA',
    '1G6': 'Cadillac USA',
    '1GM': 'Pontiac USA',
    '1G8': 'Saturn USA',
    '1H': 'Honda USA',
    '1HD': 'Harley-Davidson',
    '1J4': 'Jeep',
    '1L': 'Lincoln USA',
    '1ME': 'Mercury USA',
    '1M1': 'Mack Truck USA',
    '1M2': 'Mack Truck USA',
    '1M3': 'Mack Truck USA',
    '1M4': 'Mack Truck USA',
    '1N': 'Nissan USA',
    '1NX': 'NUMMI USA',
    '1P3': 'Plymouth USA',
    '1R9': 'Roadrunner Hay Squeeze USA',
    '1VW': 'Volkswagen USA',
    '1XK': 'Kenworth USA',
    '1XP': 'Peterbilt USA',
    '1YV': 'Mazda USA (AutoAlliance International)',
    '2C3': 'Chrysler Canada',
    '2CN': 'CAMI',
    '2D3': 'Dodge Canada',
    '2FA': 'Ford Motor Company Canada',
    '2FB': 'Ford Motor Company Canada',
    '2FC': 'Ford Motor Company Canada',
    '2FM': 'Ford Motor Company Canada',
    '2FT': 'Ford Motor Company Canada',
    '2FU': 'Freightliner',
    '2FV': 'Freightliner',
    '2FZ': 'Sterling',
    '2G': 'General Motors Canada',
    '2G1': 'Chevrolet Canada',
    '2G2': 'Pontiac Canada',
    '2G3': 'Oldsmobile Canada',
    '2G4': 'Buick Canada',
    '2HG': 'Honda Canada',
    '2HK': 'Honda Canada',
    '2HM': 'Hyundai Canada',
    '2M': 'Mercury',
    '2P3': 'Plymouth Canada',
    '2T': 'Toyota Canada',
    '2V4': 'Volkswagen Canada',
    '2WK': 'Western Star',
    '2WL': 'Western Star',
    '2WM': 'Western Star',
    '3D3': 'Dodge Mexico',
    '3FA': 'Ford Motor Company Mexico',
    '3FE': 'Ford Motor Company Mexico',
    '3G': 'General Motors Mexico',
    '3H': 'Honda Mexico',
    '3N': 'Nissan Mexico',
    '3P3': 'Plymouth Mexico',
    '3VW': 'Volkswagen Mexico',
    '4F': 'Mazda USA',
    '4M': 'Mercury',
    '4S': 'Subaru-Isuzu Automotive',
    '4T': 'Toyota',
    '4US': 'BMW USA',
    '4UZ': 'Frt-Thomas Bus',
    '4V1': 'Volvo',
    '4V2': 'Volvo',
    '4V3': 'Volvo',
    '4V4': 'Volvo',
    '4V5': 'Volvo',
    '4V6': 'Volvo',
    '4VL': 'Volvo',
    '4VM': 'Volvo',
    '4VZ': 'Volvo',
    '5F': 'Honda USA-Alabama',
    '5L': 'Lincoln',
    '5N1': 'Nissan USA',
    '5NP': 'Hyundai USA',
    '5T': 'Toyota USA - trucks',
    '6AB': 'MAN Australia',
    '6F4': 'Nissan Motor Company Australia',
    '6F5': 'Kenworth Australia',
    '6FP': 'Ford Motor Company Australia',
    '6G1': 'General Motors-Holden (post Nov 2002)',
    '6G2': 'Pontiac Australia (GTO & G8)',
    '6H8': 'General Motors-Holden (pre Nov 2002)',
    '6MM': 'Mitsubishi Motors Australia',
    '6T1': 'Toyota Motor Corporation Australia',
    '6U9': 'Privately Imported car in Australia',
    '8AG': 'Chevrolet Argentina',
    '8GG': 'Chevrolet Chile',
    '8AP': 'Fiat Argentina',
    '8AF': 'Ford Motor Company Argentina',
    '8AD': 'Peugeot Argentina',
    '8GD': 'Peugeot Chile',
    '8A1': 'Renault Argentina',
    '8AK': 'Suzuki Argentina',
    '8AJ': 'Toyota Argentina',
    '8AW': 'Volkswagen Argentina',
    '93U': 'Audi Brazil',
    '9BG': 'Chevrolet Brazil',
    '935': 'Citroen Brazil',
    '9BD': 'Fiat Brazil',
    '9BF': 'Ford Motor Company Brazil',
    '93H': 'Honda Brazil',
    '9BM': 'Mercedes-Benz Brazil',
    '936': 'Peugeot Brazil',
    '93Y': 'Renault Brazil',
    '9BS': 'Scania Brazil',
    '93R': 'Toyota Brazil',
    '9BW': 'Volkswagen Brazil',
    '9FB': 'Renault Colombia',
    }

VIN_TRANSLATION = {
    'A': 1, 'L': 3, 'Y': 8,
    'B': 2, 'M': 4, 'Z': 9,
    'C': 3, 'N': 5, '1': 1,
    'D': 4, 'P': 7, '2': 2,
    'E': 5, 'R': 9, '3': 3,
    'F': 6, 'S': 2, '4': 4,
    'G': 7, 'T': 3, '5': 5,
    'H': 8, 'V': 5, '6': 6,
    'J': 1, 'W': 6, '7': 7,
    'K': 2, 'X': 7, '8': 8,
    '9': 9, '0': 0
}

VIN_WEIGHT = [8,7,6,5,4,3,2,10,0,9,8,7,6,5,4,3,2]