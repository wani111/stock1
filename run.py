import sys
from multiprocessing import Pool  # Pool import하기
from balancesheet_itooza import *

def run_multiprocess(lists):
  if len(sys.argv) == 2:
    process = int(sys.argv[1])
  else:
    process = 8

  print(f'Working Process is {process}')
  pool = Pool(processes=process)
  try:
      pool.map(MakeDataStorage, lists)
      # print(f'1 {DataList}')
  except Exception as e:
      print(e)
      sys.exit(1)


  pool.close()
  pool.join()