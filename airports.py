import numpy as np
import pandas as pd

#read in data
airport_regionsDF = pd.read_csv("AirportRegions.csv")
pax_demandDF = pd.read_csv("PaxDemand.csv")
pax_demand_distDF = pd.read_csv("PaxDemandDist.csv")
ticket_pricesDF = pd.read_csv("TicketPrices.csv")
zip2_regionsDF = pd.read_csv("Zip2Regions.csv")

airport_regions_groupedDF = airport_regionsDF.groupby("Region").size()
#pd.DataFrame(airport_regions_groupedDF).to_csv("test.csv")
print("Number of aiports per region:")
print(pd.DataFrame(airport_regions_groupedDF))
