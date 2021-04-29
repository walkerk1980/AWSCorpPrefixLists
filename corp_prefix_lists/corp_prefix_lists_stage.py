from aws_cdk import core as cdk
from jsii import Number

from corp_prefix_lists.corp_prefix_lists_stack import CorpPrefixListsStack

class CorpPrefixListsStage(cdk.Stage):

    def __init__(self, scope: cdk.Construct, construct_id: str, props: dict, prefix_name: str, cidr_ranges: list, max_entries: Number, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        CorpPrefixListsStack(
            self,
            'corp-prefix-list-stack',
            props=props,
            prefix_name=prefix_name,
            cidr_ranges=cidr_ranges,
            max_entries=max_entries
        )