#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

from deployment_pipeline.version_control_stack import VersionControlStack
from deployment_pipeline.deployment_pipeline_stack import DeploymentPipelineStack

app = cdk.App()

# Constants
# Set Constants in cdk.context.json
props = {}
props.update({'BUSINESS_UNIT': app.node.try_get_context('BUSINESS_UNIT')})
props.update({'APP_NAME': app.node.try_get_context('APP_NAME')})
props.update({'PREFIX_LIST_NAMES': app.node.try_get_context('PREFIX_LIST_NAMES')})
props.update({'SHARE_WITH_ORG_ARN': app.node.try_get_context('SHARE_WITH_ORG_ARN')})
props.update({'DEPLOYMENT_REGION': app.node.try_get_context('DEPLOYMENT_REGION')})
props.update({'ADDITIONAL_REGIONS': app.node.try_get_context('ADDITIONAL_REGIONS')})

PIPELINE_ENV = {
    'account': os.environ["CDK_DEFAULT_ACCOUNT"],
    'region': props['DEPLOYMENT_REGION']
}

version_control_stack = VersionControlStack(
    app,
    construct_id='{0}-{1}-version-control'.format(props['BUSINESS_UNIT'], props['APP_NAME']),
    props=props,
    env=PIPELINE_ENV
)
props = version_control_stack.output_props

deployment_pipeline_stack = DeploymentPipelineStack(
    app,
    construct_id='{0}-{1}-deployment-pipeline'.format(props['BUSINESS_UNIT'], props['APP_NAME']),
    props=props,
    env=PIPELINE_ENV
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=core.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=core.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )
deployment_pipeline_stack.add_dependency(version_control_stack)

app.synth()