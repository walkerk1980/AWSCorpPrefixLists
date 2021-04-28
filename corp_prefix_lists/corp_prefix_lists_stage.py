from aws_cdk import core as cdk

from corp_prefix_lists.corp_prefix_lists_stack import CorpPrefixListsStack

class CorpPrefixListsStage(cdk.Stage):

    def __init__(self, scope: cdk.Construct, construct_id: str, props: dict, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        CorpPrefixListsStack(
            self,
            'corp-prefix-list-stack',
            props=props
        )