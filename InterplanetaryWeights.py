import pickle
dictWeightDictionary = {
  "Mercury": 0.38,
  "Venus": 0.91,
  "Moon": 0.165,
  "Mars": 0.38,
  "Jupiter": 2.34,
  "Saturn": 0.93,
  "Uranus": 0.92,
  "Neptune": 1.12,
  "Pluto": 0.066
}
dictPlanetHist = {}
eof = False
def pickleFile():
  eof = False
  try:
    jdPlanetaryWeights = open('jdPlanetaryWeights.db', 'rb')
    while not eof:
      try:
        dictPlanetHist = pickle.load(jdPlanetaryWeights)
      except EOFError:
        eof = True
      jdPlanetaryWeights.close()
  except FileNotFoundError:
    dictPlanetHist = {}
def main():
  iCheck = 0
  fWeight = 0
  sName = input("What is your name? (enter key to quit)\n")
  if sName == "":
      exit()
  while iCheck != 1:
    try:
      fWeight = float(input("What is your weight?\n"))
      if fWeight >= 0:
        iCheck = 1
      else:
        print("Please enter a positive value.")
    except:
      print("Invalid numeric entry for weight. Please try again.")
  x = 2
  dictPlanetHist.update({sName:fWeight})
  #for key, value in dictWeightDictionary.items():
    #fW = 0
    #fW = fWeight * value
    #dictPlanetHit.append(fW)
    #dictPlanetHist.update({sName:fWeight})
  print(sName + ", here are your weights on our Solar System's Planets are:\n")
  for key, value in dictWeightDictionary.items():
    print(key + " weight = ", float(value) * fWeight)
  print(dictPlanetHist)
main()