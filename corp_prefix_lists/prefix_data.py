#!/usr/bin/env python3

import os.path
from jsii import Number
import yaml

# Prefix Name must match the YAML file name without the .yaml extension

class PrefixData():
  def __init__(self, prefix_name: str, **kwargs) -> None:
    self.PREFIX_LIST_MAX_ENTRIES_LIMIT = 1000
    self.PREFIX_LIST_MAX_ENTRIES_DEFAULT = 20
    CIDR_DIR = 'cidr_ranges'
    DIRNAME = os.path.dirname(__file__)
    file_path = os.path.join(DIRNAME, CIDR_DIR, '{0}{1}'.format(prefix_name, '.yaml'))
    self.cidr_ranges = []
    self.prefix_name = prefix_name
    self.size = self.PREFIX_LIST_MAX_ENTRIES_DEFAULT
    with open(file_path, 'r') as file_descriptor:
      data = yaml.safe_load(file_descriptor.read())
      self.cidr_ranges = data.get('ranges')
      self.size = int(data.get('max_entries'))
    REQUIRED_KEYS = ['cidr', 'description']
    for range in self.cidr_ranges:
      for key in REQUIRED_KEYS:
        if key not in range.keys():
          raise ValueError('Prefix List Entries require the key: {0}'.format(key))
    
  @property
  def entries(self):
    return self.cidr_ranges

  @property
  def name(self):
    return self.prefix_name

  @property
  def max_entries(self):
    return self.size

  @max_entries.setter
  def max_entries(self, max_entries: int):
    if max_entries > self.PREFIX_LIST_MAX_ENTRIES_LIMIT:
      raise ValueError('The max_entries size limit of {0} has been exceeded.'.format(
        self.PREFIX_LIST_MAX_ENTRIES_LIMIT
      ))
    self.size = max_entries

if __name__ == '__main__':
  prefix = PrefixData(prefix_name='corp_vpn_ranges')
  prefix.max_entries = 20
  print(prefix.max_entries)
  for range in prefix.entries:
    print(range)