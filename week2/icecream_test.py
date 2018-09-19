icecreamDict = {	
					"id" : 0,
					"flavor" : "rocky road", 
					"color" : "brownish",
					"calories" : 500,
					"scoops" : [1,3,4],
				}

print (icecreamDict ["scoops"])

customers = [
 {	
	"orderRockyRoad": True,
	"success": 0.5,
 },
 {
	"orderRockyRoad": True,
	"success": 1.0,
 }
]

print (customers)

avgSuccess = (customers[0] ["success"] + customers[1] ["success"])/2

print (avgSuccess)