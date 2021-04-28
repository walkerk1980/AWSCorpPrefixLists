from aws_cdk import core as cdk

class CorpPrefixListsStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, props: dict, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
