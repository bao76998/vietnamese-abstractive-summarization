file = open("/content/control-over-copying/data/valid.Nsummary","w")
with open("/content/control-over-copying/data/valsum.txt","r") as a:
  for i in a.readlines()[:10000]:
    file.write(i)
  file.close();