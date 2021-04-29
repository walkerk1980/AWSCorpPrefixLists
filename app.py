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
props.update({'ACCEPTANCE_TEST_EMAILS': app.node.try_get_context('ACCEPTANCE_TEST_EMAILS')})
props.update({'SHARE_WITH_ORG_ID': app.node.try_get_context('SHARE_WITH_ORG_ID')})

version_control_stack = VersionControlStack(
    app,
    construct_id='{0}-{1}-version-control'.format(props['BUSINESS_UNIT'], props['APP_NAME']),
    props=props
)
props = version_control_stack.output_props

DeploymentPipelineStack(app, '{0}-{1}-deployment-pipeline'.format(props['BUSINESS_UNIT'], props['APP_NAME']), props=props
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

app.synth()
