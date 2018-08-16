'''
Just a few examples of how to do some
basic things with the PLC
'''
from eip import PLC

def ex_read(tag):
  '''
  simple tag read
  '''
  ret = comm.Read(tag)
  print ret

def ex_readArray(tag, length):
  '''
  read tag array
  '''
  ret = comm.Read(tag, length)
  print ret

def ex_multiRead():
  '''
  read multiple tags in a single packet
  '''
  tag1 = "DatabasePointer"
  tag2 = "ProductPointer"
  ret = comm.MultiRead(tag1, tag2)
  print ret
  
def ex_write(tag, value):
  '''
  simple tag write
  '''
  comm.Write(tag, value)

def ex_getPLCTime():
  '''
  get the PLC's clock time
  '''
  ret = comm.GetPLCTime()
  print ret
  
def ex_setPLCTime():
    '''
    set the PLC's clock time to the workstations time
    '''
    comm.SetPLCTime()

def ex_discover():
  '''
  discover all the Ethernet I/P devices on the network and print the
  results
  '''
  print "Discovering Ethernet I/P devices, please wait..."
  device = comm.Discover()
  print "Total number of devices found (in no particular order):", len(device)
  print ""

  i = 0
  for device in devices:
    i = i + 1
    print( "({}) {}".format(i, device.IPAddress))
    print("     ProductName/Code - {} ({})".format(device.ProductName, device.ProductCode))
    print("     Vendor/DeviceID  - {} ({})".format(device.Vendor, device.DeviceID))
    print("     Revision/Serial  - {}, {}".format(device.Revision, device.SerialNumber))
    print()

def ex_getTags():
  '''
  request the tag database from the PLC and put the results in a text file
  '''
  ret = comm.GetTagList()

  if ret is None: return

  # print out all the tags to a file
  with open("TagList.txt", "w") as text_file: 
    for tag in ret:
      name = "Name: {:60}".format(tag.TagName)
      dtype = "Type: {:4}-{:5} | ".format(tag.DataType, tag.DataTypeStr)
      offset= "Offset: {:3} |".format(tag.Offset)
    
      line = name + tabs + dtype + offset 
      text_file.write(line)
    
# define our communication
comm = PLC()
comm.IPAddress = '192.168.1.10'
#comm.ProcessorSlot = 2

# uncomment one of the examples.
#ex_read('NewProductID')
#ex_readArray('ObjectValue[0]', 10)
#ex_multiRead()
#ex_write('ThisTag.Thingy', '107')
#ex_getPLCTime()
#ex_setPLCTime()
#ex_discover()
#ex_getTags()
