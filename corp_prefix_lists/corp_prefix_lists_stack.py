from aws_cdk import core as cdk

from aws_cdk import (
    aws_ec2 as ec2
)
from jsii import Number
class CorpPrefixListsStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, props: dict, prefix_name: str, cidr_ranges: list, max_entries: Number, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        prefix_list = ec2.CfnPrefixList(
            self,
            'prefix-list',
            prefix_list_name=prefix_name,
            address_family='IPv4',
            max_entries=max_entries,
            entries=cidr_ranges
        )
