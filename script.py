
import configparser
# import os
import re

def parse_sensor_data(data):
  ignor = [0b00000001, 0b00000010, 0b00000100]
  if data in ignor:
      return "No issues detected"
  elif data == 0b00000000:
      return "Unknown value"
  else:
      return "issues detected"


 
def check_sonsers():
  import configparser
  import os
# Create a ConfigParser object
  config = configparser.ConfigParser()
# Read the INI file
  config.read('config.ini')
# Access the values in the INI file(sensor 1)
  data_0_s1 = config['data_sensor_1']['data0']#0b00000001
  data_1_s1 = config['data_sensor_1']['data1']
  data_2_s1 = config['data_sensor_1']['data2']
# Access the values in the INI file(sensor 1)
  data_0_s2 = config['data_sensor_1']['data0']#0b00000001
  data_1_s2 = config['data_sensor_1']['data1']
  data_2_s2 = config['data_sensor_1']['data2']
  data0_int_s1 = int(data_0_s1.replace("0b", ""),2)
  data0_int_s2 = int(data_0_s2.replace("0b", ""),2)
  data1_int_s1 = int(data_1_s1.replace("0b", ""),2)
  data1_int_s2 = int(data_1_s2.replace("0b", ""),2)
  data2_int_s1 = int(data_2_s1.replace("0b", ""),2)
  data2_int_s2 = int(data_2_s2.replace("0b", ""),2)
  formatted_result_l =bin(data0_int_s1 + data0_int_s2)
  result_l= "{:08b}".format(int(formatted_result_l, 2))
  formatted_result_r =bin(data1_int_s1 + data1_int_s2)
  result_r = "{:08b}".format(int(formatted_result_r, 2))
  formatted_result_b =bin(data2_int_s1 + data2_int_s2)
  result_b = "{:08b}".format(int(formatted_result_b, 2))
  l=formatted_result_r >> 1
  return(result_l,result_r,result_b,l)

################################

def check_sonsers_rst(result_l,result_r,result_b):
  
  config = configparser.ConfigParser()
# Read the INI file
  config.read('config_lrb.ini')
  data_0_F = config['data_sensor_lrb']['dataF0']
  data0_int_F = int(data_0_F.replace("0b", ""),2)
  formatted_result_F =bin(data0_int_F)
  result_F= "{:08b}".format(int(formatted_result_F, 2))
  Qualifier=parse_sensor_data(result_F)
  return ( result_F)