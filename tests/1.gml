graph [
  node [
    id 0
    label "HARVARD"
    Country "United States"
    Longitude 15
    Internal 1
    Latitude 65
  ]
  node [
    id 1
    label "SRI"
    Country "United States"
    Longitude 55
    Internal 1
    Latitude 60
  ]
  node [
    id 2
    label "UCSB"
    Country "United States"
    Longitude 50
    Internal 1
    Latitude 90
  ]
  node [
    id 3
    label "UCLA"
    Country "United States"
    Longitude 10
    Internal 1
    Latitude 85
  ]
  edge [
    source 0
    target 1
    id "e9"
  ]
  edge [
    source 0
    target 2
    id "e0"
  ]
  edge [
    source 0
    target 3
    id "e1"
  ]
  edge [
    source 1
    target 2
    id "e2"
  ]
  edge [
    source 2
    target 3
    id "e3"
  ]
]
