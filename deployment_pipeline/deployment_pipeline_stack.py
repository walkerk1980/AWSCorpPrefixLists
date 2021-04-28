import os.path
import json

from aws_cdk import core as cdk

from aws_cdk import(
    aws_codecommit as codecommit,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions,
    pipelines
)

from deployment_pipeline.version_control_stack import VersionControlStack

class DeploymentPipelineStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, props: dict, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        BUSINESS_UNIT = self.node.try_get_context('BUSINESS_UNIT')
        APP_NAME = self.node.try_get_context('APP_NAME')

        dirname = os.path.dirname(__file__)
        
        cloud_assembly_artifact = codepipeline.Artifact('cloud_assembly_artifact')

        version_control_stack = VersionControlStack(
            self,
            construct_id='{0}-{1}-version-control'.format(BUSINESS_UNIT, APP_NAME),
            props=props
        )
        props = version_control_stack.output_props
        source_artifact = codepipeline.Artifact('source')

        codecommit_repo = codecommit.Repository.from_repository_arn(
            self,
            'source_repo',
            repository_arn=props['repository_arn']
        )

        source_action = codepipeline_actions.CodeCommitSourceAction(
            action_name='Source',
            branch='main',
            repository=codecommit_repo,
            output=source_artifact
        )
        
        synth_action = pipelines.SimpleSynthAction(
            install_commands=[
                'npm install -g aws-cdk',
                'pip install --upgrade -r requirements.txt'
            ],
            synth_command='cdk synth',
            cloud_assembly_artifact=cloud_assembly_artifact,
            source_artifact=source_artifact
        )