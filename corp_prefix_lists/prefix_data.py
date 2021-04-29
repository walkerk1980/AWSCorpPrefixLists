#!/usr/bin/env python3

import os.path
from jsii import Number
import yaml

# Prefix Name must match the YAML file name without the .yaml extension

class PrefixData():
    def __init__(self, prefix_name: str, **kwargs) -> None:
      CIDR_DIR = 'cidr_ranges'
      DIRNAME = os.path.dirname(__file__)
      file_path = os.path.join(DIRNAME, CIDR_DIR, '{0}{1}'.format(prefix_name, '.yaml'))
      self.cidr_ranges = []
      self.prefix_name = prefix_name
      self.size = 20
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

if __name__ == '__main__':
  prefix = PrefixData(prefix_name='corp_vpn_ranges')
  for range in prefix.entries:
    print(range)