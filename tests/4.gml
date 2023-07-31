graph [
  DateObtained "19/10/10"
  GeoLocation "Austria"
  GeoExtent "Country"
  Network "ACOnet"
  Provenance "Primary"
  Note "Vienna is unclear - Internal links show which of two internal PoPs they connect to, but external links not clear."
  Source "http://www.aco.net/ueberblick.html?&amp;L=1"
  Version "1.0"
  Type "REN"
  DateType "Historic"
  Backbone 1
  Commercial 0
  label "Aconet"
  ToolsetVersion "0.3.34dev-20120328"
  Customer 0
  IX 0
  SourceGitVersion "e278b1b"
  DateModifier "="
  DateMonth "06"
  LastAccess "19/10/10"
  Access 0
  Layer "IP"
  Creator "Topology Zoo Toolset"
  Developed 0
  Transit 0
  NetworkDate "2009_06"
  DateYear "2009"
  LastProcessed "2011_09_01"
  Testbed 0
  node [
    id 0
    label "Eisenstadt"
    Country "Austria"
    Longitude 16.51667
    Internal 1
    Latitude 45.85
  ]
  node [
    id 1
    label "St. Polten"
    Country "Austria"
    Longitude 15.63333
    Internal 1
    Latitude 50.2
  ]
  node [
    id 2
    label "Graz2"
    Country "Austria"
    Longitude 16.45
    Internal 1
    Latitude 51.06667
  ]
  node [
    id 3
    label "Leoben"
    Country "Austria"
    Longitude 15.1
    Internal 1
    Latitude 45.38333
  ]
  node [
    id 4
    label "Vienna2"
    Country "Austria"
    Longitude 16.37208
    Internal 1
    Latitude 45.20849
  ]
  node [
    id 5
    label "Krems"
    Country "Austria"
    Longitude 15.61415
    Internal 1
    Latitude 50.40921
  ]
  node [
    id 6
    label "Vienna1"
    Country "Austria"
    Longitude 14.37208
    Internal 1
    Latitude 50.20849
  ]
  node [
    id 7
    label "Klagenfurt2"
    Country "Austria"
    Longitude 14.30528
    Internal 1
    Latitude 44.62472
  ]
  node [
    id 8
    label "Graz1"
    Country "Austria"
    Longitude 15.45
    Internal 1
    Latitude 49.06667
  ]
  node [
    id 9
    label "Linz1"
    Country "Austria"
    Longitude 14.28611
    Internal 1
    Latitude 50.30639
  ]
  node [
    id 10
    label "Salzburg2"
    Country "Austria"
    Longitude 13.04399
    Internal 1
    Latitude 49.79941
  ]
  node [
    id 11
    label "Innsbruck1"
    Country "Austria"
    Longitude 11.39454
    Internal 1
    Latitude 49.26266
  ]
  node [
    id 12
    label "Dornbirn"
    Country "Austria"
    Longitude 9.73306
    Internal 1
    Latitude 49.41667
  ]
  edge [
    source 0
    target 4
    LinkLabel "DWDM"
  ]
  edge [
    source 0
    target 7
    LinkLabel "DWDM"
  ]
  edge [
    source 1
    target 6
    LinkType "Ethernet"
    LinkSpeed "1"
    LinkLabel "1G Ethernet"
    LinkSpeedUnits "G"
    LinkSpeedRaw 1000000000.0
  ]
  edge [
    source 1
    target 7
    LinkType "Ethernet"
    LinkSpeed "1"
    LinkLabel "1G Ethernet"
    LinkSpeedUnits "G"
    LinkSpeedRaw 1000000000.0
  ]
  edge [
    source 2
    target 3
    LinkLabel "DWDM"
  ]
  edge [
    source 2
    target 5
    LinkLabel "DWDM"
  ]
  edge [
    source 2
    target 7
    LinkLabel "DWDM"
  ]
  edge [
    source 3
    target 12
    LinkLabel "DWDM"
  ]
  edge [
    source 4
    target 6
    LinkType "Ethernet"
    LinkSpeed "1"
    LinkLabel "1G Ethernet"
    LinkSpeedUnits "G"
    LinkSpeedRaw 1000000000.0
  ]
  edge [
    source 4
    target 7
    id "e25"
  ]
  edge [
    source 4
    target 8
    LinkLabel "DWDM"
  ]
  edge [
    source 4
    target 9
    LinkLabel "DWDM"
  ]
  edge [
    source 4
    target 10
    LinkLabel "DWDM"
  ]
  edge [
    source 4
    target 11
    LinkLabel "DWDM"
  ]
  edge [
    source 4
    target 12
    LinkLabel "DWDM"
  ]
  edge [
    source 5
    target 10
    LinkType "Ethernet"
    LinkSpeed "10"
    LinkLabel "10G Ethernet"
    LinkSpeedUnits "G"
    LinkSpeedRaw 10000000000.0
  ]
  edge [
    source 7
    target 8
    id "e24"
  ]
  edge [
    source 7
    target 9
    LinkLabel "DWDM"
  ]
  edge [
    source 7
    target 10
    LinkLabel "DWDM"
  ]
  edge [
    source 7
    target 11
    LinkLabel "DWDM"
  ]
  edge [
    source 7
    target 12
    LinkLabel "DWDM"
  ]
  edge [
    source 8
    target 10
    LinkType "Ethernet"
    LinkSpeed "10"
    LinkLabel "10G Ethernet"
    LinkSpeedUnits "G"
    LinkSpeedRaw 10000000000.0
  ]
  edge [
    source 9
    target 10
    LinkType "Ethernet"
    LinkSpeed "10"
    LinkLabel "10G Ethernet"
    LinkSpeedUnits "G"
    LinkSpeedRaw 10000000000.0
  ]
  edge [
    source 10
    target 11
    LinkType "Ethernet"
    LinkSpeed "10"
    LinkLabel "10G Ethernet"
    LinkSpeedUnits "G"
    LinkSpeedRaw 10000000000.0
  ]
  edge [
    source 10
    target 12
    LinkType "Ethernet"
    LinkSpeed "10"
    LinkLabel "10G Ethernet"
    LinkSpeedUnits "G"
    LinkSpeedRaw 10000000000.0
  ]
]
