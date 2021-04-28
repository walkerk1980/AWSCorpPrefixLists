Clone the orignal repository:

```
APP_NAME='CorpPrefixLists'
BUSINESS_UNIT='Networking'
URL_OF_THIS_REPOSITORY=''
git clone $URL_OF_THIS_REPOSITORY
cd corp_prefix_lists/
```

Use deployment_pipeline/codecommitrepo.yaml to deploy a Cloudformation Stack into your AWS Organization's Network Management Account.

Creds for AWS Account required for the commands below:

```
export ORIGIN_URL=$(aws cloudformation list-exports --query 'Exports[?Name==`${BUSINESS_UNIT}-${APP_NAME}-git-http-url`].Value' --output text)
git remote add origin "${ORIGIN_URL}.git"
```

Set constants in cdk.context.json

```
git add .
git commit -m 'inital code'
git push --set-upstream origin main
```

Run 'cdk bootstrap' in both PREPROD and PROD Accounts/Regions

```
cdk bootstrap
```

Install application dependencies

```
source .venv/bin/activate >/dev/null 2>&1|| python3 -m venv .venv && source .venv/bin/activate
pip install --upgrade -r requirements.txt
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
