Prereqs: 

Install Git, the AWS CDK and the AWS CLI:

https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html
https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html#getting_started_prerequisites
https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html#getting_started_install


Clone the orignal repository:

```
export APP_NAME='CorpPrefixLists'
export BUSINESS_UNIT='NET'
export REGION='us-west-2'
export ORIGINAL_URL_OF_THIS_REPOSITORY='https://github.com/walkerk1980/AWSCorpPrefixLists.git'
git clone $ORIGINAL_URL_OF_THIS_REPOSITORY corp_prefix_lists
cd corp_prefix_lists/
```

Use deployment_pipeline/codecommitrepo.yaml to deploy a Cloudformation Stack into your AWS Organization's Network Management Account:

```
aws --region ${REGION} cloudformation deploy --template-file deployment_pipeline/codecommit_repo.yaml \
--stack-name "${BUSINESS_UNIT}${APP_NAME}-codecommit-repo" \
--parameter-overrides "BusinessUnit=${BUSINESS_UNIT}" "AppName=${APP_NAME}" \
"RepoDescription=List of IP Ranges to be used in EC2 Security Groups" 
```

```
export NEW_ORIGIN_URL=$(aws --region ${REGION} cloudformation list-exports \
--query 'Exports[?Name==`'${BUSINESS_UNIT}-${APP_NAME}-git-http-url'`].Value' --output text)
git remote remove origin
git remote add origin "${NEW_ORIGIN_URL}.git"
git push --set-upstream origin main
git remote add upstream "${ORIGINAL_URL_OF_THIS_REPOSITORY}"
```

Set constants in cdk.context.json.

Change contents of yaml files in corp_prefix_lists/cidr_ranges/ as desired.

Update local repo:

```
git add .
git commit -m 'updated constants and prefix lists'
```

Install application dependencies:

```
source .venv/bin/activate >/dev/null 2>&1|| python3 -m venv .venv && source .venv/bin/activate
pip install --upgrade -r requirements.txt
```

Bootstrap your AWS Account/Regions

```
cdk bootstrap "aws://$(aws sts get-caller-identity --query Account --output text)/${REGION}"
```

Test with a synth and then deploy

```
cdk synth 
cdk deploy --all
```

# Welcome to your CDK Python project!

You should explore the contents of this project. It demonstrates a CDK app with an instance of a stack (`api_pipeline_stack`)
which contains an Amazon SQS queue that is subscribed to an Amazon SNS topic.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization process also creates
a virtualenv within this project, stored under the .venv directory.  To create the virtualenv
it assumes that there is a `python3` executable in your path with access to the `venv` package.
If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv
manually once the init process completes.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

You can now begin exploring the source code, contained in the hello directory.
There is also a very trivial test included that can be run like this:

```
$ pytest
```

To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
