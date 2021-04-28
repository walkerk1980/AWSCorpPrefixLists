import os.path
import json
from sys import platform

from aws_cdk import (
    aws_codecommit as codecommit,
    core
)

class VersionControlStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, props: dict, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        dirname = os.path.dirname(__file__)

        codecommit_repo = codecommit.Repository.from_repository_name(
            self,
            'codecommit_repo',
            repository_name='{0}-{1}'.format(
                props['BUSINESS_UNIT'],
                props['APP_NAME']
            )
        )

        # Prepares output attributes to be passed into other stacks
        self.output_props = props.copy()
        self.output_props['repository_clone_url_http'] = codecommit_repo.repository_clone_url_http
        self.output_props['repository_arn'] = codecommit_repo.repository_arn

        # @property
        # def outputs(self):
        #     return self.output_props