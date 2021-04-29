from aws_cdk import core as cdk

from aws_cdk import (
    aws_ec2 as ec2,
    aws_ram as ram,
    aws_iam as iam
)
from jsii import Number
class CorpPrefixListsStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, props: dict, prefix_name: str, cidr_ranges: list, max_entries: Number, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        prefix_list = ec2.CfnPrefixList(
            self,
            'prefix-list',
            prefix_list_name='{0}-{1}'.format(props['BUSINESS_UNIT'], prefix_name),
            address_family='IPv4',
            max_entries=max_entries,
            entries=cidr_ranges
        )

        if props.get('SHARE_WITH_ORG_ARN'):
            prefix_list_share = ram.CfnResourceShare(
                self,
                'prefix-list-share',
                name='{0}-{1}'.format(props['BUSINESS_UNIT'], prefix_name),
                resource_arns=[prefix_list.attr_arn],
                principals=[props['SHARE_WITH_ORG_ARN']],
                allow_external_principals=False
            )
