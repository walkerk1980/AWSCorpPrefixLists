import os.path
import json

from aws_cdk import core as cdk

from aws_cdk import(
    aws_codecommit as codecommit,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions,
    pipelines
)

from corp_prefix_lists.corp_prefix_lists_stage import CorpPrefixListsStage
from corp_prefix_lists.prefix_data import PrefixData

class DeploymentPipelineStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, props: dict, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        BUSINESS_UNIT = self.node.try_get_context('BUSINESS_UNIT')
        APP_NAME = self.node.try_get_context('APP_NAME')

        dirname = os.path.dirname(__file__)
        
        cloud_assembly_artifact = codepipeline.Artifact('cloud_assembly_artifact')

        source_artifact = codepipeline.Artifact('source')

        codecommit_repo = codecommit.Repository.from_repository_arn(
            self,
            'source-repo',
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

        deployment_pipeline = pipelines.CdkPipeline(
            self,
            'deployment-pipeline',
            cloud_assembly_artifact=cloud_assembly_artifact,
            source_action=source_action,
            synth_action=synth_action
        )

        # These names passed to the class must match the file name
        # without the .yaml prefix
        prefix_lists = []
        for prefix_list_name in props['PREFIX_LIST_NAMES']:
            prefix_lists.append(PrefixData(prefix_list_name))

        for prefix_list in prefix_lists:
            list_stage = CorpPrefixListsStage(
                self,
                '{0}-stage-{1}'.format(prefix_list.name, 'home-region').replace('_','-'),
                props=props,
                prefix_name=prefix_list.name,
                cidr_ranges=prefix_list.entries,
                max_entries=prefix_list.max_entries
            )
            deployment_pipeline.add_application_stage(list_stage)
            for region in props['ADDITIONAL_REGIONS']:
                cross_region_list_stage = CorpPrefixListsStage(
                    self,
                    '{0}-stage-{1}'.format(prefix_list.name, region).replace('_','-'),
                    props=props,
                    prefix_name=prefix_list.name,
                    cidr_ranges=prefix_list.entries,
                    max_entries=prefix_list.max_entries,
                    env={'region': region}
                )
                deployment_pipeline.add_application_stage(cross_region_list_stage)
