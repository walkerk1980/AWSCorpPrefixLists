import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="corp_prefix_lists",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "corp_prefix_lists"},
    packages=setuptools.find_packages(where="corp_prefix_lists"),

    install_requires=[
        "aws-cdk.core",
        "aws-cdk.aws-events",
        "aws-cdk.aws-events-targets",
        "aws-cdk.aws-ec2",
        "aws-cdk.aws-ecs-patterns",
        "aws-cdk.aws_iam",
        "aws-cdk.aws_s3_assets",
        "aws-cdk.aws_secretsmanager",
        "aws-cdk.aws_codecommit",
        "aws-cdk.aws_codepipeline",
        "aws-cdk.aws_codepipeline-actions",
        "aws-cdk.pipelines"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
